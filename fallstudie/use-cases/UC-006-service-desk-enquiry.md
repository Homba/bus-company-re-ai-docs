# UC-006 — Answer a passenger enquiry with current context

**Primary actor:** Customer service agent (P4 Tobias) · **Level:** user goal · **Status:** draft · **Traces to:** BR-01, BR-08

**Main success scenario**
1. Agent searches by line, stop or disruption ID.
2. PRISMA shows exactly what each channel currently displays for that scope.
3. PRISMA additionally shows internal-only context: expected duration, dispatcher note,
   whether a correction is pending.
4. Agent can flag the disruption as "generating many calls", visible to the control centre.

**Business rule:** Internal-only fields are never distributed to passenger channels; this is
enforced at the data model level, not in the UI (FR-023).

**Open point:** OPN-06 — should agents be able to draft a disruption for dispatcher approval?
