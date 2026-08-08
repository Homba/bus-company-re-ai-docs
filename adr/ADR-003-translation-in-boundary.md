# ADR-003 — Übersetzung innerhalb der kantonalen Cloud-Grenze

**Status:** proposed · **Entscheider:** STK-05, STK-11, STK-03 · **Bezug zu:** RSK-04, CON-04, CON-06

## Kontext

BR-07 verlangt vier Sprachen innerhalb von 60 s nach der Freigabe ohne Aufwand für die Disposition. Der naheliegende
Ansatz ist ein verwalteter Übersetzungsdienst, aber CON-04 beschränkt die Lösung auf den genehmigten
kantonalen Cloud-Katalog, und CON-06 wirft Fragen bezüglich der Übermittlung operativer Inhalte an einen
Dienst ausserhalb der Grenze auf.

## Optionen

1. **Verwalteter externer Übersetzungsdienst** — beste Qualität, erfüllt CON-04 beim heutigen Stand des Katalogs nicht,
   erfordert eine Datenschutzfolgenabschätzung.
2. **Selbst gehostetes Übersetzungsmodell innerhalb der Grenze** — erfüllt CON-04 und CON-06, höhere
   Betriebskosten, Qualität muss am Vorlagenkatalog gemessen werden.
3. **Vorübersetzter Vorlagenkatalog mit einem übersetzten Freitext-Feld** — deterministisch,
   auditierbar, am günstigsten; begrenzt die Ausdrucksfähigkeit und erfordert einen Übersetzungsworkflow für neue Vorlagen.

## Vorgeschlagene Entscheidung

Option 3 als Baseline, mit Option 2 als Erweiterung für das Freitext-Feld. Begründung:
FR-008 begrenzt den Freitext bereits auf 240 Zeichen, die zu übersetzende Fläche ist also klein; ein
deterministischer Katalog lässt sich bei einem Audit (BR-09) auch leichter verteidigen und beseitigt den
schlimmsten Fall von RSK-03, bei dem eine generierte Übersetzung die operationelle Bedeutung einer Nachricht verändert.

## Konsequenzen

Erfordert einen Verantwortlichen für die Vorlagen-Governance — das ist genau OPN-02, der geschlossen werden muss, bevor
dieser ADR akzeptiert werden kann.
