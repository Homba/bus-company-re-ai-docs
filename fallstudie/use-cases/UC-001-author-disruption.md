# UC-001 — Author a disruption

**Primary actor:** Dispatcher · **Level:** user goal · **Status:** approved · **Traces to:** BR-01, BR-04, BR-07

**Trigger:** The dispatcher learns of an event affecting service.

**Precondition:** Authenticated with role `prisma.dispatcher`.

**Main success scenario**
1. Dispatcher starts a new disruption, optionally from a template or a past disruption.
2. Dispatcher selects the cause from the standardised taxonomy.
3. Dispatcher selects the affected area: lines, route sections or individual stops, with map support.
4. Dispatcher sets severity and validity start; optionally an expected end.
5. PRISMA proposes a structured message built from cause, area and validity.
6. Dispatcher edits the free-text slot within the character limit; PRISMA warns on terms
   outside the controlled vocabulary.
7. PRISMA saves the disruption in status `draft` and shows a preview per channel.

**Alternate flows**
- 1a. Dispatcher duplicates a recurring disruption (e.g. weekly roadworks) and adjusts dates.
- 3a. The affected area is a whole line for a whole day → dispatcher selects the shortcut "line out of service".
- 6a. Free text exceeds the display limit → PRISMA shows the truncation point for stop displays,
  keeping the full text for app and web (FR-015).

**Exception flow**
- \*a. Draft is not saved for 15 minutes with the browser closed → PRISMA retains it as an
  unreleased draft for 24 h, visible to all dispatchers.
