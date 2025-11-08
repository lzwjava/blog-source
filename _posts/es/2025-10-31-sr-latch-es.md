---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Comprensión del Biestable SR
translated: true
type: note
---

### ¿Qué es un SR Latch?
Un **SR Latch** (Set-Reset Latch) es un bloque fundamental en la electrónica digital y la arquitectura de computadoras. Es un tipo de **flip-flop** que almacena un solo bit de información (0 o 1) y lo "recuerda" hasta que es cambiado explícitamente por señales de entrada. Las siglas "SR" significan **Set** (para forzar la salida a 1) y **Reset** (para forzar la salida a 0).

Un SR Latch básico se construye típicamente usando dos puertas **NOR** (o puertas NAND en una variante) acopladas en cruz. Aquí hay un diagrama textual simple de la versión basada en NOR:

```
   S ───┐
        │ NOR1 ── Q
        │    │
   R ───┘    │
             │
             └─ NOR2 ── Q' (complemento de Q)
                  │
                  └────── realimentación a NOR1
```

- **S** (Set): Cuando está en alto (1), establece Q a 1.
- **R** (Reset): Cuando está en alto (1), establece Q a 0.
- **Q**: La salida almacenada (la "memoria").
- El bucle de realimentación entre las puertas hace que el circuito "mantenga" el estado incluso después de que S y R vuelvan a 0.

### ¿Qué Significa "Latch" Aquí?
El término **latch** se refiere a la capacidad del circuito para **mantener (o "engancharse a") un estado estable** en el tiempo, sin necesidad de una entrada continua de energía para mantenerlo. Es como un interruptor que permanece en su posición después de que lo accionas—hasta que lo accionas de nuevo.

- **No solo abstracto**: Si bien "latch" es una idea conceptual en el diseño de lógica digital (una abstracción para el comportamiento de memoria), se implementa como un **circuito eléctrico real**. Puedes construirlo con componentes físicos como transistores o puertas lógicas en un chip (por ejemplo, en CIs como la serie 7400).
  
- **Lógica vs. Circuito**: ¡Es ambas cosas!
  - **Configuración lógica**: En teoría, es un modelo de lógica booleana donde las salidas dependen de las entradas y la realimentación (por ejemplo, Q = ¬(S ∨ ¬Q) en la versión NOR).
  - **Circuito eléctrico**: En la práctica, es hardware cableado que opera en niveles de voltaje (por ejemplo, lógica de 5V). Las puertas son alimentadas por electricidad y las señales se propagan como corrientes/voltajes.

### ¿Es un Concepto Abstracto?
Sí, parcialmente—**latch** es un **modelo abstracto** en las ciencias de la computación y el diseño digital, que representa la forma más simple de memoria biestable (dos estados estables). Pero está fundamentado en la física: el circuito explota la histéresis electrónica (realimentación) para almacenar el estado. Sin el circuito físico, la abstracción no funcionaría.

Si lo estás simulando o estudiando:
- Usa herramientas como Logisim o Tinkercad para un circuito virtual.
- Tabla de verdad para el SR Latch (versión NOR):

| S | R | Q (siguiente) | Q' (siguiente) | Descripción     |
|---|----|---------------|----------------|-----------------|
| 0 | 0 | Q (previo)    | Q' (previo)    | Mantener (latch)|
| 0 | 1 | 0             | 1              | Reset           |
| 1 | 0 | 1             | 0              | Set             |
| 1 | 1 | ?             | ?              | Inválido (carrera) |

¡Este comportamiento de "mantenimiento" cuando S=R=0 es lo que lo convierte en un latch—es memoria!

Para análisis más profundos, consulta recursos como "Digital Design" de Morris Mano. Si tienes en mente un diagrama o simulación específica, ¡comparte más detalles!