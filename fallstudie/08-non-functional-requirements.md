# Non-Functional Requirements

Grouped along ISO/IEC 25010 product quality characteristics. Every NFR states a **measure**,
a **target value** and a **verification method** — an NFR without those three is a wish, not a
requirement, and does not pass review here.

Status: baselined v1.2

---

## Performance efficiency

**NFR-001 — Publication latency**
*Measure:* Time from the release (or approval) action to the last channel acknowledgement.
*Target:* ≤ 10 s median, ≤ 20 s at the 95th percentile, under peak load per NFR-003.
*Verification:* Load test before go-live; continuous measurement in production.
*Parent:* BR-02

**NFR-002 — Authoring interaction cost**
*Measure:* Number of interactions (clicks or keystrokes-with-intent) from an open draft to
released, for a template-based disruption.
*Target:* ≤ 3.
*Verification:* Task analysis on the delivered UI, plus timing in the BR-04 time study.
*Parent:* BR-04

**NFR-003 — Peak load**
*Measure:* Sustained throughput without violating NFR-001.
*Target:* 412 stops served, 1 800 concurrent app queries per second, 40 disruption state
changes per minute, 3 000 running-trip estimates recalculated per minute.
*Verification:* Load test with the peak profile of 2025-12-08 (snow event) multiplied by 1.5.
*Parent:* BR-02, BR-05

**NFR-004 — Estimate freshness**
*Measure:* Age of the underlying ITCS data behind a published estimate.
*Target:* ≤ 30 s at the 95th percentile.
*Verification:* End-to-end timestamp tracing in production monitoring.
*Parent:* BR-02

## Reliability

**NFR-005 — Honest degradation**
*Measure:* Behaviour when input data is stale or a channel is unreachable.
*Target:* No countdown is displayed from data older than 120 s; a staleness indicator replaces
it. Zero occurrences of a displayed countdown based on data older than 120 s.
*Verification:* Fault injection test; production alarm on any violation.
*Parent:* BR-02, BR-08
*Rationale:* A wrong countdown damages trust more than an absent one. This came out of every
passenger interview.

**NFR-006 — Partial availability**
*Measure:* System behaviour when a subsystem fails.
*Target:* Failure of the translation service, of one channel adapter, or of the reporting
component must not prevent publication to the remaining channels.
*Verification:* Chaos test per subsystem before go-live.
*Parent:* BR-02, BR-07

**NFR-007 — Availability**
*Measure:* Monthly availability of the publication path, service window 04:00–01:30.
*Target:* ≥ 99.7 % for the publication path; ≥ 99.5 % for the national platform feed (IF-06);
≥ 99.0 % for the service-desk view.
*Verification:* Monitoring report, monthly.
*Parent:* BR-03

**NFR-008 — Idempotent publication**
*Measure:* Effect of a repeated or retried publication of the same disruption version.
*Target:* Exactly one message per channel per disruption version; zero duplicates.
*Verification:* Integration test with forced retries.
*Parent:* BR-01

**NFR-009 — Recovery**
*Measure:* RTO and RPO for the publication path.
*Target:* RTO ≤ 30 min, RPO ≤ 60 s.
*Verification:* Documented restore exercise, twice a year.
*Parent:* BR-03, BR-09

## Security

**NFR-010 — Authentication and authorisation**
*Measure:* Enforcement of the role model via IF-08.
*Target:* Every state-changing operation requires an authenticated principal with the
matching role; 100 % of operations covered by an authorisation test.
*Verification:* Security test report; penetration test before go-live.
*Parent:* BR-09

**NFR-016 — Audit integrity**
*Measure:* Mutability of audit entries.
*Target:* Append-only storage; any modification attempt is detectable; retention 3 years.
*Verification:* Storage design review plus tamper test.
*Parent:* BR-09

## Usability and accessibility

**NFR-011 — Accessibility conformance**
*Measure:* Conformance of all passenger-facing digital output to the applicable accessibility
standard at level AA, and to the federal accessibility requirements for public bodies.
*Target:* Full conformance, no unresolved level-A or level-AA findings.
*Verification:* External audit signed off by STK-15 before go-live; automated checks in CI.
*Parent:* BR-06

**NFR-012 — Assistive technology task success**
*Measure:* Task success rate for "find the next departure of my line" and "understand today's
disruption on my line" using a screen reader.
*Target:* ≥ 90 % success with ≥ 8 participants who use assistive technology daily.
*Verification:* Moderated usability test.
*Parent:* BR-06
*Note:* Live regions must be `polite`, not `assertive` — otherwise a 30 s refresh restarts the
announcement (finding from P3 interview).

**NFR-015 — Comprehensibility**
*Measure:* Readability level of the plain-language message variant.
*Target:* B1 or simpler, verified by a readability metric plus review by two non-expert readers.
*Verification:* Sample of 30 generated messages per release.
*Parent:* BR-06, BR-08

## Maintainability and portability

**NFR-017 — Channel extensibility**
*Measure:* Effort to add a new channel endpoint of an existing type.
*Target:* Configuration only, no deployment, ≤ 30 min by an administrator.
*Verification:* Demonstrated in acceptance test by adding 5 stop displays.
*Parent:* BR-05

**NFR-018 — Standard conformance testability**
*Measure:* Ability to re-run the platform operator's conformance suite.
*Target:* Suite runs in CI against a staging endpoint; green before every IF-06 release.
*Verification:* CI pipeline evidence.
*Parent:* BR-03

**NFR-019 — Deployment environment**
*Measure:* Where the solution runs.
*Target:* Operable in the cantonal government cloud with the platform services available there;
no dependency on a service outside the approved catalogue.
*Verification:* Architecture review with STK-05 and the cantonal cloud team.
*Parent:* CON-04

## Data protection

**NFR-013 — Retention and deletion**
*Measure:* Storage duration per data category.
*Target:* Audit entries 3 years; raw vehicle positions 24 h; aggregated KPIs 5 years;
app subscription data deleted 90 days after last use.
*Verification:* Data lifecycle review by STK-11; automated deletion job evidence.
*Parent:* BR-09, BR-10, CON-06

**NFR-014 — Purpose limitation for vehicle data**
*Measure:* Presence of driver-identifying or duty-identifying attributes in stored or exported data.
*Target:* Zero, outside the 24 h operational window.
*Verification:* Schema inspection and export sampling by STK-11 and STK-13.
*Parent:* BR-10
