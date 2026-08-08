#!/usr/bin/env python3
"""
Consistency checker for the PRISMA requirement register.

Run locally:  python3 werkzeuge/validate_requirements.py
Exit code 0 = clean, 1 = findings. CI treats findings as a failed build.

Checks implemented:
  1.  ID format and uniqueness across the whole register
  2.  Allowed status and priority values
  3.  Every FR / NFR names at least one parent business requirement
  4.  Every named parent actually exists
  5.  No orphan business requirement (every BR is realised by something)
  6.  Every FR / NFR has at least one acceptance criterion
  7.  Every FR / NFR names at least one verification / test case
  8.  Business requirements carry metric, target and verification
  9.  Baselined requirements may not depend on a parent still in draft
 10.  Weak wording detection ("fast", "user-friendly", "etc.") in titles/criteria
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("pyyaml is required:  python3 -m pip install pyyaml")

REGISTER = Path(__file__).resolve().parent.parent / "requirements.yaml"

STATUSES = {
    "draft", "review", "approved", "baselined",
    "implemented", "verified", "rejected", "superseded",
}
PRIORITIES = {"must", "should", "may"}
ID_PATTERNS = {
    "business_requirements": re.compile(r"^BR-\d{2}$"),
    "functional_requirements": re.compile(r"^FR-\d{3}$"),
    "quality_requirements": re.compile(r"^NFR-\d{3}$"),
}
WEAK_WORDS = [
    "fast", "quick", "user-friendly", "easy to use", "state of the art",
    "as required", "if possible", "etc.", "and so on", "robust", "flexible",
    "modern", "efficiently", "appropriate", "sufficient",
]

findings: list[str] = []


def finding(req_id: str, check: str, message: str) -> None:
    findings.append(f"[{check}] {req_id}: {message}")


def weak_wording(text: str) -> list[str]:
    lowered = text.lower()
    return [w for w in WEAK_WORDS if w in lowered]


def main() -> int:
    data = yaml.safe_load(REGISTER.read_text(encoding="utf-8"))

    brs = {r["id"]: r for r in data.get("business_requirements", [])}
    frs = data.get("functional_requirements", [])
    nfrs = data.get("quality_requirements", [])
    derived = frs + nfrs

    # --- 1. ID format and uniqueness -------------------------------------
    seen: set[str] = set()
    for section, pattern in ID_PATTERNS.items():
        for req in data.get(section, []):
            rid = req.get("id", "<missing id>")
            if not pattern.match(str(rid)):
                finding(rid, "id-format", f"does not match {pattern.pattern}")
            if rid in seen:
                finding(rid, "id-unique", "duplicate identifier")
            seen.add(rid)

    # --- 2. status / priority --------------------------------------------
    for req in list(brs.values()) + derived:
        rid = req.get("id", "?")
        if req.get("status") not in STATUSES:
            finding(rid, "status", f"unknown status {req.get('status')!r}")
        if req.get("priority") not in PRIORITIES:
            finding(rid, "priority", f"unknown priority {req.get('priority')!r}")

    # --- 3/4/6/7/9. derived requirement rules -----------------------------
    realised: set[str] = set()
    for req in derived:
        rid = req["id"]
        parents = req.get("parents") or []
        if not parents:
            finding(rid, "traceability", "no parent business requirement")
        for parent in parents:
            realised.add(parent)
            if parent not in brs:
                finding(rid, "traceability", f"parent {parent} does not exist")
            elif req.get("status") == "baselined" and brs[parent].get("status") == "draft":
                finding(rid, "baseline", f"baselined but parent {parent} is still draft")

        if not req.get("acceptance"):
            finding(rid, "verifiable", "no acceptance criterion")
        if not req.get("verification"):
            finding(rid, "verifiable", "no verification / test case named")

        haystack = " ".join([req.get("title", "")] + list(req.get("acceptance") or []))
        for word in weak_wording(haystack):
            finding(rid, "wording", f"weak wording {word!r}")

    # --- 5. orphan business requirements ----------------------------------
    for rid in brs:
        if rid not in realised:
            finding(rid, "orphan", "no functional or quality requirement realises this goal")

    # --- 8. business requirement completeness ------------------------------
    for rid, req in brs.items():
        for field in ("metric", "target", "verification"):
            if not req.get(field):
                finding(rid, "measurable", f"missing {field}")

    # --- report ------------------------------------------------------------
    total = len(brs) + len(derived)
    print(f"PRISMA requirement register — {REGISTER.relative_to(REGISTER.parents[2])}")
    print(f"  business requirements : {len(brs)}")
    print(f"  functional            : {len(frs)}")
    print(f"  quality               : {len(nfrs)}")
    print(f"  total checked         : {total}")
    print()

    if findings:
        print(f"{len(findings)} finding(s):\n")
        for f in findings:
            print("  " + f)
        return 1

    print("No findings. Register is internally consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
