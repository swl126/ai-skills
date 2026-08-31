#!/usr/bin/env python3
"""Compare JSON OpenAPI contracts and report backward-incompatible removals."""
from __future__ import annotations
import argparse,json
from pathlib import Path
METHODS={"get","put","post","delete","patch","head","options","trace"}
def audit(old,new):
    findings=[]
    for path,old_item in old.get("paths",{}).items():
        new_item=new.get("paths",{}).get(path)
        if new_item is None: findings.append({"code":"PATH_REMOVED","location":path,"severity":"high"});continue
        for method,op in old_item.items():
            if method.lower() not in METHODS: continue
            if method not in new_item: findings.append({"code":"OPERATION_REMOVED","location":f"{method.upper()} {path}","severity":"high"});continue
            before={(p.get("in"),p.get("name")) for p in op.get("parameters",[]) if p.get("required")}
            after={(p.get("in"),p.get("name")) for p in new_item[method].get("parameters",[]) if p.get("required")}
            for param in sorted(after-before): findings.append({"code":"REQUIRED_PARAMETER_ADDED","location":f"{method.upper()} {path} {param[0]}:{param[1]}","severity":"high"})
            old_res=set(op.get("responses",{}));new_res=set(new_item[method].get("responses",{}))
            for status in sorted(old_res-new_res): findings.append({"code":"RESPONSE_REMOVED","location":f"{method.upper()} {path} {status}","severity":"medium"})
    old_s=old.get("components",{}).get("schemas",{});new_s=new.get("components",{}).get("schemas",{})
    for name,schema in old_s.items():
        if name not in new_s: findings.append({"code":"SCHEMA_REMOVED","location":name,"severity":"high"});continue
        removed=set(schema.get("properties",{}))-set(new_s[name].get("properties",{}))
        for field in sorted(removed): findings.append({"code":"PROPERTY_REMOVED","location":f"{name}.{field}","severity":"high"})
    return {"schema_version":"1.0.0","decision":"BLOCK" if any(x["severity"]=="high" for x in findings) else ("REVIEW" if findings else "PASS"),"finding_count":len(findings),"findings":findings}
def main():
    p=argparse.ArgumentParser();p.add_argument("baseline",type=Path);p.add_argument("candidate",type=Path);p.add_argument("--out",type=Path,required=True);p.add_argument("--fail-on-block",action="store_true");a=p.parse_args()
    r=audit(json.loads(a.baseline.read_text()),json.loads(a.candidate.read_text()));a.out.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n");print(f"{r['decision']}: {r['finding_count']} findings")
    if a.fail_on_block and r["decision"]=="BLOCK":raise SystemExit(1)
if __name__=="__main__":main()
