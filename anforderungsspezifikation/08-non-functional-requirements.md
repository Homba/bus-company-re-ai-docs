# Nicht-funktionale Anforderungen

Gruppiert nach ISO/IEC 25010 Produktqualitätsmerkmalen. Jede NFR enthält ein **Mass**,
einen **Zielwert** und eine **Verifikationsmethode** — eine NFR ohne diese drei ist ein
Wunsch, keine Anforderung, und besteht das Review hier nicht.

Status: baselined v1.2

---

## Performanz / Effizienz

**NFR-001 — Publikationslatenz**
*Mass:* Zeit von der Freigabe- (oder Genehmigungs-)Aktion bis zur letzten Kanalbestätigung.
*Zielwert:* ≤ 10 s Median, ≤ 20 s am 95. Perzentil, unter Spitzenlast gemäss NFR-003.
*Verifikation:* Lasttest vor Go-live; kontinuierliche Messung im Produktivbetrieb.
*Übergeordnet:* BR-02

**NFR-002 — Interaktionsaufwand bei der Erfassung**
*Mass:* Anzahl Interaktionen (Klicks oder zielgerichtete Tastatureingaben) von einem offenen
Entwurf bis zur Freigabe, für eine vorlagenbasierte Störung.
*Zielwert:* ≤ 3.
*Verifikation:* Aufgabenanalyse an der gelieferten UI, plus Zeitmessung in der BR-04-Zeitstudie.
*Übergeordnet:* BR-04

**NFR-003 — Spitzenlast**
*Mass:* Dauerhafter Durchsatz ohne Verletzung von NFR-001.
*Zielwert:* 412 bediente Haltestellen, 1 800 gleichzeitige App-Abfragen pro Sekunde, 40
Störungs-Statusänderungen pro Minute, 3 000 Schätzungen laufender Fahrten pro Minute
neuberechnet.
*Verifikation:* Lasttest mit dem Spitzenprofil vom 08.12.2025 (Schneeereignis) multipliziert
mit 1,5.
*Übergeordnet:* BR-02, BR-05

**NFR-004 — Schätzungsaktualität**
*Mass:* Alter der zugrunde liegenden ITCS-Daten hinter einer veröffentlichten Schätzung.
*Zielwert:* ≤ 30 s am 95. Perzentil.
*Verifikation:* End-to-End-Zeitstempel-Nachverfolgung im Produktionsmonitoring.
*Übergeordnet:* BR-02

## Zuverlässigkeit

**NFR-005 — Ehrliche Degradation**
*Mass:* Verhalten bei veralteten Eingabedaten oder unerreichbarem Kanal.
*Zielwert:* Kein Countdown wird aus Daten angezeigt, die älter als 120 s sind; stattdessen
wird ein Veraltet-Indikator angezeigt. Null Vorkommen eines angezeigten Countdowns auf
Basis von Daten älter als 120 s.
*Verifikation:* Fehlerinjektionstest; Produktionsalarm bei jeder Verletzung.
*Übergeordnet:* BR-02, BR-08
*Begründung:* Ein falscher Countdown schadet dem Vertrauen mehr als ein fehlender. Dies kam
aus jeder Fahrgastbefragung hervor.

**NFR-006 — Teilverfügbarkeit**
*Mass:* Systemverhalten bei Ausfall eines Subsystems.
*Zielwert:* Der Ausfall des Übersetzungsdienstes, eines Kanaladapters oder der
Reporting-Komponente darf die Publikation an die verbleibenden Kanäle nicht verhindern.
*Verifikation:* Chaos-Test pro Subsystem vor Go-live.
*Übergeordnet:* BR-02, BR-07

**NFR-007 — Verfügbarkeit**
*Mass:* Monatliche Verfügbarkeit des Publikationspfads, Servicefenster 04:00–01:30.
*Zielwert:* ≥ 99,7 % für den Publikationspfad; ≥ 99,5 % für den Feed der nationalen Plattform
(IF-06); ≥ 99,0 % für die Service-Desk-Ansicht.
*Verifikation:* Monitoring-Bericht, monatlich.
*Übergeordnet:* BR-03

**NFR-008 — Idempotente Publikation**
*Mass:* Auswirkung einer wiederholten oder erneut versuchten Publikation derselben
Störungsversion.
*Zielwert:* Genau eine Nachricht pro Kanal pro Störungsversion; null Duplikate.
*Verifikation:* Integrationstest mit erzwungenen Wiederholungen.
*Übergeordnet:* BR-01

**NFR-009 — Wiederherstellung**
*Mass:* RTO und RPO für den Publikationspfad.
*Zielwert:* RTO ≤ 30 min, RPO ≤ 60 s.
*Verifikation:* Dokumentierte Wiederherstellungsübung, zweimal jährlich.
*Übergeordnet:* BR-03, BR-09

## Sicherheit

