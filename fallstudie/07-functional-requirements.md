# Functional Requirements

Status: baselined v1.4 for FR-001…FR-023; FR-024…FR-030 in review.

Sentence pattern: `<condition> the system shall <verb> <object> <detail>`.
`shall` = binding. `should` = desirable, may be traded off. `may` = optional.
Every FR names its parent BR and at least one acceptance criterion.

---

## A. Master data and real-time input

**FR-001** — The system shall import planned timetable data via IF-02 in NeTEx format at
least once per day.
*Parent:* BR-02 · *Priority:* must
*Acceptance:* Given a valid NeTEx file placed at 02:00, when the import runs, then all trips
for the following 14 days are available in PRISMA before 02:30 and the import result is logged.

**FR-002** — The system shall reject a timetable import that fails schema validation, retain
the previously valid dataset, and alert IT Operations within 5 minutes.
*Parent:* BR-02 · *Priority:* must
*Acceptance:* Given a malformed file, when the import runs, then no existing data is
overwritten and an alert is raised.

**FR-003** — The system shall subscribe to vehicle position and trip progress data from the
ITCS via IF-01 and process updates at least every 10 seconds.
*Parent:* BR-02, BR-05 · *Priority:* must

**FR-004** — When ITCS data for a running trip has not been received for more than 90 seconds,
the system shall mark that trip's estimates as stale.
*Parent:* BR-02 · *Priority:* must
*Acceptance:* Given a trip whose last update is 91 s old, when a consumer requests departures,
then the response marks the estimate as stale with the age in seconds.

**FR-005** — The system shall calculate an estimated departure time per trip and stop from
planned times and current trip progress.
*Parent:* BR-02 · *Priority:* must

**FR-006** — The system shall recalculate estimates within 5 seconds of receiving new trip
progress data.
*Parent:* BR-02 · *Priority:* must

## B. Disruption authoring

**FR-007** — The system shall allow an authenticated dispatcher to create a disruption with
the mandatory attributes: cause, severity, affected area, validity start, source text.
*Parent:* BR-01, BR-04 · *Priority:* must · *Use case:* UC-001

**FR-008** — The system shall offer message templates per cause, with a bounded free-text slot
of at most 240 characters.
*Parent:* BR-04, BR-07 · *Priority:* must
*Acceptance:* Given a selected cause, when the dispatcher opens the text field, then the
template is pre-filled and the free-text slot enforces the character limit with a live counter.

**FR-009** — The system shall restrict the cause attribute to the standardised taxonomy
defined in the glossary and shall not accept free-text causes.
*Parent:* BR-01, BR-03 · *Priority:* must
*Rationale:* SIRI-SX conformance in IF-06 requires coded reasons.

**FR-010** — The system shall require approval by a duty officer before publishing a
disruption of severity `major` or `severe`, and shall not require approval for `information`
or `minor`.
*Parent:* BR-01 · *Priority:* must · *Use case:* UC-002, flow 3a

**FR-011** — On release, the system shall generate localised messages in German, French,
Italian and English from the structured content within 60 seconds.
*Parent:* BR-07 · *Priority:* must
*Acceptance:* Given a released disruption, when 60 s have passed, then messages in all four
languages exist or the fallback of UC-002 flow 5a has been applied and flagged.

**FR-012** — The system shall determine the target channels from severity and affected area
according to the channel matrix, and shall allow the dispatcher to deselect channels other
than the national platform, with a mandatory reason.
*Parent:* BR-01, BR-03 · *Priority:* must

**FR-013** — The system shall produce, for every disruption, a plain-language variant not
exceeding language level B1 for use by screen readers and audio channels.
*Parent:* BR-06 · *Priority:* should

**FR-014** — The system shall allow correction and cancellation of a published disruption and
shall propagate the change to exactly those channels currently holding the message.
*Parent:* BR-01, BR-02 · *Priority:* must · *Use case:* UC-003

