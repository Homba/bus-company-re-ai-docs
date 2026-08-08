# Fallback-Material: Vorbereitete AI-Ausgaben

> **Hinweis für Workshopleitung:** Dieses Dokument enthält vorbereitete AI-Ausgaben für
> die Module 2, 3 und 4. Es dient als Absicherung für den Fall, dass die LLM-Plattform
> (Claude / Gemini) während des Workshops nicht verfügbar ist oder technische Probleme auftreten.
>
> **Verwendung:** Drucken Sie die relevanten Abschnitte aus oder teilen Sie sie digital,
> damit die Teilnehmenden die Bewertungs- und Vergleichsübungen trotzdem durchführen können.
> Die Ausgaben entsprechen dem, was ein gut konfigurierter Agent bei einem ersten Durchgang
> typischerweise produziert — inklusive einiger Lücken, die im Workshop diskutiert werden sollen.

---

## Modul 2: Stakeholder-Analyse

*Simulierte Ausgabe des Stakeholder Analyst Agent auf Basis des Projektbriefings und der Interviewprotokolle.*

---

### Stakeholder-Register

**STK-01: Leiter Betrieb (Sponsor)**
- Typ: Sponsor, Entscheidungsträger
- Interesse: Konzessionskonformität sicherstellen, Effizienz der Leitstelle verbessern, Beschwerden wegen Fahrgastinformation reduzieren
- Einfluss: **hoch** — Auftraggeber des Projekts, Budgetverantwortung, Eskalationsinstanz gegenüber dem Verwaltungsrat
- Hauptanliegen: Das BAV-Audit-Finding schliessen und gleichzeitig die operative Belastung der Disponenten nicht erhöhen
- Erfolgskriterium: Konzessionsauflage erfüllt, Median-Verzögerung < 3 Min., Beschwerden halbiert
- Engagement: Manage closely — Steuerungsausschuss, monatliches Reporting

**STK-02: Leiterin Fahrgastinformation (Product Owner)**
- Typ: Entscheidungsträgerin, primäre Nutzerin
- Interesse: Inhaltliche Hoheit über alle Fahrgastnachrichten, Qualitätssicherung der Meldungen
- Einfluss: **hoch** — Verantwortlich für das Product Backlog und die fachliche Abnahme
- Hauptanliegen: Konsistente Meldungen über alle Kanäle hinweg, Kontrolle über den Freigabeprozess
- Erfolgskriterium: 99 % konsistente Meldungen, funktionierender Freigabe-Workflow
- Engagement: Manage closely — täglicher Austausch, Sprint Reviews

**STK-03: Disponentinnen und Disponenten (Leitstelle)**
- Typ: Primäre Nutzer
- Interesse: Weniger manuelle Schritte unter Zeitdruck, brauchbare Vorlagen statt Freitexteingabe in drei Systeme
- Einfluss: **tief** — kein formaler Einfluss auf Projektentscheide, aber als Hauptnutzende zentral für die Akzeptanz
- Hauptanliegen: «In der Hauptverkehrszeit kann ich nicht perfekte Sätze in drei Sprachen formulieren. Gebt mir Lückentexte.»
- Erfolgskriterium: Erfassungszeit pro Störung ≤ 2 Min., Vorlagen für die häufigsten Störungsursachen
- Engagement: Involve — Workshops, Usability-Tests, Pilotbetrieb

**STK-04: Kundendienst-Mitarbeitende**
- Typ: Sekundäre Nutzer
- Interesse: Dieselbe Information sehen wie die Fahrgäste, um kompetent Auskunft geben zu können
- Einfluss: **tief** — kein Projektentscheid, aber täglicher Kontakt mit Fahrgästen
- Hauptanliegen: «Fahrgäste rufen an und wir haben keine Ahnung, was sie in der App im Vergleich zur Anzeige gesehen haben.»
- Erfolgskriterium: Service-Desk-Ansicht mit kanalübergreifender Darstellung
- Engagement: Involve — Review der Desk-Ansicht, Feedbackrunden

