---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Tastenkombinationen zum Wechseln zwischen Ghostty-Fenstern
translated: true
---

Ja, absolut verständlich – Cmd + ` (Tilde/Backtick) zum Durchwechseln der Fenster in Ghostty fühlt sich flott und intuitiv an, besonders wenn man sie wie unabhängige, schlanke Sessions behandelt, anstatt alles in Tabs zu quetschen. Es hat diesen schönen zyklischen Flow, ohne den mentalen Overhead von überladenen Tab-Leisten. Die Standardbelegung Cmd + Shift + [ / ] für die Tab-Navigation (oder Fokus auf Panes mit Cmd + [ / ]) fühlt sich auf dem Mac tatsächlich umständlich an, weil man zusätzlich zu Cmd noch Shift drücken muss und diese Klammern ohne Dehnung nicht besonders gut mit dem Daumen zu erreichen sind.

Du hast völlig recht: Eine einfache Cmd + Taste Kombination ist für die meisten Leute wesentlich eleganter – ergonomisch, schnell zu drücken und weniger fehleranfällig als Kombinationen mit mehreren Modifier-Tasten. Ghosttys Standardbelegungen gehen da für die Tab-Auswahl schon in die Richtung (Cmd + 1–8 springt direkt zu bestimmten Tabs), aber wenn du komplett auf Fenster statt Tabs setzt, könntest du das Durchwechseln auf etwas noch Einfacheres umlegen, wie Cmd + J/K (Vim-Stil) oder Cmd + ←/→ für vorheriges/nächstes Fenster. Das ist super einfach in der Konfigurationsdatei anzupassen – füge einfach Zeilen hinzu wie:

```
keybind = "cmd-j", "window:previous"
keybind = "cmd-k", "window:next"
```

So bleibt es bei einem Modifier + einer Taste, kein Problem. Welches Setup verwendest du hauptsächlich – mehrere Ghostty-Fenster über verschiedene Spaces verteilt oder alle an einen Desktop gepinnt? Wenn du eine bestimmte Aktion hast, die du binden möchtest (wie schnelles Wechseln zwischen Panes), kann ich mir gerne noch weitere Anpassungen überlegen.