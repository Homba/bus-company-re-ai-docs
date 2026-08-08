# Projektbeschrieb — RVB Modernisierung Fahrgastinformation

> Dies ist das Ausgangsmaterial für den Workshop. Die Teilnehmenden erhalten diesen Beschrieb
> und nutzen AI Agents, um daraus schrittweise formale Requirements-Engineering-Artefakte zu erarbeiten.

---

## Ausgangslage

Die Regionalverkehr Bernland AG (RVB) ist ein regionales Busunternehmen in der Schweiz. Der
Kanton Bern hält 71 % der Aktien; die übrigen Anteile verteilen sich auf 24 Gemeinden
entlang der Linien. Die RVB betreibt 38 Buslinien gestützt auf eine Konzession des Bundesamts
für Verkehr (BAV). Die Finanzierung erfolgt über das Bestellverfahren von Kanton und Bund.

Die RVB beschäftigt rund 480 Personen. Die Betriebsleitstelle ist 18 Stunden pro Tag besetzt
(05:00–23:00) mit 2–3 Disponentinnen und Disponenten pro Schicht. Der Kundendienst zählt
8 Mitarbeitende, die pro Schicht rund 60–90 Anfragen per Telefon, E-Mail und Chat bearbeiten.

## Das Problem (beschrieben durch den Leiter Betrieb)

> «Wir haben ein Fahrgastinformationsproblem. Wenn im Netz etwas schiefläuft — ein Bus fällt
> aus, eine Strasse wird gesperrt, eine Umleitung nötig — müssen unsere Disponenten dieselbe
> Meldung dreimal eintippen: einmal ins CMS der Website, einmal ins SMS-System und einmal ins
> App-Backend. Oft fehlt die Zeit, alle drei zu aktualisieren, und dann sehen die Fahrgäste in
> der App etwas anderes als auf der Website. Manchmal geht die Meldung erst 15 Minuten nach dem
> Ereignis raus. Unsere Chauffeure werden von Fahrgästen beschimpft, die keine Ahnung hatten,
> dass ihr Bus ausfällt.
>
> Bei den Haltestellenanzeigen ist es noch schlimmer. Wir haben elektronische Anzeigen an 61
> unserer 412 Haltestellen, aber die hängen an unserem alten ITCS von 2009. Der Hersteller
> unterstützt diese Version kaum noch. Die Anzeigen zeigen Abfahrts-Countdowns, aber keine
> Störungsmeldungen. Wir können es uns nicht leisten, das ganze ITCS zu ersetzen — das wäre
> ein separates Projekt für CHF 8 Mio.
>
> Und dann ist da die Aufsichtsbehörde. Das BAV hat uns letzten November auditiert und
> festgestellt, dass wir keine Echtzeitdaten an die nationale Open-Data-Plattform liefern —
> eine Konzessionsauflage. Wir schicken ihnen nur einen statischen Fahrplanexport pro Nacht.
> Sie verlangen SIRI-Feeds — Echtzeit-Fahrzeugpositionen und Störungsmeldungen. Wenn wir
> das nicht in Ordnung bringen, könnte es die nächste Konzessionserneuerung gefährden.
>
> Wir brauchen ein System, bei dem ein Disponent eine Störungsmeldung einmal erfasst und sie
> automatisch überall ausgespielt wird — auf den Anzeigen, in der App, auf der Website, auf
> der nationalen Plattform und auf den Bildschirmen unserer Kundendienst-Mitarbeitenden.
> Das muss schnell und konsistent sein und mehrere Sprachen abdecken, weil wir sowohl
> deutsch- als auch französischsprachige Gebiete bedienen. Im Sommer kommen auch italienisch-
> und englischsprachige Touristen dazu.»

## Erkenntnisse aus den ersten Gesprächen

### Aktuelle Kennzahlen (gemessen Jan.–Jun. 2025)
- **11 Min. 40 Sek.** — medianer Verzug von Ereignis bis zur ersten Fahrgastmeldung
- **27 %** der Störungen mit inkonsistentem Wortlaut über die verschiedenen Kanäle
- **1'340** Beschwerden pro Jahr wegen fehlender oder falscher Information (38 % aller Beschwerden)
- **61 von 412** Haltestellen mit Echtzeit-Abfahrtsanzeige (14,8 % Abdeckung)
- BAV-Konzessionsaudit (Schreiben vom 8. November 2024): Echtzeitdatenlieferung **nicht erfüllt**

