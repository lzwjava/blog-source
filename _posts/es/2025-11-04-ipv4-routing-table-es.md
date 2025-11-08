---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Comprensión de la Salida de la Tabla de Enrutamiento IPv4
translated: true
type: note
---

### Comprendiendo la Salida de `ip route`

Esta es la tabla de enrutamiento IPv4 de tu sistema Linux (probablemente usando el comando `ip` de iproute2). Muestra cómo tu máquina decide a dónde enviar los paquetes según las IPs de destino. Las rutas se emparejan por el prefijo más largo (el más específico primero), y la ruta predeterminada captura todo lo demás.

Desglosaré cada entrada en una tabla para mayor claridad, y luego resumiré lo que significa en general. Esto se relaciona con nuestra conversación anterior: es un ejemplo del mundo real de una tabla de enrutamiento simple con rutas conectadas (subredes locales) y una puerta de enlace predeterminada para internet.

| Destino          | Puerta de Enlace (Siguiente Salto) | Dispositivo | Protocolo | Alcance | IP de Origen | Métrica | Notas |
|------------------|------------------------------------|-------------|-----------|---------|--------------|---------|-------|
| **0.0.0.0/0** (predeterminada) | 192.168.1.1       | enp4s0   | dhcp    | global| (ninguna)       | 100   | Todo el tráfico que no coincida con otras rutas va aquí. Apunta a tu router (probablemente tu puerta de enlace doméstica) en la interfaz Ethernet enp4s0. Descubierta via DHCP. |
| **169.254.0.0/16** | (directo)          | enp4s0   | kernel  | link  | (ninguna)       | 1000  | Rango link-local (APIPA) para auto-configuración cuando DHCP falla. La métrica alta significa que es un respaldo—solo se usa si no hay una ruta mejor. |
| **172.17.0.0/16** | (directo)          | docker0  | kernel  | link  | 172.17.0.1   | (ninguna)| Red bridge por defecto de Docker. "linkdown" significa que la interfaz está inactiva (¿sin contenedores activos?). Tu host actúa como puerta de enlace para esta subred. |
| **172.18.0.0/16** | (directo)          | br-c33e38e216df | kernel | link  | 172.18.0.1   | (ninguna)| Otro bridge de Docker (¿red definida por el usuario?). Activa, por lo que los contenedores en este bridge pueden alcanzar al host via 172.18.0.1. |
| **192.168.1.0/24** | (directo)         | enp4s0   | kernel  | link  | 192.168.1.35 | 100   | Tu subred LAN local. Conectada directamente via enp4s0—los paquetes para otros dispositivos en 192.168.1.x se mantienen locales (ej., para tu router en .1). La IP de tu máquina es 192.168.1.35. |

#### Puntos Clave
- **Rutas Locales/Conectadas**: Las entradas 172.x.x.x y 192.168.1.0/24 son rutas "kernel" para redes conectadas directamente (no se necesita una puerta de enlace de siguiente salto). Esto coincide con la iteración simple que describiste—tu sistema verifica si la IP de destino cae en estos rangos y la envía por el dispositivo correspondiente (ej., enp4s0 para la LAN).
- **Influencia de Docker**: Tienes Docker instalado/en ejecución, creando bridges virtuales (docker0 y br-...). Estos permiten que los contenedores tengan sus propias redes aisladas. El "linkdown" en docker0 sugiere que no hay contenedores usando el bridge por defecto en este momento.
- **Ruta Predeterminada**: Todo lo demás (ej., google.com) va via 192.168.1.1 en enp4s0. La métrica 100 es baja (preferida); la link-local tiene 1000 para despriorizarla.
- **Sin Rutas Remotas**: Esta tabla es básica—no hay protocolos de enrutamiento dinámico (como OSPF) añadiendo entradas para redes distantes. Si haces ping a algo fuera de 192.168.1.0/24, llegará a la ruta predeterminada.

#### Pruebas Rápidas para Verificar
- `ping 192.168.1.1` → Debería usar la ruta local en enp4s0.
- `ping 8.8.8.8` → Usa la ruta predeterminada; traza con `traceroute 8.8.8.8` para ver el camino.
- `ip addr show enp4s0` → Confirma la IP de tu interfaz.
- Si Docker está involucrado: `docker network ls` para listar los bridges.

Si esto es de tu configuración y algo no funciona (ej., ¿sin internet?), soluciones comunes: Verifica el cable/renovación DHCP (`dhclient enp4s0`), o limpia las rutas (`ip route flush cache`). ¿Qué está pasando—solucionando problemas de conectividad, o solo tienes curiosidad por una entrada específica?