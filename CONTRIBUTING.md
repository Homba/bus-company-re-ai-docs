# Contributing to the PRISMA requirements

## Before you write a requirement

1. Read `docs/03-glossary.md`. Most review findings in this project are terminology, not logic.
2. Find the business requirement your idea serves. If there is none, you are proposing a
   business requirement — say so, and expect it to go to the sponsor, not to the backlog.
3. Check `docs/09-constraints-and-compliance.md`. A requirement that violates a constraint is
   a change request to the constraint owner, not a requirement.

## Workflow

```
issue (FR / NFR / CR form)
   → discussion and refinement
   → branch  req/FR-0xx-short-title
   → edit docs/ and requirements/requirements.yaml together
   → run tools/validate_requirements.py
   → pull request with the quality checklist
   → peer review, then walkthrough if it is a new use case or FR block
```

## Local checks

```bash
python3 -m pip install pyyaml
python3 tools/validate_requirements.py
```

To see the validator do its job, temporarily delete the `parents:` line from any FR and run it
again — it should report a traceability finding and exit non-zero. This is the same check CI runs.

## Style rules

- One requirement per statement. If you wrote "and also", split it.
- `shall` for binding, `should` for desirable, `may` for optional. Nothing else.
- No product or technology names in FR/NFR text — CON-01 requires vendor neutrality.
- Numbers belong in requirements, adjectives do not. "Fast" is a review finding.
- Never renumber. A superseded requirement keeps its ID and points to its successor.
- Keep German as the language of record (CON-09); if the English and German texts diverge,
  the German wins and the English is corrected.

## Branch naming

| Kind | Pattern |
|---|---|
| New or changed requirement | `req/FR-014-correct-and-cancel` |
| Change request | `cr/CR-07-retention-five-years` |
| Documentation only | `docs/glossary-countdown` |
| Tooling | `tools/validator-weak-wording` |

## Review expectations

A reviewer is expected to check the ten quality criteria in
`docs/12-review-and-change-process.md`, not just readability. "LGTM" on a requirement PR is
not a review.
