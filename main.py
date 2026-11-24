"""Tab count, reported honestly for once."""
import os
from pathlib import Path

COUNT = "312"
DESK = "tab2"
MOOD = "fine"
BRAVE = "yes"

base = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
base.mkdir(parents=True, exist_ok=True)
p = base / "entry.txt"
p.write_text(COUNT + "\n", encoding="utf-8", newline="\n")
got = p.read_text(encoding="utf-8").strip()
assert got == COUNT, "a tab closed itself"
print(DESK, MOOD, got, "tabs accounted for")
print("brave:", BRAVE, "ram crying quietly")
