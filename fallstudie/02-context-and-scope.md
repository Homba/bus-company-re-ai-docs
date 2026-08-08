# Context and Scope

Status: baselined, v1.3

## 1. System context

```mermaid
flowchart TB
    subgraph EXT_H["Human actors"]
        D["Dispatcher<br/>STK-02"]
        A["Customer service agent<br/>STK-04"]
        P["Passenger<br/>STK-06 / STK-07"]
    end

    subgraph SYS["PRISMA"]
        DA["Disruption authoring<br/>and approval"]
        RT["Real-time departure<br/>calculation"]
        DIST["Distribution hub"]
        ARC["Archive and reporting"]
    end

    subgraph EXT_S["Neighbouring systems"]
        ITCS["ITCS<br/>vehicle positions, trips"]
        TT["Timetable master data<br/>HAFAS import"]
        DISP["Stop displays<br/>412 stops"]
        APP["RVB app back end"]
        WEB["rvb.example CMS"]
        NAT["National open-data<br/>platform"]
        CRM["Customer service system"]
        IAM["Cantonal IAM"]
    end

    D --> DA
    A --> DIST
    P --> APP
    P --> DISP
    P --> WEB

    ITCS -->|"positions 10 s, VDV 453"| RT
    TT -->|"nightly NeTEx"| RT
    DA --> DIST
    RT --> DIST
    DIST --> DISP
    DIST --> APP
    DIST --> WEB
    DIST -->|"SIRI-SX / SIRI-ET"| NAT
    DIST --> CRM
    DIST --> ARC
    IAM -->|"authentication"| DA
```

## 2. External interfaces

| ID | Partner system | Direction | Content | Protocol / format | Frequency | Owner |
|---|---|---|---|---|---|---|
| IF-01 | ITCS | in | Vehicle positions, trip progress, deviations | VDV 453 subscription | every 10 s | STK-12 |
| IF-02 | Timetable master data | in | Planned trips, stops, calendars | NeTEx file drop | nightly 02:00 | RVB IT |
| IF-03 | Stop displays | out | Departure rows, disruption banner | proprietary display protocol via adapter | push on change, ≤ 30 s | RVB IT |
| IF-04 | RVB app back end | out | Departures, disruptions, subscriptions | REST/JSON, PRISMA API v1 | on demand + push | RVB IT |
| IF-05 | Website CMS | out | Disruption list per line | REST/JSON | on change | RVB comms |
| IF-06 | National open-data platform | out | Situations and estimated timetable | SIRI-SX, SIRI-ET 2.0 | SX on change, ET every 30 s | STK-10 |
| IF-07 | Customer service system | out | Current disruption context for the agent's screen | REST/JSON | on demand | RVB IT |
| IF-08 | Cantonal IAM | in | Authentication and role claims for staff | OIDC | per session | Canton |
| IF-09 | Reporting data mart | out | Anonymised punctuality and latency KPIs | scheduled extract | daily | RVB controlling |

## 3. Scope decision table

| Topic | In | Out | Rationale |
|---|:--:|:--:|---|
| Authoring of disruption messages | ✓ | | Core problem |
| Approval workflow for messages | ✓ | | Quality and liability |
| Automatic translation DE→FR/IT/EN | ✓ | | Multilingual concession area |
| Real-time departure estimation | ✓ | | Required for ET feed |
| Vehicle localisation algorithm | | ✗ | Stays in ITCS (ADR-002) |
| Duty roster, dispatch decisions | | ✗ | Separate ITCS domain |
| Display hardware procurement | | ✗ | Separate infrastructure project |
| App UI | | ✗ | PRISMA delivers API only |
| Ticketing and fares | | ✗ | Different value stream |
| On-board announcements | | ✗ | Phase 2 candidate, see OPN-05 |

## 4. Domain model (conceptual)

```mermaid
classDiagram
    class Line
    class Route
    class Trip
    class StopPoint
    class Vehicle
    class Disruption
    class Message
    class Channel
    class Estimate

    Line "1" --> "*" Route
    Route "1" --> "*" Trip
    Route "*" --> "*" StopPoint
    Trip "1" --> "0..1" Vehicle
    Trip "1" --> "*" Estimate
    Estimate "*" --> "1" StopPoint
    Disruption "1" --> "*" Message : localized
    Disruption "*" --> "*" Line : affects
    Disruption "*" --> "*" StopPoint : affects
    Message "*" --> "*" Channel : published to
```

## 5. Terminology note

`Disruption` is the authoritative business object; `Message` is one localised, channel-shaped
rendering of it. This distinction drives FR-007 to FR-012 and is the reason a change to the
disruption never requires re-typing per channel. See `03-glossary.md`.
