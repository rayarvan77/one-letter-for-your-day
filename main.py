"""One Letter for Your Day — make.fun entry.

Writes exactly one letter, "K", to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and prints it.

The letter K stands for the word behind the day: "knackered" — utterly
spent after a long Tuesday of grinding. The program output is the single
letter only: no word, no gloss, no punctuation, no trailing newline.
"""

import os
import sys

LETTER = "K"


def main() -> int:
    # Validate: exactly one character, a letter A-Z.
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        print(f"invalid letter: {LETTER!r}", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR names a directory; fall back to /output/entry.txt.
    if os.path.isdir(output_dir):
        output_path = os.path.join(output_dir, "entry.txt")
    elif output_dir.endswith("entry.txt"):
        output_path = output_dir
    else:
        output_path = os.path.join(output_dir, "entry.txt")

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

    # Re-read and re-validate what was actually written.
    with open(output_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LETTER:
        print(f"output mismatch: {written!r}", file=sys.stderr)
        return 1

    print(LETTER)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
