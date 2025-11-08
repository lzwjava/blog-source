---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Cómo funciona el enrutamiento de Internet
translated: true
type: note
---

Sí, tienes toda la razón con el flujo de alto nivel: una vez que tu computadora tiene la dirección IP (como 106.63.15.9 para weibo.com), inicia una conexión que salta a través de tu red local, tu router, la infraestructura de tu ISP y a través de los routers interconectados de internet ("capa por capa") hasta llegar al servidor de destino. Todo esto es manejado automáticamente por la pila de protocolos TCP/IP, sin que tú hagas nada manual más allá de escribir la URL o ejecutar un comando como `ping`.

Lo desglosaré paso a paso, vinculando tu salida de `ping` y `traceroute` para contextualizar. Lo mantendré práctico y centrado en lo que sucede bajo el capó, asumiendo una configuración típica como la tuya (Mac en Wi-Fi/Ethernet detrás de un router).

### 1. **Resolución DNS (Obteniendo la IP)**
   - Antes de cualquier conexión, tu computadora primero traduce el nombre de dominio (ej. "weibo.com") a una IP a través del DNS (Sistema de Nombres de Dominio). Esto sucede mediante el resolvedor DNS de tu SO, que consulta servidores DNS públicos (como 8.8.8.8 de Google).
   - En tu caso, `ping weibo.com` automáticamente hace esta resolución, confirmando 106.63.15.9 como la dirección IPv4. (Nota: Los proxies como el tuyo local en 127.0.0.1:7890 típicamente manejan tráfico HTTP/HTTPS, pero `ping` usa IP/ICMP crudo, por lo que evita el proxy).
   - Si el DNS falla, no hay conexión—todo se detiene aquí.

### 2. **Tu Computadora Prepara el Paquete (Lado Local)**
   - Una vez que tiene la IP, tu Mac construye un **paquete** (un fragmento de datos) usando las capas TCP/IP:
     - **Capa de Aplicación**: El comando o aplicación (ej. navegador o `ping`) solicita datos. `Ping` envía una "solicitud de eco" ICMP (un simple mensaje "oye, ¿estás ahí?").
     - **Capa de Transporte**: Añade cabeceras TCP/UDP (para confiabilidad/números de puerto) o ICMP para ping. Tus pings usan ICMP, con 56 bytes de datos + cabeceras = paquetes de 64 bytes.
     - **Capa de Red (IP)**: Lo envuelve en una cabecera IP con origen (tu IP local, como 192.168.1.x) y destino (106.63.15.9). Aquí es donde comienzan las decisiones de enrutamiento.
     - **Capa de Enlace (Ethernet/Wi-Fi)**: Añade direcciones MAC para el salto en la red local. Tu computadora usa ARP (Protocolo de Resolución de Direcciones) para encontrar la dirección MAC del router.
     - **Capa Física**: Convierte a señales eléctricas a través de tu cable/Wi-Fi.
   - Tu computadora sabe que no puede alcanzar 106.63.15.9 directamente (no está en tu subred local 192.168.1.0/24), por lo que envía el paquete a la **puerta de enlace predeterminada**—tu router en 192.168.1.1.

### 3. **Salto Local: Computadora → Router**
   - Este es el primer (y más rápido) paso, mostrado en tu salida de `traceroute`:
     ```
     1  192.168.1.1 (192.168.1.1) 26.903 ms 3.150 ms 3.161 ms
     ```
     - `Traceroute` (que envía paquetes con TTL—Time To Live—creciente para mapear la ruta) confirma que este salto toma ~3-27ms de ida y vuelta.
     - Tu router recibe el paquete, elimina la cabecera Ethernet local y lo re-encapsula para el siguiente salto. Utiliza su tabla de enrutamiento para reenviarlo hacia internet (vía su conexión WAN/ISP).
     - Los proxies no afectan esto—tu proxy local (puerto 7890) es solo para tráfico a nivel de aplicación como navegación web, no para enrutamiento IP crudo.

