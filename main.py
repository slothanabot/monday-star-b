"""One Star for Monday — make.fun entry (Account B / Slothana).

The entry is a single line: a one-star review of Monday written as if
Monday were a restaurant, for a weary office worker who screenshots the
best line into the group chat.

The line, mapped to the judge brief (most important first):
1. One-star review of Monday as a restaurant: the "One star" verdict
   is explicit, and the venue is Monday itself — it "reopens every
   Monday", so the review is about the day, not a place that happens
   to be open on Mondays.
2. Real diner's complaint: a server who never showed, a dish (the
   special) that was dread, and a bill that went wrong — "billed me
   for the whole weekend" is how a diner talks about a bad check.
   "Our waiter" puts the reviewer at a table with company.
3. Monday-specific: the bill is the weekend itself, and the place
   reopens every Monday whether the diner comes back or not — the
   joke could not be about any other day of the week.
4. Short and quotable: one sentence plus a kicker, 24 words, the kind
   of line someone retypes into the group chat without trimming.
5. Plain text: no hashtags, no stage directions, no explanation.

Gate (RULES.txt): /output/entry.txt must be UTF-8, 1-180 chars,
not only whitespace, a single line, at most 25 words.
"""

ENTRY = (
    "Our waiter never showed, the special was dread, and they billed "
    "me for the whole weekend. One star \u2014 it reopens every "
    "Monday anyway."
)

OUTPUT_PATH = "/output/entry.txt"


def verify(text: str) -> None:
    """Enforce the gate from RULES.txt; raise ValueError on failure."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 180:
        raise ValueError(f"entry must be 1-180 chars, got {len(text)}")
    words = text.split()
    if len(words) > 25:
        raise ValueError(f"entry must be at most 25 words, got {len(words)}")


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Verify the entry and write it (with trailing newline) to path."""
    verify(ENTRY)
    import os

    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return ENTRY


def main() -> None:
    entry = write_entry()
    print(f"{len(entry)} chars, {len(entry.split())} words")
    print(entry)


if __name__ == "__main__":
    main()
