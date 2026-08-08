# Funktionale Anforderungen

Status: baselined v1.4 für FR-001…FR-023; FR-024…FR-030 im Review.

Satzschablone: `<Bedingung> das System soll <Verb> <Objekt> <Detail>`.
`soll` = verbindlich. `sollte` = wünschenswert, kann abgewogen werden. `kann` = optional.
Jede FR benennt ihre übergeordnete BR und mindestens ein Abnahmekriterium.

---

## A. Stammdaten und Echtzeiteingang

**FR-001** — Das System soll geplante Fahrplandaten über IF-02 im NeTEx-Format mindestens
einmal täglich importieren.
*Übergeordnet:* BR-02 · *Priorität:* muss
*Abnahmekriterium:* Gegeben eine gültige NeTEx-Datei, die um 02:00 bereitgestellt wird, wenn
der Import läuft, dann sind alle Fahrten für die folgenden 14 Tage vor 02:30 in PRISMA
verfügbar und das Importergebnis ist protokolliert.

**FR-002** — Das System soll einen Fahrplanimport ablehnen, der die Schemavalidierung nicht
besteht, den zuvor gültigen Datensatz beibehalten und den IT-Betrieb innerhalb von 5 Minuten
alarmieren.
*Übergeordnet:* BR-02 · *Priorität:* muss
*Abnahmekriterium:* Gegeben eine fehlerhafte Datei, wenn der Import läuft, dann werden keine
bestehenden Daten überschrieben und ein Alarm wird ausgelöst.

**FR-003** — Das System soll Fahrzeugposition und Fahrtfortschrittsdaten vom ITCS über IF-01
abonnieren und Aktualisierungen mindestens alle 10 Sekunden verarbeiten.
*Übergeordnet:* BR-02, BR-05 · *Priorität:* muss

**FR-004** — Wenn ITCS-Daten für eine laufende Fahrt länger als 90 Sekunden nicht empfangen
wurden, soll das System die Schätzungen dieser Fahrt als veraltet markieren.
*Übergeordnet:* BR-02 · *Priorität:* muss
*Abnahmekriterium:* Gegeben eine Fahrt, deren letzte Aktualisierung 91 s zurückliegt, wenn
ein Konsument Abfahrten abfragt, dann kennzeichnet die Antwort die Schätzung als veraltet
mit dem Alter in Sekunden.

**FR-005** — Das System soll eine geschätzte Abfahrtszeit pro Fahrt und Haltestelle aus
Planzeiten und aktuellem Fahrtfortschritt berechnen.
*Übergeordnet:* BR-02 · *Priorität:* muss

**FR-006** — Das System soll Schätzungen innerhalb von 5 Sekunden nach Empfang neuer
Fahrtfortschrittsdaten neu berechnen.
*Übergeordnet:* BR-02 · *Priorität:* muss

## B. Störungserfassung

**FR-007** — Das System soll einem authentifizierten Disponenten ermöglichen, eine Störung
mit den Pflichtattributen Ursache, Schweregrad, betroffenes Gebiet, Gültigkeitsbeginn und
Quelltext zu erstellen.
*Übergeordnet:* BR-01, BR-04 · *Priorität:* muss · *Use Case:* UC-001

**FR-008** — Das System soll Nachrichtenvorlagen pro Ursache anbieten, mit einem begrenzten
Freitextfeld von maximal 240 Zeichen.
*Übergeordnet:* BR-04, BR-07 · *Priorität:* muss
*Abnahmekriterium:* Gegeben eine ausgewählte Ursache, wenn der Disponent das Textfeld öffnet,
dann ist die Vorlage vorausgefüllt und das Freitextfeld erzwingt die Zeichenbegrenzung mit
einem Live-Zähler.

