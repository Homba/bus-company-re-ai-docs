# Prompt für Gemini: Workshop-Qualitätsprüfung

> **Anleitung:** Kopiere diesen gesamten Text als Nachricht in Gemini (AI Studio oder
> gemini.google.com). Hänge anschliessend alle Dateien aus `workshop/exercises/`,
> `workshop/starting-materials/` und `workshop/agents/` als Datei-Upload an — oder
> kopiere deren Inhalt unterhalb der Markierung `---WORKSHOP-INHALT---` am Ende dieses Prompts.

---

Du bist ein erfahrener Workshop-Designer und Requirements-Engineering-Experte. Ich bitte dich um ein detailliertes Review eines Workshops, den ich für Business Analysts entwickelt habe.

## Kontext

**Workshop-Titel:** KI-gestütztes Requirements Engineering
**Zielgruppe:** Business Analysts und Product Owner (deutschsprachig, Schweiz), die KI-Agents für Requirements Engineering einsetzen wollen
**Format:** Halbtagesformat — 90 Minuten + Pause + 180 Minuten (~4,5 Stunden netto)
**Sprache:** Deutsch (Schweizer Hochdeutsch), Agent-Prompts auf Englisch
**Tools:** Teilnehmende nutzen Claude oder Gemini als LLM-Plattform
**Fallstudie:** PRISMA — fiktives Fahrgastinformationssystem für ein Schweizer ÖV-Unternehmen

## Kernidee

Statt einer generischen KI erstellen die Teilnehmenden **8 spezialisierte Agents** (via System Prompts), die jeweils eine spezifische RE-Aufgabe abdecken. Der Workshop führt schrittweise vom rohen Projektbriefing über Business Requirements, funktionale Spezifikationen, Use Cases und Validierung bis zu User Stories.

## Zeitplan

### Block 1 — Grundlagen (90 Min.)

| Modul | Dauer | Inhalt | Agent |
|-------|-------|--------|-------|
| Einführungsvideo | 20 Min. | Fallstudie PRISMA vorstellen, Konzept «Agents als Methodenträger» erklären | — |
| Modul 1: Setup | 15 Min. | LLM-Zugang prüfen, Demo «generischer Prompt vs. Agent» | — |
| Modul 2: Stakeholder-Analyse | 25 Min. | Stakeholder identifizieren, Konflikte erkennen, RACI erstellen | Stakeholder Analyst |
| Modul 3: Business Requirements | 30 Min. | Messbare Ziele aus Briefing und Interviews extrahieren | Requirements Elicitor |

### Pause (15–30 Min.)

### Block 2 — Vertiefung (180 Min.)

| Modul | Dauer | Inhalt | Agent |
|-------|-------|--------|-------|
| Modul 4: Functional & Quality Requirements | 50 Min. | BRs in FRs zerlegen (MASTeR-Muster), NFRs nach ISO 25010 spezifizieren | Requirements Refiner + Quality Attribute Analyst |
| Modul 5: Use Cases *(optional)* | 35 Min. | Cockburn-Use-Cases schreiben, alternative/Ausnahme-Abläufe | Use Case Author |
| Modul 6: Validierung & Traceability | 35 Min. | Anforderungen auf Mängel prüfen, Traceability-Matrix erstellen | Requirements Reviewer + Traceability Checker |
| Modul 7: Backlog *(optional)* | 25 Min. | Epics und User Stories mit INVEST-Kriterien ableiten | Story Writer |
| Modul 8: Abschluss & Reflexion | 15 Min. | Erkenntnisse, Diskussion, nächste Schritte | — |
| Puffer | 20 Min. | Reserve für Diskussion / Überlauf | — |

**Kernpfad** (bei Zeitknappheit): Module 1, 3, 4, 6, 8 — Module 5 und 7 sind optional.

## Die 8 Agents

| # | Agent | RE-Aufgabe | Methodischer Kern |
|---|-------|------------|-------------------|
| 1 | Stakeholder Analyst | Stakeholder identifizieren, Interessen/Einfluss bewerten, Konflikte erkennen | RACI, Influence/Interest-Mapping |
| 2 | Requirements Elicitor | Business Requirements aus Narrativen extrahieren | ISO 29148, SMART-Ziele |
| 3 | Requirements Refiner | Anforderungen präzisieren und testbar machen | MASTeR-Satzmuster, Weak-Word-Detection |
| 4 | Quality Attribute Analyst | NFRs identifizieren und quantifizieren | ISO/IEC 25010, Messbarkeit |
| 5 | Use Case Author | Use Cases mit allen Abläufen schreiben | Cockburn-Methodik |
| 6 | Requirements Reviewer | Anforderungen auf Mängel inspizieren | Perspektivenbasiertes Lesen, IEEE 29148 |
| 7 | Traceability Checker | Rückverfolgbarkeit prüfen, Lücken finden | Bidirektionale Traceability |
| 8 | Story Writer | Sprint-fähige User Stories ableiten | INVEST-Kriterien, Given-When-Then |