**NFR-010 — Authentifizierung und Autorisierung**
*Mass:* Durchsetzung des Rollenmodells über IF-08.
*Zielwert:* Jede zustandsändernde Operation erfordert einen authentifizierten Prinzipal mit
der entsprechenden Rolle; 100 % der Operationen durch einen Autorisierungstest abgedeckt.
*Verifikation:* Sicherheitstestbericht; Penetrationstest vor Go-live.
*Übergeordnet:* BR-09

**NFR-016 — Audit-Integrität**
*Mass:* Veränderbarkeit von Audit-Einträgen.
*Zielwert:* Append-only-Speicher; jeder Änderungsversuch ist erkennbar; Aufbewahrung 3 Jahre.
*Verifikation:* Speicherdesign-Review plus Manipulationstest.
*Übergeordnet:* BR-09

## Benutzbarkeit und Barrierefreiheit

**NFR-011 — Barrierefreiheitskonformität**
*Mass:* Konformität aller fahrgastbezogenen digitalen Ausgaben mit dem anwendbaren
Barrierefreiheitsstandard auf Stufe AA und mit den bundesrechtlichen
Barrierefreiheitsanforderungen für öffentliche Stellen.
*Zielwert:* Vollständige Konformität, keine ungelösten Befunde der Stufe A oder AA.
*Verifikation:* Externes Audit, abgenommen durch STK-15 vor Go-live; automatisierte Prüfungen
in der CI.
*Übergeordnet:* BR-06

**NFR-012 — Aufgabenerfolg mit assistiver Technologie**
*Mass:* Aufgabenerfolgsrate für «Finde die nächste Abfahrt meiner Linie» und «Verstehe die
heutige Störung auf meiner Linie» mittels Screenreader.
*Zielwert:* ≥ 90 % Erfolg mit ≥ 8 Teilnehmenden, die täglich assistive Technologie nutzen.
*Verifikation:* Moderierter Usability-Test.
*Übergeordnet:* BR-06
*Hinweis:* Live-Regionen müssen `polite` sein, nicht `assertive` — andernfalls startet eine
30-s-Aktualisierung die Ansage neu (Erkenntnis aus P3-Interview).

**NFR-015 — Verständlichkeit**
*Mass:* Lesbarkeitsniveau der Nachrichtenvariante in einfacher Sprache.
*Zielwert:* B1 oder einfacher, verifiziert durch eine Lesbarkeitsmetrik plus Review durch zwei
fachfremde Leser.
*Verifikation:* Stichprobe von 30 generierten Nachrichten pro Release.
*Übergeordnet:* BR-06, BR-08

## Wartbarkeit und Portabilität

**NFR-017 — Kanalerweiterbarkeit**
*Mass:* Aufwand zum Hinzufügen eines neuen Kanal-Endpunkts eines bestehenden Typs.
*Zielwert:* Nur Konfiguration, kein Deployment, ≤ 30 min durch einen Administrator.
*Verifikation:* Im Abnahmetest demonstriert durch Hinzufügen von 5 Haltestellenanzeigen.
*Übergeordnet:* BR-05

**NFR-018 — Testbarkeit der Standardkonformität**
*Mass:* Möglichkeit, die Konformitätssuite des Plattformbetreibers erneut auszuführen.
*Zielwert:* Suite läuft in der CI gegen einen Staging-Endpunkt; grün vor jedem IF-06-Release.
*Verifikation:* CI-Pipeline-Nachweis.
*Übergeordnet:* BR-03

**NFR-019 — Betriebsumgebung**
*Mass:* Wo die Lösung betrieben wird.
*Zielwert:* Betreibbar in der kantonalen Verwaltungscloud mit den dort verfügbaren
Plattformdiensten; keine Abhängigkeit von einem Dienst ausserhalb des genehmigten Katalogs.
*Verifikation:* Architektur-Review mit STK-05 und dem kantonalen Cloud-Team.
*Übergeordnet:* CON-04

## Datenschutz

**NFR-013 — Aufbewahrung und Löschung**
*Mass:* Speicherdauer pro Datenkategorie.
*Zielwert:* Audit-Einträge 3 Jahre; rohe Fahrzeugpositionen 24 h; aggregierte KPIs 5 Jahre;
App-Abonnementdaten 90 Tage nach letzter Nutzung gelöscht.
*Verifikation:* Datenlebenszyklus-Review durch STK-11; Nachweis des automatisierten
Löschjobs.
*Übergeordnet:* BR-09, BR-10, CON-06

**NFR-014 — Zweckbindung für Fahrzeugdaten**
*Mass:* Vorhandensein von fahrer- oder dienstidentifizierenden Attributen in gespeicherten
oder exportierten Daten.
*Zielwert:* Null, ausserhalb des 24-h-Betriebsfensters.
*Verifikation:* Schemainspektion und Exportstichprobe durch STK-11 und STK-13.
*Übergeordnet:* BR-10
