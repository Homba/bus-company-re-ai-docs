# Modul 1: Setup & Einführung (15 Min. kompakt / 45 Min. vollständig)

> **Kompaktformat:** Die Einführungspräsentation (`workshop/intro-script.md`) ersetzt
> Teil A. Führen Sie Teil B (Setup, 10 Min.) + nur Schritt 2 von Teil C als kurze Demo (5 Min.) durch.

## Lernziele

- Aufbau des Workshop und die PRISMA-Fallstudie verstehen
- Die eigene AI-Agent-Umgebung einrichten (Claude oder Gemini)
- Verstehen, was einen guten Requirements Engineering Agent von einem generischen AI-Prompt unterscheidet
- Den schrittweisen Verfeinerungsfluss von der Vision bis zu Sprint-fähigen User Stories kennenlernen

## Teil A: Die Fallstudie (15 Min.)

Lesen Sie `workshop/starting-materials/project-brief.md`. Dies ist die Rohinformation, die Sie
als Business Analyst bei der Übernahme dieses Projekts erhalten würden. Beachten Sie:

- Die Problembeschreibung ist ein Mix aus Symptomen, Einschätzungen und impliziten Anforderungen
- Verschiedene Stakeholder legen Wert auf unterschiedliche Dinge
- Einige Randbedingungen sind explizit formuliert, andere verstecken sich im Kontext
- Es gibt keine formale Struktur — nur ein Projektbriefing und einige Notizen

Ihre Aufgabe in den nächsten 7 Modulen ist es, dieses Rohmaterial in eine vollständige, formale
Anforderungsspezifikation zu überführen — unter Einsatz spezialisierter AI-Agents, um jeden Schritt zu beschleunigen.

## Teil B: Einrichten der Agent-Umgebung (15 Min.)

Wählen Sie Ihre Plattform und prüfen Sie, ob Sie mit einem LLM interagieren können:

### Claude Code (empfohlen)
```bash
# Prüfen, ob Claude Code installiert ist
claude --version

# Eine einfache Interaktion testen
claude "Fasse das Hauptproblem in diesem Text zusammen: [ersten Absatz des Projektbriefings einfügen]"
```

### Claude Console (claude.ai)
1. Gehen Sie zu claude.ai
2. Starten Sie eine neue Konversation
3. Test: Fügen Sie einen Absatz aus dem Projektbriefing ein und bitten Sie um eine Zusammenfassung

### Gemini (AI Studio)
1. Gehen Sie zu aistudio.google.com
2. Erstellen Sie einen neuen Chat-Prompt
3. Test: Fügen Sie einen Absatz aus dem Projektbriefing ein und bitten Sie um eine Zusammenfassung

## Teil C: Generische AI vs. spezialisierte Agents (15 Min.)

### Übung: Der Unterschied, den ein System Prompt macht

**Schritt 1:** Fragen Sie Ihr LLM (ohne System Prompt):
> «Lies dieses Projektbriefing und identifiziere die Stakeholder.»
> [Projektbriefing einfügen]

Beachten Sie die Ausgabe. Sie wird brauchbar sein, aber generisch — vermutlich eine unstrukturierte
Aufzählung, bei der einige Stakeholder fehlen und keine Konfliktanalyse enthalten ist.

**Schritt 2:** Richten Sie nun den Stakeholder Analyst Agent ein:
- Kopieren Sie den System Prompt aus `workshop/agents/01-stakeholder-analyst.md`
- Setzen Sie ihn als Systemanweisung (Claude: CLAUDE.md; Gemini: Feld «System instructions»)
- Stellen Sie die gleiche Frage mit dem gleichen Projektbriefing

**Vergleichen Sie die beiden Ausgaben:**
- Identifiziert die Agent-Version mehr Stakeholder?
- Erkennt sie Konflikte zwischen Stakeholdern?
- Ist das Ausgabeformat strukturierter und konsistenter?
- Weist sie auf abgeleitete Stakeholder und Lücken hin?

### Diskussionsfragen

1. Was hat der System Prompt hinzugefügt, das die Ausgabe besser gemacht hat?
2. Welche Teile des System Prompt kodieren Requirements Engineering-Methodik und welche das Ausgabeformat?
3. Könnte man das gleiche Ergebnis erzielen, indem man jedes Mal eine sehr detaillierte Frage formuliert?
   Welche Vor- und Nachteile hat das?
4. Wann wäre ein generischer Prompt einem spezialisierten Agent überlegen?
