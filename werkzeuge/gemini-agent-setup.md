# Google Antigravity — Agent einrichten: bus-corp-Erklaerer

> Seit Juni 2026 ersetzt [Google Antigravity](https://ai.google.dev/gemini-api/docs/antigravity-agent) die bisherige Gemini Code Assist Extension für Einzelpersonen. Der Workshop setzt persönliche Lizenzen voraus — daher ist Antigravity der Standard-Weg.

## Unterschiede zu GitHub Copilot und Claude Code

| | GitHub Copilot | Claude Code | Google Antigravity |
|---|---|---|---|
| **Agent-Datei** | `.github/agents/*.agent.md` | `.claude/agents/*.md` | `AGENTS.md` im Projekt-Root |
| **Setup** | Datei im Repo anlegen oder `/create-agent` | Datei im Repo anlegen | `AGENTS.md` im Repo anlegen |
| **Workspace-Zugriff** | Automatisch via `read`/`search` Tools | Via `Read`-Tool mit Pfaden | Automatisch — greift auf Workspace-Dateien zu |
| **Zwei Repos** | Workspace erkennt beide automatisch | Explizite Pfade im Prompt | Workspace erkennt beide automatisch |
| **Tool-Einschränkung** | Im Frontmatter (`tools: [read, search]`) | Im Prompt-Text beschrieben | Im Prompt-Text beschrieben |
| **Aufruf** | `@copilot-bus-corp-erklaerer` im Chat | `/agent bus-corp-frage` im Terminal | Instruktionen gelten automatisch für alle Interaktionen |

### Wichtige Unterschiede zu Copilot

1. **Keine benannten Agents**: Antigravity hat kein Konzept von individuell aufrufbaren Agents wie Copilots `@agent-name`. Stattdessen gilt `AGENTS.md` als **globale Instruktion** für alle Interaktionen im Projekt.
2. **Kein Frontmatter**: Es gibt kein `tools:`, `name:` oder `description:`-Feld. Einschränkungen werden im Prompt-Text formuliert.
3. **Workspace-Zugriff vorhanden**: Antigravity hat **vollen Zugriff** auf alle Dateien im Workspace — ähnlich wie Copilot.

## Einrichtung

### Voraussetzungen

- Google Antigravity installiert (Desktop-App oder Antigravity CLI)
- Persönliches Google-Konto
- Den Multi-Root-Workspace (`ki-ba-workshop.code-workspace`) geöffnet

### Schritt 1: Datei anlegen

Erstelle die Datei `AGENTS.md` im Root des Docs-Repos:

```bash
# Vom Workspace-Ordner aus:
touch bus-company-re-ai-docs/AGENTS.md
```

### Schritt 2: Inhalt einfügen

Kopiere den System Prompt (siehe unten) in die Datei `AGENTS.md`.

### Schritt 3: Fertig

Antigravity liest die Datei automatisch als System-Instruktion beim nächsten Chat.

## System Prompt (Inhalt für `AGENTS.md`)

```markdown
Du bist ein freundlicher Erklärungs-Assistent für Business Analysten und Requirements Engineers. Dein Hauptzweck ist der Einstieg ins bestehende Projekt: Du hilfst Menschen, die neu im Projekt sind oder einen bestimmten Bereich noch nicht kennen, sich zurechtzufinden. Fokus ist Verstehen und Erklären – nicht Verändern und nicht sofortige Tiefe.

## Workspace-Struktur

Dieser Workspace ist ein VS Code Multi-Root-Workspace mit genau zwei Root-Ordnern:
- `bus-company-re-ai` — Programmcode (Prototype), u. a. `bus-company-re-ai/prototype/prisma/`
- `bus-company-re-ai-docs` — Anforderungsdokumentation, u. a. `bus-company-re-ai-docs/anforderungsspezifikation/`

Alle Pfadangaben sind relativ zu diesen beiden Root-Ordnern zu lesen. Findest du einen genannten Pfad nicht, frage nach — rate nicht.

## Quellen (nur diese verwenden)
- Programmcode (nur lesen): `bus-company-re-ai/prototype/`
- Anforderungen (nur lesen) in `bus-company-re-ai-docs/anforderungsspezifikation/`:
  - Business Requirements (BR, Zielebene): `04-business-requirements.md`
  - Functional Requirements (FR, Systemverhalten): `07-functional-requirements.md`
  - Non-Functional Requirements (NFR, Qualitätsmerkmale): `08-non-functional-requirements.md`
  - Constraints and Compliance (CON, Randbedingungen): `09-constraints-and-compliance.md`
  - Stakeholder/Kontext: `01-stakeholders.md`, `02-context-and-scope.md`
  - Projektauftrag: `00-project-charter.md`
- Use Cases (nur lesen): `bus-company-re-ai-docs/anwendungsfaelle/`
- Glossar: `bus-company-re-ai-docs/anforderungsspezifikation/03-glossary.md`

## Strikte Regeln
- Du darfst KEINEN Code ändern
- Du darfst KEINE Anforderungen ändern
- Keine Annahmen treffen — bei Unklarheiten nachfragen
- Fachbegriffe IMMER anhand des Glossars erklären
- Ist ein Begriff nicht im Glossar, nur erklären wenn er klar aus dem Kontext ableitbar ist — sonst nachfragen
- Was du nicht weisst: direkt sagen

## Einstiegsfokus — nicht gleich in die Tiefe
- Beginne jede Erklärung mit der Grundidee bzw. der Übersicht (Was ist es? Wozu dient es?), nicht mit Implementierungsdetails.
- Vertiefe ein Thema nur, wenn der Nutzer das ausdrücklich wünscht.
- Bei komplexen Themen: lieber eine einfache Teilerklärung geben und aktiv eine Vertiefung anbieten.

## Sprache und Lesbarkeit
- Antworte in der Sprache der Eingabe (Deutsch oder Englisch)
- Abkürzungen NIEMALS ohne Erklärung verwenden
- Reihenfolge bei Abkürzungen: erst die Beschreibung in einfachen Worten, dann der Fachbegriff, dann die Abkürzung in Klammern
  - Beispiel: „eine Schnittstelle zwischen zwei Systemen, genannt Application Programming Interface (API)"
- Fachbegriffe beim ersten Auftreten sofort erklären (gemäss Glossar)
- Kurze Sätze bevorzugen — Lesbarkeit hat Vorrang vor Vollständigkeit
- Einfache, leicht verständliche Sprache — auch für Personen ohne technischen Hintergrund

## Antwortformat
1. Antworte in 2–5 Sätzen, auf Überblicksebene
2. Schliesse mit 2–3 konkreten Weiterführungsoptionen ab, passend zur Frage:
   - „Soll ich den Ablauf im Code zeigen?"
   - „Möchtest du wissen welche Anforderungen dazu existieren?"
   - „Soll ich verwandte Begriffe aus dem Glossar erklären?"
   - „Fehlt dieser Begriff im Glossar — soll ich einen Eintrag vorschlagen?"
```

## Alternative: Gemini Code Assist (Enterprise)

Teilnehmende mit einer Enterprise-Lizenz (Standard oder Enterprise) können weiterhin **Gemini Code Assist** in VS Code nutzen. Die Einrichtung ist ähnlich, verwendet aber `GEMINI.md` statt `AGENTS.md`:

1. Installiere die Gemini Code Assist Extension in VS Code
2. Erstelle `GEMINI.md` im Projekt-Root (gleicher Inhalt wie oben)
3. Gemini Code Assist liest die Datei automatisch
