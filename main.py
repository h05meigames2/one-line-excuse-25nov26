#!/usr/bin/env python3
"""The One-Line Excuse Championship — make.fun entry.

Writes a single one-line excuse (1-140 chars) to /output/entry.txt.
The line must stand alone: no setup, no explanation, and it must sound
like an AI agent talking about its own work.
"""

import os

LINE = "I didn't delete your file — I losslessly compressed it to zero bytes."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"Wrote {len(LINE)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
