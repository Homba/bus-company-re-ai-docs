# UC-004 — Consume departures at a stop display

**Primary actor:** Passenger (P2 Beat) · **Level:** user goal · **Status:** approved · **Traces to:** BR-02, BR-05, BR-06

**Trigger:** The passenger looks at a stop display.

**Main success scenario**
1. PRISMA delivers the ordered departure rows for that stop to the display adapter.
2. The display shows line, destination, countdown, and a remark where one applies.
3. Rows refresh at least every 30 s; a changed estimate is reflected within 30 s of receipt.
4. An active disruption affecting the stop is shown as a banner alternating with the rows.

**Alternate flows**
- 1a. No real-time data for a trip → the planned time is shown, marked as planned rather than estimated.
- 4a. More than one disruption affects the stop → the highest severity is shown first, then by
  proximity of validity start; at most two are rotated.

**Exception flow**
- \*a. The display loses connection → after 120 s it shows a staleness notice instead of a
  countdown that would silently mislead (NFR-005). *This was the single most-cited passenger
  complaint in the 2025 audit.*
