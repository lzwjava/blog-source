---
audio: true
generated: false
lang: es
layout: post
title: Comandos de Red de Windows
translated: true
---

Vamos a sumergirnos en algunos comandos útiles de red de Windows que puedes ejecutar en el Símbolo del sistema (CMD) para solucionar problemas, recopilar información o gestionar tu red. Explicaré algunos populares como `getmac` y añadiré otros que podrían ser útiles. No necesitas ser un experto en tecnología; estos son bastante sencillos una vez que les coges el tranquillo.

Primero, para usar estos comandos, abre el Símbolo del sistema: presiona `Windows Key + R`, escribe `cmd` y pulsa Enter. ¿Fácil, verdad?

### 1. `getmac` - Encuentra tu Dirección MAC
El comando `getmac` muestra la dirección de Control de Acceso a Medios (MAC) de tus adaptadores de red, esos identificadores únicos para tu dispositivo en una red. Aquí te explico cómo funciona:

- Escribe `getmac` y presiona Enter.
- Verás una lista de direcciones MAC para cada adaptador de red (como Ethernet o Wi-Fi).
- Añade el interruptor `-v` (`getmac -v`) para el modo detallado, que proporciona detalles adicionales como el nombre del adaptador y el tipo de transporte (por ejemplo, Ethernet o Inalámbrico).

El resultado podría verse así:
```
Dirección Física    Nombre de Transporte
=================== ==========================================================
00-14-22-01-23-45   \Device\Tcpip_{12345678-ABCD-1234-EF56-7890ABCDEF12}
```
La “Dirección Física” es tu MAC. Útil para solucionar problemas de red o configurar el filtrado MAC en un router.

### 2. `ipconfig` - Verifica tu Configuración IP
Este es un comando básico para obtener información de red:
- Escribe `ipconfig` y pulsa Enter para ver detalles básicos como tu dirección IP, máscara de subred y puerta de enlace predeterminada.
- Usa `ipconfig /all` para un desglose completo, incluyendo servidores DNS, estado DHCP y, sí, tu dirección MAC de nuevo.

Es ideal para averiguar si tu dispositivo está correctamente conectado o si hay un conflicto de IP.

### 3. `ping` - Prueba la Conectividad
¿Quieres comprobar si puedes llegar a otro dispositivo o sitio web?
- Escribe `ping [dirección]` (por ejemplo, `ping google.com` o `ping 8.8.8.8`).
- Envía unos paquetes y te dice si vuelven, además del tiempo que tardan (en milisegundos).

Si obtienes “Solicitud de tiempo agotado”, algo está bloqueando la conexión; podría ser un firewall, un servidor inactivo o tu propia red.

### 4. `tracert` - Rastrear la Ruta
Abreviatura de "rastrear ruta", esto muestra el camino que toma tu datos hasta un destino:
- Escribe `tracert [dirección]` (por ejemplo, `tracert google.com`).
- Lista cada salto (router o servidor) en el camino, con tiempos de respuesta.

Es útil para detectar dónde se ralentiza o falla una conexión.

### 5. `netstat` - Ver Actividad de Red
Este es para ver qué está pasando en tu red en este momento:
- Escribe `netstat -a` para ver todas las conexiones activas y puertos en escucha.
- Añade `-n` (`netstat -an`) para mostrar direcciones IP en lugar de nombres de host; más rápido y más crudo.

Es como una ventana a lo que está hablando tu computadora; útil para detectar actividad sospechosa.

### 6. `nslookup` - Investigar DNS
Si los sitios web no se cargan, esto verifica la resolución del Sistema de Nombres de Dominio (DNS):
- Escribe `nslookup [dominio]` (por ejemplo, `nslookup google.com`).
- Devuelve la dirección IP asociada a ese dominio, mostrando si tu DNS está funcionando.

### Consejos para Hacerlo Más Suave
- Ejecuta CMD como Administrador (haz clic derecho en Símbolo del sistema > “Ejecutar como administrador”) si un comando necesita privilegios más altos.
- Combina comandos con `|` (tubería) para filtrar; por ejemplo, `getmac | find "00-14"` para buscar una MAC específica.
- Si te atascas, escribe `[comando] /?` (por ejemplo, `ipconfig /?`) para obtener ayuda sobre ese comando.

Estas son tus herramientas esenciales para explorar una red de Windows. ¿Quieres centrarte en una, como `getmac`, o probar algo específico? ¡Hazme saber a qué apuntas!