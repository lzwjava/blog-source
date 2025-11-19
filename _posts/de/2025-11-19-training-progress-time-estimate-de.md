---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Trainingsfortschritt und Zeitabschätzung
translated: true
type: note
---

### Aktueller Fortschritt
- Du hast gerade Iteration 2800 geschafft (von deinem Ziel 20.000)
- Stabile Geschwindigkeit aktuell: **≈ 3,91 Sekunden pro Iteration**  
  (die gelegentlichen 19-Sekunden-Logs bei den Evaluierungsschritten sind nur alle 500 Iterationen und beeinflussen den Durchschnitt kaum)

### Verbleibende Iterationen
20.000 − 2.800 = **17.200 Iterationen übrig**

### Geschätzte verbleibende Zeit

| Durchschn. Iterationszeit | Verbleibende Zeit | Voraussichtlicher Abschluss (ab jetzt, 19. Nov. 2025) |
|-------------------|----------------|---------------------------------------------|
| 3,91 s (aktuell)  | **18 Stunden 35 Minuten** | ~ **morgen (20. Nov.) gegen 14:30–15:30** (abhängig von deiner Zeitzone und dem genauen Startzeitpunkt dieses Logs) |
| Etwas schneller (3,8 s, häufig wenn die MFU noch etwas steigt) | ~ 18 Stunden         | morgen früher bis mittlerer Nachmittag              |
| Etwas langsamer (4,0 s) | ~ 19 Stunden 5 Min   | morgen ~16:00                            |

Realistische Erwartung bei einer RTX 4070 mit diesem exakten Setup: **18–19 Stunden ab jetzt**.

### Kurzreferenz
- Wenn du mit dem Loggen heute gegen Mittag–frühen Nachmittag angefangen hast → Abschluss morgen Vormittag–früher Nachmittag.
- Wenn du es über Nacht laufen lässt → wachst du morgen mit einem fertigen (oder fast fertigen) sehr starken 40M Modell auf.

Dein Loss-Wert sinkt erfreulich (Val Loss bereits bei 3,94 nach nur ~1,5B gesehenen Tokens) und fällt weiterhin stetig. Es lohnt sich absolut, die vollen 20k laufen zu lassen — lass es einfach über Nacht laufen und du hast morgen Nachmittag ein exzellentes Modell!