**FR-015** — Where a channel imposes a length limit, the system shall shorten the message
according to the channel's truncation rule and shall show the dispatcher the resulting text
before release.
*Parent:* BR-01 · *Priority:* must

## C. Distribution

**FR-016** — The system shall deliver departure rows for a stop to the display adapter,
ordered by estimated departure time.
*Parent:* BR-05 · *Priority:* must · *Use case:* UC-004

**FR-017** — The system shall express the countdown in whole minutes up to 59 minutes and as a
clock time beyond that.
*Parent:* BR-05 · *Priority:* must
*Acceptance:* Given an estimate 61 minutes ahead, when the row is rendered, then a clock time
is shown, not "61".

**FR-018** — The system shall push a disruption to all selected channels within 10 seconds of
release or approval.
*Parent:* BR-02 · *Priority:* must

**FR-019** — When a channel has not acknowledged an update for longer than the channel's
freshness threshold, the system shall instruct that channel to display a staleness indicator.
*Parent:* BR-02, BR-08 · *Priority:* must · *Use case:* UC-004 exception

**FR-020** — The system shall provide a query interface returning departures and active
disruptions filtered by stop, line and language.
*Parent:* BR-05, BR-07 · *Priority:* must

**FR-021** — The system shall provide every passenger-facing text as machine-readable text and
shall not deliver information exclusively as an image.
*Parent:* BR-06 · *Priority:* must

**FR-022** — The system shall provide a service-desk view showing, per line or stop, the
current content of each channel.
*Parent:* BR-08 · *Priority:* should · *Use case:* UC-006

**FR-023** — The system shall hold internal-only annotations on a disruption that are
excluded from all passenger channels by the data model.
*Parent:* BR-08, BR-09 · *Priority:* must

## D. Interoperability

**FR-024** — The system shall serve SIRI-SX situation exchange to subscribed consumers and
push an update within 10 seconds of any disruption state change.
*Parent:* BR-03 · *Priority:* must · *Use case:* UC-005 · *Status:* review

**FR-025** — The system shall serve SIRI-ET estimated timetable updates at least every 30
seconds for all currently running trips.
*Parent:* BR-03 · *Priority:* must · *Status:* review

**FR-026** — The system shall answer subscription heartbeat requests within 5 seconds and
shall re-establish a subscription after three consecutive missed heartbeats.
*Parent:* BR-03 · *Priority:* must · *Status:* review

## E. Audit, reporting, administration

**FR-027** — The system shall write an append-only audit entry for every creation, approval,
release, correction, cancellation and publication attempt, recording actor, timestamp,
channel and outcome.
*Parent:* BR-09 · *Priority:* must · *Status:* review

**FR-028** — The system shall allow an authorised auditor to retrieve the complete
communication history of any disruption within the retention period and to export it.
*Parent:* BR-09 · *Priority:* must · *Status:* review

**FR-029** — The system shall aggregate vehicle-derived data before it enters the reporting
data mart such that no individual driver or vehicle duty can be identified.
*Parent:* BR-10 · *Priority:* must · *Status:* review

**FR-030** — The system shall allow an administrator to add a channel endpoint and assign it
to stops or lines without a software deployment.
*Parent:* BR-05 · *Priority:* should · *Status:* review
*Rationale:* Makes the 45 % → 100 % coverage path in BR-05 a configuration task.

---

## Channel matrix (referenced by FR-012)

| Severity | Stop display | App push | App list | Website | National platform | Service desk |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| `information` | – | – | ✓ | ✓ | ✓ | ✓ |
| `minor` | ✓ | – | ✓ | ✓ | ✓ | ✓ |
| `major` | ✓ | ✓ affected lines | ✓ | ✓ | ✓ | ✓ |
| `severe` | ✓ all stops on line | ✓ all subscribers | ✓ | ✓ front page | ✓ | ✓ + alert |
