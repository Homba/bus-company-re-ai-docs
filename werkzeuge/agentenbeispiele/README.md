# RE Agent Prompts — Einrichtung & Verwendung

> **Hinweis zur Sprache der Agent-Prompts:** Die System Prompts in diesem Verzeichnis sind bewusst auf Englisch verfasst. LLMs arbeiten mit englischen Systemanweisungen am zuverlässigsten — die Ausgabequalität, das Befolgen komplexer Instruktionen und die Konsistenz sind in der Regel höher, wenn der System Prompt auf Englisch formuliert ist. Die Teilnehmenden interagieren jedoch ganz normal auf Deutsch mit den Agents: Fragen, Eingaben und Diskussionen finden auf Deutsch statt, und die Agents antworten ebenfalls auf Deutsch.

---

## Überblick

Dieses Verzeichnis enthält System Prompts für 9 spezialisierte Requirements Engineering Agents.
Jeder Prompt kodiert eine spezifische RE-Methodik, ein Ausgabeformat und einen Qualitätsstandard. Sie
funktionieren mit jedem leistungsfähigen LLM — Claude, Gemini, GPT oder lokalen Modellen.

## Agents verwenden

### Option A: Claude Code (empfohlen für den Workshop)

1. Ein Projektverzeichnis für den Agent erstellen
2. Den System Prompt des Agents in eine Datei namens `CLAUDE.md` in diesem Verzeichnis kopieren
3. `claude` in diesem Verzeichnis ausführen — der Agent verhält sich gemäss seinem System Prompt
4. Ausgangsmaterialien einfügen und im Gespräch iterieren

```bash
mkdir stakeholder-agent && cd stakeholder-agent
cp ../werkzeuge/agentenbeispiele/01-stakeholder-analyst.md CLAUDE.md
claude
# Now paste or reference the project brief and interview transcripts
```

### Option B: Claude API

```python
import anthropic

client = anthropic.Anthropic()

# Read the agent system prompt
with open("werkzeuge/agentenbeispiele/01-stakeholder-analyst.md") as f:
    system_prompt = f.read()

# Read starting materials
with open("ausgangsmaterial/projektbriefing.md") as f:
    brief = f.read()

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    system=system_prompt,
    messages=[
        {"role": "user", "content": f"Analyze stakeholders for this project:\n\n{brief}"}
    ]
)
```

### Option C: Gemini (AI Studio oder API)

1. Google AI Studio öffnen (aistudio.google.com)
2. Auf «Create new prompt» klicken → «Chat» wählen
3. Den System Prompt des Agents ins Feld «System instructions» einfügen
4. Gespräch starten, Ausgangsmaterialien als erste Nachricht einfügen

**Gemini API:**
```python
import google.generativeai as genai

genai.configure(api_key="YOUR_KEY")
model = genai.GenerativeModel(
    model_name="gemini-2.5-pro",
    system_instruction=open("werkzeuge/agentenbeispiele/01-stakeholder-analyst.md").read()
)
chat = model.start_chat()
response = chat.send_message(open("ausgangsmaterial/projektbriefing.md").read())
```

### Option D: Claude Custom Agents (fortgeschritten)

Für Teilnehmende, die eine Pipeline von Agents aufbauen möchten: Verwenden Sie das Claude Agent SDK oder
die Anthropic API, um Agents programmatisch zu verketten. Die Ausgabe eines Agents wird als Eingabe
für den nächsten verwendet.

## Agent-Übersicht

| # | Agent | Eingabe | Ausgabe | Zentrale Standards |
|---|-------|---------|---------|--------------------|
| 1 | Stakeholder Analyst | Projektbriefing, Interviews | Stakeholder-Register, Interessen-/Einfluss-Karte, Konflikte | — |
| 2 | Requirements Elicitor | Briefing, Interviews, Stakeholder-Register | Entwurf Business Requirements (BR-nn) | ISO 29148 |
| 3 | Requirements Refiner | Entwurfsanforderungen | SMART, testbare Anforderungen mit Abnahmekriterien | MASTeR-Muster |
| 4 | Quality Attribute Analyst | Functional Requirements, Randbedingungen | NFRs nach ISO 25010-Kategorien | ISO 25010, ISO 29148 |
| 5 | Use Case Author | Anforderungen, Personas | Use Cases im Cockburn-Stil mit allen Abläufen | Cockburn-Methodik |
| 6 | Requirements Reviewer | Beliebiges RE-Artefakt | Mängelliste mit Schweregrad, Fundstelle, Verbesserungsvorschlag | IEEE 29148 Qualitätskriterien |
| 7 | Traceability Checker | Vollständiges Anforderungsset | Abdeckungsmatrix, Erkennung verwaister Anforderungen, Lückenanalyse | ISO 29148 Traceability |
| 8 | Story Writer | Anforderungen, Use Cases, Epics | Sprintfähige User Stories mit Abnahmekriterien | INVEST-Kriterien |
| 9 | Glossary Manager | Alle Projektdokumente | Kontrolliertes Glossar, Terminologie-Konflikte | — |

## Designprinzipien hinter diesen Prompts

1. **Methodik zuerst:** Jeder Prompt kodiert, *wie* eine erfahrene Analystin oder ein erfahrener Analyst diese Aufgabe
   angeht — nicht nur, welches Ergebnis zu produzieren ist.
2. **Formatvorgaben:** Ausgabeformate sind präzise spezifiziert, damit die Ergebnisse über alle Teilnehmenden hinweg
   konsistent und vergleichbar sind.
3. **Selbstkritisch:** Die Agents sind angewiesen, Unsicherheiten zu kennzeichnen, klärende Fragen zu stellen
   und Annahmen explizit zu machen, anstatt stillschweigend zu raten.
4. **Domänenunabhängig:** Obwohl der PRISMA-Fall als Übungsbeispiel dient, funktionieren diese Prompts
   für jedes Projekt, indem der Domänenkontext angepasst wird.
5. **Pipeline-Kontext:** Jeder Agent beschreibt, welche Artefakte er von welchem Upstream-Agent erhält und
   welche Ergebnisse er an welchen Downstream-Agent weitergibt.
6. **Interaktionsprotokoll:** Jeder Agent stellt klärende Fragen, bevor er mit der Analyse beginnt —
   damit die Teilnehmenden den Umfang und Fokus steuern können.
7. **Worked Examples:** Jeder Prompt enthält ein ausgearbeitetes Beispiel aus der PRISMA-Domäne,
   das den erwarteten Input und Output konkret demonstriert.
8. **Reasoning-Anleitung:** Für komplexe Analyseschritte wird der Agent angeleitet, systematisch
   Schritt für Schritt zu denken, anstatt vorschnelle Schlüsse zu ziehen.
