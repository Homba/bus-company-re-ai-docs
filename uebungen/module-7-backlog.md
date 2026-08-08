# Modul 7: Backlog & User Stories (25 Min. kompakt / 45 Min. vollständig)

> **Dieses Modul ist optional** im kompakten Zeitplan. Falls eingebunden, nur Übung 1
> durchführen (20 Min.) + 5 Min. Vergleich. Eignet sich auch gut als Selbststudium nach dem Workshop.

## Lernziele

- Den Story Writer Agent nutzen, um Anforderungen in Sprint-fähige User Stories zu zerlegen
- INVEST-Kriterien zur Bewertung der Story-Qualität anwenden
- Akzeptanzkriterien im Given-When-Then-Format schreiben
- Verstehen, wie formale Anforderungen auf agile Backlogs abgebildet werden

## Vorbereitung

Konfigurieren Sie den **Story Writer** Agent mit dem System Prompt aus
`werkzeuge/agentenbeispiele/08-story-writer.md`.

## Übung 1: Epics und Stories erstellen (25 Min.)

**Geben Sie dem Agent:**
1. Ihre Functional Requirements (aus Modul 4)
2. Ihre Use Cases (aus Modul 5)
3. Allfällige Abhängigkeitsinformationen aus Ihrer Traceability-Matrix

**Prompt:**
> «Organisieren Sie diese Anforderungen in Epics und zerlegen Sie sie in Sprint-fähige
> User Stories. Jede Story muss dem Format ‹Als ... / möchte ich ... / damit ...›
> folgen, mit Given-When-Then-Akzeptanzkriterien. Schätzen Sie Story Points und schlagen
> Sie eine Sprint-Reihenfolge unter Berücksichtigung der Abhängigkeiten vor. Verwenden
> Sie die Personas aus dem Projekt (Nadia die Disponentin, Beat der Pendler, Frau
> Lehmann die Screenreader-Nutzerin, Tobias der Kundenberater).»

**Bewerten Sie die Ausgabe:**
- [ ] Sind Epics thematisch kohärent (nicht bloss willkürliche Gruppierungen)?
- [ ] Erfüllt jede Story die INVEST-Kriterien?
- [ ] Sind Akzeptanzkriterien konkret und testbar?
- [ ] Sind die Story-Point-Schätzungen realistisch (nichts über 8)?
- [ ] Ist die Sprint-Reihenfolge logisch (Grundlagen vor Features)?
- [ ] Ist jede Story auf übergeordnete FRs zurückverfolgbar?

## Übung 2: Die Stories hinterfragen (15 Min.)

Wählen Sie 3 Stories aus und fordern Sie den Agent heraus:

**Für eine grosse Story (8+ Punkte):**
> «Diese Story ist zu gross für einen Sprint. Teilen Sie sie in kleinere, unabhängig
> lieferbare Stories auf.»

**Für eine Story ohne Grenzfälle:**
> «Was passiert in dieser Story, wenn die ITCS-Verbindung ausfällt? Wenn die Sitzung
> des Disponenten während der Erfassung abläuft? Fügen Sie Akzeptanzkriterien für
> diese Grenzfälle hinzu.»

**Für eine technische Story:**
> «Das liest sich wie eine technische Aufgabe, nicht wie eine User Story. Wer ist der
> Benutzer? Welchen Nutzen hat er? Schreiben Sie die Story so um, dass sie einem
> Stakeholder vorgeführt werden kann.»

### Vergleich mit der Referenz

Öffnen Sie `backlog/epics.md` und `backlog/sprint-04.md`:

| Aspekt | Ihre Ausgabe | Referenz |
|--------|-------------|----------|
| Anzahl Epics | | 9 (E1–E9) |
| Sprint-Umfang | | 10 Sprints |
| Beispiel-Sprint-Stories | | 5 Stories, 5–8 Punkte je Story |
| Stories mit Given-When-Then-Kriterien | | 5/5 |

## Übung 3: Sprint-Planungsübung (5 Min.)

**Prompt:**
> «Bei einer Team-Velocity von 30 Story Points pro Sprint: Planen Sie Sprint 4 (den
> ersten Sprint mit Fokus auf Release und Verteilung). Wählen Sie Stories aus, stellen
> Sie sicher, dass deren Abhängigkeiten durch vorherige Sprints erfüllt sind, und
> definieren Sie ein Sprint-Ziel.»

### Diskussionsfragen

1. Wie gut handhabt der Agent den Übergang von formalen Anforderungen zu agilen Stories?
   Was geht dabei verloren?
2. Sind die Akzeptanzkriterien spezifisch genug, damit ein QA-Engineer automatisierte
   Tests schreiben kann?
3. Wie sollten NFRs im Backlog erscheinen — als separate Stories oder als Kriterien auf
   funktionalen Stories?
4. Worauf basiert der Agent seine Story-Point-Schätzungen? Wie verlässlich ist das?

## Fazit

Der Story Writer Agent überbrückt die Lücke zwischen formalem Requirements Engineering (was der
Vertrag verspricht) und agiler Umsetzung (was das Team baut). Die formalen Anforderungen
bleiben die Baseline; Stories sind die Sprint-Ebenen-Zerlegung, die sich weiterentwickeln
kann, ohne dass ein Change Request nötig ist — solange sie innerhalb des Scopes ihres
übergeordneten FR bleiben.
