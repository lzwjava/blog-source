---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de Certificados SSL de Python Certifi
translated: true
type: note
---

El paquete **`certifi`** en PyPI es una pequeña librería que proporciona **los certificados raíz confiables de Mozilla** en un bundle. Es comúnmente utilizado por librerías de Python como `requests`, `urllib3` o cualquier cliente HTTPS que necesite validar certificados SSL/TLS.

Aquí se explica cómo usarlo:

---

### 1. Instalar `certifi`

```bash
pip install certifi
```

---

### 2. Obtener la ruta del bundle de CA

En Python:

```python
import certifi

print(certifi.where())
```

Esto imprimirá la ruta completa al bundle de certificados de CA (un archivo `.pem`). Por ejemplo:

```
/usr/local/lib/python3.11/site-packages/certifi/cacert.pem
```

---

### 3. Usar con `requests` o `urllib3`

```python
import requests
import certifi

response = requests.get("https://example.com", verify=certifi.where())
print(response.status_code)
```

Por defecto, `requests` ya usa `certifi` internamente, pero pasar explícitamente `verify=certifi.where()` asegura que utiliza el bundle actualizado.

---

### 4. Usar en otras librerías HTTPS

Si trabajas directamente con `urllib3`:

```python
import urllib3
import certifi

http = urllib3.PoolManager(
    cert_reqs="CERT_REQUIRED",
    ca_certs=certifi.where()
)

response = http.request("GET", "https://example.com")
print(response.status)
```

---

### 5. Uso a nivel del sistema (opcional)

A veces puedes querer dirigir una aplicación para que use el bundle de CA de certifi:

```bash
export SSL_CERT_FILE=$(python -m certifi)
```

---

👉 En resumen:

* Instala con `pip install certifi`
* Usa `certifi.where()` para obtener la ruta del bundle de certificados
* Pásaselo a las librerías que necesiten validación de certificados

---

¿Quieres que también te muestre **cómo hacer que todo tu entorno de Python use los certificados de certifi por defecto**, para que no necesites configurar cada librería individualmente?