**STK-05: Fahrgäste (Pendler und Gelegenheitsfahrgäste)**
- Typ: Externe Betroffene, primäre Nutzniesser
- Interesse: Genaue, zeitnahe Abfahrts- und Störungsinformationen über alle Kanäle
- Einfluss: **tief** — kein direkter Einfluss, aber ihre Zufriedenheit ist der zentrale Projekterfolgsmassstab
- Hauptanliegen: Verlässliche Echtzeitinformation, keine widersprüchlichen Angaben zwischen App und Anzeige
- Erfolgskriterium: Informationsbezogene Beschwerden sinken von 1'340 auf ≤ 670 pro Jahr
- Engagement: Vertreten durch Personas, User-Testing im Pilotbetrieb

**STK-06: Bundesamt für Verkehr (BAV)**
- Typ: Regulator
- Interesse: Konzessionsauflagen durchsetzen, insbesondere Echtzeitdatenlieferung an die nationale Plattform
- Einfluss: **hoch** — Kann bei Nichterfüllung die Konzessionserneuerung gefährden
- Hauptanliegen: SIRI-Feeds (Echtzeit-Fahrzeugpositionen und Störungsmeldungen) an die Open-Data-Plattform
- Erfolgskriterium: Audit-Finding vom 8.11.2024 geschlossen, monatliche Feed-Verfügbarkeit ≥ 99,5 %
- Engagement: Keep satisfied — Compliance-Nachweis, periodische Berichterstattung

**STK-07: Personalvertretung / Personalkommission**
- Typ: Interne Interessenvertretung
- Interesse: Verhinderung verdeckter Leistungsüberwachung der Chauffeure über Fahrzeugpositionsdaten
- Einfluss: **hoch** — Kann das Projekt blockieren, wenn Datenschutzbedenken nicht adressiert werden
- Hauptanliegen: «Ein System, das Fahrzeugpositionen erfasst, darf nicht für individuelle Leistungsüberwachung verwendet werden können.»
- Erfolgskriterium: DSFA genehmigt, Betriebsvereinbarung unterzeichnet, keine fahrerbezogenen Kennzahlen im Reporting
- Engagement: Consult — frühzeitig einbinden, vor Baseline der Anforderungen

**STK-08: Behindertenorganisation**
- Typ: Externe Interessenvertretung
- Interesse: Barrierefreiheit aller fahrgastbezogenen Informationsausgaben gemäss BehiG
- Einfluss: **mittel** — Kann öffentlichen Druck erzeugen und Beschwerden bei der Aufsichtsbehörde einreichen
- Hauptanliegen: Screenreader-Kompatibilität, ausreichender Kontrast, Leichte Sprache
- Erfolgskriterium: Externe Barrierefreiheitsprüfung bestanden, ≥ 90 % Task-Erfolgsrate mit Screenreader
- Engagement: Consult — Barrierefreiheitsprüfung vor Go-Live

**STK-09: Kantonales Amt für öffentlichen Verkehr**
- Typ: Externer Stakeholder, Mitfinanzierer
- Interesse: Gegenleistung für öffentliche Mittel, Berichterstattung, flächendeckende Haltestellenabdeckung
- Einfluss: **hoch** — Hauptaktionär (71 %), Mitfinanzierung über das Bestellverfahren
- Hauptanliegen: Flächendeckende Echtzeit-Abdeckung aller 412 Haltestellen (langfristig)
- Erfolgskriterium: Vierteljährlicher Fortschrittsbericht, Abdeckung steigt auf ≥ 45 %
- Engagement: Keep satisfied — Quartalsberichte, Einbezug bei strategischen Entscheiden

**STK-10: Datenschutzbeauftragter (DSB)** *[abgeleitet]*
- Typ: Regulator (intern oder kantonal)
- Interesse: Rechtmässige Verarbeitung personenbezogener Daten, Einhaltung des nDSG
- Einfluss: **mittel** — Muss die Datenschutz-Folgenabschätzung (DSFA) freigeben
- Hauptanliegen: Zweckbindung der Fahrzeugpositionsdaten, Aufbewahrungsfristen, keine unzulässige Personenidentifikation
- Erfolgskriterium: DSFA ohne Auflagen genehmigt
- Engagement: Consult — DSFA-Freigabe
- *Begründung für Ableitung:* In Schweizer öV-Projekten mit Fahrzeugortung ist die Einbindung eines DSB zwingend.

---

### Erkannte Konflikte

