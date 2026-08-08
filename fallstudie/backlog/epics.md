# Epics

Epics group the FRs into deliverable slices. Each epic names the FRs it satisfies, so the
traceability from business goal to sprint work is unbroken.

| Epic | Covers | Value delivered when done | Target increment |
|---|---|---|---|
| E1 — Real-time backbone | FR-001…FR-006 | Estimates exist and are honest about their age | Sprint 1–3 |
| E2 — Author once | FR-007, FR-008, FR-009, FR-015 | A dispatcher can produce a correct draft in under a minute | Sprint 2–4 |
| E3 — Release and distribute | FR-010, FR-011, FR-012, FR-018, NFR-008 | One release reaches every channel — the core of BR-01 | Sprint 4–6 |
| E4 — Stop displays | FR-016, FR-017, FR-019, FR-030 | 61 existing displays fed from PRISMA | Sprint 5–7 |
| E5 — National platform feed | FR-024, FR-025, FR-026, NFR-018 | FOT finding closed | Sprint 6–8 |
| E6 — Correct and cancel | FR-014, FR-019 | Wrong information can be fixed, not just added to | Sprint 7–8 |
| E7 — Accessibility and language | FR-011, FR-013, FR-021, NFR-011, NFR-012 | Passenger information usable by everyone in four languages | Sprint 3–9, continuous |
| E8 — Audit and reporting | FR-027, FR-028, FR-029, NFR-016 | Three-year reconstruction possible; DPIA satisfiable | Sprint 8–10 |
| E9 — Service desk | FR-022, FR-023 | Agents see what the passenger sees | Sprint 9–10 |

## Sequencing rationale

E1 first because everything downstream is worthless if the estimates are wrong — and because
RSK-01 (ITCS data quality) must be resolved before the team commits to NFR-004. E5 is pulled
earlier than its business priority would suggest, because BR-03 is a regulatory finding with
an external deadline. E7 runs across the whole programme rather than as a phase, because
retro-fitting accessibility is the classic cause of RSK-06.
