---
audio: false
date: 2025-09-07
generated: true
image: false
lang: de
layout: post
title: Optimierung Ihres Many-Models-Code-Routers
translated: true
type: note
---

Kurze Antwort: ja – Ihr „Many-Models-Router“ kann absolut schlechter abschneiden als ein eng integrierter Stack wie Codex (OpenAIs Code-Assistent), der Ende-zu-Ende auf eine Modellfamilie plus tiefem IDE-Kontext abgestimmt ist. Hier ist der Grund und wie Sie es schnell beheben können.

### Warum sich Codex besser anfühlen kann

* **Ein Gehirn pro Aufgabe.** Das Verbleiben auf einem einzigen Modell erhält dessen latenten Plan und Codierstil. Das Springen zwischen Modellen während einer Aufgabe setzt diesen Plan zurück und führt oft zu widersprüchlichen Konventionen.
* **Vertikale Integration.** Codex (OpenAI) kontrolliert Modell → Tool-Aufrufe → Repo-Index → Tests → Inline-Bearbeitungen. Diese geschlossene Schleife liefert reichhaltigere Signale (Symbolgraph, Datei-Heatmaps, fehlschlagende Tests) mit weniger Latenz durch Verbindungscode.
* **Prompt- und Policy-Abgleich.** Deren Prompts, Code-Formatierer und „Erstelle ein minimales, kompilierbares Diff“-Heuristiken sind für die GPT-5-Familie co-designt. Ein allgemeiner Router kann leicht Temperatur, Stop-Sequenzen oder das Patch-Format für einige Modelle falsch spezifizieren.
* **Latenz/Durchsatz.** Jeder zusätzliche Hop (Proxy, OpenRouter-Middleware, Modell-Aushandlung) fügt Jitter hinzu. Coding-Workflows sind feedback-intensiv; 300–800 ms zusätzliche Latenz pro Runde beeinträchtigen den „Flow“ spürbar.
* **Kontextqualität.** IDE-Integrationen, die eine Repo-Map berechnen (Topologie von Dateien, Symbolen, letzten Änderungen), schlagen „einfach langen Kontext ausspucken“. Lange Kontexte ohne Struktur verschwenden Tokens und verwässern die Aufmerksamkeit.

### Was in Ihrer Konfiguration Ihnen wahrscheinlich schadet

* **Modell-Sprawl.** Sie mischen Generalisten, Coder- und Denkmodelle. Die „Denk“-Varianten (z.B. `claude-3.7-sonnet:thinking`, `deepseek-r1`) sind großartig für Beweise, aber langsamer und gesprächiger für Code-Bearbeitungen.
* **Fehlende Übereinstimmung der Standardroute.** `default: "openrouter,x-ai/grok-code-fast-1"` sieht so aus, als wollten Sie Grok Code Fast, aber es ist nicht in Ihrem `models`-Array aufgeführt. Das kann zu stillem Fallback und Inkonsistenz führen.
* **Unbegrenzte Intents.** Ein „Default“ für alles bedeutet, dass kleine Bearbeitungen, schwere Refactorings und Long-Context-Lesevorgänge alle denselben Pfad kämpfen.
* **Temperatur-/Format-Drift.** Wenn Sie nicht Low-Temp + strenges Patch-Format pro Modell erzwingen, variieren die Ausgaben wild über verschiedene Provider hinweg.

### Machen Sie Ihren Router „Codex-ähnlich“

1.  **Wählen Sie einen Primären und bleiben Sie pro Aufgabe dabei.** Wählen Sie einen starken Coder als Standard (z.B. `openai/gpt-5` oder `x-ai/grok-code-fast-1` oder `qwen/qwen3-coder`) und wechseln Sie nur bei klaren Gründen (sehr langer Kontext oder schwere Mathematik).
2.  **Sharden nach Intent (nicht nach Marke).**

    *   *Kleine Bearbeitung / schnelle Fixes:* schnelles Modell (GPT-5-mini oder Gemini-Flash).
    *   *Refactoring / Multi-File-Change:* GPT-5 (oder Claude Sonnet 3.7 non-thinking).
    *   *Ultra-Long-Context-Read:* Kimi-K2.
    *   *Schweres Reasoning vor dem Coden:* DeepSeek-R1 für Umriss → Übergabe an Coder-Modell zur Erstellung des Patches.
