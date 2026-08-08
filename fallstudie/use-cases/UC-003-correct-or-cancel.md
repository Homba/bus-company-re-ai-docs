# UC-003 — Correct or cancel a published disruption

**Primary actor:** Dispatcher · **Level:** user goal · **Status:** approved · **Traces to:** BR-01, BR-02, BR-09

**Trigger:** The situation changes, or the published information turns out to be wrong.

**Main success scenario**
1. Dispatcher opens a `published` disruption and chooses *Correct* or *Cancel*.
2. For a correction: dispatcher edits the changed fields; PRISMA shows a diff against what is
   currently published.
3. PRISMA requires a change reason from a fixed list (`situation_changed`, `error_correction`,
   `duplicate`, `resolved_early`).
4. PRISMA regenerates the localised messages and republishes to exactly the channels that
   currently hold the message.
5. For a cancellation: PRISMA sends a withdrawal to every channel holding the message and sets
   status `cancelled`.
6. PRISMA writes a new audit entry linked to the original; the previous version stays retrievable.

**Alternate flow**
- 4a. A channel no longer applies after the correction (e.g. the affected area shrank) →
  PRISMA sends a withdrawal to that channel and a new message to the newly affected ones.

**Exception flow**
- 5a. A stop display cannot be reached → the withdrawal is queued; the display shows a
  staleness indicator after the freshness threshold expires (NFR-005, FR-019).

**Business rule:** A `severe` disruption may only be cancelled by a duty officer.
