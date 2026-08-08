# UC-005 — Deliver real-time data to the national platform

**Primary actor:** National open-data platform (STK-10) · **Level:** subfunction · **Status:** approved · **Traces to:** BR-03

**Precondition:** A valid subscription exists between the platform and PRISMA.

**Main success scenario**
1. The platform holds a SIRI-SX subscription for situations and a SIRI-ET subscription for
   estimated timetables.
2. On every disruption publication, correction or cancellation, PRISMA pushes the
   corresponding SIRI-SX situation within 10 s.
3. PRISMA pushes SIRI-ET updates at least every 30 s for all trips currently running.
4. PRISMA answers heartbeat requests within 5 s.

**Exception flows**
- 2a. Delivery fails → retry with backoff for 30 min, then alarm to IT Operations.
- 4a. Three consecutive missed heartbeats → PRISMA re-establishes the subscription itself.

**Compliance note:** Conformance is proven with the platform operator's test suite before
go-live and re-run after every release that touches IF-06 (CON-02).
