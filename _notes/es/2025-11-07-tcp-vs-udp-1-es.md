---
audio: false
generated: true
image: false
lang: es
layout: post
model: anthropic/claude-4.5-sonnet
title: Diferencias entre las conexiones TCP y UDP
translated: true
---

¡Tienes la intuición correcta! Permíteme aclarar las diferencias clave:

## Conexión TCP

Cuando se **establece** una conexión TCP (mediante el handshake de 3 vías), ambas partes mantienen **información de estado** sobre la otra:

**Lo que almacena cada lado:**
- **Dirección IP y puerto remoto** (¿con quién estoy hablando?)
- **Dirección IP y puerto local** (mi endpoint)
- **Números de secuencia** (para orden y confiabilidad)
- **Tamaños de ventana** (para control de flujo)
- **Estado de la conexión** (ESTABLISHED, CLOSING, etc.)

Entonces sí, "conectado" significa que tanto el cliente como el servidor han asignado memoria y recursos para rastrear esta conversación específica. Se conocen entre sí y mantienen esta relación hasta que la conexión se cierra.

## UDP - Sin Conexión

UDP es **sin conexión**. No hay handshake, no hay estado almacenado:

- El cliente simplemente envía un paquete a una IP:puerto
- El servidor lo recibe y lo procesa
- **Ninguna de las partes mantiene información de relación**
- Cada paquete es independiente
- Muy ligero - sin sobrecarga de memoria por "conexión"

## La Diferencia Clave

**TCP:** "Hola, soy el Cliente X. Hablemos. Aquí está mi información, tengo la tuya. Ahora estamos conectados." → **Con estado**

**UDP:** "Aquí hay un paquete para la dirección Y:puerto Z" → Disparar y olvidar → **Sin estado**

Tienes toda la razón en que UDP es mucho más ligero porque no hay estado de conexión que mantener, ni búferes que gestionar, ni acuses de recibo que rastrear. La contrapartida es que TCP proporciona confiabilidad, orden y control de flujo, mientras que UDP proporciona velocidad y simplicidad.