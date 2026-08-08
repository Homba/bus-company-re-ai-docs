# Randbedingungen und Compliance

Eine Randbedingung ist innerhalb dieses Projekts nicht verhandelbar. Wenn ein Stakeholder-Wunsch
mit einer Randbedingung kollidiert, hat die Randbedingung Vorrang und der Wunsch wird zu einem
Änderungsantrag an den Eigentümer der Randbedingung.

| ID | Randbedingung | Typ | Eigentümer | Konsequenz für die Spezifikation |
|---|---|---|---|---|
| CON-01 | Es gilt das öffentliche Beschaffungsrecht; die Spezifikation muss herstellerneutral sein und Ergebnisse beschreiben, nicht Produkte | rechtlich | Beschaffung | Keine Produktnamen in FR/NFR; NFR-Zielwerte müssen objektiv prüfbar sein |
| CON-02 | Die Konzession verpflichtet RVB zur Lieferung von Echtzeitdaten an die nationale Plattform; dieser Kanal kann nicht abgewählt werden | rechtlich | STK-09 | FR-012 Ausnahme; UC-002 Ablauf 6a |
| CON-03 | Fahrgastinformationen öffentlicher Stellen müssen die geltenden Barrierefreiheitsanforderungen erfüllen | rechtlich | STK-15 | NFR-011, NFR-012, FR-021 |
| CON-04 | Die Lösung läuft in der kantonalen Verwaltungscloud; nur Dienste aus dem genehmigten Katalog dürfen verwendet werden | technisch / Policy | Kantons-IT | NFR-019; schliesst mehrere verwaltete Übersetzungsdienste aus — siehe ADR-003 |
| CON-05 | Das ITCS-Kernsystem wird in diesem Programm nicht ersetzt und seine Schnittstelle ist ausschliesslich das dokumentierte VDV-453-Abonnement | technisch | STK-12 | FR-003; ADR-002 |
| CON-06 | Es gilt das schweizerische Datenschutzgesetz; eine DSFA ist vor Go-live erforderlich | rechtlich | STK-11 | NFR-013, NFR-014 |
| CON-07 | Gesamtarbeitsvertrag: Fahrzeugdaten dürfen nicht zur individuellen Leistungsbeurteilung verwendet werden | organisatorisch | STK-13 | BR-10, FR-029, NFR-014 |
| CON-08 | Budgetobergrenze CHF 4,2 Mio. über drei Haushaltsjahre, mit jährlicher kantonaler Genehmigung | finanziell | STK-08 | Priorisierung in BR-05; Phase-2-Kandidaten in OPN-Liste |
| CON-09 | Dokumentensprache der Spezifikation ist Deutsch; die englische Version in diesem Repository ist eine Arbeitsübersetzung | organisatorisch | STK-03 | Terminologiedispute werden anhand des deutschen Glossars entschieden |
| CON-10 | Go-live darf nicht zwischen 15. Dezember und 10. Januar fallen (Winterbetrieb-Spitze) | betrieblich | STK-01 | Releaseplanung; Pilot muss bis 30. November abgeschlossen sein |
| CON-11 | Schnittstellen zur nationalen Plattform müssen dem SIRI-Profil entsprechen, das die Plattform vorgibt | technisch | STK-10 | FR-024…FR-026, NFR-018 |
| CON-12 | Personalschulung muss in bestehende Schichtstrukturen passen — maximal 4 h pro Disponent | organisatorisch | STK-01 | Treibt NFR-002 und das UI-Einfachheitsziel |

## Referenzierte Standards

| Standard | Verwendet für |
|---|---|
| ISO/IEC/IEEE 29148:2018 | Struktur und Qualitätskriterien dieser Spezifikation |
| ISO/IEC 25010 | Klassifikation der Qualitätsanforderungen |
| SIRI (SX, ET) | IF-06 Echtzeitaustausch |
| NeTEx | IF-02 Stammdatenimport |
| VDV 453 | IF-01 ITCS-Abonnement |
| OIDC | IF-08 Personalauthentifizierung |
| WCAG 2.1 AA | Barrierefreiheits-Zielstufe für digitale Kanäle |

## Compliance-Nachweisplan

| Anforderungsquelle | Erstellter Nachweis | Wann | Abgelegt bei |
|---|---|---|---|
| Konzession / BAV-Feststellung | Konformitätssuite-Ergebnis, Verfügbarkeitsbericht | Vor Go-live, dann monatlich | STK-09 |
| Barrierefreiheit | Externer Auditbericht, Screenreader-Testprotokoll | Vor Go-live | STK-15, Kanton |
| Datenschutz | DSFA, Löschjob-Nachweis, Schemainspektion | Vor Go-live, jährlich | STK-11 |
| Gesamtarbeitsvertrag | Schemainspektion-Abnahme | Vor Go-live | STK-13 |
| Beschaffung | Herstellerneutralitäts-Review der Ausschreibungsunterlagen | Vor Ausschreibung | Beschaffung |
