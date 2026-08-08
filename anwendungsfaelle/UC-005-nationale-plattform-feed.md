# UC-005 — Echtzeitdaten an die nationale Plattform liefern

**Primärer Akteur:** Nationale Open-Data-Plattform (STK-10) · **Ebene:** Subfunktion · **Status:** approved · **Traces to:** BR-03

**Vorbedingung:** Zwischen der Plattform und PRISMA besteht ein gültiges Abonnement.

**Hauptszenario**
1. Die Plattform hält ein SIRI-SX-Abonnement für Situationen und ein SIRI-ET-Abonnement für
   geschätzte Fahrpläne.
2. Bei jeder Störungspublikation, -korrektur oder -aufhebung übermittelt PRISMA die
   entsprechende SIRI-SX-Situation innerhalb von 10 s.
3. PRISMA übermittelt SIRI-ET-Aktualisierungen mindestens alle 30 s für alle aktuell fahrenden Fahrten.
4. PRISMA beantwortet Heartbeat-Anfragen innerhalb von 5 s.

**Ausnahmeabläufe**
- 2a. Zustellung schlägt fehl → Wiederholung mit Backoff während 30 Min., danach Alarm an den IT-Betrieb.
- 4a. Drei aufeinanderfolgende verpasste Heartbeats → PRISMA stellt das Abonnement selbstständig wieder her.

**Konformitätshinweis:** Die Konformität wird vor dem Go-live mit der Testsuite des Plattformbetreibers nachgewiesen
und nach jedem Release, das IF-06 betrifft, erneut durchgeführt (CON-02).
