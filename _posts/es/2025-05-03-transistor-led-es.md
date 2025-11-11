---
audio: false
generated: true
lang: es
layout: post
title: Circuito LED con un Transistor
translated: true
type: note
---

Aquí tienes un tutorial basado en el video de YouTube que proporcionaste, que explica cómo usar un transistor para controlar un circuito con LED.

**Objetivo:** Aprender a usar un transistor como interruptor para encender y apagar un LED utilizando una señal de baja corriente.

**Información de Contexto:**

* Los transistores permiten que una corriente mayor fluya entre su colector y emisor, controlada por una corriente más pequeña que fluye desde la base hacia el emisor.
* La corriente del colector puede ser significativamente mayor que la corriente de la base (ej. 100 veces).
* Los LEDs típicamente requieren una cantidad específica de corriente (ej. 20mA) para iluminarse correctamente.

**Pasos:**

1.  **Configurar el circuito básico del LED:** Conecta una fuente de alimentación de 5V, un LED, una resistencia (como de 220 ohmios) y el transistor en un arreglo en serie. La resistencia es crucial para limitar la corriente que fluye hacia el LED. El transistor funcionará como el interruptor dentro de este circuito.
2.  **Conectar el transistor:** Identifica los pines del emisor, la base y el colector en tu transistor. Conecta el pin del emisor a tierra. Conecta el pin del colector en el circuito entre la resistencia (y el LED) y el emisor.
3.  **Conectar la señal de control:** Conecta el terminal positivo de tu señal de control al pin de la base del transistor. Conecta la tierra de la señal de control al pin del emisor (que también está conectado a la tierra del circuito principal).
4.  **Observar el resultado:** Cuando la señal de control está activa (encendida), una pequeña corriente fluirá desde la base hacia el emisor. Esta pequeña corriente de base permite que una corriente mucho mayor fluya desde el colector hacia el emisor, haciendo que el LED se encienda con brillo. Cuando la señal de control está inactiva (apagada), no fluye corriente de la base al emisor, el transistor se apaga y el LED se oscurece.

**Conceptos Clave:**

* **Amplificación de Corriente:** Los transistores pueden amplificar una pequeña corriente de base para controlar una corriente de colector mucho mayor.
* **Interruptor Controlado por Corriente:** Los transistores funcionan como interruptores donde una pequeña corriente de entrada dicta el flujo de una corriente mayor.

Al implementar este circuito, puedes usar efectivamente una pequeña señal de control para gestionar un circuito que requiere una corriente más alta, como uno que alimenta un LED.
http://googleusercontent.com/youtube_content/0