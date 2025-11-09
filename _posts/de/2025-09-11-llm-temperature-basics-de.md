---
audio: false
date: 2025-09-11
generated: true
image: false
lang: de
layout: post
model: openai/gpt-5
title: Grundlagen des LLM-Temperaturparameters
translated: true
type: note
---

In LLM-APIs (wie OpenAI, Copilot API, Anthropic, etc.) ist **Temperature** ein Parameter, der steuert, wie *zufällig* oder *deterministisch* die Ausgabe des Modells ist.

---

### Was Temperature bewirkt

* **Niedrige Temperature (nahe 0):**
  Das Modell wird deterministisch und wählt immer den wahrscheinlichsten nächsten Token.
  Beispiel: Wenn Sie nach einer Definition fragen, wird es jedes Mal die standardmäßigste/erwartete Antwort geben.

* **Hohe Temperature (nahe 1 oder darüber):**
  Das Modell sampelt freier und erkundet weniger wahrscheinliche Tokens. Dies erhöht die Vielfalt, Kreativität und Unvorhersehbarkeit.
  Beispiel: Für Brainstorming, Geschichtenerzählen oder das Generieren von Code-Variationen kann eine höhere Temperature besser sein.

---

### Was „0.7“ bedeutet

* `temperature = 0.7` ist eine **moderate Balance**.

  * Sie erlaubt etwas Zufälligkeit und Vielfalt.
  * Das Modell wird nicht so starr sein wie bei `0`, aber nicht so „wild“ wie bei `1.2`.
  * Deshalb wird **0.7 oft als Standard** in vielen APIs verwendet, einschließlich Copilot-ähnlichen Systemen – sie liefert kreative, aber dennoch zuverlässige Ergebnisse.

---

### Wie man sie verwendet

In den meisten APIs übergeben Sie sie als Parameter in der Anfrage. Zum Beispiel:

**OpenAI API (Chat Completion):**

```json
{
  "model": "gpt-4.1",
  "messages": [
    {"role": "user", "content": "Write a short story about a dragon and a robot."}
  ],
  "temperature": 0.7
}
```

**GitHub Copilot API:**
Der Parameter funktioniert ähnlich. Copilot verwendet intern die Temperature, um zwischen wörtlicheren Vervollständigungen und explorativeren Vorschlägen zu entscheiden. Die meisten IDE-Integrationen setzen sie auf etwa `0.7`, aber einige Kontexte (wie Code-Completion) können niedrigere Werte für Stabilität verwenden.

---

✅ **Faustregel:**

* **0–0.3** → Deterministisch, sachlich, vorhersehbar. Gut für Mathematik, API-Dokumentation, Konfiguration, Unit-Tests.
* **0.4–0.7** → Ausgewogen, natürliches Schreiben, Standard-Coding. Guter Standard für die meisten Fälle.
* **0.8–1.2** → Kreativ, explorativ, risikofreudig. Gut für Brainstorming, Geschichten, Poesie.

---

Möchten Sie, dass ich Ihnen auch zeige, wie **Temperature mit `top_p` (Nucleus Sampling) interagiert**, da beide oft in Copilot/LLM-APIs verfügbar sind?