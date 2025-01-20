---
audio: true
lang: es
layout: post
title: Function Compute en Alibaba Cloud
translated: true
---

He configurado una función utilizando el servicio Function Compute de Alibaba Cloud. Mi objetivo es generar un tráfico que parezca normal para ayudar a ocultar la actividad de mi servidor proxy del Gran Firewall (GFW). Para lograr esto, he desplegado un servidor de ancho de banda junto a mi proxy. Ahora, estoy utilizando Function Compute de Alibaba Cloud para hacer una solicitud a esta API de ancho de banda cada minuto, creando una mezcla de tráfico normal y de proxy.

```python
from flask import Flask, request, jsonify
import requests
import time

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # Registrar el ID de la solicitud y otros detalles
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    data = request.stream.read()
    print("Path: " + path)
    print("Data: " + str(data))

    # Inicializar contadores
    start_time = time.time()  # Registrar el tiempo de inicio
    duration = 60  # Ejecutar durante 1 minuto (60 segundos)
    total_calls = 0  # Seguimiento del total de llamadas API
    successful_calls = 0  # Seguimiento de las llamadas API exitosas

    # Bucle durante 1 minuto
    while time.time() - start_time < duration:
        try:
            # Llamar a la API externa /bandwidth
            response = requests.get('https://www.lzwjava.xyz/bandwidth')
            response.raise_for_status()  # Lanzar una excepción para errores HTTP
            successful_calls += 1  # Incrementar el contador de llamadas exitosas
        except Exception as e:
            print("Error al obtener datos de ancho de banda:", e)
        finally:
            total_calls += 1  # Incrementar el contador de llamadas totales

        # Esperar 5 segundos antes de la siguiente solicitud
        time.sleep(5)

    # Registrar el final de la solicitud
    print("FC Invoke End RequestId: " + rid)

    # Devolver el número de llamadas y llamadas exitosas
    return jsonify({
        "message": "Hello, World!",
        "total_calls": total_calls,
        "successful_calls": successful_calls
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```