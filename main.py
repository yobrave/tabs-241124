"""Tab count entry: confirm the digits, then relay entry.txt to the gate output."""
import json
import os
import re
import sys

TALLY = "entry.txt"
DIGITS_MAX = 5


def confirm(text: str) -> dict:
    bare = text.strip()
    checks = [
        ("only_digits", bool(re.fullmatch(r"[0-9]{1,5}", bare))),
        ("within_span", 1 <= len(bare) <= DIGITS_MAX),
        ("nonempty_bytes", len(bare.encode("utf-8")) >= 1),
    ]
    return {
        "digits": bare,
        "confirmations": [n for n, good in checks if good],
        "missing": [n for n, good in checks if not good],
        "admitted": all(good for _, good in checks),
    }


def relay() -> int:
    with open(TALLY, encoding="utf-8") as tap:
        raw = tap.read()
    note = confirm(raw)
    tray = os.environ.get("MAKEFUN_OUTPUT_DIR", "tray")
    os.makedirs(tray, exist_ok=True)
    with open(os.path.join(tray, TALLY), "wb") as tap:
        tap.write(raw.encode("utf-8"))
    print(json.dumps({"tally": "browser-tabs", "note": note, "tray": tray}))
    return 0 if note["admitted"] else 1


if __name__ == "__main__":
    sys.exit(relay())
