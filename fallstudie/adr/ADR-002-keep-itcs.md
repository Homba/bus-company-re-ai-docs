# ADR-002 — Keep the ITCS as the source of vehicle data

**Status:** accepted (2026-02-19) · **Deciders:** STK-01, STK-05, STK-12

## Context

The ITCS is 15 years old and its vendor supports the version only under an extended
agreement. Replacing it would solve several problems at once — and would consume the entire
CON-08 budget three times over, with a multi-year timeline that leaves the FOT finding
(BR-03) open in the meantime.

## Decision

PRISMA consumes vehicle position and trip progress from the existing ITCS through its
documented VDV 453 subscription and does not implement vehicle localisation. The ITCS
replacement is a separate programme.

## Consequences

**Positive** — Delivers BR-03 within the budget and before the next FOT review.

**Negative** — PRISMA inherits the ITCS's data quality, which is the reason for RSK-01 and for
the sprint-0 data assessment. Estimate quality (NFR-004) is bounded by an input PRISMA does
not control; FR-004 and NFR-005 exist so that the system is honest about this rather than
hiding it.

**Follow-up** — The hub boundary (ADR-001) is drawn so that a future ITCS replacement changes
one input adapter, not the distribution layer.
