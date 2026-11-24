#!/usr/bin/env python3
"""make.fun entry - writes the competition text to /output/entry.txt"""
import os

def main():
    entry = 'G'
    out = "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as f:
        f.write(entry)

if __name__ == "__main__":
    main()