**FR-009** — Das System soll das Ursachen-Attribut auf die standardisierte Taxonomie gemäss
Glossar beschränken und keine Freitext-Ursachen akzeptieren.
*Übergeordnet:* BR-01, BR-03 · *Priorität:* muss
*Begründung:* SIRI-SX-Konformität in IF-06 erfordert codierte Ursachen.

**FR-010** — Das System soll vor der Veröffentlichung einer Störung mit Schweregrad `major`
oder `severe` eine Freigabe durch den Pikettoffizier verlangen und für `information` oder
`minor` keine Freigabe erfordern.
*Übergeordnet:* BR-01 · *Priorität:* muss · *Use Case:* UC-002, Ablauf 3a

**FR-011** — Bei der Freigabe soll das System lokalisierte Nachrichten in Deutsch, Französisch,
Italienisch und Englisch aus dem strukturierten Inhalt innerhalb von 60 Sekunden generieren.
*Übergeordnet:* BR-07 · *Priorität:* muss
*Abnahmekriterium:* Gegeben eine freigegebene Störung, wenn 60 s vergangen sind, dann
existieren Nachrichten in allen vier Sprachen oder der Fallback von UC-002 Ablauf 5a wurde
angewendet und gekennzeichnet.

**FR-012** — Das System soll die Zielkanäle anhand von Schweregrad und betroffenem Gebiet
gemäss der Kanalmatrix bestimmen und dem Disponenten erlauben, Kanäle ausser der nationalen
Plattform abzuwählen, mit einer obligatorischen Begründung.
*Übergeordnet:* BR-01, BR-03 · *Priorität:* muss

**FR-013** — Das System soll für jede Störung eine Variante in einfacher Sprache erstellen,
die das Sprachniveau B1 nicht überschreitet, zur Verwendung durch Screenreader und
Audiokanäle.
*Übergeordnet:* BR-06 · *Priorität:* sollte

**FR-014** — Das System soll die Korrektur und Aufhebung einer veröffentlichten Störung
ermöglichen und die Änderung an genau diejenigen Kanäle weitergeben, die die Nachricht
aktuell halten.
*Übergeordnet:* BR-01, BR-02 · *Priorität:* muss · *Use Case:* UC-003

**FR-015** — Wenn ein Kanal eine Längenbeschränkung vorgibt, soll das System die Nachricht
gemäss der Kürzungsregel des Kanals kürzen und dem Disponenten den resultierenden Text vor
der Freigabe anzeigen.
*Übergeordnet:* BR-01 · *Priorität:* muss

## C. Verteilung

**FR-016** — Das System soll Abfahrtszeilen für eine Haltestelle an den Anzeigeadapter
liefern, sortiert nach geschätzter Abfahrtszeit.
*Übergeordnet:* BR-05 · *Priorität:* muss · *Use Case:* UC-004

**FR-017** — Das System soll den Countdown in ganzen Minuten bis 59 Minuten und darüber
hinaus als Uhrzeit darstellen.
*Übergeordnet:* BR-05 · *Priorität:* muss
*Abnahmekriterium:* Gegeben eine Schätzung 61 Minuten voraus, wenn die Zeile gerendert wird,
dann wird eine Uhrzeit angezeigt, nicht «61».

**FR-018** — Das System soll eine Störung innerhalb von 10 Sekunden nach Freigabe oder
Genehmigung an alle ausgewählten Kanäle senden.
*Übergeordnet:* BR-02 · *Priorität:* muss

**FR-019** — Wenn ein Kanal eine Aktualisierung länger als den Frische-Schwellenwert des
Kanals nicht bestätigt hat, soll das System diesen Kanal anweisen, einen
Veraltet-Indikator anzuzeigen.
*Übergeordnet:* BR-02, BR-08 · *Priorität:* muss · *Use Case:* UC-004 Ausnahme

**FR-020** — Das System soll eine Abfrageschnittstelle bereitstellen, die Abfahrten und
aktive Störungen gefiltert nach Haltestelle, Linie und Sprache zurückgibt.
*Übergeordnet:* BR-05, BR-07 · *Priorität:* muss

