#!/usr/bin/env python3
"""Create and verify integrity-bound local evidence envelopes."""
from __future__ import annotations
import argparse,hashlib,json,mimetypes
from datetime import datetime,timezone
from pathlib import Path

def digest(path:Path)->str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):h.update(chunk)
    return h.hexdigest()

def create(path:Path,target_id:str,target_version:str,environment:str,collector_id:str,collector_version:str,method:str)->dict:
    path=path.resolve()
    if not path.is_file():raise ValueError("artifact must be a regular file")
    return {"schema_version":"1.0.0","artifact":{"path":path.name,"sha256":digest(path),"size_bytes":path.stat().st_size,"media_type":mimetypes.guess_type(path.name)[0] or "application/octet-stream"},"target":{"id":target_id,"version":target_version,"environment":environment},"collector":{"id":collector_id,"version":collector_version,"method":method},"collected_at":datetime.now(timezone.utc).isoformat()}

def verify(envelope:dict,artifact:Path)->None:
    if set(envelope)!={"schema_version","artifact","target","collector","collected_at"}:raise ValueError("envelope fields are incomplete or unknown")
    if envelope["schema_version"]!="1.0.0":raise ValueError("unsupported schema version")
    art=envelope["artifact"]
    if art.get("path")!=artifact.name:raise ValueError("artifact name does not match envelope")
    if art.get("size_bytes")!=artifact.stat().st_size:raise ValueError("artifact size does not match envelope")
    if art.get("sha256")!=digest(artifact):raise ValueError("artifact SHA-256 does not match envelope")
    datetime.fromisoformat(envelope["collected_at"].replace("Z","+00:00"))
    for group,fields in (("target",("id","version","environment")),("collector",("id","version","method"))):
        if set(envelope.get(group,{}))!=set(fields) or not all(isinstance(envelope[group][x],str) and envelope[group][x] for x in fields):raise ValueError(f"{group} identity is incomplete")

def main():
    p=argparse.ArgumentParser();sub=p.add_subparsers(dest="command",required=True)
    c=sub.add_parser("create");c.add_argument("artifact",type=Path);c.add_argument("--target-id",required=True);c.add_argument("--target-version",required=True);c.add_argument("--environment",required=True);c.add_argument("--collector-id",required=True);c.add_argument("--collector-version",required=True);c.add_argument("--method",required=True);c.add_argument("--out",type=Path,required=True)
    v=sub.add_parser("verify");v.add_argument("envelope",type=Path);v.add_argument("artifact",type=Path)
    a=p.parse_args()
    try:
        if a.command=="create":a.out.write_text(json.dumps(create(a.artifact,a.target_id,a.target_version,a.environment,a.collector_id,a.collector_version,a.method),indent=2,sort_keys=True)+"\n");print(f"Evidence envelope created: {a.out}")
        else:verify(json.loads(a.envelope.read_text()),a.artifact);print("Evidence envelope verified")
    except (OSError,ValueError,json.JSONDecodeError) as exc:print(f"ERROR: {exc}");raise SystemExit(2)
if __name__=="__main__":main()
