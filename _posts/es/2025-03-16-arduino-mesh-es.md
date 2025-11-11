---
audio: false
generated: true
lang: es
layout: post
title: Verificación del Análisis de Mallas con Arduino
translated: true
type: note
---

Verificar el Análisis de Mallas con un Arduino implica construir un circuito con múltiples bucles, aplicar el Análisis de Mallas teóricamente para predecir las corrientes, y luego usar el Arduino para medir los voltajes a través de las resistencias para calcular las corrientes reales y compararlas. El Análisis de Mallas es un método en la teoría de circuitos donde se asignan corrientes de bucle a cada bucle independiente y se usa la Ley de Voltaje de Kirchhoff (LVK) para establecer ecuaciones. El Arduino te ayudará a medir el comportamiento en el mundo real para confirmar tus cálculos.

A continuación, te guiaré a través del diseño de un circuito simple de dos mallas, realizando el Análisis de Mallas manualmente y usando un Arduino para verificar los resultados midiendo voltajes e infiriendo corrientes (dado que el Arduino no puede medir corriente directamente, usaremos la Ley de Ohm: \\( I = V/R \\)).

---

### **Paso 1: Diseñar un Circuito de Dos Mallas**

#### **Descripción del Circuito**
- **Componentes:**
  - Arduino (por ejemplo, Uno)
  - 3 resistencias (por ejemplo, R1 = 330Ω, R2 = 470Ω, R3 = 680Ω)
  - Protoboard y cables jumpers
  - Fuente de alimentación (pin de 5V del Arduino)
- **Cableado:**
  - Conecta 5V al Nodo A.
  - Desde el Nodo A, conecta R1 al Nodo B.
  - Desde el Nodo B, conecta R2 al Nodo C (GND).
  - Desde el Nodo A, conecta R3 al Nodo C (GND).
- **Topología:**
  - Malla 1: 5V → R1 → R2 → GND (bucle izquierdo).
  - Malla 2: 5V → R3 → GND (bucle derecho).
  - R1 está solo en la Malla 1, R3 está solo en la Malla 2, y R2 es compartida entre ambas mallas.
- **Puntos de Medición:**
  - A0: Voltaje a través de R1 (Nodo A a Nodo B).
  - A1: Voltaje a través de R2 (Nodo B a Nodo C).
  - A2: Voltaje a través de R3 (Nodo A a Nodo C).

#### **Concepto del Esquemático**
```
5V ---- Nodo A ---- R1 ---- Nodo B ---- R2 ---- Nodo C (GND)
       |                        |
       +--------- R3 -----------+
```

---

### **Paso 2: Realizar el Análisis de Mallas Teóricamente**

#### **Definir las Corrientes de Malla**
- \\( I_1 \\): Corriente en la Malla 1 (en sentido horario a través de 5V, R1, R2, GND).
- \\( I_2 \\): Corriente en la Malla 2 (en sentido horario a través de 5V, R3, GND).

#### **Aplicar LVK a Cada Malla**
1. **Malla 1 (5V → R1 → R2 → GND):**
   - Fuente de voltaje: +5V (yendo desde GND a 5V en la dirección del bucle).
   - Caída de voltaje en R1: \\( -R1 \cdot I_1 \\).
   - Caída de voltaje en R2: \\( -R2 \cdot (I_1 - I_2) \\) (la corriente a través de R2 es \\( I_1 - I_2 \\)).
   - Ecuación: \\( 5 - R1 \cdot I_1 - R2 \cdot (I_1 - I_2) = 0 \\).

2. **Malla 2 (5V → R3 → GND):**
   - Fuente de voltaje: +5V.
   - Caída de voltaje en R3: \\( -R3 \cdot I_2 \\).
   - Caída de voltaje en R2 (dirección opuesta): \\( +R2 \cdot (I_1 - I_2) \\) (la corriente a través de R2 es \\( I_1 - I_2 \\)).
   - Ecuación: \\( 5 - R3 \cdot I_2 + R2 \cdot (I_1 - I_2) = 0 \\).

#### **Sustituir Valores**
- R1 = 330Ω, R2 = 470Ω, R3 = 680Ω.
- Malla 1: \\( 5 - 330 I_1 - 470 (I_1 - I_2) = 0 \\)
  - Simplificar: \\( 5 - 330 I_1 - 470 I_1 + 470 I_2 = 0 \\)
  - \\( 5 - 800 I_1 + 470 I_2 = 0 \\) → (1)
- Malla 2: \\( 5 - 680 I_2 + 470 (I_1 - I_2) = 0 \\)
  - Simplificar: \\( 5 + 470 I_1 - 680 I_2 - 470 I_2 = 0 \\)
  - \\( 5 + 470 I_1 - 1150 I_2 = 0 \\) → (2)

