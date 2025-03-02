---
audio: false
generated: false
lang: es
layout: post
title: Prefiera usar solicitudes HTTP sin procesar en lugar de wrappers
translated: true
---

```python
import requests
import json
import time
def traducir_texto(texto, idioma_destino, especial=False):
    if not texto or not texto.strip():
        return ""
    if idioma_destino == 'en':
        print(f"  Omitiendo traducción para inglés: {texto[:50]}...")
        return texto
    print(f"  Traduciendo texto: {texto[:50]}...")

    reintentos = 3
    for intento in range(reintentos):
        try:
            respuesta = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": crear_prompt_traducción(idioma_destino, especial)},
                    {"role": "user", "content": texto}
                ],
                stream=False
            )
            if not respuesta or not respuesta.choices or not respuesta.choices[0].message.content:
                print(f"  Error: La respuesta de traducción está vacía o es inválida: {respuesta}")
            if respuesta and respuesta.choices:
                texto_traducido = respuesta.choices[0].message.content
                return texto_traducido
            else:
                print(f"  La traducción falló en el intento {intento + 1}.")
                if intento == reintentos - 1:
                    return None
        except Exception as e:
            print(f"  La traducción falló con error en el intento {intento + 1}: {e}")
            if intento == reintentos - 1:
                return None
            time.sleep(1)  # Esperar antes de reintentar
    return None
```

Error:

```bash
 La traducción falló con error en el intento 1: Expecting value: line 5 column 1 (char 4)
```

Este error indica que la API de DeepSeek está devolviendo una respuesta que no es un JSON válido, posiblemente HTML u otro formato. Esto es inesperado, ya que se espera que la API devuelva JSON. El problema podría deberse a un problema temporal de la API, limitación de tasa, o un problema con el prompt. Es importante manejar esto de manera adecuada registrando el error y posiblemente reintentando.