#!/usr/bin/env python3
"""Join CycloneDX components to an offline normalized advisory set and prioritize risk."""
from __future__ import annotations
import argparse,json
from pathlib import Path
RANK={"unknown":0,"low":1,"medium":2,"high":3,"critical":4}
def triage(sbom,advisories):
    by_purl={x.get("purl"):x for x in sbom.get("components",[]) if x.get("purl")};findings=[]
    for adv in advisories:
        purl=adv.get("purl")
        if purl not in by_purl:continue
        sev=str(adv.get("severity","unknown")).lower()
        findings.append({"advisory_id":adv["id"],"purl":purl,"severity":sev,"reachable":bool(adv.get("reachable",False)),"fix_version":adv.get("fix_version"),"priority":RANK.get(sev,0)+(2 if adv.get("reachable") else 0)+(1 if not adv.get("fix_version") else 0)})
    findings.sort(key=lambda x:(-x["priority"],x["advisory_id"]))
    block=any(RANK.get(x["severity"],0)>=4 and x["reachable"] for x in findings)
    return {"schema_version":"1.0.0","decision":"BLOCK" if block else ("REVIEW" if findings else "PASS"),"finding_count":len(findings),"findings":findings}
def main():
    p=argparse.ArgumentParser();p.add_argument("sbom",type=Path);p.add_argument("advisories",type=Path);p.add_argument("--out",type=Path,required=True);p.add_argument("--fail-on-block",action="store_true");a=p.parse_args()
    r=triage(json.loads(a.sbom.read_text()),json.loads(a.advisories.read_text()));a.out.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n");print(f"{r['decision']}: {r['finding_count']} matched advisories")
    if a.fail_on_block and r["decision"]=="BLOCK":raise SystemExit(1)
if __name__=="__main__":main()
