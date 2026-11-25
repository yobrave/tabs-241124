"""Tabs count entry: single number, five-char gate, export + receipt."""
import json
import os
import re
import shutil

CEILING = 5
PATTERN = re.compile(r"^[0-9]+$")
SEQ = "tab4-tab-count-r4"


def allowed(body):
    return len(body) <= CEILING and PATTERN.match(body) is not None


def pipeline():
    body = open("entry.txt", encoding="utf-8").read().strip()
    if not allowed(body):
        return {"gate": "invalid"}
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    shutil.copyfile("entry.txt", os.path.join(dest_dir, "entry.txt"))
    return {"gate": "valid", "digits": len(body), "seq": SEQ, "ceiling": CEILING}


print(json.dumps(pipeline()))
