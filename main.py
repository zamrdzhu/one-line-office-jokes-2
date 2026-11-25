"""One line that makes office life funny.

Prints the joke to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the joke is a constant in this file.
The 199-character gate is checked on every run so an over-long edit
can never slip through silently.
"""

import os
import sys

LINE = (
    "The reply-all chain is 47 emails long now, and the original "
    "question is still unanswered."
)


def main() -> int:
    if not 1 <= len(LINE) <= 199:
        print(f"error: line is {len(LINE)} chars, must be 1-199",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


# The exit code mirrors the gate: 0 only when the joke is valid.
if __name__ == "__main__":
    raise SystemExit(main())
