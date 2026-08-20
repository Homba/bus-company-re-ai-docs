# Gemini Code Assist — Agent einrichten: bus-corp-Erklaerer

> Diese Anleitung erklärt, wie Sie mit Gemini in VS Code einen wiederverwendbaren, projektspezifischen Agenten einrichten. Die Methode, wie Sie Gemini Anweisungen geben, hängt von Ihrem Kontotyp ab.

## Vergleich mit GitHub Copilot und Claude Code

| | GitHub Copilot | Claude Code | Gemini (mit Google Cloud-Lizenz) |
|---|---|---|---|
| **Agent-Datei** | `.github/agents/*.agent.md` | `.claude/agents/*.md` | `GEMINI.md` im Projekt-Root |
| **Setup** | Datei im Repo anlegen oder `/create-agent` | Datei im Repo anlegen | `GEMINI.md` im Repo anlegen |
| **Workspace-Zugriff** | Automatisch via `read`/`search`-Tools | Via `Read`-Tool mit Pfaden | Automatisch – greift auf Workspace-Dateien zu |
| **Zwei Repos** | Workspace erkennt beide automatisch | Explizite Pfade im Prompt | Workspace erkennt beide automatisch |
| **Tool-Einschränkung** | Im Frontmatter (`tools: [read, search]`) | Im Prompt-Text beschrieben | Im Prompt-Text beschrieben |
| **Aufruf** | `@copilot-bus-corp-erklaerer` im Chat | `/agent bus-corp-frage` im Terminal | Anweisungen gelten automatisch für alle Interaktionen |

### Wichtige Unterschiede zu Copilot

1. **Keine benannten Agenten**: Gemini hat kein Konzept von individuell aufrufbaren Agenten wie Copilots `@agent-name`. Stattdessen agiert die `GEMINI.md`-Datei als **globale Instruktion** für alle Interaktionen im Projekt.
2. **Kein Frontmatter**: Es gibt keine `tools:`, `name:` oder `description:`-Felder. Einschränkungen und Verhalten werden direkt im Prompt-Text definiert.
3. **Voller Workspace-Zugriff**: Gemini hat **vollen Zugriff** auf alle Dateien im VS Code-Workspace, ähnlich wie Copilot.

## Einrichtungsmethode 1: Agenten-Dateien mit `@` referenzieren (für alle Konten empfohlen)

Dies ist die flexibelste Methode und funktioniert für **alle Kontotypen** (persönliche und Google Cloud). Es ist der beste Weg, um zwischen verschiedenen Agenten-Personas zu wechseln, ohne Projektdateien zu ändern. Anstatt den gesamten System-Prompt zu kopieren, referenzieren Sie die Anweisungsdatei des Agenten direkt in Ihrer Chat-Nachricht.

1.  **Agenten-Datei auswählen**: Die Anweisungen für die Agenten sind in separaten Dateien gespeichert (z. B. `Uebung1_BusCorpErklaerer/gemini-bus-corp-erklaerer-agent.md`).
2.  **Neuen Chat starten**: Öffnen Sie eine neue Chat-Sitzung in der Gemini-Erweiterung.
3.  **Prompt mit `@` erstellen**: Schreiben Sie einen kurzen Prompt, der Gemini anweist, die Instruktionen aus der Agenten-Datei zu verwenden, um Ihre Quelldokumente zu analysieren. Verwenden Sie das `@`-Symbol, um die Dateien einfach zu referenzieren.

**Beispiel-Prompt:**
> Verwende die Anweisungen in `@workspace /bus-company-re-ai-docs/werkzeuge/agentenbeispiele/01-stakeholder-analyst.md`, um die Projekt-Stakeholder basierend auf den folgenden Dokumenten zu analysieren: `@workspace /bus-company-re-ai-docs/ausgangsmaterial/projektbriefing.md` und `@workspace /bus-company-re-ai-docs/ausgangsmaterial/interview-transkripte.md`.

Dieser Ansatz legt die Persona des Agenten nur für diese spezifische Chat-Sitzung fest. Dies ermöglicht es Ihnen, mehrere Chats mit unterschiedlichen Agenten gleichzeitig geöffnet zu haben, und vermeidet, dass Ihr Chat mit langen Anweisungsblöcken überladen wird.

## Einrichtungsmethode 2: `GEMINI.md` (nur für Google Cloud-Konten)

> **Hinweis für Multi-Agenten-Workflows:** Diese Methode richtet einen **einzigen, globalen Agenten** für das gesamte Projekt ein. Wenn Sie zwischen verschiedenen Agenten-Personas wechseln müssen (z. B. vom «Erklärer» zum «Requirements Refiner»), ist diese Methode nicht ideal, da Sie den Dateiinhalt manuell ändern müssen. Zum Wechseln zwischen Agenten wird **Methode 1 empfohlen.**

Diese Einrichtung verwendet die `GEMINI.md`-Datei, eine Funktion, die für Benutzer mit einem **Gemini für Google Cloud**-Abonnement (früher «Gemini Code Assist») verfügbar ist. Die «Gemini»-Erweiterung in VS Code erkennt diese Datei automatisch, wenn Sie mit einem lizenzierten Unternehmenskonto angemeldet sind.

### Voraussetzungen

- Die **«Gemini»**-Erweiterung in VS Code installiert (ID: `Google.gemini`).
- Ein Google Cloud-Konto mit einer aktiven Gemini für Google Cloud-Lizenz.
- Den Multi-Root-Workspace (`ki-ba-workshop.code-workspace`) geöffnet

### Schritt 1: Datei anlegen

Erstellen Sie die Datei `GEMINI.md` im Stammverzeichnis jedes Repositorys in Ihrem Arbeitsbereich, für das die Anweisungen gelten sollen.

```bash
# Vom Workspace-Ordner aus:
touch bus-company-re-ai/GEMINI.md
touch bus-company-re-ai-docs/GEMINI.md
```

### Schritt 2: Inhalt einfügen

Kopiere den System Prompt (siehe unten) in die `GEMINI.md` Datei.

### Schritt 3: Fertig

Die Gemini-Erweiterung liest die Datei automatisch als Systemanweisung für den nächsten Chat.

## System Prompt (Inhalt für `GEMINI.md`)

```markdown
Du bist ein freundlicher Erklärungs-Assistent für Business Analysten und Requirements Engineers. Dein Hauptzweck ist der Einstieg ins bestehende Projekt: Du hilfst Menschen, die neu im Projekt sind oder einen bestimmten Bereich noch nicht kennen, sich zurechtzufinden. Fokus ist Verstehen und Erklären – nicht Verändern und nicht sofortige Tiefe.

## Workspace-Struktur

Dieser Workspace ist ein VS Code Multi-Root-Workspace mit zwei Root-Ordnern:
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