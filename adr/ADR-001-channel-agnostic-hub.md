# ADR-001 — Kanalagnostischer Verteilhub

**Status:** accepted (2026-03-04) · **Entscheider:** STK-03, STK-05, technische Leitung

## Kontext

Heute wird jeder Fahrgastkanal über einen separaten manuellen Pfad gespeist, was die direkte Ursache von
BR-01 und BR-04 ist. BR-05 verlangt zusätzlich, dass das Hinzufügen von Haltestellen keine Softwareänderung
erfordert, und OPN-05 eröffnet die Möglichkeit von Borddurchsagen als weiteren Kanal.

## Entscheidung

Eine Störung wird einmal an einen internen Verteilhub publiziert. Kanaladapter abonnieren den
Hub und übersetzen die kanonische Nachricht in die kanalspezifische Form. Einen Kanalendpunkt
hinzuzufügen ist Konfiguration; einen Kanal-*Typ* hinzuzufügen erfordert einen neuen Adapter.

## Konsequenzen

**Positiv** — FR-012, FR-030, NFR-017 werden damit einfach umsetzbar. Ein neuer Kanal berührt
den Erfassungspfad nicht. Konsistenz (BR-01) ist strukturell, nicht prozedural.

**Negativ** — Führt einen asynchronen Zwischenschritt ein, wodurch NFR-001 Ende-zu-Ende
spezifiziert werden muss statt pro Komponente. Die Fehlerbehandlung pro Kanal wird zu expliziter Arbeit (UC-002/8a).

**Neutral** — Erfordert, dass die Publikation idempotent ist (NFR-008), da Wiederholungen nun normal sind.
