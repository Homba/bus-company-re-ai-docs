# Agent-Übersicht — Kurzreferenz für Teilnehmende

> Einseiter zum Ausdrucken. Zeigt alle Agents, ihre Aufgabe und wann sie im Workshop eingesetzt werden.

---

## Die 9 RE-Agents auf einen Blick

| # | Agent | Was er tut | Modul | Kern-Input | Kern-Output |
|---|-------|-----------|-------|------------|-------------|
| 1 | **Stakeholder Analyst** | Stakeholder identifizieren, Einfluss bewerten, Konflikte erkennen | 2 | Projektbriefing, Interviews | Stakeholder-Register, RACI-Matrix |
| 2 | **Requirements Elicitor** | Messbare Geschäftsziele aus Erzählungen extrahieren | 3 | Briefing, Interviews, Stakeholder-Register | Business Requirements (BR-nn) |
| 3 | **Requirements Refiner** | Anforderungen präzise, testbar und eindeutig machen | 4 | Entwurfs-BRs | Functional Requirements (FR-nnn) |
| 4 | **Quality Attribute Analyst** | Qualitätsanforderungen nach ISO 25010 spezifizieren | 4 | FRs, Interviews, Randbedingungen | Non-Functional Requirements (NFR-nnn) |
| 5 | **Use Case Author** | Use Cases im Cockburn-Stil mit allen Abläufen schreiben | 5 | FRs, NFRs, Personas | Use Cases (UC-nnn) |
| 6 | **Requirements Reviewer** | Anforderungen auf Mängel prüfen (Mehrdeutigkeit, Lücken, Widersprüche) | 6 | Beliebiges RE-Artefakt | Befundliste mit Schweregrad |
| 7 | **Traceability Checker** | Rückverfolgbarkeit prüfen, Lücken und verwaiste Anforderungen finden | 6 | Alle Anforderungen + Use Cases | Traceability-Matrix, Lückenanalyse |
| 8 | **Story Writer** | Sprint-fähige User Stories mit Akzeptanzkriterien ableiten | 7 | FRs, Use Cases | Epics, User Stories (US-nnn) |
| 9 | **Glossary Manager** | Begriffe extrahieren, definieren, Synonyme und Konflikte erkennen | 1–8 | Alle Projektdokumente | Kontrolliertes Glossar |

## Wie Sie einen Agent einrichten

```
1. System Prompt kopieren aus:  werkzeuge/agentenbeispiele/0X-agent-name.md
2. Als Systemanweisung setzen:
   - Claude Code → in CLAUDE.md ablegen
   - Claude Console → Projekt-Systemanweisung
   - Gemini AI Studio → Feld «System instructions»
3. Ausgangsmaterial als Nachricht senden
4. Iterieren: Ergebnis prüfen → Rückfragen stellen → verfeinern
```

## Der Verfeinerungsfluss

```
Projektbriefing          Stakeholder-      Business          Functional &
& Interviews        →    Register     →    Requirements  →   Quality Reqs
                         (Agent 1)         (Agent 2)         (Agent 3+4)
                                                                 │
User Stories ←  Traceability  ←  Review-    ←  Use Cases    ←────┘
(Agent 8)       Matrix            Befunde       (Agent 5)
                (Agent 7)         (Agent 6)
```

## 3 goldene Regeln

1. **Ersten Entwurf nie einfach übernehmen.** Der Agent liefert einen Kandidaten. Sie entscheiden.
2. **Rückfragen sind Ihr Werkzeug.** «Warum?», «Was fehlt?», «Was darf das System NICHT tun?»
3. **Vergleichen Sie mit der Referenz** in `anforderungsspezifikation/` — nicht als «die Antwort», sondern als Massstab.

---

*Workshop: KI-gestütztes Requirements Engineering — PRISMA-Fallstudie*
