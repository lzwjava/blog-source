---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Guía de Circuitos Lógicos Combinacionales
translated: true
type: note
---

Esta guía cubre los conceptos clave del capítulo sobre Circuitos Lógicos Combinacionales de *Fundamentals of Electronic Technology (III)*. Los circuitos lógicos combinacionales son sistemas digitales donde la salida depende únicamente de las entradas actuales, sin elementos de memoria (a diferencia de los circuitos secuenciales). Lo desglosaremos en las secciones especificadas: análisis y diseño, módulos comunes, y peligros (hazards) con métodos de eliminación. El enfoque está en la comprensión práctica, con ejemplos y explicaciones paso a paso.

## 1. Análisis y Diseño de Lógica Combinacional

### Análisis
El análisis consiste en determinar el comportamiento de salida de un circuito dado a partir de su descripción a nivel de compuertas.

- **Tablas de Verdad**: La base del análisis. Enumere todas las combinaciones de entrada posibles y calcule las salidas.
  - Para un circuito con *n* entradas, hay 2^n filas.
  - Ejemplo: Analizar un circuito AND-OR de 2 entradas: Salida = (A · B) + (A' · B') (donde ' denota NOT).

    | A | B | A · B | A' · B' | Salida |
    |---|---|-------|---------|--------|
    | 0 | 0 |   0   |    1    |   1    |
    | 0 | 1 |   0   |    0    |   0    |
    | 1 | 0 |   0   |    0    |   0    |
    | 1 | 1 |   1   |    0    |   1    |

    Esto se simplifica a A XOR B (OR exclusivo).

- **Mapas de Karnaugh (K-Maps)**: Herramienta visual para simplificar expresiones booleanas durante el análisis.
  - Trace los minterms (1s) en una cuadrícula; agrupe los 1s adyacentes (potencias de 2) para encontrar los implicantes primos.
  - Se reduce a la forma de Suma de Productos (SOP) o Producto de Sumas (POS).

### Diseño
El diseño parte de una especificación del problema (por ejemplo, una tabla de verdad o una descripción verbal) y construye el circuito.

- **Pasos**:
  1. Derivar la tabla de verdad a partir de las especificaciones.
  2. Escribir la expresión canónica SOP/POS (suma/producto de minterms/maxterms).
  3. Simplificar usando K-Maps o el método de Quine-McCluskey.
  4. Implementar con compuertas (AND, OR, NOT, NAND, NOR).

- **Ejemplo de Diseño**: Diseñar un circuito para un votante mayoritario (salida 1 si al menos dos de las tres entradas A, B, C son 1).
  - Tabla de verdad (parcial):

    | A | B | C | Salida |
    |---|---|---|--------|
    | 0 | 0 | 0 |   0    |
    | 0 | 0 | 1 |   0    |
    | 0 | 1 | 1 |   1    |
    | 1 | 0 | 1 |   1    |
    | 1 | 1 | 0 |   1    |
    | 1 | 1 | 1 |   1    |

  - K-Map (para SOP):
    ```
    CD\AB | 00 | 01 | 11 | 10
    ------|----|----|----|----
    00    | 0  | 0  | 0  | 0
    01    | 0  | 0  | 1  | 0
    11    | 0  | 1  | 1  | 1
    10    | 0  | 1  | 1  | 0
    ```
    (Filas/columnas etiquetadas con código Gray.)

  - Simplificado: F = AB + AC + BC.
  - Implementación con compuertas: Tres compuertas AND para cada término, una compuerta OR.

Consejos: Verifique siempre con simulación o reanalice el circuito final.

## 2. Módulos Comunes

Estos son bloques de construcción estándar para sistemas más grandes, que reducen la complejidad del diseño.

### Codificadores (Encoders)
- Convierten entradas activas a código binario.
- Ejemplo: Codificador de Prioridad de 4 a 2 Líneas (entradas: Y3, Y2, Y1, Y0; salidas: A1, A0; bandera válida V).
  - Tabla de Verdad:

    | Y3 | Y2 | Y1 | Y0 | A1 | A0 | V |
    |----|----|----|----|----|----|---|
    | 0  | 0  | 0  | 1  | 0  | 0  | 1 |
    | 0  | 0  | 1  | X  | 0  | 1  | 1 |
    | 0  | 1  | X  | X  | 1  | 0  | 1 |
    | 1  | X  | X  | X  | 1  | 1  | 1 |
    | 0  | 0  | 0  | 0  | X  | X  | 0 |

  - Lógica: A1 = Y3 + Y2; A0 = Y3 + Y1; V = Y3 + Y2 + Y1 + Y0.
  - Uso: Entrada de teclado a binario.

### Decodificadores (Decoders)
- Opuesto a los codificadores: Entrada binaria a salida one-hot (activa una línea).
- Ejemplo: Decodificador de 2 a 4 (entradas: A1, A0; salidas: D0-D3).
  - Tabla de Verdad:

    | A1 | A0 | D3 | D2 | D1 | D0 |
    |----|----|----|----|----|----|
    | 0  | 0  | 0  | 0  | 0  | 1  |
    | 0  | 1  | 0  | 0  | 1  | 0  |
    | 1  | 0  | 0  | 1  | 0  | 0  |
    | 1  | 1  | 1  | 0  | 0  | 0  |

  - Lógica: D0 = A1' · A0'; D1 = A1' · A0; etc.
  - Uso: Direccionamiento de memoria, controladores de display de 7 segmentos.

### Multiplexores (MUX)
- Seleccionan una de muchas entradas para una sola salida basándose en líneas de selección.
- Ejemplo: MUX de 4 a 1 (entradas: I0-I3; selecciones: S1, S0; salida: Y).
  - Tabla de Verdad:

    | S1 | S0 | Y  |
    |----|----|----|
    | 0  | 0  | I0 |
    | 0  | 1  | I1 |
    | 1  | 0  | I2 |
    | 1  | 1  | I3 |

  - Lógica: Y = (S1' · S0' · I0) + (S1' · S0 · I1) + (S1 · S0' · I2) + (S1 · S0 · I3).
  - Encadenamiento: Construir MUX más grandes (por ejemplo, 8 a 1 a partir de dos 4 a 1).
  - Uso: Enrutamiento de datos, generadores de funciones (implementar cualquier función de n variables con un MUX 2^n a 1).

## 3. Peligros (Hazards) y Métodos de Eliminación

Los peligros son glitches no deseados (salidas incorrectas temporales) debido a diferencias de temporización en los retardos de las compuertas, incluso si la lógica en estado estable es correcta.

### Tipos de Peligros
- **Peligro Estático (Static Hazard)**: La salida debería permanecer constante (0→0 o 1→1) pero tiene un glitch.
  - Estático-1: Se debe a un término de producto faltante en SOP (por ejemplo, transición donde dos términos se superponen insuficientemente).
- **Peligro Dinámico (Dynamic Hazard)**: La salida debería cambiar (0→1 o 1→0) pero oscila múltiples veces.
  - Más complejo, a menudo proviene de múltiples peligros estáticos.

- **Detección**: Usar diagramas de temporización o coberturas de peligro en K-Maps (verificar 1s adyacentes para cambios de una sola variable).

Ejemplo: Circuito SOP F = AB + A'C (peligro estático-1 en A=1, B:0→1, C=1; glitch si el término AB se retrasa).

### Métodos de Eliminación
- **Añadir Términos Redundantes (Coberturas de Peligro)**:
  - En el K-Map, añadir implicantes extra para cubrir transiciones (por ejemplo, añadir AC para el ejemplo: F = AB + A'C + AC).
  - Asegura superposición durante los cambios; aumenta el conteo de compuertas pero elimina los glitches.

- **Usar Implementaciones Libres de Peligros**:
  - Implicantes Primos Esenciales (EPIs) + términos de consenso.
  - Para dinámicos: Asegurar una sola transición por variable.

- **Otras Técnicas**:
  - Retardos balanceados (igualar las rutas de las compuertas, impracticable en VLSI).
  - Soluciones basadas en latch (pero eso es secuencial).
  - Herramientas de simulación para verificación.

Consejos: Los peligros son críticos en diseños de alta velocidad; verifique siempre los cambios de una sola entrada.

## Resumen y Consejos Prácticos
- **Conclusión Clave**: La lógica combinacional se trata de mapear entradas a salidas de manera eficiente. Domine las tablas de verdad y los K-Maps, se usan en todas partes.
- **Práctica**: Diseñe un sumador completo usando MUX; analice un decodificador en busca de peligros.
- **Próximos Pasos**: Pase a la lógica secuencial para elementos de memoria.

Para profundizar, consulte textos estándar como *Digital Design* de Mano.

[Digital Design by M. Morris Mano](https://www.pearson.com/us/higher-education/program/Morris-Mano-Digital-Design-with-an-Introduction-to-the-Verilog-HDL-5th-Edition/PGM110392.html)  
[Fundamentals of Digital Logic with Verilog Design by Brown and Vranesic](https://www.mheducation.com/highered/product/fundamentals-digital-logic-verilog-design-brown-vranesic/M9780073380544.html)