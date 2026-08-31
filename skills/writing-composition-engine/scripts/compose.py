#!/usr/bin/env python3
"""Compose evidence-traceable Markdown from a strict brief and audit Markdown drafts."""
from __future__ import annotations
import argparse,json,re
from collections import Counter
from pathlib import Path
ALLOWED={"$schema","schema_version","title","audience","purpose","genre","sections","sources"}
GENRES={"academic","technical","technical-memo","policy","proposal","executive"}
class ContractError(ValueError):pass
def nonempty(value,label):
    if not isinstance(value,str) or not value.strip():raise ContractError(f"{label} must be a non-empty string")
    return value.strip()
def validate_brief(data):
    if not isinstance(data,dict):raise ContractError("brief must be an object")
    unknown=set(data)-ALLOWED
    if unknown:raise ContractError("unknown brief fields: "+", ".join(sorted(unknown)))
    if data.get("schema_version")!="1.0.0":raise ContractError("schema_version must be 1.0.0")
    for key in ("title","audience","purpose"):nonempty(data.get(key),key)
    if data.get("genre") not in GENRES:raise ContractError("unsupported genre")
    sources=data.get("sources")
    if not isinstance(sources,list):raise ContractError("sources must be an array")
    ids=set()
    for i,s in enumerate(sources):
        if not isinstance(s,dict) or set(s)!={"id","citation","verified"}:raise ContractError(f"sources[{i}] fields are invalid")
        sid=nonempty(s["id"],f"sources[{i}].id")
        if sid in ids:raise ContractError(f"duplicate source id: {sid}")
        ids.add(sid);nonempty(s["citation"],f"sources[{i}].citation")
        if not isinstance(s["verified"],bool):raise ContractError(f"sources[{i}].verified must be boolean")
    sections=data.get("sections")
    if not isinstance(sections,list) or len(sections)<2:raise ContractError("at least two sections are required")
    headings=set()
    for i,s in enumerate(sections):
        if not isinstance(s,dict) or set(s)!={"heading","paragraphs","claims"}:raise ContractError(f"sections[{i}] fields are invalid")
        heading=nonempty(s["heading"],f"sections[{i}].heading")
        if heading.casefold() in headings:raise ContractError(f"duplicate section heading: {heading}")
        headings.add(heading.casefold())
        if not isinstance(s["paragraphs"],list) or not s["paragraphs"]:raise ContractError(f"sections[{i}].paragraphs must be non-empty")
        for j,p in enumerate(s["paragraphs"]):nonempty(p,f"sections[{i}].paragraphs[{j}]")
        if not isinstance(s["claims"],list):raise ContractError(f"sections[{i}].claims must be an array")
        for j,c in enumerate(s["claims"]):
            if not isinstance(c,dict) or set(c)!={"text","evidence_ids"}:raise ContractError(f"sections[{i}].claims[{j}] fields are invalid")
            nonempty(c["text"],f"sections[{i}].claims[{j}].text")
            refs=c["evidence_ids"]
            if not isinstance(refs,list) or not refs or not all(isinstance(x,str) and x for x in refs):raise ContractError("claim evidence_ids must be non-empty")
            missing=set(refs)-ids
            if missing:raise ContractError("claim references unknown evidence: "+", ".join(sorted(missing)))
    return data
def compose(data):
    validate_brief(data);lines=[f"# {data['title']}","",f"**Audience:** {data['audience']}  ",f"**Purpose:** {data['purpose']}  ",f"**Genre:** {data['genre']}",""]
    for section in data["sections"]:
        lines += [f"## {section['heading']}",""]
        for paragraph in section["paragraphs"]:lines += [paragraph.strip(),""]
        for claim in section["claims"]:
            cites=" ".join(f"[{x}]" for x in claim["evidence_ids"]);lines += [f"{claim['text'].strip()} {cites}",""]
    lines += ["## Sources",""]
    for source in data["sources"]:lines.append(f"- [{source['id']}] {source['citation']} — {'verified' if source['verified'] else 'unverified'}")
    return "\n".join(lines).rstrip()+"\n"
def audit(text):
    findings=[]
    if not re.search(r"^#\s+\S",text,re.M):findings.append({"code":"TITLE_MISSING","severity":"high","message":"A level-one title is required."})
    headings=re.findall(r"^##\s+(.+)$",text,re.M)
    substantive=[x for x in headings if x.strip().casefold()!="sources"]
    if len(substantive)<2:findings.append({"code":"SECTIONS_INSUFFICIENT","severity":"high","message":"At least two substantive sections are required."})
    if re.search(r"\b(?:TODO|TBD|FIXME|replace-with)\b",text,re.I):findings.append({"code":"UNFINISHED_MARKER","severity":"high","message":"The draft contains an unfinished marker."})
    registered=set(re.findall(r"^- \[([-A-Za-z0-9_.:]+)\]\s+.+$",text,re.M))
    prose=re.sub(r"^- \[[-A-Za-z0-9_.:]+\]\s+.+$","",text,flags=re.M)
    cited=set(re.findall(r"\[([A-Za-z][-A-Za-z0-9_.:]*\d[-A-Za-z0-9_.:]*)\]",prose))
    for ref in sorted(cited-registered):findings.append({"code":"CITATION_UNRESOLVED","severity":"high","message":f"Citation {ref} is not registered."})
    for ref in sorted(registered-cited):findings.append({"code":"SOURCE_UNUSED","severity":"medium","message":f"Source {ref} is registered but unused."})
    paragraphs=[p.strip() for p in re.split(r"\n\s*\n",text) if p.strip() and not p.lstrip().startswith(("#","- ","|","**"))]
    for i,p in enumerate(paragraphs,1):
        if len(re.findall(r"\b\w+\b",p))>180:findings.append({"code":"PARAGRAPH_LONG","severity":"medium","message":f"Paragraph {i} exceeds 180 words."})
    sentences=[re.sub(r"\s+"," ",x.strip()).casefold() for x in re.split(r"(?<=[.!?])\s+",text) if len(x.split())>=5]
    for sentence,count in Counter(sentences).items():
        if count>1:findings.append({"code":"SENTENCE_REPEATED","severity":"medium","message":"A substantive sentence is repeated."});break
    decision="BLOCK" if any(x["severity"]=="high" for x in findings) else ("REVIEW" if findings else "PASS")
    return {"schema_version":"1.0.0","decision":decision,"summary":{"finding_count":len(findings),"section_count":len(substantive),"registered_sources":len(registered),"cited_sources":len(cited)},"findings":findings}
def main():
    p=argparse.ArgumentParser();sub=p.add_subparsers(dest="command",required=True)
    c=sub.add_parser("compose");c.add_argument("--brief",type=Path,required=True);c.add_argument("--out",type=Path,required=True);c.add_argument("--audit",type=Path)
    a=sub.add_parser("audit");a.add_argument("--input",type=Path,required=True);a.add_argument("--out",type=Path,required=True);a.add_argument("--fail-on-block",action="store_true")
    args=p.parse_args()
    try:
        if args.command=="compose":
            draft=compose(json.loads(args.brief.read_text()));args.out.write_text(draft);result=audit(draft)
            if args.audit:args.audit.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
        else:
            result=audit(args.input.read_text());args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
        print(f"{result['decision']}: {result['summary']['finding_count']} findings")
        if getattr(args,"fail_on_block",False) and result["decision"]=="BLOCK":raise SystemExit(1)
    except (OSError,json.JSONDecodeError,ContractError) as exc:print(f"ERROR: {exc}");raise SystemExit(2)
if __name__=="__main__":main()
