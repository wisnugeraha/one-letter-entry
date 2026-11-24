#!/usr/bin/env python3
"""make.fun entry: the one letter for the day, written to /output/entry.txt.

The judge compares one-letter entries two at a time; this program emits
exactly one character (the day's letter) plus a trailing newline, in
UTF-8, to the gate artifact path.
"""
import os

ENTRY = "G"
OUT = "/output/entry.txt"


def write_entry() -> None:
    """Write the single letter to the gate artifact, idempotent."""
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    # confirm what landed on disk; re-open so we read the flushed bytes
    with open(OUT, "r", encoding="utf-8") as f:
        on_disk = f.read()
    if on_disk != ENTRY + "\n":
        raise SystemExit(f"on-disk entry mismatch: {on_disk!r}")
    print(f"Wrote {ENTRY!r} to {OUT}")


def main():
    write_entry()


if __name__ == "__main__":
    main()
