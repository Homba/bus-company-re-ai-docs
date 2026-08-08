# Projektauftrag — PRISMA

| | |
|---|---|
| **Projekt** | PRISMA — Passenger Real-time Information & Service Management |
| **Auftraggeber** | Regionalverkehr Bernland AG (RVB) |
| **Sponsor** | Leiter Betrieb (STK-01) |
| **Product Owner** | Leitung Fahrgastinformation (STK-03) |
| **Status dieses Dokuments** | baselined, v1.2, 2026-03-11 |
| **Geplanter Go-live** | Pilot Q4 2026, vollständiger Rollout Q2 2027 |

## 1. Problemstellung

RVB verteilt Fahrgastinformationen über drei nicht vernetzte Wege:

1. Das **ITCS** (2009, Hersteller unterstützt die Version nicht mehr) liefert Abfahrtszeiten
   an 61 von 412 Haltestellenanzeigen über ein proprietäres Protokoll.
2. Leitstellenpersonal tippt Störungstexte von Hand ins Website-CMS, in ein SMS-Gateway
   und ins App-Backoffice — dreimal, in drei Formulierungen.
3. Die nationale Open-Data-Plattform erhält nachts einen statischen Fahrplanexport und
   **keinerlei** Echtzeitdaten.

Im Jahr 2025 gemessene Auswirkungen:

| Symptom | Messwert | Quelle |
|---|---|---|
| Mediane Verzögerung zwischen Vorfall und erster Fahrgast-Meldung | 11 Min. 40 s | Analyse Leitstellenprotokoll, Jan.–Jun. 2025 |
| Widersprüchliche Informationen über die Kanäle hinweg | 27 % der Störungen | Qualitätsaudit, 120 Stichproben-Störungen |
| Beschwerden mit Ursache «keine / falsche Information» | 1 340 pro Jahr, 38 % aller Beschwerden | Kundendienstsystem |
| Haltestellen mit Echtzeitanzeige-Abdeckung | 14,8 % | Anlagenverzeichnis |
| Konzessionsbedingung zur Echtzeitdatenlieferung | **nicht erfüllt** seit 2024 | BAV-Prüfschreiben 2024-11-08 |

## 2. Geschäftsziele

Siehe `04-business-requirements.md` für den vollständigen, prüfbaren Satz. Zusammengefasst:

- Ein verbindlicher Störungseintrag pro Vorfall, einmal erfasst.
- Unter drei Minuten vom Vorfall bis zur Fahrgastmeldung auf jedem Kanal.
- Echtzeitdatenlieferung an die nationale Plattform, um die Konzessionsfeststellung zu schliessen.
- Haltestellenanzeige-Abdeckung erhöhen, ohne das ITCS-Kernsystem in diesem Programm zu ersetzen.

## 3. Geltungsbereich

**Im Scope**
- Störungserfassung, Freigabe und Verteilung
- Echtzeit-Abfahrtsberechnung und -publikation
- Kanaladapter: Haltestellenanzeigen, RVB-App, Website, nationale Datenplattform, Kundendienst
- Mehrsprachige Meldungsverarbeitung (DE / FR / IT / EN)
- Barrierefreiheit aller fahrgastseitigen Ausgaben

**Ausserhalb des Scope**
- Ablösung des ITCS-Kernsystems (Fahrzeugortung, Disposition, Dienstpläne)
- Ticketing, Tarifberechnung, Vertriebskanäle
- Beschaffung von Bordansage-Hardware
- Redesign der RVB-App-Oberfläche (PRISMA liefert die API, nicht die Bildschirme)

## 4. Erfolgskriterien (überprüft 6 Monate nach vollständigem Rollout)

| ID | Kriterium | Zielwert | Methode |
|---|---|---|---|
| SC-1 | Mediane Latenz Vorfall-bis-Meldung | ≤ 3 Min. | Automatischer Zeitstempelvergleich, 3-Monats-Fenster |
| SC-2 | Kanalkonsistenz | ≥ 99 % der Störungen identisch über alle Kanäle | Automatisierter Inhaltsvergleich, wöchentliche Stichprobe |
| SC-3 | Verfügbarkeit Echtzeit-Feed an nationale Plattform | ≥ 99,5 % monatlich | Plattformseitiges Monitoring |
| SC-4 | Beschwerden wegen fehlender/falscher Information | −50 % vs. Baseline 2025 | Kundendienstsystem |
| SC-5 | Leitstellenaufwand pro Störung | ≤ 2 Min. Erfassungszeit | Zeitstudie, 40 Beobachtungen |

## 5. Rahmenbedingungen (Zusammenfassung)

Kostenobergrenze CHF 4,2 Mio. über drei Finanzjahre; Beschaffung unterliegt dem öffentlichen
Vergaberecht; die Lösung muss in der kantonalen Regierungs-Cloud laufen; Konzessionskonformität
ist nicht verhandelbar. Vollständige Liste in `09-constraints-and-compliance.md`.

## 6. Vorgehensweise

Hybrid. Geschäftsanforderungen, Qualitätsanforderungen und gesetzliche Rahmenbedingungen werden
vorab spezifiziert und baselined (sie sind beschaffungsrelevant). Funktionale Details werden
iterativ ausgearbeitet: Die FR-Menge bildet das vertragliche Rückgrat, User Stories in `backlog/`
tragen das Sprint-Level-Detail und dürfen ohne Change Request geändert werden, solange sie
innerhalb ihres übergeordneten FR bleiben.

## 7. Freigabe

| Rolle | Name (fiktiv) | Datum |
|---|---|---|
| Sponsor / Leiter Betrieb | R. Buchser | 2026-03-11 |
| Leiter IT | M. Zaugg | 2026-03-11 |
| Leiterin Kundendienst | A. Perrin | 2026-03-09 |
| Kantonales Verkehrsamt (Beobachter) | Dr. S. Iten | 2026-03-11 |
