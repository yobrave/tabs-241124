"""Open tab tally counter."""
import json
import os
import re
from pathlib import Path

digits = (Path(__file__).resolve().parent / "entry.txt").read_bytes().decode("utf-8").strip()
SCREENS = "monitors-open"
tally = re.fullmatch(r"[0-9]+", digits) is not None
if tally:
    bin_ = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    bin_.mkdir(parents=True, exist_ok=True)
    (bin_ / "entry.txt").write_bytes(digits.encode("utf-8"))
print(json.dumps({"tally": "counted" if tally else "rejected", "tabs": digits if tally else None}))
