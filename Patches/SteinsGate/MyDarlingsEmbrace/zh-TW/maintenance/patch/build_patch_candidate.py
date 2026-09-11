#!/usr/bin/env python3
"""Repository-native deterministic packer for the accepted BR-V5 postfix milestone."""
from __future__ import annotations
import argparse, hashlib, json, pathlib, zipfile
EXPECTED={
 "EasyPatcher.exe":"75404cfe8aac6d1d69f4d7f8fa1a9ec03e746699184c538350d0ad7652fb315d",
 "EasyPatcher.exe.config":"f82338e8e9c746b5d95cd2ccc7bf94dd5de2b9b8982fffddf2118e475de50e15",
 "fastJSON.dll":"6ae4faf9c1e2eb4a9eead6843c56cba6d7ab77f0b6753aa8c3564d6562de143b",
 "MagesLib.dll":"e82996f2888998c2a43f4025b98c3b9990f9285162adc47f1139e5ddcda129e1",
 "berd/MDE.bmp":"855457b70e4c450b448c8589f2a6f221e05ba5b50fb3d22930cc5a610b510e72",
 "berd/meta.json":"1cabcacce4dde81a29b73a1363b92cdbad0d378fff1f866739a30545a75e1837",
 "berd/script.json":"ba565c667981168fa8b987fb5d40689461a3d7a87c635e6539a413870325b417",
 "berd/system.json":"164c905ae2eddfb5bc026feac3f1735ad39deb8106aa3d469f377bb058bb01b2"
}
TARGET_SHA="edbd65e66eb9e650be0cbe8a3763cd669eb7f1a15b0e7005148d993431a26219"
TARGET_BYTES=10418010
ORDER=["EasyPatcher.exe","EasyPatcher.exe.config","fastJSON.dll","MagesLib.dll","berd/MDE.bmp","berd/meta.json","berd/script.json","berd/system.json"]
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1024*1024),b''): h.update(c)
 return h.hexdigest()
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--tool-root',required=True,type=pathlib.Path,help='directory containing exact accepted EasyPatcher/MagesLib/fastJSON shell')
 ap.add_argument('--game-root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[2],help='zh-TW game root; defaults from this script location')
 ap.add_argument('--output',required=True,type=pathlib.Path)
 a=ap.parse_args(); T=a.tool_root.resolve(); G=a.game_root.resolve()
 paths={
  'EasyPatcher.exe':T/'EasyPatcher.exe','EasyPatcher.exe.config':T/'EasyPatcher.exe.config','fastJSON.dll':T/'fastJSON.dll','MagesLib.dll':T/'MagesLib.dll',
  'berd/MDE.bmp':G/'patch/berd/MDE.bmp','berd/meta.json':G/'patch/berd/meta.json','berd/script.json':G/'patch/berd/script.json','berd/system.json':G/'patch/berd/system.json'}
 for n,p in paths.items():
  if not p.is_file(): raise SystemExit(f'missing {n}: {p}')
  if sha(p)!=EXPECTED[n]: raise SystemExit(f'identity mismatch {n}: {sha(p)}')
 s=json.loads(paths['berd/script.json'].read_text(encoding='utf-8')); d=s.get('data')
 if s.get('type')!='scx' or s.get('file')!='script.mpk' or not isinstance(d,dict): raise SystemExit('script header mismatch')
 if len(d)!=78 or sum(len(v) for v in d.values())!=21512 or sum(1 for v in d.values() for x in v if x is None)!=72: raise SystemExit('script structural mismatch')
 if len(d.get('_TIPS.SCX',[]))!=924 or len(d.get('_SYSTEM.SCX',[]))!=209: raise SystemExit('TIPS/SYSTEM cardinality mismatch')
 a.output.parent.mkdir(parents=True,exist_ok=True)
 if a.output.exists(): a.output.unlink()
 with zipfile.ZipFile(a.output,'w',compression=zipfile.ZIP_STORED) as z:
  for n in ORDER:
   i=zipfile.ZipInfo(n,(1980,1,1,0,0,0)); i.compress_type=zipfile.ZIP_STORED; i.create_system=3; i.external_attr=0x01A40000; z.writestr(i,paths[n].read_bytes())
 actual=sha(a.output); size=a.output.stat().st_size; status='PASS' if actual==TARGET_SHA and size==TARGET_BYTES else 'FAIL'
 print(json.dumps({'status':status,'sha256':actual,'bytes':size,'expected_sha256':TARGET_SHA,'expected_bytes':TARGET_BYTES},indent=2))
 raise SystemExit(0 if status=='PASS' else 2)
if __name__=='__main__': main()