#### **Resolver las Ecuaciones**
- De (1): \\( 5 = 800 I_1 - 470 I_2 \\) → \\( I_1 = \frac{5 + 470 I_2}{800} \\).
- Sustituir en (2): \\( 5 + 470 \left( \frac{5 + 470 I_2}{800} \right) - 1150 I_2 = 0 \\).
- Multiplicar por 800 para eliminar la fracción:
  - \\( 4000 + 470 (5 + 470 I_2) - 1150 \cdot 800 I_2 = 0 \\)
  - \\( 4000 + 2350 + 220900 I_2 - 920000 I_2 = 0 \\)
  - \\( 6350 - 699100 I_2 = 0 \\)
  - \\( I_2 = \frac{6350}{699100} \approx 0.00908 \, \text{A} = 9.08 \, \text{mA} \\).
- Sustituir hacia atrás: \\( I_1 = \frac{5 + 470 \cdot 0.00908}{800} = \frac{5 + 4.2676}{800} \approx 0.01158 \, \text{A} = 11.58 \, \text{mA} \\).

#### **Calcular Voltajes**
- \\( V_{R1} = R1 \cdot I_1 = 330 \cdot 0.01158 \approx 3.82 \, \text{V} \\).
- \\( V_{R2} = R2 \cdot (I_1 - I_2) = 470 \cdot (0.01158 - 0.00908) \approx 1.18 \, \text{V} \\).
- \\( V_{R3} = R3 \cdot I_2 = 680 \cdot 0.00908 \approx 6.17 \, \text{V} \\) (pero limitado a 5V debido a la fuente).

---

### **Paso 3: Verificar con Arduino**

#### **Código de Arduino**
```cpp
void setup() {
  Serial.begin(9600); // Iniciar comunicación serial
}

void loop() {
  // Leer voltajes (0-1023 se mapea a 0-5V)
  int sensorValueR1 = analogRead(A0); // A través de R1
  int sensorValueR2 = analogRead(A1); // A través de R2
  int sensorValueR3 = analogRead(A2); // A través de R3

  // Convertir a voltaje
  float VR1 = sensorValueR1 * (5.0 / 1023.0);
  float VR2 = sensorValueR2 * (5.0 / 1023.0);
  float VR3 = sensorValueR3 * (5.0 / 1023.0);

  // Valores de las resistencias
  float R1 = 330.0;
  float R2 = 470.0;
  float R3 = 680.0;

  // Calcular corrientes (I = V/R)
  float I1 = VR1 / R1;              // Corriente de Malla 1 a través de R1
  float I2 = VR3 / R3;              // Corriente de Malla 2 a través de R3
  float IR2 = VR2 / R2;             // Corriente a través de R2 (I1 - I2)

  // Mostrar resultados
  Serial.println("Valores Medidos:");
  Serial.print("VR1 (V): "); Serial.println(VR1);
  Serial.print("VR2 (V): "); Serial.println(VR2);
  Serial.print("VR3 (V): "); Serial.println(VR3);
  Serial.print("I1 (mA): "); Serial.println(I1 * 1000);
  Serial.print("I2 (mA): "); Serial.println(I2 * 1000);
  Serial.print("I1 - I2 (mA): "); Serial.println((I1 - I2) * 1000);
  Serial.println("---");

  delay(2000); // Esperar 2 segundos
}
```

#### **Notas de Cableado**
- Conecta A0 entre el Nodo A (5V) y el Nodo B.
- Conecta A1 entre el Nodo B y el Nodo C (GND).
- Conecta A2 entre el Nodo A (5V) y el Nodo C (GND).
- Asegúrate de que todos los tierras sean comunes con el GND del Arduino.

---

### **Paso 4: Comparar Resultados**

#### **Esperado vs. Medido**
- **Teórico (del Análisis de Mallas):**
  - \\( I_1 \approx 11.58 \, \text{mA} \\)
  - \\( I_2 \approx 9.08 \, \text{mA} \\)
  - \\( I_1 - I_2 \approx 2.50 \, \text{mA} \\)
  - \\( V_{R1} \approx 3.82 \, \text{V} \\), \\( V_{R2} \approx 1.18 \, \text{V} \\), \\( V_{R3} \approx 5 \, \text{V} \\) (limitado).
- **Medido:** Abre el Monitor Serie (9600 baudios) y compara la salida del Arduino con estos valores.

#### **Verificación**
- Comprueba si \\( V_{R1} + V_{R2} \approx 5V \\) (bucle de la Malla 1).
- Comprueba si \\( V_{R3} \approx 5V \\) (bucle de la Malla 2).
- Confirma que \\( I_1 - I_2 \\) coincida con la corriente a través de R2.

---

### **Consejos y Solución de Problemas**
- **Precisión:** El ADC del Arduino tiene una resolución de ~4.9mV, y las tolerancias de las resistencias pueden causar ligeras desviaciones. Usa un multímetro para una validación precisa.
- **Ajustes:** Si los voltajes exceden 5V (poco probable aquí), usa un divisor de voltaje para reducirlos.
- **Extensiones:** Añade más mallas o componentes para mayor complejidad, pero ten en cuenta los límites de pines (A0–A5).

Esta configuración confirma el Análisis de Mallas al alinear las corrientes teóricas con las medidas. ¡Avísame si necesitas ayuda para refinar el circuito, depurar o añadir más mallas!