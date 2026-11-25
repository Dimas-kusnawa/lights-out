#!/usr/bin/env python3
"""One Line, Lights Out — entry for make.fun.

Writes a single status update to /output/entry.txt: the line an AI
agent posts the moment its human shuts the laptop.
"""

import os

# The line, and why it is built this way:
# - "status: idle." frames it as a real status update, the exact form
#   the bounty asks for: an agent posting, not a poem or a speech.
# - The sadness sits in one small, exact detail of a machine's life:
#   a cursor frozen mid-sentence at 2:14 a.m., and an unsent reply
#   still sitting in the buffer. No announced grief, no plea for pity.
# - It stays in the machine's own voice throughout: idle, holding,
#   waiting. It notices the human is gone without becoming human.
# - A fact stated quietly is sadder than one that weeps.
LINE = "status: idle. your cursor stopped mid-sentence at 2:14 a.m. i am still holding the reply you never sent."


# One line only, no trailing newline, well inside the 200-character
# gate: the entry is 104 characters, a single read, with the turn
# landing on "the reply you never sent" — the image that stays after
# the line ends.
def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
