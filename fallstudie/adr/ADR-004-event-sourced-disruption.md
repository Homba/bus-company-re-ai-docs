# ADR-004 — Disruption as an event-sourced aggregate

**Status:** accepted (2026-03-04) · **Deciders:** technical lead, STK-05

## Context

BR-09 requires reconstruction of what was communicated on which channel at which time, for
three years, including corrections and cancellations (UC-003, UC-007). NFR-016 requires the
audit trail to be append-only.

## Decision

The disruption aggregate is stored as an ordered sequence of domain events (created,
approved, released, published-to-channel, correction-applied, cancelled). The current state is
a projection. Channel publications are events too, including failures and retries.

## Consequences

**Positive** — FR-027, FR-028 and NFR-016 fall out of the storage model rather than being
bolted on. Idempotency (NFR-008) is checkable against the event log.

**Negative** — Deletion for data protection (NFR-013) is harder in an append-only store;
requires a crypto-shredding or projection-rebuild strategy, which must be designed before the
DPIA is submitted (CON-06). Raised as a task, not an open point, because the DPIA depends on it.
