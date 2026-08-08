# UC-007 — Kommunikationshistorie für ein Audit rekonstruieren

**Primärer Akteur:** Compliance-Beauftragte/r · **Ebene:** Benutzerziel · **Status:** draft · **Traces to:** BR-09, BR-10

**Hauptszenario**
1. Beauftragte/r wählt einen Zeitraum und optional eine Linie oder Haltestelle.
2. PRISMA listet alle Störungen mit jeder Version, Freigabe, Korrektur und Aufhebung auf.
3. Für jede Störung zeigt PRISMA je Kanal: was gesendet wurde, zu welchem Zeitpunkt, mit welcher Bestätigung.
4. Beauftragte/r exportiert das Ergebnis als signiertes PDF/A und als CSV.

**Einschränkungen**
- Aufbewahrung 3 Jahre (BR-09); der Export enthält keine personenbezogenen Daten von Fahrerinnen und Fahrern (BR-10, CON-07).
- Zugriff erfordert die Rolle `prisma.auditor`; jeder Export wird selbst protokolliert.