### Bestehende Systeme
- **ITCS (Intermodal Transport Control System):** 2009 durch VendorTech AG installiert.
  Zuständig für Fahrzeugortung, Disposition und Dienstplanung. Sendet Abfahrtsdaten via
  VDV-453-Protokoll an 61 Haltestellenanzeigen. Der Hersteller leistet «Best-Effort»-Support,
  empfiehlt aber die Migration auf seine neue Plattform (separates Projekt, CHF 8 Mio.,
  nicht im Projektumfang).
- **Website-CMS:** WordPress-basiert, betreut durch das Marketing. Störungsmeldungen werden
  manuell als eigener Beitragstyp erfasst.
- **SMS-Gateway:** Für registrierte Fahrgäste mit Opt-in. Meldungen werden manuell eingetippt.
- **App-Backend:** Separate REST-API, betreut durch einen externen Mobile-Entwickler.
  Störungsmeldungen werden über ein Admin-Panel eingegeben.
- **Nationale Plattform:** Erhält nächtlich einen NeTEx-Fahrplanexport. Kein Echtzeit-Feed.
- **Kundendienst-Tool:** Separates CRM. Die Mitarbeitenden haben keine Einsicht, welche
  Meldungen über welche Kanäle verschickt wurden.

### Erwähnte Stakeholder
- Leiter Betrieb (Auftraggeber, will das Problem lösen)
- Leiterin Fahrgastinformation (würde die Rolle Product Owner übernehmen)
- Disponenten (3 Schichten, Hauptnutzende eines allfälligen Erfassungstools)
- Kundendienst-Mitarbeitende (müssen sehen, was die Fahrgäste sehen)
- BAV (Aufsichtsbehörde, Konzessionskonformität)
- Kantonales Amt für öffentlichen Verkehr (Beobachterrolle, Hauptaktionär)
- Personalkommission (besorgt über Systeme, die Fahrverhalten überwachen könnten)
- Behindertenorganisation (hat mangelnde Barrierefreiheit der Informationen bemängelt)
- Gemeinden (finanzieren das Angebot mit, erhalten Beschwerden aus der Bevölkerung)

### Budget und Zeitplan
- **Budgetobergrenze:** CHF 4,2 Mio. über drei Geschäftsjahre
- **Gewünschter Zeitplan:** Pilotbetrieb mit 2–3 Linien in Q4 2026, flächendeckende Einführung Q2 2027
- Die Beschaffung muss dem öffentlichen Beschaffungsrecht (BöB) entsprechen
- Die Lösung muss in der kantonalen Verwaltungscloud betrieben werden (keine Public Cloud)

### Ergänzende Hinweise aus den Interviews
- Die Personalkommission hat ausdrücklich festgehalten: «Ein System, das Fahrzeugpositionen
  erfasst, darf nicht für individuelle Leistungsüberwachung verwendet werden können. Dem werden
  wir nicht zustimmen.»
- Die Behindertenorganisation verlangt, dass alle fahrgastbezogenen Ausgaben barrierefrei sind
  (Screenreader-Kompatibilität, Kontrast, leichte Sprache).
- Eine Disponentin sagte: «Ich habe nichts dagegen, die Meldung zu tippen, aber ich brauche
  Vorlagen. In der Hauptverkehrszeit kann ich nicht perfekte Sätze in drei Sprachen formulieren.
  Gebt mir Lückentexte zum Ausfüllen.»
- Ein Kundendienst-Mitarbeiter sagte: «Fahrgäste rufen an und wir haben keine Ahnung, was sie
  in der App im Vergleich zur Anzeige gesehen haben. Wir wirken inkompetent.»
- Das IT-Betriebsteam besteht auf einer Lösung, die in der kantonalen Cloud deploybar ist. Eine
  SaaS-Lösung, die ausserhalb der Schweiz gehostet wird, werden sie nicht genehmigen.
- Französische Übersetzungen von Störungsmeldungen werden derzeit ad hoc erstellt, wenn zufällig
  ein französischsprachiger Disponent im Dienst ist. Es gibt keinen systematischen Prozess.
