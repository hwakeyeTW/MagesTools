#!/usr/bin/env python3
from pathlib import Path
import zipfile, hashlib, json, sys
EXPECTED_RELEASE="c221b13a5be3b4252c1c949818da6b7fee3f7604b8d72825b2a7e64ea7ca7cb9"
EXPECTED_META="1cabcacce4dde81a29b73a1363b92cdbad0d378fff1f866739a30545a75e1837"
PRESERVE={"EasyPatcher.exe": "75404cfe8aac6d1d69f4d7f8fa1a9ec03e746699184c538350d0ad7652fb315d", "EasyPatcher.exe.config": "f82338e8e9c746b5d95cd2ccc7bf94dd5de2b9b8982fffddf2118e475de50e15", "fastJSON.dll": "6ae4faf9c1e2eb4a9eead6843c56cba6d7ab77f0b6753aa8c3564d6562de143b", "MagesLib.dll": "e82996f2888998c2a43f4025b98c3b9990f9285162adc47f1139e5ddcda129e1", "berd/MDE.bmp": "855457b70e4c450b448c8589f2a6f221e05ba5b50fb3d22930cc5a610b510e72", "berd/script.json": "2fb7fa0b69d7fc9b6736698c1ca02eb4efa53aac502590e94b087c2582bb5978", "berd/system.json": "164c905ae2eddfb5bc026feac3f1735ad39deb8106aa3d469f377bb058bb01b2"}
if len(sys.argv)!=2:
    print("usage: validate_patchbuild_r2_v11.py RELEASE.zip")
    raise SystemExit(2)
p=Path(sys.argv[1]); errors=[]
b=p.read_bytes()
if hashlib.sha256(b).hexdigest()!=EXPECTED_RELEASE:
    errors.append("release sha mismatch")
with zipfile.ZipFile(p) as z:
    if z.testzip() is not None: errors.append("CRC failure")
    meta_b=z.read("berd/meta.json")
    if hashlib.sha256(meta_b).hexdigest()!=EXPECTED_META:
        errors.append("meta sha mismatch")
    meta=json.loads(meta_b.decode("utf-8"))
    notice=meta["notice"]
    if notice.count("\n")!=3:
        errors.append(f"actual LF count {notice.count(chr(10))} != 3")
    if "\\n" in notice:
        errors.append("literal backslash+n present after JSON parse")
    for stale in ("TEXT-FREEZE-GATE02","PLAYABLE-RC02","37 個 runtime-evidence obligations 仍待驗證"):
        if stale in notice:
            errors.append("stale notice: "+stale)
    for n,h in PRESERVE.items():
        if hashlib.sha256(z.read(n)).hexdigest()!=h:
            errors.append("preserve mismatch "+n)
print(json.dumps({"status":"PASS" if not errors else "FAIL","errors":errors},ensure_ascii=False,indent=2))
raise SystemExit(0 if not errors else 1)
