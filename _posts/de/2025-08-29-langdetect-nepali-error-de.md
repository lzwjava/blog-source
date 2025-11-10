---
audio: false
generated: true
image: false
lang: de
layout: post
title: Langdetect hielt Text fälschlicherweise für Nepali
translated: true
type: note
---

Ah, verstehe – danke für die Klarstellung.

In dem von dir eingefügten Log:

```
Debug: raw langdetect output: [('ne', 0.9999953270916105)]
Debug: normalized langdetect output: [('ne', 0.9999953270916105)]
Debug: Detected languages: [('ne', 0.9999953270916105)]
```

Hier ist **`ne` nicht das französische Wort** – es handelt sich tatsächlich um einen **Sprachcode**, der von `langdetect` ausgegeben wird.

Die `langdetect`-Bibliothek gibt manchmal `"ne"` als ISO 639-1-Code für **Nepali** zurück.

* `"en"` = Englisch
* `"fr"` = Französisch
* `"hi"` = Hindi
* `"ne"` = Nepali

In diesem Fall dachte `langdetect` also, dein Text sei Nepali, mit einer Wahrscheinlichkeit von `~0.99999`.

Deshalb ist deine Validierung fehlgeschlagen mit:

```
Translated text does not contain the target language 'hi' (detected: [('ne', 0.9999953270916105)])
```

👉 Zusammenfassend:

* `ne` bedeutet hier = ISO-Sprachcode **Nepali**, nicht das französische Verneinungswort `"ne"`.
* Es erscheint, wenn `langdetect` entscheidet, dass deine Eingabe wie Nepali aussieht.

Möchtest du, dass ich dir zeige, wie du **`ne` (Nepali) normalisieren oder umleiten** kannst in deiner `_map_target_code`, damit dein Validator nicht abstürzt, wenn unerwartete Sprachen auftauchen?