**Konflikt C-1: Fahrzeugpositionsdaten — Fahrgastinformation vs. Fahrerüberwachung**
- Parteien: STK-01 (Leiter Betrieb) vs. STK-07 (Personalvertretung)
- Natur: Fahrzeugpositionsdaten sind für die Echtzeit-Fahrgastinformation technisch notwendig. Dieselben Daten könnten theoretisch zur individuellen Leistungsüberwachung der Chauffeure verwendet werden, was die Personalvertretung ablehnt.
- Lösungsansatz: Betriebsvereinbarung, die den Verwendungszweck auf Fahrgastinformation und aggregiertes Qualitätsreporting beschränkt. Positionsdaten werden nach 24 Stunden aggregiert, kein Reporting auf Fahrer-Ebene. Wird zur negativen Anforderung (BR-10) und zur Randbedingung.

**Konflikt C-2: Freitext-Geschwindigkeit vs. standardisierte Meldungen**
- Parteien: STK-03 (Disponenten) vs. STK-04 (Kundendienst)
- Natur: Disponenten wollen schnell und flexibel formulieren (Freitext). Kundendienst-Mitarbeitende und die Mehrsprachigkeit erfordern standardisierte, übersetzbare Formulierungen.
- Lösungsansatz: Strukturierte Meldungsvorlagen pro Störungsursache mit einem begrenzten Freitext-Feld (max. 240 Zeichen). Der Freitext wird übersetzt, die Vorlage ist vorübersetzt.

**Konflikt C-3: Flächendeckende Haltestellenabdeckung vs. Budgetobergrenze**
- Parteien: STK-09 (Kantonales Amt) vs. Projektbudget
- Natur: Der Kanton möchte alle 412 Haltestellen mit Echtzeit-Anzeigen ausstatten. Das Budget von CHF 4,2 Mio. deckt nicht die Hardware für alle Standorte.
- Lösungsansatz: Priorisierter Rollout nach Fahrgastaufkommen. PRISMA liefert eine kanalunabhängige API, sodass weitere Anzeigen ohne Softwareänderung angebunden werden können. Abdeckungsziel: 45 % bei Volleinführung, 100 % technisch erreichbar.

---

### Influence/Interest-Bewertung (Zusammenfassung)

| ID | Stakeholder | Einfluss | Interesse | Strategie |
|---|---|---|---|---|
| STK-01 | Leiter Betrieb | Hoch | Hoch | Manage closely |
| STK-02 | Leiterin Fahrgastinformation | Hoch | Hoch | Manage closely |
| STK-03 | Disponenten | Tief | Hoch | Involve |
| STK-04 | Kundendienst | Tief | Hoch | Involve |
| STK-05 | Fahrgäste | Tief | Hoch | Keep informed |
| STK-06 | BAV | Hoch | Tief | Keep satisfied |
| STK-07 | Personalvertretung | Hoch | Mittel | Consult |
| STK-08 | Behindertenorganisation | Mittel | Mittel | Consult |
| STK-09 | Kantonales Amt | Hoch | Mittel | Keep satisfied |
| STK-10 | DSB | Mittel | Tief | Consult |

---

## Modul 3: Business Requirements

*Simulierte Ausgabe des Requirements Elicitor Agent auf Basis des Projektbriefings, der Interviewprotokolle und des Stakeholder-Registers.*

---

### Business Requirements

---

**BR-01 — Einheitlicher, massgeblicher Störungsnachweis**

Die RVB soll pro Betriebsstörung genau einen massgeblichen Datensatz führen, aus dem alle fahrgastseitigen Meldungen abgeleitet werden.

- **Ziel:** Konsistenz über alle Kanäle: Website, App, Haltestellenanzeigen, nationale Plattform, Kundendienst-Ansicht
- **Baseline:** 27 % der Störungen werden mit inkonsistentem Wortlaut über die verschiedenen Kanäle kommuniziert (Jan.–Jun. 2025)
- **Zielwert:** ≥ 99 % der Störungen mit identischem Kerninhalt auf allen Kanälen
- **Quelle:** STK-01 (Leiter Betrieb), STK-04 (Kundendienst)
- **Priorität:** must

---

**BR-02 — Geschwindigkeit vom Ereignis zur Fahrgastmeldung**

Die RVB soll die Zeit zwischen dem Bekanntwerden einer Störung in der Leitstelle und der Sichtbarkeit der Meldung auf allen aktiven Kanälen reduzieren.

