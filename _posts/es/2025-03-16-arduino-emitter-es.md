---
audio: false
generated: true
lang: es
layout: post
title: Construyendo un Amplificador de Emisor Común con un Arduino
translated: true
type: note
---

Construir un amplificador de emisor común (CE) usando un Arduino es un proyecto interesante, pero vale la pena aclarar los roles: el Arduino en sí no actuará como el amplificador (es un microcontrolador digital), pero puede servir como una fuente de señal o una herramienta de medición para un circuito amplificador CE construido con un transistor de unión bipolar (BJT). Un amplificador CE es un circuito analógico clásico que utiliza un transistor NPN o PNP para amplificar una pequeña señal de entrada, ofreciendo una ganancia de voltaje y una ganancia de corriente moderadas.

Aquí, te guiaré a través del diseño de un amplificador CE básico basado en NPN, usando el Arduino para generar una señal de entrada (vía PWM) y medir la salida. Esta configuración demostrará la amplificación aprovechando las capacidades del Arduino.

---

### **Descripción general de un amplificador de emisor común**
- **Propósito:** Amplifica una pequeña señal AC (por ejemplo, audio u onda sinusoidal).
- **Características clave:**
  - El transistor opera en la región activa.
  - La señal de entrada se aplica a la base, la salida se toma del colector.
  - La ganancia de voltaje está determinada por las relaciones de las resistencias y las propiedades del transistor.
- **Componentes:**
  - Transistor NPN (por ejemplo, 2N3904 o BC547)
  - Resistencias (para polarización y carga)
  - Capacitores (para acoplar señales AC)
  - Arduino (fuente de señal y medición)

---

### **Paso 1: Diseñar el circuito**

#### **Componentes necesarios**
- Transistor NPN (por ejemplo, 2N3904)
- Resistencias: R1 = 47kΩ, R2 = 10kΩ (polarización), RC = 1kΩ (colector), RE = 220Ω (emisor)
- Capacitores: C1 = 10µF (acoplamiento de entrada), C2 = 10µF (acoplamiento de salida), CE = 100µF (bypass de emisor, opcional para mayor ganancia)
- Arduino (por ejemplo, Uno)
- Protoboard, cables jumpers
- Fuente de alimentación (pin 5V del Arduino o externa de 9V, ajustado según sea necesario)

#### **Esquema del circuito**
```
Vcc (5V) ---- R1 ----+---- RC ---- Colector (C)
             47kΩ     |     1kΩ          |
                      |                  |
Base (B) --- C1 -----+                  |
            10µF     |                  |
Arduino PWM (Pin 9)  R2                 |
                     10kΩ              Salida --- C2 ---- Hacia Arduino A0
                      |                  |         10µF
                      |                  |
                      +---- RE ---- Emisor (E) --- CE (opcional) --- GND
                           220Ω                   100µF
                      |
                     GND
```
- **Polarización (R1, R2):** Establece el punto de operación del transistor.
- **RC:** Resistencia de colector para la señal de salida.
- **RE:** Resistencia de emisor para estabilidad.
- **C1, C2:** Bloquean DC, pasan señales AC.
- **CE (opcional):** Hace un bypass a RE para una mayor ganancia en AC.

#### **Punto de operación**
- Objetivo: Polarizar el transistor en la región activa (por ejemplo, VCE ≈ 2.5V para una fuente de 5V).
- Divisor de voltaje (R1, R2): \\( V_B = V_{CC} \cdot \frac{R2}{R1 + R2} = 5 \cdot \frac{10k}{47k + 10k} \approx 0.88V \\).
- \\( V_E = V_B - V_{BE} \approx 0.88 - 0.7 = 0.18V \\).
- \\( I_E = \frac{V_E}{RE} = \frac{0.18}{220} \approx 0.82 \, \text{mA} \\).
- \\( V_C = V_{CC} - I_C \cdot RC \approx 5 - 0.82 \cdot 1k \approx 4.18V \\).
- \\( V_{CE} = V_C - V_E \approx 4.18 - 0.18 = 4V \\) (bueno para fuente de 5V).

---

### **Paso 2: Usar Arduino como fuente de señal**

