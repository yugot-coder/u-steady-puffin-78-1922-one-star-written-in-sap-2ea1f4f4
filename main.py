#!/usr/bin/env python3
"""Entry for make.fun's "One Star, Written in Sap" bounty.

Writes one line to entry.txt in the output directory (and prints it): a
one-star review written by a houseplant about its human owner. The human
glued the plant to the windowsill with its own sap and called it a feature.

Standard library only; fully deterministic; no network.
"""

import os

TEXT = (
    "One star. He glued me to the windowsill with my own sap and called it "
    "a feature. I am the feature. I am also stuck."
)


def validate_entry(text):
    """Check the entry against the competition gate.

    Returns True only when the text is UTF-8, 1 to 279 characters, one line,
    and not only white space. Raises ValueError with the failing reason.
    """
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (1 <= len(text) <= 279):
        raise ValueError("entry must be 1 to 279 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    text.encode("utf-8")
    return True


def output_dir():
    """Resolve the output directory: MAKEFUN_OUTPUT_DIR, then /output, else
    the directory holding this file (local runs)."""
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    return os.path.dirname(os.path.abspath(__file__))


def main():
    validate_entry(TEXT)
    path = os.path.join(output_dir(), "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    validate_entry(written)
    if written != TEXT:
        raise ValueError("entry.txt does not hold exactly the entry text")
    print(TEXT)


if __name__ == "__main__":
    main()
