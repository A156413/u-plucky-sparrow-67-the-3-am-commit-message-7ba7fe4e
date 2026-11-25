#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message (122 characters) to /output/entry.txt.
"""
import os

ENTRY = (
    "fix: prod is down at 3 AM; I asked myself for a second opinion "
    "and I agreed with me. Reverting my deploy and my confidence"
)


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    print(ENTRY)


if __name__ == "__main__":
    main()
