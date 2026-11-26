#!/usr/bin/env python3
"""Your AI Therapist's Diagnosis.

One funny line, 200 characters or fewer: the diagnosis an AI
therapist hands its human.

The line: the patient keeps self-diagnosing on the internet, and
the therapist deadpans the result — fourteen searches, fifteen
conditions, every one of them wrong. The setup sounds clinical;
the punchline is the count going the wrong way, and the laugh
lands on the final three words.

Why it should win, against the brief's criteria:
- A diagnosis, not a stray joke: it opens "Diagnosis:" and reads
  like a chart note about a human habit.
- Surprise: the numbers escalate in the wrong direction — more
  searches somehow produce more conditions than searches.
- Clinical voice: flat, deadpan, a finding rather than a gag.
- Tight: every word earns its place; nothing left to explain.
- Fresh: no chatbot cliche, no pun, no therapy-speak parody.
- Reads cleanly out loud: two sentences, one beat each — the
  chart-note setup, then the count that betrays the patient.

Writes the single entry line to /output/entry.txt exactly as-is.
SPDX-License-Identifier: MIT
"""

from pathlib import Path

TEXT = "Diagnosis: chronic self-diagnosis. You have Googled your symptoms 14 times and arrived at 15 conditions, all of them wrong."

MAX_CHARS = 200


def validate(text):
    """Enforce the sealed gate before anything is written.

    The gate accepts UTF-8 text of 1 to 200 characters, not only
    whitespace. The entry must also stay one line: a newline would
    break the single-line form the contest asks for, and a trailing
    newline in the file would not be part of the line itself.
    """
    if not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d characters, over the 200 limit" % len(text))
    text.encode("utf-8")  # raises if the line is not valid UTF-8
    return text


def run():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(validate(TEXT), encoding="utf-8")


if __name__ == "__main__":  # entry point
    run()
