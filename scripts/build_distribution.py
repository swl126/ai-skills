#!/usr/bin/env python3
"""Build a deterministic minimal ai-skills-hub installation archive."""
from __future__ import annotations
import argparse,hashlib,json,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ROOT_FILES=("SKILL.md","VERSION","LICENSE","TRUST.md","embedded-skills.json")
def files():
    selected=[ROOT/x for x in ROOT_FILES]
    selected += [p for p in (ROOT/"skills").rglob("*") if p.is_file() and "__pycache__" not in p.parts]
    return sorted(selected,key=lambda p:p.relative_to(ROOT).as_posix())
def build(out:Path):
    entries=files();out.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
        for p in entries:
            info=zipfile.ZipInfo("ai-skills-hub/"+p.relative_to(ROOT).as_posix(),(1980,1,1,0,0,0));info.external_attr=0o644<<16
            z.writestr(info,p.read_bytes(),compress_type=zipfile.ZIP_DEFLATED)
    sha=hashlib.sha256(out.read_bytes()).hexdigest();out.with_suffix(out.suffix+".sha256").write_text(f"{sha}  {out.name}\n")
    return {"files":len(entries),"sha256":sha}
def main():
    p=argparse.ArgumentParser();p.add_argument("--out",type=Path,required=True);a=p.parse_args();r=build(a.out);print(json.dumps(r,sort_keys=True))
if __name__=="__main__":main()
