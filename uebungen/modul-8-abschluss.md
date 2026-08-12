# Modul 8: Abschluss & Reflexion (15 Min. kompakt / 30 Min. vollständig)

## Was wir behandelt haben

Im Verlauf dieses Workshops haben Sie:

1. **Stakeholder analysiert** — von einem rohen Projektbriefing zu einem strukturierten
   Register mit Konflikterkennung
2. **Business Requirements erhoben** — messbare Ziele aus Erzählungen extrahiert
3. **Zu Functional und Quality Requirements verfeinert** — unter Anwendung der Satzschablone,
   ISO 25010 und Qualitätskriterien
4. **Use Cases geschrieben** — im Cockburn-Stil mit alternativen und Ausnahmeabläufen
5. **Validiert und nachverfolgt** — Artefakte auf Mängel geprüft und Abdeckung verifiziert
6. **Ein Backlog erstellt** — Sprint-fähige User Stories mit Akzeptanzkriterien

Bei jedem Schritt haben Sie einen **spezialisierten KI-Agent** mit einem sorgfältig
erarbeiteten System Prompt verwendet, der RE-Methodik kodiert — nicht bloss generischen
KI-Chat.

## Zentrale Erkenntnisse

### 1. Agents sind Methodenträger, keine Magie

Die von Ihnen verwendeten System Prompts kodieren jahrzehntelange RE-Praxis: ISO 29148,
ISO 25010, Cockburn, Satzschablone, INVEST-Kriterien. Die KI «kennt» Requirements Engineering
nicht — sie folgt der Methodik, die Sie ihr vorgeben. Ein besserer Prompt liefert deutlich
bessere Ergebnisse.

### 2. Der Wert des Analysten liegt in der Iteration

Die erste Ausgabe jedes Agents ist ein Ausgangspunkt. Die eigentliche Kompetenz liegt in:
- Erkennen, was fehlt (Negativanforderungen, implizite Stakeholder)
- Hinterfragen von Lösung-als-Anforderung-Verwechslungen
- Einfordern von Messbarkeit und Testbarkeit
- Einbringen von Domänenwissen, über das die KI nicht verfügt

### 3. Verschiedene Aufgaben brauchen verschiedene Agents

Ein einzelner «Anforderungen schreiben»-Prompt kann nicht die Qualität zweckgebauter Agents
für Stakeholder-Analyse, Erhebung, Verfeinerung, Validierung und Story-Erstellung erreichen.
Spezialisierung zählt — bei Menschen und bei KI-Agents.

### 4. KI glänzt bei Struktur, scheitert am Kontext

Die Agents sind hervorragend bei:
- Konsistente Formatierung und Strukturierung
- Erkennung schwacher Formulierungen und Mehrdeutigkeiten
- Aufbau von Traceability-Matrizen
- Zerlegung von Anforderungen in Standardmuster

Die Agents haben Mühe mit:
- Organisationspolitik und impliziten Machtverhältnissen
- Domänenspezifischem Regulierungswissen (ohne expliziten Kontext)
- Negativanforderungen (was das System NICHT tun darf)
- Einschätzung, ob eine Anforderung «gut genug» vs. überarbeitet ist

### 5. Verifikation ist nicht verhandelbar

KI-generierte Anforderungen sind standardmässig plausibel. Sie lesen sich gut. Sie folgen
dem Format. Aber plausibel ist nicht dasselbe wie korrekt. Jedes KI-generierte Artefakt
braucht ein menschliches Review — idealerweise mit einem strukturierten Review-Prozess
(wie Sie ihn in Modul 6 geübt haben).

## Reflexionsübung (15 Min.)

### Einzelreflexion (5 Min.)

Schreiben Sie Ihre Antworten auf:

1. Welcher Agent war für Ihre Arbeit am nützlichsten? Warum?
2. Welche RE-Aufgabe hat am wenigsten von KI-Unterstützung profitiert? Warum?
3. Was würden Sie an den verwendeten Agent-Prompts ändern?
4. Wie würden Sie diese Agents an den RE-Prozess Ihrer Organisation anpassen?

### Gruppendiskussion (10 Min.)

1. **Vertrauenskalibrierung:** Wie stark vertrauen Sie nach diesem Workshop KI-generierten
   Anforderungen? Welche Verifikation würden Sie hinzufügen, bevor Sie sie in einem realen
   Projekt einsetzen?

2. **Prozessintegration:** An welcher Stelle Ihres aktuellen RE-Prozesses würden Sie diese
   Agents einsetzen? Würden Sie sie für Erstentwürfe, Reviews oder beides verwenden?

3. **Agent-Verbesserung:** Welche zusätzlichen Agents wären nützlich? (Architekturentscheid-
   Dokumentierer? Glossar-Manager? Compliance-Checker?)

4. **LLM-Vergleich:** Falls Sie sowohl Claude als auch Gemini ausprobiert haben — welche
   Unterschiede haben Sie bei Anforderungsqualität, Formattreue und Domänenverständnis
   festgestellt?

## Nächste Schritte

### Für Ihre Projekte
- Beginnen Sie mit dem Agent, der Ihren grössten Schmerzpunkt adressiert (oft: Requirements
  Reviewer für bestehende Spezifikationen oder Requirements Elicitor für neue Projekte)
- Passen Sie die System Prompts an die Vorlagen und Standards Ihrer Organisation an
- Bauen Sie eine Bibliothek domänenspezifischen Kontexts auf, den Sie neben dem System Prompt
  einspeisen

### Für Ihr Team
- Teilen Sie die Agent-Prompts als Team-Werkzeuge — einheitliche Methodik über alle Analysten
- Nutzen Sie den Reviewer Agent für Peer Reviews — Vorprüfung vor der menschlichen Inspektion
- Verfolgen Sie, welche KI-Vorschläge akzeptiert vs. abgelehnt werden, um Prompts laufend
  zu verbessern

### Weiterführende Themen (nicht in diesem Workshop behandelt)
- Agents programmatisch verketten (Elicitor -> Refiner -> Reviewer Pipeline)
- System Prompts auf Basis vergangener Anforderungsmängel Ihrer Organisation optimieren
- KI für Anforderungsverhandlung und Konfliktlösung einsetzen
- Automatisierte Traceability-Pflege in CI/CD (siehe `werkzeuge/validate_requirements.py`)

## Ressourcen

- **Dieses Repository:** Referenzlösungen in `anforderungsspezifikation/`, Agent-Prompts in `werkzeuge/agentenbeispiele/`
- **ISO/IEC/IEEE 29148:2018:** Standard für Requirements Engineering
- **ISO/IEC 25010:** Software-Qualitätsmodell
- **Cockburn, A. «Writing Effective Use Cases»** — die in diesem Workshop verwendete Use-Case-Methodik
- **Chris Rupp, «Requirements-Engineering und -Management»** — Satzschablone (Anforderungsschablone)
