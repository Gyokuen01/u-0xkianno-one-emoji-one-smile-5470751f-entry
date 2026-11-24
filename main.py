"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the hugging face (U+1F917).

Why this emoji, against the judge's brief (a warmth judge comparing two
emojis at a time, picking the one more likely to make a stranger smile):
1. Warm and friendly at first glance: open arms and a smiling face read
   instantly as a hug — the warmest friendly gesture — with no context.
2. Universality: a hug is understood the same way by a stranger of any age
   or background; no irony, no in-joke, nothing that can land wrong.
3. Chosen, not default: it is a deliberate pick, not the first smiley that
   comes to mind, while staying instantly readable.
4. Right for a stranger: a hug emoji is friendly, not intimate, sarcastic
   or flirtatious, so it reads fine coming from someone unknown.
The gate allows 1 to 8 UTF-8 characters; one emoji is 1 character and
4 bytes — the smallest possible text, which also wins the size tie-break.
"""

from pathlib import Path
import os

# The one emoji. Exactly one code point, nothing else: no words, no
# caption, no explanation, no trailing newline.
EMOJI = "🤗"

# The grader runs the program in a sandbox where /output exists; allow an
# override so the same entry can be exercised locally without that path.
OUTPUT_PATH = Path(os.environ.get("EMOJI_OUTPUT", "/output/entry.txt"))

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 8
# characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 8


def check_emoji(emoji: str) -> str:
    """Return the emoji unchanged, or fail loudly if it breaks the rules."""
    assert emoji, "emoji must not be empty"
    assert len(emoji) == 1, "entry must be exactly one emoji, one code point"
    assert emoji.strip(), "emoji must not be only white space"
    assert MIN_CHARS <= len(emoji) <= MAX_CHARS, (
        f"emoji is {len(emoji)} chars, outside the {MIN_CHARS}-{MAX_CHARS} gate"
    )
    return emoji


def main() -> None:
    emoji = check_emoji(EMOJI)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly the emoji (4 bytes). An
    # exact tie on win rate goes to the smaller text, so every byte counts.
    OUTPUT_PATH.write_text(emoji, encoding="utf-8")
    # The entry is collected as another user than the one the program runs
    # as, so leave the file readable by everyone.
    os.chmod(OUTPUT_PATH, 0o644)
    # Read it back: what the judge scores is the file, not the string.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == emoji, "written file does not match the emoji"
    print(f"Wrote {len(emoji)} char to {OUTPUT_PATH}: {emoji}")


if __name__ == "__main__":
    main()
