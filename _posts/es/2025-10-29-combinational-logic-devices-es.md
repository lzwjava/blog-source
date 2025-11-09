---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Descripción General de Dispositivos de Lógica Combinacional
translated: true
type: note
---

### Resumen
El video de "The Learning Circuit" explica los dispositivos de lógica combinacional, que generan salidas basadas únicamente en las entradas actuales (sin memoria de estados pasados). Cubre cuatro tipos clave: multiplexores (MUX), demultiplexores (DEMUX), codificadores y decodificadores. Estos son esenciales para el enrutamiento de señales, la compresión/expansión de datos y el control digital en electrónica.

### Multiplexores (MUX)
- **Propósito**: Como una centralita digital—selecciona una de muchas entradas para enviarla a una única salida, controlado por líneas de selección.
- **Ejemplo Básico (74LS157 Quad 2-to-1 MUX)**:
  - 4 canales, cada uno con entradas A y B, pin de selección (S) y pin de habilitación (E).
  - S en alto: Selecciona las entradas A; S en bajo: Selecciona las entradas B.
  - E en bajo: Habilita la salida; E en alto: Deshabilita (las salidas se ponen en bajo).
- **Ejemplos Mayores**:
  - MUX 4-to-1: 2 líneas de selección eligen entre 4 entradas.
  - MUX 8-to-1: 3 líneas de selección; solo una entrada pasa a través.
- **Consejo**: La forma general es \\(2^n\\)-to-1, donde \\(n\\) es el número de líneas de selección.

### Demultiplexores (DEMUX)
- **Propósito**: Opuesto al MUX—enruta una entrada a una de muchas salidas, basado en líneas de selección.
- **Ejemplo Básico (DEMUX 1-to-2)**:
  - Una línea de selección (S): S en bajo → entrada a Y0; S en alto → entrada a Y1.
- **Regla General**: \\(1\\)-to-\\(2^n\\) salidas, coincidiendo con las líneas de selección del MUX (ej., 2 selecciones → 4 salidas).

### Codificadores
- **Propósito**: Comprime múltiples entradas en una salida codificada (ej., binaria).
- **Codificador Binario Básico**:
  - Ejemplo: 4 entradas → salida binaria de 2 bits (ej., entrada 3 activa → salida 11).
  - Problema: Múltiples entradas activas pueden causar conflictos (salida ambigua).
- **Codificador de Prioridad** (Soluciona Conflictos):
  - Asigna prioridad (la más alta anula a las demás).
  - Ejemplo (8 entradas, activo en bajo): Entrada 7 (la más alta) activa → salida 111, ignora las entradas más bajas.
  - Sin entradas activas → salida 000.

### Decodificadores
- **Propósito**: Expande una entrada codificada en múltiples salidas (ej., activa líneas específicas).
- **Decodificador Binario Básico**:
  - Como un DEMUX: La entrada binaria selecciona una salida (ej., entrada de 2 bits 10 → activa la salida 2).
- **Decodificador BCD a 7 Segmentos**:
  - Entrada BCD de 4 bits (0–9) → Controla 7 segmentos LED para mostrar el dígito.
  - Ejemplos: "0" enciende 6 segmentos; "1" enciende 2 (barras del lado derecho).
- **Decodificador BCD a Decimal**:
  - Entrada de 4 bits → Activa una de 10 salidas (para los dígitos 0–9).

### Puntos Clave
- **MUX/DEMUX**: Enrutadores de datos (directores de tráfico).
- **Codificadores**: Más entradas que salidas (compresión de datos, como comprimir).
- **Decodificadores**: Más salidas que entradas (expansión de datos, como descomprimir).
- Todos son "combinacionales"—la salida cambia instantáneamente con las entradas, sin relojes ni almacenamiento.

[Cómo Funcionan los Dispositivos de Lógica Combinacional - The Learning Circuit](https://www.youtube.com/watch?v=gsmB7J72Tgc)