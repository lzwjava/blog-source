---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Uso de Proxy con Conjuntos de Datos de Hugging Face
translated: true
type: note
---

Sí — `datasets` sigue la **configuración de proxy de tu sistema / entorno**, pero **no** tiene su propia configuración de proxy.
Por lo tanto, definitivamente puedes hacer que Hugging Face descargue conjuntos de datos a través de un proxy cuando estés en China.

Así es cómo se hace.

---

# Cómo hacer que `load_dataset` use un proxy (compatible con China)

## 1. Establecer variables de entorno para el proxy HTTP/HTTPS

`datasets` utiliza internamente la librería `requests` de Python.
`requests` usa automáticamente las variables de entorno de proxy estándar:

### Linux / macOS

```bash
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
```

Si tu proxy usa SOCKS5:

```bash
export HTTP_PROXY="socks5://127.0.0.1:1080"
export HTTPS_PROXY="socks5://127.0.0.1:1080"
```

### Windows (PowerShell)

```powershell
setx HTTP_PROXY "http://127.0.0.1:7890"
setx HTTPS_PROXY "http://127.0.0.1:7890"
```

Luego, vuelve a abrir la terminal.

---

## 2. Si estás ejecutando Python dentro de código (como Jupyter), configúralo dentro de Python

```python
import os

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
```

Esto funciona de forma fiable.

---

## 3. Confirmar que el proxy está funcionando

Puedes probar con:

```python
import requests
print(requests.get("https://api.ipify.org?format=json").text)
```

Si la IP es el nodo de salida de tu proxy, entonces las descargas de conjuntos de datos de Hugging Face también pasarán por ese proxy.

---

## 4. `huggingface_hub` de Hugging Face también respeta estas variables

`datasets` utiliza internamente `huggingface_hub`, y **también** sigue:

* `HTTP_PROXY`
* `HTTPS_PROXY`
* `http_proxy`
* `https_proxy`

Así que, una vez que las variables de entorno estén establecidas, tanto las descargas de modelos como de conjuntos de datos usarán tu proxy automáticamente.

---

# Notas sobre el uso en China

* Las descargas directas de Hugging Face a menudo requieren un proxy porque se alojan en endpoints de EE. UU./Europa.
* Si ves tiempos de espera agotados (timeouts) con archivos de conjunto de datos `.zst`, esto es normal sin un proxy.
* Un proxy global (Clash, V2Ray, Qv2ray, etc.) hace que todo funcione más suavemente.

---

# Si quieres, puedo mostrar:

* Cómo asegurar que NanoGPT descargue conjuntos de datos a través de tu proxy
* Cómo almacenar en caché el conjunto de datos localmente para evitar descargas futuras
* Cómo hacer un mirror local de los conjuntos de datos de Hugging Face en China (por ejemplo, la alternativa del espejo de Tsinghua)

Solo dime lo que necesitas.