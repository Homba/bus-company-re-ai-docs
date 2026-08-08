# Workshop-Einführung — Videoskript

> **Format:** Narration + Bildschirmvisuals. ~8 Minuten.
> **Ton:** Gesprächig, professionell. Wie eine Erklärung unter Fachkollegen.
>
> Layout: zwei Spalten. Links = was die Zuschauer sehen. Rechts = Narration (Voiceover
> oder Presenter vor der Kamera).

---

## Szene 1 — Der Einstieg (45 Sek.)

| BILD | NARRATION |
|------|-----------|
| Text auf dem Bildschirm: *«Schreib mir Anforderungen für ein Fahrgastinformationssystem»* wird in einen generischen AI-Chat getippt. Eine Wand aus Aufzählungspunkten erscheint. | Die meisten Leute nutzen KI für Requirements Engineering so: Chat öffnen, eine breite Anfrage eintippen, eine Textwand zurückbekommen. Copy-paste ins Pflichtenheft. Fertig, oder? |
| Text blendet aus. Bildschirm zeigt: *«80% des Potenzials bleibt liegen.»* | Das funktioniert — einigermassen. Aber es bleibt ein Grossteil des Potenzials liegen. |
| Titelkarte: **KI-gestütztes Requirements Engineering — Workshop-Einführung** | In diesem Workshop lernt ihr einen grundlegend anderen Ansatz. Statt eines generischen Assistenten baut ihr ein **Team spezialisierter Agenten** — jeder auf eine bestimmte RE-Aufgabe zugeschnitten. |

---

## Szene 2 — Was sind RE-Agenten? (60 Sek.)

| BILD | NARRATION |
|------|-----------|
| Animiertes Diagramm: acht beschriftete Boxen in einem Ablauf — *Stakeholder-Analyst → Anforderungs-Elicitor → Anforderungs-Verfeinerer → Qualitätsattribut-Analyst → Use-Case-Autor → Anforderungs-Reviewer → Traceability-Prüfer → Story-Writer* | Die Idee: statt einer KI, die alles macht, erstellen wir acht Spezialisten. Einer analysiert Stakeholder. Einer extrahiert messbare Ziele aus Interviews. Einer nimmt grobe Anforderungen und macht sie präzise und testbar. Einer schreibt Use Cases. Einer reviewt eure Arbeit auf Mängel. |
| Zoom auf eine Box. Ein Ausschnitt eines System-Prompts wird gezeigt. | Jeder Agent wird durch einen **System-Prompt** gesteuert — eine Seite Anweisungen, die RE-Methodik codiert. ISO 29148 für die Struktur. Cockburn für Use Cases. ISO 25010 für Qualitätsattribute. Der Prompt sagt nicht einfach «schreib gute Anforderungen». Er definiert das Format, die Qualitätskriterien, die typischen Fehler und die Fragen, die bei fehlender Information gestellt werden sollen. |
| Text-Overlay: *«Ein System-Prompt ist eine formalisierte Methodik.»* | Denkt es euch so: Ein System-Prompt ist eine formalisierte Methodik. Ihr codiert das, was ein erfahrener Analyst tut — in ein wiederverwendbares, konsistentes Werkzeug. |

---

## Szene 3 — Die Fallstudie: PRISMA (3 Min.)

