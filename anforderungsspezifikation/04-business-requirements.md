# Geschäftsanforderungen

Zielebene. Jede BR beschreibt ein messbares geschäftliches Ergebnis, kein Systemverhalten.
Status: baselined, v1.2

---

### BR-01 — Einheitlicher, verbindlicher Störungseintrag

Die RVB soll pro Betriebsstörung genau einen verbindlichen Datensatz führen, aus dem alle
fahrgastseitigen Meldungen abgeleitet werden.

- **Begründung:** 27 % der Störungen wurden 2025 widersprüchlich kommuniziert, weil jeder
  Kanal manuell befüllt wurde.
- **Metrik:** Anteil der Störungen mit identischem Kerninhalt über alle Kanäle.
- **Baseline / Zielwert:** 73 % → ≥ 99 %.
- **Überprüfung:** Automatisierter wöchentlicher Inhaltsvergleich über alle Kanäle.
- **Stakeholder:** STK-01, STK-02, STK-04, STK-06
- **Priorität:** muss

---

### BR-02 — Geschwindigkeit vom Vorfall bis zum Fahrgast

Die RVB soll die Zeitspanne zwischen dem Bekanntwerden einer Störung in der Leitstelle und
der Sichtbarkeit der entsprechenden Meldung auf allen aktiven Kanälen reduzieren.

- **Metrik:** Mediane Latenz, Vorfallzeitstempel → Meldung sichtbar.
- **Baseline / Zielwert:** 11 Min. 40 s → ≤ 3 Min. (Median), ≤ 8 Min. (95. Perzentil).
- **Überprüfung:** Zeitstempelvergleich über ein rollendes 3-Monats-Fenster.
- **Stakeholder:** STK-01, STK-06, STK-08
- **Priorität:** muss

---

### BR-03 — Konzessionskonforme Datenlieferung

Die RVB soll Echtzeit-Betriebsdaten in den von der Konzession geforderten Formaten und mit
der geforderten Verfügbarkeit an die nationale Open-Data-Plattform liefern und damit die
BAV-Prüffeststellung vom 2024-11-08 schliessen.

- **Metrik:** Monatliche Feed-Verfügbarkeit und Konformitätstestergebnis.
- **Baseline / Zielwert:** kein Feed → ≥ 99,5 % Verfügbarkeit, Konformitätstest bestanden.
- **Überprüfung:** Plattformseitiges Monitoring plus Konformitätsprüfsuite des Plattformbetreibers.
- **Stakeholder:** STK-09, STK-10, STK-08
- **Priorität:** muss

---

### BR-04 — Geringerer Erfassungsaufwand in der Leitstelle

Die RVB soll den Aufwand reduzieren, den ein/e Disponent/in für die Kommunikation einer
Störung aufwendet, damit die Kommunikation während eines Vorfalls nicht mit operativen
Entscheidungen konkurriert.

- **Metrik:** Durchschnittliche Bearbeitungszeit pro Störung (Hands-on).
- **Baseline / Zielwert:** 6 Min. 20 s (drei Kanäle, manuell) → ≤ 2 Min.
- **Überprüfung:** Zeitstudie, 40 beobachtete Störungen nach Rollout.
- **Stakeholder:** STK-02, STK-01
- **Priorität:** muss

---

### BR-05 — Breitere Echtzeitabdeckung ohne ITCS-Ablösung

Die RVB soll den Anteil der Haltestellen mit Echtzeitinformation erhöhen und dabei eine
kanalagnostische Verteilungsschicht nutzen, sodass ein weiterer Anzeigenrollout keine
Softwareänderung erfordert.

- **Metrik:** Abdeckung = Haltestellen mit Echtzeitdaten / 412.
- **Baseline / Zielwert:** 14,8 % → ≥ 45 % bei vollständigem Rollout; 100 % erreichbar ohne Codeänderung.
- **Überprüfung:** Abgleich mit Anlagenverzeichnis; Architekturreview für die zweite Hälfte.
- **Stakeholder:** STK-08, STK-14, STK-06
- **Priorität:** soll

