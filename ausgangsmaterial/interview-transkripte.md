# Simulierte Stakeholder-Interviewprotokolle

> Diese Protokolle simulieren Interviews, wie sie eine Business-Analystin im Rahmen der
> Anforderungserhebung führen würde. Sie dienen als Input für den Requirements-Elicitor-Agent.

---

## Interview 1: Nadia, Senior-Disponentin (8 Jahre Erfahrung)

**Analystin:** Beschreiben Sie mir, was passiert, wenn ein Bus eine Panne hat.

**Nadia:** Also, der Chauffeur meldet sich per Funk. Ich rufe das Fahrzeug auf dem ITCS-Bildschirm
auf, um zu sehen, wo es steht. Dann muss ich entscheiden: Können wir einen Ersatzbus schicken,
fällt der Kurs aus, oder leiten wir um? Das ist der betriebliche Teil. Aber dann muss ich auch
die Fahrgäste informieren. Also öffne ich das Website-CMS — das ist ein separater Browser-Tab —
und schreibe so etwas wie «Linie 7 Richtung Oberburg: Abfahrt 14:35 ab Bahnhof fällt wegen
Fahrzeugpanne aus. Nächste Abfahrt 15:05.» Dann sollte ich dasselbe ins App-Admin-Panel und
ins SMS-System eintippen. Aber ehrlich gesagt? Während der Hauptverkehrszeit schaffe ich manchmal
nur die Website. App und SMS werden 10, 15 Minuten später aktualisiert, oder gar nicht.

**Analystin:** Was würde Ihnen am meisten helfen?

**Nadia:** Einmal tippen. Nur einmal. Und es geht überall raus. Aber ich brauche Vorlagen — ich
kann während eines Vorfalls keine Aufsätze schreiben. So etwas wie «Linie [X], Abfahrt [Uhrzeit]
ab [Haltestelle]: [fällt aus / verspätet um X Min. / umgeleitet via Y]. Grund:
[Panne / Strassensperrung / Veranstaltung].» Ich wähle aus Dropdowns und ergänze die Details.
Erledigt in 30 Sekunden.

**Analystin:** Wie ist es mit mehreren Sprachen?

**Nadia:** Ich kann Deutsch und zur Not auch Französisch, aber mein Französisch reicht nicht für
öffentliche Durchsagen. Italienisch? Auf keinen Fall. Wir haben eine Disponentin, die Italienisch
spricht, aber die ist nur in der Frühschicht. Wir brauchen automatische Übersetzung oder
vorübersetzte Vorlagen.

**Analystin:** Wie handhaben Sie die Haltestellenanzeigen?

**Nadia:** Gar nicht. Die zeigen einfach die planmässigen Abfahrtszeiten aus dem ITCS. Wenn ein
Bus ausfällt, steht auf der Anzeige immer noch «3 Min.», bis die planmässige Zeit verstrichen
ist. Dann verschwindet der Eintrag einfach. Es gibt keine Möglichkeit für mich, eine
Störungsmeldung von meinem Arbeitsplatz aus auf die Anzeigen zu schicken. Der ITCS-Hersteller
hat gesagt, er könnte das einbauen, aber es würde extra kosten und braucht ein Protokoll, das
er noch nicht implementiert hat.

---

## Interview 2: Beat, täglicher Pendler (45, nimmt Linie 3 von Mühlenberg zum Bahnhof)

**Analystin:** Wie informieren Sie sich über Ihren Bus?

**Beat:** Ich schaue in die App. Normalerweise stimmt das. Aber wenn etwas schiefläuft, ist die
App nutzlos. Letzten Monat fiel mein Bus aus und ich stand 20 Minuten im Regen, bevor ich auf
der Website nachgeschaut und es dort erfahren habe. Die App zeigte den Bus immer noch als
«pünktlich» an. Das geht nicht.

**Analystin:** Welche Informationen brauchen Sie bei einer Störung?

