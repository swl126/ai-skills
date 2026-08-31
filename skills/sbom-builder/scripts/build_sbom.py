#!/usr/bin/env python3
"""Build a deterministic CycloneDX 1.5 JSON SBOM from common lock and manifest files."""
from __future__ import annotations
import argparse,hashlib,json,re
from pathlib import Path

def component(ecosystem,name,version,scope="required"):
    purl=f"pkg:{ecosystem}/{name}@{version}"
    return {"type":"library","name":name,"version":version,"scope":scope,"purl":purl,"bom-ref":purl}

def parse(root:Path):
    found={}
    req=root/"requirements.txt"
    if req.is_file():
        for raw in req.read_text().splitlines():
            line=raw.strip()
            if not line or line.startswith("#"): continue
            m=re.fullmatch(r"([A-Za-z0-9_.-]+)==([^\s;]+)",line)
            if m: found[("pypi",m.group(1).lower(),m.group(2))]=component("pypi",m.group(1),m.group(2))
    lock=root/"package-lock.json"
    if lock.is_file():
        data=json.loads(lock.read_text())
        for path,item in data.get("packages",{}).items():
            if not path or "version" not in item: continue
            name=item.get("name") or path.rsplit("node_modules/",1)[-1]
            scope="optional" if item.get("dev") else "required"
            found[("npm",name,item["version"])]=component("npm",name,item["version"],scope)
    cargo=root/"Cargo.lock"
    if cargo.is_file():
        name=version=None
        for line in cargo.read_text().splitlines()+["[[package]]"]:
            if line=="[[package]]":
                if name and version: found[("cargo",name,version)]=component("cargo",name,version)
                name=version=None
            elif line.startswith("name = "): name=line.split('"',2)[1]
            elif line.startswith("version = "): version=line.split('"',2)[1]
    return sorted(found.values(),key=lambda x:x["purl"])

def build(root:Path,name:str,version:str):
    comps=parse(root); serial=hashlib.sha256(json.dumps(comps,sort_keys=True).encode()).hexdigest()
    return {"bomFormat":"CycloneDX","specVersion":"1.5","serialNumber":f"urn:uuid:{serial[:8]}-{serial[8:12]}-{serial[12:16]}-{serial[16:20]}-{serial[20:32]}","version":1,"metadata":{"component":{"type":"application","name":name,"version":version}},"components":comps}
def main():
    p=argparse.ArgumentParser();p.add_argument("root",type=Path);p.add_argument("--name",required=True);p.add_argument("--version",required=True);p.add_argument("--out",type=Path,required=True);a=p.parse_args()
    result=build(a.root,a.name,a.version);a.out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n");print(f"SBOM components: {len(result['components'])}")
if __name__=="__main__":main()
