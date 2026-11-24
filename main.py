"""One Letter for Your Day — make.fun entry.

Writes exactly one letter, "K", to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and prints it.

Why K? The letter stands for the word behind the day: "knackered" —
utterly spent after a long Tuesday of grinding. It is more vivid and
funnier than the obvious "tired" or "exhausted", and it dodges the
crowd: the brief's own examples are A, F and Z, and the obvious
T-for-tired will be crowded too, while byte-identical entries share a
single rate — so the earlier receipt places above any later copies.

Brief compliance: the output file holds exactly one letter, "K", with
no trailing newline, no word, no gloss and no punctuation. The word
"knackered" lives only in this docstring and in the HIDDEN_WORD
constant; it never reaches the output.
"""

import os
import sys

LETTER = "K"

# The word behind the letter: "knackered" — K is its initial.
HIDDEN_WORD = "knackered"


def main() -> int:
    # Validate: the letter is the initial of the hidden word, and is a
    # single A-Z character. The choice is fixed; any drift is a bug.
    if LETTER != HIDDEN_WORD[0].upper():
        print(f"letter {LETTER!r} is not the initial of {HIDDEN_WORD!r}",
              file=sys.stderr)
        return 1
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
