---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Farbcodes von Widerständen lesen
translated: true
type: note
---

### Widerstandsfarbcodes verstehen

Widerstände sind kleine elektronische Bauteile, die den Fluss des elektrischen Stroms begrenzen. Ihr Widerstandswert (gemessen in Ohm, Ω) wird oft durch farbige Ringe auf ihrem Körper angezeigt. Diese Ringe folgen einem standardisi Farbcodesystem. Die meisten Widerstände haben 4, 5 oder 6 Ringe, wobei 4- und 5-Ring-Typen am gebräuchlichsten sind. Lesen Sie die Ringe immer von links nach rechts, beginnend mit dem Ring, der einem Ende am nächsten ist (dem "Leseende"). Der Toleranzring (oft gold oder silber) befindet sich normalerweise auf der rechten Seite – wenn Sie unsicher sind, drehen Sie den Widerstand so, dass sich ein metallischer Ring auf der rechten Seite befindet.

#### Farbcode-Tabelle
Jede Farbe stellt eine Ziffer (0-9) für die signifikanten Stellen oder einen Multiplikator (Potenz von 10) zur Skalierung des Wertes dar. Hier ist die Standardzuordnung:

| Farbe    | Zahlenwert | Multiplikator (Potenz von 10) |
|----------|-------------|---------------------------|
| Schwarz | 0           | ×10⁰ (1)                 |
| Braun   | 1           | ×10¹ (10)                |
| Rot     | 2           | ×10² (100)               |
| Orange  | 3           | ×10³ (1.000)             |
| Gelb    | 4           | ×10⁴ (10.000)            |
| Grün    | 5           | ×10⁵ (100.000)           |
| Blau    | 6           | ×10⁶ (1.000.000)         |
| Violett | 7           | ×10⁷ (10.000.000)        |
| Grau    | 8           | ×10⁸ (100.000.000)       |
| Weiß    | 9           | ×10⁹ (1.000.000.000)     |
| Gold    | -           | ×10⁻¹ (0,1)              |
| Silber  | -           | ×10⁻² (0,01)             |

#### Toleranzringe
Der letzte Ring (oder die letzten Ringe) gibt die Toleranz an (Genauigkeit des Widerstandswertes):
- Braun: ±1%
- Rot: ±2%
- Grün: ±0,5%
- Blau: ±0,25%
- Violett: ±0,1%
- Grau: ±0,05%
- Gold: ±5%
- Silber: ±10%
- Kein Ring: ±20%

#### So lesen Sie einen 4-Ring-Widerstand
1. Identifizieren Sie die ersten beiden Ringe als die signifikanten Ziffern (z.B. braun-schwarz = 10).
2. Der dritte Ring ist der Multiplikator – multiplizieren Sie die Ziffern mit dieser Potenz von 10 (z.B. rot = ×100, also 10 × 100 = 1.000 Ω).
3. Der vierte Ring ist die Toleranz (z.B. gold = ±5%).

**Beispiel**: Braun (1), Schwarz (0), Rot (×100), Gold (±5%) = 10 × 100 = 1.000 Ω ±5% (oder 1 kΩ).

#### So lesen Sie einen 5-Ring-Widerstand
Diese bieten eine höhere Präzision mit einer zusätzlichen signifikanten Ziffer.
1. Identifizieren Sie die ersten drei Ringe als signifikante Ziffern (z.B. braun-schwarz-rot = 102).
2. Der vierte Ring ist der Multiplikator (z.B. orange = ×1.000, also 102 × 1.000 = 102.000 Ω).
3. Der fünfte Ring ist die Toleranz (z.B. braun = ±1%).

**Beispiel**: Braun (1), Schwarz (0), Rot (2), Orange (×1.000), Braun (±1%) = 102 × 1.000 = 102.000 Ω ±1% (oder 102 kΩ).

#### Hinweise
- Bei 6-Ring-Widerständen folgen die ersten fünf Ringe dem 5-Ring-Muster, und der sechste gibt den Temperaturkoeffizienten an (wie sich der Widerstand mit der Wärme ändert, z.B. braun = 100 ppm/°C).
- Wenn die Ringe verblasst oder undeutlich sind, verwenden Sie ein Multimeter, um den tatsächlichen Widerstand zu messen.
- Null-Ohm-Widerstände (Jumper) können einen einzelnen schwarzen Ring haben.

[How To Read Resistor Color Codes | Arrow.com](https://www.arrow.com/en/research-and-events/articles/resistor-color-code)  
[RESISTOR COLOR CODE GUIDE (PDF)](https://neurophysics.ucsd.edu/courses/physics_120/resistorcharts.pdf)