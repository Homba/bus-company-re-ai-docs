# Traceability-Matrix

Gepflegt in `requirements.yaml` und hier gerendert.
`werkzeuge/validate_requirements.py` lässt den Build fehlschlagen, wenn eine hier aufgeführte
Anforderung kein übergeordnetes Element, kein Abnahmekriterium oder keine Verifikationsmethode hat.

## 1. Geschäftsanforderung → funktionale / Qualitätsanforderungen

| BR | Titel | Realisiert durch | Verifiziert durch |
|---|---|---|---|
| BR-01 | Einzige massgebliche Quelle | FR-007, FR-008, FR-009, FR-010, FR-012, FR-014, FR-015, NFR-008 | TC-01, TC-07, TC-12 |
| BR-02 | Geschwindigkeit zum Fahrgast | FR-001…FR-006, FR-018, FR-019, NFR-001, NFR-003, NFR-004, NFR-005 | TC-02, TC-03, TC-14 |
| BR-03 | Konzessionskonforme Lieferung | FR-009, FR-012, FR-024, FR-025, FR-026, NFR-007, NFR-018 | TC-04, TC-15 |
| BR-04 | Geringerer Erfassungsaufwand | FR-007, FR-008, NFR-002 | TC-05, Zeitstudie |
| BR-05 | Breitere Abdeckung | FR-003, FR-016, FR-017, FR-020, FR-030, NFR-003, NFR-017 | TC-06, TC-16 |
| BR-06 | Gleichberechtigter Zugang | FR-013, FR-021, NFR-011, NFR-012, NFR-015 | TC-08, externes Audit |
| BR-07 | Mehrsprachigkeit | FR-008, FR-011, FR-020, NFR-006 | TC-09 |
| BR-08 | Weniger Beschwerden | FR-019, FR-022, FR-023, NFR-005, NFR-015 | TC-10, Beschwerdebericht |
| BR-09 | Auditierbare Historie | FR-023, FR-027, FR-028, NFR-009, NFR-010, NFR-013, NFR-016 | TC-11, Audit-Übung |
| BR-10 | Keine verdeckte Überwachung | FR-029, NFR-013, NFR-014 | DSFA, Schemainspektion |

**Prüfung: keine Waisen.** Jede FR-001…FR-030 und NFR-001…NFR-019 kommt oben mindestens einmal vor.

## 2. Use Case → funktionale Anforderungen

| UC | Ausgeübte FRs |
|---|---|
| UC-001 Erfassen | FR-007, FR-008, FR-009, FR-015 |
| UC-002 Freigeben und publizieren | FR-010, FR-011, FR-012, FR-018, FR-024, FR-027, NFR-001, NFR-008 |
| UC-003 Korrigieren / aufheben | FR-014, FR-018, FR-019, FR-027 |
| UC-004 Haltestellenanzeige | FR-016, FR-017, FR-019, FR-021, NFR-005 |
| UC-005 Nationale Plattform | FR-024, FR-025, FR-026, NFR-007, NFR-018 |
| UC-006 Service Desk | FR-022, FR-023 |
| UC-007 Audit | FR-027, FR-028, NFR-016 |

## 3. Randbedingung → betroffene Anforderungen

| CON | Betrifft |
|---|---|
| CON-02 | FR-012, UC-002/6a |
| CON-03 | FR-013, FR-021, NFR-011, NFR-012 |
| CON-04 | NFR-019, ADR-003 |
| CON-05 | FR-003, FR-004, ADR-002 |
| CON-06 | NFR-013, NFR-014 |
| CON-07 | FR-029, NFR-014, BR-10 |
| CON-11 | FR-024, FR-025, FR-026, NFR-018 |
| CON-12 | NFR-002 |

## 4. Testfall-Index

| TC | Umfang | Typ |
|---|---|---|
| TC-01 | Eine Störung, alle Kanäle, Inhalt identisch | Integration |
| TC-02 | Publikationslatenz unter Spitzenprofil | Performanz |
| TC-03 | Schätzungsneuberechnung bei ITCS-Update | Integration |
| TC-04 | SIRI-Konformitätssuite | Konformität |
| TC-05 | Drei-Interaktionen-Freigabepfad | Usability |
| TC-06 | Abfahrtssortierung und Countdown-Darstellung | Unit + Integration |
| TC-07 | Freigaberegel pro Schweregrad | Unit |
| TC-08 | Screenreader-Aufgabenerfolg | Usability |
| TC-09 | Viersprachige Generierung innerhalb von 60 s | Integration |
| TC-10 | Veraltet-Indikator bei verlorenem Kanal | Fehlerinjektion |
| TC-11 | Audit-Rekonstruktion von 20 historischen Störungen | Abnahme |
| TC-12 | Korrektur wird nur an haltende Kanäle propagiert | Integration |
| TC-14 | Schätzung nach 90 s Stille als veraltet markiert | Unit |
| TC-15 | Heartbeat und Neuabonnierung | Integration |
| TC-16 | 5 Anzeigen nur durch Konfiguration hinzufügen | Abnahme |
