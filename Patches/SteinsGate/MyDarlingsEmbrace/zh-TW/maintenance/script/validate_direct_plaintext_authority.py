#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, pathlib

EXPECTED_SHA = "ba565c667981168fa8b987fb5d40689461a3d7a87c635e6539a413870325b417"
EXPECTED_BYTES = 2028270

def sha_file(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for c in iter(lambda:f.read(1024*1024),b""):
            h.update(c)
    return h.hexdigest()

ap=argparse.ArgumentParser()
ap.add_argument("script_json", type=pathlib.Path)
args=ap.parse_args()
p=args.script_json
obj=json.loads(p.read_text(encoding="utf-8"))
data=obj.get("data")
rec={
    "sha256": sha_file(p),
    "bytes": p.stat().st_size,
    "type": obj.get("type"),
    "file": obj.get("file"),
    "scx_keys": len(data) if isinstance(data,dict) else None,
    "transforms": sum(len(v) for v in data.values()) if isinstance(data,dict) else None,
    "nulls": sum(1 for v in data.values() for x in v if x is None) if isinstance(data,dict) else None,
    "_TIPS.SCX": len(data.get("_TIPS.SCX",[])) if isinstance(data,dict) else None,
    "_SYSTEM.SCX": len(data.get("_SYSTEM.SCX",[])) if isinstance(data,dict) else None,
}
expected={
    "sha256": EXPECTED_SHA, "bytes": EXPECTED_BYTES, "type":"scx", "file":"script.mpk",
    "scx_keys":78, "transforms":21512, "nulls":72, "_TIPS.SCX":924, "_SYSTEM.SCX":209
}
rec["status"]="PASS" if all(rec[k]==v for k,v in expected.items()) else "FAIL"
print(json.dumps(rec,ensure_ascii=False,indent=2))
raise SystemExit(0 if rec["status"]=="PASS" else 2)
