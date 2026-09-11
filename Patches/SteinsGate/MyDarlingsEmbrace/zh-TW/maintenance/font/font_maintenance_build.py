#!/opt/pyvenv/bin/python
# NEW_CANONICAL_MAINTENANCE_IMPLEMENTATION_CANDIDATE
# BR-V5-MAINT-SRCFREEZE01-FONT-MACHINERY-REPAIR01
# This is newly authored maintenance machinery. It is NOT recovered historical A02 source.

from __future__ import annotations

import argparse
import base64
import copy
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import shutil
import struct
import subprocess
import sys
import zipfile

from PIL import Image, ImageChops, ImageDraw, ImageFont, features

CLASSIFICATION = "NEW_CANONICAL_MAINTENANCE_IMPLEMENTATION_CANDIDATE"
TASK = "BR-V5-MAINT-SRCFREEZE01-FONT-MACHINERY-REPAIR01"
HISTORICAL_ASSEMBLER_SHA256 = "dfda4be76c5cca42e838f8602bf7dcc32d2ac4b7d8afc8fbba9ab6cc56583e06"

EXPECTED = {
    "runtime_rc2": "e91444df1f1ecef8279517d69c78bbe0dffbe49dff32098dd5d058c4a59e7575",
    "baseline_system": "3c060db19107e12a2762a06e7a87f87b6849ad86142237e8f19e64cedad0c2a8",
    "baseline": {
        "FONT.DDS": "a52f194ec757f415138564137a2872898ab6ac3fcad91bc3d50eecafd9098421",
        "FONT2.DDS": "5e4e11016ca5f325953581ce4e6d8cef7a7f30237a265d1838bebc66ed7e6dbe",
    },
    "source_font": "7f0b3856b79bb254c0deabad6fac9ae8fe00c8bef3c2330ec74efa142473c21a",
    "source_font_bytes": 10726468,
    "toolchain_capture": "3b30c76c15b6e2ce2112219641030e5b087894752347fd7be6215f614484113a",
    "python": "17b78e0a93175e86f9ac03141924fd7a7f0c0c52e66b34bfa0de20ffef989df1",
    "magick": "108c178f9f6646913add77751d3f1b865e4e069cbe10573f278c52c4ce3ec6c3",
    "noop": {
        "FONT.DDS": "c30bec1744455112dbdd2d33322fa5e618dcf92ac2d93fa099d6fbd810077996",
        "FONT2.DDS": "575c268ca61f7885e428938d19e4ab193bf1b20fae154ffdc0ea44fb4b9d688c",
    },
    "current": {
        "FONT.DDS": "784aebbca02b0ba740edc7f0fa1e5830671219c961a56387f57ffd1077f5f8f1",
        "FONT2.DDS": "f1230bc4375cc6b8825e8bffb0d61434fdb96628dc63c49003a8bf4259ba760b",
        "system.json": "164c905ae2eddfb5bc026feac3f1735ad39deb8106aa3d469f377bb058bb01b2",
    },
}

WIDTH = 3072
HEIGHT = 2832
CELL = 48
COLUMNS = 64
ROWS = 59
SLOTS = 3776
MIP_COUNT = 12
DDS_HEADER_BYTES = 128
DDS_BYTES = 11601392
AUTHORIZED_SLOTS = tuple(range(3754, 3762))
HEADROOM_SLOTS = tuple(range(3762, 3776))
CHARS = "断浩彦榊瞇噘癒慷"
FONT_SIZE = 46
DRAW_OFFSET = (1, -1)
CLEAR = (255, 255, 255, 0)
FILL = (255, 255, 255, 255)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def mip_dimensions(level: int) -> tuple[int, int]:
    return max(1, WIDTH >> level), max(1, HEIGHT >> level)


