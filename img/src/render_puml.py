"""Render TEPO PlantUML sources to PNG using the public PlantUML server.

Usage: python render_puml.py [src_dir] [out_dir]

PlantUML's URL encoding: UTF-8 -> raw deflate -> custom base64 alphabet.
"""
import os
import sys
import time
import zlib
import urllib.request

BASE = "https://www.plantuml.com/plantuml/png/"


def _encode6bit(b: int) -> str:
    if b < 10:
        return chr(48 + b)
    b -= 10
    if b < 26:
        return chr(65 + b)
    b -= 26
    if b < 26:
        return chr(97 + b)
    b -= 26
    if b == 0:
        return "-"
    if b == 1:
        return "_"
    return "?"


def _append3bytes(b1: int, b2: int, b3: int) -> str:
    c1 = b1 >> 2
    c2 = ((b1 & 0x3) << 4) | (b2 >> 4)
    c3 = ((b2 & 0xF) << 2) | (b3 >> 6)
    c4 = b3 & 0x3F
    return (
        _encode6bit(c1 & 0x3F)
        + _encode6bit(c2 & 0x3F)
        + _encode6bit(c3 & 0x3F)
        + _encode6bit(c4 & 0x3F)
    )


def plantuml_encode(text: str) -> str:
    data = zlib.compress(text.encode("utf-8"))[2:-4]
    out = []
    for i in range(0, len(data), 3):
        chunk = data[i:i + 3]
        if len(chunk) == 3:
            out.append(_append3bytes(chunk[0], chunk[1], chunk[2]))
        elif len(chunk) == 2:
            out.append(_append3bytes(chunk[0], chunk[1], 0))
        else:
            out.append(_append3bytes(chunk[0], 0, 0))
    return "".join(out)


def render(src: str, dst: str) -> None:
    with open(src, encoding="utf-8") as fh:
        source = fh.read()
    if "@startuml" not in source:
        raise ValueError(f"{src}: missing @startuml")
    url = BASE + plantuml_encode(source)
    request = urllib.request.Request(url, headers={"User-Agent": "TEPO-D1-build/1.0"})
    with urllib.request.urlopen(request, timeout=90) as response:
        payload = response.read()
    if not payload.startswith(b"\x89PNG"):
        raise RuntimeError(f"{src}: server did not return a PNG ({payload[:80]!r})")
    with open(dst, "wb") as fh:
        fh.write(payload)
    print(f"ok {os.path.basename(dst)} ({len(payload)} bytes)")


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    src_dir = sys.argv[1] if len(sys.argv) > 1 else here
    out_dir = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(here)
    os.makedirs(out_dir, exist_ok=True)
    failures = 0
    for name in sorted(os.listdir(src_dir)):
        if not name.endswith(".puml"):
            continue
        src = os.path.join(src_dir, name)
        dst = os.path.join(out_dir, name[:-5] + ".png")
        for attempt in range(3):
            try:
                render(src, dst)
                break
            except Exception as exc:  # noqa: BLE001 - report and retry
                print(f"retry {name} ({attempt + 1}/3): {exc}")
                time.sleep(2)
        else:
            failures += 1
            print(f"FAILED {name}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
