# Glossar

Kontrolliertes Vokabular. Jede Anforderung verwendet diese Begriffe genau so, wie sie hier definiert sind.
Mit **[Konflikt gelöst]** gekennzeichnete Begriffe hatten abteilungsübergreifend konkurrierende Bedeutungen.

| Begriff | Definition | Hinweise |
|---|---|---|
| **Störung** | Ein verbindlicher Datensatz über ein Ereignis, das den fahrplanmässigen Betrieb beeinträchtigt, mit Gültigkeitszeitraum, betroffenen Linien/Haltestellen, Schweregrad und Ursache. Ein Ereignis = eine Störung. | Nicht der Text, der den Fahrgästen angezeigt wird |
| **Meldung** | Eine lokalisierte, kanalspezifische Darstellung einer Störung in einer Sprache. | Abgeleitet, nie pro Kanal manuell erfasst |
| **Situation** | SIRI-SX-Begriff für das, was PRISMA als Störung bezeichnet. Wird nur im Zusammenhang mit IF-06 verwendet. | Externes Vokabular |
| **Schätzung** | Prognostizierte Ankunfts-/Abfahrtszeit einer Fahrt an einem Haltepunkt, von PRISMA aus ITCS-Eingaben berechnet. | Unterscheidet sich von der Planzeit |
| **Planzeit** | Zeit gemäss dem veröffentlichten Fahrplan (IF-02). | |
| **Verspätung** | Schätzung minus Planzeit, in Sekunden, positiv = verspätet. | |
| **Abfahrtszeile** | Eine Zeile auf einer Haltestellenanzeige: Liniennummer, Ziel, Countdown, Bemerkung. | |
| **Countdown** | Verbleibende Minuten bis zur geschätzten Abfahrt, den Fahrgästen angezeigt. Werte über 59 Min. werden stattdessen als Uhrzeit dargestellt. | **[Konflikt gelöst]** — Disponenten sagten «Countdown», Kommunikation sagte «Wartezeit» |
| **ITCS** | Intermodal Transport Control System — das bestehende Dispositionssystem von 2009. | Ablösung ausserhalb des Scope |
| **Leitstelle** | Der Betriebsraum der RVB, besetzt 04:30–01:00, 2–4 Disponenten. | |
| **Disponent/in** | Leitstellen-Mitarbeitende/r, berechtigt, Störungen zu erfassen und freizugeben. | IAM-Rolle: `prisma.dispatcher` |
| **Pikett-Verantwortliche/r** | Dienstälteste/r Disponent/in, berechtigt, Schweregrad «schwerwiegend» und höher freizugeben. | Rolle: `prisma.duty_officer` |
| **Schweregrad** | Einer von `information`, `minor`, `major`, `severe`. Bestimmt Freigaberegeln und Kanalauswahl. | Siehe FR-010 |
| **Ursache** | Standardisierter Grundcode, abgestimmt auf die SIRI-SX-Ursachentaxonomie (z. B. `roadworks`, `accident`, `staffShortage`). | Freitext nicht erlaubt |
| **Betroffenes Gebiet** | Die Menge an Linien, Routen und Haltepunkten, auf die eine Störung zutrifft. | |
| **Gültigkeitszeitraum** | Start- und optionaler End-Zeitstempel einer Störung. Offenes Ende ist für `severe` zulässig. | |
| **Publikation** | Der Vorgang der Verteilung von Meldungen einer Störung an einen oder mehrere Kanäle. | |
| **Kanal** | Ein Verteilungsziel: `stop_display`, `app`, `web`, `national_platform`, `service_desk`. | |
| **Freigabe** | Die Disponenten-Aktion, die eine Störung für die Publikation berechtigt. | **[Konflikt gelöst]** — früher «senden», was eine kanalspezifische Aktion suggerierte |
| **Konzession** | Die Bundeskonzession, unter der die RVB ihre Linien betreibt, mit angehängten Bedingungen. | |
| **Bestellverfahren** | Der Prozess, durch den Kanton und Bund den regionalen Personenverkehr bestellen und finanzieren. | |
| **BAV** | Bundesamt für Verkehr, die Regulierungsbehörde. | |
| **Nationale Open-Data-Plattform** | Die Bundesplattform, die Echtzeit-Daten des öffentlichen Verkehrs empfängt. | IF-06 |
| **NeTEx** | Europäisches Austauschformat für Stammdaten des öffentlichen Verkehrs. | IF-02 |
| **SIRI-SX / SIRI-ET** | Service Interface for Real-time Information: Situation Exchange / Estimated Timetable. | IF-06 |
| **VDV 453** | Deutsche Schnittstellennorm, die das ITCS für Echtzeitdaten verwendet. | IF-01 |
| **BehiG** | Bundesgesetz über die Beseitigung von Benachteiligungen von Menschen mit Behinderungen. | Bestimmt NFR-011 |
| **DSFA** | Datenschutz-Folgenabschätzung. | Erforderlich gemäss CON-06 |
| **Abdeckung** | Anteil der Haltestellen mit Echtzeitdaten, gemessen am Anlagenverzeichnis mit 412 Haltestellen. | KPI in BR-05 |
