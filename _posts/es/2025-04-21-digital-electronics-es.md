---
audio: false
generated: true
lang: es
layout: post
title: Electrónica Digital
translated: true
type: note
---

¡Por supuesto! Aquí tienes un tutorial completo y accesible para la **Parte II: Electrónica Digital** de *Fundamentals of Electronic Technology (III)*. Esta parte se centra en cómo los sistemas digitales representan, procesan y manipulan información binaria.

---

## 🔹 Parte II: Electrónica Digital

---

### **5. Fundamentos de Circuitos Digitales**

#### a. **Sistemas Numéricos y Códigos**
- **Binario (Base-2)**: Utiliza los dígitos 0 y 1. Es el más fundamental para los sistemas digitales.
- **Octal (Base-8) y Hexadecimal (Base-16)**: Formas abreviadas para grupos binarios (3 o 4 bits).
- **BCD (Decimal Codificado en Binario)**: Cada dígito decimal se representa por separado en binario (0000–1001).
- **Código Gray**: Solo un bit cambia a la vez entre valores sucesivos; se utiliza en codificadores de posición.

#### b. **Álgebra de Boole y Compuertas Lógicas**
- **Operaciones Booleanas**:
  - **AND**: A·B = 1 si ambos son 1
  - **OR**: A + B = 1 si alguno es 1
  - **NOT**: 𝑨̅ = inverso de A
- **Compuertas Derivadas**:
  - **NAND**, **NOR**, **XOR**, **XNOR**
- **Lógica Combinacional**: La salida depende únicamente de las entradas actuales.
  - Utiliza **tablas de verdad** y **Mapas de Karnaugh (K-Maps)** para la simplificación.

#### c. **Circuitos Integrados TTL y CMOS**
- **TTL (Lógica Transistor-Transistor)**:
  - Más rápida pero consume más potencia.
  - Nivel lógico 1: ~5V; nivel 0: ~0V.
- **CMOS (Semiconductor de Óxido de Metal Complementario)**:
  - Bajo consumo de energía, velocidad más lenta, muy común en los CI modernos.
  - Compatible con un amplio rango de voltajes.

---

### **6. Circuitos de Lógica Combinacional**

#### a. **Análisis y Diseño**
- Comienza con una **tabla de verdad**.
- Deriva una **expresión booleana**.
- Simplifícala (usando leyes booleanas o K-Map).
- Dibuja el **circuito lógico**.

#### b. **Módulos Comunes**
- **Codificadores (Encoders)**: Convierten 2ⁿ líneas de entrada en una salida de n bits (ej., codificador de 8 a 3).
- **Decodificadores (Decoders)**: Lo opuesto a un codificador; se utilizan en la decodificación de direcciones de memoria.
- **Multiplexores (MUX)**: Seleccionan una de muchas entradas.
  - Ej., MUX 4 a 1: 2 líneas de selección, 4 entradas → 1 salida.
- **Demultiplexores (DEMUX)**: Una entrada se dirige a una de muchas salidas.

#### c. **Riesgos (Hazards)**
- **Riesgo Estático (Static Hazard)**: La salida cambia momentáneamente debido a retardos en las compuertas.
- **Riesgo Dinámico (Dynamic Hazard)**: Múltiples glitches en la salida debido a desajustes de temporización.
- **Eliminación**: Utiliza lógica redundante o diseños síncronos.

---

### **7. Circuitos de Lógica Secuencial**

#### a. **Biestables (Flip-Flops)**
- **Biestable RS (RS Flip-Flop)**: Biestable de Puesta a Cero (Reset) y Puesta a Uno (Set); memoria simple.
- **Biestable D (D Flip-Flop)**: Biestable de Datos o Retardo (Delay); el más común.
- **Biestable JK (JK Flip-Flop)**: Versátil; evita el estado inválido del RS.
- **Biestable T (T Flip-Flop)**: Conmuta con el reloj; se utiliza en contadores.

#### b. **Contadores y Registros de Desplazamiento**
- **Contadores**:
  - **Asíncronos (Ripple)**: El reloj se pasa secuencialmente; más lentos.
  - **Síncronos**: Todos los FFs se sincronizan juntos; más rápidos.
  - Tipos: Ascendente (Up), Descendente (Down), Ascendente/Descendente (Up/Down).
- **Registros de Desplazamiento (Shift Registers)**:
  - Almacenan y desplazan bits en serie o en paralelo.
  - Tipos: SISO, SIPO, PISO, PIPO.

#### c. **Análisis de Circuitos Secuenciales**
- **Tablas/Diagramas de Estado**: Muestran las transiciones entre estados.
- Utiliza tablas de excitación de FF para analizar y diseñar.
- Los circuitos síncronos son más fáciles de controlar y depurar que los asíncronos.

---

### **8. Dispositivos Lógicos Programables (PLDs)**

#### a. **Tipos de PLDs**
- **PAL (Programmable Array Logic)**: OR fijo, AND programable.
- **GAL (Generic Array Logic)**: PAL reprogramable.
- **FPGA (Field Programmable Gate Array)**:
  - Altamente configurable.
  - Miles/millones de bloques lógicos.
  - Se utiliza en sistemas complejos como procesamiento de señales digitales, procesamiento de video, etc.

#### b. **Introducción a HDL (VHDL/Verilog)**
- **HDL (Hardware Description Language)**:
  - VHDL: Verboso y fuertemente tipado.
  - Verilog: Sintaxis compacta y similar a C.
- Se utiliza para modelar sistemas digitales en varios niveles (compuerta, transferencia de registros, comportamiento).

#### c. **Ejemplos de Diseño de Sistemas Lógicos**
- Ejemplo 1: Contador binario de 4 bits en Verilog.
- Ejemplo 2: Controlador simple de semáforo con FSM (Máquina de Estados Finita).
- Ejemplo 3: ALU (Unidad Aritmético Lógica) con operaciones básicas.

---

¿Te gustarían diagramas, tablas de verdad o fragmentos de código (por ejemplo, en Verilog o VHDL)? También puedo darte problemas de práctica, hojas de referencia o cuestionarios para repasar. ¡Dime qué tan profundo quieres llegar