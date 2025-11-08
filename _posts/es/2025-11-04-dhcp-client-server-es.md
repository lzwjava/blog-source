---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Roles de Cliente y Servidor DHCP
translated: true
type: note
---

No, es una confusión común, pero DHCP no necesita "ejecutar" lo mismo tanto en el cliente como en el router: es un protocolo cliente-servidor con roles distintos para cada lado. Permíteme explicarlo de forma sencilla.

### Descripción Rápida de DHCP
DHCP (Dynamic Host Configuration Protocol) automatiza la asignación de direcciones IP y otras configuraciones de red (como máscara de subred, puerta de enlace, DNS) a los dispositivos en una red. Elimina la configuración manual.

### Roles en una Configuración Típica
- **Router (o Servidor DHCP)**: Ejecuta el software del **servidor DHCP**. Este es el "jefe" que reparte direcciones IP de un grupo que gestiona. La mayoría de los routers domésticos/de pequeñas oficinas (por ejemplo, de TP-Link, Netgear) lo tienen integrado y activado por defecto.
- **Cliente (por ejemplo, tu portátil, teléfono, PC)**: Ejecuta un **cliente DHCP** (integrado en el sistema operativo, como `dhclient` en Linux o la configuración automática de IP de Windows). Este solicita una IP al servidor pero no sirve IPs a otros.

Ambos lados son esenciales para el handshake, pero no están ejecutando procesos idénticos de "DHCP": uno sirve, el otro solicita.

### Cómo Funciona (Flujo Básico)
1.  **Cliente difunde "DISCOVER"**: Un nuevo dispositivo se une a la red y grita: "¡Eh, alguien tiene una IP para mí?".
2.  **Servidor (router) ofrece "OFFER"**: "Claro, aquí tienes una IP disponible y la configuración".
3.  **Cliente solicita "REQUEST"**: "Me quedo con esa, por favor".
4.  **Servidor confirma "ACK"**: "Hecho: úsala".

Si el servidor DHCP del router está apagado, los clientes podrían necesitar IPs estáticas u otro servidor (por ejemplo, en una configuración con Pi-hole o empresarial).

### Escenarios Comunes

| Configuración | Ubicación del Servidor DHCP | Comportamiento del Cliente |
|---------------|-----------------------------|----------------------------|
| **Red Doméstica** | Router (activado) | Configura todo automáticamente |
| **Sin DHCP en el Router** | IPs manuales/estáticas o servidor externo | El cliente recurre a APIPA (169.254.x.x) si no hay respuesta |
| **Empresa** | Servidor DHCP dedicado (no el router) | Mismo proceso de solicitud del cliente |

Si estás solucionando un problema específico (por ejemplo, "Mi dispositivo no obtiene una IP"), comparte más detalles: ¡puedo ayudar a depurarlo! Para una lectura más profunda, consult el RFC oficial: [RFC 2131: Dynamic Host Configuration Protocol](https://datatracker.ietf.org/doc/html/rfc2131).