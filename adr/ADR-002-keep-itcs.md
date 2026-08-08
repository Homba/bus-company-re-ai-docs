# ADR-002 — Das ITCS als Quelle der Fahrzeugdaten beibehalten

**Status:** accepted (2026-02-19) · **Entscheider:** STK-01, STK-05, STK-12

## Kontext

Das ITCS ist 15 Jahre alt und der Hersteller unterstützt die Version nur im Rahmen einer erweiterten
Vereinbarung. Ein Ersatz würde mehrere Probleme auf einmal lösen — und würde das gesamte
CON-08-Budget dreimal aufbrauchen, mit einem mehrjährigen Zeitplan, der den BAV-Befund
(BR-03) in der Zwischenzeit offen lässt.

## Entscheidung

PRISMA bezieht Fahrzeugposition und Fahrtfortschritt vom bestehenden ITCS über dessen
dokumentierte VDV-453-Subskription und implementiert keine eigene Fahrzeuglokalisierung. Der ITCS-Ersatz
ist ein separates Programm.

## Konsequenzen

**Positiv** — Liefert BR-03 innerhalb des Budgets und vor der nächsten BAV-Prüfung.

**Negativ** — PRISMA erbt die Datenqualität des ITCS, was der Grund für RSK-01 und für
die Sprint-0-Datenbewertung ist. Die Prognosequalität (NFR-004) ist durch einen Input begrenzt, den PRISMA
nicht kontrolliert; FR-004 und NFR-005 existieren, damit das System ehrlich darüber ist, statt
es zu verbergen.

**Folgemassnahme** — Die Hub-Grenze (ADR-001) ist so gezogen, dass ein zukünftiger ITCS-Ersatz
einen Eingangsadapter ändert, nicht die Verteilschicht.