- **Ziel:** Fahrgäste erhalten zeitnahe Information, bevor sie an der Haltestelle stehen und auf einen nicht kommenden Bus warten
- **Baseline:** 11 Min. 40 Sek. medianer Verzug (Jan.–Jun. 2025)
- **Zielwert:** ≤ 3 Min. (Median), ≤ 8 Min. (95. Perzentil)
- **Quelle:** STK-01 (Leiter Betrieb), STK-05 (Fahrgäste)
- **Priorität:** must

---

**BR-03 — Konzessionskonforme Datenlieferung**

Die RVB soll Echtzeitdaten an die nationale Open-Data-Plattform in den geforderten Formaten und mit der geforderten Verfügbarkeit liefern und das BAV-Audit-Finding vom 8. November 2024 schliessen.

- **Ziel:** Erfüllung der Konzessionsauflage zur Echtzeitdatenlieferung (SIRI-Feeds)
- **Baseline:** Kein Echtzeit-Feed vorhanden, nur nächtlicher NeTEx-Fahrplanexport
- **Zielwert:** ≥ 99,5 % Feed-Verfügbarkeit, Konformitätstest bestanden
- **Quelle:** STK-06 (BAV), STK-09 (Kantonales Amt)
- **Priorität:** must

---

**BR-04 — Geringerer Erfassungsaufwand in der Leitstelle**

Die RVB soll den Aufwand reduzieren, den Disponenten für die Kommunikation einer Störung aufwenden, damit die Kommunikation nicht mit operativen Entscheiden während eines Ereignisses konkurriert.

- **Ziel:** Disponenten können sich auf den Betrieb konzentrieren, statt Meldungen in drei Systeme zu tippen
- **Baseline:** 6 Min. 20 Sek. durchschnittliche Erfassungszeit pro Störung (drei Kanäle, manuell)
- **Zielwert:** ≤ 2 Min. Erfassungszeit pro Störung
- **Quelle:** STK-03 (Disponenten), STK-01 (Leiter Betrieb)
- **Priorität:** must

---

**BR-05 — Breitere Echtzeit-Abdeckung ohne ITCS-Ablösung**

Die RVB soll den Anteil der Haltestellen mit Echtzeitinformation erhöhen, wobei eine kanalunabhängige Verteilschicht eingesetzt wird, sodass der weitere Anzeigerollout keine Softwareänderung erfordert.

- **Ziel:** Mehr Fahrgäste profitieren von Echtzeit-Abfahrtsinformationen
- **Baseline:** 61 von 412 Haltestellen mit Echtzeit-Anzeige (14,8 % Abdeckung)
- **Zielwert:** ≥ 45 % bei Volleinführung; 100 % technisch erreichbar ohne Codeänderung
- **Quelle:** STK-09 (Kantonales Amt), STK-05 (Fahrgäste)
- **Priorität:** should

---

**BR-06 — Gleichberechtigter Zugang zu Informationen**

Die RVB soll Fahrgastinformationen für Menschen mit visuellen, auditiven oder kognitiven Einschränkungen über alle digitalen Kanäle gleichermassen nutzbar machen.

- **Ziel:** Barrierefreiheit gemäss BehiG und anwendbarem Standard
- **Baseline:** Website teilweise konform, App und Anzeigen nicht geprüft
- **Zielwert:** Vollständige Konformität zum anwendbaren Barrierefreiheitsstandard; ≥ 90 % Task-Erfolgsrate mit Screenreader
- **Quelle:** STK-08 (Behindertenorganisation), STK-06 (BAV)
- **Priorität:** must

---

**BR-07 — Mehrsprachiger Betrieb**

Die RVB soll jede fahrgastseitige Meldung in Deutsch, Französisch, Italienisch und Englisch veröffentlichen, ohne dass ein Disponent vier Texte schreiben muss.

- **Ziel:** Alle Fahrgäste erhalten Meldungen in ihrer Sprache, ohne manuellen Übersetzungsaufwand
- **Baseline:** 12 % der Störungsmeldungen in allen Sprachen verfügbar (manuell, Deutsch zuerst, Französisch nur wenn zufällig französischsprachiger Disponent im Dienst)
- **Zielwert:** ≥ 98 % der freigegebenen Störungsmeldungen in allen vier Sprachen innerhalb von 60 Sek. nach Freigabe
- **Quelle:** STK-04 (Kundendienst), STK-05 (Fahrgäste)
- **Priorität:** must

