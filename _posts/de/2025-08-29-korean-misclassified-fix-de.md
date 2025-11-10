---
audio: false
generated: true
image: false
lang: de
layout: post
title: Koreanisch fälschlicherweise als Chinesisch klassifiziert Korrektur
translated: true
type: note
---

Verstanden — in dieser Debug-Ausgabe:

```
Debug: raw langdetect output: [('ko', 0.9999995211930662)]
...
Erkannte Sprachen: [('ko', 0.9999995211930662)]
```

Der Code **`ko`** ist der ISO 639-1-Sprachcode für **Koreanisch**. 🇰🇷

`langdetect` sagt also:

* Es hält den Text für Koreanisch (`ko`)
* Mit einer Wahrscheinlichkeit von ≈ **0.9999995** (praktisch 100%)

Das erklärt den Fehler: Dein Validator erwartete `"zh-tw"` (Traditionelles Chinesisch), aber der Detektor entschied, dass die Eingabe wie Koreanisch aussieht.

👉 Kurze Zuordnungserinnerung von `langdetect` / ISO 639-1:

* `zh` → Chinesisch (nicht spezifiziert)
* `zh-cn` → Vereinfachtes Chinesisch (China)
* `zh-tw` (oder `hant` in deiner Zuordnung) → Traditionelles Chinesisch (Taiwan)
* `ja` → Japanisch
* `ko` → Koreanisch
* `ne` → Nepalesisch
* `hi` → Hindi

Möchtest du, dass ich vorschlage, wie du **deinen Validator robuster machen** kannst, damit er nicht fehlschlägt, wenn `langdetect` falsch klassifiziert (z.B. durch einen Fallback, wenn die Zielschriftzeichen eindeutig Chinesisch sind, der Code aber als `ko` zurückkommt)?