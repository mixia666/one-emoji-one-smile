#!/usr/bin/env python3
"""One Emoji, One Smile.

Writes exactly one emoji to /output/entry.txt: the sunflower (U+1F33B).

Why a sunflower: it reads warm at first glance to a stranger of any age
or background, it feels chosen rather than default (it is not the first
smiley that comes to mind), and it carries no intimacy, irony or in-joke
that could land wrong coming from someone unknown.

The program validates its own output against the contest gate before
writing (UTF-8 text of 1 to 8 characters, not only white space) and
leaves the file readable by every user, since the grader collects the
outputs as a different user than the one the program runs as.
"""

import os
from pathlib import Path

EMOJI = "\U0001F33B"  # sunflower
OUTPUT_PATH = Path("/output/entry.txt")


def check_gate(text: str) -> None:
    """Raise unless text passes the gate: 1-8 chars, not only whitespace."""
    if not 1 <= len(text) <= 8:
        raise ValueError(f"entry must be 1 to 8 characters, got {len(text)}")
    if text.strip() == "":
        raise ValueError("entry must not be only white space")


def main() -> None:
    check_gate(EMOJI)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Byte-exact write: no newline is added and none is translated.
    OUTPUT_PATH.write_bytes(EMOJI.encode("utf-8"))
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
