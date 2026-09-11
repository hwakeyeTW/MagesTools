# BR-V5 FONT v1.1 canonical maintenance implementation candidate

Classification: `NEW_CANONICAL_MAINTENANCE_IMPLEMENTATION_CANDIDATE`

This source tree is newly authored maintenance machinery for `BR-V5-MAINT-SRCFREEZE01-FONT-MACHINERY-REPAIR01`.
It is **not** recovered historical A02 source and must not be assigned the historical assembler identity
`dfda4be76c5cca42e838f8602bf7dcc32d2ac4b7d8afc8fbba9ab6cc56583e06`.

The builder implements FONT Runtime Build Spec v1.1 only:

- authenticate Runtime RC2, source font, exact toolchain capture and active captured toolchain bytes;
- decode each authenticated Runtime RC2 DDS mip0 with Pillow;
- build the v1.1 no-op control chain directly from mip0 with Pillow LANCZOS;
- clear/draw only combined slots 3754..3761 using `断浩彦榊瞇噘癒慷`, font size 46, offset (+1,-1);
- encode each mip independently with the exact captured ImageMagick DXT5 executable;
- assemble `baseline 128-byte header + 12 single-level BC3 payloads`;
- rebuild `system.json` by replacing only `data["FONT.DDS"]` and `data["FONT2.DDS"]`;
- compute exact precompression difference masks, affected BC3 block sets, structural/locality checks;
- perform two clean child-process builds and require byte-identical results.

## Invocation

Run under the restored captured Python executable, with the capture restored at its original absolute paths:

```text
/opt/pyvenv/bin/python font_maintenance_build.py \
  --runtime-rc2 <SteinsGate_MDE_TC_Patch_FinalText_RuntimeRC2.zip> \
  --source-font <GenYoGothic2TW-M.otf> \
  --toolchain-capture <BR-V5-MAINT-SRCFREEZE01-FONT-TOOLCHAIN-CAPTURE_v1_0.zip> \
  --magick /opt/imagemagick/bin/magick \
  --run-root <fresh-run-directory>
```

The accepted final DDS/system payloads are **not inputs**. Only their fixed expected SHA-256 identities are embedded as validation targets.
No network, package installation, fallback font, alternate compressor, dynamic atlas sizing, or PATH-only executable lookup is used.
