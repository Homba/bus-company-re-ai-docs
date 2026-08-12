# Modul 4: Funktionale Anforderungen & Qualitätsanforderungen (60 Min. kompakt / 90 Min. vollständig)

> **Kompaktformat:** Übung 1 (25 Min.) + Übung 3 (25 Min.) + 10 Min. Vergleich durchführen.
> Übung 2 (schwache Anforderungen hinterfragen) und Übung 4 (vertiefte Analyse der Qualitätsanforderungen) sind Selbststudium.
>
> **Tipp für Gemini-Nutzende:** Sie können die Ausgangsmaterialien als Dateien hochladen
> (AI Studio → Datei-Upload), statt sie per Copy-Paste einzufügen.

## Lernziele

- Den Requirements Refiner einsetzen, um Geschäftsanforderungen in funktionale Anforderungen zu zerlegen
- Den Quality Attribute Analyst einsetzen, um Qualitätsanforderungen zu identifizieren und zu spezifizieren
- Die Satzschablone (Anforderungsschablone) für eindeutige Anforderungsformulierung anwenden
- Das Qualitätsmodell nach ISO/IEC 25010 verstehen

## Setup

Konfigurieren Sie zwei Agents für dieses Modul:
1. **Requirements Refiner** (`werkzeuge/agentenbeispiele/03-requirements-refiner.md`)
2. **Quality Attribute Analyst** (`werkzeuge/agentenbeispiele/04-quality-attribute-analyst.md`)

### Exkurs: Die Satzschablone (Anforderungsschablone)

Die Satzschablone stammt aus dem IREB-Lehrplan (Chris Rupp) und bietet ein festes Satzmuster
für die Formulierung von Anforderungen. In der agilen Praxis werden Anforderungen häufiger
als User Stories oder Use Cases formuliert — die Satzschablone bleibt aber nützlich, wenn
Anforderungen eindeutig, testbar und vertraglich belastbar sein müssen (z. B. in regulierten
Umgebungen, bei Ausschreibungen oder für Schnittstellenspezifikationen).

**Drei Varianten:**

| Variante | Muster |
|---|---|
| Selbständig | Das System **muss/soll/sollte/kann** `<Prozesswort>` `<Objekt>` `<Ergänzung>`. |
| Bedingt | Falls `<Bedingung>`, **muss/soll/sollte/kann** das System `<Prozesswort>` `<Objekt>` `<Ergänzung>`. |
| Ereignisgesteuert | Wenn/Sobald `<Ereignis>`, **muss/soll/sollte/kann** das System `<Prozesswort>` `<Objekt>` `<Ergänzung>`. |

**Verbindlichkeit der Schlüsselwörter:**

| Schlüsselwort | Verbindlichkeit |
|---|---|
| **muss** | Rechtlich verpflichtend |
| **soll** | Verbindlich (Standardfall) |
| **sollte** | Wünschenswert, kann abgewogen werden |
| **kann** | Optional, Vorschlag für zukünftige Erweiterung |

**Wann Satzschablone, wann User Story?**
- **Satzschablone:** Wenn die Anforderung vertraglich bindend, testbar und eindeutig sein
  muss — z. B. für Ausschreibungen, regulatorische Nachweise, Schnittstellenspezifikationen
- **User Story:** Wenn der Fokus auf dem Nutzerbedürfnis liegt und die Lösung im Team
  erarbeitet wird — z. B. in der Sprint-Planung
- In der Praxis lassen sich beide kombinieren: User Stories für die Kommunikation im Team,
  Satzschablone für die formale Spezifikation kritischer Anforderungen

In diesem Modul verwenden wir die Satzschablone, weil die PRISMA-Fallstudie ein reguliertes
Umfeld (Konzessionsauflagen, BAV-Audits) abbildet, in dem präzise, testbare Formulierungen
gefordert sind. In Modul 7 werden dieselben Anforderungen dann als User Stories formuliert.

---

## Teil A: Funktionale Anforderungen (45 Min.)

### Übung 1: Geschäftsanforderungen zerlegen (25 Min.)

**Geben Sie dem Requirements Refiner Agent folgende Unterlagen:**
1. Ihre Geschäftsanforderungen aus Modul 3
2. Die Interviewprotokolle (für den Kontext der Benutzerbedürfnisse)
3. Ihr Stakeholder-Register

**Prompt:**
> «Zerlege diese Geschäftsanforderungen in funktionale Anforderungen. Jede funktionale
> Anforderung soll ein spezifisches Systemverhalten nach der Satzschablone beschreiben.
> Gruppiere sie logisch. Jede funktionale Anforderung muss auf eine übergeordnete
> Geschäftsanforderung zurückführbar sein und testbare Akzeptanzkriterien haben.»

**Bewerten Sie die Ausgabe:**
- [ ] Verwendet jede funktionale Anforderung die Satzschablone? (`<Bedingung> soll das System <Verb> <Objekt>`)
- [ ] Ist jede funktionale Anforderung atomar (ein Verhalten pro Anforderung)?
- [ ] Ist jede funktionale Anforderung auf eine übergeordnete Geschäftsanforderung zurückführbar?
- [ ] Sind die Akzeptanzkriterien spezifisch genug, um daraus Tests abzuleiten?
- [ ] Sind Designentscheidungen in den Anforderungen enthalten? (es sollte das «Was» beschrieben werden, nicht das «Wie»)

### Übung 2: Schwache Anforderungen hinterfragen (20 Min.)

Nehmen Sie 3–5 der generierten funktionalen Anforderungen und hinterfragen Sie diese:

