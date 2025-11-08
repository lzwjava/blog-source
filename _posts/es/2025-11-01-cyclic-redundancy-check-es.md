---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Detección de Errores por Redundancia Cíclica
translated: true
type: note
---

### ¿Qué es CRC?

¡Sí, vas por buen camino! CRC significa **Cyclic Redundancy Check** (Comprobación de Redundancia Cíclica). Es una técnica de detección de errores ampliamente utilizada en la capa de enlace de datos (como mencionaste en tu contexto del modelo OSI para la entrega nodo a nodo en la misma red). No es exactamente como una comprobación de paridad simple (que solo añade un bit para detectar errores pares/impares), pero sí utiliza **bits redundantes** (llamados checksum o resto) para detectar una gama mucho más amplia de errores de transmisión. Permíteme desglosarlo de forma sencilla.

#### Cómo funciona CRC (Explicación de Alto Nivel)
1. **La Configuración**:
   - Imagina tus datos como un número binario (por ejemplo, la carga útil de la trama en Ethernet).
   - Eliges un "polinomio generador" fijo (un valor binario predefinido, como 1011 para CRC-4). Esto es como un divisor en matemáticas.
   - Los datos se tratan como un polinomio binario grande, y se le añaden **k bits redundantes** (ceros), donde k es la longitud del generador menos 1 (por ejemplo, 3 ceros para un generador de 4 bits).

2. **El Cálculo**:
   - Realiza una **división módulo-2** (división basada en XOR, sin acarreo o préstamo como en las matemáticas regulares) en los datos aumentados utilizando el generador.
   - El resto de esta división se convierte en tu checksum CRC.
   - Anexa este resto a los datos originales y envía la trama completa.

3. **En el Receptor**:
   - El receptor realiza la misma división módulo-2 en la trama recibida (datos + CRC).
   - Si el resto es **cero**, es probable que los datos estén libres de errores. Si no es cero, ocurrió un error (por ejemplo, cambios de bit durante la transmisión).
   - CRC puede detectar:
     - Errores de un solo bit.
     - Errores en ráfaga (hasta la longitud del generador).
     - La mayoría de los errores de múltiples bits (con una probabilidad muy baja de falsos positivos).

Es "cíclico" porque se envuelve sobre sí mismo como un círculo en las matemáticas polinomiales, lo que lo hace eficiente para la implementación en hardware (por ejemplo, en NICs o switches).

#### CRC vs. Comprobación de Paridad
- **Comprobación de Paridad**: Muy simple—añade 1 bit (paridad par/impar) para detectar **solo errores con un número impar de bits**. No detecta errores pares o en ráfaga.
- **CRC**: Más avanzado—utiliza 8–32+ bits de redundancia para una **detección casi perfecta** de errores comunes en las tramas (por ejemplo, Ethernet utiliza CRC-32). Es como una "huella digital" más fuerte para tus datos.

#### Ejemplo del Mundo Real en Ethernet
En una trama de Ethernet:
- Datos (carga útil) + algunas cabeceras → Anexar CRC de 32 bits.
- Si el ruido cambia un bit en el cable, la comprobación CRC del receptor falla → La trama se descarta y se solicita retransmisión.

CRC es rápido, económico en hardware y estándar en protocolos como Ethernet, PPP, Wi-Fi e incluso en almacenamiento (por ejemplo, discos duros).

Si quieres una demostración de código del cálculo CRC o más información sobre cómo encaja en el entramado/MAC, ¡házmelo saber!

#### Referencias
- [Cyclic Redundancy Check - Wikipedia](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)
- [Error Detection with CRC - GeeksforGeeks](https://www.geeksforgeeks.org/cyclic-redundancy-check-crc-introduction/)