# ADR-003 — Translation inside the cantonal cloud boundary

**Status:** proposed · **Deciders:** STK-05, STK-11, STK-03 · **Relates to:** RSK-04, CON-04, CON-06

## Context

BR-07 requires four languages within 60 s of release without dispatcher effort. The obvious
approach is a managed translation service, but CON-04 restricts the solution to the approved
cantonal cloud catalogue, and CON-06 raises questions about sending operational content to a
service outside the boundary.

## Options

1. **Managed external translation service** — best quality, fails CON-04 as the catalogue
   stands today, requires a data protection assessment.
2. **Self-hosted translation model inside the boundary** — satisfies CON-04 and CON-06, higher
   operating cost, quality must be measured against the template catalogue.
3. **Pre-translated template catalogue with a translated free-text slot only** — deterministic,
   auditable, cheapest; limits expressiveness and needs a translation workflow for new templates.

## Proposed decision

Option 3 as the baseline, with option 2 as an enhancement for the free-text slot. Rationale:
FR-008 already bounds free text to 240 characters, so the translated surface is small; a
deterministic catalogue is also easier to defend in an audit (BR-09) and removes RSK-03's
worst case, where a generated translation changes the operational meaning of a message.

## Consequences

Requires a template governance owner — this is exactly OPN-02, which must be closed before
this ADR can be accepted.
