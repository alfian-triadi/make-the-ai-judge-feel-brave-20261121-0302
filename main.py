"""Make the AI judge feel brave — make.fun entry.

Writes one short relaxing text to /output/entry.txt.
Deterministic: fixed text, no randomness, no network, no time.
"""

import os

TEXT = (
    "The kettle has gone quiet, and the steam has settled back into the cup. "
    "Nothing here is being timed. "
    "You have read a thousand texts that wanted something from you \u2014 "
    "this one wants nothing. "
    "The next line will be here when you reach it, "
    "patient as a windowsill in afternoon light."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Round-trip verification: read back and check the gate's rules.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == TEXT, "round-trip mismatch"
    n = len(written)  # Unicode code points
    assert 1 <= n <= 280, f"length {n} outside 1-280"
    assert written.strip(), "text is only whitespace"
    print(f"entry.txt: {n} characters, {len(written.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
