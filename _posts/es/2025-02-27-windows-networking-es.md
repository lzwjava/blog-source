---
audio: false
generated: true
lang: es
layout: post
title: Comandos de Red de Windows
translated: true
type: note
---

Adentrémonos en algunos comandos útiles de redes para Windows que puedes ejecutar en el Símbolo del sistema (CMD) para solucionar problemas, recopilar información o administrar tu red. Explicaré algunos populares como `getmac` y mencionaré otros que podrían ser útiles. No necesitas ser un experto en tecnología; son bastante sencillos una vez que les coges el truco.

Primero, para usar estos comandos, abre el Símbolo del sistema: presiona `Tecla Windows + R`, escribe `cmd` y pulsa Enter. Bastante fácil, ¿verdad?

### 1. `getmac` - Encuentra tu dirección MAC
El comando `getmac` muestra la dirección de Control de Acceso al Medio (MAC) de tus adaptadores de red—esos identificadores únicos para tu dispositivo en una red. Así es como funciona:

- Escribe `getmac` y presiona Enter.
- Verás una lista de direcciones MAC para cada adaptador de red (como Ethernet o Wi-Fi).
- Añade el modificador `-v` (`getmac -v`) para el modo detallado, que proporciona información extra como el nombre del adaptador y el tipo de transporte (por ejemplo, Ethernet o Wireless).

Un ejemplo de salida podría verse así:
```
Dirección física     Nombre de transporte
=================== ==========================================================
00-14-22-01-23-45   \Device\Tcpip_{12345678-ABCD-1234-EF56-7890ABCDEF12}
```
La "Dirección física" es tu MAC. Es útil para solucionar problemas de red o configurar el filtrado MAC en un router.

### 2. `ipconfig` - Comprueba tu configuración IP
Este es un comando esencial para obtener información de la red:
- Escribe `ipconfig` y pulsa Enter para ver detalles básicos como tu dirección IP, máscara de subred y puerta de enlace predeterminada.
- Usa `ipconfig /all` para un desglose completo, que incluye servidores DNS, estado DHCP y—sí—de nuevo tu dirección MAC.

Es ideal para averiguar si tu dispositivo está correctamente conectado o si hay un conflicto de IP.

### 3. `ping` - Prueba la conectividad
¿Quieres comprobar si puedes alcanzar otro dispositivo o sitio web?
- Escribe `ping [dirección]` (por ejemplo, `ping google.com` o `ping 8.8.8.8`).
- Envía algunos paquetes y te indica si regresan, además de cuánto tiempo tardan (en milisegundos).

Si obtienes "Solicitud agotó el tiempo de espera", algo está bloqueando la conexión—podría ser un firewall, un servidor caído o tu propia red.

### 4. `tracert` - Traza la ruta
Abreviatura de "trace route", muestra la ruta que toman tus datos hacia un destino:
- Escribe `tracert [dirección]` (por ejemplo, `tracert google.com`).
- Enumera cada salto (router o servidor) en el camino, con los tiempos de respuesta.

Útil para detectar dónde se ralentiza o falla una conexión.

### 5. `netstat` - Ve la actividad de la red
Este es para comprobar qué está pasando en tu red en este momento:
- Escribe `netstat -a` para ver todas las conexiones activas y los puertos en escucha.
- Añade `-n` (`netstat -an`) para mostrar direcciones IP en lugar de nombres de host—más rápido y en bruto.

Es como una ventana a con qué está hablando tu computadora—útil para detectar actividad sospechosa.

### 6. `nslookup` - Investiga el DNS
Si los sitios web no cargan, esto comprueba la resolución del Sistema de Nombres de Dominio (DNS):
- Escribe `nslookup [dominio]` (por ejemplo, `nslookup google.com`).
- Devuelve la dirección IP asociada a ese dominio, mostrando si tu DNS funciona.

### Consejos para que sea más fluido
- Ejecuta CMD como Administrador (haz clic derecho en Símbolo del sistema > "Ejecutar como administrador") si un comando necesita privilegios elevados.
- Combina comandos con `|` (pipe) para filtrar—por ejemplo, `getmac | find "00-14"` para buscar una MAC específica.
- Si estás atascado, escribe `[comando] /?` (por ejemplo, `ipconfig /?`) para obtener ayuda sobre ese comando.

Estas son tus herramientas básicas para indagar en una red Windows. ¿Quieres centrarte en una—como `getmac`—o probar algo específico? ¡Dime qué estás intentando hacer!