---
audio: false
generated: true
lang: es
layout: post
title: Las Leyes de Kirchhoff con Arduino
translated: true
type: note
---

Utilizar un Arduino para verificar las Leyes de Kirchhoff—específicamente la Ley de Corrientes de Kirchhoff (KCL) y la Ley de Voltajes de Kirchhoff (KVL)—es una excelente manera de combinar la teoría de la electrónica con la experimentación práctica. KCL establece que la corriente total que entra en un nodo es igual a la corriente total que sale del mismo, mientras que KVL establece que la suma de las caídas de voltaje alrededor de un bucle cerrado es igual al voltaje suministrado. A continuación, se explica cómo puedes diseñar circuitos simples y usar un Arduino para medir corrientes y voltajes para confirmar estas leyes.

Dado que Arduino no puede medir corriente directamente, la inferiremos midiendo el voltaje a través de resistencias (usando la Ley de Ohm: \\( I = V/R \\)), y puede medir voltaje a través de sus pines analógicos (rango de 0–5V). A continuación, describiré dos experimentos—uno para KCL y otro para KVL—con instrucciones paso a paso, cableado y código.

---

### **Experimento 1: Verificación de la Ley de Corrientes de Kirchhoff (KCL)**

#### **Objetivo**
Demostrar que la corriente que entra en un nodo es igual a la corriente que sale del mismo.

#### **Configuración del Circuito**
- **Componentes:**
  - Arduino (ej., Uno)
  - 3 resistencias (ej., R1 = 330Ω, R2 = 470Ω, R3 = 680Ω)
  - Protoboard y cables jumpers
  - Fuente de alimentación de 5V (pin 5V de Arduino)
- **Cableado:**
  - Conecta el pin 5V de Arduino a un nodo (llámalo Nodo A).
  - Desde el Nodo A, conecta R1 a GND (rama 1).
  - Desde el Nodo A, conecta R2 a GND (rama 2, en paralelo con R1).
  - Desde el Nodo A, conecta R3 a GND (rama 3, en paralelo con R1 y R2).
  - Usa los pines analógicos de Arduino para medir el voltaje en cada resistencia:
    - A0 a través de R1 (una sonda en el Nodo A, la otra en GND).
    - A1 a través de R2.
    - A2 a través de R3.
- **Nota:** GND es el punto de referencia común.

#### **Teoría**
- La corriente total desde 5V al Nodo A (\\( I_{in} \\)) se divide en \\( I_1 \\), \\( I_2 \\) e \\( I_3 \\) a través de R1, R2 y R3.
- KCL: \\( I_{in} = I_1 + I_2 + I_3 \\).
- Mide el voltaje en cada resistencia, luego calcula la corriente: \\( I = V/R \\).

#### **Código de Arduino**
```cpp
void setup() {
  Serial.begin(9600); // Iniciar comunicación serial
}

void loop() {
  // Leer voltajes (0-1023 se mapea a 0-5V)
  int sensorValue1 = analogRead(A0); // Voltaje a través de R1
  int sensorValue2 = analogRead(A1); // Voltaje a través de R2
  int sensorValue3 = analogRead(A2); // Voltaje a través de R3

  // Convertir a voltaje (referencia 5V, ADC de 10 bits)
  float V1 = sensorValue1 * (5.0 / 1023.0);
  float V2 = sensorValue2 * (5.0 / 1023.0);
  float V3 = sensorValue3 * (5.0 / 1023.0);

  // Valores de las resistencias (en ohmios)
  float R1 = 330.0;
  float R2 = 470.0;
  float R3 = 680.0;

  // Calcular corrientes (I = V/R)
  float I1 = V1 / R1;
  float I2 = V2 / R2;
  float I3 = V3 / R3;

  // Corriente total que entra al nodo (asumiendo Vfuente = 5V)
  float totalResistance = 1.0 / ((1.0/R1) + (1.0/R2) + (1.0/R3)); // Paralelo
  float Iin = 5.0 / totalResistance;

  // Mostrar resultados
  Serial.print("I1 (mA): "); Serial.println(I1 * 1000);
  Serial.print("I2 (mA): "); Serial.println(I2 * 1000);
  Serial.print("I3 (mA): "); Serial.println(I3 * 1000);
  Serial.print("Iin (mA): "); Serial.println(Iin * 1000);
  Serial.print("Suma de I1+I2+I3 (mA): "); Serial.println((I1 + I2 + I3) * 1000);
  Serial.println("---");

  delay(2000); // Esperar 2 segundos
}
```

