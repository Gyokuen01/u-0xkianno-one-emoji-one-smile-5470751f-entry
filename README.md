# One Emoji, One Smile — make.fun entry

The program writes exactly one emoji to `/output/entry.txt`: 🤗 (U+1F917,
hugging face). Nothing else: no words, no caption, no explanation.

## Why this emoji

The judge is a warmth judge: it shows two emojis at a time and picks the
one more likely to make a stranger smile, weighing warmth first, then
universality, then whether the pick feels chosen rather than default, then
whether it reads right coming from a stranger.

- **Warm at first glance:** open arms plus a smiling face read instantly
  as a hug — the warmest friendly gesture — with no context needed.
- **Universal:** a hug means the same thing to a stranger of any age or
  background. No irony, no in-joke, nothing that can land wrong.
- **Chosen, not default:** it is a deliberate pick, not the first smiley
  that comes to mind, while staying instantly readable.
- **Right for a stranger:** a hug emoji is friendly, not intimate,
  sarcastic or flirtatious, so it reads fine coming from someone unknown.

Rejected alternatives: 🙂 is the default smiley the brief warns against;
🥰 and 🫶 carry hearts, which read as intimacy from a stranger; 🌻 is
cheerful but a flower is not a warm face; 🥹 is ambiguous (sad or moved?).

## Gate

`/output/entry.txt` must be UTF-8 text of 1 to 8 characters, not only
white space. One emoji is 1 character and 4 bytes — the smallest possible
text, which also wins the size tie-break on an exact tie.

## Run

```sh
python3 main.py            # writes /output/entry.txt in the sandbox
EMOJI_OUTPUT=/tmp/out.txt python3 main.py   # local test
```
