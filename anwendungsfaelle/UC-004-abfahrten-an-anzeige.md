# UC-004 — Abfahrten an einer Haltestellenanzeige konsumieren

**Primärer Akteur:** Fahrgast (P2 Beat) · **Ebene:** Benutzerziel · **Status:** approved · **Traces to:** BR-02, BR-05, BR-06

**Auslöser:** Der Fahrgast blickt auf eine Haltestellenanzeige.

**Hauptszenario**
1. PRISMA liefert die geordneten Abfahrtszeilen für diese Haltestelle an den Anzeigeadapter.
2. Die Anzeige zeigt Linie, Ziel, Countdown und eine Bemerkung, sofern eine vorhanden ist.
3. Die Zeilen werden mindestens alle 30 s aktualisiert; eine geänderte Prognose wird innerhalb von 30 s nach Empfang angezeigt.
4. Eine aktive Störung, die die Haltestelle betrifft, wird als Banner im Wechsel mit den Zeilen angezeigt.

**Alternative Abläufe**
- 1a. Keine Echtzeitdaten für eine Fahrt → die Sollzeit wird angezeigt, gekennzeichnet als geplant statt prognostiziert.
- 4a. Mehr als eine Störung betrifft die Haltestelle → der höchste Schweregrad wird zuerst angezeigt, dann nach
  zeitlicher Nähe des Gültigkeitsbeginns; maximal zwei werden rotiert.

**Ausnahmeablauf**
- \*a. Die Anzeige verliert die Verbindung → nach 120 s zeigt sie einen Aktualitätshinweis anstelle eines
  Countdowns, der stillschweigend irreführen würde (NFR-005). *Dies war die meistgenannte Fahrgastbeschwerde
  im Audit 2025.*
