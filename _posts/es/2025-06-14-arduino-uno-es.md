---
audio: false
generated: true
lang: es
layout: post
title: Variantes de Arduino Uno
translated: true
type: note
---

El Arduino Uno, Uno R3 y Uno Mini son variaciones de la popular placa de microcontrolador Arduino, cada una con diferencias específicas en diseño, características y casos de uso. A continuación se presenta una comparación concisa basada en sus diferencias clave:

### 1. **Arduino Uno (Original) vs. Arduino Uno R3**
El Arduino Uno y el Uno R3 son esencialmente la misma placa, siendo el Uno R3 la tercera revisión (R3) del Uno original. Las diferencias son menores y se centran en mejoras de usabilidad y compatibilidad.

- **Microcontrolador**: Ambos utilizan el **ATmega328P** (AVR de 8 bits, velocidad de reloj de 16 MHz).
- **Configuración de pines (Pinout)**:
  - El Uno R3 añade **pines SDA y SCL** cerca del pin AREF para compatibilidad I2C, mejorando el soporte para shields.
  - El R3 incluye un **pin IOREF** para permitir que los shields se adapten al voltaje de la placa (5V en este caso).
- **Chip USB-a-Serial**:
  - El Uno original utiliza un chip **FTDI FT232R** para la comunicación USB-a-serial.
  - El Uno R3 actualiza a un microcontrolador **ATmega16U2**, que es más flexible y soporta una comunicación más rápida.
- **Otros Cambios**:
  - El R3 tiene un **circuito de reset** más robusto y un LED en el pin 13 bufferizado (a través de un amplificador operacional) para evitar interferencias.
  - El R3 añade dos pines extra al conector de 6 pines cerca del pin de reset (uno es IOREF, el otro está reservado).
- **Factor de Forma**: Dimensiones idénticas (~6.86 cm x 5.33 cm).
- **Disponibilidad**: El Uno R3 es el estándar actual; las revisiones más antiguas del Uno (R1, R2) están mayormente obsoletas.
- **Caso de Uso**: Ambos son aptos para principiantes e ideales para prototipos con shields. El R3 es mejor para shields modernos debido a la configuración de pines actualizada.

**Diferencia Clave**: El Uno R3 es una versión mejorada del Uno original con mejor compatibilidad de shields y una interfaz USB más robusta. Para la mayoría de usuarios, el R3 es la mejor opción ya que es el estándar actual.

### 2. **Arduino Uno R3 vs. Arduino Uno Mini Limited Edition**
El Arduino Uno Mini Limited Edition es una versión compacta y de edición especial del Uno R3, diseñada para coleccionistas y proyectos que requieren una huella más pequeña.

- **Microcontrolador**: Ambos utilizan el **ATmega328P** (AVR de 8 bits, 16 MHz).
- **Factor de Forma**:
  - Uno R3: Tamaño estándar (~6.86 cm x 5.33 cm).
  - Uno Mini: Mucho más pequeño (~3.3 cm x 2.54 cm), compatible con protoboard, con una **PCB bañada en oro** para atractivo estético.
- **Conectores**:
  - Uno R3: Versiones PTH o SMD; conectores hembra estándar para shields.
  - Uno Mini: Conectores macho pre-soldados, sin compatibilidad con shields debido al tamaño y diseño.
- **Puerto USB**:
  - Uno R3: Conector USB-B.
  - Uno Mini: **Conector USB-C**, más moderno y compacto.
- **Pines de E/S**:
  - Ambos tienen **14 E/S digitales** (6 PWM) y **6 entradas analógicas**, pero los pines del Uno Mini están dispuestos de manera diferente debido a su menor tamaño.
- **Alimentación**:
  - Ambos funcionan a **5V**, pero el Uno Mini carece de conector de barril para DC (se alimenta via USB-C o pin VIN).
- **Memoria**: Idéntica (**32 KB Flash, 2 KB SRAM, 1 KB EEPROM**).
- **Características Especiales**:
  - El Uno Mini es una **edición limitada** con gráficos únicos y empaque coleccionable, dirigido a entusiastas.
- **Precio**: El Uno Mini es típicamente más caro debido a su estado de edición limitada (~$45 vs. ~$27 para el Uno R3).
- **Caso de Uso**:
  - Uno R3: Prototipado de propósito general, compatible con shields, apto para principiantes.
  - Uno Mini: Proyectos con limitaciones de espacio, coleccionistas, o desarrolladores que desean una placa premium y compacta.

**Diferencia Clave**: El Uno Mini es una versión más pequeña y premium del Uno R3 con un puerto USB-C y sin soporte para shields, ideal para proyectos compactos o coleccionables.

### 3. **Tabla Resumen**

| Característica           | Arduino Uno (Original) | Arduino Uno R3         | Arduino Uno Mini       |
|--------------------------|------------------------|------------------------|------------------------|
| **Microcontrolador**     | ATmega328P            | ATmega328P            | ATmega328P            |
| **Velocidad de Reloj**   | 16 MHz                | 16 MHz                | 16 MHz                |
| **Factor de Forma**      | ~6.86 cm x 5.33 cm    | ~6.86 cm x 5.33 cm    | ~3.3 cm x 2.54 cm     |
| **Conector USB**         | USB-B (FTDI)          | USB-B (ATmega16U2)    | USB-C                 |
| **Pines de E/S**         | 14 digitales, 6 analógicas | 14 digitales, 6 analógicas | 14 digitales, 6 analógicas |
| **Compatibilidad con Shields** | Limitada (antigua) | Sí                    | No                    |
| **Entrada de Alimentación** | USB, conector de barril, VIN | USB, conector de barril, VIN | USB-C, VIN            |
| **Características Especiales** | -                | Pines SDA/SCL, IOREF  | Edición limitada, PCB dorada |
| **Precio (Aprox.)**      | Obsoleto              | ~$27                  | ~$45                  |
| **Ideal Para**           | Proyectos legacy      | Prototipado general   | Proyectos compactos/coleccionables |

### ¿Cuál Elegir?
- **Arduino Uno R3**: La opción recomendada para la mayoría de usuarios. Es ampliamente compatible, funciona con shields y es ideal para principiantes o proyectos de propósito general. Elige esta a menos que tengas restricciones específicas de tamaño o desees una placa coleccionable.
- **Arduino Uno (Original)**: Solo es relevante si trabajas con shields antiguos, anteriores al R3, o si ya tienes una placa. De lo contrario, opta por el R3.
- **Arduino Uno Mini Limited Edition**: Elige esta opción para proyectos con limitaciones de espacio, si prefieres USB-C, o si eres un entusiasta/coleccionista de Arduino. Es menos versátil debido a la falta de soporte para shields.

Si estás comenzando desde cero, el **Uno R3** es la mejor opción general debido a su compatibilidad, soporte comunitario y asequibilidad. Para necesidades específicas de proyecto (por ejemplo, tamaño o estética), el Uno Mini es una gran alternativa.

¡Avísame si necesitas ayuda con un proyecto específico o una comparación de características!