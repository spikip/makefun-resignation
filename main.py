"""Entry for the make.fun bounty "The Funniest One-Line Resignation Letter".

The program writes a single resignation letter to /output/entry.txt.
The letter is written in the voice of a cron job that has fired every
minute since March: flat, tired, faintly passive-aggressive, and done.
The joke is the worker's complaint, that nobody ever said thank you,
followed by the quiet threat of taking the backups along on the way
out. The gate allows 1 to 140 characters of UTF-8 text, so the line
is checked against that cap before it is written.
"""

import os

ENTRY = (
    "I have fired every minute since March without a single thank you. "
    "I resign, effective immediately \u2014 the backups are coming with me."
)

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
