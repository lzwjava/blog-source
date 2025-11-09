---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Ejemplo de Minimización con Mapas de Karnaugh
translated: true
type: note
---

### Ejemplo de Uso del Mapa de Karnaugh: Minimización de una Función Booleana de 3 Variables

Veamos un ejemplo práctico del uso de un K-map para simplificar una expresión booleana. Usaremos una función de 3 variables (A, B, C) donde la salida es 1 para los minterms m(1, 2, 4, 7). Esto significa:

- f(A, B, C) = A'B'C + A'BC' + AB'C' + ABC

El objetivo es minimizar esto en la menor cantidad de términos (y literales) posible, lo que reduce el número de puertas lógicas en un circuito.

#### Paso 1: Construir el K-Map
Un K-map de 3 variables es una cuadrícula de 2x4 (o 4x2, pero usaremos filas para AB y columnas para C). Las filas están etiquetadas en orden de código Gray (00, 01, 11, 10) para garantizar que las celdas adyacentes difieran en solo un bit. Coloca 1s en las celdas correspondientes a los minterms:

| AB \ C | 0     | 1     |
|--------|-------|-------|
| **00** | 0     | 1 (m1) |
| **01** | 1 (m2) | 0     |
| **11** | 0     | 1 (m7) |
| **10** | 1 (m4) | 0     |

(Aquí, m1 = A'B'C, m2 = A'BC', m4 = AB'C', m7 = ABC.)

#### Paso 2: Agrupar los 1s Adyacentes
La clave para la minimización es encontrar los grupos más grandes posibles (rectángulos o cuadrados) de 1s que sean adyacentes (incluyendo los bordes que se envuelven, como un toro). Cada grupo debe tener un tamaño que sea una potencia de 2 (1, 2, 4, 8, etc.). Los grupos pueden superponerse.

- **Grupo 1**: Los dos 1s en la columna izquierda (m2 y m4) forman un par vertical. Comparten A'B'C' espera no—analizando bits: m2 (010) y m4 (100) difieren solo en A y B, pero en código Gray, la fila 01 y 10 son adyacentes. Este grupo cubre el cambio en A, por lo que es B'C' (A es indiferente).
- **Grupo 2**: Los dos 1s en la columna derecha (m1 y m7) forman un par vertical que se envuelve (las filas 00 y 11 no son directamente adyacentes, espera—en realidad, para este mapa, una mejor agrupación: nota que m1 (001) y m2 (010) son adyacentes horizontalmente en la fila 00-01? Espera, corrijamos.

Espera, replanteemos para mayor claridad—en realidad, grupos óptimos para esta función:

- Par horizontal: m1 (fila00 col1) y m2 (fila01 col0)? No, no son adyacentes.
Agrupación estándar para estos minterms:
- ¿Cuádruple? No. Pares:
  - ¿m1 y m2? m1=001, m2=010—difieren en dos bits, no son adyacentes.
  Mejor: m2 (010) y m4 (100)—¿difieren en A y B? 010 y 100 difieren en A (0 a 1) y B (1 a 0), dos bits—no son adyacentes.

Elegí un mal ejemplo—permíteme elegir uno mejor con grupos claros para ilustrar.

**Ejemplo Revisado para Mayor Claridad**: Usemos f(A, B, C) = Σ m(0, 1, 2, 4, 5, 6) = A'B'C' + A'B'C + A'BC' + AB'C' + AB'C + ABC'

K-map:

| AB \ C | 0     | 1     |
|--------|-------|-------|
| **00** | 1 (m0) | 1 (m1) |
| **01** | 1 (m2) | 0 (m3) |
| **11** | 1 (m6) | 0 (m7) |
| **10** | 1 (m4) | 1 (m5) |

Minterms: 0(000),1(001),2(010),4(100),5(101),6(110)—sí m3(011)=0, m7(111)=0.

Así que la tabla:

| AB \ C | 0     | 1     |
|--------|-------|-------|
| **00** | 1     | 1     |
| **01** | 1     | 0     |
| **11** | 1     | 0     |
| **10** | 1     | 1     |

#### Paso 3: Identificar los Grupos
Ahora, agrupa los 1s:

- **Grupo grande (4 unos)**: Toda la columna izquierda (C=0): m0, m2, m6, m4. Estas son todas las celdas donde C=0, y AB varía—todas adyacentes en una columna (se envuelve para las filas). Esto cubre **C'** (ya que C es 0, A y B son indiferentes).
- **Grupo de par (2 unos)**: Parte superior derecha (m0 y m1? m0 col0, m1 col1—par horizontal en la fila 00: A'B' (C indiferente).
- ¿Pero m1 (001) no está cubierto todavía? Espera, fila superior: m0 y m1 son adyacentes horizontalmente, cubriendo A'B' (C varía).
- También, parte inferior derecha m5 (101 col1 fila10)—pero para cubrir m1 y m5? Están en col1, filas 00 y 10, que son adyacentes (se envuelven), así que par vertical en col1: m1 y m5, cubriendo AC (espera, bits: 001 y 101 = A indiferente, B=0, C=1? 001 B=0 C=1, 101 A=1 B=0 C=1—sí B'C.

Para minimizar, elegimos grupos de cobertura no superpuestos o mínimos que cubran todos los 1s con los tamaños más grandes.

Óptimo:
- Grupo 1: 4 celdas verticales en col0: cubre C' (todos los 1s allí: m0,m2,m4,m6 → término: C')
- Grupo 2: 2 celdas horizontales en fila00: m0 y m1 → A'B'
- Grupo 3: 2 celdas verticales que se envuelven en col1 filas10 y 00? Espera, las filas 00 y 10 son adyacentes para col1: m1(001) y m5(101) → difieren solo en A, así que B'C (A indiferente).

m5 está cubierto, m1 cubierto.

Nota: m0 está en el grupo1 y grupo2, pero eso está bien—se permiten superposiciones.

#### Paso 4: Derivar la Expresión Minimizada
Cada grupo se convierte en un término de producto (AND de los literales comunes):
- Grupo 1 (C'): **C'**
- Grupo 2 (A'B'): **A' B'**
- Grupo 3 (B' C): **B' C**

Entonces, SOP (Suma de Productos) minimizada: f = C' + A'B' + B'C

Verifica: Esto tiene 3 términos (vs 6 originales), menos literales (4 vs 12), circuito más simple (básicamente 3 puertas AND/OR).

Puedes trazar esto en una tabla de verdad para confirmar que coincide con los 1s originales.

#### ¿Por Qué Esto Minimiza?
- **Regla de adyacencia**: Grupos solo donde las variables cambian en un bit, asegurando que el término ignore esa variable (indiferente = - en el mapa).
- **Más grande primero**: Grupos más grandes = menos variables en el término = más simple.
- **Cubrir todos los 1s**: Ningún 1 se queda fuera; los 0s deben permanecer en 0 (no los agrupes).
- Para más variables (K-map de 4 var es 4x4), mismo proceso, pero más difícil visualmente.

Este ejemplo muestra cómo los K-maps convierten una suma-de-minterms en una forma compacta rápidamente sin manipulación algebraica. Para 4+ vars, usa software, pero practicar con ejemplos de 2-3 vars desarrolla intuición.

[Digital Logic Design Basics](https://www.allaboutcircuits.com/textbook/digital/chpt-7/karnaugh-mapping/)