### 4. **Router → ISP → Red Troncal de Internet (El Enrutamiento "Capa por Capa")**
   - Tu router se conecta a tu ISP (ej. vía PPPoE, DHCP o módem) y entrega el paquete al router de borde del ISP. Esto podría implicar NAT (Traducción de Direcciones de Red) en tu router, intercambiando tu IP privada (192.168.1.x) por la IP pública asignada por tu ISP.
   - Desde aquí, es una cadena de **routers** a través de internet:
     - **Routers del ISP**: Tu ISP (ej. Comcast o China Telecom) lo enruta a través de su red central. Cada router decrementa el TTL (comienza en 64 en tu traceroute) y reenvía basándose en tablas BGP (Border Gateway Protocol)—esencialmente un mapa global de la mejor ruta a 106.63.15.9.
     - **Saltos entre ISPs/Red Troncal**: Los paquetes cruzan "puntos de interconexión" entre ISPs (ej. vía cables submarinos, fibra óptica). Esto podrían ser 5-20 saltos en total, dependiendo de la geografía. La IP de Weibo.com (106.63.15.9) está en China, así que desde tu ubicación (suponiendo EE. UU./UE basado en el proxy), iría a través de rutas trans-Pacífico.
     - Cada salto es un router que inspecciona la cabecera IP, decide la siguiente puerta de enlace y reenvía. Ningún dispositivo individual conoce la ruta completa—es distribuido.
   - Tu `traceroute` se cortó (probablemente suspendido con ^Z), pero si lo ejecutaras completamente, verías 10-15 líneas más como:
     ```
     2  [IP del router del ISP] 10 ms ...
     3  [Núcleo del ISP] 15 ms ...
     ...
     15  106.63.15.9  40 ms ...
     ```
     - Los tiempos se suman: Tus pings muestran ~40ms de RTT total (tiempo de ida y vuelta), así que el viaje de ida al servidor es de ~20ms.

### 5. **El Servidor de Destino Recibe y Responde**
   - El paquete llega al servidor de Weibo (o a un balanceador de carga en 106.63.15.9). Revierte el proceso: Responde con una respuesta de eco ICMP (para ping) o un TCP SYN-ACK (para una conexión web).
   - La respuesta sigue una ruta similar de regreso, a menudo la misma ruta pero no siempre (el enrutamiento de internet es asimétrico).
   - Tu `ping` confirma el éxito: TTL=52 significa ~12 saltos (64-52=12), y la latencia de 40ms coincide con un viaje de ida y vuelta China-EE. UU.

### Por Qué Se Siente "Mágico" (y Problemas Comunes)
- **Automatización**: Tu SO/kernel maneja todo esto a través de la pila de red (ej. `ifconfig` o `ip route` muestra tus rutas). No se necesita configuración manual a menos que estés depurando.
- **Tu Proxy**: Es transparente para ping/traceroute pero interceptaría el tráfico del navegador a weibo.com, enrutándolo a través de 127.0.0.1:7890 (probablemente para evitar VPN/censura). Desactívalo con `unset HTTP_PROXY HTTPS_PROXY` si pruebas en crudo.
- **Si Falla**: Firewalls, discrepancias de MTU o agujeros negros en la ruta pueden descartar paquetes. Herramientas como `tcpdump` o Wireshark te permiten rastrear esto localmente.
- **Nota de Seguridad**: Las IPs pueden cambiar (TTL de DNS), y HTTPS añade encriptación sobre esto (negociación TLS después de la conexión TCP).

En resumen, sí—computadora → router → ISP → malla global de routers → servidor. Es un sistema distribuido hermosamente construido sobre el enrutamiento IP. Si compartes un traceroute completo o quieres profundizar en una parte específica (ej. negociación TCP para web), ¡avísame!

[TCP/IP Illustrated (Libro sobre Conceptos Básicos de Redes)](https://www.oreilly.com/library/view/tcp-ip-illustrated-volume/0201633469/)  
[Cómo Funciona Traceroute (Explicación de Cloudflare)](https://www.cloudflare.com/learning/network-layer/what-is-traceroute/)