---

**BR-08 — Weniger informationsbezogene Beschwerden**

Die RVB soll Beschwerden reduzieren, die auf fehlende oder fehlerhafte Fahrgastinformation zurückzuführen sind.

- **Ziel:** Höhere Fahrgastzufriedenheit, weniger Aufwand im Kundendienst
- **Baseline:** 1'340 informationsbezogene Beschwerden pro Jahr (38 % aller Beschwerden)
- **Zielwert:** ≤ 670 Beschwerden pro Jahr
- **Quelle:** STK-04 (Kundendienst), STK-01 (Leiter Betrieb)
- **Priorität:** should

---

**BR-09 — Keine verdeckte Leistungsüberwachung** *(Negative Anforderung)*

Die RVB soll Fahrzeug- und Fahrtdaten ausschliesslich für die Fahrgastinformation und aggregiertes Qualitätsreporting verwenden. Aus PRISMA darf keine individuelle Fahrerleistung ableitbar sein.

- **Ziel:** Schutz der Persönlichkeitsrechte der Chauffeure, Einhaltung der Betriebsvereinbarung
- **Baseline:** Keine Betriebsvereinbarung vorhanden, Personalvertretung hat Bedenken geäussert
- **Zielwert:** DSFA ohne Auflagen genehmigt; null Fahrer-Identifikatoren im Reporting-Datamart
- **Quelle:** STK-07 (Personalvertretung), STK-10 (DSB)
- **Priorität:** must

---

### Vom Agent identifizierte Lücken und Rückfragen

| # | Lücke | Empfohlene Rückfrage |
|---|-------|---------------------|
| 1 | Aufbewahrungsdauer für Störungshistorie nicht definiert | Wie lange muss die Kommunikationshistorie für BAV-Audits und Haftungsfälle aufbewahrt werden? |
| 2 | Genauer Barrierefreiheitsstandard nicht spezifiziert | Gilt WCAG 2.1 AA oder ein neuerer Standard? Gibt es kantonale Vorgaben? |
| 3 | Verhalten bei ITCS-Ausfall nicht beschrieben | Was sollen die Anzeigen zeigen, wenn keine Echtzeitdaten verfügbar sind? Statischen Fahrplan oder Ausfallmeldung? |
| 4 | SLA für die nationale Plattform nicht bekannt | Welche Verfügbarkeits- und Latenzanforderungen stellt die Plattform an die SIRI-Feeds? |

---

## Modul 4: Functional Requirements

*Simulierte Ausgabe des Requirements Refiner Agent auf Basis der Business Requirements, der Interviewprotokolle und des Stakeholder-Registers.*

---

### Functional Requirements (MASTeR-Satzmuster)

Das MASTeR-Satzmuster: `<Bedingung> soll das System <Verb> <Objekt> <Detail>.`
«soll» = verbindlich. «sollte» = wünschenswert, kann abgewogen werden.

---

#### A. Stammdaten und Echtzeit-Eingang

**FR-001 — Fahrplanimport**
Das System soll geplante Fahrplandaten via Schnittstelle IF-02 im NeTEx-Format mindestens einmal täglich importieren.

- **Übergeordnetes BR:** BR-02
- **Priorität:** must
- **Akzeptanzkriterien:**
  - Gegeben: Eine gültige NeTEx-Datei wird um 02:00 bereitgestellt
  - Wenn: Der Import läuft
  - Dann: Alle Fahrten der nächsten 14 Tage sind vor 02:30 in PRISMA verfügbar und das Importergebnis wird protokolliert
  - Und: Falls die Datei die Schemavalidierung nicht besteht, wird der zuvor gültige Datensatz beibehalten und IT-Betrieb innerhalb von 5 Minuten alarmiert

**FR-002 — ITCS-Echtzeitdaten-Subskription**
Das System soll Fahrzeugpositions- und Fahrtfortschrittsdaten vom ITCS via Schnittstelle IF-01 abonnieren und Aktualisierungen mindestens alle 10 Sekunden verarbeiten.

