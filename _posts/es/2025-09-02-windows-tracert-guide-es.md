---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de Diagnóstico de Ruta de Red con Tracert de Windows
translated: true
type: note
---

En Windows, **`tracert`** (abreviatura de *trace route*, traza de ruta) es una herramienta de diagnóstico de línea de comandos utilizada para rastrear la ruta que toman los paquetes desde tu computadora hasta un host de destino (como un sitio web o una dirección IP). Se usa principalmente para identificar dónde ocurren retrasos o problemas de conexión en una ruta de red.

Así es cómo funciona paso a paso:

### 1. Solicitudes de Eco ICMP con TTL Incremental

* `tracert` envía **paquetes de Solicitud de Eco ICMP** (similar a `ping`).
* Manipula el campo **Time-To-Live (TTL)** en la cabecera IP.
* El TTL comienza en 1 y luego aumenta (2, 3, 4, …) con cada prueba.

### 2. Expiración del TTL y Respuestas de "Tiempo Excedido"

* Cuando un router recibe un paquete, decrementa el TTL en 1.
* Si el TTL llega a **0**, el router descarta el paquete y devuelve un mensaje **ICMP Time Exceeded** al remitente.
* Esto le permite a `tracert` conocer la identidad (IP/nombre de host) de ese router.

### 3. Construyendo la Ruta

* Para TTL = 1, ves el primer salto (tu puerta de enlace predeterminada).
* Para TTL = 2, ves el siguiente router, y así sucesivamente.
* Esto continúa hasta que:

  * El host de destino responde con una **Respuesta de Eco ICMP**, o
  * Se alcanza el límite máximo de saltos (por defecto 30).

### 4. Midiendo la Latencia

* `tracert` envía **tres pruebas** por salto (por defecto).
* Muestra el **tiempo de ida y vuelta (RTT)** en milisegundos para cada prueba.
* Si un router no responde, verás `*` en lugar de un tiempo.

### 5. Ejemplo de Salida

```text
Trazando la ruta a example.com [93.184.216.34]
sobre un máximo de 30 saltos:

  1     1 ms    <1 ms     1 ms  192.168.1.1
  2    10 ms     9 ms    11 ms  isp-gateway.example.net [203.0.113.1]
  3    25 ms    23 ms    24 ms  core-router.example.net [198.51.100.1]
  ...
  8    45 ms    46 ms    47 ms  example.com [93.184.216.34]
```

### 6. Notas sobre el Comportamiento

* Algunos routers pueden bloquear o despriorizar las respuestas ICMP, causando `* * *`.
* `tracert` en **Windows** usa Solicitudes de Eco ICMP, mientras que `traceroute` en Linux/Unix a menudo usa **sondas UDP** (aunque puede cambiarse).
* Los firewalls o el filtrado del ISP a veces pueden ocultar partes de la ruta.

---

👉 ¿Quieres que también explique **cómo interpretar casos como `* * *` o grandes retardos** en un resultado de `tracert`, para que puedas usarlo para una solución de problemas real?