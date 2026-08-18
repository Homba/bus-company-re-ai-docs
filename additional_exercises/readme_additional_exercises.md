# Workshop: KI-gestütztes Requirements Engineering

> **Claude / Gemini Agents einsetzen, um Anforderungen vom Projektziel bis zu sprintfähigen User Stories zu verfeinern**

---

## Worum es in diesem Workshop geht

Dies ist ein praxisorientierter Workshop für **Business Analysts und Product Owner**, die lernen möchten, wie sie KI-Agents — Claude, Gemini oder andere leistungsfähige LLMs — nutzen können, um Requirements Engineering zu beschleunigen und qualitativ zu verbessern. Sie werden nicht einfach «eine KI bitten, Anforderungen zu schreiben». Stattdessen erstellen Sie **spezialisierte Agents**, die jeweils auf eine bestimmte RE-Aufgabe zugeschnitten sind, und setzen diese über alle Detaillierungsstufen hinweg ein: von der Stakeholder-Analyse über Business Requirements, funktionale Spezifikationen, Use Cases bis hin zu sprintfähigen User Stories.

Als Übungsbeispiel dient **PRISMA** — ein realistisches (fiktives) Fahrgastinformationssystem für ein regionales Schweizer Busunternehmen. Es ist komplex genug, um echte RE-Herausforderungen sichtbar zu machen: regulatorische Vorgaben, widersprüchliche Stakeholder-Interessen, Barrierefreiheit, Mehrsprachigkeit und die Integration von Altsystemen.