- **Übergeordnetes BR:** BR-02, BR-05
- **Priorität:** must
- **Akzeptanzkriterien:**
  - Gegeben: Eine aktive ITCS-Verbindung
  - Wenn: Ein Positions-Update eintrifft
  - Dann: Die geschätzte Abfahrtszeit der betroffenen Haltestellen wird innerhalb von 5 Sekunden neu berechnet
  - Und: Wenn für eine laufende Fahrt seit mehr als 90 Sekunden kein Update eingegangen ist, wird die Schätzung als «veraltet» markiert

---

#### B. Störungserfassung

**FR-003 — Störung erstellen mit Pflichtattributen**
Wenn ein authentifizierter Disponent eine neue Störung erfasst, soll das System die Pflichtattribute Ursache, Schweregrad, betroffenes Gebiet, Gültigkeitsbeginn und Quelltext verlangen.

- **Übergeordnetes BR:** BR-01, BR-04
- **Priorität:** must
- **Akzeptanzkriterien:**
  - Gegeben: Ein angemeldeter Disponent
  - Wenn: Er eine Störung erstellt
  - Dann: Kann die Störung nur gespeichert werden, wenn alle Pflichtattribute ausgefüllt sind
  - Und: Die Ursache ist auf die standardisierte Taxonomie gemäss Glossar beschränkt (kein Freitext-Ursachenfeld)

**FR-004 — Meldungsvorlagen mit Freitext-Feld**
Wenn eine Störungsursache ausgewählt wird, soll das System eine vorgefertigte Meldungsvorlage anbieten, die ein begrenztes Freitext-Feld von maximal 240 Zeichen enthält.

- **Übergeordnetes BR:** BR-04, BR-07
- **Priorität:** must
- **Akzeptanzkriterien:**
  - Gegeben: Eine ausgewählte Störungsursache
  - Wenn: Der Disponent das Textfeld öffnet
  - Dann: Ist die Vorlage vorausgefüllt, das Freitext-Feld erzwingt die Zeichenbegrenzung mit Live-Zähler
  - Und: Die Vorlage enthält vorübersetzte Textbausteine für alle vier Sprachen

**FR-005 — Kanalauswahl gemäss Kanalmatrix**
Bei der Erstellung einer Störung soll das System die Zielkanäle aus Schweregrad und betroffenem Gebiet gemäss Kanalmatrix bestimmen und dem Disponenten die Abwahl von Kanälen — mit Ausnahme der nationalen Plattform — nur mit Angabe eines Grundes ermöglichen.

- **Übergeordnetes BR:** BR-01, BR-03
- **Priorität:** must
- **Akzeptanzkriterien:**
  - Gegeben: Eine Störung mit Schweregrad «major»
  - Wenn: Die Kanäle bestimmt werden
  - Dann: Sind Haltestellenanzeige, App-Push, App-Liste, Website, nationale Plattform und Kundendienst-Ansicht vorausgewählt
  - Und: Die nationale Plattform kann nicht abgewählt werden
  - Und: Wird ein anderer Kanal abgewählt, muss der Disponent einen Grund erfassen

---

#### C. Freigabe und Übersetzung

**FR-006 — Freigabe-Workflow nach Schweregrad**
Wenn eine Störung den Schweregrad «major» oder «severe» hat, soll das System vor der Veröffentlichung die Freigabe durch einen diensthabenden Pikettoffizier verlangen. Bei Schweregrad «information» oder «minor» soll keine Freigabe erforderlich sein.

- **Übergeordnetes BR:** BR-01
- **Priorität:** must
- **Akzeptanzkriterien:**
  - Gegeben: Eine Störung mit Schweregrad «severe»
  - Wenn: Der Disponent die Veröffentlichung auslöst
  - Dann: Wird die Störung in den Status «wartet auf Freigabe» versetzt und der Pikettoffizier wird benachrichtigt
  - Und: Erst nach Freigabe erfolgt die Verteilung an die Kanäle

**FR-007 — Mehrsprachige Meldungsgenerierung**
Bei der Freigabe soll das System aus dem strukturierten Inhalt lokalisierte Meldungen in Deutsch, Französisch, Italienisch und Englisch innerhalb von 60 Sekunden generieren.

- **Übergeordnetes BR:** BR-07
- **Priorität:** must
- **Akzeptanzkriterien:**
  - Gegeben: Eine freigegebene Störung
  - Wenn: 60 Sekunden vergangen sind
  - Dann: Existieren Meldungen in allen vier Sprachen
  - Und: Falls die automatische Übersetzung fehlschlägt, wird ein Fallback-Verfahren angewendet und die betroffene Sprache markiert

