---
audio: false
generated: true
lang: es
layout: post
title: MOSFET como interruptor controlado por Arduino
translated: true
type: note
---

Parece que podría haber un malentendido en tu pregunta. Un Arduino no puede usarse para *construir* Transistores de Efecto de Campo de Metal-Óxido-Semiconductor (MOSFET) porque los MOSFET son dispositivos semiconductores fundamentales fabricados mediante procesos complejos como la fotolitografía y el dopado en un entorno de sala limpia. Sin embargo, asumo que quisiste decir "cómo usar un Arduino para construir un circuito *que utilice* MOSFET" o "cómo usar MOSFET en un proyecto de Arduino". Si he interpretado mal, ¡por favor acláralo!

Procederé explicando cómo usar un Arduino para controlar un MOSFET en un circuito práctico, como un simple interruptor o amplificador. Los MOSFET son componentes versátiles, a menudo utilizados como interruptores o en circuitos de amplificación, y se combinan bien con las salidas digitales de Arduino. A continuación, proporcionaré una guía paso a paso para una aplicación común: usar un MOSFET de canal N (por ejemplo, IRF540 o 2N7000) como un interruptor de alta potencia controlado por un Arduino.

---

### **Proyecto: MOSFET como Interruptor Controlado por Arduino**

#### **Descripción General**
- **Propósito:** Usar un Arduino para encender y apagar una carga de alta potencia (por ejemplo, una tira de LED, un motor o una lámpara) a través de un MOSFET.
- **¿Por qué un MOSFET?** A diferencia de los BJT, los MOSFET son controlados por voltaje, requieren una corriente mínima del Arduino y pueden manejar corrientes/voltajes más altos que los pines del Arduino (máx. 40mA, 5V).

#### **Componentes Necesarios**
- Arduino (por ejemplo, Uno)
- MOSFET de canal N (por ejemplo, IRF540 o 2N7000; IRF540 para mayor potencia)
- Resistencia: R1 = 10kΩ (pull-down), R2 = 220Ω (protección de puerta, opcional)
- Carga: por ejemplo, tira de LED de 12V, motor DC, o lámpara (con la fuente de alimentación apropiada)
- Diodo (por ejemplo, 1N4007, para cargas inductivas como motores)
- Protoboard, cables jumper
- Fuente de alimentación externa (por ejemplo, 12V para la carga)

#### **Esquema del Circuito**
```
Pin 9 de Arduino ---- R2 (220Ω) ---- Puerta (G)
                             |
                             |
V_carga (ej. 12V) ---- Carga ---- Drenador (D)
                             | 
                             |
                           Fuente (S) ---- GND
                             |
                            R1 (10kΩ)
                             |
                            GND
```
- **Para Cargas Inductivas (ej. Motor):** Añade un diodo de retroceso (flyback) (1N4007) en paralelo con la carga (cátodo a V_carga, ánodo a Drenador) para proteger el MOSFET de picos de voltaje.
- **Alimentación:** Arduino alimentado por USB o 5V; la carga alimentada por fuente externa (ej. 12V). Conecta todos los GND juntos.

#### **Cómo Funciona**
- **Función del MOSFET:** Actúa como un interruptor entre el Drenador y la Fuente, controlado por el voltaje de la Puerta.
- **Función del Arduino:** Envía una señal HIGH (5V) o LOW (0V) a la Puerta a través del Pin 9.
- **Lógica:**
  - HIGH (5V) en la Puerta → MOSFET se activa (ON) → La carga recibe energía.
  - LOW (0V) en la Puerta → MOSFET se desactiva (OFF) → La carga se detiene.
- **R1 (Pull-down):** Garantiza que la Puerta esté en LOW cuando el Arduino esté apagado o el pin esté en estado de alta impedancia (flotante).
- **R2 (Opcional):** Limita la corriente hacia la Puerta (generalmente innecesario para MOSFET de nivel lógico).

---

### **Paso 1: Construir el Circuito**

1. **Conectar el MOSFET:**
   - **Puerta (G):** Al Pin 9 del Arduino a través de R2 (220Ω, opcional).
   - **Drenador (D):** Al lado negativo de la carga (por ejemplo, cátodo de la tira de LED).
   - **Fuente (S):** A GND.
2. **Carga y Alimentación:**
   - Conecta el lado positivo de la carga a V_carga (por ejemplo, fuente de 12V).
   - Conecta el GND de la fuente de 12V al GND del Arduino.
