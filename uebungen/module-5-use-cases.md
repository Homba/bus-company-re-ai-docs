# Modul 5: Use Cases & Szenarien (35 Min. kompakt / 60 Min. vollständig)

> **Dieses Modul ist optional** im kompakten Zeitplan. Wenn die Zeit knapp ist, überspringen
> Sie es — der Kernpfad führt von Modul 4 (Anforderungen) direkt zu Modul 6 (Validierung).
> Übung 1 eignet sich auch gut als Selbststudium.

## Lernziele

- Den Use Case Author Agent nutzen, um Use Cases im Cockburn-Stil zu schreiben
- Haupterfolgsszenario, alternative Abläufe und Ausnahmebehandlung identifizieren
- Sicherstellen, dass die Use Cases die Functional Requirements aus Modul 4 abdecken
- Die Beziehung zwischen Use Cases, Anforderungen und Testdesign verstehen

## Vorbereitung

Konfigurieren Sie den **Use Case Author** Agent mit dem System Prompt aus
`workshop/agents/05-use-case-author.md`.

> **Tipp für Gemini-Nutzende:** Sie können die Markdown-Dateien direkt als Datei-Upload
> in AI Studio hochladen, statt den Inhalt per Copy-Paste einzufügen.

## Übung 1: Einen zentralen Use Case schreiben (25 Min.)

Beginnen Sie mit dem wichtigsten Szenario: **Ein Disponent veröffentlicht eine Störungsmeldung.**

**Geben Sie dem Agent folgende Inputs:**
1. Ihre Functional Requirements zu Störungserfassung und -veröffentlichung
2. Relevante Interview-Transkripte (Nadia die Disponentin, Tobias der Kundenberater)
3. Ihr Stakeholder-Register

**Prompt:**
> «Schreiben Sie einen detaillierten Use Case für ‹Störungsmeldung erstellen und
> veröffentlichen›. Der primäre Akteur ist ein Disponent. Verwenden Sie Cockburns
> Struktur mit Haupterfolgsszenario, alternativen Abläufen und Ausnahmeabläufen.
> Verknüpfen Sie jeden Schritt mit den FRs, die er abdeckt. Der Use Case soll
> folgende Aspekte umfassen: Nachricht mit Vorlagen erstellen, Kanäle auswählen,
> Freigabe (falls erforderlich), mehrsprachige Veröffentlichung und Bestätigung.»

**Bewerten Sie die Ausgabe:**
- [ ] Gibt es ein klares Ziel pro Use Case?
- [ ] Wechseln die Schritte zwischen Akteur-Aktionen und Systemreaktionen ab?
- [ ] Sind Vorbedingungen und Nachbedingungen (Erfolgs- und Fehlergarantien) formuliert?
- [ ] Werden alternative Abläufe für mindestens 3 Erweiterungspunkte identifiziert?
- [ ] Sind Ausnahmeabläufe für Fehlersituationen definiert?
- [ ] Ist der Use Case auf spezifische FRs zurückverfolgbar?

### Häufige Probleme, die Sie ansprechen sollten:
- Schritte, die zu feingranular sind («klickt auf den Senden-Button») — Use Cases beschreiben
  Verhalten, keine UI-Interaktionen
- Fehlende Fehlergarantien — was passiert, wenn der Use Case bei Schritt 5 fehlschlägt?
- Alternative Abläufe, die eigentlich separate Use Cases sind (Aufteilung nötig)
- Fehlender «Freigabe-Workflow» als Erweiterung — gewisse Störungen benötigen eine Vorgesetztenfreigabe

## Übung 2: Einen konsumentenseitigen Use Case schreiben (20 Min.)

Schreiben Sie nun einen Use Case aus der Fahrgast-Perspektive.

**Prompt:**
> «Schreiben Sie einen Use Case für ‹Fahrgast sieht Abfahrtsinformationen an einer
> Haltestellenanzeige›. Der primäre Akteur ist ein Fahrgast. Das System umfasst die
> Haltestellenanzeige und das Echtzeit-Daten-Backend. Behandeln Sie: normale Countdown-
> Anzeige, was passiert, wenn eine Störung die angezeigte Linie betrifft, und was
> passiert, wenn der Datenfeed veraltet oder nicht verfügbar ist. Dieser Use Case soll
> die NFR zur ehrlichen Degradation abdecken.»

**Warum das wichtig ist:** Konsumentenseitige Use Cases zeigen Qualitätsanforderungen in Aktion. Das
Szenario der «ehrlichen Degradation» (NFR-005 in der Referenz) beschreibt den Fall, in dem die
Haltestellenanzeige darauf hinweisen muss, dass die Daten möglicherweise veraltet sind, anstatt einen
potenziell irreführenden Countdown anzuzeigen.

## Übung 3: Abdeckung überprüfen (15 Min.)

**Prompt an den Agent:**
> «Welche FRs sind anhand dieser Functional Requirements [fügen Sie Ihre FR-Liste ein]
> NICHT durch die beiden geschriebenen Use Cases abgedeckt? Welche zusätzlichen Use Cases
> werden für eine vollständige Abdeckung benötigt?»

Vergleichen Sie mit den Referenz-Use-Cases in `docs/use-cases/`:
- UC-001: Störung erstellen
- UC-002: Störung veröffentlichen
- UC-003: Korrektur oder Rückzug
- UC-004: Abfahrten an der Anzeige
- UC-005: Nationale Plattform Feed
- UC-006: Service-Desk-Anfrage
- UC-007: Audit-Rekonstruktion

### Diskussionsfragen

1. Wie viele Use Cases brauchen Sie für eine vollständige FR-Abdeckung? Ist ein Use Case pro FR zu viel?
2. Die Referenz trennt «Erstellen» und «Veröffentlichen» in UC-001 und UC-002. Hat Ihr Agent
   sie zusammengefasst? Welche Vor- und Nachteile hat das?
3. UC-007 (Audit-Rekonstruktion) deckt ein Compliance-Szenario ab. Hat Ihr Agent den Bedarf
   für diesen Use Case selbst erkannt, oder mussten Sie gezielt danach fragen?
4. Wie hängen Use Cases mit dem Testdesign zusammen? Könnte ein Tester Testfälle direkt
   aus Ihren Use Cases ableiten?

## Ergebnis für das nächste Modul

Speichern Sie Ihre Use Cases — Sie werden sie dem Requirements Reviewer in Modul 6
zusammen mit all Ihren anderen Artefakten für einen Validierungsdurchlauf zuführen.
