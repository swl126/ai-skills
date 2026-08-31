#!/usr/bin/env python3
"""Statically inspect PostgreSQL DDL for missing or dangerously permissive RLS controls."""
from __future__ import annotations
import argparse,json,re
from pathlib import Path
IDENT=r'(?:"[^"]+"|[A-Za-z_][A-Za-z0-9_$]*)(?:\.(?:"[^"]+"|[A-Za-z_][A-Za-z0-9_$]*))?'
def norm(x):return x.replace('"','').lower()
def audit(sql):
    clean=re.sub(r"--.*?$|/\*.*?\*/","",sql,flags=re.M|re.S)
    tables={norm(x) for x in re.findall(rf"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?({IDENT})",clean,re.I)}
    enabled={norm(x) for x in re.findall(rf"ALTER\s+TABLE\s+({IDENT})\s+ENABLE\s+ROW\s+LEVEL\s+SECURITY",clean,re.I)}
    forced={norm(x) for x in re.findall(rf"ALTER\s+TABLE\s+({IDENT})\s+FORCE\s+ROW\s+LEVEL\s+SECURITY",clean,re.I)}
    policies={}
    for m in re.finditer(rf"CREATE\s+POLICY\s+\S+\s+ON\s+({IDENT})(.*?);",clean,re.I|re.S):
        policies.setdefault(norm(m.group(1)),[]).append(m.group(2))
    findings=[]
    for table in sorted(tables):
        if table not in enabled:findings.append({"code":"RLS_NOT_ENABLED","table":table,"severity":"critical"});continue
        if table not in policies:findings.append({"code":"POLICY_MISSING","table":table,"severity":"high"})
        if table not in forced:findings.append({"code":"RLS_NOT_FORCED","table":table,"severity":"medium"})
        for body in policies.get(table,[]):
            if re.search(r"USING\s*\(\s*true\s*\)",body,re.I):findings.append({"code":"PERMISSIVE_USING_TRUE","table":table,"severity":"high"})
            command=(re.search(r"FOR\s+(ALL|SELECT|INSERT|UPDATE|DELETE)",body,re.I) or [None,"ALL"])[1].upper()
            if command in {"ALL","INSERT","UPDATE"} and "WITH CHECK" not in body.upper():findings.append({"code":"WITH_CHECK_MISSING","table":table,"severity":"high"})
    return {"schema_version":"1.0.0","decision":"BLOCK" if any(x["severity"] in {"critical","high"} for x in findings) else ("REVIEW" if findings else "PASS"),"tables":len(tables),"finding_count":len(findings),"findings":findings}
def main():
    p=argparse.ArgumentParser();p.add_argument("sql",type=Path);p.add_argument("--out",type=Path,required=True);p.add_argument("--fail-on-block",action="store_true");a=p.parse_args();r=audit(a.sql.read_text());a.out.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n");print(f"{r['decision']}: {r['finding_count']} findings")
    if a.fail_on_block and r["decision"]=="BLOCK":raise SystemExit(1)
if __name__=="__main__":main()
