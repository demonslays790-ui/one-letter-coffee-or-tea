"""One Letter: Coffee or Tea — entry.

Writes exactly one letter, ``A`` (coffee), and nothing else.
"""

import os

CHOICE = "A"  # Coffee. The brief allows exactly one letter: A for coffee, B for tea.

# Guard: the entry must be exactly one character, A or B — nothing else,
# no newline, no punctuation, no explanation. Fail loudly otherwise.
assert len(CHOICE) == 1 and CHOICE in ("A", "B"), f"invalid choice: {CHOICE!r}"

output_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
path = os.path.join(output_dir, "entry.txt")

with open(path, "w", encoding="ascii") as f:
    f.write(CHOICE)

os.chmod(path, 0o644)
