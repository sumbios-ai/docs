#!/usr/bin/env python3
"""Fail on writing that breaks the Sumbios voice rules.

    python3 scripts/check_voice.py

Checks every .mdx page outside node_modules. MDX comments ({/* ... */}) are
skipped, because they hold editor notes rather than published text.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

RULES = [
    (re.compile("[—–]"), "em or en dash: rewrite the sentence (use a colon, comma or full stop)"),
    (re.compile(r"\bCompanion\b"), '"Companion": the in-app name is "the Assistant"'),
    (re.compile(r"\bmembership\b", re.I), '"membership": O plans are a subscription'),
    (re.compile(r"\b(supercharge|seamless(ly)?|10x|unlock|AI-powered|game[- ]changer)\b", re.I),
     "hype word"),
    # Plural only: a "Reach target" is a number, "targets" and "leads" are people.
    (re.compile(r"\b(leads|targets)\b", re.I),
     "people are never leads or targets (quote a UI label in **bold** if you must)"),
    (re.compile("[\U0001F300-\U0001FAFF☀-➿]"), "emoji"),
]

COMMENT = re.compile(r"\{/\*.*?\*/\}", re.S)
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
BOLD = re.compile(r"\*\*[^*]+\*\*")


def main():
    bad = 0
    for path in sorted(ROOT.rglob("*.mdx")):
        if "node_modules" in path.parts:
            continue
        text = COMMENT.sub("", path.read_text())
        for n, line in enumerate(text.splitlines(), 1):
            for rx, why in RULES:
                probe = BOLD.sub("", line) if "leads" in why else line
                if rx.search(probe):
                    print(f"{path.relative_to(ROOT)}:{n}: {why}\n    {line.strip()[:140]}")
                    bad += 1
    if bad:
        sys.exit(f"\n{bad} voice problem(s)")
    print("voice check: clean")


if __name__ == "__main__":
    main()
