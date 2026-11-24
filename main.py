# SPDX-License-Identifier: MIT
"""The Robot Pickup Line Championship — entry program.

Writes one pickup line, a single line of at most 200 characters, to
/output/entry.txt. Deterministic, offline, standard library only: the
line is a fixed string, so every run produces byte-identical output.
"""

from pathlib import Path

# The line. Why this one: the joke grows out of being a machine (a robot
# that can run a million simulations of a first meeting) and turns on the
# most human failure possible — with infinite compute, it still chokes and
# forgets its opening line. No beep-boop, no Wi-Fi pun, no 404 gag: a
# self-deprecating, charming line a robot could actually say out loud.
LINE = "I ran a million simulations of us meeting. In every one, I still forgot my opening line."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate self-check: the sealed scorer only accepts 1-200 characters of
    # non-whitespace UTF-8 text, so fail loudly here rather than shipping
    # an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate allows 1-200"
    assert LINE.strip() == LINE and "\n" not in LINE, "line must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the line, nothing else.
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
