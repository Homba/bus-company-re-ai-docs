# ADR-004 — Störung als event-sourced Aggregat

**Status:** accepted (2026-03-04) · **Entscheider:** technische Leitung, STK-05

## Kontext

BR-09 verlangt die Rekonstruktion dessen, was auf welchem Kanal zu welchem Zeitpunkt kommuniziert wurde,
über drei Jahre, einschliesslich Korrekturen und Annullierungen (UC-003, UC-007). NFR-016 verlangt, dass der
Audit-Trail append-only ist.

## Entscheidung

Das Störungs-Aggregat wird als geordnete Folge von Domain Events gespeichert (created,
approved, released, published-to-channel, correction-applied, cancelled). Der aktuelle Zustand ist
eine Projektion. Kanalpublikationen sind ebenfalls Events, einschliesslich Fehlern und Wiederholungen.

## Konsequenzen

**Positiv** — FR-027, FR-028 und NFR-016 ergeben sich aus dem Speichermodell, statt nachträglich
angebaut zu werden. Idempotenz (NFR-008) ist anhand des Event-Logs überprüfbar.

**Negativ** — Löschung zum Datenschutz (NFR-013) ist in einem append-only Store schwieriger;
erfordert eine Crypto-Shredding- oder Projektions-Neuaufbau-Strategie, die vor Einreichung der
DSFA entworfen werden muss (CON-06). Als Aufgabe erfasst, nicht als offener Punkt, da die DSFA davon abhängt.
