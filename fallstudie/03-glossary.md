# Glossary

Controlled vocabulary. Every requirement uses these terms exactly as defined here.
Terms marked **[conflict resolved]** had competing meanings across departments.

| Term | Definition | Notes |
|---|---|---|
| **Disruption** | An authoritative record of an event affecting scheduled service, with a validity period, affected lines/stops, severity and cause. One event = one Disruption. | Not the text shown to passengers |
| **Message** | A localised, channel-shaped rendering of a Disruption in one language. | Derived, never authored per channel |
| **Situation** | SIRI-SX term for what PRISMA calls a Disruption. Used only when discussing IF-06. | External vocabulary |
| **Estimate** | Predicted arrival/departure time for a Trip at a StopPoint, produced by PRISMA from ITCS input. | Distinct from planned time |
| **Planned time** | Time from the published timetable (IF-02). | |
| **Delay** | Estimate minus planned time, in seconds, positive = late. | |
| **Departure row** | One line on a stop display: line number, destination, countdown, remark. | |
| **Countdown** | Minutes remaining until estimated departure, shown to passengers. Values above 59 min are shown as a clock time instead. | **[conflict resolved]** — dispatchers said "countdown", comms said "waiting time" |
| **ITCS** | Intermodal Transport Control System — the existing 2009 dispatch system. | Out of scope for replacement |
| **Control centre** | RVB's operations room, staffed 04:30–01:00, 2–4 dispatchers. | |
| **Dispatcher** | Control-centre staff member authorised to author and release disruptions. | Role in IAM: `prisma.dispatcher` |
| **Duty officer** | Senior dispatcher authorised to approve severity level "major" and above. | Role: `prisma.duty_officer` |
| **Severity** | One of `information`, `minor`, `major`, `severe`. Drives approval rules and channel selection. | See FR-010 |
| **Cause** | Standardised reason code aligned with the SIRI-SX reason taxonomy (e.g. `roadworks`, `accident`, `staffShortage`). | Free text not permitted |
| **Affected area** | The set of Lines, Routes and StopPoints a Disruption applies to. | |
| **Validity period** | Start and optional end timestamp of a Disruption. Open-ended is allowed for `severe`. | |
| **Publication** | The act of distributing Messages of a Disruption to one or more Channels. | |
| **Channel** | A distribution target: `stop_display`, `app`, `web`, `national_platform`, `service_desk`. | |
| **Release** | The dispatcher action that makes a Disruption eligible for Publication. | **[conflict resolved]** — previously "send", which implied per-channel action |
| **Concession** | The federal licence under which RVB operates its lines, with conditions attached. | |
| **Ordering procedure** | The process by which canton and federal government commission and fund regional services. | |
| **FOT** | Federal Office of Transport, the regulator. | |
| **National open-data platform** | The federal platform receiving real-time public transport data. | IF-06 |
| **NeTEx** | European exchange format for public transport master data. | IF-02 |
| **SIRI-SX / SIRI-ET** | Service Interface for Real-time Information: Situation Exchange / Estimated Timetable. | IF-06 |
| **VDV 453** | German interface standard used by the ITCS for real-time data. | IF-01 |
| **BehiG** | Federal act on the elimination of disadvantages for people with disabilities. | Drives NFR-011 |
| **DPIA** | Data protection impact assessment. | Required by CON-06 |
| **Coverage** | Share of stops receiving real-time data, measured against the 412-stop asset register. | KPI in BR-05 |
