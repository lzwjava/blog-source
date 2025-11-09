---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Registros DHCP para la Interfaz WAN del Router
translated: true
type: note
---

### Comprender las entradas del registro DHCP en el router 360 Wi-Fi T7

Este fragmento del registro de su router 360 T7 (probablemente extraído de la sección **Sistema > Registro** en la interfaz web) muestra a la interfaz WAN del router actuando como un cliente DHCP para obtener y renovar su dirección IP pública del servidor DHCP de su ISP. DHCP (Protocolo de configuración dinámica de host) es el protocolo estándar para asignar direcciones IP automáticamente en las redes. El router solicita o renueva periódicamente una concesión de IP para mantener la conectividad a Internet—normalmente cada 12-24 horas, dependiendo del tiempo de concesión de su ISP.

Estas entradas son **normales e indican un funcionamiento correcto**, no un error. Representan el proceso estándar DORA (Discover, Offer, Request, ACK) para la asignación inicial de IP, seguido de renovaciones de concesión. Aquí tiene un desglose de cada línea en orden cronológico (nota: las marcas de tiempo están en orden inverso en su registro, pero las he reordenado para mayor claridad; las fechas están en formato AAAA/MM/DD-HH:MM:SS):

| ID de Registro | Marca de tiempo      | Mensaje                 | Explicación |
|----------------|----------------------|-------------------------|-------------|
| 148   | 2025/09/19-03:44:57 | Enviando DHCP discover  | El router transmite un mensaje **DHCP Discover** en el lado WAN para localizar un servidor DHCP disponible (el de su ISP). Este es el primer paso cuando la concesión expira o el router se reinicia. (Reintenta rápidamente en la siguiente línea). |
| 147   | 2025/09/19-03:45:00 | Enviando DHCP discover  | Un reintento del mensaje Discover (común si no hay respuesta inmediata; los routers envían 2-4 reintentos con retroceso exponencial). |
| 146   | 2025/09/19-03:45:02 | DHCP offer Received     | El servidor DHCP del ISP responde con una **DHCP Offer**, proponiendo una dirección IP disponible, máscara de subred, gateway, servidores DNS y duración de la concesión (ej., 24 horas). |
| 145   | 2025/09/19-03:45:02 | Sending DHCP request    | El router envía un **DHCP Request** para aceptar la IP ofrecida y solicitar formalmente al servidor que la asigne (se transmite para que otros servidores puedan retirar sus ofertas si las hay). |
| 144   | 2025/09/19-03:45:02 | DHCP ACK received       | El servidor envía un **DHCP ACK** (Acuse de recibo), confirmando la asignación de la IP. El router ahora tiene una IP WAN válida y puede conectarse a Internet. Esto completa la adquisición inicial de la concesión (~5 segundos en total aquí). |
| 143   | 2025/09/19-15:45:02 | Sending DHCP renew      | ~12 horas después (a la mitad de una concesión típica de 24 horas), el router envía proactivamente un **DHCP Renew** (un Request unicast al servidor conocido) para extender la concesión sin un redescubrimiento completo. |
| 142   | 2025/09/19-15:45:02 | DHCP ACK received       | El servidor reconoce la renovación—la concesión se extendió sin problemas. |
| 141   | 2025/09/20-03:45:02 | Sending DHCP renew      | Otra renovación ~12 horas después (ya en el día siguiente). Si no sigue un ACK (no se muestra aquí), podría escalar a un rebind completo o redescubrimiento. |

#### Por qué sucede esto
- **Ciclo de Concesión**: Los ISP establecen tiempos de concesión (ej., 24 horas). Al 50% transcurrido, el cliente renueva para evitar interrupciones. Si la renovación falla al 87.5%, hace un rebind (Request de difusión); al 100%, reinicia el proceso DORA completo.
- **En el Contexto del 360 T7**: Esto se registra bajo eventos de conexión WAN. El T7 utiliza un cliente DHCP ligero (probablemente basado en udhcpc) en su firmware, que genera estos mensajes exactos. No hay problemas a menos que vea fallos como "DHCP NAK received" (IP rechazada) o Discovers repetidos sin ACKs (podría indicar problemas del ISP o del cable).
- **Consejos para la Resolución de Problemas**:
  - Si Internet se cae alrededor de estos momentos, verifique el estado de la WAN en la interfaz de usuario (**Estado > WAN**) para ver cambios de IP o errores.
  - Exporte los registros completos a través de la interfaz de usuario para identificar patrones.
  - Para forzar una renovación: Libere/renueve la WAN en **Red > WAN** o reinicie el router.

Este es un comportamiento rutinario: su router simplemente está manteniendo válido su "boleto de Internet".

[Understanding DHCP Basics (Microsoft)](https://learn.microsoft.com/en-us/windows-server/troubleshoot/dynamic-host-configuration-protocol-basics)  
[DHCP Process Overview (Netmanias)](https://www.netmanias.com/en/post/techdocs/5998/dhcp-network-protocol/understanding-the-basic-operations-of-dhcp)