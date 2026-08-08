# Risiken, Annahmen und offene Punkte

## 1. Risiken

Exposition = Wahrscheinlichkeit × Auswirkung, jeweils 1–5.

| ID | Risiko | W | A | Exp | Massnahme | Eigentümer | Status |
|---|---|:--:|:--:|:--:|---|---|---|
| RSK-01 | ITCS-Datenqualität ist schlechter als angenommen; Schätzungen auf einigen Linien unbrauchbar | 4 | 5 | 20 | Mindern — Datenqualitätsanalyse auf 6 Linien in Sprint 0, bevor NFR-004 festgelegt wird | STK-03 | offen |
| RSK-02 | ITCS-Lieferant verrechnet Schnittstellenunterstützung als Change Requests und schmälert das Budget | 3 | 4 | 12 | Transferieren — Festpreis-Schnittstellensupport-Klausel vor Ausschreibung verhandelt | STK-01 | in Umsetzung |
| RSK-03 | Automatische Übersetzung erzeugt rechtlich oder betrieblich irreführende Formulierungen | 3 | 4 | 12 | Mindern — begrenztes Freitextfeld, geprüfter Vorlagenkatalog, menschliches Review-Flag für `severe` | STK-04 | in Umsetzung |
| RSK-04 | Kantonaler Cloud-Dienstkatalog enthält keinen geeigneten Übersetzungsdienst | 3 | 3 | 9 | Mindern — ADR-003 evaluiert frühzeitig On-Premise-Alternative | STK-05 | offen |
| RSK-05 | Personalkommission verweigert Zustimmung und blockiert die Nutzung von Fahrzeugdaten | 2 | 5 | 10 | Vermeiden — frühzeitige Konsultation, Zweckbindung in BR-10 und NFR-014 verankert | STK-01 | in Umsetzung |
| RSK-06 | Barrierefreiheits-Audit fällt spät durch und verzögert Go-live über den CON-10-Freeze hinaus | 3 | 4 | 12 | Mindern — Barrierefreiheitsprüfungen in der CI ab Sprint 1, Vor-Audit bei 60 % Feature-Fertigstellung | STK-03 | offen |
| RSK-07 | Anzeigeadapter für die 2009er-Hardware erweist sich im Massstab als unzuverlässig | 3 | 3 | 9 | Mindern — Adapter-Lasttest mit 60 realen Anzeigen im Pilotbetrieb | STK-05 | offen |
| RSK-08 | Disponenten nutzen aus Gewohnheit weiterhin die alten Kanäle parallel | 3 | 3 | 9 | Mindern — alte Kanäle werden am Pilotende ausser Betrieb genommen; Schulung gemäss CON-12 | STK-01 | offen |
| RSK-09 | Spitzenlastprofil unterschätzt; Schneeereignisse überschreiten NFR-003 | 2 | 4 | 8 | Mindern — 1,5×-Marge bereits in NFR-003 enthalten; Autoscaling im Lasttest verifiziert | STK-05 | akzeptiert |
| RSK-10 | Scope Creep durch Gemeinden, die lokale Anzeigefunktionen wünschen | 3 | 2 | 6 | Kontrollieren — Änderungsprozess in Dok. 12; Gemeindeanfragen werden über STK-08 gelenkt | STK-03 | offen |

## 2. Annahmen

| ID | Annahme | Falls falsch | Validiert durch |
|---|---|---|---|
| ASM-01 | Die ITCS-VDV-453-Schnittstelle bleibt für die Projektdauer unverändert verfügbar | FR-003 muss neu spezifiziert werden; erhebliche Kostenauswirkung | Schriftliche Bestätigung von STK-12, erhalten am 14.02.2026 |
| ASM-02 | Fahrplan-Stammdaten sind für alle 38 Linien vollständig und korrekt | Importregeln benötigen Bereinigungslogik; Aufwand +15 % | Datenprofiling in Sprint 0 |
| ASM-03 | 61 bestehende Anzeigen können über einen Adapter ohne Hardwareänderung angesteuert werden | Abdeckungsziel in BR-05 innerhalb von CON-08 nicht erreichbar | Adapter Proof of Concept, Sprint 1 |
| ASM-04 | Das SIRI-Profil der nationalen Plattform ändert sich vor Go-live nicht | Nacharbeit an FR-024…FR-026 | Schnittstellenvereinbarung mit STK-10 |
| ASM-05 | Vier Sprachen genügen; kein Rätoromanisch-Bedarf im Konzessionsgebiet | FR-011 Erweiterung | Geprüft mit STK-08, 22.01.2026 |
| ASM-06 | Kantonales IAM kann die vier PRISMA-Rollen ausstellen | Eigenes Rollenmanagement erforderlich; Auswirkung auf Security-Review | Bestätigung Kantons-IT ausstehend |

## 3. Offene Punkte

| ID | Frage | Benötigt bis | Eigentümer | Status |
|---|---|---|---|---|
| OPN-01 | Wird eine rätoromanische Variante benötigt, falls der Kanton das Konzessionsgebiet erweitert? | Vor FR-011 Baseline | STK-08 | offen |
| OPN-02 | Wer verantwort den Nachrichtenvorlagenkatalog nach Go-live — Kommunikation oder Betrieb? | Vor Go-live | STK-01 | offen |
| OPN-03 | Welche 45 % der Haltestellen sind im Scope für den Anzeigerollout, und nach welchem Kriterium? | Vor Pilotbetrieb | STK-08 / STK-14 | in Bearbeitung |
| OPN-04 | Braucht eine `severe`-Störung eine Freigabe, wenn der Pikettoffizier sie selbst erfasst hat? | Vor FR-010 Implementierung | STK-02 | offen |
| OPN-05 | Sind Bordansagen ein Phase-2-Kanal, und ändert das die API jetzt schon? | Vor ADR-001 Revision | STK-03 | offen |
| OPN-06 | Dürfen Service-Desk-Mitarbeitende Störungen zur Disponenten-Freigabe entwerfen? | Vor UC-006 Baseline | STK-04 | offen |
| OPN-07 | Aufbewahrung von 3 Jahren — sind 5 Jahre gemäss kantonaler Archivierungsvorschriften erforderlich? | Vor NFR-013 Baseline | STK-11 | offen |
