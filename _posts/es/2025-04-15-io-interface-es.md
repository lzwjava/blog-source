---
audio: false
generated: true
lang: es
layout: post
title: Tecnología de E/S e Interfaz
translated: true
type: note
---

¡Excelente! Aquí tienes un **tutorial completo** para la **Parte 4: Tecnología de E/S e Interfaz**, basado en el esquema de tu curso. Este tutorial está estructurado para explicar los conceptos con claridad, proporcionar ejemplos prácticos y mostrar cómo componentes como el 8255A, 8253/8254 y 8251A trabajan juntos en un sistema de microcomputadora.

---

## 📘 Parte 4: Tecnología de E/S e Interfaz

---

### **1. Conceptos Básicos de Interfaces de E/S**

#### ✅ Direccionamiento de Puertos

Las interfaces de E/S permiten que un microprocesador se comunique con dispositivos externos. Existen **dos esquemas principales de direccionamiento**:

- **E/S Mapeada en Memoria**:
  - Los dispositivos de E/S se tratan como ubicaciones de memoria.
  - Utiliza las mismas instrucciones que el acceso a memoria (ej., `MOV`).
  - Pros: Espacio de direcciones más grande, puede usar todas las instrucciones de la CPU.
  - Contras: Consume espacio de direcciones de memoria.

- **E/S Aislada (E/S Mapeada en Puertos)**:
  - Instrucciones especiales como `IN` y `OUT`.
  - Espacio de direcciones limitado (usualmente 256 puertos).
  - Espacio de direcciones separado de la memoria.

| Tipo                  | Conjunto de Instrucciones | Espacio de Direcciones |
|-----------------------|---------------------------|------------------------|
| Mapeada en Memoria    | `MOV`, etc.               | Parte de la memoria    |
| Aislada (Mapeada en E/S) | `IN`, `OUT`           | Espacio de E/S separado|

---

#### ✅ Modos de Transferencia de Datos

1. **E/S Controlada por Programa**:
   - La CPU verifica el estado del dispositivo y lee/escribe datos directamente.
   - Simple pero ineficiente (espera ocupada).

2. **E/S Basada en Interrupciones**:
   - El dispositivo notifica a la CPU cuando está listo mediante una **interrupción**.
   - La CPU ejecuta una Rutina de Servicio de Interrupción (ISR).
   - Mejora la eficiencia.

3. **DMA (Acceso Directo a Memoria)**:
   - El dispositivo transfiere datos directamente hacia/desde la memoria.
   - Omite a la CPU para transferencias de datos grandes o rápidas.
   - Se usa para dispositivos de alta velocidad como discos.

---

### **2. Sistemas de Interrupción**

#### ✅ Tabla de Vectores de Interrupción

- Almacena las direcciones de las **Rutinas de Servicio de Interrupción (ISR)**.
- Cada tipo de interrupción tiene un **vector único** (ej., INT 0x08 para el Temporizador).
- La CPU consulta la tabla para saltar a la ISR correcta.

#### ✅ Manejo de Prioridades

- Cuando ocurren múltiples interrupciones simultáneamente, la **prioridad** determina cuál se atiende primero.
- La prioridad puede ser **fija** o **programable**.

#### ✅ Controlador de Interrupciones Programable 8259A

- Gestiona múltiples fuentes de interrupción (hasta 8).
- Puede **encadenarse** para 64 entradas de interrupción.
- Funciones clave:
  - Enmascaramiento de interrupciones.
  - Configuración de prioridades.
  - Envío del vector de interrupción a la CPU.

**Registros**:
- IMR (Registro de Máscara de Interrupciones)
- ISR (Registro de Servicio)
- IRR (Registro de Solicitud de Interrupción)

**Ejemplo**: El teclado y el Temporizador activan interrupciones — el 8259A las prioriza según la prioridad configurada.

---

### **3. Chips de Interfaz Comunes**

---

#### ✅ Interfaz Periférica Programable 8255A (PPI)

Se utiliza para interactuar con dispositivos paralelos externos como interruptores, LEDs, etc.

- Tiene 3 puertos: **Puerto A**, **Puerto B** y **Puerto C**.
- Se controla mediante la **Palabra de Control**.

**Modos de Operación**:

- **Modo 0** – E/S Simple
  - Cada puerto puede ser entrada/salida.
- **Modo 1** – E/S con Protocolo de Comunicación (Handshaking)
  - Sincronización con el periférico.
- **Modo 2** – E/S Bidireccional (solo para el Puerto A)
  - Transferencia de datos bidireccional con protocolo de comunicación.

**Ejemplo**:
- Puerto A: salida a una pantalla de LEDs
- Puerto B: entrada desde interruptores DIP
- Puerto C: se usa para señales de control

---

#### ✅ Temporizador de Intervalos Programable 8253 / 8254

Se utiliza para generar retardos, velocidades en baudios, etc.

- Tiene 3 contadores independientes de 16 bits.
- Cada contador tiene modos (0–5), ej.:

| Modo | Descripción                  |
|------|------------------------------|
| 0    | Interrupción en cuenta final   |
| 2    | Generador de tasa (ej., para reloj) |
| 3    | Generador de onda cuadrada    |

**Aplicaciones**:
- Generación de retardos
- Reloj en tiempo real
- Generación de velocidad en baudios para puertos serie

**Uso Típico**:
- Contador 0: Tic del temporizador del SO
- Contador 1: Refresco de DRAM
- Contador 2: Tono del altavoz

---

#### ✅ USART 8251A (Transceptor Síncrono/Asíncrono Universal)

Se utiliza para **comunicación serie**.

- Convierte entre datos paralelos y serie.
- Admite ambos modos:
  - **Síncrono**: requiere señal de reloj
  - **Asíncrono**: usa bits de inicio/parada

**Características Clave**:
- Control de velocidad en baudios (vía 8253/8254)
- Longitud de carácter, bits de parada y paridad configurables
- Admite almacenamiento en búfer de transmisión y recepción

**Aplicación**: Comunicación por puerto serie con PC o microcontrolador.

---

## ✅ Tabla Resumen

| Chip    | Función                      | Características Clave                 |
|---------|------------------------------|---------------------------------------|
| 8255A   | E/S Paralela                 | 3 puertos, 3 modos, protocolo de comunicación |
| 8253/54 | Temporización/Conteo         | 3 contadores, múltiples modos         |
| 8251A   | Comunicación Serie           | Sínc/Asínc, control de baudios        |
| 8259A   | Control de Interrupciones    | Prioridad, enmascaramiento, vectorización de ISR |

---

## 🧠 Ejemplo de Escenario del Mundo Real

Quieres diseñar un sistema simple de microcomputadora para:

- Controlar una matriz de LEDs a través del Puerto A (8255A Modo 0)
- Recibir entrada del teclado mediante interrupciones (8259A)
- Generar un tic del sistema periódico cada 1ms (8253 Modo 2)
- Enviar datos de sensores a una PC por serie (8251A en modo asíncrono)

Cada chip se configuraría y conectaría a la CPU a través de decodificación de direcciones y señales de control, con el software apropiado escrito para gestionar la comunicación.

---

¡Házme saber si quieres código de ejemplo, diagramas de simulación o un cuestionario para este capítulo