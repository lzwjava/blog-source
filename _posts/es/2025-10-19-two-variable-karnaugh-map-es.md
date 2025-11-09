---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Ejemplo de Mapa de Karnaugh de Dos Variables
translated: true
type: note
---

### Ejemplo Simple de Mapa de Karnaugh: Función de 2 Variables

Usemos una función booleana de 2 variables muy básica: f(A, B) = A'B + AB' + AB (suma de minterms m(1, 2, 3)). Esta es la función OR: f = A + B, pero la "descubriremos" usando un K-map.

#### Paso 1: Construir el K-Map
Un K-map de 2 variables es una cuadrícula de 2x2. Filas para A (0, 1), columnas para B (0, 1) en código Gray (ya es simple). Coloca 1s para los minterms:

| A \ B | 0 (B') | 1 (B) |
|-------|--------|-------|
| **0 (A')** | 0 (m0) | 1 (m1) |
| **1 (A)**  | 1 (m2) | 1 (m3) |

#### Paso 2: Agrupar los 1s Adyacentes
Busca los grupos más grandes de 1s (potencias de 2: 1, 2, 4...). Adyacente significa compartir un lado (no en diagonal).

- **Grupo 1**: Columna derecha (m1 y m3)—par vertical. Común: B (A varía, por lo tanto no importa).
- **Grupo 2**: Fila inferior (m2 y m3)—par horizontal. Común: A (B varía).

(La superposición en m3 está bien).

#### Paso 3: Derivar la Expresión Minimizada
Cada grupo da un término:
- Grupo 1: **B**
- Grupo 2: **A**

Minimizada: f = A + B

Esto simplifica de 3 términos (originalmente 9 literales, espera no: 3 términos con 2 literales cada uno) a 2 términos con 1 literal cada uno—¡menos compuertas!

Coincide con la función OR. Para una práctica aún más simple, prueba con todos 1s: se agrupa en solo 1 (verdadero).

[All About Circuits: Karnaugh Maps](https://www.allaboutcircuits.com/textbook/digital/chpt-7/karnaugh-mapping/)