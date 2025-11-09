---
audio: false
generated: true
image: false
lang: es
layout: post
model: mistralai/mistral-medium-3.1
title: Truncar objetos JSON de manera eficiente
translated: true
type: note
---

Para truncar las primeras `n` claves de un objeto JSON (ya sea un array o un mapa), puedes utilizar el siguiente enfoque. Esto es particularmente útil cuando se trabaja con respuestas JSON grandes que necesitan ser truncadas debido a límites de contexto, como cuando se utiliza un LLM (Language Model) para generar casos de prueba.

Aquí hay una función en Python que demuestra cómo truncar las primeras `n` claves de un objeto JSON:

```python
import json

def truncate_json(json_obj, n):
    if isinstance(json_obj, list):
        # Truncar los primeros n elementos de la lista
        return json_obj[n:]
    elif isinstance(json_obj, dict):
        # Truncar las primeras n claves del diccionario
        keys = list(json_obj.keys())
        for key in keys[:n]:
            del json_obj[key]
        return json_obj
    else:
        return json_obj

# Ejemplo de uso
json_str = '''
{
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
'''

json_obj = json.loads(json_str)
n = 2  # Número de claves a truncar

truncated_json = truncate_json(json_obj, n)
print(json.dumps(truncated_json, indent=4))
```

### Explicación

1.  **Definición de la función**: La función `truncate_json` toma un objeto JSON y un entero `n` como entrada.
2.  **Manejo de listas**: Si el objeto JSON es una lista, devuelve una nueva lista con los primeros `n` elementos eliminados.
3.  **Manejo de diccionarios**: Si el objeto JSON es un diccionario, elimina las primeras `n` claves del diccionario.
4.  **Ejemplo de uso**: El ejemplo demuestra cómo usar la función con un objeto JSON de ejemplo.

### Salida del ejemplo

Para el objeto JSON de ejemplo dado y `n = 2`, la salida será:

```json
{
    "key3": "value3",
    "key4": "value4",
    "key5": "value5"
}
```

Este enfoque asegura que el objeto JSON se trunca apropiadamente, facilitando su manejo dentro de los límites de contexto de un LLM.