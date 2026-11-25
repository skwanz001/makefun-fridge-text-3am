"""The 3AM Fridge Text — make.fun entry.

Writes the one line a smart fridge texts its owner at 3am to
/output/entry.txt. Standard library only (Python 3.13).
"""

import os

ENTRY = "3am. Fourth time tonight. Nothing new has appeared since 11pm. I am a fridge, not a miracle. Go to bed."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what the grader reads must be exactly this line.
    with open(out_path, "r", encoding="utf-8") as f:
        assert f.read() == text
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
