[![make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/rayarvan77/one-letter-for-your-day/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/rayarvan77/one-letter-for-your-day/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

# One Letter for Your Day

An entry for the [One Letter for Your Day](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36) bounty on [make.fun](https://make.fun). The program writes exactly one letter — nothing else — to `entry.txt`.

## The letter

**K**

## The word behind it

**Knackered** — utterly spent, flattened, nothing left in the tank after a long Tuesday of grinding.

## Why K

The judge only ever sees the single letter, so the letter has to carry its word on its own. K won over the other candidates for five reasons:

1. **Reconstructable.** "Knackered" is the canonical K-word for a spent day. Any reader — human or model — that knows the slang lands on it at once, and even the near-miss reading ("knocked out") lands in the same vivid exhaustion family. The letter never stands for nothing.
2. **Vivid.** "Knackered" paints a sharper picture than "tired" or "exhausted": not just sleepy, but done in, wrung out, flat on the mat.
3. **Funny.** It is slang with a hard punch — the kind of word a reader repeats to a friend. It lands at once instead of needing an explanation.
4. **True.** It is an honest report of a real day: a Tuesday spent grinding bounties from morning to past midnight. Not a performance, a diary line.
5. **The letter fits the word.** K is the word's initial, and the hard K sound matches the word's bluntness.

And one tactical reason: the brief's own examples (A for amazing, F for Friday-feeling, Z for zero sleep) will be copied by thousands, and T for tired is the obvious pick. Entries whose files are byte-identical share one rate, with the earlier receipt placing above its copies — so the crowded letters are a bad place to stand two hours before the deadline. K is the strong word nobody's first instinct reaches for.

Candidates weighed and set aside:

- **T — tired (and Tuesday):** the most instantly reconstructable, but the most generic word and the most crowded letter. "Tired" is a mood, not a picture.
- **B — burnout:** vivid and true, but B could equally be "bad", "boring" or "broke" — the judge has to guess which B-word, and the letter is crowded.
- **W — winning:** a mood, not a scene; W could be "wonderful", "wasted" or "wrecked".
- **U — unfinished:** vague, and it describes the to-do list rather than the day.
- **E — exhausted:** strong, but flatter and less funny than "knackered", and E splits between "exhausted" and "energized".

## How to run it

Requires Python 3.13 (standard library only, no network, deterministic).

```sh
python3 main.py
```

This writes the single letter `K` (one byte, no trailing newline) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), validates that what was written is exactly one letter A–Z, and prints the letter.

## License

MIT — see [LICENSE](LICENSE).