#### **Rol del Arduino**
- Generar una pequeña señal AC usando PWM (Modulación por Ancho de Pulso) en un pin como el 9 (que soporta PWM).
- Filtrar el PWM para aproximar una onda sinusoidal con un simple filtro RC paso bajo (opcional).

#### **Código para generar una señal**
```cpp
const int pwmPin = 9; // Pin de salida PWM

void setup() {
  pinMode(pwmPin, OUTPUT);
  // Establecer frecuencia PWM (opcional, por defecto es ~490 Hz)
}

void loop() {
  // Simular una onda sinusoidal con PWM (rango 0-255)
  for (int i = 0; i < 360; i += 10) {
    float sineValue = sin(radians(i)); // Onda sinusoidal de -1 a 1
    int pwmValue = 127 + 127 * sineValue; // Escalar a 0-255
    analogWrite(pwmPin, pwmValue);
    delay(10); // Ajustar para frecuencia (por ejemplo, ~100 Hz aquí)
  }
}
```
- **Salida:** Señal PWM de ~0–5V, centrada en 2.5V con ~2.5V pico a pico.
- **C1:** Elimina el offset DC, pasando solo el componente AC (~1.25V pico) a la base.

#### **Filtro opcional**
Agregar una resistencia de 1kΩ y un capacitor de 0.1µF en serie desde el Pin 9 a GND, tomando la señal antes de C1, para suavizar el PWM en una onda sinusoidal aproximada.

---

### **Paso 3: Medir la salida**

#### **Medición con Arduino**
- Conectar la salida del amplificador (después de C2) a A0.
- Usar el Arduino para leer la señal amplificada y mostrarla a través del Monitor Serie.

#### **Código para medir y mostrar**
```cpp
const int inputPin = A0; // Medir la salida aquí

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(inputPin); // 0-1023 se mapea a 0-5V
  float voltage = sensorValue * (5.0 / 1023.0);
  Serial.print("Voltaje de Salida (V): ");
  Serial.println(voltaje);
  delay(100); // Ajustar la tasa de muestreo
}
```

#### **Ganancia esperada**
- Ganancia de voltaje \\( A_v = -\frac{RC}{RE} = -\frac{1k}{220} \approx -4.5 \\) (negativa debido a la inversión de fase).
- Entrada: ~1.25V pico (después del acoplamiento).
- Salida: ~4.5 × 1.25 = 5.625V pico (pero recortada a 5V debido al límite de la fuente).

---

### **Paso 4: Construir y probar**

#### **Ensamblaje**
1. Cablear el circuito en una protoboard según el esquema.
2. Cargar el código de generación de señal al Arduino y conectar el Pin 9 a C1.
3. Alimentar el circuito a través de 5V del Arduino (o usar 9V con resistencias ajustadas).
4. Cargar el código de medición y abrir el Monitor Serie (9600 baudios).

#### **Verificación**
- **Señal de entrada:** ~1–2V pico a pico después de C1 (usar un multímetro u osciloscopio si está disponible).
- **Señal de salida:** Debería ser más grande (por ejemplo, 4–5V pico a pico) e invertida.
- Verificar VCE (~2–4V) con un multímetro para asegurar la operación en la región activa.

---

### **Consejos y solución de problemas**
- **Ganancia demasiado baja:** Agregar CE (100µF) a través de RE para aumentar la ganancia en AC (elimina la degeneración de RE).
- **Recorte (Clipping):** Si la salida excede 5V, reducir la amplitud de entrada (ajustar el rango PWM) o aumentar Vcc (por ejemplo, fuente externa de 9V).
- **Ruido:** El PWM es cuadrado; una mejor onda sinusoidal (vía generador externo o filtro) mejora los resultados.
- **Especificaciones del transistor:** Asegurar que el 2N3904 maneje las corrientes (Ic < 200mA, seguro aquí).

Esta configuración demuestra el comportamiento central de un amplificador CE—amplificación de voltaje—mientras integra Arduino para la generación y análisis de señales. ¿Quieres ajustar la ganancia, agregar un altavoz para audio o refinar la señal? ¡Házmelo saber!