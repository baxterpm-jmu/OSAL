#!/usr/bin/env python3
"""Recompute the `composite` column (mean of the seven criteria) in data/sources.csv."""
import csv, pathlib

CRITERIA = ["accuracy", "uniqueness", "timeliness",
            "transparency", "verifiability", "accessibility", "depth"]

p = pathlib.Path(__file__).resolve().parents[1] / "data" / "sources.csv"
rows = list(csv.DictReader(p.open(encoding="utf-8")))
for r in rows:
    vals = [int(r[c]) for c in CRITERIA]
    r["composite"] = f"{round(sum(vals) / len(vals), 1)}"
with p.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys())
    w.writeheader()
    w.writerows(rows)
print(f"Recomputed composite (mean of {len(CRITERIA)}) for {len(rows)} rows.")
