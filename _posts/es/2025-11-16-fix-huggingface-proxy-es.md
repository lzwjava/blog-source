---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Corrección del Proxy para Descargas de HuggingFace
translated: true
type: note
---

Sí — **puede** usar tu proxy, pero por el output que pegaste, **tu proxy NO se está usando en este momento**.
Por eso la descarga está atascada en **17.6 bytes/s** — síntoma clásico de una conexión directa China-a-HF.

Déjame mostrarte **cómo confirmarlo** y **cómo solucionarlo**.

---

# 1. Por qué tu ejecución actual *no* está usando el proxy

La línea:

```
78.0/630M [00:16<9947:51:33, 17.6B/s]
```

es clara: si un proxy adecuado (Clash, V2Ray, Shadowsocks) estuviera activo a través de `HTTP_PROXY` / `HTTPS_PROXY`, verías velocidades como:

* cientos de KB/s
* o varios MB/s
* no ~17 bytes/s

Así que el proceso de Python no está detectando ninguna variable de entorno del proxy.

---

# 2. VERIFICA si existen tus variables de entorno del proxy

En la misma terminal exacta donde ejecutas:

```
python data/openwebtext_10k/prepare.py
```

Ejecuta:

```bash
echo $HTTP_PROXY
echo $HTTPS_PROXY
```

Si no imprime nada → no están configuradas, así que HuggingFace no puede usarlas.

---

# 3. SOLUCIÓN: configura el proxy para esa sesión de terminal

Ejemplo para Clash ejecutándose en el puerto 7890:

```bash
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
```

Si usas SOCKS5 (ej. Shadowsocks):

```bash
export HTTP_PROXY="socks5://127.0.0.1:1080"
export HTTPS_PROXY="socks5://127.0.0.1:1080"
```

**Luego ejecuta de nuevo:**

```bash
python data/openwebtext_10k/prepare.py
```

Ahora tu velocidad debería aumentar dramáticamente.

---

# 4. Verificación adicional dentro de Python

Añade estas líneas al principio de `prepare.py` solo para probar:

```python
import os
print("HTTP_PROXY:", os.getenv("HTTP_PROXY"))
print("HTTPS_PROXY:", os.getenv("HTTPS_PROXY"))
```

Si imprimen `None` → tu shell no las pasó → arregla tu entorno.

---

# 5. Opcional: verifica con `requests` antes de cargar el dataset

Ejecuta:

```python
import requests
print(requests.get("https://api.ipify.org?format=json", timeout=5).text)
```

* Si la IP devuelta es la de tu VPN/proxy → bien.
* Si es la IP de tu ISP de casa → el proxy no se está usando.

---

# 6. Detalle importante: HuggingFace usa **HTTP**, no SOCKS**, a menos que uses pysocks

Si tu proxy es SOCKS5, algunas instalaciones de Python no funcionan con él a menos que `PySocks` esté instalado:

```bash
pip install pysocks
```

Luego los proxies SOCKS funcionan normalmente.

---

# 7. Resumen

✔ HuggingFace *sí* usará el proxy
✔ Pero solo si las variables de entorno están configuradas
✘ Tus registros muestran que tu proxy NO está activo
✔ Solución: configura las variables de entorno del proxy en la misma shell

---

Si quieres, puedo:

* Ajustar tu configuración de shell (`.bashrc` o `.zshrc`) para usar siempre el proxy
* Hacer un script de "proxy-on" / "proxy-off"
* Parchear tu `prepare.py` de NanoGPT para forzar los proxies dentro de Python

Dime qué dirección prefieres.