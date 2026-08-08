# UC-002 — Störung freigeben und publizieren

| | |
|---|---|
| **ID** | UC-002 |
| **Zielebene** | Benutzerziel (sea level) |
| **Primärer Akteur** | Disponent/in (P1 Nadia, STK-02) |
| **Unterstützende Akteure** | Pikett-Verantwortliche/r, Übersetzungsdienst, Kanaladapter |
| **Stakeholder und Interessen** | Fahrgast: korrekte Information, schnell. Betrieb: haftungssichere Formulierung. BAV: standardkonformer Datenfeed. |
| **Auslöser** | Die Disponentin / der Disponent hat eine entworfene Störung (UC-001) und entscheidet, dass sie die Fahrgäste erreichen muss |
| **Status** | baselined |
| **Traces to** | BR-01, BR-02, BR-04, BR-07, BR-09 |

## Vorbedingungen

1. Die Disponentin / der Disponent ist authentifiziert mit der Rolle `prisma.dispatcher` (IF-08).
2. Eine Störung existiert im Status `draft` mit allen Pflichtfeldern: Schweregrad, Ursache,
   betroffener Bereich, Gültigkeitsbeginn, deutscher Quelltext.
3. Mindestens ein Kanaladapter meldet den Status `available`.

## Erfolgsgarantie (Nachbedingung)

1. Die Störung hat den Status `published`.
2. Lokalisierte Meldungen existieren in DE, FR, IT, EN.
3. Jeder gemäss Schweregrad-Regel ausgewählte Kanal hat entweder den Empfang bestätigt oder wurde
   als fehlgeschlagen mit geplantem Wiederholungsversuch erfasst.
4. Ein unveränderlicher Audit-Eintrag dokumentiert, wer was wann an welche Kanäle freigegeben hat.

## Minimalgarantie

Die Störung verbleibt in einem konsistenten Status, und jede teilweise Publikation ist erfasst und
für die Disponentin / den Disponenten sichtbar. Kein Kanal enthält eine Meldung, von der PRISMA nichts weiss.

## Hauptszenario

| # | Akteur | Schritt |
|---|---|---|
| 1 | Disponent/in | Öffnet die entworfene Störung und wählt *Freigeben*. |
| 2 | PRISMA | Validiert die Vollständigkeit und den Gültigkeitszeitraum gegen die aktuelle Zeit. |
| 3 | PRISMA | Ermittelt die erforderliche Freigabestufe anhand der Schweregrad-Regel (FR-010). |
| 4 | PRISMA | Schweregrad ist `minor`: keine Zweitfreigabe erforderlich. |
| 5 | PRISMA | Generiert die lokalisierten Meldungen für DE, FR, IT, EN aus dem strukturierten Inhalt (FR-011). |
| 6 | PRISMA | Ermittelt die Zielkanäle anhand von Schweregrad und betroffenem Bereich (FR-012). |
| 7 | PRISMA | Rendert jede Meldung in die kanalspezifische Form: Anzeige-Banner, App-Payload, Web-Eintrag, SIRI-SX-Situation, Leitstellen-Ansicht. |
| 8 | PRISMA | Übermittelt an jeden Kanaladapter und sammelt die Bestätigungen. |
| 9 | PRISMA | Setzt den Status auf `published` und schreibt den Audit-Eintrag. |
| 10 | PRISMA | Zeigt der Disponentin / dem Disponenten eine Publikationszusammenfassung mit Kanalstatus und Zeitstempeln an. |

## Alternative Abläufe

**3a — Schweregrad ist `major` oder `severe`**
1. PRISMA setzt den Status auf `awaiting_approval` und benachrichtigt die Pikett-Verantwortliche / den Pikett-Verantwortlichen.
2. Pikett-Verantwortliche/r genehmigt → weiter bei Schritt 5.
3. Pikett-Verantwortliche/r lehnt mit Kommentar ab → Status geht zurück auf `draft`, Disponent/in wird benachrichtigt. Use Case endet.
4. Keine Entscheidung innerhalb von 4 Minuten → PRISMA eskaliert an die zweite Pikett-Verantwortliche / den zweiten Pikett-Verantwortlichen und vermerkt die Verzögerung im Audit-Trail.

**5a — Automatische Übersetzung nicht verfügbar**
1. PRISMA publiziert die deutsche Meldung sofort auf allen Kanälen.
2. PRISMA markiert die anderen Sprachen als `pending` und wiederholt den Versuch alle 30 s während 10 Minuten.
3. Falls weiterhin nicht verfügbar, publiziert PRISMA den vorübersetzten Vorlagensatz ohne das
   Freitextfeld und markiert die Störung für manuelle Übersetzung.
   *Begründung: Teilinformation ist besser als keine — siehe NFR-006.*

**6a — Disponent/in übersteuert die Kanalauswahl**
1. Disponent/in deselektiert einen Kanal mit einem obligatorischen Grund aus einer festen Liste.
2. Übersteuerung und Grund werden im Audit-Eintrag festgehalten. Weiter bei Schritt 7.
   *Einschränkung: Der Kanal zur nationalen Plattform kann nicht deselektiert werden (CON-02).*

## Ausnahmeabläufe

**8a — Ein Kanaladapter bestätigt nicht innerhalb von 20 s**
1. PRISMA markiert den Kanal als `failed` und wiederholt den Versuch mit exponentiellem Backoff während 15 Minuten.
2. Die Publikationszusammenfassung zeigt den Fehler an; die Störung erreicht dennoch den Status `published`,
   wenn mindestens ein Kanal erfolgreich war.
3. Falls alle Kanäle fehlschlagen, wird der Status `publication_failed` gesetzt und ein Alarm an den
   IT-Betrieb ausgelöst (STK-05).

**2a — Gültigkeitszeitraum bereits abgelaufen**
PRISMA verweigert die Freigabe und nennt das ungültige Feld. Status bleibt `draft`.

**\*a — Verlust der Sitzung der Disponentin / des Disponenten in einem beliebigen Schritt**
Die Störung wird mit ihrem letzten konsistenten Status bewahrt. Nach erneuter Authentifizierung
sieht die Disponentin / der Disponent die Störung und ihren Publikationsstatus.

## Nichtfunktionale Erwartungen zu diesem Use Case

| ID | Erwartung |
|---|---|
| NFR-001 | Schritte 2–10 werden innerhalb von 20 s beim 95. Perzentil abgeschlossen |
| NFR-002 | Die Freigabeaktion erfordert maximal drei Interaktionen ab der geöffneten Störung |
| NFR-008 | Die Publikation ist idempotent — eine wiederholte Freigabe erzeugt kein Duplikat auf einem Kanal |
| NFR-013 | Der Audit-Eintrag ist append-only und wird 3 Jahre aufbewahrt (BR-09) |

## Offene Punkte

- OPN-04: Muss eine `severe`-Störung freigegeben werden, wenn die Pikett-Verantwortliche / der Pikett-Verantwortliche selbst die Autorin / der Autor ist?
