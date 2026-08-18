# Modul 6: Validierung & Traceability (40 Min. kompakt / 60 Min. vollständig)

> **Kompaktformat:** Führen Sie Übung 1 (15 Min.) + Übung 2 (10 Min.) + Übung 3 (10 Min.)
> \+ 5 Min. Diskussion durch. Übung 4 (Lückenanalyse) ist Selbststudium.
> **Übung 2 ist Pflicht** — der Lerneffekt, auch den «Goldstandard» zu hinterfragen, ist zentral.

## Lernziele

- Den Requirements Reviewer nutzen, um Ihre Artefakte auf Mängel zu prüfen
- Den Traceability Checker nutzen, um Abdeckung zu verifizieren und Lücken zu finden
- Perspektivenbasiertes Lesen verstehen (Benutzer, Entwickler, Tester, Compliance)
- KI-generierte Review-Ergebnisse kritisch bewerten lernen

## Vorbereitung

Konfigurieren Sie zwei Agents für dieses Modul:
1. **Requirements Reviewer** (`werkzeuge/agentenbeispiele/06-requirements-reviewer.md`)
2. **Traceability Checker** (`werkzeuge/agentenbeispiele/07-traceability-checker.md`)

> **Tipp für Gemini-Nutzende:** Laden Sie alle bisherigen Artefakte als Dateien hoch —
> Geminis grosses Kontextfenster profitiert davon, den gesamten Kontext zu sehen.

## Teil A: Requirements Review (30 Min.)

### Übung 1: Eigene Anforderungen prüfen (20 Min.)

**Geben Sie dem Requirements Reviewer Agent ALLE Ihre Artefakte:**
1. Business Requirements (aus Modul 3)
2. Functional Requirements (aus Modul 4)
3. Quality Requirements (aus Modul 4)
4. Use Cases (aus Modul 5)

**Prompt:**
> «Führen Sie eine formale Inspektion dieser Anforderungen durch. Prüfen Sie jede
> Anforderung anhand der Qualitätskriterien in Ihrer Checkliste. Klassifizieren Sie
> jeden gefundenen Mangel nach Schweregrad und Typ. Wenden Sie perspektivenbasiertes
> Lesen an: Prüfen Sie aus der Perspektive von Benutzer, Entwickler, Tester und
> Compliance. Geben Sie eine Gesamtbewertung ab.»

**Bewerten Sie die Review-Ausgabe:**
- [ ] Sind die Befunde spezifisch (exakte Anforderungs-ID, exakte problematische Formulierung)?
- [ ] Sind die Schweregrade angemessen (nicht alles ist «kritisch»)?
- [ ] Hat der Agent alle vier Perspektiven angewendet?
- [ ] Sind die Vorschläge konstruktiv und umsetzbar?
- [ ] Wurden schwache Formulierungen erkannt («angemessen», «schnell», «behandeln»)?

### Übung 2: Die Referenzlösung prüfen (10 Min.)

Dies ist die spannendste Übung: **Setzen Sie den Reviewer Agent auf den «Goldstandard» an.**

**Prompt:**
> «Prüfen Sie diese veröffentlichten Anforderungen auf Mängel.»
> [Inhalt aus anforderungsspezifikation/07-functional-requirements.md einfügen]

**Zentrale Erkenntnis:** Auch sorgfältig erarbeitete Referenzlösungen haben Schwachstellen.
Der Reviewer Agent sollte einige berechtigte Probleme finden. Diskutieren Sie:
- Welche Befunde sind echte Mängel vs. Fehlalarme?
- Kennzeichnet der Agent Dinge übermässig, die im Kontext eigentlich in Ordnung sind?
- Wie kalibriert man einen KI-Reviewer, um das Rauschen zu reduzieren?

## Teil B: Traceability-Prüfung (30 Min.)

### Übung 3: Die Traceability-Matrix erstellen (15 Min.)

**Geben Sie dem Traceability Checker Agent:**
1. Alle Ihre Anforderungen (BRs, FRs, NFRs)
2. Ihre Use Cases
3. Alle identifizierten Randbedingungen

**Prompt:**
> «Erstellen Sie eine vollständige Traceability-Matrix von den Business Requirements
> über die Functional und Quality Requirements bis zu den Use Cases. Identifizieren Sie:
> verwaiste Anforderungen (ohne übergeordnete Anforderung), Sackgassen-Anforderungen
> (ohne untergeordnete Anforderung oder Test), Abdeckungslücken (nicht vollständig
> heruntergebrochene Geschäftsziele) und Scope-Diskrepanzen.»

**Bewerten Sie die Ausgabe:**
- [ ] Ist jedes BR auf mindestens ein FR oder NFR zurückverfolgbar?
- [ ] Ist jedes FR auf mindestens einen Use Case zurückverfolgbar?
- [ ] Werden verwaiste Anforderungen identifiziert und erklärt?
- [ ] Sind Abdeckungslücken spezifisch und umsetzbar?

### Übung 4: Lückenanalyse (15 Min.)

Der Traceability Checker wird wahrscheinlich Lücken finden. Für jede Lücke:

1. Handelt es sich um eine echte fehlende Anforderung?
2. Ist es ein Artefakt der Art, wie Sie die Anforderungen zerlegt haben?
3. Muss man für weitere Informationen auf die Stakeholder zurückkommen?

**Vergleichen Sie mit** `anforderungsspezifikation/10-traceability-matrix.md` — die Referenz verfolgt jedes BR
über FR/NFR über UC bis zum Testfall (TC).

### Diskussionsfragen

1. Wie viel Review-Aufwand sollte KI-gestützt vs. menschlich sein? Wo bringt der KI-Reviewer
   den grössten Mehrwert?
2. Der KI-Reviewer generiert Befunde in Sekunden. Ein menschliches Review dauert Stunden.
   Aber welches erkennt die subtileren Probleme?
3. Würden Sie einem KI-Traceability-Checker in einer sicherheitskritischen Domäne vertrauen?
   Welche zusätzlichen Absicherungen wären nötig?
4. Wie gehen Sie mit dem «Fehlalarm-Problem» um — KI-Reviewer, die zu viele Nicht-Probleme
   kennzeichnen?

## Ergebnis für das nächste Modul

Speichern Sie Ihre Review-Befunde und die Traceability-Matrix. Beheben Sie alle kritischen
und schwerwiegenden Mängel in Ihren Anforderungen, bevor Sie mit Modul 7 (Backlog-Erstellung)
fortfahren.
