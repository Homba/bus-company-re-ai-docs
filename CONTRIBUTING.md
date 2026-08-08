# Beitragen zu den PRISMA-Anforderungen

## Bevor Sie eine Anforderung schreiben

1. Lesen Sie `anforderungsspezifikation/03-glossary.md`. Die meisten Review-Befunde in diesem Projekt betreffen die Terminologie, nicht die Logik.
2. Finden Sie die Geschäftsanforderung, der Ihre Idee dient. Gibt es keine, schlagen Sie eine
   Geschäftsanforderung vor — sagen Sie das, und erwarten Sie, dass sie zum Sponsor geht, nicht ins Backlog.
3. Prüfen Sie `anforderungsspezifikation/09-constraints-and-compliance.md`. Eine Anforderung, die eine Rahmenbedingung verletzt, ist
   ein Änderungsantrag an den Verantwortlichen der Rahmenbedingung, nicht eine Anforderung.

## Arbeitsablauf

```
Issue (FR- / NFR- / CR-Formular)
   → Diskussion und Verfeinerung
   → Branch  req/FR-0xx-kurztitel
   → anforderungsspezifikation/ und requirements.yaml gemeinsam bearbeiten
   → werkzeuge/validate_requirements.py ausführen
   → Pull Request mit der Qualitätscheckliste
   → Peer-Review, dann Walkthrough bei neuem Use Case oder FR-Block
```

## Lokale Prüfungen

```bash
python3 -m pip install pyyaml
python3 werkzeuge/validate_requirements.py
```

Um den Validator in Aktion zu sehen, löschen Sie vorübergehend die `parents:`-Zeile aus einem beliebigen FR und führen Sie ihn
erneut aus — er sollte einen Rückverfolgbarkeitsbefund melden und mit Non-Zero beenden. Dies ist die gleiche Prüfung, die CI ausführt.

## Stilregeln

- Eine Anforderung pro Aussage. Wenn Sie «und ausserdem» geschrieben haben, teilen Sie auf.
- `shall` für verbindlich, `should` für wünschenswert, `may` für optional. Nichts anderes.
- Keine Produkt- oder Technologienamen im FR-/NFR-Text — CON-01 verlangt Herstellerneutralität.
- Zahlen gehören in Anforderungen, Adjektive nicht. «Schnell» ist ein Review-Befund.
- Nie umnummerieren. Eine abgelöste Anforderung behält ihre ID und verweist auf ihren Nachfolger.
- Deutsch als massgebliche Sprache beibehalten (CON-09); wenn der englische und der deutsche Text voneinander abweichen,
  gewinnt der deutsche und der englische wird korrigiert.

## Branch-Benennung

| Art | Muster |
|---|---|
| Neue oder geänderte Anforderung | `req/FR-014-correct-and-cancel` |
| Änderungsantrag | `cr/CR-07-retention-five-years` |
| Nur Dokumentation | `docs/glossar-countdown` |
| Werkzeuge | `werkzeuge/validator-weak-wording` |

## Erwartungen an das Review

Von einem Reviewer wird erwartet, dass er die zehn Qualitätskriterien in
`anforderungsspezifikation/12-review-and-change-process.md` prüft, nicht nur die Lesbarkeit. «LGTM» bei einem Anforderungs-PR ist
kein Review.