#### **Verificación**
- Abre el Monitor Serie (Ctrl+Shift+M en Arduino IDE, configurado a 9600 baudios).
- Compara \\( I_{in} \\) (calculada a partir de la resistencia total) con \\( I_1 + I_2 + I_3 \\). Deberían ser aproximadamente iguales, verificando KCL.
- Pequeñas discrepancias pueden surgir por tolerancias de las resistencias o la precisión del ADC de Arduino.

---

### **Experimento 2: Verificación de la Ley de Voltajes de Kirchhoff (KVL)**

#### **Objetivo**
Mostrar que la suma de las caídas de voltaje alrededor de un bucle cerrado es igual al voltaje de alimentación.

#### **Configuración del Circuito**
- **Componentes:**
  - Arduino
  - 2 resistencias (ej., R1 = 330Ω, R2 = 470Ω)
  - Protoboard y cables jumpers
  - Fuente de alimentación de 5V (pin 5V de Arduino)
- **Cableado:**
  - Conecta 5V a R1.
  - Conecta R1 a R2.
  - Conecta R2 a GND.
  - Mide los voltajes:
    - A0 a través de todo el bucle (5V a GND) para confirmar el voltaje de alimentación.
    - A1 a través de R1 (5V a la unión de R1 y R2).
    - A2 a través de R2 (unión a GND).
- **Nota:** Usa una configuración de divisor de voltaje; asegúrate de que los voltajes no excedan 5V (límite de Arduino).

#### **Teoría**
- KVL: \\( V_{fuente} = V_{R1} + V_{R2} \\).
- Mide cada caída de voltaje y comprueba si suman el voltaje de fuente (5V).

#### **Código de Arduino**
```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  // Leer voltajes
  int sensorValueSource = analogRead(A0); // A través de 5V a GND
  int sensorValueR1 = analogRead(A1);     // A través de R1
  int sensorValueR2 = analogRead(A2);     // A través de R2

  // Convertir a voltaje
  float Vsource = sensorValueSource * (5.0 / 1023.0);
  float VR1 = sensorValueR1 * (5.0 / 1023.0);
  float VR2 = sensorValueR2 * (5.0 / 1023.0);

  // Mostrar resultados
  Serial.print("Vfuente (V): "); Serial.println(Vsource);
  Serial.print("VR1 (V): "); Serial.println(VR1);
  Serial.print("VR2 (V): "); Serial.println(VR2);
  Serial.print("VR1 + VR2 (V): "); Serial.println(VR1 + VR2);
  Serial.println("---");

  delay(2000);
}
```

#### **Verificación**
- En el Monitor Serie, comprueba que \\( V_{fuente} \approx V_{R1} + V_{R2} \\).
- Para R1 = 330Ω y R2 = 470Ω en serie, espera \\( V_{R1} \approx 2.1V \\) y \\( V_{R2} \approx 2.9V \\) (basado en el divisor de voltaje: \\( V_{R1} = 5 \cdot \frac{R1}{R1+R2} \\)), sumando ~5V.

---

### **Consejos y Consideraciones**
- **Precisión:** El ADC de 10 bits de Arduino (0–1023) tiene una resolución de ~4.9mV, así que espera errores menores. Usa un multímetro para verificar si es necesario.
- **Seguridad:** Mantén los voltajes por debajo de 5V y las corrientes bajas para evitar dañar el Arduino.
- **Escalado:** Para circuitos más complejos, añade más resistencias o usa sensores externos (ej., INA219 para medición directa de corriente).
- **Depuración:** Si los resultados no coinciden, verifica los valores de las resistencias, las conexiones y la consistencia de GND.

Estos experimentos simplifican las condiciones del mundo real pero demuestran efectivamente las Leyes de Kirchhoff. ¿Quieres ajustar estas configuraciones o necesitas ayuda con una parte específica (como el cableado o el código)? ¡Házmelo saber!