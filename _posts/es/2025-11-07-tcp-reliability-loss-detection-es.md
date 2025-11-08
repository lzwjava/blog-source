---
audio: false
generated: true
image: false
lang: es
layout: post
model: moonshotai/kimi-k2-thinking
title: Fiabilidad de TCP y Detección de Pérdidas
translated: true
type: note
---

Permíteme desglosar esta conversación sobre la fiabilidad de TCP en conceptos claros:

## **1. Detección de Paquetes Perdidos**

TCP utiliza dos mecanismos principales para detectar datos faltantes:

- **Timeout**: Un simple temporizador de cuenta regresiva comienza cuando se envía un paquete. Si no llega ningún acuse de recibo (ACK) antes de que expire el temporizador, el paquete se declara perdido y se retransmite. Este es el método de detección de "último recurso".

- **ACKs Duplicados (Retransmisión Rápida)**: Esto es más sofisticado. Cuando el receptor recibe paquetes *fuera de orden*, sigue enviando ACKs para el *último* paquete recibido *en orden* exitosamente. Por ejemplo:
  - Si recibió los paquetes #1, #2, pero falta el #3, sigue enviando ACK para #2 incluso cuando luego recibe #4, #5, etc.
  - **Tres ACKs duplicados** para el mismo número de secuencia (#2 en nuestro ejemplo) indica que es probable que el paquete #3 esté perdido (no solo retrasado), lo que desencadena una retransmisión *inmediata*—mucho más rápido que esperar a que ocurra un timeout.

## **2. Impacto en el Rendimiento por RTT Alto**

Tienes razón—un Tiempo de Ida y Vuelta (RTT) alto hace que las retransmisiones sean problemáticas:
- Si RTT = 200ms (ej., entre continentes), y se pierde un paquete, esperas *al menos* 200ms para descubrirlo mediante timeout
- Durante ese período de espera, el ancho de banda permanece inactivo, el rendimiento se desploma y la conexión se siente "lenta"
- La retransmisión rápida ayuda dramáticamente aquí, reduciendo el tiempo de detección de segundos a milisegundos

## **3. Intervalos de Timeout Adaptativos**

TCP no utiliza un valor de timeout fijo—rastrea inteligentemente las condiciones de la red:

- **Estimación de RTT**: TCP mide continuamente cuánto tiempo tardan en regresar los acuses de recibo
- **Timeout Dinámico**: El tiempo de espera de retransmisión (RTO) se calcula en base al RTT medido más un margen de seguridad (típicamente RTT + 4×desviación)
- **Autoajuste**: Cuando el RTT aumenta (congestión de la red, rutas más largas), el timeout se estira automáticamente para evitar retransmisiones *prematuras*
- **Evitar Retransmisiones Innecesarias**: Sin esto, TCP podría reenviar paquetes perfectamente bien que solo estaban retrasados, desperdiciando ancho de banda y causando entregas duplicadas

**Conclusión**: La fiabilidad de TCP no se trata solo de retransmitir—se trata de detectar *inteligentemente* la pérdida sin esperar demasiado tiempo ni actuar con demasiada premura.