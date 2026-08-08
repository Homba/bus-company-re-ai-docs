# ADR-001 — Channel-agnostic distribution hub

**Status:** accepted (2026-03-04) · **Deciders:** STK-03, STK-05, technical lead

## Context

Today each passenger channel is fed by a separate manual path, which is the direct cause of
BR-01 and BR-04. BR-05 additionally requires that adding stops does not require software
change, and OPN-05 raises the possibility of on-board announcements as a further channel.

## Decision

A disruption is published once to an internal distribution hub. Channel adapters subscribe to
the hub and translate the canonical message into channel-specific shape. Adding a channel
endpoint is configuration; adding a channel *type* is one new adapter.

## Consequences

**Positive** — FR-012, FR-030, NFR-017 become straightforward. A new channel does not touch
the authoring path. Consistency (BR-01) is structural, not procedural.

**Negative** — Introduces an asynchronous hop, which pushes NFR-001 to be specified end-to-end
rather than per component. Per-channel failure handling becomes explicit work (UC-002/8a).

**Neutral** — Requires the publication to be idempotent (NFR-008), since retries are now normal.