| BILD | NARRATION |
|------|-----------|
| Karte einer fiktiven Schweizer Region mit eingezeichneten Buslinien. Logo: «RVB — Regionalverkehr Bernland AG» | Jetzt zur Fallstudie. RVB ist ein regionales Busunternehmen in der Schweiz. Der Kanton hält 71%, die Gemeinden den Rest. 38 Buslinien, 412 Haltestellen, rund 480 Mitarbeitende. Fiktiv — aber an echten Schweizer ÖV-Unternehmen angelehnt. |
| Splitscreen: Disponent an einer Arbeitsstation, drei Browserfenster offen (CMS, SMS-Panel, App-Admin). Eine Uhr tickt. | Ihr Problem ist die Fahrgastinformation. Wenn ein Bus ausfällt oder eine Strasse gesperrt wird, müssen die Disponenten dieselbe Meldung in drei separate Systeme tippen — Website, SMS-Gateway und App-Backend. Dreimal, drei verschiedene Formulierungen. In der Stosszeit schaffen sie oft nur eines davon. |
| Animation: Fahrgast an einer Haltestelle, Regen, schaut aufs Handy. App zeigt «pünktlich». Bus kommt nicht. | Die Fahrgäste sehen dann auf der App etwas anderes als auf der Website — und an der Haltestelle gar nichts. Sie stehen im Regen und wissen nicht, was passiert ist. |
| Infografik mit vier Kennzahlen, die nacheinander eingeblendet werden: | Die Zahlen sind deutlich. |
| **11 Min. 40 Sek.** — mit Uhr-Icon | Elf Minuten und vierzig Sekunden — die mittlere Verzögerung vom Vorfall bis zur ersten Fahrgastmeldung. |
| **27%** — mit Warnungs-Icon | Siebenundzwanzig Prozent der Störungen haben widersprüchliche Informationen über die Kanäle hinweg. |
| **1'340** — mit Beschwerde-Icon | Eintausenddreihundertvierzig Beschwerden pro Jahr wegen fehlender oder falscher Information. |
| **61 / 412** — mit Kartennadel-Icon | Nur 61 von 412 Haltestellen haben überhaupt eine Echtzeitanzeige. |
| Dokument-Icon: «BAV-Auditbefund — 08.11.2024» | Und das Bundesamt für Verkehr hat einen formellen Befund ausgestellt: die Echtzeitdaten-Lieferung an die nationale Plattform — eine Konzessionsbedingung — wird nicht erfüllt. |
| Sechs Stakeholder-Icons in einem Kreis, mit Spannungslinien zwischen einigen. Beschriftungen: *Personalvertretung, Behindertenrechts-Organisation, Datenschutz, BAV, Disponenten, Fahrgäste* | Jetzt wird es für Requirements Engineering interessant. Das ist nicht nur ein technisches Problem. Da gibt es eine Personalvertretung, die alles blockiert, was zur Fahrerüberwachung genutzt werden könnte. Eine Behindertenrechts-Organisation, die barrierefreie Information fordert. Einen Datenschutzbeauftragten, der sich um Fahrzeug-Trackingdaten sorgt. Vier Sprachen. Ein striktes Budget. Und die Vorgabe, alles in der kantonalen Cloud zu betreiben. Diese Stakeholder haben widersprüchliche Prioritäten — und genau das muss echtes Requirements Engineering navigieren. |
| Lösungsdiagramm: eine zentrale Box «PRISMA» mit Pfeilen zu: Anzeigen, App, Website, nationale Plattform, Kundendienst. | Die vorgeschlagene Lösung heisst PRISMA. Ein massgeblicher Störungsdatensatz, einmal erfasst, automatisch an jeden Kanal verteilt. Eure Aufgabe im Workshop ist es, die formale Anforderungsspezifikation für PRISMA zu erarbeiten — mit KI-Agenten bei jedem Schritt. |

---

## Szene 4 — Das Repository (90 Sek.)

| BILD | NARRATION |
|------|-----------|
| Bildschirmaufnahme: GitHub-Repo oder Ordnerstruktur wird aufgeklappt. `workshop/`-Ordner hervorgehoben. | Alles, was ihr braucht, ist in diesem Repository. Ich zeige euch kurz die Struktur. |
| Zoom auf `workshop/starting-materials/`. `project-brief.md` öffnen, langsam scrollen. | Unter Ausgangsmaterial findet ihr den rohen Projektauftrag — den unstrukturierten Input, den ihr als Analyst zu Beginn eines solchen Projekts bekommt. Dazu sechs Interview-Transkripte mit Stakeholdern: eine Disponentin, ein Pendler, eine sehbehinderte Fahrgästin, ein Kundenberater, der Datenschutzbeauftragte und ein BAV-Inspektor. |
| Zoom auf `workshop/agents/`. Dateiliste zeigen: `01-stakeholder-analyst.md` bis `08-story-writer.md`. Einen kurz öffnen, Prompt-Struktur zeigen. | Unter Agents findet ihr acht System-Prompts. Jeder davon verwandelt eine generische KI — Claude, Gemini, was ihr bevorzugt — in einen RE-Spezialisten. Die Prompts sind bewusst auf Englisch gehalten, weil Sprachmodelle mit englischen Systemanweisungen am zuverlässigsten arbeiten. Eure Interaktion mit dem Agenten findet aber ganz normal auf Deutsch statt. |
| Zoom auf `workshop/exercises/`. Modulliste zeigen. | Die Übungen führen euch Schritt für Schritt durch jedes Modul — was ihr dem Agenten gebt, was ihr fragt, wie ihr den Output bewertet, und wo ihr nachfragen müsst. |
| Zoom auf `docs/`. Dokumente kurz auffächern. | Und unter docs liegt die vollständige Referenzlösung. Zehn Business Requirements, dreissig funktionale Anforderungen, sieben Use Cases, eine vollständige Traceability-Matrix. Nach jeder Übung vergleicht ihr euer Ergebnis damit. |

