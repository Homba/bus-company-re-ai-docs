# Workshop-Leitfaden — KI-gestütztes Requirements Engineering

## Lernziele

Am Ende dieses Workshops können die Teilnehmenden:

1. **Spezialisierte KI-Agents entwerfen** für verschiedene RE-Aufgaben (Stakeholder-Analyse, Erhebung,
   Verfeinerung, Use-Case-Erstellung, Validierung, Story Mapping)
2. **Wirksame System Prompts formulieren**, die RE-Methodik, Ausgabeformate und Qualitätskriterien
   in das Verhalten eines Agents einprogrammieren
3. **Anforderungen schrittweise verfeinern** — von einem groben Projektbriefing über Business Requirements,
   funktionale Spezifikationen, Use Cases bis zu User Stories — unter Einsatz von KI auf jeder Stufe
4. **KI-generierte Anforderungen kritisch bewerten** hinsichtlich typischer Mängel: Mehrdeutigkeit, fehlende
   Abnahmekriterien, nicht rückverfolgbare Ziele, implizite Annahmen
5. **Agent-Prompts anpassen** an unterschiedliche LLMs (Claude, Gemini) und verschiedene Projektkontexte

## Kerngedanke: Agents als Träger der RE-Methodik

Die zentrale Erkenntnis dieses Workshops lautet: **Ein gut gestalteter System Prompt ist eine formalisierte
RE-Methodik.** Wenn Sie einen Agent-Prompt schreiben, kodieren Sie darin:

- Welche Artefakte in welchem Format zu erstellen sind
- Welche Qualitätskriterien einzuhalten sind (Testbarkeit, Atomarität, Traceability)
- Welche Standards befolgt werden (ISO 29148, ISO 25010, Cockburn)
- Auf welche Fehler zu achten ist (mehrdeutiges «soll», fehlender Stakeholder, nicht rückverfolgbare Anforderung)
- Welcher Domänenkontext gilt (regulatorisches Umfeld, organisatorische Rahmenbedingungen)

Damit werden KI-Agents nicht nur zu Produktivitätswerkzeugen, sondern zu **Werkzeugen der Methodendurchsetzung** — sie
helfen Analysten, Praktiken konsequent einzuhalten, die unter Zeitdruck gerne abgekürzt werden.

## Vorbereitung für Workshop-Leitende

### Benötigte Materialien
- Jede teilnehmende Person benötigt Zugang zu Claude (claude.ai, Claude Code oder API) oder Gemini
  (AI Studio oder API)
- Ausgangsmaterialien aus `starting-materials/` ausdrucken oder digital bereitstellen
- Referenzlösungen aus `docs/` zum Vergleich bereithalten
- Optional: Beamer für Live-Demos von Agent-Interaktionen

### Raumeinrichtung
- Teilnehmende arbeiten einzeln oder zu zweit
- Jedes Paar/jede Person hat einen Laptop mit LLM-Zugang
- Die Workshop-Leitung führt jeden Agent vor, bevor die Übung beginnt

### Zeitplanung (Standard: Halbtagesformat)

Der Workshop ist auf **90 Min. + Pause + 180 Min.** ausgelegt (~4,5 Stunden Instruktionszeit).

**Block 1 — Grundlagen (90 Min.):**
- Einführungspräsentation mit `intro-script.md` (20 Min.)
- Setup & Demo «generisch vs. Agent» — Modul 1 (15 Min.)
- Stakeholder-Analyse — Modul 2, komprimiert (25 Min.)
- Business Requirements — Modul 3 (30 Min.)

**Pause (15–30 Min.)**

**Block 2 — Vertiefung (180 Min.):**
- Functional & Quality Requirements — Modul 4 (60 Min.)
- Use Cases — Modul 5 *(optional, bei Zeitrückstand überspringen)* (35 Min.)
- Validation & Traceability — Modul 6 (40 Min.)
- Backlog & User Stories — Modul 7 *(optional, bei Zeitrückstand überspringen)* (25 Min.)
- Abschluss — Modul 8 (15 Min.)
- Puffer für Diskussion (5 Min.)

**Kernpfad** (bei sehr knapper Zeit): Einführung → Module 1, 3, 4, 6, 8.
Dies deckt Erhebung, Verfeinerung und Validierung ab — die drei wirkungsvollsten KI-Anwendungsfälle.

**Alternative: 2-Stunden-Kurzformat:** Einführung + Modul 1 + Modul 3 + Modul 6

## Ablauf der Übungen

Jedes Übungsmodul enthält:

1. **Kontext** — welche RE-Phase behandelt wird und warum sie wichtig ist
2. **Agent-Einrichtung** — der zu verwendende System Prompt mit Erläuterung der wichtigsten Designentscheide
3. **Aufgabe** — welche Eingaben der Agent erhält und welches Ergebnis erwartet wird
4. **Bewertungskriterien** — woran sich beurteilen lässt, ob die KI-Ausgabe ausreichend gut ist
5. **Referenzlösung** — Verweis auf das entsprechende Artefakt in `docs/`
6. **Diskussionsfragen** — Fragen für die Gruppenreflexion

### Der schrittweise Verfeinerungsfluss

```
Modul 2                 Modul 3                Modul 4
Stakeholder-     →      Business         →     Functional &
Analyse                 Requirements           Quality Reqs
                                                    │
Modul 7                 Modul 6                Modul 5
Backlog &        ←      Validation &     ←     Use Cases &
Stories                  Traceability           Szenarien
```

Die Ausgabe jedes Moduls wird zur Eingabe für das nächste. Dies spiegelt die reale RE-Praxis wider und zeigt,
wie spezialisierte Agents zu einem durchgängigen Workflow verkettet werden.

## Tipps für maximalen Workshop-Ertrag

- **Ersten Entwurf nicht einfach akzeptieren.** Die eigentliche Kompetenz liegt im Dialog: den Agent
  hinterfragen, Entscheide begründen lassen, auf mehr Präzision drängen.
- **LLMs vergleichen.** Wenn Sie Zugang zu Claude und Gemini haben, probieren Sie denselben Prompt
  auf beiden aus und vergleichen Sie die Ergebnisse. Verschiedene Modelle haben unterschiedliche Stärken.
- **Prompts anpassen.** Die bereitgestellten Agent-Prompts sind Ausgangspunkte. Passen Sie sie an die
  Vorlagen, Standards und Terminologie Ihrer Organisation an.
- **Den Menschen im Prozess belassen.** Die Agents generieren Kandidaten. Die Analystin oder der Analyst
  entscheidet, was richtig ist. Achten Sie auf plausibel klingende Anforderungen, die nicht wirklich
  zur Fachdomäne passen.
