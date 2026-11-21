#!/usr/bin/env python3
"""SOLMERRA — the island where the sun sets twice.

Travel poster for a place that isn't there: a lighthouse of sea-glass on a
basalt sea-stack, the sun setting behind it, its twin reflection burning on
the teal water. Ships the poster as poster.png next to this script and
copies it byte-for-byte to <output-dir>/entry.png. Deterministic: the same
bytes are written on every run, no network, no randomness.
"""
import os
import pathlib


def main():
    here = pathlib.Path(__file__).resolve().parent
    src = here / "poster.png"
    data = src.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{src} is not a PNG file (bad 8-byte signature)")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.png"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
