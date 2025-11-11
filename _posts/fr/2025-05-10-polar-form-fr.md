---
audio: false
generated: true
lang: fr
layout: post
title: Système de coordonnées polaires
translated: true
type: note
---

Le système de coordonnées polaires est un système de coordonnées bidimensionnel dans lequel chaque point d'un plan est déterminé par une distance par rapport à un point de référence et un angle par rapport à une direction de référence. Cela contraste avec le système de coordonnées cartésiennes, qui utilise les coordonnées x et y pour définir un point.

En coordonnées polaires, un point est représenté par \\((r, \theta)\\), où :
- \\(r\\) est la distance radiale depuis l'origine (le point de référence).
- \\(\theta\\) est la coordonnée angulaire, généralement mesurée en radians à partir de l'axe des x positifs (la direction de référence).

### Exemples de coordonnées polaires

1. **Point simple :**
   - Coordonnées cartésiennes : \\((1, 0)\\)
   - Coordonnées polaires : \\((1, 0)\\)
   - Explication : Le point est à 1 unité de l'origine le long de l'axe des x positifs.

2. **Point dans le plan :**
   - Coordonnées cartésiennes : \\((0, 1)\\)
   - Coordonnées polaires : \\((1, \frac{\pi}{2})\\)
   - Explication : Le point est à 1 unité de l'origine, à un angle de \\(\frac{\pi}{2}\\) radians (90 degrés) par rapport à l'axe des x positifs.

3. **Point dans le deuxième quadrant :**
   - Coordonnées cartésiennes : \\((-1, 1)\\)
   - Coordonnées polaires : \\((\sqrt{2}, \frac{3\pi}{4})\\)
   - Explication : Le point est à \\(\sqrt{2}\\) unités de l'origine, à un angle de \\(\frac{3\pi}{4}\\) radians (135 degrés) par rapport à l'axe des x positifs.

4. **Point dans le troisième quadrant :**
   - Coordonnées cartésiennes : \\((-1, -1)\\)
   - Coordonnées polaires : \\((\sqrt{2}, \frac{5\pi}{4})\\)
   - Explication : Le point est à \\(\sqrt{2}\\) unités de l'origine, à un angle de \\(\frac{5\pi}{4}\\) radians (225 degrés) par rapport à l'axe des x positifs.

5. **Point dans le quatrième quadrant :**
   - Coordonnées cartésiennes : \\((1, -1)\\)
   - Coordonnées polaires : \\((\sqrt{2}, \frac{7\pi}{4})\\)
   - Explication : Le point est à \\(\sqrt{2}\\) unités de l'origine, à un angle de \\(\frac{7\pi}{4}\\) radians (315 degrés) par rapport à l'axe des x positifs.

### Conversion entre coordonnées cartésiennes et polaires

- **Des coordonnées cartésiennes vers les coordonnées polaires :**
  \\[
  r = \sqrt{x^2 + y^2}
  \\]
  \\[
  \theta = \arctan\left(\frac{y}{x}\right)
  \\]

- **Des coordonnées polaires vers les coordonnées cartésiennes :**
  \\[
  x = r \cdot \cos(\theta)
  \\]
  \\[
  y = r \cdot \sin(\theta)
  \\]

Les coordonnées polaires sont particulièrement utiles dans les situations impliquant une symétrie circulaire, comme dans les problèmes de physique et d'ingénierie impliquant une rotation ou un mouvement circulaire.