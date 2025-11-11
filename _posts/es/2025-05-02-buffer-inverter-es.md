---
audio: false
generated: true
lang: es
layout: post
title: Circuitos de Búfer e Inversor
translated: true
type: note
---

Aquí tienes un tutorial sobre circuitos buffer e inversor basado en el video de YouTube proporcionado:

### Comprensión de los Circuitos con Transistores

* El video explora dos circuitos con transistores con entradas y salidas, centrándose en el voltaje.
* Los transistores actúan como interruptores de corriente; un voltaje de entrada positivo (ej. +5V) crea corriente, encendiendo el transistor. Un voltaje cero significa que no hay corriente y el transistor está apagado.
* Las entradas y salidas se discuten en términos de unos y ceros, donde 0 representa 0V y 1 representa +5V.

### Circuito 1: Seguidor de Emisor / Buffer

* **La entrada es 0 (0V):** El transistor está apagado y la salida está conectada a tierra a través de una resistencia, lo que da como resultado una salida de 0.
* **La entrada es 1 (+5V):** Fluye corriente y la salida está conectada directamente a +5V, haciendo que la salida sea 1.
* Este circuito se llama **seguidor de emisor** porque el emisor sigue a la base (entrada).
* Otro nombre para él es **buffer**, que emite el mismo nivel de voltaje que la entrada.
* El buffer se simboliza con un triángulo en los diagramas de lógica digital.

### Circuito 2: Inversor

* **La entrada es 0:** No fluye corriente, el transistor está apagado y la salida está conectada a +5V a través de una resistencia pull-up, haciendo que la salida sea 1.
* **La entrada es 1:** Fluye corriente, conectando la salida a tierra, lo que da como resultado una salida de 0.
* Este circuito se conoce como **inversor**.
* El símbolo lógico del inversor es similar al de un buffer pero con una burbuja en la salida, lo que indica la inversión.
* Un circuito inversor emite lo opuesto a la entrada.

En resumen, el video explica cómo los circuitos con transistores pueden funcionar como un buffer, que mantiene la señal de entrada, o como un inversor, que revierte la señal de entrada.
http://googleusercontent.com/youtube_content/0