def bc3_payload_size(w: int, h: int) -> int:
    return ((w + 3) // 4) * ((h + 3) // 4) * 16


def expected_payload_sizes() -> list[int]:
    return [bc3_payload_size(*mip_dimensions(i)) for i in range(MIP_COUNT)]


def parse_dds(data: bytes, *, expected_w: int | None = None, expected_h: int | None = None,
              expected_mips: int | None = None, expected_total: int | None = None) -> dict:
    errors: list[str] = []
    if len(data) < DDS_HEADER_BYTES:
        return {"errors": ["too_short"], "bytes": len(data)}
    if data[:4] != b"DDS ":
        errors.append("magic")
    header_size = struct.unpack_from("<I", data, 4)[0]
    height = struct.unpack_from("<I", data, 12)[0]
    width = struct.unpack_from("<I", data, 16)[0]
    mip_count = struct.unpack_from("<I", data, 28)[0]
    pf_size = struct.unpack_from("<I", data, 76)[0]
    fourcc = data[84:88]
    if header_size != 124:
        errors.append("header_size")
    if pf_size != 32:
        errors.append("pixel_format_size")
    if fourcc != b"DXT5":
        errors.append("fourcc")
    if expected_w is not None and width != expected_w:
        errors.append("width")
    if expected_h is not None and height != expected_h:
        errors.append("height")
    if expected_mips is not None and mip_count != expected_mips:
        errors.append("mip_count")
    if expected_total is not None and len(data) != expected_total:
        errors.append("total_bytes")
    return {
        "bytes": len(data),
        "sha256": sha256_bytes(data),
        "header_sha256": sha256_bytes(data[:DDS_HEADER_BYTES]),
        "width": width,
        "height": height,
        "mip_count": mip_count,
        "fourcc": fourcc.decode("ascii", errors="replace"),
        "errors": errors,
    }


def decode_embedded_resource(encoded: str) -> bytes:
    return gzip.decompress(base64.b64decode(encoded))


def encode_embedded_resource(data: bytes) -> str:
    return base64.b64encode(gzip.compress(data, compresslevel=9, mtime=0)).decode("ascii")


def active_capture_binding(capture_zip: Path) -> dict:
    actual_capture_sha = sha256_path(capture_zip)
    if actual_capture_sha != EXPECTED["toolchain_capture"]:
        raise RuntimeError("toolchain capture identity mismatch")
    with zipfile.ZipFile(capture_zip) as z:
        bad = z.testzip()
        if bad is not None:
            raise RuntimeError(f"toolchain capture CRC failure: {bad}")
        manifest = json.loads(z.read("metadata/TOOLCHAIN_FILE_MANIFEST.json"))
    missing = []
    content_mismatch = []
    type_mismatch = []
    verified = 0
    for item in manifest["items"]:
        p = Path(item["original_path"])
        if not p.exists() and not p.is_symlink():
            missing.append(item["original_path"])
            continue
        if item["file_type"] == "symlink" and not p.is_symlink():
            type_mismatch.append(item["original_path"])
        try:
            target = Path(os.path.realpath(p))
            size = target.stat().st_size
            h = sha256_path(target)
        except Exception as exc:
            content_mismatch.append({"path": item["original_path"], "error": repr(exc)})
            continue
        if size != item["bytes"] or h != item["sha256"]:
            content_mismatch.append({
                "path": item["original_path"],
                "actual_bytes": size,
                "expected_bytes": item["bytes"],
                "actual_sha256": h,
                "expected_sha256": item["sha256"],
            })
        else:
            verified += 1
    status = "PASS" if not (missing or content_mismatch or type_mismatch) else "FAIL"
    return {
        "status": status,
        "capture_sha256": actual_capture_sha,
        "manifest_entries": len(manifest["items"]),
        "manifest_entries_verified": verified,
        "missing": missing,
        "content_mismatch": content_mismatch,
        "type_mismatch": type_mismatch,
        "active_layout": "original_absolute_paths",
    }


def verify_anchor_toolchain(magick: Path) -> dict:
    python_path = Path(sys.executable)
    python_sha = sha256_path(python_path)
    magick_sha = sha256_path(magick)
    proc = subprocess.run([str(magick), "-version"], check=True, capture_output=True, text=True)
    version_output = proc.stdout
    out = {
        "python": {
            "path": str(python_path),
            "sha256": python_sha,
            "version": sys.version,
            "expected_sha256": EXPECTED["python"],
            "expected_version_prefix": "3.13.5",
        },
        "pillow": {
            "version": Image.__version__,
            "expected_version": "12.3.0",
        },
        "freetype": {
            "version": features.version("freetype2"),
            "expected_version": "2.14.3",
        },
        "imagemagick": {
            "path": str(magick),
            "sha256": magick_sha,
            "expected_sha256": EXPECTED["magick"],
            "version_output": version_output,
            "expected_family": "ImageMagick 7.1.2-1",
        },
    }
    ok = (
        python_sha == EXPECTED["python"]
        and sys.version.startswith("3.13.5")
        and Image.__version__ == "12.3.0"
        and features.version("freetype2") == "2.14.3"
        and magick_sha == EXPECTED["magick"]
        and "ImageMagick 7.1.2-1" in version_output
    )
    out["status"] = "PASS" if ok else "FAIL"
    if not ok:
        raise RuntimeError("captured toolchain anchor mismatch")
    return out


def authenticate_inputs(runtime_rc2: Path, source_font: Path) -> tuple[dict, bytes, dict[str, bytes]]:
    errors: list[str] = []
    runtime_sha = sha256_path(runtime_rc2)
    font_sha = sha256_path(source_font)
    font_bytes = source_font.stat().st_size
    if runtime_sha != EXPECTED["runtime_rc2"]:
        errors.append("Runtime RC2 SHA-256 mismatch")
    if font_sha != EXPECTED["source_font"] or font_bytes != EXPECTED["source_font_bytes"]:
        errors.append("source font identity mismatch")
    baseline_system = b""
    baselines: dict[str, bytes] = {}
    with zipfile.ZipFile(runtime_rc2) as z:
        bad = z.testzip()
        if bad is not None:
            errors.append(f"Runtime RC2 CRC failure: {bad}")
        baseline_system = z.read("berd/system.json")
    if sha256_bytes(baseline_system) != EXPECTED["baseline_system"]:
        errors.append("baseline system.json mismatch")
    system_obj = json.loads(baseline_system)
    for name in ("FONT.DDS", "FONT2.DDS"):
        data = decode_embedded_resource(system_obj["data"][name])
        baselines[name] = data
        if sha256_bytes(data) != EXPECTED["baseline"][name]:
            errors.append(f"baseline {name} mismatch")
        dds = parse_dds(data, expected_w=WIDTH, expected_h=HEIGHT, expected_mips=MIP_COUNT, expected_total=DDS_BYTES)
        if dds["errors"]:
            errors.append(f"baseline {name} structural errors: {dds['errors']}")
    result = {
        "status": "PASS" if not errors else "FAIL",
        "runtime_rc2": {"path": str(runtime_rc2), "sha256": runtime_sha},
        "source_font": {"path": str(source_font), "sha256": font_sha, "bytes": font_bytes},
        "baseline_system_json": {"sha256": sha256_bytes(baseline_system), "bytes": len(baseline_system)},
        "baseline_resources": {
            name: {"sha256": sha256_bytes(data), "bytes": len(data), "header_sha256": sha256_bytes(data[:DDS_HEADER_BYTES])}
            for name, data in baselines.items()
        },
        "target_payload_bytes_present_as_inputs": False,
        "errors": errors,
    }
    if errors:
        raise RuntimeError("; ".join(errors))
    return result, baseline_system, baselines


def edit_base(base: Image.Image, source_font: Path) -> tuple[Image.Image, dict]:
    edited = base.copy()
    draw = ImageDraw.Draw(edited)
    font = ImageFont.truetype(str(source_font), FONT_SIZE)
    glyph_rows = []
    for ch, slot in zip(CHARS, AUTHORIZED_SLOTS):
        x = (slot % COLUMNS) * CELL
        y = (slot // COLUMNS) * CELL
        local_bbox = ImageDraw.Draw(Image.new("RGBA", (CELL, CELL), CLEAR)).textbbox(DRAW_OFFSET, ch, font=font)
        bounded = local_bbox[0] >= 0 and local_bbox[1] >= 0 and local_bbox[2] <= CELL and local_bbox[3] <= CELL
        draw.rectangle((x, y, x + CELL - 1, y + CELL - 1), fill=CLEAR)
        draw.text((x + DRAW_OFFSET[0], y + DRAW_OFFSET[1]), ch, font=font, fill=FILL)
        alpha_bbox = edited.crop((x, y, x + CELL, y + CELL)).getchannel("A").getbbox()
        glyph_rows.append({
            "character": ch,
            "combined_slot": slot,
            "row": slot // COLUMNS,
            "column": slot % COLUMNS,
            "pixel_x": x,
            "pixel_y": y,
            "textbbox_local": list(local_bbox),
            "draw_cell_bounded": bounded,
            "alpha_bbox_local": list(alpha_bbox) if alpha_bbox else None,
            "nonblank": alpha_bbox is not None,
        })
    return edited, {"glyphs": glyph_rows}


def exact_diff_mask(noop: Image.Image, current: Image.Image) -> dict:
    if noop.size != current.size:
        raise RuntimeError("diff image size mismatch")
    diff = ImageChops.difference(noop, current)
    bbox = diff.getbbox()
    w, h = noop.size
    if bbox is None:
        spans: list[list[int]] = []
        affected: set[int] = set()
        count = 0
    else:
        x0, y0, x1, y1 = bbox
        crop = diff.crop(bbox)
        raw = crop.tobytes()
        cw = x1 - x0
        spans = []
        affected = set()
        count = 0
        for ry in range(y1 - y0):
            y = y0 + ry
            run_start = None
            for rx in range(cw):
                off = (ry * cw + rx) * 4
                changed = raw[off] or raw[off + 1] or raw[off + 2] or raw[off + 3]
                x = x0 + rx
                if changed:
                    count += 1
                    affected.add((y // 4) * ((w + 3) // 4) + (x // 4))
                    if run_start is None:
                        run_start = x
                elif run_start is not None:
                    spans.append([y, run_start, x])
                    run_start = None
            if run_start is not None:
                spans.append([y, run_start, x1])
    canonical = json.dumps({"size": [w, h], "spans": spans}, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return {
        "width": w,
        "height": h,
        "difference_pixels": count,
        "difference_bbox": list(bbox) if bbox else None,
        "mask_spans": spans,
        "mask_sha256": sha256_bytes(canonical),
        "affected_bc3_block_indices": sorted(affected),
        "affected_bc3_block_count": len(affected),
    }


def validate_base_locality(base: Image.Image, edited: Image.Image, edit_meta: dict) -> dict:
    mask = exact_diff_mask(base, edited)
    outside = 0
    for y, x0, x1 in mask["mask_spans"]:
        for x in range(x0, x1):
            slot = (y // CELL) * COLUMNS + (x // CELL)
            if slot not in AUTHORIZED_SLOTS:
                outside += 1
    headroom = []
    for slot in HEADROOM_SLOTS:
        x = (slot % COLUMNS) * CELL
        y = (slot // COLUMNS) * CELL
        raw = edited.crop((x, y, x + CELL, y + CELL)).tobytes()
        expected = bytes(CLEAR) * (CELL * CELL)
        headroom.append({"slot": slot, "transparent_white_blank": raw == expected})
    glyphs = edit_meta["glyphs"]
    ok = outside == 0 and all(g["nonblank"] and g["draw_cell_bounded"] for g in glyphs) and all(x["transparent_white_blank"] for x in headroom)
    return {
        "status": "PASS" if ok else "FAIL",
        "authorized_slots": list(AUTHORIZED_SLOTS),
        "outside_authorized_pixel_differences": outside,
        "inside_authorized_pixel_differences": mask["difference_pixels"],
        "base_mask": mask,
        "glyphs": glyphs,
        "headroom": headroom,
    }


def encode_single_mip(image: Image.Image, *, magick: Path, temp_dir: Path, stem: str, level: int) -> tuple[bytes, dict]:
    w, h = image.size
    png = temp_dir / f"{stem}.mip{level}.png"
    dds = temp_dir / f"{stem}.mip{level}.dds"
    image.save(png, format="PNG")
    cmd = [str(magick), str(png), "-define", "dds:compression=dxt5", str(dds)]
    proc = subprocess.run(cmd, check=True, capture_output=True, text=True)
    data = dds.read_bytes()
    parsed = parse_dds(data, expected_w=w, expected_h=h, expected_mips=1, expected_total=128 + bc3_payload_size(w, h))
    if parsed["errors"]:
        raise RuntimeError(f"temporary DDS structural error {stem} mip{level}: {parsed['errors']}")
    payload = data[DDS_HEADER_BYTES:]
    meta = {
        "level": level,
        "width": w,
        "height": h,
        "command": cmd,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
        "temporary_dds": parsed,
        "payload_bytes": len(payload),
        "payload_sha256": sha256_bytes(payload),
    }
    png.unlink()
    dds.unlink()
    return payload, meta


def build_resource(name: str, baseline_dds: bytes, source_font: Path, magick: Path, work_dir: Path) -> dict:
    temp_dir = work_dir / "temp" / name.replace(".", "_")
    temp_dir.mkdir(parents=True, exist_ok=True)
    baseline_info = parse_dds(baseline_dds, expected_w=WIDTH, expected_h=HEIGHT, expected_mips=MIP_COUNT, expected_total=DDS_BYTES)
    if baseline_info["errors"]:
        raise RuntimeError(f"baseline DDS invalid: {name}")
    base = Image.open(io.BytesIO(baseline_dds)).convert("RGBA")
    if base.size != (WIDTH, HEIGHT):
        raise RuntimeError("decoded mip0 geometry mismatch")
    edited, edit_meta = edit_base(base, source_font)
    base_locality = validate_base_locality(base, edited, edit_meta)
    if base_locality["status"] != "PASS":
        raise RuntimeError(f"base locality failure: {name}")

    noop_payloads = []
    current_payloads = []
    mip_masks = []
    bc3_locality = []
    encode_meta = []
    for level in range(MIP_COUNT):
        dims = mip_dimensions(level)
        noop_mip = base if level == 0 else base.resize(dims, Image.Resampling.LANCZOS)
        current_mip = edited if level == 0 else edited.resize(dims, Image.Resampling.LANCZOS)
        mask = exact_diff_mask(noop_mip, current_mip)
        no_payload, no_meta = encode_single_mip(noop_mip, magick=magick, temp_dir=temp_dir, stem="noop", level=level)
        cur_payload, cur_meta = encode_single_mip(current_mip, magick=magick, temp_dir=temp_dir, stem="current", level=level)
        noop_payloads.append(no_payload)
        current_payloads.append(cur_payload)
        changed_blocks = []
        for i in range(len(no_payload) // 16):
            lo = i * 16
            if no_payload[lo:lo + 16] != cur_payload[lo:lo + 16]:
                changed_blocks.append(i)
        affected_set = set(mask["affected_bc3_block_indices"])
        unexpected = [i for i in changed_blocks if i not in affected_set]
        locality_row = {
            "resource": name,
            "level": level,
            "width": dims[0],
            "height": dims[1],
            "affected_block_count": len(affected_set),
            "affected_block_indices": mask["affected_bc3_block_indices"],
            "changed_compressed_block_count": len(changed_blocks),
            "changed_compressed_block_indices": changed_blocks,
            "unexpected_changed_block_indices": unexpected,
            "outside_affected_blocks_byte_identical": len(unexpected) == 0,
        }
        if unexpected:
            raise RuntimeError(f"BC3 locality failure: {name} mip{level}")
        mask_row = {"resource": name, "level": level, **mask}
        mip_masks.append(mask_row)
        bc3_locality.append(locality_row)
        encode_meta.append({"resource": name, "variant": "noop", **no_meta})
        encode_meta.append({"resource": name, "variant": "current", **cur_meta})

    header = baseline_dds[:DDS_HEADER_BYTES]
    noop_dds = header + b"".join(noop_payloads)
    current_dds = header + b"".join(current_payloads)
    noop_info = parse_dds(noop_dds, expected_w=WIDTH, expected_h=HEIGHT, expected_mips=MIP_COUNT, expected_total=DDS_BYTES)
    current_info = parse_dds(current_dds, expected_w=WIDTH, expected_h=HEIGHT, expected_mips=MIP_COUNT, expected_total=DDS_BYTES)
    noop_info["header_exact_to_baseline"] = noop_dds[:DDS_HEADER_BYTES] == header
    current_info["header_exact_to_baseline"] = current_dds[:DDS_HEADER_BYTES] == header
    noop_info["expected_sha256"] = EXPECTED["noop"][name]
    current_info["expected_sha256"] = EXPECTED["current"][name]
    noop_info["identity_match"] = noop_info["sha256"] == EXPECTED["noop"][name]
    current_info["identity_match"] = current_info["sha256"] == EXPECTED["current"][name]
    if noop_info["errors"] or not noop_info["identity_match"]:
        raise RuntimeError(f"BLOCKED_V11_TOOLCHAIN_CONTROL_MISMATCH: {name}")
    if current_info["errors"] or not current_info["identity_match"]:
        raise RuntimeError(f"BLOCKED_FINAL_DDS_IDENTITY_MISMATCH: {name}")

    out_dir = work_dir / "outputs"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"noop_{name}").write_bytes(noop_dds)
    (out_dir / name).write_bytes(current_dds)
    return {
        "resource": name,
        "baseline": baseline_info,
        "base_locality": base_locality,
        "mip_masks": mip_masks,
        "bc3_locality": bc3_locality,
        "encode_meta": encode_meta,
        "noop": noop_info,
        "current": current_info,
        "payload_sizes": [len(x) for x in current_payloads],
    }


def build_system_json(baseline_system: bytes, current_resources: dict[str, bytes], out_path: Path) -> dict:
    base = json.loads(baseline_system)
    out = copy.deepcopy(base)
    for name in ("FONT.DDS", "FONT2.DDS"):
        out["data"][name] = encode_embedded_resource(current_resources[name])
    out_bytes = (json.dumps(out, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    out_path.write_bytes(out_bytes)

    bcmp = copy.deepcopy(base)
    ocmp = copy.deepcopy(out)
    for name in ("FONT.DDS", "FONT2.DDS"):
        bcmp["data"][name] = "<FONT>"
        ocmp["data"][name] = "<FONT>"
    resources = {}
    for name in ("FONT.DDS", "FONT2.DDS"):
        decoded = decode_embedded_resource(out["data"][name])
        reencoded = encode_embedded_resource(decoded)
        resources[name] = {
            "decoded_sha256": sha256_bytes(decoded),
            "matches_generated_dds": decoded == current_resources[name],
            "roundtrip_base64_gzip_exact": reencoded == out["data"][name],
            "encoded_chars": len(out["data"][name]),
        }
    result = {
        "baseline_system_sha256": sha256_bytes(baseline_system),
        "output_system_sha256": sha256_bytes(out_bytes),
        "output_bytes": len(out_bytes),
        "expected_output_sha256": EXPECTED["current"]["system.json"],
        "identity_match": sha256_bytes(out_bytes) == EXPECTED["current"]["system.json"],
        "authorized_changes": ['data["FONT.DDS"]', 'data["FONT2.DDS"]'],
        "all_other_parsed_json_deep_equal": bcmp == ocmp,
        "embedded_resources": resources,
    }
    ok = result["identity_match"] and result["all_other_parsed_json_deep_equal"] and all(
        r["matches_generated_dds"] and r["roundtrip_base64_gzip_exact"] for r in resources.values()
    )
    result["status"] = "PASS" if ok else "FAIL"
    if not ok:
        raise RuntimeError("BLOCKED_SYSTEM_JSON_IDENTITY_MISMATCH")
    return result


def single_build(args) -> int:
    out = Path(args.single_build)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    toolchain = verify_anchor_toolchain(Path(args.magick))
    input_auth, baseline_system, baselines = authenticate_inputs(Path(args.runtime_rc2), Path(args.source_font))
    resource_results = {}
    current_bytes = {}
    for name in ("FONT.DDS", "FONT2.DDS"):
        rr = build_resource(name, baselines[name], Path(args.source_font), Path(args.magick), out)
        resource_results[name] = rr
        current_bytes[name] = (out / "outputs" / name).read_bytes()
    system_validation = build_system_json(baseline_system, current_bytes, out / "outputs" / "system.json")
    summary = {
        "classification": CLASSIFICATION,
        "task": TASK,
        "status": "PASS",
        "toolchain_anchors": toolchain,
        "input_authentication": input_auth,
        "resources": resource_results,
        "system_json": system_validation,
        "products": {
            "noop_FONT.DDS": {"sha256": sha256_path(out / "outputs" / "noop_FONT.DDS"), "bytes": (out / "outputs" / "noop_FONT.DDS").stat().st_size},
            "noop_FONT2.DDS": {"sha256": sha256_path(out / "outputs" / "noop_FONT2.DDS"), "bytes": (out / "outputs" / "noop_FONT2.DDS").stat().st_size},
            "FONT.DDS": {"sha256": sha256_path(out / "outputs" / "FONT.DDS"), "bytes": (out / "outputs" / "FONT.DDS").stat().st_size},
            "FONT2.DDS": {"sha256": sha256_path(out / "outputs" / "FONT2.DDS"), "bytes": (out / "outputs" / "FONT2.DDS").stat().st_size},
            "system.json": {"sha256": sha256_path(out / "outputs" / "system.json"), "bytes": (out / "outputs" / "system.json").stat().st_size},
        },
    }
    write_json(out / "build_summary.json", summary)
    return 0


def normal_build(args) -> int:
    run_root = Path(args.run_root)
    if run_root.exists():
        shutil.rmtree(run_root)
    run_root.mkdir(parents=True)
    capture_binding = active_capture_binding(Path(args.toolchain_capture))
    if capture_binding["status"] != "PASS":
        raise RuntimeError("BLOCKED_EXACT_CAPTURED_TOOLCHAIN_NOT_EXECUTABLE")
    anchors = verify_anchor_toolchain(Path(args.magick))
    input_auth, _, _ = authenticate_inputs(Path(args.runtime_rc2), Path(args.source_font))
    write_json(run_root / "capture_binding.json", capture_binding)
    write_json(run_root / "toolchain_anchors.json", anchors)
    write_json(run_root / "input_authentication.json", input_auth)

    build_dirs = []
    for tag in ("A", "B"):
        dest = run_root / f"build_{tag}"
        build_dirs.append(dest)
        cmd = [
            sys.executable,
            str(Path(__file__).resolve()),
            "--runtime-rc2", str(Path(args.runtime_rc2).resolve()),
            "--source-font", str(Path(args.source_font).resolve()),
            "--toolchain-capture", str(Path(args.toolchain_capture).resolve()),
            "--magick", str(Path(args.magick).resolve()),
            "--single-build", str(dest),
        ]
        log = run_root / f"build_{tag}.log"
        with log.open("w", encoding="utf-8") as fh:
            fh.write("classification=" + CLASSIFICATION + "\n")
            fh.write("command=" + json.dumps(cmd, ensure_ascii=False) + "\n")
            fh.flush()
            proc = subprocess.run(cmd, stdout=fh, stderr=subprocess.STDOUT, text=True)
        if proc.returncode != 0:
            raise RuntimeError(f"clean build {tag} failed; see {log}")

    summaries = [json.loads((d / "build_summary.json").read_text(encoding="utf-8")) for d in build_dirs]
    product_names = ("noop_FONT.DDS", "noop_FONT2.DDS", "FONT.DDS", "FONT2.DDS", "system.json")
    products = {}
    deterministic = True
    for name in product_names:
        a = summaries[0]["products"][name]
        b = summaries[1]["products"][name]
        same = a == b and (build_dirs[0] / "outputs" / name).read_bytes() == (build_dirs[1] / "outputs" / name).read_bytes()
        products[name] = {"build_A": a, "build_B": b, "byte_identical": same}
        deterministic &= same
    if not deterministic:
        raise RuntimeError("deterministic clean rebuild mismatch")
    result = {
        "classification": CLASSIFICATION,
        "task": TASK,
        "status": "PASS",
        "capture_binding": capture_binding,
        "toolchain_anchors": anchors,
        "input_authentication": input_auth,
        "clean_builds": [str(d) for d in build_dirs],
        "products": products,
        "byte_identical_all_products": deterministic,
        "historical_source_recovered": False,
        "historical_assembler_sha256_provenance_only": HISTORICAL_ASSEMBLER_SHA256,
        "target_payload_bytes_present_as_inputs": False,
        "network_used": False,
        "package_installation_or_substitution": False,
    }
    write_json(run_root / "orchestrator_summary.json", result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def parse_args():
    p = argparse.ArgumentParser(description=TASK + " new canonical FONT v1.1 maintenance builder")
    p.add_argument("--runtime-rc2", required=True)
    p.add_argument("--source-font", required=True)
    p.add_argument("--toolchain-capture", required=True)
    p.add_argument("--magick", required=True)
    p.add_argument("--run-root")
    p.add_argument("--single-build", help=argparse.SUPPRESS)
    a = p.parse_args()
    if not a.single_build and not a.run_root:
        p.error("--run-root is required")
    return a


def main() -> int:
    args = parse_args()
    if args.single_build:
        return single_build(args)
    return normal_build(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"{type(exc).__name__}: {exc}", file=sys.stderr)
        raise