> **Prototyp:** Der lauffähige PRISMA-Prototyp befindet sich im separaten Repository [bus-company-re-ai](https://github.com/Homba/bus-company-re-ai). Dort kann die Fallstudie als interaktive Anwendung ausprobiert werden.

## Zielgruppe

- Business Analysts, die ihre RE-Praxis mit KI erweitern möchten
- Product Owner, die Anforderungen schreiben oder verfeinern
- Systemingenieure und Architekten, die an Spezifikationen mitwirken
- Workshop-Leitende, die RE-Methodik vermitteln

**Voraussetzungen:** Vertrautheit mit Requirements Engineering-Konzepten. Kein KI-/ML-Hintergrund nötig — der Workshop zeigt Schritt für Schritt, wie man Agents erstellt und einsetzt.

## Zeitplan (Halbtages-Workshop — 90 Min. + Pause + 180 Min.)

### Block 1 — Grundlagen (90 Min.)

| # | Modul | Dauer | Eingesetzte(r) Agent(s) |
|---|-------|-------|-------------------------|
| — | [Einführungspräsentation](uebungen/intro-skript.md) | 20 Min. | — |
| 1 | [Setup & Demo «generisch vs. Agent»](uebungen/modul-1-einfuehrung.md) | 15 Min. | — |
| 2 | [Stakeholder-Analyse](uebungen/modul-2-stakeholder-analyse.md) | 25 Min. | Stakeholder Analyst |
| 3 | [Business Requirements](uebungen/modul-3-geschaeftsanforderungen.md) | 30 Min. | Requirements Elicitor |

### Pause (15–30 Min.)

### Block 2 — Vertiefung (180 Min.)

| # | Modul | Dauer | Eingesetzte(r) Agent(s) |
|---|-------|-------|-------------------------|
| 4 | [Functional & Quality Requirements](uebungen/modul-4-funktionale-anforderungen.md) | 60 Min. | Requirements Refiner, Quality Attribute Analyst |
| 5 | [Use Cases & Szenarien](uebungen/modul-5-anwendungsfaelle.md) *(optional)* | 35 Min. | Use Case Author |
| 6 | [Validation & Traceability](uebungen/modul-6-validierung.md) | 40 Min. | Requirements Reviewer, Traceability Checker |
| 7 | [Backlog & User Stories](uebungen/module-7-backlog.md) *(optional)* | 25 Min. | Story Writer |
| 8 | [Abschluss & Reflexion](uebungen/modul-8-abschluss.md) | 15 Min. | — |
|   | *Puffer / Reserve für Diskussion* | *5 Min.* | |

Module mit dem Vermerk *(optional)* können bei Zeitknappheit ausgelassen werden — der Kernpfad (Module 1–4, 6, 8) deckt den gesamten RE-Lebenszyklus von der Erhebung bis zur Validierung ab. Die optionalen Module eignen sich hervorragend als Selbststudium nach dem Workshop.

Jedes Modul folgt dem gleichen Muster:
1. **Lernen** — kurze Einführung in die RE-Technik und was einen guten Agent dafür ausmacht
2. **Konfigurieren** — den spezialisierten Agent einrichten (System Prompt wird bereitgestellt)
3. **Anwenden** — den Agent auf den PRISMA-Fall anwenden, mit den bereitgestellten Ausgangsmaterialien
4. **Vergleichen** — das KI-gestützte Ergebnis mit der Referenzlösung in `anforderungsspezifikation/` abgleichen
5. **Reflektieren** — was hat der Agent gut gemacht? Wo brauchte es menschliches Urteilsvermögen?

## Verzeichnisstruktur

| Pfad | Zweck |
|------|-------|
| `ausgangsmaterial/` | Rohmaterialien für die Übungen (Projektbriefing, Interview-Transkripte) |
| `anforderungsspezifikation/` | Vollständige Anforderungsspezifikation als Referenzlösung (12 Kapitel) |
| `anwendungsfaelle/` | Use Cases im Cockburn-Stil |
| `adr/` | Architecture Decision Records |
| `backlog/` | Epics und Sprint-Planung |
| `uebungen/` | Workshop-Leitfaden, Übungsmodule, Handouts, Fallback-Material |
| `werkzeuge/` | Agent-System-Prompts und CI-Validierungsskript |
| `.github/` | Issue-Vorlagen, PR-Vorlage, CI-Workflow |

## Die PRISMA-Fallstudie (kurzer Überblick)

Regionalverkehr Bernland AG (RVB) ist ein regionales Busunternehmen (71 % in öffentlichem Besitz, 38 Linien, 412 Haltestellen). Ihre Fahrgastinformation ist mangelhaft:

- Störungsmeldungen werden manuell in 3 Kanäle eingetippt — in 27 % der Fälle mit inkonsistenten Formulierungen
- 11 Min. 40 Sek. mediane Verzögerung zwischen Ereignis und Fahrgast-Meldung
- Nur 61 von 412 Haltestellen haben Echtzeitanzeigen
- Das BAV hat die Nichteinhaltung der Datenlieferungspflichten beanstandet

**PRISMA** löst dies: ein einziger massgeblicher Störungsvorfall, automatisch an alle Kanäle verteilt, mehrsprachig, barrierefrei, auditierbar. Budget CHF 4,2 Mio., Pilot Q4 2026.

Siehe `ausgangsmaterial/projektbriefing.md` für das Rohbriefing, mit dem die Teilnehmenden starten.

## Die 9 spezialisierten Agents

Jeder Agent hat einen sorgfältig erstellten System Prompt, der RE-Best-Practices für seine spezifische Aufgabe abbildet. Die Teilnehmenden lernen, diese Agents zu konfigurieren, einzusetzen, zu bewerten und zu verbessern.

| # | Agent | RE-Aufgabe | Prompt |
|---|-------|------------|--------|
| 1 | Stakeholder Analyst | Stakeholder identifizieren, Interessen kartieren, Konflikte erkennen | [01-stakeholder-analyst.md](werkzeuge/agentenbeispiele/01-stakeholder-analyst.md) |
| 2 | Requirements Elicitor | Anforderungen aus Erzählungen und Interviews extrahieren | [02-requirements-elicitor.md](werkzeuge/agentenbeispiele/02-requirements-elicitor.md) |
| 3 | Requirements Refiner | Anforderungen SMART, messbar und testbar machen | [03-requirements-refiner.md](werkzeuge/agentenbeispiele/03-requirements-refiner.md) |
| 4 | Quality Attribute Analyst | NFRs nach ISO/IEC 25010-Kategorien spezifizieren | [04-quality-attribute-analyst.md](werkzeuge/agentenbeispiele/04-quality-attribute-analyst.md) |
| 5 | Use Case Author | Use Cases im Cockburn-Stil mit allen Abläufen schreiben | [05-use-case-author.md](werkzeuge/agentenbeispiele/05-use-case-author.md) |
| 6 | Requirements Reviewer | Auf Mehrdeutigkeit, Unvollständigkeit, Inkonsistenz prüfen | [06-requirements-reviewer.md](werkzeuge/agentenbeispiele/06-requirements-reviewer.md) |
| 7 | Traceability Checker | Anforderungsverknüpfungen und Abdeckungslücken validieren | [07-traceability-checker.md](werkzeuge/agentenbeispiele/07-traceability-checker.md) |
| 8 | Story Writer | Anforderungen in sprintfähige User Stories umwandeln | [08-story-writer.md](werkzeuge/agentenbeispiele/08-story-writer.md) |
| 9 | Glossary Manager | Begriffe extrahieren, definieren, Synonyme und Konflikte erkennen | [09-glossary-manager.md](werkzeuge/agentenbeispiele/09-glossary-manager.md) |

## Agents verwenden

Jeder Agent-Prompt funktioniert mit **Claude** (über Claude Code, API oder Konsole) oder **Gemini** (über AI Studio, API oder Vertex AI). Die Prompts sind LLM-unabhängige Systemanweisungen — einfach als System Prompt einfügen und die Interaktion starten.

Siehe `werkzeuge/agentenbeispiele/README.md` für detaillierte Einrichtungsanleitungen für beide Plattformen.

## Validator ausführen

```bash
python3 -m pip install pyyaml
python3 werkzeuge/validate_requirements.py
```

## Lizenz

CC0 1.0 — Public Domain. Frei verwendbar in Kursen, Schulungen, Konferenzen oder kommerziellen Workshops.