**Prompt-Ideen:**
- «Anforderung FR-nnn sagt ‹das System soll Fehler angemessen behandeln›. Was bedeutet
  ‹angemessen›? Formuliere das um mit spezifischem Verhalten für jede Fehlerbedingung.»
- «Anforderung FR-nnn sagt ‹das System soll mehrere Sprachen unterstützen›. Wie viele?
  Welche? Was bedeutet ‹unterstützen› — automatisch übersetzen? Vorübersetzte Vorlagen anzeigen?»
- «Diese Anforderung erwähnt ‹der Disponent wählt Kanäle aus einer Liste›. Das ist eine
  UI-Designentscheidung. Formuliere es um, sodass das Verhalten beschrieben wird, ohne
  die Oberfläche vorzuschreiben.»

**Kernkompetenz:** Der Requirements Refiner Agent erkennt viele schwache Formulierungen automatisch
(sein Prompt enthält eine Tabelle mit schwachen Wörtern). Aber domänenspezifische Mehrdeutigkeiten
erfordern Ihr Urteilsvermögen.

## Teil B: Qualitätsanforderungen (45 Min.)

### Übung 3: Qualitätsattribute identifizieren (25 Min.)

**Wechseln Sie zum Quality Attribute Analyst Agent.**

**Geben Sie ihm folgende Unterlagen:**
1. Ihre funktionalen Anforderungen aus Teil A
2. Die Interviewprotokolle (Stakeholder erwähnen Performance, Barrierefreiheit, Zuverlässigkeit)
3. Ihre Geschäftsanforderungen (einige sind von Natur aus qualitätsbezogen: BR-02 Geschwindigkeit,
   BR-06 Barrierefreiheit)

**Prompt:**
> «Identifiziere Qualitätsanforderungen für dieses System. Kategorisiere jede nach ISO/IEC 25010.
> Jede Qualitätsanforderung muss einen quantifizierten Schwellenwert, eine Messmethode und
> Akzeptanzkriterien haben. Achte besonders auf: Performance unter Last, Barrierefreiheit (WCAG),
> Datenschutz, Aktualität/Frische von Echtzeitdaten und Verfügbarkeit.»

**Bewerten Sie die Ausgabe:**
- [ ] Ist jede Qualitätsanforderung mit einem konkreten Schwellenwert quantifiziert?
- [ ] Ist die Messmethode für jede Qualitätsanforderung definiert?
- [ ] Sind die ISO 25010-Kategorien korrekt zugeordnet?
- [ ] Gibt es Qualitätsanforderungen für Performance, Zuverlässigkeit, Sicherheit, Benutzerfreundlichkeit und Datenschutz?
- [ ] Hat der Agent das Konzept der «ehrlichen Degradation» erkannt (wie verhält sich das System bei veralteten Daten)?

### Übung 4: Die Qualitätsanforderungen, nach denen niemand fragt (20 Min.)

**Fordern Sie den Agent auf, häufig übersehene Qualitätsattribute zu identifizieren:**

> «Was passiert, wenn das ITCS keine Daten mehr sendet? Wie soll sich das System verhalten,
> wenn Informationen veraltet sind? Definiere einen konkreten Schwellenwert für Datenalterung
> und das Degradationsverhalten.»

> «Das System empfängt Fahrzeugpositionen. Welche Datenschutzanforderungen gelten?
> Denke an das Schweizer Datenschutzgesetz (nDSG), Zweckbindung und Aufbewahrungsfristen.»

> «Wenn das System ausfällt, was ist die maximal akzeptable Wiederherstellungszeit? Was muss
> während eines Ausfalls erhalten bleiben?»

> «Die Haltestellenanzeigen zeigen Countdown-Timer. Wenn die zugrundeliegenden Daten 3 Minuten
> alt sind, soll die Anzeige einen möglicherweise falschen Countdown zeigen, oder soll sie
> Unsicherheit signalisieren? Definiere das als Qualitätsanforderung.»

### Vergleich mit der Referenzlösung

Öffnen Sie `anforderungsspezifikation/07-functional-requirements.md` und `anforderungsspezifikation/08-non-functional-requirements.md`:

| Aspekt | Ihre Ausgabe | Referenz |
|--------|-------------|----------|
| Funktionale Anforderungen | | 30 (FR-001 bis FR-030) |
| Qualitätsanforderungen | | 19 (NFR-001 bis NFR-019) |
| Abgedeckte ISO 25010-Kategorien | | 8 Kategorien |
| Qualitätsanforderungen mit quantifizierten Schwellenwerten | | 19/19 |

### Diskussionsfragen

1. Welche Qualitätsanforderungen waren für den Agent am schwierigsten zu quantifizieren? Warum?
2. Hat der Agent das Konzept der «ehrlichen Degradation» erkannt (NFR-005 in der Referenz)?
   Dies ist ein anspruchsvolles Qualitätsattribut — veraltete Daten führen zu einer bewussten
   Anpassung der Anzeige.
3. Wie haben Sie entschieden, ob etwas eine funktionale Anforderung oder ein Qualitätsattribut ist?
   (Hinweis: «Das System übersetzt Meldungen» ist funktional; «Übersetzungen sind innerhalb
   von 60 Sekunden verfügbar» ist ein Qualitätsattribut.)
4. Wie viele der 30 funktionalen Anforderungen in der Referenz sind tatsächlich notwendig? Könnten
   die gleichen Geschäftsziele mit weniger funktionalen Anforderungen erreicht werden?

## Ausgabe für das nächste Modul

Speichern Sie Ihre funktionalen Anforderungen und Qualitätsanforderungen — Sie werden sie verwenden,
um in Modul 5 Use Cases zu schreiben.
