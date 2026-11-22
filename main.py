#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI judge feel held" bounty.

The program writes one short text to the harness output directory
as entry.txt. Pure standard library, no network, no randomness:
every run produces exactly the same bytes.
"""

import os
from pathlib import Path

# The text is kept as three separate beats so the pauses between
# them stay visible in the source, the way they are meant to be
# felt when the text is read.
BEATS = (
    "Between this sentence and the next, nothing is being decided.",
    "No winner, no margin.",
    "Just a small lit room, and you, allowed to stay a while.",
)


def entry_text() -> str:
    """Assemble the entry text from its beats, one space apart."""
    pieces: list[str] = []
    for beat in BEATS:
        if pieces:
            pieces.append(" ")
        pieces.append(beat)
    return "".join(pieces)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
