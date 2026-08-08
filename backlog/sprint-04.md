# Sprint 4 Backlog (Beispiel)

**Sprint-Ziel:** Ein Disponent kann eine Störung der Stufe `minor` freigeben und sie innerhalb von 10 Sekunden auf dem App-Kanal und der Website sehen, auf Deutsch.

Epic-Fokus: E3 — Freigeben und verteilen.

---

### US-031 — Freigabeaktion für einen Störungsentwurf
*Als Disponent möchte ich einen fertiggestellten Entwurf mit einer Aktion freigeben, damit ich mich nicht pro Kanal wiederholen muss.*
**Übergeordnet:** FR-007, FR-012 · **Punkte:** 5

- Gegeben ein Entwurf mit allen Pflichtfeldern, wenn ich Freigeben wähle, dann wechselt die Störung in den
  Status `published` und eine Zusammenfassung pro Kanal wird angezeigt.
- Gegeben ein Entwurf mit einem fehlenden Pflichtfeld, wenn ich Freigeben wähle, dann wird das fehlende Feld
  benannt und der Status bleibt unverändert.
- Gegeben Schweregrad `minor`, wenn ich Freigeben wähle, dann wird kein Genehmigungsschritt ausgelöst.

---

### US-032 — Schweregrad-gesteuerte Kanalauswahl
*Als Leiter Fahrgastinformation möchte ich, dass Kanäle automatisch anhand des Schweregrads gewählt werden, damit die Kanalmatrix konsistent angewendet wird.*
**Übergeordnet:** FR-012 · **Punkte:** 8

- Gegeben Schweregrad `minor`, wenn die Störung freigegeben wird, dann werden Haltestellenanzeige, App-Liste, Web,
  nationale Plattform und Service Desk angesteuert und App-Push nicht.
- Gegeben ein beliebiger Schweregrad, wenn ich versuche, die nationale Plattform abzuwählen, dann wird die Aktion
  mit der Begründung «Konzessionsanforderung» (CON-02) verweigert.
- Gegeben ein abgewählter optionaler Kanal, wenn ich freigebe, dann wird der von mir gewählte Grund in den
  Audit-Eintrag geschrieben.

---

### US-033 — Publikation an den App-Kanaladapter
*Als Fahrgast möchte ich, dass Störungen in der App erscheinen, damit ich sie dort sehe, wo ich hinschaue.*
**Übergeordnet:** FR-018 · **Punkte:** 5

- Gegeben eine freigegebene Störung, wenn 10 s vergangen sind, dann hält das App-Backend die Nachricht bereit.
- Gegeben der Adapter ist nicht erreichbar, wenn das Timeout abläuft, dann wird der Kanal als
  `failed` markiert, mit Backoff wiederholt, und der Disponent sieht den Fehler.
- Gegeben eine wiederholte Freigabe derselben Version, wenn sie verarbeitet wird, dann hält die App
  genau eine Nachricht (NFR-008).

---

### US-034 — Publikationsübersicht
*Als Disponent möchte ich den Publikationsstatus pro Kanal sehen, damit ich weiss, ob meine Nachricht tatsächlich angekommen ist.*
**Übergeordnet:** FR-012, FR-027 · **Punkte:** 3

- Gegeben eine abgeschlossene Publikation, wenn ich die Übersicht öffne, dann zeigt jeder Kanal Status und
  Zeitstempel.
- Gegeben ein fehlgeschlagener Kanal, wenn ich die Übersicht öffne, dann werden Fehlergrund und nächster
  Wiederholungszeitpunkt angezeigt.
- Barrierefreiheit: Die Übersicht ist per Tastatur bedienbar und wird vom Screenreader vorgelesen (NFR-011).

---

### US-035 — Audit-Eintrag für Freigabe und Publikation
*Als Compliance-Beauftragter möchte ich, dass jede Freigabe und jeder Publikationsversuch protokolliert wird, damit die Historie rekonstruiert werden kann.*
**Übergeordnet:** FR-027 · **Punkte:** 5

- Gegeben eine beliebige Freigabe, wenn sie abgeschlossen wird oder fehlschlägt, dann erfasst ein append-only Eintrag Akteur,
  Zeitstempel, Kanal und Ergebnis.
- Gegeben ein Audit-Eintrag, wenn eine Änderung versucht wird, dann wird sie abgelehnt und der Versuch
  wird protokolliert.

---

### Nicht in diesem Sprint, und warum

| Element | Grund |
|---|---|
| Genehmigungsfluss (FR-010) | Abhängig von der Pikettdienst-Rolle im kantonalen IAM — ASM-06 noch nicht bestätigt |
| Übersetzung (FR-011) | Blockiert durch ADR-003, der durch OPN-02 blockiert ist |
| Haltestellenanzeige-Adapter (FR-016) | Hardware für den Adapter-Proof-of-Concept trifft in Sprint 5 ein |

### Sprint-Risiken

RSK-04 (kein Übersetzungsdienst im Katalog) würde FR-011 auch aus Sprint 5 verschieben —
Eskalation am nächsten Change Board, falls ADR-003 nicht bis zum Sprint Review akzeptiert ist.
