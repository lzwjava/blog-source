---
audio: false
generated: true
image: false
lang: de
layout: post
title: Deaktiviere Cache in Claude Code
translated: true
type: note
---

In **Claude Code** bedeutet dieser Ausschnitt

```json
"cache_control": {
  "type": "ephemeral"
}
```

dass die Antwort (oder das Artefakt), die vom Modell erzeugt wird, **nicht zwischengespeichert wird, um wiederverwendet zu werden**.

### Warum es existiert

Normalerweise können Claude Code (und andere Anthropic SDKs) Antworten zwischenspeichern, um die Abläufe zu beschleunigen, wenn Sie denselben Prompt erneut senden. Wenn Sie jedoch `"cache_control": { "type": "ephemeral" }` setzen, teilen Sie der API Folgendes mit:

* **Dieses Ergebnis nicht im Cache persistieren**.
* **Es nicht wiederverwenden**, falls später eine identische Anfrage eingeht.
* Die Antwort als **kurzlebig** behandeln – nur für diesen Aufruf.

### Wann man es verwendet

Dies ist nützlich, wenn:

* Ihre Anfrage **sensible oder persönliche Daten** enthält, die Sie nicht zwischengespeichert haben möchten.
* Sie **einmalige Abfragen** senden, die von einer Wiederverwendung nicht profitieren würden.
* Sie jedes Mal **frische Ausgaben** wünschen, selbst wenn der Anfragetext identisch ist.

Kurz gesagt macht `"ephemeral"` Claudes Ausgabe *flüchtig* – privat für diese Interaktion, ohne Zwischenspeicherung über Aufrufe hinweg.

Möchten Sie, dass ich auch erkläre, wie sich dies vom standardmäßigen `cache_control`-Verhalten in Claude Code unterscheidet (z.B. `type: "default"` vs. `"none"` vs. `"ephemeral"`)?