# Modul 4: Functional & Quality Requirements (60 Min. kompakt / 90 Min. vollständig)

> **Kompaktformat:** Übung 1 (25 Min.) + Übung 3 (25 Min.) + 10 Min. Vergleich durchführen.
> Übung 2 (schwache Anforderungen hinterfragen) und Übung 4 (vertiefte NFR-Analyse) sind Selbststudium.
>
> **Tipp für Gemini-Nutzende:** Sie können die Ausgangsmaterialien als Dateien hochladen
> (AI Studio → Datei-Upload), statt sie per Copy-Paste einzufügen.

## Lernziele

- Den Requirements Refiner einsetzen, um Business Requirements in Functional Requirements zu zerlegen
- Den Quality Attribute Analyst einsetzen, um Non-Functional Requirements zu identifizieren und zu spezifizieren
- Das MASTeR-Satzmuster für eindeutige Anforderungsformulierung anwenden
- Das Qualitätsmodell nach ISO/IEC 25010 verstehen

## Setup

Konfigurieren Sie zwei Agents für dieses Modul:
1. **Requirements Refiner** (`workshop/agents/03-requirements-refiner.md`)
2. **Quality Attribute Analyst** (`workshop/agents/04-quality-attribute-analyst.md`)

## Teil A: Functional Requirements (45 Min.)

### Übung 1: Business Requirements zerlegen (25 Min.)

**Geben Sie dem Requirements Refiner Agent folgende Unterlagen:**
1. Ihre Business Requirements aus Modul 3
2. Die Interviewprotokolle (für den Kontext der Benutzerbedürfnisse)
3. Ihr Stakeholder-Register

**Prompt:**
> «Zerlege diese Business Requirements in Functional Requirements. Jedes FR soll ein
> spezifisches Systemverhalten nach dem MASTeR-Satzmuster beschreiben. Gruppiere sie logisch.
> Jedes FR muss auf ein übergeordnetes BR zurückführbar sein und testbare Akzeptanzkriterien haben.»

**Bewerten Sie die Ausgabe:**
- [ ] Verwendet jedes FR das MASTeR-Satzmuster? (`<Bedingung> soll das System <Verb> <Objekt>`)
- [ ] Ist jedes FR atomar (ein Verhalten pro Anforderung)?
- [ ] Ist jedes FR auf ein übergeordnetes BR zurückführbar?
- [ ] Sind die Akzeptanzkriterien spezifisch genug, um daraus Tests abzuleiten?
- [ ] Sind Designentscheidungen in den Anforderungen enthalten? (es sollte das «Was» beschrieben werden, nicht das «Wie»)

### Übung 2: Schwache Anforderungen hinterfragen (20 Min.)

Nehmen Sie 3–5 der generierten FRs und hinterfragen Sie diese:

**Prompt-Ideen:**
- «FR-nnn sagt ‹das System soll Fehler angemessen behandeln›. Was bedeutet ‹angemessen›?
  Formuliere das um mit spezifischem Verhalten für jede Fehlerbedingung.»
- «FR-nnn sagt ‹das System soll mehrere Sprachen unterstützen›. Wie viele? Welche? Was
  bedeutet ‹unterstützen› — automatisch übersetzen? Vorübersetzte Vorlagen anzeigen?»
- «Dieses FR erwähnt ‹der Disponent wählt Kanäle aus einer Liste›. Das ist eine
  UI-Designentscheidung. Formuliere es um, sodass das Verhalten beschrieben wird, ohne
  die Oberfläche vorzuschreiben.»

**Kernkompetenz:** Der Requirements Refiner Agent erkennt viele schwache Formulierungen automatisch
(sein Prompt enthält eine Tabelle mit schwachen Wörtern). Aber domänenspezifische Mehrdeutigkeiten
erfordern Ihr Urteilsvermögen.

## Teil B: Quality Requirements (45 Min.)

### Übung 3: Quality Attributes identifizieren (25 Min.)

**Wechseln Sie zum Quality Attribute Analyst Agent.**

