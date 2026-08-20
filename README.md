# PRISMA — Anforderungsspezifikation

Anforderungsdokumentation für das Fahrgastinformationssystem **PRISMA** der Regionalverkehr Bernland AG.

> **Prototyp:** Der lauffähige PRISMA-Prototyp befindet sich im separaten Repository [bus-company-re-ai](https://github.com/Homba/bus-company-re-ai).

## Verzeichnisstruktur

| Pfad | Zweck |
|------|-------|
| `anforderungsspezifikation/` | Vollständige Anforderungsspezifikation (12 Kapitel) |
| `anwendungsfaelle/` | Use Cases im Cockburn-Stil |
| `adr/` | Architecture Decision Records |
| `ausgangsmaterial/` | Rohmaterialien (Projektbriefing, Interview-Transkripte) |
| `werkzeuge/` | Agent-System-Prompts und CI-Validierungsskript |
| `additional_exercises/` | Ursprüngliche Workshop-Übungen, Fallstudie und weitere Materialien |

## Validator ausführen

```bash
python3 -m pip install pyyaml
python3 werkzeuge/validate_requirements.py
```

## Lizenz

CC0 1.0 — Public Domain.