## Ausgangsmaterialien

Die Teilnehmenden erhalten:
1. **Projektbeschrieb** (~100 Zeilen) — Ausgangslage, Problem, bestehende Systeme, Budget, Stakeholder-Liste
2. **Interviewprotokolle** (~180 Zeilen) — 6 simulierte Stakeholder-Interviews (Disponentin, Pendler, sehbehinderte Fahrgästin, Kundenberater, Datenschutzbeauftragter, BAV-Inspektor)

## Referenzlösungen

Als Vergleichsbasis liegt eine vollständige RE-Spezifikation vor (im `docs/`-Verzeichnis):
- 10 Business Requirements (BR-01 bis BR-10)
- 30 Functional Requirements (FR-001 bis FR-030)
- 19 Quality Requirements (NFR-001 bis NFR-019)
- 7 Use Cases (UC-001 bis UC-007)
- 4 Architecture Decision Records
- Vollständige Traceability-Matrix
- Stakeholder-Register mit 15 Stakeholdern und 4 Konflikten

---

## Meine Fragen an dich

Bitte prüfe den Workshop-Aufbau, den Zeitplan und die Inhalte. Gib mir ein strukturiertes Review mit folgenden Abschnitten:

### 1. Gesamtbewertung
- Ist der Workshop für die Zielgruppe (Business Analysts, Schweiz) geeignet?
- Ist die Kernbotschaft «Agents als Methodenträger» klar und überzeugend?
- Stimmt der Schwierigkeitsgrad?

### 2. Zeitplanung
- Sind die Zeitblöcke realistisch? Wo wird es eng?
- Ist die Aufteilung 90 + 180 Minuten sinnvoll?
- Sind die optionalen Module richtig gewählt?
- Wo sollte mehr / weniger Zeit eingeplant werden?

### 3. Didaktischer Aufbau
- Ist der progressive Verfeinerungsfluss (Stakeholder → BR → FR/NFR → UC → Validierung → Stories) schlüssig?
- Fehlen wichtige RE-Schritte oder -Themen?
- Ist die Balance zwischen Theorie und Praxis richtig?
- Wie gut funktioniert der Vergleich mit der Referenzlösung als Lernmethode?

### 4. Agent-Design
- Sind die 8 Agents sinnvoll aufgeteilt? Gibt es Überlappungen oder Lücken?
- Welche RE-Aufgaben fehlen und sollten als Agent abgedeckt werden?
- Ist die Entscheidung, die Prompts auf Englisch zu belassen, richtig?
- Wie könnte man die Agents für Gemini spezifisch optimieren?

### 5. Fallstudie PRISMA
- Ist die Fallstudie komplex genug, um echte RE-Herausforderungen zu zeigen?
- Ist sie zu komplex für ein Halbtagesformat?
- Sind die simulierten Interviews realistisch und ergiebig genug?
- Fehlen wichtige Stakeholder-Perspektiven?

### 6. Verbesserungsvorschläge
- Was sind die 5 wichtigsten Verbesserungen, die du empfiehlst?
- Gibt es Quick Wins (kleine Änderungen, grosse Wirkung)?
- Was würdest du für eine Volltagsversion anders machen?
- Welche Elemente fehlen, die den Workshop deutlich besser machen würden?

### 7. Risiken und Stolperfallen
- Was kann während des Workshops schiefgehen?
- Wo werden Teilnehmende wahrscheinlich Probleme haben?
- Wie robust ist der Workshop gegenüber unterschiedlichem Vorwissen der Teilnehmenden?
- Was passiert, wenn die LLM-Plattform (Claude/Gemini) während des Workshops Probleme hat?

### 8. Gemini-spezifische Empfehlungen
- Wenn Teilnehmende Gemini statt Claude nutzen: wo muss der Workflow angepasst werden?
- Welche Gemini-Features (z.B. Grounding, Code Execution, lange Kontextfenster) könnten
  den Workshop bereichern?
- Gibt es Gemini-spezifische Stärken oder Schwächen bei RE-Aufgaben?

---

Antworte auf Deutsch (Schweizer Hochdeutsch). Sei konkret und praxisorientiert — keine generischen Workshop-Tipps, sondern spezifische Verbesserungen für diesen Workshop.

---WORKSHOP-INHALT---

> Ab hier die Inhalte der Workshop-Dateien einfügen (Exercises, Agents, Starting Materials)
> oder als Datei-Upload anhängen.
