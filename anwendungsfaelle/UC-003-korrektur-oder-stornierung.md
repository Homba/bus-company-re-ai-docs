# UC-003 — Publizierte Störung korrigieren oder aufheben

**Primärer Akteur:** Disponent/in · **Ebene:** Benutzerziel · **Status:** approved · **Traces to:** BR-01, BR-02, BR-09

**Auslöser:** Die Situation ändert sich, oder die publizierte Information erweist sich als falsch.

**Hauptszenario**
1. Disponent/in öffnet eine `published`-Störung und wählt *Korrigieren* oder *Aufheben*.
2. Bei einer Korrektur: Disponent/in bearbeitet die geänderten Felder; PRISMA zeigt einen Vergleich
   mit dem aktuell publizierten Stand an.
3. PRISMA verlangt einen Änderungsgrund aus einer festen Liste (`situation_changed`, `error_correction`,
   `duplicate`, `resolved_early`).
4. PRISMA generiert die lokalisierten Meldungen neu und republiziert auf genau den Kanälen, die
   aktuell die Meldung enthalten.
5. Bei einer Aufhebung: PRISMA sendet einen Widerruf an jeden Kanal, der die Meldung enthält, und setzt
   den Status auf `cancelled`.
6. PRISMA schreibt einen neuen Audit-Eintrag, der mit dem Original verknüpft ist; die vorherige Version bleibt abrufbar.

**Alternativer Ablauf**
- 4a. Ein Kanal ist nach der Korrektur nicht mehr betroffen (z. B. der betroffene Bereich wurde verkleinert) →
  PRISMA sendet einen Widerruf an diesen Kanal und eine neue Meldung an die neu betroffenen Kanäle.

**Ausnahmeablauf**
- 5a. Eine Haltestellenanzeige ist nicht erreichbar → der Widerruf wird in die Warteschlange gestellt; die Anzeige zeigt einen
  Aktualitätshinweis an, nachdem die Frischeschwelle abgelaufen ist (NFR-005, FR-019).

**Geschäftsregel:** Eine `severe`-Störung darf nur von einer Pikett-Verantwortlichen / einem Pikett-Verantwortlichen aufgehoben werden.
