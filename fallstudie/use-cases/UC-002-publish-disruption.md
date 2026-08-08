# UC-002 — Release and publish a disruption

| | |
|---|---|
| **ID** | UC-002 |
| **Goal level** | User goal (sea level) |
| **Primary actor** | Dispatcher (P1 Nadia, STK-02) |
| **Supporting actors** | Duty officer, translation service, channel adapters |
| **Stakeholders and interests** | Passenger: correct information fast. Operations: liability-safe wording. FOT: standard-conformant feed. |
| **Trigger** | The dispatcher has a drafted disruption (UC-001) and decides it must reach passengers |
| **Status** | baselined |
| **Traces to** | BR-01, BR-02, BR-04, BR-07, BR-09 |

## Preconditions

1. The dispatcher is authenticated with role `prisma.dispatcher` (IF-08).
2. A disruption exists in status `draft` with mandatory fields complete: severity, cause,
   affected area, validity start, German source text.
3. At least one channel adapter reports status `available`.

## Success guarantee (postcondition)

1. The disruption has status `published`.
2. Localised messages exist in DE, FR, IT, EN.
3. Every channel selected by the severity rule has either confirmed receipt or been recorded
   as failed with a retry scheduled.
4. An immutable audit entry records who released what, when, to which channels.

## Minimal guarantee

The disruption remains in a consistent status, and any partial publication is recorded and
visible to the dispatcher. No channel holds a message that PRISMA does not know about.

## Main success scenario

| # | Actor | Step |
|---|---|---|
| 1 | Dispatcher | Opens the drafted disruption and selects *Release*. |
| 2 | PRISMA | Validates completeness and the validity period against the current time. |
| 3 | PRISMA | Determines the required approval level from the severity rule (FR-010). |
| 4 | PRISMA | Severity is `minor`: no second approval required. |
| 5 | PRISMA | Generates the localised messages for DE, FR, IT, EN from the structured content (FR-011). |
| 6 | PRISMA | Determines the target channels from severity and affected area (FR-012). |
| 7 | PRISMA | Renders each message into the channel-specific shape: display banner, app payload, web item, SIRI-SX situation, desk view. |
| 8 | PRISMA | Transmits to each channel adapter and collects acknowledgements. |
| 9 | PRISMA | Sets status to `published` and writes the audit entry. |
| 10 | PRISMA | Shows the dispatcher a publication summary with per-channel state and timestamps. |

## Alternate flows

**3a — Severity is `major` or `severe`**
1. PRISMA sets status `awaiting_approval` and notifies the duty officer.
2. Duty officer approves → continue at step 5.
3. Duty officer rejects with a comment → status returns to `draft`, dispatcher is notified. Use case ends.
4. No decision within 4 minutes → PRISMA escalates to the second duty officer and marks the delay in the audit trail.

**5a — Automatic translation is unavailable**
1. PRISMA publishes the German message immediately to all channels.
2. PRISMA marks the other languages as `pending` and retries every 30 s for 10 minutes.
3. If still unavailable, PRISMA publishes the pre-translated template sentence without the
   free-text slot and flags the disruption for manual translation.
   *Rationale: partial information beats none — see NFR-006.*

**6a — Dispatcher overrides the channel selection**
1. Dispatcher deselects a channel with a mandatory reason from a fixed list.
2. Override and reason are written to the audit entry. Continue at step 7.
   *Constraint: the national platform channel cannot be deselected (CON-02).*

## Exception flows

**8a — A channel adapter does not acknowledge within 20 s**
1. PRISMA marks the channel `failed`, retries with exponential backoff for 15 minutes.
2. The publication summary shows the failure; the disruption still reaches status `published`
   if at least one channel succeeded.
3. If all channels fail, status becomes `publication_failed` and an alarm is raised to IT
   Operations (STK-05).

**2a — Validity period already ended**
PRISMA refuses the release and states which field is invalid. Status stays `draft`.

**\*a — Loss of the dispatcher's session at any step**
The disruption is preserved with its last consistent status. On re-authentication the
dispatcher sees the disruption and its publication state.

## Non-functional expectations touching this use case

| ID | Expectation |
|---|---|
| NFR-001 | Steps 2–10 complete within 20 s at the 95th percentile |
| NFR-002 | The release action requires at most three interactions from the open disruption |
| NFR-008 | Publication is idempotent — a repeated release produces no duplicate on any channel |
| NFR-013 | The audit entry is append-only and retained for 3 years (BR-09) |

## Open points

- OPN-04: does a `severe` disruption need approval when the duty officer *is* the author?
