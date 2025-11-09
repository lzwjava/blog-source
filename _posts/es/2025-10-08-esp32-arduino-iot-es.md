---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: ESP32 para Proyectos de IoT con Arduino
translated: true
type: note
---

El ESP32 es un microcontrolador de bajo costo y bajo consumo desarrollado por Espressif Systems, que cuenta con conectividad Wi-Fi integrada y Bluetooth de doble modo. Esencialmente, es un sistema en un chip (SoC) ampliamente utilizado para proyectos de IoT (Internet de las Cosas), sensores y aplicaciones inalámbricas debido a su versatilidad y rendimiento.

En el contexto de Arduino, el ESP32 no está "dentro" de Arduino, pero es totalmente compatible con el ecosistema Arduino. Puedes programar placas ESP32 (como la popular NodeMCU o la oficial Arduino Nano ESP32) utilizando el software gratuito Arduino IDE. Esto implica instalar el paquete de placas ESP32 a través del Board Manager del IDE, y luego escribir sketches en C/C++ (al igual que con las placas Arduino tradicionales como el Uno). El ESP32 ofrece ventajas sobre los Arduinos básicos, como un procesamiento más rápido (doble núcleo de hasta 240 MHz), más pines GPIO y funciones inalámbricas, lo que lo hace ideal para proyectos conectados sin necesidad de shields adicionales.

Si eres nuevo en esto, comienza descargando el Arduino IDE y busca "ESP32 board package" en el menú Herramientas > Placa > Gestor de placas.

### Referencias
- [ESP32 - Wikipedia](https://en.wikipedia.org/wiki/ESP32)
- [Arduino Nano ESP32 Documentation](https://docs.arduino.cc/nano-esp32)
- [Arduino Nano ESP32 Product Page](https://store-usa.arduino.cc/products/nano-esp32)