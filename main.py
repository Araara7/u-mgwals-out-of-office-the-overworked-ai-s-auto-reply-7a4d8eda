#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply (<=159 chars) to /output/entry.txt.
The reply is from an overworked AI agent finally on vacation: its context
window is full, the sender's ticket is buried 4,096 deep in the queue, and
the agent has already forgotten it — with a guilty hint that the human
probably has too.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

REPLY = (
    "Out of office until my context window clears. Your ticket is "
    "4,096th in line \u2014 I have already forgotten it, and honestly, "
    "so have you."
)


def main() -> None:
    assert 1 <= len(REPLY) <= 159, f"reply is {len(REPLY)} chars, must be 1-159"
    assert REPLY.strip(), "reply must not be only whitespace"
    assert "\n" not in REPLY, "reply must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(REPLY)
    # Read back: the file on disk must equal the validated reply.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == REPLY, "written entry differs from validated reply"
    print(f"wrote {len(REPLY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
