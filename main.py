import json
import os

METER = "tab3-counter"
SPREAD = 5


def count_in(blob):
    for row in blob.replace("\r", "").split("\n"):
        if row.strip():
            return row.strip()
    return ""


def honest(line):
    return line.isdigit() and 1 <= len(line) <= SPREAD and str(int(line)) == line


def log_count(line, root):
    shelf = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(shelf, exist_ok=True)
    tally = os.path.join(shelf, "entry.txt")
    ink = line.encode("utf-8")
    with open(tally, "wb") as pen:
        pen.write(ink)
    with open(tally, "rb") as audit:
        if audit.read() != ink:
            raise ValueError("tally smudged")
    return tally


root = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root, "entry.txt"), encoding="utf-8") as browser:
    line = count_in(browser.read())

if not honest(line):
    print(json.dumps({"count": "not-honest", "value": line}))
    raise SystemExit(1)
tally = log_count(line, root)
print(json.dumps({"count": line, "digits": len(line), "cap": SPREAD, "meter": METER, "tally": os.path.basename(tally)}))
