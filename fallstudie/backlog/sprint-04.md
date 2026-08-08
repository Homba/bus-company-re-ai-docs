# Sprint 4 backlog (example)

**Sprint goal:** A dispatcher can release a `minor` disruption and see it appear on the app
channel and the website within 10 seconds, in German.

Epic focus: E3 — Release and distribute.

---

### US-031 — Release action on a draft disruption
*As a dispatcher I want to release a completed draft with one action so that I do not have to
repeat myself per channel.*
**Parent:** FR-007, FR-012 · **Points:** 5

- Given a draft with all mandatory fields, when I select Release, then the disruption moves to
  status `published` and a per-channel summary is shown.
- Given a draft missing a mandatory field, when I select Release, then the missing field is
  named and the status is unchanged.
- Given severity `minor`, when I select Release, then no approval step is triggered.

---

### US-032 — Severity-driven channel selection
*As a passenger information lead I want channels chosen automatically from severity so that
the channel matrix is applied consistently.*
**Parent:** FR-012 · **Points:** 8

- Given severity `minor`, when the disruption is released, then stop display, app list, web,
  national platform and service desk are targeted and app push is not.
- Given any severity, when I attempt to deselect the national platform, then the action is
  refused with the reason "concession requirement" (CON-02).
- Given a deselected optional channel, when I release, then the reason I chose is written to
  the audit entry.

---

### US-033 — Publish to the app channel adapter
*As a passenger I want disruptions to appear in the app so that I see them where I look.*
**Parent:** FR-018 · **Points:** 5

- Given a released disruption, when 10 s have elapsed, then the app back end holds the message.
- Given the adapter is unreachable, when the timeout expires, then the channel is marked
  `failed`, retried with backoff, and the dispatcher sees the failure.
- Given a repeated release of the same version, when it is processed, then the app holds
  exactly one message (NFR-008).

---

### US-034 — Publication summary view
*As a dispatcher I want to see per-channel publication state so that I know whether my message
actually arrived.*
**Parent:** FR-012, FR-027 · **Points:** 3

- Given a completed publication, when I open the summary, then each channel shows state and
  timestamp.
- Given a failed channel, when I open the summary, then the failure reason and next retry time
  are shown.
- Accessibility: the summary is operable by keyboard and announced by screen reader (NFR-011).

---

### US-035 — Audit entry for release and publication
*As a compliance officer I want every release and publication attempt recorded so that history
can be reconstructed.*
**Parent:** FR-027 · **Points:** 5

- Given any release, when it completes or fails, then an append-only entry records actor,
  timestamp, channel, outcome.
- Given an audit entry, when a modification is attempted, then it is rejected and the attempt
  is logged.

---

### Not in this sprint, and why

| Item | Reason |
|---|---|
| Approval flow (FR-010) | Depends on the duty-officer role in cantonal IAM — ASM-06 not yet confirmed |
| Translation (FR-011) | Blocked by ADR-003, which is blocked by OPN-02 |
| Stop display adapter (FR-016) | Hardware for the adapter proof of concept arrives in sprint 5 |

### Sprint risks

RSK-04 (no translation service in the catalogue) would move FR-011 out of sprint 5 as well —
escalate at the next change board if ADR-003 is not accepted by the sprint review.
