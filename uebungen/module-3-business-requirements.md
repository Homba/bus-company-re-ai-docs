# Modul 3: Business Requirements (30 Min. kompakt / 60 Min. vollständig)

> **Kompaktformat:** Übung 1 durchführen (20 Min.) + 10 Min. Vergleich mit der Referenzlösung.
> Übung 2 (harte Anforderungen herausarbeiten) ist Selbststudium, aber sehr empfehlenswert.

## Lernziele

- Den Requirements Elicitor Agent einsetzen, um Business Requirements aus Rohmaterial zu extrahieren
- Ziele von Lösungen und Randbedingungen unterscheiden
- Sicherstellen, dass jedes Business Requirement ein messbares Ziel hat
- Den Unterschied zwischen expliziten und impliziten Anforderungen verstehen

## Setup

Konfigurieren Sie den **Requirements Elicitor** Agent mit dem System Prompt aus
`workshop/agents/02-requirements-elicitor.md`.

> **Tipp für Gemini-Nutzende:** Sie können die Markdown-Dateien direkt als Datei-Upload
> in AI Studio hochladen, statt den Inhalt per Copy-Paste einzufügen.

## Übung 1: Business Requirements extrahieren (25 Min.)

**Geben Sie dem Agent folgende Unterlagen:**
1. Das Projektbriefing
2. Die Interviewprotokolle
3. Ihr Stakeholder-Register aus Modul 2

**Prompt:**
> «Extrahiere Business Requirements aus diesen Unterlagen. Ich benötige zielorientierte
> Anforderungen — messbare Ergebnisse, die das Projekt erreichen muss — keine funktionalen
> Spezifikationen. Jede Anforderung muss eine Baseline (Ist-Zustand) und ein Ziel (Soll-Zustand)
> haben. Identifiziere ausserdem Randbedingungen und Bereiche, in denen weitere Informationen
> benötigt werden.»

**Bewerten Sie die Ausgabe:**
- [ ] Sind die Anforderungen zielorientiert (Ergebnisse, nicht Features)?
- [ ] Hat jede ein messbares Ziel mit einer Baseline?
- [ ] Sind die Quellen auf bestimmte Stakeholder zurückgeführt?
- [ ] Hat der Agent Anforderungen von Randbedingungen unterschieden?
- [ ] Hat der Agent Lücken markiert und Rückfragen vorgeschlagen?

### Häufige AI-Stolperfallen

Der Agent wird wahrscheinlich einige Anforderungen produzieren, die in Wirklichkeit verkappte Lösungen sind:
- «Das System soll eine webbasierte Autorenoberfläche bereitstellen» → das ist eine Lösung, kein Ziel
- «Disponenten sollen Störungsmeldungen in unter 2 Minuten erstellen können» → das IST ein Ziel

**Hinterfragen Sie den Agent:** Fragen Sie bei jeder Anforderung, die nach einer Lösung klingt:
> «Warum braucht der Stakeholder das? Welches Problem wird damit gelöst? Formuliere es als
> zielorientiertes Business Requirement um.»

## Übung 2: Die schwierigen Anforderungen (20 Min.)

Einige Business Requirements werden selten explizit ausgesprochen. Fordern Sie den Agent heraus:

**Prompt-Ideen:**
- «Die Personalvertretung hat Bedenken bezüglich Fahrerüberwachung. Welches Business Requirement
  adressiert das? Denke daran: Eine Anforderung kann auch beschreiben, was das System NICHT tun darf.»
- «Das BAV verlangt SIRI-Feeds. Ist das ein Business Requirement oder eine Randbedingung? Was
  ist in diesem Fall der Unterschied?»
- «Die Behindertenorganisation möchte barrierefreie Informationen. Formuliere das als messbares
  Business Requirement, nicht nur als ‹barrierefrei sein›.»
- «Gibt es Anforderungen an die Nachvollziehbarkeit vergangener Ereignisse? Denke an
  regulatorische Rechenschaftspflicht.»

**Kernaussage:** Negative Anforderungen (BR-10: «keine verdeckte Fahrerüberwachung») und
Compliance-Anforderungen (BR-03: «konzessionskonforme Feeds») werden beim ersten Durchgang
häufig übersehen. Ein guter Analyst — und ein gut prompter Agent — sucht aktiv danach.

## Übung 3: Vergleich mit der Referenzlösung (15 Min.)

Öffnen Sie `docs/04-business-requirements.md` und vergleichen Sie:

| Aspekt | Ihre Agent-Ausgabe | Referenz (BR-01 bis BR-10) |
|--------|-------------------|---------------------------|
| Anzahl identifizierter BRs | | 10 |
| BRs mit messbaren Zielen | | 10/10 |
| Negative Anforderungen (darf-NICHT) | | 1 (BR-10) |
| Regulatorische/Compliance-BRs | | 2 (BR-03, BR-06) |
| Datenschutz-BRs | | 1 (BR-10) |

### Anforderungen, die der Agent häufig übersieht:

- **BR-05 (breitere Echtzeit-Abdeckung ohne ITCS-Ablösung):** Der Teil «ohne ITCS-Ablösung»
  ist eine in die Anforderung eingebettete Randbedingung — schwierig korrekt abzubilden
- **BR-07 (Mehrsprachigkeit innerhalb von 60 Sek.):** Das Zeitziel setzt voraus, dass man versteht,
  dass die Übersetzungsgeschwindigkeit relevant ist, nicht nur die Verfügbarkeit einer Übersetzung
- **BR-09 (auditierbare Historie):** Wird häufig übersehen, weil niemand explizit danach gefragt hat —
  es ergibt sich aus dem regulatorischen Kontext
- **BR-10 (keine verdeckte Fahrerüberwachung):** Negative Anforderungen sind bei der AI-gestützten
  Erhebung systematisch unterrepräsentiert

### Diskussionsfragen

1. Hat der Agent Business Requirements mit Randbedingungen vermischt? Woran erkennt man
   den Unterschied?
2. Waren einige der vorgeschlagenen Anforderungen in Wirklichkeit funktionale Spezifikationen?
3. Wie hat das Stakeholder-Register aus Modul 2 dem Agent geholfen, Anforderungen zu finden,
   die er allein aus dem Briefing übersehen hätte?
4. Was ist die richtige Anzahl Business Requirements für ein Projekt dieser Grössenordnung? Sind 10 zu wenig?
   Zu viele?

## Ausgabe für das nächste Modul

Speichern Sie Ihre Business Requirements — Sie werden sie dem Requirements Refiner in Modul 4 übergeben,
um sie in Functional Requirements und Quality Requirements zu zerlegen.
