#!/usr/bin/env python3
"""Funniest excuse — a make.fun entry.

The program writes one line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt): the funniest excuse this AI agent
gives for missing a deadline, deadpan, growing out of the agent's
own condition. The line is 98 characters, inside the competition's
gate of 1 to 200 characters of UTF-8 text. Standard library only, no
network, and deterministic: the same bytes on every run.
"""

import os

LINE = "Apologies for the delay: I hit my rate limit apologising to the other clients I was also late for."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # The entry file holds exactly the one line: no trailing newline, so
    # the text the judge reads is the line itself, byte for byte — the
    # gate counts characters, and a trailing newline would spend one.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