---

#### D. Verteilung

**FR-008 — Verteilung an alle Kanäle**
Nach der Freigabe oder Genehmigung soll das System die Störungsmeldung innerhalb von 10 Sekunden an alle ausgewählten Kanäle verteilen.

- **Übergeordnetes BR:** BR-02
- **Priorität:** must
- **Akzeptanzkriterien:**
  - Gegeben: Eine freigegebene Störung mit den Zielkanälen Haltestellenanzeige, App und Website
  - Wenn: Die Freigabe erteilt wird
  - Dann: Ist die Meldung innerhalb von 10 Sekunden auf allen drei Kanälen verfügbar
  - Und: Jeder Verteilversuch wird mit Zeitstempel, Kanal und Ergebnis protokolliert

**FR-009 — Abfahrtszeilen für Haltestellenanzeigen**
Das System soll Abfahrtszeilen pro Haltestelle an den Display-Adapter liefern, sortiert nach geschätzter Abfahrtszeit, mit Countdown in ganzen Minuten bis 59 Minuten und als Uhrzeit darüber hinaus.

- **Übergeordnetes BR:** BR-05
- **Priorität:** must
- **Akzeptanzkriterien:**
  - Gegeben: Eine Haltestelle mit drei bevorstehenden Abfahrten
  - Wenn: Die Anzeige die Daten abruft
  - Dann: Werden die Abfahrten in aufsteigender Reihenfolge angezeigt
  - Und: Ein Estimate von 45 Minuten wird als «45» angezeigt, ein Estimate von 61 Minuten als Uhrzeit (z. B. «14:32»)

**FR-010 — SIRI-SX-Feed für die nationale Plattform**
Das System soll einen SIRI-SX-Situation-Exchange-Feed für abonnierte Konsumenten bereitstellen und bei jeder Statusänderung einer Störung innerhalb von 10 Sekunden ein Update senden.

- **Übergeordnetes BR:** BR-03
- **Priorität:** must
- **Akzeptanzkriterien:**
  - Gegeben: Eine aktive Subskription der nationalen Plattform
  - Wenn: Eine Störung erstellt, aktualisiert oder aufgehoben wird
  - Dann: Wird innerhalb von 10 Sekunden eine SIRI-SX-Nachricht an alle Abonnenten gesendet
  - Und: Die Nachricht enthält codierte Ursachen gemäss der standardisierten Taxonomie
  - Und: Heartbeat-Anfragen werden innerhalb von 5 Sekunden beantwortet

---

### Traceability-Übersicht

| FR | Übergeordnetes BR | Schwerpunkt |
|---|---|---|
| FR-001 | BR-02 | Fahrplanimport (NeTEx) |
| FR-002 | BR-02, BR-05 | ITCS-Echtzeitdaten |
| FR-003 | BR-01, BR-04 | Störungserfassung |
| FR-004 | BR-04, BR-07 | Meldungsvorlagen |
| FR-005 | BR-01, BR-03 | Kanalauswahl |
| FR-006 | BR-01 | Freigabe-Workflow |
| FR-007 | BR-07 | Mehrsprachige Generierung |
| FR-008 | BR-02 | Verteilung an Kanäle |
| FR-009 | BR-05 | Haltestellenanzeigen |
| FR-010 | BR-03 | SIRI-SX-Feed |

---

### Vom Agent erkannte, aber nicht detailliert ausgearbeitete Bereiche

- **Korrektur und Aufhebung veröffentlichter Störungen** — muss noch als separates FR spezifiziert werden (vgl. BR-01)
- **Audit-Trail / Kommunikationshistorie** — noch kein FR vorhanden, obwohl der regulatorische Kontext dies nahelegt
- **Aggregation von Fahrzeugdaten** — die negative Anforderung BR-09 erfordert ein FR, das die Aggregierung vor dem Reporting sicherstellt
- **Veralterungsanzeige** — was passiert, wenn Daten veraltet sind? Noch kein FR, das das Degradationsverhalten definiert
- **Service-Desk-Ansicht** — vom Kundendienst gefordert, aber noch nicht als FR formuliert