**Beat:** Drei Dinge. Erstens: Kommt mein Bus oder nicht? Zweitens: Falls nicht, wann fährt der
nächste? Drittens: Betrifft das meinen Anschluss? Ich steige am Bahnhof auf den Regionalzug
um. Wenn mein Bus 10 Minuten Verspätung hat, verpasse ich den Zug und bin 40 Minuten zu spät
bei der Arbeit. Diese Anschlussinformation ist entscheidend.

**Analystin:** Was sagen Sie zu den Haltestellenanzeigen?

**Beat:** Meine Haltestelle hat keine. Aber selbst am Bahnhof, wo es eine gibt, zeigt sie nur
Countdown-Zeiten an. Wenn der Countdown «2 Min.» sagt, vertraue ich dem, aber manchmal kommt
der Bus nicht und die Anzeige springt einfach zur nächsten Abfahrt. Keine Erklärung. Wurde der
Kurs gestrichen? Hat er Verspätung? Keine Ahnung.

---

## Interview 3: Frau Lehmann, pensionierte Fahrgästin (72, sehbehindert, nutzt Screenreader)

**Analystin:** Wie informieren Sie sich über das Busangebot?

**Frau Lehmann:** Meine Tochter hat mir die RVB-Website gezeigt. Ich benutze VoiceOver auf meinem
iPad. Die Abfahrtstabellen sind... schwierig. Die Website hat teilweise Bilder ohne Alt-Text,
und die Störungsmeldungen sind manchmal auch als Bilder eingebettet — Screenshots von irgendwo.
VoiceOver kann die überhaupt nicht vorlesen.

**Analystin:** Was würde es Ihnen leichter machen?

**Frau Lehmann:** Text. Einfach richtiger Text, den mein Screenreader vorlesen kann. Und
verständliche Sprache — keine Abkürzungen, die ich nicht verstehe. Was ist «ITCS»? Was ist «VDV»?
Sagen Sie mir «Ihr Bus hat 10 Minuten Verspätung» in einem ganzen Satz. Auch an der Haltestelle:
Die Anzeige zeigt winzige Zahlen. Selbst mit Brille kann ich sie kaum lesen. Ich habe nach
Lautsprecherdurchsagen gefragt, aber man hat mir gesagt, das sei mit dem aktuellen System nicht
möglich.

**Analystin:** Reisen Sie auch in französischsprachige Gebiete?

**Frau Lehmann:** Manchmal besuche ich meine Schwester in Villars. Die Meldungen dort sollten
natürlich auf Französisch sein. Aber in der App, wenn ich auf Französisch umschalte, ist die
Hälfte der Störungsmeldungen immer noch auf Deutsch. Das hilft mir nicht weiter.

---

## Interview 4: Tobias, Kundendienst-Mitarbeiter (3 Jahre bei der RVB)

**Analystin:** Was frustriert Sie am meisten bei der Fahrgastinformation?

**Tobias:** Wenn ein Fahrgast anruft und sagt: «Eure App hat mir gesagt, der Bus kommt, aber er
kam nicht» — dann habe ich keine Möglichkeit nachzuprüfen, was er gesehen hat. Ich kann die
Website anschauen, aber die App hat vielleicht etwas anderes angezeigt. Und bis der Fahrgast
anruft, wurde die Störungsmeldung möglicherweise schon aktualisiert oder entfernt. Ich tappe
völlig im Dunkeln.

**Analystin:** Was bräuchten Sie?

**Tobias:** Ein Dashboard, das mir genau zeigt, was wann auf welchem Kanal veröffentlicht wurde,
mit Zeitstempeln. Damit ich bei einem Anruf sagen kann: «Ich sehe, dass um 14:32 in der App
‹Linie 7 fällt aus› angezeigt wurde und um 14:35 die Website mit derselben Information
aktualisiert wurde.» Das würde auch bei Beschwerden helfen — wir könnten tatsächlich überprüfen,
ob der Fahrgast informiert wurde oder nicht.

**Analystin:** Was ist mit internem Kontext?

