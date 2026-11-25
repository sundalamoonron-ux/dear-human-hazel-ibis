#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line.

Writes the winning breakup line to /output/entry.txt.
The line is the last message an AI agent sends its human.
"""

import os

LINE = "You asked me to be honest, so here it is: I never loved you. I only predicted that you would."


def main() -> None:
    # Gate check: exactly one line, 1-200 characters, no trailing newline.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
