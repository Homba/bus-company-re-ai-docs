# UC-001 — Störung erfassen

**Primärer Akteur:** Disponent/in · **Ebene:** Benutzerziel · **Status:** approved · **Traces to:** BR-01, BR-04, BR-07

**Auslöser:** Die Disponentin / der Disponent erfährt von einem Ereignis, das den Betrieb beeinträchtigt.

**Vorbedingung:** Authentifiziert mit der Rolle `prisma.dispatcher`.

**Hauptszenario**
1. Disponent/in startet eine neue Störung, optional ab einer Vorlage oder einer früheren Störung.
2. Disponent/in wählt die Ursache aus der standardisierten Taxonomie.
3. Disponent/in wählt den betroffenen Bereich: Linien, Streckenabschnitte oder einzelne Haltestellen, mit Kartenunterstützung.
4. Disponent/in legt den Schweregrad und den Gültigkeitsbeginn fest; optional ein voraussichtliches Ende.
5. PRISMA schlägt eine strukturierte Meldung vor, aufgebaut aus Ursache, Bereich und Gültigkeit.
6. Disponent/in bearbeitet das Freitextfeld innerhalb des Zeichenlimits; PRISMA warnt bei Begriffen
   ausserhalb des kontrollierten Vokabulars.
7. PRISMA speichert die Störung im Status `draft` und zeigt eine Vorschau je Kanal an.

**Alternative Abläufe**
- 1a. Disponent/in dupliziert eine wiederkehrende Störung (z. B. wöchentliche Baustelle) und passt die Daten an.
- 3a. Der betroffene Bereich ist eine ganze Linie für einen ganzen Tag → Disponent/in wählt die Schnellfunktion «Linie ausser Betrieb».
- 6a. Der Freitext überschreitet das Anzeigelimit → PRISMA zeigt die Abschneidestelle für Haltestellenanzeigen an
  und behält den vollständigen Text für App und Web (FR-015).

**Ausnahmeablauf**
- \*a. Der Entwurf wird 15 Minuten lang nicht gespeichert und der Browser ist geschlossen → PRISMA bewahrt ihn als
  nicht freigegebenen Entwurf für 24 h auf, sichtbar für alle Disponent/innen.