3.  **Erzwingen Sie einen strengen Patch-Vertrag.** Fragen Sie immer nach einem Unified Diff oder explizitem „ApplyPatch“-JSON mit Dateipfaden + Hunks. Lehnen Sie alles andere ab und reprompten Sie automatisch.
4.  **Reduzieren Sie die Zufälligkeit für Code.** `temperature: 0–0.2`, keine Frequency/Presence Penalties, und begrenzen Sie `top_p` ~0.9.
5.  **Geben Sie eine Repo-Map, nicht nur Tokens.** Füttern Sie einen kompakten Symbolindex: Einstiegspunkte, Schlüsselklassen/-funktionen, Test-Targets, letzte Diffs. Das schlägt das Ausspucken von 200k Tokens roher Dateien.
6.  **Halten Sie die Tool-Schleife eng.** Ein Modell schlägt Patch vor → Sie führen Build/Tests/Linters aus → geben Sie Fehler zum *selben* Modell zurück, um zu iterieren. Vermeiden Sie Modellwechsel mitten in der Schleife.
7.  **Kürzen Sie die Modellliste.** Behalten Sie max. 3–5. Jedes zusätzliche erhöht die Varianz und Routing-Fehler.
8.  **Entfernen Sie „Thinking“-Modelle aus Hot Paths.** Verwenden Sie sie nur, um einen kurzen Design-Plan zu erstellen, und wechseln Sie dann zu einem Coder für die eigentlichen Bearbeitungen.

### Eine schlankere Konfiguration (Drop-in-Idee; passen Sie die Namen an Ihr Framework an)

```json
{
  "PROXY_URL": "http://127.0.0.1:7890",
  "LOG": true,
  "Providers": [
    {
      "name": "openrouter",
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "",
      "models": [
        "openai/gpt-5",
        "openai/gpt-5-mini",
        "x-ai/grok-code-fast-1",
        "moonshotai/kimi-k2",
        "anthropic/claude-3.7-sonnet",
        "qwen/qwen3-coder"
      ],
      "transformer": {"use": ["openrouter"]}
    }
  ],
  "Router": {
    "default": "openrouter,openai/gpt-5",
    "quickEdit": "openrouter,openai/gpt-5-mini",
    "refactor": "openrouter,openai/gpt-5",
    "reasonPlan": "openrouter,anthropic/claude-3.7-sonnet",
    "longContext": "openrouter,moonshotai/kimi-k2",
    "longContextThreshold": 220000,
    "webSearch": "openrouter,qwen/qwen3-coder"
  }
}
```

### Prompt-Scaffolds, die die Ausgaben stabilisieren (keine Tabellen)

*   **System:** „You are a senior software engineer. Produce minimal, compilable patches. Keep style consistent with the repo. If unsure, ask a single clarifying question, otherwise proceed.“
*   **Regeln:** „Output ONLY a unified diff (git format). Never include commentary. If a file doesn’t exist, create it and include in the diff. Preserve license headers.“
*   **Kontextblock:** Repo-Map (Dateien, Schlüsselsymbole), aktuelle Fehler, Test-Targets.
*   **Tool-Schleife:** Nach dem Diff automatisch `build + tests + lints` ausführen; geben Sie nur Fehler zum *selben* Modell zurück.

### Praktische Hygiene

*   Kürzen Sie Ihre Modellliste und korrigieren Sie den Standard auf ein Modell, das tatsächlich in `models` existiert.
*   Setzen Sie Temperaturen pro Route; halten Sie Code bei 0–0.2.
*   Cachen Sie die Repo-Map zwischen den Turns; senden Sie keine riesigen Kontexte erneut, es sei denn, Dateien haben sich geändert.
*   Vermeiden Sie Modellwechsel mitten in der Aufgabe.
*   Bevorzugen Sie „Diff“ gegenüber „Ersetze diese ganze Datei“, um halluzinierte Imports zu reduzieren.

Wenn Sie möchten, posten Sie die Prompt- und Temperatureinstellungen Ihres Routers, und ich werde sie für jede Route straffen, damit Claude Code und Ihr Stack sich konsistenter mit Codex-ähnlicher Zuverlässigkeit verhalten.