---

## Szene 5 — Der Aha-Moment: generisch vs. Agent (90 Sek.)

| BILD | NARRATION |
|------|-----------|
| Splitscreen. Links: generischer Claude/Gemini-Chat. Rechts: dasselbe Modell mit geladenem Stakeholder-Analyst-Prompt. | Jetzt zeige ich euch den Unterschied, den ein System-Prompt macht. Dieselbe KI, derselbe Input — der Projektauftrag. Links frage ich das generische Modell, die Stakeholder zu identifizieren. Rechts frage ich den Stakeholder-Analyst-Agenten. |
| Linke Seite: eine Aufzählungsliste erscheint. «Disponenten, Fahrgäste, Management, IT-Abteilung...» — vernünftig, aber flach. | Das generische Modell liefert eine brauchbare Liste. Namen, kurze Beschreibungen. Solide als Startpunkt. |
| Rechte Seite: strukturierter Output erscheint. IDs (STK-01, STK-02...), Einfluss- und Interesse-Levels, Konflikterkennung, RACI-Matrix. | Der Agent liefert ein strukturiertes Register mit eindeutigen IDs, Einfluss- und Interesse-Bewertungen, Engagement-Strategien — und eine Konflikterkennung, die die Spannung zwischen Personalvertretung und Betriebsleitung aufdeckt. Er leitet auch Stakeholder ab, die ich nicht erwähnt habe — einen Datenschutzbeauftragten, den ITCS-Lieferanten — und kennzeichnet sie als abgeleitet. |
| Konflikte-Abschnitt auf der rechten Seite hervorheben. | Diese Konflikterkennung? Das ist nicht die KI, die schlau ist. Das ist der System-Prompt, der ihr sagt, nach Konflikten zu suchen. Die Methodik steckt im Prompt, nicht im Modell. |
| Text-Overlay: *«Ihr bittet die KI nicht, schlauer zu sein. Ihr sagt ihr, systematisch zu sein.»* | Ihr bittet die KI nicht, schlauer zu sein. Ihr sagt ihr, systematisch zu sein. Und genau das üben wir heute. |

---

## Szene 6 — Was ihr lernt (30 Sek.)

| BILD | NARRATION |
|------|-----------|
| Ablaufdiagramm, das Modul für Modul aufleuchtet: Stakeholder → Business Requirements → Funktionale & Qualitätsanforderungen → Use Cases → Validierung → Backlog | In den nächsten Stunden arbeitet ihr euch durch den gesamten RE-Lebenszyklus — von der Stakeholder-Analyse über Business Requirements, funktionale Spezifikationen, Use Cases, Validierung bis zu sprintfähigen User Stories. Bei jedem Schritt konfiguriert ihr einen spezialisierten Agenten, wendet ihn auf den PRISMA-Fall an, bewertet den Output — und lernt, wo KI hilft und wo euer Urteil als Analyst unverzichtbar ist. |
| Abschlusskarte: **«Los geht's.»** Repository-URL eingeblendet. | Alles, was ihr braucht, ist im Repository. Los geht's. |

---

## Produktionshinweise

- **Ziel-Laufzeit:** 7–8 Minuten
- **Benötigte Visuals:** Infografiken für die Kennzahlen, ein einfaches Stakeholder-Diagramm,
  ein Ablaufdiagramm der 8 Agenten, Bildschirmaufnahmen eines echten Generisch-vs-Agent-Vergleichs
- **Musik:** dezent im Hintergrund, blendet während der Narration ab
- **Stil:** sauber, minimalistisch — eher Konferenzvortrag als Corporate Training
- **Sprache:** Schweizer Hochdeutsch (kein ß, Schweizer Zahlenschreibweise mit Apostroph)
