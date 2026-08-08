# Epics

Epics gruppieren die FRs in lieferbare Scheiben. Jedes Epic benennt die FRs, die es erfüllt, sodass die
Rückverfolgbarkeit vom Geschäftsziel zur Sprint-Arbeit lückenlos ist.

| Epic | Umfasst | Gelieferter Wert bei Abschluss | Zielinkrement |
|---|---|---|---|
| E1 — Echtzeit-Backbone | FR-001…FR-006 | Prognosen existieren und sind ehrlich bezüglich ihres Alters | Sprint 1–3 |
| E2 — Einmal erfassen | FR-007, FR-008, FR-009, FR-015 | Ein Disponent kann in unter einer Minute einen korrekten Entwurf erstellen | Sprint 2–4 |
| E3 — Freigeben und verteilen | FR-010, FR-011, FR-012, FR-018, NFR-008 | Eine Freigabe erreicht jeden Kanal — der Kern von BR-01 | Sprint 4–6 |
| E4 — Haltestellenanzeigen | FR-016, FR-017, FR-019, FR-030 | 61 bestehende Anzeigen werden aus PRISMA gespeist | Sprint 5–7 |
| E5 — Nationale Plattform-Schnittstelle | FR-024, FR-025, FR-026, NFR-018 | BAV-Befund geschlossen | Sprint 6–8 |
| E6 — Korrigieren und annullieren | FR-014, FR-019 | Falsche Information kann korrigiert werden, nicht nur ergänzt | Sprint 7–8 |
| E7 — Barrierefreiheit und Sprachen | FR-011, FR-013, FR-021, NFR-011, NFR-012 | Fahrgastinformation für alle nutzbar in vier Sprachen | Sprint 3–9, laufend |
| E8 — Audit und Reporting | FR-027, FR-028, FR-029, NFR-016 | Dreijährige Rekonstruktion möglich; DSFA erfüllbar | Sprint 8–10 |
| E9 — Service Desk | FR-022, FR-023 | Agenten sehen, was der Fahrgast sieht | Sprint 9–10 |

## Begründung der Reihenfolge

E1 zuerst, weil alles Nachgelagerte wertlos ist, wenn die Prognosen falsch sind — und weil
RSK-01 (ITCS-Datenqualität) gelöst werden muss, bevor sich das Team auf NFR-004 festlegt. E5 wird
früher eingeplant, als es seine geschäftliche Priorität nahelegen würde, weil BR-03 ein regulatorischer Befund mit
einer externen Frist ist. E7 läuft über das gesamte Programm statt als Phase, weil das
nachträgliche Einbauen von Barrierefreiheit die klassische Ursache von RSK-06 ist.