---

### BR-06 — Gleichberechtigter Zugang zu Informationen

Die RVB soll Fahrgastinformationen für Menschen mit Seh-, Hör- oder kognitiven
Beeinträchtigungen über alle digitalen Kanäle gleichwertig nutzbar machen.

- **Metrik:** Ergebnis des Konformitätsaudits; Aufgabenerfüllungsrate bei Tests mit assistiven Technologien.
- **Baseline / Zielwert:** Website teilweise konform → vollständige Konformität mit dem
  anwendbaren Barrierefreiheitsstandard; ≥ 90 % Aufgabenerfüllung mit Screenreader.
- **Überprüfung:** Externes Barrierefreiheitsaudit vor Go-live, abgenommen durch STK-15.
- **Stakeholder:** STK-07, STK-15
- **Priorität:** muss

---

### BR-07 — Mehrsprachiges Bediengebiet

Die RVB soll jede fahrgastseitige Meldung in Deutsch, Französisch, Italienisch und Englisch
publizieren, ohne dass ein/e Disponent/in vier Texte schreiben muss.

- **Metrik:** Anteil der freigegebenen Störungen, die innerhalb von 60 s nach Freigabe in allen vier Sprachen verfügbar sind.
- **Baseline / Zielwert:** 12 % (manuell, Deutsch zuerst) → ≥ 98 %.
- **Überprüfung:** Analyse des Publikationsprotokolls.
- **Stakeholder:** STK-04, STK-06, STK-08
- **Priorität:** muss

---

### BR-08 — Weniger informationsbezogene Beschwerden

Die RVB soll Beschwerden reduzieren, die auf fehlende oder falsche Fahrgastinformation
zurückzuführen sind.

- **Metrik:** Beschwerden mit Kategorie `information` pro Jahr.
- **Baseline / Zielwert:** 1 340 → ≤ 670.
- **Überprüfung:** Bericht aus dem Kundendienstsystem, 12 Monate nach vollständigem Rollout.
- **Stakeholder:** STK-04, STK-01, STK-08
- **Priorität:** soll

---

### BR-09 — Nachvollziehbare Kommunikationshistorie

Die RVB soll für jede vergangene Störung rekonstruieren können, was auf welchem Kanal zu
welchem Zeitpunkt kommuniziert wurde, und zwar für mindestens drei Jahre.

- **Begründung:** Haftungsfälle, BAV-Audits, kantonale Berichterstattung.
- **Metrik:** Anteil der in Stichproben geprüften historischen Störungen, die vollständig rekonstruierbar sind.
- **Baseline / Zielwert:** heute nicht möglich → 100 % der geprüften Fälle.
- **Überprüfung:** Auditübung anhand von 20 zufällig ausgewählten historischen Störungen.
- **Stakeholder:** STK-01, STK-08, STK-09
- **Priorität:** muss

---

### BR-10 — Keine verdeckte Leistungsüberwachung

Die RVB soll Fahrzeug- und Fahrtdaten ausschliesslich für Fahrgastinformation und aggregierte
Betriebsqualitätsauswertungen verwenden und soll keine individuelle Fahrer-Leistungsableitung
aus PRISMA ermöglichen.

- **Begründung:** Betriebsvereinbarung, Konflikt C-1 in `01-stakeholders.md`.
- **Metrik:** Ergebnis der Datenschutzprüfung; Abwesenheit fahrerbezogener Kennungen in den gespeicherten Daten.
- **Baseline / Zielwert:** DSFA ohne Vorbehalt genehmigt; null Fahrerkennungen im
  Reporting-Data-Mart.
- **Überprüfung:** DSFA-Freigabe (STK-11) plus Schemainspektion durch STK-13.
- **Priorität:** muss
