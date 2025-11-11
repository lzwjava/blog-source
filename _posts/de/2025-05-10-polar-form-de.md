---
audio: false
generated: true
lang: de
layout: post
title: Polarkoordinatensystem
translated: true
type: note
---

Das Polarkoordinatensystem ist ein zweidimensionales Koordinatensystem, in dem jeder Punkt auf einer Ebene durch einen Abstand von einem Referenzpunkt und einen Winkel von einer Referenzrichtung bestimmt wird. Dies steht im Gegensatz zum kartesischen Koordinatensystem, das x- und y-Koordinaten verwendet, um einen Punkt zu definieren.

In Polarkoordinaten wird ein Punkt als \\((r, \theta)\\) dargestellt, wobei:
- \\(r\\) der radiale Abstand vom Ursprung (dem Referenzpunkt) ist.
- \\(\theta\\) die Winkelkoordinate ist, üblicherweise gemessen in Radiant von der positiven x-Achse (der Referenzrichtung).

### Beispiele für Polarkoordinaten

1. **Einfacher Punkt:**
   - Kartesische Koordinaten: \\((1, 0)\\)
   - Polarkoordinaten: \\((1, 0)\\)
   - Erklärung: Der Punkt befindet sich 1 Einheit vom Ursprung entfernt entlang der positiven x-Achse.

2. **Punkt in der Ebene:**
   - Kartesische Koordinaten: \\((0, 1)\\)
   - Polarkoordinaten: \\((1, \frac{\pi}{2})\\)
   - Erklärung: Der Punkt ist 1 Einheit vom Ursprung entfernt, in einem Winkel von \\(\frac{\pi}{2}\\) Radiant (90 Grad) von der positiven x-Achse.

3. **Punkt im zweiten Quadranten:**
   - Kartesische Koordinaten: \\((-1, 1)\\)
   - Polarkoordinaten: \\((\sqrt{2}, \frac{3\pi}{4})\\)
   - Erklärung: Der Punkt ist \\(\sqrt{2}\\) Einheiten vom Ursprung entfernt, in einem Winkel von \\(\frac{3\pi}{4}\\) Radiant (135 Grad) von der positiven x-Achse.

4. **Punkt im dritten Quadranten:**
   - Kartesische Koordinaten: \\((-1, -1)\\)
   - Polarkoordinaten: \\((\sqrt{2}, \frac{5\pi}{4})\\)
   - Erklärung: Der Punkt ist \\(\sqrt{2}\\) Einheiten vom Ursprung entfernt, in einem Winkel von \\(\frac{5\pi}{4}\\) Radiant (225 Grad) von der positiven x-Achse.

5. **Punkt im vierten Quadranten:**
   - Kartesische Koordinaten: \\((1, -1)\\)
   - Polarkoordinaten: \\((\sqrt{2}, \frac{7\pi}{4})\\)
   - Erklärung: Der Punkt ist \\(\sqrt{2}\\) Einheiten vom Ursprung entfernt, in einem Winkel von \\(\frac{7\pi}{4}\\) Radiant (315 Grad) von der positiven x-Achse.

### Umrechnung zwischen kartesischen und Polarkoordinaten

- **Von kartesisch zu polar:**
  \\[
  r = \sqrt{x^2 + y^2}
  \\]
  \\[
  \theta = \arctan\left(\frac{y}{x}\right)
  \\]

- **Von polar zu kartesisch:**
  \\[
  x = r \cdot \cos(\theta)
  \\]
  \\[
  y = r \cdot \sin(\theta)
  \\]

Polarkoordinaten sind besonders nützlich in Situationen mit zirkularer Symmetrie, wie zum Beispiel in physikalischen und technischen Problemen, die Rotation oder Kreisbewegung beinhalten.