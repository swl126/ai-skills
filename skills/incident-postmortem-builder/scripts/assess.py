#!/usr/bin/env python3
"""Dependency-free normalized-evidence assessment engine."""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA_VERSION="1.0.0"
ROOT=Path(__file__).resolve().parents[1]
PROFILE_PATH=ROOT/"references/engine-profile.json"
SEVERITY_ORDER={"low":1,"medium":2,"high":3,"critical":4}

class ContractError(ValueError): pass

def load_json(path:Path)->Any:
    try: return json.loads(path.read_text(encoding="utf-8"))
    except (OSError,json.JSONDecodeError) as exc: raise ContractError(f"cannot read JSON {path}: {exc}") from exc

def canonical_hash(value:Any)->str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def require_string(value:Any,label:str)->str:
    if not isinstance(value,str) or not value.strip(): raise ContractError(f"{label} must be a non-empty string")
    return value

def require_number(value:Any,label:str,minimum:float|None=None)->float:
    if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value): raise ContractError(f"{label} must be a finite number")
    number=float(value)
    if minimum is not None and number<minimum: raise ContractError(f"{label} must be >= {minimum}")
    return number

def reject_unknown(value:dict[str,Any],allowed:set[str],label:str)->None:
    unknown=sorted(set(value)-allowed)
    if unknown: raise ContractError(f"{label} contains unknown fields: {', '.join(unknown)}")

def validate_profile(profile:dict[str,Any])->dict[str,Any]:
    if not isinstance(profile,dict): raise ContractError("engine profile must be an object")
    reject_unknown(profile,{"schema_version","skill_id","title","max_evidence_age_days","required_categories","block_severities","review_severities","rules"},"engine profile")
    if profile.get("schema_version")!=SCHEMA_VERSION: raise ContractError(f"profile schema_version must be {SCHEMA_VERSION}")
    require_string(profile.get("skill_id"),"profile.skill_id"); require_string(profile.get("title"),"profile.title")
    require_number(profile.get("max_evidence_age_days"),"profile.max_evidence_age_days",0)
    categories=profile.get("required_categories")
    if not isinstance(categories,list) or not categories or not all(isinstance(x,str) and x for x in categories): raise ContractError("profile.required_categories must be a non-empty string array")
    if len(categories)!=len(set(categories)): raise ContractError("profile.required_categories contains duplicates")
    for field in ("block_severities","review_severities"):
        if not isinstance(profile.get(field),list) or not all(x in SEVERITY_ORDER for x in profile[field]): raise ContractError(f"profile.{field} contains invalid severity")
    rules=profile.get("rules")
    if not isinstance(rules,list) or not rules: raise ContractError("profile.rules must be a non-empty array")
    seen=set()
    for i,rule in enumerate(rules):
        if not isinstance(rule,dict): raise ContractError(f"profile.rules[{i}] must be an object")
        reject_unknown(rule,{"id","category","field","operator","expected","severity","message"},f"profile.rules[{i}]")
        rid=require_string(rule.get("id"),f"profile.rules[{i}].id")
        if rid in seen: raise ContractError(f"duplicate profile rule id: {rid}")
        seen.add(rid)
        if rule.get("category") not in categories: raise ContractError(f"profile.rules[{i}].category is not required")
        require_string(rule.get("field"),f"profile.rules[{i}].field")
        if rule.get("operator") not in {"equals","not_equals","min","max","one_of","none_of","present","contains_all"}: raise ContractError(f"profile.rules[{i}].operator is unsupported")
        if rule.get("severity") not in SEVERITY_ORDER: raise ContractError(f"profile.rules[{i}].severity is invalid")
        require_string(rule.get("message"),f"profile.rules[{i}].message")
    return profile

