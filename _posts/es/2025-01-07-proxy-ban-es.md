---
audio: false
generated: false
image: true
lang: es
layout: post
title: GFW, APIs de Proxy, Detección de VPN
translated: true
type: post
---

### Tabla de Contenidos

1. [¿Pueden las APIs en servidores proxy evitar los bloqueos del GFW?](#¿pueden-las-apis-en-servidores-proxy-evitarlos-bloqueos-del-gfw)
   - Mezclar tráfico de proxy y API evita bloqueos del GFW
   - GFW distingue entre tráfico de proxy y tráfico HTTP/HTTPS normal
   - GFW probablemente bloquea según tráfico exclusivo de proxy
   - GFW utiliza una ventana de tiempo para el análisis de tráfico
   - Acceder regularmente a la API puede evitar la detección

2. [Cómo funciona el Gran Cortafuegos (GFW).](#cómo-funciona-el-gran-cortafuegos-gfw)
   - GFW registra solicitudes con datos de origen y destino
   - Bloquea IPs asociadas con actividades ilegales
   - Utiliza reglas para detectar protocolos específicos
   - Puede bloquear según el porcentaje de solicitudes ilegales
   - Emplea IA para la detección inteligente de patrones de tráfico

3. [Análisis de la detección de VPN en ChatGPT iOS](#análisis-de-la-detecciónde-vpn-en-chatgpt-ios)
   - ChatGPT iOS ahora funciona con algunas VPNs
   - El acceso depende de la ubicación del servidor VPN
   - La detección se basa en direcciones IP específicas
   - Algunas IPs de proveedores en la nube están bloqueadas

---

## ¿Pueden las APIs en servidores proxy evitar los bloqueos del GFW?

Ejecuto un servidor simple en mi instancia de Shadowsocks con el siguiente código:

```python
from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

@app.route('/bandwidth', methods=['GET'])
def get_bandwidth():
    # Ejecutar el comando vnstat para obtener estadísticas de tráfico en intervalos de 5 minutos para eth0
    result = subprocess.run(['vnstat', '-i', 'eth0', '-5', '--json'], capture_output=True, text=True)
    data = result.stdout

    # Devolver los datos capturados como respuesta JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Y uso nginx para servir el puerto 443 como se muestra a continuación:

```bash
server {
    listen 443 ssl;
    server_name www.some-domain.xyz;

    ssl_certificate /etc/letsencrypt/live/www.some-domain.xyz/fullchain.pem; # gestionado por
    # ...
    location / {

        proxy_pass http://127.0.0.1:5000/;
        # ...
    }
}
```

Este programa de servidor proporciona datos de red, y uso el servidor como mi servidor proxy, lo que me permite mostrar mi estado en línea en mi blog utilizando los datos de red.

Lo interesante es que el servidor no ha sido bloqueado por el Gran Cortafuegos (GFW) ni por otros sistemas de control de red en varios días. Normalmente, el servidor proxy que configuro suele ser bloqueado en uno o dos días. El servidor ejecuta un programa Shadowsocks en un puerto como 51939, por lo que opera con tráfico de Shadowsocks mezclado con tráfico normal de API. Esta mezcla parece hacer que el GFW crea que el servidor no es un proxy dedicado, sino un servidor normal, evitando así que bloquee la IP.

Esta observación es intrigante. Parece que el GFW utiliza una lógica específica para diferenciar el tráfico de proxy del tráfico normal. Aunque muchos sitios web como Twitter y YouTube están bloqueados en China, numerosos sitios extranjeros, como los de universidades y empresas internacionales, siguen siendo accesibles.

Esto sugiere que el GFW probablemente opera en función de reglas que distinguen entre el tráfico HTTP/HTTPS normal y el tráfico relacionado con proxy. Los servidores que manejan ambos tipos de tráfico parecen evitar los bloqueos, mientras que los servidores que solo manejan tráfico de proxy tienen más probabilidades de ser bloqueados.

Una pregunta es qué rango de tiempo utiliza el GFW para acumular datos con fines de bloqueo, ya sea un día o una hora. Durante este rango de tiempo, detecta si el tráfico proviene exclusivamente de un proxy. Si es así, la IP del servidor se bloquea.

A menudo visito mi blog para revisar lo que he escrito, pero en las próximas semanas, mi enfoque cambiará a otras tareas en lugar de escribir entradas en el blog. Esto reducirá mi acceso a la API `bandwidth` a través del puerto 443. Si descubro que vuelvo a ser bloqueado, debería escribir un programa para acceder regularmente a esta API y engañar al GFW.

---

## Cómo funciona el Gran Cortafuegos (GFW).

### Paso 1: Registrar solicitudes

```python
import time

# Base de datos para almacenar datos de solicitudes
request_log = []

# Función para registrar solicitudes
def log_request(source_ip, target_ip, target_port, body):
    request_log.append({
        'source_ip': source_ip,
        'target_ip': target_ip,
        'target_port': target_port,
        'body': body,
        'timestamp': time.time()
    })
```

La función `log_request` registra las solicitudes entrantes con información esencial como la IP de origen, IP de destino, puerto de destino, cuerpo de la solicitud y marca de tiempo.

### Paso 2: Verificar y bloquear IPs

```python
# Función para verificar solicitudes y bloquear IPs
def check_and_ban_ips():
    banned_ips = set()

    # Iterar sobre todas las solicitudes registradas
    for request in request_log:
        if is_illegal(request):
            banned_ips.add(request['target_ip'])
        else:
            banned_ips.discard(request['target_ip'])

    # Aplicar bloqueos a todas las IPs identificadas
    ban_ips(banned_ips)
```

La función `check_and_ban_ips` recorre todas las solicitudes registradas, identificando y bloqueando IPs asociadas con actividades ilegales.

### Paso 3: Definir qué hace que una solicitud sea ilegal

```python
# Función para simular la verificación de si una solicitud es ilegal
def is_illegal(request):
    # Marcador de posición para la lógica real de verificación de solicitudes ilegales
    # Por ejemplo, verificar el cuerpo de la solicitud o el destino
    return "illegal" in request['body']
```

Aquí, `is_illegal` verifica si el cuerpo de la solicitud contiene la palabra "illegal". Esto puede expandirse a una lógica más sofisticada según lo que constituya una actividad ilegal.

### Paso 4: Bloquear IPs identificadas

```python
# Función para bloquear una lista de IPs
def ban_ips(ip_set):
    for ip in ip_set:
        print(f"Bloqueando IP: {ip}")
```

Una vez identificadas las IPs ilegales, la función `ban_ips` las bloquea imprimiendo sus direcciones IP (o, en un sistema real, podría bloquearlas).

### Paso 5: Método alternativo para verificar y bloquear IPs según el 80% de solicitudes ilegales

```python
# Función para verificar solicitudes y bloquear IPs según el 80% de solicitudes ilegales
def check_and_ban_ips():
    banned_ips = set()
    illegal_count = 0
    total_requests = 0

    # Iterar sobre todas las solicitudes registradas
    for request in request_log:
        total_requests += 1
        if is_illegal(request):
            illegal_count += 1

    # Si el 80% o más de las solicitudes son ilegales, bloquear esas IPs
    if total_requests > 0 and (illegal_count / total_requests) >= 0.8:
        for request in request_log:
            if is_illegal(request):
                banned_ips.add(request['target_ip'])

    # Aplicar bloqueos a todas las IPs identificadas
    ban_ips(banned_ips)
```

Este método alternativo evalúa si una IP debe ser bloqueada según el porcentaje de solicitudes ilegales. Si el 80% o más de las solicitudes de una IP son ilegales, se bloquea.

### Paso 6: Verificación mejorada de solicitudes ilegales (ejemplo: detección de protocolos Shadowsocks y Trojan)

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
- **Trojan**: Si la solicitud llega a través del puerto 443 (HTTPS) y coincide con patrones específicos (ejemplo: características del tráfico de Trojan), se marca como ilegal.

### Paso 7: Ejemplo de solicitudes legales

Por ejemplo, solicitudes como `GET https://some-domain.xyz/bandwidth` son seguras y no activarán el mecanismo de bloqueo.

### Paso 8: Características del tráfico de servidores proxy

Los servidores proxy tienen características de tráfico muy diferentes en comparación con los servidores web o de API normales. El GFW necesita distinguir entre el tráfico de servidores web normales y el tráfico de servidores proxy, que puede parecer completamente diferente.

### Paso 9: Modelos de IA y aprendizaje automático para detección inteligente

Dado el amplio rango de solicitudes y respuestas que pasan por internet, el GFW podría emplear modelos de IA y aprendizaje automático para analizar patrones de tráfico y detectar de manera inteligente comportamientos ilegales. Al entrenar el sistema con una variedad de tipos de tráfico y utilizando técnicas avanzadas, podría bloquear o filtrar el tráfico de manera más efectiva según los patrones observados.

---

## Actualización

A pesar de mis esfuerzos, mi servidor proxy sigue siendo bloqueado. Para mitigar esto, he implementado una solución alternativa utilizando la función de IP invertida de Digital Ocean, que me permite asignar rápidamente una nueva dirección IP cada vez que ocurre un bloqueo.

---

## Análisis de la detección de VPN en ChatGPT iOS

*26.12.2024*

Hoy descubrí que la aplicación ChatGPT iOS ahora permite iniciar sesión con una VPN en China. Anteriormente, mostraba un mensaje de bloqueo, como el que se muestra a continuación.

Sin embargo, a partir de hoy, funciona bien con una VPN.

Recuerdo que cuando se lanzó por primera vez la aplicación ChatGPT iOS, usarla con una VPN no era un problema. Más tarde, la detección de VPN se volvió más estricta, lo que dificultaba el inicio de sesión. Afortunadamente, parece que esta restricción se ha relajado recientemente.

Tras realizar más pruebas, descubrí que al usar una VPN de la región de Singapur de DigitalOcean, no podía acceder a la aplicación. Sin embargo, al usar VPNs de Taiwán o el Reino Unido (proporcionadas por https://zhs.cloud), funcionaba perfectamente.

Parece que la detección de VPN en ChatGPT iOS se basa en direcciones IP específicas. Algunos proveedores de servicios en la nube o ciertas direcciones IP están bloqueadas, lo que podría explicar el comportamiento inconsistente según la ubicación del servidor VPN.

![](assets/images/chatgpt/block.jpg){: .responsive }

![](assets/images/chatgpt/c1.png){: .responsive }