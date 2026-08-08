# Risks, Assumptions and Open Points

## 1. Risks

Exposure = probability × impact, both 1–5.

| ID | Risk | P | I | Exp | Response | Owner | Status |
|---|---|:--:|:--:|:--:|---|---|---|
| RSK-01 | ITCS data quality is worse than assumed; estimates unusable on some lines | 4 | 5 | 20 | Mitigate — data quality assessment on 6 lines in sprint 0 before committing to NFR-004 | STK-03 | open |
| RSK-02 | ITCS vendor bills interface support as change requests, eroding the budget | 3 | 4 | 12 | Transfer — fixed-price interface support clause negotiated before tender | STK-01 | mitigating |
| RSK-03 | Automatic translation produces wording that is legally or operationally misleading | 3 | 4 | 12 | Mitigate — bounded free-text slot, reviewed template catalogue, human review flag for `severe` | STK-04 | mitigating |
| RSK-04 | Cantonal cloud service catalogue lacks a suitable translation service | 3 | 3 | 9 | Mitigate — ADR-003 evaluates on-premise alternative early | STK-05 | open |
| RSK-05 | Works council withholds agreement, blocking use of vehicle data | 2 | 5 | 10 | Avoid — early consultation, purpose limitation written into BR-10 and NFR-014 | STK-01 | mitigating |
| RSK-06 | Accessibility audit fails late, delaying go-live past the CON-10 freeze | 3 | 4 | 12 | Mitigate — accessibility checks in CI from sprint 1, pre-audit at 60 % feature completion | STK-03 | open |
| RSK-07 | Display adapter for the 2009 hardware proves unreliable at scale | 3 | 3 | 9 | Mitigate — adapter load test with 60 real displays in the pilot | STK-05 | open |
| RSK-08 | Dispatchers keep using the old channels in parallel out of habit | 3 | 3 | 9 | Mitigate — old channels decommissioned at pilot end; training per CON-12 | STK-01 | open |
| RSK-09 | Peak-load profile underestimated; snow events exceed NFR-003 | 2 | 4 | 8 | Mitigate — 1.5× margin already in NFR-003; autoscaling verified in load test | STK-05 | accepted |
| RSK-10 | Scope creep from municipalities wanting local display features | 3 | 2 | 6 | Control — change process in doc 12; municipality requests routed via STK-08 | STK-03 | open |

## 2. Assumptions

| ID | Assumption | If false | Validated by |
|---|---|---|---|
| ASM-01 | The ITCS VDV 453 interface remains available unchanged for the project duration | FR-003 must be re-specified; major cost impact | Written confirmation from STK-12, obtained 2026-02-14 |
| ASM-02 | Timetable master data is complete and correct for all 38 lines | Import rules need cleansing logic; effort +15 % | Data profiling in sprint 0 |
| ASM-03 | 61 existing displays can be driven through an adapter without hardware change | Coverage target in BR-05 unreachable within CON-08 | Adapter proof of concept, sprint 1 |
| ASM-04 | The national platform's SIRI profile does not change before go-live | Rework of FR-024…FR-026 | Interface agreement with STK-10 |
| ASM-05 | Four languages suffice; no Romansh requirement in the concession area | FR-011 extension | Checked with STK-08, 2026-01-22 |
| ASM-06 | Cantonal IAM can issue the four PRISMA roles | Own role management needed; security review impact | Canton IT confirmation pending |

## 3. Open points

| ID | Question | Needed by | Owner | Status |
|---|---|---|---|---|
| OPN-01 | Is a Romansh variant needed if the canton extends the concession area? | Before FR-011 baseline | STK-08 | open |
| OPN-02 | Who owns the message template catalogue after go-live — comms or operations? | Before go-live | STK-01 | open |
| OPN-03 | Which 45 % of stops are in scope for display rollout, and by what criterion? | Before pilot | STK-08 / STK-14 | in progress |
| OPN-04 | Does a `severe` disruption need approval when the duty officer authored it? | Before FR-010 implementation | STK-02 | open |
| OPN-05 | Are on-board announcements a phase 2 channel, and does that change the API now? | Before ADR-001 revision | STK-03 | open |
| OPN-06 | May service agents draft disruptions for dispatcher approval? | Before UC-006 baseline | STK-04 | open |
| OPN-07 | Retention of 3 years — is 5 required by the cantonal archiving rules? | Before NFR-013 baseline | STK-11 | open |
