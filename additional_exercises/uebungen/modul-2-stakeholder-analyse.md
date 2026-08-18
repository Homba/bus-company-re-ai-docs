# Modul 2: Stakeholder-Analyse (25 Min. kompakt / 60 Min. vollständig)

> **Kompaktformat:** Nur Übung 1 durchführen (20 Min.) + 5 Min. Vergleich mit der Referenzlösung.
> Übungen 2 und 3 sind Selbststudium.

## Lernziele

- Den Stakeholder Analyst Agent einsetzen, um Stakeholder zu identifizieren und zu kategorisieren
- Konflikte zwischen Stakeholder-Interessen erkennen
- AI-generierte Stakeholder-Analysen auf Vollständigkeit und Korrektheit prüfen
- Verstehen, wie die Stakeholder-Analyse in die Anforderungserhebung einfliesst

## Setup

Konfigurieren Sie den **Stakeholder Analyst** Agent mit dem System Prompt aus
`werkzeuge/agentenbeispiele/01-stakeholder-analyst.md`.

> **Tipp für Gemini-Nutzende:** Sie können die Markdown-Dateien direkt als Datei-Upload
> in AI Studio hochladen, statt den Inhalt per Copy-Paste einzufügen.

## Übung 1: Erste Stakeholder-Identifikation (20 Min.)

**Geben Sie dem Agent folgende Unterlagen:**
1. Das Projektbriefing (`ausgangsmaterial/projektbriefing.md`)
2. Die Interviewprotokolle (`ausgangsmaterial/interview-transkripte.md`)

**Prompt:**
> «Analysiere die Stakeholder für dieses Projekt. Identifiziere alle Stakeholder, die in
> den folgenden Unterlagen erwähnt oder impliziert werden, klassifiziere sie, bewerte ihre
> Interessen und ihren Einfluss, erkenne Konflikte und erstelle eine RACI-Matrix.»

**Bewerten Sie die Ausgabe:**
- [ ] Hat der Agent alle explizit genannten Stakeholder identifiziert? (mindestens 9)
- [ ] Hat er Stakeholder abgeleitet, die nicht ausdrücklich genannt wurden? (z. B. DSB, IT-Betrieb, ITCS-Lieferant)
- [ ] Sind die Bewertungen von Interesse und Einfluss plausibel?
- [ ] Hat er mindestens 2 Konflikte erkannt?
- [ ] Ist die RACI-Matrix für die wichtigsten Aktivitäten vollständig?

## Übung 2: Iterative Verfeinerung (20 Min.)

Die erste Ausgabe ist selten vollständig. Fordern Sie den Agent heraus:

**Prompt-Ideen:**
- «Gibt es Stakeholder, die von diesem Projekt betroffen sind, aber in keinem Interview
  erwähnt wurden? Denke an den Kontext des Schweizer öffentlichen Verkehrs.»
- «Der Konflikt mit der Personalvertretung bezüglich Fahrerüberwachung — wie sollte dieser
  gelöst werden? Welche Anforderung würde deren Bedenken adressieren?»
- «Welche Stakeholder könnten dieses Projekt blockieren? Wie lässt sich das mitigieren?»
- «Die Behindertenorganisation wurde erwähnt, aber nicht interviewt. Welche Fragen würden
  Sie ihr stellen?»

**Kernkompetenz:** Der Mehrwert des Business Analyst liegt in den Rückfragen, nicht im ersten Prompt.
Der Agent liefert einen Entwurf — Sie machen ihn richtig.

## Übung 3: Abgleich mit der Referenzlösung (15 Min.)

Öffnen Sie `anforderungsspezifikation/01-stakeholders.md` und vergleichen Sie:

| Aspekt | Ihre Agent-Ausgabe | Referenzlösung |
|--------|-------------------|----------------|
| Anzahl identifizierter Stakeholder | | 15 (STK-01 bis STK-15) |
| Erkannte Konflikte | | 4 (C-1 bis C-4) |
| Abdeckung der RACI-Matrix | | 6 Aktivitäten × 15 Stakeholder |
| Abgeleitete Stakeholder | | DSB, IT-Betrieb, Personalvertretung, ITCS-Lieferant |

### Diskussionsfragen

1. Was hat der Agent übersehen, das in der Referenz enthalten ist? Woran könnte das liegen?
2. Was hat der Agent produziert, das die Referenz nicht enthält? Ist es valide?
3. Welche Stakeholder werden leicht übersehen, wenn man nur das Projektbriefing ohne Interviews liest?
4. Wie würden Sie den Agent-Prompt anpassen, um die erkannten Lücken zu schliessen?

## Erkenntnisse

- AI-Agents sind hervorragend darin, explizit genannte Stakeholder zu extrahieren und die
  Analyse zu strukturieren
- Sie übersehen oft Stakeholder, die sich aus dem institutionellen Kontext ergeben (Personalvertretungen
  in Schweizer/deutschen Unternehmen, Datenschutzbeauftragte, Aufsichtsbehörden wie das BAV)
- Die Qualität der Konflikterkennung hängt stark davon ab, ob Interviewprotokolle vorliegen, nicht nur Briefings
- Das Urteilsvermögen des Analysten ist nötig, um Einflussbewertungen zu validieren — der Agent kennt
  die internen politischen Verhältnisse nicht

## Ausgabe für das nächste Modul

Speichern Sie Ihr Stakeholder-Register — Sie werden es dem Requirements Elicitor in Modul 3 übergeben.
