# Project Charter — PRISMA

| | |
|---|---|
| **Project** | PRISMA — Passenger Real-time Information & Service Management |
| **Client** | Regionalverkehr Bernland AG (RVB) |
| **Sponsor** | Head of Operations (STK-01) |
| **Product Owner** | Passenger Information Lead (STK-03) |
| **Status of this document** | baselined, v1.2, 2026-03-11 |
| **Planned go-live** | Pilot Q4 2026, full rollout Q2 2027 |

## 1. Problem statement

RVB distributes passenger information through three unconnected paths:

1. The **ITCS** (2009, vendor no longer supporting the version) pushes departure times to
   61 of 412 stop displays over a proprietary protocol.
2. Control-centre staff type disruption texts by hand into the website CMS, into an SMS
   gateway, and into the app back office — three times, in three wordings.
3. The national open-data platform receives a static timetable export nightly and **no**
   real-time data at all.

Consequences measured in 2025:

| Symptom | Measurement | Source |
|---|---|---|
| Median delay between an incident and the first passenger-facing message | 11 min 40 s | Control-centre log analysis, Jan–Jun 2025 |
| Contradictory information across channels | 27 % of disruptions | Quality audit, 120 sampled disruptions |
| Complaints attributed to "no / wrong information" | 1 340 per year, 38 % of all complaints | Customer service system |
| Stops with real-time display coverage | 14.8 % | Asset register |
| Concession condition on real-time data delivery | **not met** since 2024 | FOT audit letter 2024-11-08 |

## 2. Business goals

See `04-business-requirements.md` for the full, testable set. In short:

- One authoritative disruption record per incident, entered once.
- Under three minutes from incident to passenger-facing message on every channel.
- Real-time data delivered to the national platform, closing the concession finding.
- Stop-display coverage raised without replacing the ITCS core in this programme.

## 3. Scope boundary

**In scope**
- Disruption authoring, approval and distribution
- Real-time departure calculation and publication
- Channel adapters: stop displays, RVB app, website, national data platform, customer desk
- Multilingual message handling (DE / FR / IT / EN)
- Accessibility of all passenger-facing output

**Out of scope**
- Replacement of the ITCS core (vehicle localisation, dispatch, duty rosters)
- Ticketing, fare calculation, sales channels
- On-board announcement hardware procurement
- The RVB app's UI redesign (PRISMA delivers the API, not the screens)

## 4. Success criteria (verified 6 months after full rollout)

| ID | Criterion | Target | Method |
|---|---|---|---|
| SC-1 | Median incident-to-message latency | ≤ 3 min | Automatic timestamp comparison, 3-month window |
| SC-2 | Channel consistency | ≥ 99 % of disruptions identical across channels | Automated content diff, weekly sample |
| SC-3 | Real-time feed availability to national platform | ≥ 99.5 % monthly | Platform-side monitoring |
| SC-4 | Complaints citing missing/wrong information | −50 % vs. 2025 baseline | Customer service system |
| SC-5 | Control-centre effort per disruption | ≤ 2 min authoring time | Time study, 40 observations |

## 5. Constraints summary

Cost ceiling CHF 4.2 M over three financial years; procurement subject to public tendering law;
the solution must run in the cantonal government cloud; concession compliance is not negotiable.
Full list in `09-constraints-and-compliance.md`.

## 6. Approach

Hybrid. Business requirements, quality requirements and legal constraints are specified up
front and baselined (they are procurement-relevant). Functional detail is elaborated
iteratively: the FR set is the contractual backbone, user stories in `backlog/` carry
the sprint-level detail and are allowed to change without a change request as long as they
stay inside their parent FR.

## 7. Sign-off

| Role | Name (fictional) | Date |
|---|---|---|
| Sponsor / Head of Operations | R. Buchser | 2026-03-11 |
| Head of IT | M. Zaugg | 2026-03-11 |
| Head of Customer Service | A. Perrin | 2026-03-09 |
| Cantonal transport office (observer) | Dr. S. Iten | 2026-03-11 |
