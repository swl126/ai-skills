#!/usr/bin/env python3
"""Scan authorized local files for likely secrets without printing secret values."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

PATTERNS = {
    "aws-access-key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "github-token": re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b"),
    "private-key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "credential-assignment": re.compile(r"(?i)\b(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"]([^'\"\s]{8,})"),
}
EXCLUDED = {".git", ".hg", ".svn", "node_modules", "__pycache__", ".venv", "venv"}

def fingerprint(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()[:16]

def scan(root: Path) -> dict:
    root = root.resolve(); findings=[]; scanned=0; skipped=0
    for path in sorted(root.rglob("*")):
        if not path.is_file() or any(part in EXCLUDED for part in path.parts):
            continue
        try:
            if path.stat().st_size > 2_000_000:
                skipped += 1; continue
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            skipped += 1; continue
        scanned += 1
        for line_no,line in enumerate(text.splitlines(),1):
            for kind,pattern in PATTERNS.items():
                for match in pattern.finditer(line):
                    value=match.group(1) if match.lastindex else match.group(0)
                    findings.append({"rule_id":kind,"path":path.relative_to(root).as_posix(),"line":line_no,"fingerprint":fingerprint(value),"redacted":True})
    return {"schema_version":"1.0.0","scanner":"secrets-hygiene-auditor","root":str(root),"files_scanned":scanned,"files_skipped":skipped,"finding_count":len(findings),"decision":"BLOCK" if findings else "PASS","findings":findings}

def main():
    p=argparse.ArgumentParser(); p.add_argument("root",type=Path); p.add_argument("--out",type=Path,required=True); p.add_argument("--fail-on-findings",action="store_true"); a=p.parse_args()
    result=scan(a.root); a.out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(f"{result['decision']}: {result['finding_count']} redacted findings across {result['files_scanned']} files")
    if a.fail_on_findings and result["findings"]: raise SystemExit(1)
if __name__=="__main__": main()
