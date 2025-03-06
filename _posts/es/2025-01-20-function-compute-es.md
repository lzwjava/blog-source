---
audio: false
generated: false
lang: es
layout: post
title: Función Compute en Alibaba Cloud
translated: true
---

Estoy utilizando Function Compute de Alibaba Cloud para generar tráfico que parezca normal, lo cual ayuda a ocultar la actividad de mi servidor proxy del GFW. He desplegado un servidor de ancho de banda junto a mi proxy, y esta función de Function Compute hace una solicitud a la API de ancho de banda cada minuto. Esto crea una mezcla de tráfico normal y de proxy.

```python
from flask import Flask, request, jsonify
import requests
import concurrent.futures

REQUEST_ID_HEADER = 'x-fc-request-id'

app = Flask(__name__)

# Función para llamar a la API externa
def call_bandwidth_api():
    try:
        response = requests.get('https://www.lzwjava.xyz/bandwidth')
        response.raise_for_status()  # Lanza una excepción para errores HTTP
        return True  # Indica éxito
    except Exception as e:
        print("Error al obtener datos de ancho de banda:", e)
        return False  # Indica fallo

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world(path):
    # Registra el ID de la solicitud y otros detalles
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    data = request.stream.read()
    print("Path: " + path)
    print("Data: " + str(data))

    # Inicializa contadores
    total_calls = 10  # Número total de llamadas a la API a realizar
    successful_calls = 0  # Seguimiento de llamadas exitosas a la API

    # Usa ThreadPoolExecutor para llamar a la API 10 veces concurrentemente
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Envía tareas al ejecutor
        futures = [executor.submit(call_bandwidth_api) for _ in range(total_calls)]

        # Espera a que todas las tareas se completen y cuenta los éxitos
        for future in concurrent.futures.as_completed(futures):
            if future.result():  # Si la llamada fue exitosa
                successful_calls += 1

    # Registra el final de la solicitud
    print("FC Invoke End RequestId: " + rid)

    # Devuelve el número de llamadas y llamadas exitosas
    return jsonify({
        "message": "Hello, World!",
        "total_calls": total_calls,
        "successful_calls": successful_calls
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
```