**Geben Sie ihm folgende Unterlagen:**
1. Ihre Functional Requirements aus Teil A
2. Die Interviewprotokolle (Stakeholder erwähnen Performance, Barrierefreiheit, Zuverlässigkeit)
3. Ihre Business Requirements (einige sind von Natur aus qualitätsbezogen: BR-02 Geschwindigkeit,
   BR-06 Barrierefreiheit)

**Prompt:**
> «Identifiziere Quality Requirements für dieses System. Kategorisiere jedes nach ISO/IEC 25010.
> Jedes NFR muss einen quantifizierten Schwellenwert, eine Messmethode und Akzeptanzkriterien haben.
> Achte besonders auf: Performance unter Last, Barrierefreiheit (WCAG), Datenschutz,
> Aktualität/Frische von Echtzeitdaten und Verfügbarkeit.»

**Bewerten Sie die Ausgabe:**
- [ ] Ist jedes NFR mit einem konkreten Schwellenwert quantifiziert?
- [ ] Ist die Messmethode für jedes NFR definiert?
- [ ] Sind die ISO 25010-Kategorien korrekt zugeordnet?
- [ ] Gibt es NFRs für Performance, Zuverlässigkeit, Sicherheit, Benutzerfreundlichkeit und Datenschutz?
- [ ] Hat der Agent das Konzept der «ehrlichen Degradation» erkannt (wie verhält sich das System bei veralteten Daten)?

### Übung 4: Die NFRs, nach denen niemand fragt (20 Min.)

**Fordern Sie den Agent auf, häufig übersehene Quality Attributes zu identifizieren:**

> «Was passiert, wenn das ITCS keine Daten mehr sendet? Wie soll sich das System verhalten,
> wenn Informationen veraltet sind? Definiere einen konkreten Schwellenwert für Datenalterung
> und das Degradationsverhalten.»

> «Das System empfängt Fahrzeugpositionen. Welche Datenschutzanforderungen gelten?
> Denke an das Schweizer Datenschutzgesetz (nDSG), Zweckbindung und Aufbewahrungsfristen.»

> «Wenn das System ausfällt, was ist die maximal akzeptable Wiederherstellungszeit? Was muss
> während eines Ausfalls erhalten bleiben?»

> «Die Haltestellenanzeigen zeigen Countdown-Timer. Wenn die zugrundeliegenden Daten 3 Minuten
> alt sind, soll die Anzeige einen möglicherweise falschen Countdown zeigen, oder soll sie
> Unsicherheit signalisieren? Definiere das als NFR.»

### Vergleich mit der Referenzlösung

Öffnen Sie `docs/07-functional-requirements.md` und `docs/08-non-functional-requirements.md`:

| Aspekt | Ihre Ausgabe | Referenz |
|--------|-------------|----------|
| Functional Requirements | | 30 (FR-001 bis FR-030) |
| Quality Requirements | | 19 (NFR-001 bis NFR-019) |
| Abgedeckte ISO 25010-Kategorien | | 8 Kategorien |
| NFRs mit quantifizierten Schwellenwerten | | 19/19 |

### Diskussionsfragen

1. Welche NFRs waren für den Agent am schwierigsten zu quantifizieren? Warum?
2. Hat der Agent das Konzept der «ehrlichen Degradation» erkannt (NFR-005 in der Referenz)?
   Dies ist ein anspruchsvolles Quality Attribute — veraltete Daten führen zu einer bewussten
   Anpassung der Anzeige.
3. Wie haben Sie entschieden, ob etwas ein Functional Requirement oder ein Quality Attribute ist?
   (Hinweis: «Das System übersetzt Meldungen» ist funktional; «Übersetzungen sind innerhalb
   von 60 Sekunden verfügbar» ist ein Quality Attribute.)
4. Wie viele der 30 FRs in der Referenz sind tatsächlich notwendig? Könnten die gleichen
   Geschäftsziele mit weniger FRs erreicht werden?

## Ausgabe für das nächste Modul

Speichern Sie Ihre Functional Requirements und Quality Requirements — Sie werden sie verwenden,
um in Modul 5 Use Cases zu schreiben.
