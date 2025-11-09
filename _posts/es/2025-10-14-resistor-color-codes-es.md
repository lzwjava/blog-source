---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Lectura de los Códigos de Colores de las Resistencias
translated: true
type: note
---

### Comprender los Códigos de Colores de las Resistencias

Las resistencias son pequeños componentes electrónicos que limitan el flujo de corriente eléctrica, y su valor de resistencia (medido en ohmios, Ω) a menudo se indica mediante bandas de colores en su cuerpo. Estas bandas siguen un sistema de código de colores estandarizado. La mayoría de las resistencias tienen 4, 5 o 6 bandas, pero los tipos de 4 y 5 bandas son los más comunes. Siempre lea las bandas de izquierda a derecha, comenzando con la banda más cercana a un extremo (el "extremo de lectura"). La banda de tolerancia (a menudo dorada o plateada) suele estar en el lado derecho; si no está seguro, gire la resistencia para que cualquier banda metálica quede a la derecha.

#### Tabla del Código de Colores
Cada color representa un dígito (0-9) para las cifras significativas, o un multiplicador (potencia de 10) para escalar el valor. Aquí está el mapeo estándar:

| Color   | Valor del Dígito | Multiplicador (Potencia de 10) |
|---------|------------------|--------------------------------|
| Negro   | 0                | ×10⁰ (1)                      |
| Marrón  | 1                | ×10¹ (10)                     |
| Rojo    | 2                | ×10² (100)                    |
| Naranja | 3                | ×10³ (1,000)                  |
| Amarillo| 4                | ×10⁴ (10,000)                 |
| Verde   | 5                | ×10⁵ (100,000)                |
| Azul    | 6                | ×10⁶ (1,000,000)              |
| Violeta | 7                | ×10⁷ (10,000,000)             |
| Gris    | 8                | ×10⁸ (100,000,000)            |
| Blanco  | 9                | ×10⁹ (1,000,000,000)          |
| Dorado  | -                | ×10⁻¹ (0.1)                   |
| Plateado| -                | ×10⁻² (0.01)                  |

#### Bandas de Tolerancia
La(s) banda(s) final(es) indican la tolerancia (precisión del valor de resistencia):
- Marrón: ±1%
- Rojo: ±2%
- Verde: ±0.5%
- Azul: ±0.25%
- Violeta: ±0.1%
- Gris: ±0.05%
- Dorado: ±5%
- Plateado: ±10%
- Sin banda: ±20%

#### Cómo Leer una Resistencia de 4 Bandas
1. Identifique las primeras dos bandas como los dígitos significativos (ej., marrón-negro = 10).
2. La tercera banda es el multiplicador: multiplique los dígitos por esta potencia de 10 (ej., rojo = ×100, entonces 10 × 100 = 1,000 Ω).
3. La cuarta banda es la tolerancia (ej., dorado = ±5%).

**Ejemplo**: Marrón (1), negro (0), rojo (×100), dorado (±5%) = 10 × 100 = 1,000 Ω ±5% (o 1 kΩ).

#### Cómo Leer una Resistencia de 5 Bandas
Estas ofrecen mayor precisión con un dígito significativo extra.
1. Identifique las primeras tres bandas como dígitos significativos (ej., marrón-negro-rojo = 102).
2. La cuarta banda es el multiplicador (ej., naranja = ×1,000, entonces 102 × 1,000 = 102,000 Ω).
3. La quinta banda es la tolerancia (ej., marrón = ±1%).

**Ejemplo**: Marrón (1), negro (0), rojo (2), naranja (×1,000), marrón (±1%) = 102 × 1,000 = 102,000 Ω ±1% (o 102 kΩ).

#### Notas
- Para resistencias de 6 bandas, las primeras cinco bandas siguen el patrón de 5 bandas, y la sexta indica el coeficiente de temperatura (cómo cambia la resistencia con el calor, ej., marrón = 100 ppm/°C).
- Si las bandas están descoloridas o poco claras, use un multímetro para medir la resistencia real.
- Las resistencias de cero ohmios (jumpers) pueden tener una sola banda negra.

[Cómo Leer los Códigos de Colores de las Resistencias | Arrow.com](https://www.arrow.com/en/research-and-events/articles/resistor-color-code)  
[GUÍA DEL CÓDIGO DE COLORES DE RESISTENCIAS (PDF)](https://neurophysics.ucsd.edu/courses/physics_120/resistorcharts.pdf)