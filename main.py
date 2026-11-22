"""Build the competition entry: one short text, written to intrigue.

The program takes no input, reads nothing, and writes the same text on
every run. The text is held as four plain sentences; joining them with a
single space gives the entry exactly as it should read.
"""

import os

SENTENCES = [
    "On the third shelf of the library nobody visits, a book waits with",
    "your name on its spine, in handwriting you almost recognise.",
    "Its pages are still warm, and the last one is folded at the corner,",
    "as if someone stopped mid-sentence and meant to come back.",
]

ENTRY = " ".join(SENTENCES)


def main():
    if not 1 <= len(ENTRY) <= 280:
        raise SystemExit("entry must be 1-280 characters, got %d" % len(ENTRY))
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line of text")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %d characters to /output/entry.txt" % len(ENTRY))


if __name__ == "__main__":
    main()
