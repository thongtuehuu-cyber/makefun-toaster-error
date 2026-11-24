import os
import sys

LINE = "ERROR: Third slice today. I am a toaster, not an accomplice. Seek help."

def main():
    # Gate: UTF-8, 1-120 chars, not only whitespace, one line, no leading/trailing whitespace.
    assert 1 <= len(LINE) <= 120, "line must be 1-120 characters"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE == LINE.strip(), "line must have no leading/trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
