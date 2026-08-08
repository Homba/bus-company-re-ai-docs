# UC-006 — Fahrgastanfrage mit aktuellem Kontext beantworten

**Primärer Akteur:** Kundendienstmitarbeiter/in (P4 Tobias) · **Ebene:** Benutzerziel · **Status:** draft · **Traces to:** BR-01, BR-08

**Hauptszenario**
1. Mitarbeiter/in sucht nach Linie, Haltestelle oder Störungs-ID.
2. PRISMA zeigt genau an, was jeder Kanal für diesen Bereich aktuell anzeigt.
3. PRISMA zeigt zusätzlich nur intern sichtbaren Kontext: voraussichtliche Dauer, Disponenten-Notiz,
   ob eine Korrektur ausstehend ist.
4. Mitarbeiter/in kann die Störung als «erzeugt viele Anrufe» kennzeichnen, sichtbar für die Leitstelle.

**Geschäftsregel:** Nur intern sichtbare Felder werden niemals an Fahrgastkanäle verteilt; dies wird
auf Datenmodellebene durchgesetzt, nicht in der Benutzeroberfläche (FR-023).

**Offener Punkt:** OPN-06 — Sollen Kundendienstmitarbeitende eine Störung zur Freigabe durch den Disponenten entwerfen können?
