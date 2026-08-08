# UC-007 — Reconstruct communication history for an audit

**Primary actor:** Compliance officer · **Level:** user goal · **Status:** draft · **Traces to:** BR-09, BR-10

**Main success scenario**
1. Officer selects a time range and optionally a line or stop.
2. PRISMA lists all disruptions with every version, release, correction and cancellation.
3. For each, PRISMA shows per channel: what was sent, at what time, with what acknowledgement.
4. Officer exports the result as a signed PDF/A and a CSV.

**Constraints**
- Retention 3 years (BR-09); export contains no personal data of drivers (BR-10, CON-07).
- Access requires role `prisma.auditor`; every export is itself logged.