3. **Seguridad:**
   - Añade R1 (10kΩ) entre la Puerta y GND.
   - Para motores, añade el diodo en paralelo con la carga.

---

### **Paso 2: Código de Arduino**

#### **Interruptor Simple Encendido/Apagado**
```cpp
const int pinMosfet = 9; // Pin capaz de PWM

void setup() {
  pinMode(pinMosfet, OUTPUT); // Configurar pin como salida
}

void loop() {
  digitalWrite(pinMosfet, HIGH); // Encender MOSFET
  delay(1000);                   // Esperar 1 segundo
  digitalWrite(pinMosfet, LOW);  // Apagar MOSFET
  delay(1000);                   // Esperar 1 segundo
}
```
- **Salida:** La carga se enciende y apaga cada segundo.

#### **Atenuación por PWM (para LED/Motores)**
```cpp
const int pinMosfet = 9;

void setup() {
  pinMode(pinMosfet, OUTPUT);
}

void loop() {
  for (int brillo = 0; brillo <= 255; brillo += 5) {
    analogWrite(pinMosfet, brillo); // Aumentar brillo
    delay(50);
  }
  for (int brillo = 255; brillo >= 0; brillo -= 5) {
    analogWrite(pinMosfet, brillo); // Disminuir brillo
    delay(50);
  }
}
```
- **Salida:** La carga (por ejemplo, LED) se atenúa gradualmente (fade in/out).

---

### **Paso 3: Probar y Verificar**

1. **Cargar el Código:** Usa el IDE de Arduino para cargar cualquiera de los dos sketches.
2. **Encender:** Conecta el Arduino vía USB y la fuente externa a la carga.
3. **Observar:**
   - Para el código de encendido/apagado, la carga debería alternar cada segundo.
   - Para el PWM, la carga debería aumentar y disminuir su brillo gradualmente.
4. **Medir:** Usa un multímetro para comprobar:
   - Voltaje en la Puerta (0V o 5V).
   - Voltaje a través de la carga (0V o V_carga).

---

### **Elegir el MOSFET Correcto**
- **MOSFET de Nivel Lógico (por ejemplo, IRL540, 2N7000):** Se activa completamente con 5V del Arduino. Preferido para este proyecto.
- **MOSFET Estándar (por ejemplo, IRF540):** Necesita ~10V en la Puerta para activarse completamente. Con 5V, puede conducir parcialmente—usa un transistor o un driver (por ejemplo, BJT o IC como TC4420) para aumentar el voltaje de Puerta si usas estos.
- **Especificaciones:** Comprueba que V_DS (voltaje máximo) e I_D (corriente máxima) coincidan con tu carga (por ejemplo, IRF540: 100V, 33A).

---

### **Alternativa: Amplificador con MOSFET**
Si te referías a un amplificador basado en MOSFET (por ejemplo, Amplificador de Fuente Común), aquí tienes un esquema rápido:
- **Configuración:** Similar al amplificador EC pero con un MOSFET (por ejemplo, 2N7000).
- **Esquema:** Vcc → R_D (resistencia de Drenador) → Drenador; Fuente → GND; Puerta → Señal de entrada (vía condensador).
- **Función del Arduino:** Generar una pequeña señal AC (como en el ejemplo del amplificador EC).
- **Ganancia:** \\( A_v = -g_m \cdot R_D \\), donde \\( g_m \\) es la transconductancia.
- **Desafío:** Requiere un sesgado (biasing) preciso; menos común para principiantes que los amplificadores con BJT.

¡Avísame si prefieres cambiar a esto!

---

### **Consejos y Resolución de Problemas**
- **Calor:** Si el MOSFET se calienta, no está completamente activo (compatibilidad de nivel lógico) o la carga excede su capacidad—añade un disipador de calor o reduce la corriente.
- **Sin Respuesta:** Verifica las conexiones, la disposición de pines del MOSFET (GDS) y la fuente de alimentación.
- **Ruido:** La conmutación por PWM puede ser audible con motores—ajusta la frecuencia si es necesario (ajuste avanzado).
- **Voltaje Más Alto:** Para cargas >5V, asegúrate de que se cumple el voltaje umbral V_GS del MOSFET.

Este proyecto muestra cómo integrar un MOSFET con Arduino para un control práctico. ¿Quieres escalarlo (por ejemplo, control de velocidad de motor) o explorar la amplificación? ¡Solo dilo!