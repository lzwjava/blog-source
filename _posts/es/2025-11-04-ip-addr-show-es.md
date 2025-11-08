---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Comprender la Salida de ip addr show enp4s0
translated: true
type: note
---

### Desglosando la salida de `ip addr show enp4s0`

Este comando muestra información detallada de tu interfaz Ethernet (enp4s0), que es la que maneja tu conexión LAN local según la tabla de enrutamiento que discutimos. Está activa y funcionando sin problemas—ideal para conectividad básica. La analizaré línea por línea y luego resumiré.

#### Secciones Clave Explicadas
- **Estado de la Interfaz**:  
  `2: enp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000`  
  - Índice 2 (segunda interfaz, después de lo).  
  - Banderas: Soporta broadcast/multicast, completamente UP (enlace detectado y operativo).  
  - MTU: 1500 bytes (tamaño de trama Ethernet estándar—sin jumbo frames).  
  - Disciplina de cola: fq_codel (fair queuing para tráfico de baja latencia, común en Linux moderno).  
  - Estado: UP (lista para enviar/recibir).

- **Capa de Enlace (Dirección MAC)**:  
  `link/ether 04:7c:16:d9:54:5b brd ff:ff:ff:ff:ff:ff`  
  - Tu MAC de hardware: 04:7c:16:d9:54:5b (única para esta NIC).  
  - Broadcast: ff:ff:ff:ff:ff:ff (todos unos para broadcasts Ethernet).

- **Dirección IPv4**:  
  `inet 192.168.1.35/24 brd 192.168.1.255 scope global dynamic noprefixroute enp4s0`  
  `valid_lft 4790sec preferred_lft 4790sec`  
  - IP: 192.168.1.35 con subred /24 (máscara 255.255.255.0). Coincide con el "src 192.168.1.35" en tu tabla de rutas.  
  - Broadcast: 192.168.1.255 (para broadcasts en toda la subred).  
  - Alcance: global (enrutable más allá de este host).  
  - Dinámica: Asignada via DHCP (desde tu router en 192.168.1.1).  
  - Sin ruta de prefijo: No añade automáticamente una ruta conectada (pero el kernel lo hizo de todos modos, como se ve en `ip route`).  
  - Arrendamiento: ~79 minutos restantes (4790 segundos) antes de la renovación.

- **Dirección IPv6**:  
  `inet6 fe80::a884:a0f6:e8b4:4a7d/64 scope link noprefixroute`  
  `valid_lft forever preferred_lft forever`  
  - IPv6 link-local: fe80::... (generada automáticamente desde la MAC; solo para comunicación de enlace local, como neighbor discovery).  
  - Prefijo /64, alcance link (no enrutable fuera de esta interfaz).  
  - Permanente (sin expiración).

#### Tabla Resumen Rápida

| Aspecto       | Valor/Detalles                  | Qué Significa |
|--------------|--------------------------------|---------------|
| **Estado**  | UP, MTU 1500                  | La interfaz está activa y manejando paquetes estándar. |
| **MAC**     | 04:7c:16:d9:54:5b             | La dirección de hardware de tu dispositivo en el cable. |
| **IPv4**    | 192.168.1.35/24 (DHCP)        | IP LAN local; las rutas a esta subred se mantienen en enp4s0. |
| **IPv6**    | fe80::a884:a0f6:e8b4:4a7d/64  | IPv6 solo local; útil para funciones IPv6 de vecinos. |
| **Arrendamiento**   | ~79 min restantes                  | DHCP se renovará pronto—verifica con `dhclient -r enp4s0 && dhclient enp4s0` si es necesario. |

Esta configuración explica por qué tu ruta por defecto apunta aquí para acceso a internet y por qué el tráfico local 192.168.1.x es directo. Si haces ping dentro de la LAN, hará ARP para la MAC y enviará tramas por esta interfaz.

¿Todo parece correcto, o hay algún problema (por ejemplo, sin dirección IPv6 global, o caídas de conectividad)? Si compartes `ip addr` para otras interfaces o resultados de `ping`, puedo profundizar más. ¿Qué sigue—probando bridges de Docker, o algo más?