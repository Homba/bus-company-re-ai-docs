# Personas

Four personas, derived from 14 contextual interviews and two control-centre observation shifts
(Feb 2026). Fictional people; the behaviours are the point.

---

## P1 — Nadia, dispatcher (STK-02)

*41, eight years in the control centre, works the 13:00–22:00 shift.*

**Situation.** A bus is stuck behind an accident on line 12. Within ninety seconds Nadia must
decide on a diversion, inform the driver, notify the following vehicles — and tell passengers.
Today she does the last part three times in three tools, so she usually does it after
everything else, or not at all.

**Goals.** Communicate once. Reuse the wording from last week's identical incident. Never be
the reason a wrong message went out.

**Frustrations.** Copy-paste between tools. Being asked by customer service what is going on
while she is still typing. No way to correct a message on the app once sent.

**Implications for PRISMA.** Keyboard-first authoring, templates, one release action,
correction and cancellation as first-class operations. Drives UC-002, FR-007…FR-012, NFR-002.

---

## P2 — Beat, commuter (STK-06)

*29, changes from line 4 to line 12 at Marktplatz every morning, 4-minute connection.*

**Situation.** He does not read a disruption list. He reads a countdown on a display while
walking, or glances at the app on the platform. What he needs is: does my connection hold.

**Goals.** Know within seconds whether to run, wait or take another route.

**Frustrations.** A display saying "3 min" for a bus that already left. A generic banner
"delays on the network" that does not tell him about *his* line.

**Implications.** Per-line filtering, connection-relevant messaging, honest countdown that
degrades gracefully when data is stale. Drives FR-016…FR-020, NFR-004, NFR-005.

---

## P3 — Frau Lehmann, passenger with low vision (STK-07)

*68, uses a screen reader on her phone and cannot read stop displays at all.*

**Situation.** She travels to the hospital twice a week. A replacement bus stop 200 m away is
useless information unless she can hear where it is.

**Goals.** Get the same information as everyone else, in a form her screen reader announces
in a sensible order.

**Frustrations.** Disruption text embedded in an image. Announcements that read the reason
code before the affected line. Countdown that updates so often the screen reader restarts.

**Implications.** Semantic structure, polite live regions, text alternatives, spoken-language
message variant. Drives NFR-011, NFR-012, FR-013, FR-021.

---

## P4 — Tobias, customer service agent (STK-04)

*24, handles phone and chat, sees 60–90 contacts a shift.*

**Situation.** A caller asks why the 12 is not coming. Tobias currently checks the website,
the app and, if unsure, phones the control centre — which is exactly the moment they are busiest.

**Goals.** See what the passenger sees, plus the operational context, on one screen.

**Frustrations.** Being less informed than the caller. Contradictory channel content.

**Implications.** Service-desk view fed by the same distribution hub, with internal-only
annotations. Drives FR-022, FR-023, IF-07.