def validate_assessment(data:dict[str,Any],profile:dict[str,Any])->dict[str,Any]:
    if not isinstance(data,dict): raise ContractError("assessment must be an object")
    reject_unknown(data,{"$schema","schema_version","assessment_id","target","evidence","records","metadata"},"assessment")
    if data.get("schema_version")!=SCHEMA_VERSION: raise ContractError(f"assessment schema_version must be {SCHEMA_VERSION}")
    require_string(data.get("assessment_id"),"assessment_id")
    target=data.get("target")
    if not isinstance(target,dict): raise ContractError("target must be an object")
    reject_unknown(target,{"id","version","environment"},"target")
    for field in ("id","version","environment"): require_string(target.get(field),f"target.{field}")
    evidence=data.get("evidence")
    if not isinstance(evidence,list) or not evidence: raise ContractError("evidence must be a non-empty array")
    seen=set()
    for i,item in enumerate(evidence):
        if not isinstance(item,dict): raise ContractError(f"evidence[{i}] must be an object")
        reject_unknown(item,{"id","kind","source","age_days","verified","hash"},f"evidence[{i}]")
        eid=require_string(item.get("id"),f"evidence[{i}].id")
        if eid in seen: raise ContractError(f"duplicate evidence id: {eid}")
        seen.add(eid); require_string(item.get("kind"),f"evidence[{i}].kind"); require_string(item.get("source"),f"evidence[{i}].source")
        require_number(item.get("age_days"),f"evidence[{i}].age_days",0)
        if not isinstance(item.get("verified"),bool): raise ContractError(f"evidence[{i}].verified must be boolean")
        if "hash" in item: require_string(item["hash"],f"evidence[{i}].hash")
    records=data.get("records")
    if not isinstance(records,list) or not records: raise ContractError("records must be a non-empty array")
    seen=set(); allowed=set(profile["required_categories"])
    for i,record in enumerate(records):
        if not isinstance(record,dict): raise ContractError(f"records[{i}] must be an object")
        reject_unknown(record,{"id","category","severity","owner","evidence_ids","values","notes"},f"records[{i}]")
        rid=require_string(record.get("id"),f"records[{i}].id")
        if rid in seen: raise ContractError(f"duplicate record id: {rid}")
        seen.add(rid)
        if record.get("category") not in allowed: raise ContractError(f"records[{i}].category is not allowed by the profile")
        if record.get("severity") not in SEVERITY_ORDER: raise ContractError(f"records[{i}].severity is invalid")
        require_string(record.get("owner"),f"records[{i}].owner")
        refs=record.get("evidence_ids")
        if not isinstance(refs,list) or not refs or not all(isinstance(x,str) and x for x in refs): raise ContractError(f"records[{i}].evidence_ids must be a non-empty string array")
        if not isinstance(record.get("values"),dict): raise ContractError(f"records[{i}].values must be an object")
    return data

def field_value(values:dict[str,Any],path:str)->tuple[bool,Any]:
    current:Any=values
    for part in path.split("."):
        if not isinstance(current,dict) or part not in current: return False,None
        current=current[part]
    return True,current

def rule_passes(operator:str,actual:Any,expected:Any,present:bool)->bool:
    if operator=="present": return present and actual not in (None,"",[],{})
    if not present: return False
    if operator=="equals": return actual==expected
    if operator=="not_equals": return actual!=expected
    if operator in {"min","max"}:
        if isinstance(actual,bool) or not isinstance(actual,(int,float)): return False
        return actual>=expected if operator=="min" else actual<=expected
    if operator=="one_of": return isinstance(expected,list) and actual in expected
    if operator=="none_of": return isinstance(expected,list) and actual not in expected
    if operator=="contains_all": return isinstance(actual,list) and isinstance(expected,list) and set(expected).issubset(set(actual))
    raise ContractError(f"unsupported operator: {operator}")

def make_finding(code:str,severity:str,message:str,record_id:str|None=None,evidence_ids:list[str]|None=None)->dict[str,Any]:
    return {"code":code,"severity":severity,"message":message,"record_id":record_id,"evidence_ids":evidence_ids or []}