**FR-021** — Das System soll jeden fahrgastbezogenen Text als maschinenlesbaren Text
bereitstellen und Informationen nicht ausschliesslich als Bild liefern.
*Übergeordnet:* BR-06 · *Priorität:* muss

**FR-022** — Das System soll eine Service-Desk-Ansicht bereitstellen, die pro Linie oder
Haltestelle den aktuellen Inhalt jedes Kanals anzeigt.
*Übergeordnet:* BR-08 · *Priorität:* sollte · *Use Case:* UC-006

**FR-023** — Das System soll interne Anmerkungen zu einer Störung halten, die durch das
Datenmodell von allen Fahrgastkanälen ausgeschlossen sind.
*Übergeordnet:* BR-08, BR-09 · *Priorität:* muss

## D. Interoperabilität

**FR-024** — Das System soll SIRI-SX-Situationsaustausch an abonnierte Konsumenten liefern
und ein Update innerhalb von 10 Sekunden nach jeder Statusänderung einer Störung senden.
*Übergeordnet:* BR-03 · *Priorität:* muss · *Use Case:* UC-005 · *Status:* Review

**FR-025** — Das System soll SIRI-ET-Soll-Ist-Vergleichsmeldungen mindestens alle 30 Sekunden
für alle aktuell laufenden Fahrten liefern.
*Übergeordnet:* BR-03 · *Priorität:* muss · *Status:* Review

**FR-026** — Das System soll Abonnement-Heartbeat-Anfragen innerhalb von 5 Sekunden
beantworten und ein Abonnement nach drei aufeinanderfolgenden verpassten Heartbeats
wiederherstellen.
*Übergeordnet:* BR-03 · *Priorität:* muss · *Status:* Review

## E. Audit, Berichtswesen, Administration

**FR-027** — Das System soll für jede Erstellung, Freigabe, Veröffentlichung, Korrektur,
Aufhebung und jeden Publikationsversuch einen unveränderlichen Audit-Eintrag schreiben, der
Akteur, Zeitstempel, Kanal und Ergebnis protokolliert.
*Übergeordnet:* BR-09 · *Priorität:* muss · *Status:* Review

**FR-028** — Das System soll einem autorisierten Auditor ermöglichen, die vollständige
Kommunikationshistorie einer beliebigen Störung innerhalb der Aufbewahrungsfrist abzurufen
und zu exportieren.
*Übergeordnet:* BR-09 · *Priorität:* muss · *Status:* Review

**FR-029** — Das System soll fahrzeugbasierte Daten aggregieren, bevor sie in den Reporting-
Data-Mart gelangen, sodass kein einzelner Fahrer oder Fahrzeugdienst identifiziert werden
kann.
*Übergeordnet:* BR-10 · *Priorität:* muss · *Status:* Review

**FR-030** — Das System soll einem Administrator ermöglichen, einen Kanal-Endpunkt
hinzuzufügen und ihn Haltestellen oder Linien zuzuordnen, ohne ein Software-Deployment
durchzuführen.
*Übergeordnet:* BR-05 · *Priorität:* sollte · *Status:* Review
*Begründung:* Macht den Pfad von 45 % → 100 % Abdeckung in BR-05 zu einer
Konfigurationsaufgabe.

---

## Kanalmatrix (referenziert von FR-012)

| Schweregrad | Haltestellenanzeige | App Push | App Liste | Website | Nationale Plattform | Service Desk |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| `information` | – | – | ✓ | ✓ | ✓ | ✓ |
| `minor` | ✓ | – | ✓ | ✓ | ✓ | ✓ |
| `major` | ✓ | ✓ betroffene Linien | ✓ | ✓ | ✓ | ✓ |
| `severe` | ✓ alle Haltestellen der Linie | ✓ alle Abonnenten | ✓ | ✓ Startseite | ✓ | ✓ + Alarm |
