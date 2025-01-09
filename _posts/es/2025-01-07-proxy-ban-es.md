---
audio: true
lang: es
layout: post
title: Análisis de la Prohibición del Servidor Proxy
---

## ¿Pueden las API en servidores proxy evitar los bloqueos del Gran Firewall?

Ejecuto un servidor simple en mi instancia de Shadowsocks con el siguiente código:

```python
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
```

```python
app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas
```

```python
@app.route('/bandwidth', methods=['GET'])
def get_bandwidth():
    # Ejecuta el comando vnstat para obtener las estadísticas de tráfico en intervalos de 5 minutos para eth0
    result = subprocess.run(['vnstat', '-i', 'eth0', '-5', '--json'], capture_output=True, text=True)
    data = result.stdout
```

    # Devolver los datos capturados como una respuesta JSON
    return jsonify(data)

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Y uso nginx para servir el puerto 443 como se muestra a continuación:

```bash
server {
    listen 443 ssl;
    server_name www.some-domain.xyz;
```

    ssl_certificate /etc/letsencrypt/live/www.some-domain.xyz/fullchain.pem; # gestionado por 
    # ...
    location / {

```nginx
        proxy_pass http://127.0.0.1:5000/;
        # ...
    }
}
```

Este programa de servidor proporciona datos de red, y utilizo el servidor como mi servidor proxy, lo que me permite mostrar mi estado en línea en mi blog utilizando los datos de la red.

Lo interesante es que el servidor no ha sido bloqueado por el Gran Cortafuegos (GFW) ni por ningún otro sistema de control de red durante varios días. Normalmente, el servidor proxy que configuro sería bloqueado en uno o dos días. El servidor ejecuta un programa de Shadowsocks en un puerto como el 51939, por lo que opera con tráfico de Shadowsocks mezclado con tráfico regular de API. Esta mezcla parece hacer que el GFW crea que el servidor no es un proxy dedicado, sino un servidor normal, evitando que bloquee la IP.

Esta observación es intrigante. Parece que el Gran Cortafuegos (GFW) utiliza una lógica específica para diferenciar el tráfico de proxy del tráfico regular. Aunque muchos sitios web como Twitter y YouTube están bloqueados en China, numerosos sitios web extranjeros, como los de universidades y empresas internacionales, siguen siendo accesibles.

Esto sugiere que el Gran Cortafuegos (GFW) probablemente opera en base a reglas que distinguen entre el tráfico normal HTTP/HTTPS y el tráfico relacionado con proxies. Los servidores que manejan ambos tipos de tráfico parecen evitar bloqueos, mientras que los servidores que manejan únicamente tráfico de proxy tienen más probabilidades de ser bloqueados.

Una pregunta es el rango de tiempo que utiliza el GFW para acumular datos y aplicar bloqueos, ya sea un día o una hora. Durante este período, detecta si el tráfico proviene exclusivamente de un proxy. Si es así, la IP del servidor es bloqueada.

A menudo visito mi blog para revisar lo que he escrito, pero en las próximas semanas, mi enfoque se centrará en otras tareas en lugar de escribir publicaciones en el blog. Esto reducirá mi acceso a la API de `bandwidth` a través del puerto 443. Si descubro que me bloquean nuevamente, debería escribir un programa para acceder regularmente a esta API y engañar al GFW.

Aquí tienes la versión refinada de tu texto con una estructura y claridad mejoradas:

## Cómo funciona el Gran Cortafuegos (GFW).

### Paso 1: Registrar Solicitudes

```python
import time
```

# Base de datos para almacenar datos de solicitudes
request_log = []

# Función para registrar solicitudes
```python
def log_request(source_ip, target_ip, target_port, body):
    request_log.append({
        'source_ip': source_ip,
        'target_ip': target_ip,
        'target_port': target_port,
        'body': body,
        'timestamp': time.time()
    })
```

La función `log_request` registra las solicitudes entrantes con información esencial como la IP de origen, la IP de destino, el puerto de destino, el cuerpo de la solicitud y la marca de tiempo.

### Paso 2: Verificación y bloqueo de IPs

```python
# Función para verificar solicitudes y prohibir IPs
def check_and_ban_ips():
    banned_ips = set()
```

```python
# Iterar sobre todas las solicitudes registradas
for request in request_log:
    if is_illegal(request):
        banned_ips.add(request['target_ip'])
    else:
        banned_ips.discard(request['target_ip'])
```

    # Aplicar prohibiciones a todas las IPs identificadas
    ban_ips(banned_ips)
```

La función `check_and_ban_ips` recorre todas las solicitudes registradas, identificando y bloqueando las IPs asociadas con actividades ilegales.

### Paso 3: Definir qué hace que una solicitud sea ilegal

```python
# Función para simular la verificación de si una solicitud es ilegal
def is_illegal(request):
    # Marcador de posición para la lógica real de verificación de solicitudes ilegales
    # Por ejemplo, verificar el cuerpo de la solicitud o el objetivo
    return "illegal" in request['body']
```

Aquí, `is_illegal` verifica si el cuerpo de la solicitud contiene la palabra "illegal". Esto se puede ampliar a una lógica más sofisticada dependiendo de lo que se considere actividad ilegal.

### Paso 4: Bloquear IPs identificadas

```python
# Función para prohibir una lista de IPs
def ban_ips(ip_set):
    for ip in ip_set:
        print(f"Prohibiendo IP: {ip}")
```

Una vez que se identifican las IPs ilegales, la función `ban_ips` las bloquea imprimiendo sus direcciones IP (o, en un sistema real, podría bloquearlas).

### Paso 5: Método Alternativo para Verificar y Bloquear IPs Basado en un 80% de Solicitudes Ilegales

```python
# Función para verificar solicitudes y prohibir IPs basado en un 80% de solicitudes ilegales
def check_and_ban_ips():
    banned_ips = set()
    illegal_count = 0
    total_requests = 0
```

```python
# Iterar sobre todas las solicitudes registradas
for request in request_log:
    total_requests += 1
    if is_illegal(request):
        illegal_count += 1
```

    # Si el 80% o más de las solicitudes son ilegales, prohibir esas IPs
    if total_requests > 0 and (illegal_count / total_requests) >= 0.8:
        for request in request_log:
            if is_illegal(request):
                banned_ips.add(request['target_ip'])

    # Aplicar prohibiciones a todas las IPs identificadas
    ban_ips(banned_ips)
```

Este método alternativo evalúa si una IP debería ser bloqueada en función del porcentaje de solicitudes ilegales. Si el 80% o más de las solicitudes provenientes de una IP son ilegales, esta es bloqueada.

### Paso 6: Verificación Mejorada de Solicitudes Ilegales (por ejemplo, Detección de Protocolos Shadowsocks y Trojan)

```python
def is_illegal(request):
    # Verificar si la solicitud utiliza el protocolo Shadowsocks (el cuerpo contiene datos similares a binarios)
    if request['target_port'] == 443:
        if is_trojan(request):
            return True
    elif is_shadowsocks(request):
        return True
    return False
```

La función `is_illegal` ahora también verifica protocolos específicos como Shadowsocks y Trojan:
- **Shadowsocks**: Podríamos verificar datos cifrados o similares a binarios en el cuerpo de la solicitud.
- **Trojan**: Si la solicitud llega a través del puerto 443 (HTTPS) y coincide con patrones específicos (por ejemplo, características del tráfico de Trojan), se marca como ilegal.

### Paso 7: Ejemplo de Solicitudes Legales

Por ejemplo, solicitudes como `GET https://some-domain.xyz/bandwidth` son definitivamente legales y no activarán el mecanismo de bloqueo.

### Paso 8: Características del Tráfico del Servidor Proxy

Los servidores proxy tienen características de tráfico muy diferentes en comparación con los servidores web o API regulares. El Gran Cortafuegos (GFW) necesita distinguir entre el tráfico de un servidor web normal y el tráfico de un servidor proxy, ya que pueden parecer completamente distintos.

### Paso 9: Modelos de Aprendizaje Automático e IA para Detección Inteligente

Dada la amplia gama de solicitudes y respuestas que pasan a través de Internet, el Gran Cortafuegos (GFW) podría emplear modelos de inteligencia artificial y aprendizaje automático para analizar patrones de tráfico y detectar de manera inteligente comportamientos ilegales. Al entrenar el sistema con una variedad de tipos de tráfico y utilizando técnicas avanzadas, podría prohibir o filtrar el tráfico de manera más efectiva basándose en los patrones observados.