def assess(profile:dict[str,Any],data:dict[str,Any])->dict[str,Any]:
    validate_profile(profile); validate_assessment(data,profile)
    evidence={x["id"]:x for x in data["evidence"]}; by_category:dict[str,list[dict[str,Any]]]={}; findings=[]
    for record in data["records"]:
        by_category.setdefault(record["category"],[]).append(record)
        missing=sorted(set(record["evidence_ids"])-set(evidence))
        if missing: findings.append(make_finding("EVIDENCE-MISSING","critical",f"Missing evidence references: {', '.join(missing)}",record["id"],record["evidence_ids"]))
        for eid in record["evidence_ids"]:
            item=evidence.get(eid)
            if not item: continue
            if not item["verified"]: findings.append(make_finding("EVIDENCE-UNVERIFIED","high",f"Evidence {eid} is unverified",record["id"],[eid]))
            if item["age_days"]>profile["max_evidence_age_days"]: findings.append(make_finding("EVIDENCE-STALE","medium",f"Evidence {eid} exceeds the freshness window",record["id"],[eid]))
    for category in sorted(set(profile["required_categories"])-set(by_category)):
        findings.append(make_finding(f"COVERAGE-{category.upper()}","high",f"Required category is missing: {category}"))
    for rule in profile["rules"]:
        for record in by_category.get(rule["category"],[]):
            present,actual=field_value(record["values"],rule["field"])
            if not rule_passes(rule["operator"],actual,rule.get("expected"),present):
                severity=rule["severity"]
                if SEVERITY_ORDER[record["severity"]]>SEVERITY_ORDER[severity]: severity=record["severity"]
                findings.append(make_finding(rule["id"],severity,rule["message"],record["id"],record["evidence_ids"]))
    if any(x["severity"] in set(profile["block_severities"]) for x in findings): decision="BLOCK"
    elif any(x["severity"] in set(profile["review_severities"]) for x in findings): decision="REVIEW"
    else: decision="PASS"
    counts={name:sum(1 for x in findings if x["severity"]==name) for name in SEVERITY_ORDER}
    coverage={cat:len(by_category.get(cat,[])) for cat in profile["required_categories"]}
    return {"schema_version":SCHEMA_VERSION,"skill_id":profile["skill_id"],"assessment_id":data["assessment_id"],"target":data["target"],"generated_at":datetime.now(timezone.utc).isoformat(),"profile_sha256":canonical_hash(profile),"assessment_sha256":canonical_hash(data),"decision":decision,"summary":{"finding_count":len(findings),"severity_counts":counts,"coverage":coverage},"findings":findings}

def markdown(result:dict[str,Any])->str:
    lines=[f"# {result['skill_id']} assessment: {result['assessment_id']}","",f"- **Target:** {result['target']['id']} {result['target']['version']} ({result['target']['environment']})",f"- **Decision:** {result['decision']}",f"- **Findings:** {result['summary']['finding_count']}","","## Coverage","","| Category | Records |","| --- | ---: |"]
    lines.extend(f"| {name} | {count} |" for name,count in result["summary"]["coverage"].items())
    lines.extend(["","## Findings","","| Code | Severity | Record | Evidence | Message |","| --- | --- | --- | --- | --- |"])
    if result["findings"]:
        for item in result["findings"]: lines.append(f"| {item['code']} | {item['severity']} | {item['record_id'] or ''} | {', '.join(item['evidence_ids'])} | {item['message']} |")
    else: lines.append("| — | — | — | — | No findings |")
    lines.extend(["","## Integrity","",f"- Profile SHA-256: {result['profile_sha256']}",f"- Assessment SHA-256: {result['assessment_sha256']}"])
    return "\n".join(lines)+"\n"

def build_parser()->argparse.ArgumentParser:
    root=argparse.ArgumentParser(description=__doc__); sub=root.add_subparsers(dest="command",required=True)
    validate=sub.add_parser("validate"); validate.add_argument("--input",type=Path,required=True)
    run=sub.add_parser("assess"); run.add_argument("--input",type=Path,required=True); run.add_argument("--out",type=Path,required=True); run.add_argument("--report",type=Path); run.add_argument("--fail-on-block",action="store_true")
    return root

def main()->None:
    args=build_parser().parse_args()
    try:
        profile=validate_profile(load_json(PROFILE_PATH)); data=validate_assessment(load_json(args.input),profile)
        if args.command=="validate":
            print(f"Assessment contract valid: {data['assessment_id']} / {profile['skill_id']}"); return
        result=assess(profile,data); args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
        if args.report: args.report.write_text(markdown(result),encoding="utf-8")
        print(f"{result['decision']}: {result['assessment_id']} / {profile['skill_id']}")
        if args.fail_on_block and result["decision"]=="BLOCK": raise SystemExit(1)
    except ContractError as exc:
        print(f"ERROR: {exc}",file=sys.stderr); raise SystemExit(2) from exc

if __name__=="__main__": main()