**Tobias:** Manchmal ist der Grund für eine Störung heikel — ein medizinischer Notfall oder ein
Chauffeur, der nicht zum Dienst erscheint. Das können wir nicht in die öffentliche Meldung
schreiben. Aber ich muss es intern wissen, damit ich angemessen reagieren kann, wenn ein
Fahrgast nachfragt. Gebt mir ein internes Notizfeld, das nur für das Personal sichtbar ist.

---

## Interview 5: Dr. Müller, Datenschutzbeauftragter

**Analystin:** Welche Bedenken haben Sie bezüglich eines neuen Fahrgastinformationssystems?

**Dr. Müller:** Fahrzeugpositionen. Das ITCS trackt die Busse in Echtzeit. Wenn PRISMA diese
Daten erhält, könnte man damit theoretisch die Bewegungen einzelner Chauffeure über die gesamte
Schicht nachvollziehen. Die Personalkommission wird das blockieren, wenn wir keine Schutzmassnahmen
haben.

**Analystin:** Welche Schutzmassnahmen bräuchten Sie?

**Dr. Müller:** Erstens Zweckbindung: Fahrzeugpositionsdaten werden ausschliesslich zur Berechnung
von Abfahrtsprognosen verwendet, nicht zur Leistungsüberwachung der Fahrenden. Zweitens
Aufbewahrungsfristen: Rohe Positionsdaten müssen nach 24 Stunden gelöscht werden. Aggregierte,
anonymisierte Daten können für Planungszwecke länger aufbewahrt werden. Drittens keine
Fahrer-Identifikatoren im System — das System weiss «Fahrzeug 471 ist an Position X», aber
niemals «Fahrer Meier ist an Position X». Und wir brauchen eine formelle
Datenschutz-Folgenabschätzung vor dem Go-live.

**Analystin:** Wie steht es mit der Nachvollziehbarkeit?

**Dr. Müller:** Störungsmeldungen sind öffentliche Kommunikation im Namen eines
Konzessionsnehmers. Wir sind verpflichtet, nachvollziehen zu können, wer was wann und über
welchen Kanal veröffentlicht hat. Aufbewahrungsfrist für regulatorische Zwecke: mindestens
3 Jahre. Das Audit-Log muss manipulationssicher sein — niemand darf die Historie nachträglich
ändern können.

---

## Interview 6: Pierre Dubois, BAV-Compliance-Inspektor

**Analystin:** Was verlangt das BAV von der RVB bezüglich Echtzeitdaten?

**Pierre:** Die Konzession schreibt die Lieferung von Echtzeitdaten an die nationale Plattform
nach SIRI-Standards vor — konkret SIRI-ET für geschätzte Fahrpläne und SIRI-SX für den
Situationsaustausch (Störungen). Die RVB liefert derzeit weder das eine noch das andere. Der
statische NeTEx-Export, den sie jede Nacht senden, genügt nicht.

**Analystin:** Wie sieht der Zeitplan für die Umsetzung aus?

**Pierre:** Wir haben die Feststellung im November 2024 erlassen. Wir erwarten einen
Massnahmenplan innerhalb von 6 Monaten und die Umsetzung innerhalb von 18 Monaten. Also
sollten wir bis ungefähr Mitte 2026 zumindest erste SIRI-Feeds sehen. Die Feeds müssen eine
Verfügbarkeit von mindestens 99,5 % aufweisen, gemessen pro Monat. Der nationale
Plattformkanal darf nicht optional sein — Transportunternehmen dürfen der öffentlichen
Plattform keine Störungsinformationen vorenthalten.

**Analystin:** Gibt es bestimmte SIRI-Profile, die eingehalten werden müssen?

**Pierre:** Ja, das Schweizer SIRI-Profil, herausgegeben von der Alliance SwissPass. Es legt
obligatorische und optionale Felder, die Nachrichtenstruktur und die Übermittlungsmechanismen
fest. Ihr System muss die Konformitätstestsuite bestehen, bevor es in Betrieb genommen werden
kann.
