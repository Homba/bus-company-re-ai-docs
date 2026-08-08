# Traceability Matrix

Maintained in `requirements/requirements.yaml` and rendered here.
`tools/validate_requirements.py` fails the build if a requirement listed here has no parent,
no acceptance criterion, or no verification method.

## 1. Business requirement → functional / quality requirements

| BR | Title | Realised by | Verified by |
|---|---|---|---|
| BR-01 | Single authoritative record | FR-007, FR-008, FR-009, FR-010, FR-012, FR-014, FR-015, NFR-008 | TC-01, TC-07, TC-12 |
| BR-02 | Speed to passenger | FR-001…FR-006, FR-018, FR-019, NFR-001, NFR-003, NFR-004, NFR-005 | TC-02, TC-03, TC-14 |
| BR-03 | Concession-compliant delivery | FR-009, FR-012, FR-024, FR-025, FR-026, NFR-007, NFR-018 | TC-04, TC-15 |
| BR-04 | Lower authoring effort | FR-007, FR-008, NFR-002 | TC-05, time study |
| BR-05 | Wider coverage | FR-003, FR-016, FR-017, FR-020, FR-030, NFR-003, NFR-017 | TC-06, TC-16 |
| BR-06 | Equal access | FR-013, FR-021, NFR-011, NFR-012, NFR-015 | TC-08, external audit |
| BR-07 | Multilingual | FR-008, FR-011, FR-020, NFR-006 | TC-09 |
| BR-08 | Fewer complaints | FR-019, FR-022, FR-023, NFR-005, NFR-015 | TC-10, complaint report |
| BR-09 | Auditable history | FR-023, FR-027, FR-028, NFR-009, NFR-010, NFR-013, NFR-016 | TC-11, audit exercise |
| BR-10 | No covert monitoring | FR-029, NFR-013, NFR-014 | DPIA, schema inspection |

**Check: no orphans.** Every FR-001…FR-030 and NFR-001…NFR-019 appears at least once above.

## 2. Use case → functional requirements

| UC | FRs exercised |
|---|---|
| UC-001 Author | FR-007, FR-008, FR-009, FR-015 |
| UC-002 Release and publish | FR-010, FR-011, FR-012, FR-018, FR-024, FR-027, NFR-001, NFR-008 |
| UC-003 Correct / cancel | FR-014, FR-018, FR-019, FR-027 |
| UC-004 Stop display | FR-016, FR-017, FR-019, FR-021, NFR-005 |
| UC-005 National platform | FR-024, FR-025, FR-026, NFR-007, NFR-018 |
| UC-006 Service desk | FR-022, FR-023 |
| UC-007 Audit | FR-027, FR-028, NFR-016 |

## 3. Constraint → affected requirements

| CON | Affects |
|---|---|
| CON-02 | FR-012, UC-002/6a |
| CON-03 | FR-013, FR-021, NFR-011, NFR-012 |
| CON-04 | NFR-019, ADR-003 |
| CON-05 | FR-003, FR-004, ADR-002 |
| CON-06 | NFR-013, NFR-014 |
| CON-07 | FR-029, NFR-014, BR-10 |
| CON-11 | FR-024, FR-025, FR-026, NFR-018 |
| CON-12 | NFR-002 |

## 4. Test case index

| TC | Scope | Type |
|---|---|---|
| TC-01 | One disruption, all channels, content identical | integration |
| TC-02 | Publication latency under peak profile | performance |
| TC-03 | Estimate recalculation on ITCS update | integration |
| TC-04 | SIRI conformance suite | conformance |
| TC-05 | Three-interaction release path | usability |
| TC-06 | Departure ordering and countdown rendering | unit + integration |
| TC-07 | Approval rule per severity | unit |
| TC-08 | Screen-reader task success | usability |
| TC-09 | Four-language generation within 60 s | integration |
| TC-10 | Staleness indicator on lost channel | fault injection |
| TC-11 | Audit reconstruction of 20 historic disruptions | acceptance |
| TC-12 | Correction propagates only to holding channels | integration |
| TC-14 | Estimate marked stale after 90 s silence | unit |
| TC-15 | Heartbeat and re-subscription | integration |
| TC-16 | Add 5 displays by configuration only | acceptance |
