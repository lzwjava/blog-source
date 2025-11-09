---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Grundlagen der Effektivspannungsberechnung
translated: true
type: note
---

### Erklärung

Die Effektivspannung (RMS-Spannung), \\( V_{RMS} \\), repräsentiert den effektiven Wert einer Wechselspannung, der die gleiche Leistung in einem ohmschen Widerstand erzeugt wie eine Gleichspannung (DC) derselben Größe. Für einen sinusförmigen Verlauf \\( v(t) = V_{max} \sin(\omega t) \\), wobei \\( V_{max} \\) die Spitzenspannung (maximale Spannung) ist, wird der RMS-Wert wie folgt abgeleitet:

1.  **Mittelwert des Quadrats**: Das Quadrat der Momentanspannung über eine Periode \\( T \\) ist \\( v^2(t) = V_{max}^2 \sin^2(\omega t) \\). Der Durchschnitt (Mittelwert) von \\( \sin^2(\omega t) \\) über eine Periode ist \\( \frac{1}{2} \\), also ist der quadratische Mittelwert der Spannung \\( \frac{V_{max}^2}{2} \\).

2.  **RMS-Berechnung**: Ziehe die Quadratwurzel aus dem quadratischen Mittelwert:  
    \\[
    V_{RMS} = \sqrt{\frac{V_{max}^2}{2}} = \frac{V_{max}}{\sqrt{2}}
    \\]

3.  **Numerische Annäherung**: Da \\( \sqrt{2} \approx 1.414 \\), ist \\( \frac{1}{\sqrt{2}} \approx 0.707 \\). Somit gilt: \\( V_{RMS} \approx 0.707 \times V_{max} \\).

Dies bestätigt Option **B**. Die anderen Optionen sind falsch:  
- A überschätzt den Wert (ignoriert die Mittelwertbildung).  
- C kehrt den Faktor um (das ist \\( V_{max} = \sqrt{2} \times V_{RMS} \\)).  
- D unterschätzt den Wert (das ist der Gleichrichtwert für eine sinusförmige Wechselspannung, nicht der RMS-Wert).