---
audio: false
generated: true
lang: es
layout: post
title: Electrónica Analógica
translated: true
type: note
---

¡Increíble! Aquí tienes un tutorial completo sobre **Parte I: Electrónica Analógica** de *Fundamentals of Electronic Technology (III)*. Lo desglosaré sección por sección con explicaciones, diagramas (donde sea útil) y relevancia en el mundo real.

---

## 🔹 Parte I: Electrónica Analógica

---

### **1. Fundamentos del Análisis de Circuitos**

#### a. **Conceptos y Leyes Básicas de Circuitos**
- **Voltaje (V)**: Diferencia de potencial eléctrico entre dos puntos.
- **Corriente (I)**: Flujo de carga eléctrica; medido en amperios (A).
- **Resistencia (R)**: Oposición a la corriente; medida en ohmios (Ω).
- **Potencia (P)**: Energía utilizada por unidad de tiempo: \\( P = VI \\)

#### ⚡ **Ley de Ohm**
\\[
V = IR
\\]
Simple y crucial. Relaciona voltaje, corriente y resistencia en una resistencia lineal.

#### ⚡ **Leyes de Kirchhoff**
- **LCK (Ley de Corrientes)**: La corriente total que entra a un nodo es igual a la corriente total que sale de él.
  \\[
  \sum I_{entra} = \sum I_{sale}
  \\]
- **LVK (Ley de Voltajes)**: La suma de los voltajes alrededor de un lazo cerrado es cero.
  \\[
  \sum V = 0
  \\]

#### b. **Métodos de Análisis de Circuitos Lineales**
- **Análisis Nodal**: Resuelve para los voltajes de nodo usando LCK.
  - Elige un nodo de referencia (tierra).
  - Escribe las ecuaciones de corriente en cada nodo.
- **Teorema de Superposición**:
  - Para circuitos lineales con múltiples fuentes, analiza una fuente a la vez.
  - Reemplaza otras fuentes de voltaje con cortocircuitos y fuentes de corriente con circuitos abiertos.

#### c. **Circuitos Dinámicos y Análisis Transitorio**
- **Circuitos RC y RL**: Comportamiento transitorio al encenderse/apagarse.
  - Voltaje del capacitor: \\( V(t) = V_0 (1 - e^{-t/RC}) \\)
  - Corriente del inductor: \\( I(t) = I_0 (1 - e^{-t/LR}) \\)
- **Constantes de Tiempo**: RC o L/R; indica qué tan rápido reaccionan los circuitos a los cambios.

---

### **2. Principios de Circuitos Amplificadores**

#### a. **Dispositivos Semiconductores**
- **Diodos**: Permiten la corriente en una sola dirección; se usan en rectificadores.
- **Transistores de Unión Bipolar (BJT)**:
  - Tres terminales: Base, Colector, Emisor.
  - **Modo activo**: Amplifican corriente.
  - **Curvas características**: Muestran la corriente de salida vs. el voltaje colector-emisor.

#### b. **Configuraciones Básicas de Amplificadores**
- **Emisor Común (CE)**:
  - Alta ganancia.
  - Desplazamiento de fase: 180°.
- **Colector Común (CC)** (Seguidor de Emisor):
  - Ganancia unitaria (≈1), pero excelente búfer.
- **Base Común (CB)**:
  - Baja impedancia de entrada, aplicaciones de alta frecuencia.

#### c. **Respuesta en Frecuencia y Estabilidad**
- **Ancho de Banda**: Rango de frecuencias en el que el amplificador funciona bien.
- **Producto Ganancia-Ancho de Banda**: Compensación entre ganancia y velocidad.
- **Estabilidad**: Evitar oscilaciones, a menudo controlado por retroalimentación.

---

### **3. Amplificadores Operacionales (Op-Amps) y Aplicaciones**

#### a. **Características del Op-Amp**
- **Op-Amp Ideal**:
  - Ganancia infinita
  - Impedancia de entrada infinita
  - Impedancia de salida cero
- **Corto Virtual**: \\( V_+ = V_- \\) cuando hay retroalimentación negativa.
- **Abierto Virtual**: Corriente de entrada ≈ 0

#### b. **Circuitos Típicos con Op-Amps**
- **Amplificador Inversor**:
  \\[
  V_{salida} = -\left(\frac{R_f}{R_{entrada}}\right) V_{entrada}
  \\]
- **Amplificador No Inversor**:
  \\[
  V_{salida} = \left(1 + \frac{R_f}{R_1}\right) V_{entrada}
  \\]
- **Integrador/Diferenciador**: Usa un capacitor en la retroalimentación o la entrada.

#### c. **Aplicaciones No Lineales**
- **Comparador**: Compara dos voltajes, genera una salida alta o baja.
- **Disparador Schmitt**: Añade histéresis al comparador para inmunidad al ruido.
- **Generadores de Formas de Onda**: Genera ondas cuadradas, triangulares o sinusoidales usando op-amps y retroalimentación.

---

### **4. Fuentes de Alimentación DC**

#### a. **Circuitos Rectificadores y Filtros**
- **Rectificador de Media Onda**: Usa un diodo.
- **Rectificador de Onda Completa**: Usa cuatro diodos (puente).
- **Filtro**: Usualmente capacitores para suavizar la salida.

#### b. **Reguladores Lineales vs. Conmutados**
- **Regulador Lineal**:
  - Simple, estable, pero ineficiente (pérdida de calor).
  - Ejemplo: 7805 (salida de 5V)
- **Regulador Conmutado**:
  - Usa conmutación de alta velocidad e inductores/capacitores.
  - Alta eficiencia.
  - Tipos: Buck, Boost, Buck-Boost.

---

¿Te gustarían diagramas, problemas de ejemplo o resúmenes para cada tema? También puedo ayudarte con cuestionarios o crear una hoja de estudio si estás repasando.