# Business Requirements

Goal level. Each BR states a measurable business outcome, not a system behaviour.
Status: baselined, v1.2

---

### BR-01 — Single authoritative disruption record

RVB shall maintain exactly one authoritative record per service disruption, from which all
passenger-facing messages are derived.

- **Rationale:** 27 % of disruptions were communicated inconsistently in 2025 because each
  channel was filled by hand.
- **Metric:** Share of disruptions with identical core content across all channels.
- **Baseline / target:** 73 % → ≥ 99 %.
- **Verification:** Automated weekly content diff across channels.
- **Stakeholders:** STK-01, STK-02, STK-04, STK-06
- **Priority:** must

---

### BR-02 — Speed from incident to passenger

RVB shall reduce the time between a disruption being known in the control centre and the
corresponding message being visible on all active channels.

- **Metric:** Median latency, incident timestamp → message visible.
- **Baseline / target:** 11 min 40 s → ≤ 3 min (median), ≤ 8 min (95th percentile).
- **Verification:** Timestamp comparison over a rolling 3-month window.
- **Stakeholders:** STK-01, STK-06, STK-08
- **Priority:** must

---

### BR-03 — Concession-compliant data delivery

RVB shall deliver real-time service data to the national open-data platform in the formats and
at the availability the concession requires, closing the FOT audit finding of 2024-11-08.

- **Metric:** Monthly feed availability and conformance test result.
- **Baseline / target:** no feed → ≥ 99.5 % availability, conformance test passed.
- **Verification:** Platform-side monitoring plus the platform operator's conformance suite.
- **Stakeholders:** STK-09, STK-10, STK-08
- **Priority:** must

---

### BR-04 — Lower authoring effort in the control centre

RVB shall reduce the effort a dispatcher spends communicating a disruption, so that
communication does not compete with operational decisions during an incident.

- **Metric:** Average hands-on authoring time per disruption.
- **Baseline / target:** 6 min 20 s (three channels, manual) → ≤ 2 min.
- **Verification:** Time study, 40 observed disruptions after rollout.
- **Stakeholders:** STK-02, STK-01
- **Priority:** must

---

### BR-05 — Wider real-time coverage without ITCS replacement

RVB shall raise the share of stops served with real-time information, using a
channel-agnostic distribution layer so that further display rollout does not require
software change.

- **Metric:** Coverage = stops receiving real-time data / 412.
- **Baseline / target:** 14.8 % → ≥ 45 % at full rollout; 100 % reachable without code change.
- **Verification:** Asset register reconciliation; architecture review for the second half.
- **Stakeholders:** STK-08, STK-14, STK-06
- **Priority:** should

---

### BR-06 — Equal access to information

RVB shall make passenger information equally usable by people with visual, hearing or
cognitive impairments across all digital channels.

- **Metric:** Conformance audit result; task success rate in assisted-technology testing.
- **Baseline / target:** website partially conformant → full conformance to the applicable
  accessibility standard; ≥ 90 % task success with screen reader.
- **Verification:** External accessibility audit before go-live, signed off by STK-15.
- **Stakeholders:** STK-07, STK-15
- **Priority:** must

---

### BR-07 — Multilingual service area

RVB shall publish every passenger-facing message in German, French, Italian and English
without a dispatcher writing four texts.

- **Metric:** Share of released disruptions available in all four languages within 60 s of release.
- **Baseline / target:** 12 % (manual, German-first) → ≥ 98 %.
- **Verification:** Publication log analysis.
- **Stakeholders:** STK-04, STK-06, STK-08
- **Priority:** must

---

### BR-08 — Fewer information-related complaints

RVB shall reduce complaints attributed to missing or incorrect passenger information.

- **Metric:** Complaints with category `information` per year.
- **Baseline / target:** 1 340 → ≤ 670.
- **Verification:** Customer service system report, 12 months after full rollout.
- **Stakeholders:** STK-04, STK-01, STK-08
- **Priority:** should

---

### BR-09 — Auditable communication history

RVB shall be able to reconstruct, for any past disruption, what was communicated on which
channel at which time, for at least three years.

- **Rationale:** Liability cases, FOT audits, cantonal reporting.
- **Metric:** Share of sampled historic disruptions fully reconstructable.
- **Baseline / target:** not possible today → 100 % of sampled cases.
- **Verification:** Audit exercise on 20 random historic disruptions.
- **Stakeholders:** STK-01, STK-08, STK-09
- **Priority:** must

---

### BR-10 — No covert performance monitoring

RVB shall use vehicle and trip data for passenger information and aggregate service quality
reporting only, and shall not make individual driver performance derivable from PRISMA.

- **Rationale:** Works agreement, conflict C-1 in `01-stakeholders.md`.
- **Metric:** Data protection review outcome; absence of per-driver identifiers in stored data.
- **Baseline / target:** DPIA approved without reservation; zero driver identifiers in the
  reporting data mart.
- **Verification:** DPIA sign-off (STK-11) plus schema inspection by STK-13.
- **Priority:** must
