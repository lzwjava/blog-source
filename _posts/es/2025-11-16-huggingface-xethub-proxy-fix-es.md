---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Solucionando el Problema del Proxy de Hugging Face XetHub
translated: true
type: note
---

Tus registros muestran algo muy importante:

**La conexión fallida *no* va directamente a HuggingFace.**
Va a **[https://transfer.xethub.hf.co](https://transfer.xethub.hf.co)** — este es el backend *XetHub* de Hugging Face (cliente Rust `reqwest`), que el proxy que configuraste **NO intercepta automáticamente**.

Esto explica todo:

* Ya configuraste `HTTP_PROXY` para Python → bien
* Pero XetHub usa **rust reqwest**, no Python requests
* Rust reqwest **ignora las variables de proxy del sistema a menos que configures las variables en minúsculas HTTPS_PROXY**, o use una configuración de proxy explícita

Entonces: **tu entorno de Python está usando el proxy, pero XetHub (el nuevo proveedor de almacenamiento de HF) NO**.

Por eso ves:

```
ConnectError("Connection refused")
```

y reintentos.

---

# Por qué sucede esto (versión corta)

Hugging Face migró recientemente el almacenamiento a **XetHub**, que utiliza un cliente Rust.
Ese cliente obedece:

* `https_proxy`
* `http_proxy`

pero **no siempre** las versiones en mayúsculas, dependiendo de la compilación.

¿Configuraste en mayúsculas? → Puede que las ignore.

---

# Solución (funciona de forma fiable en China)

## 1. Configura variables de proxy en minúsculas Y mayúsculas

En tu shell **antes de ejecutar NanoGPT**:

```bash
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"

export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
```

Rust reqwest prefiere minúsculas
Python requests prefiere mayúsculas
Configurar ambas evita problemas.

Luego ejecuta:

```bash
python data/openwebtext_10k/prepare.py
```

Deberías ver la velocidad de descarga adecuada inmediatamente.

---

# 2. Importante si tu proxy es SOCKS5

Rust reqwest **no admite socks5** a menos que se compile con características opcionales.
Así que si tu proxy es socks5:// → fallará.

Debes cambiar al puerto HTTP de tu cliente, usualmente:

* Clash: 7890 (HTTP)
* V2RayN: 10809 (HTTP)

Usa HTTP, no SOCKS.

---

# 3. Cómo probar si la parte Rust está usando el proxy

Prueba via `curl`, **no Python**, porque curl se comporta de manera similar a Rust en las reglas de proxy:

```bash
curl -I https://transfer.xethub.hf.co --proxy http://127.0.0.1:7890
```

Si esto funciona → las descargas de Rust también funcionarán.

Si falla → tu proxy no puede alcanzar el dominio `xethub.hf.co`.

---

# 4. Si quieres forzar a Hugging Face a evitar XetHub

Puedes configurar la variable de entorno:

```bash
export HF_HUB_DISABLE_XETHUB=1
```

Esto fuerza el antiguo backend S3 de HuggingFace en lugar de XetHub, mucho más compatible con proxy.

Luego:

```bash
python data/openwebtext_10k/prepare.py
```

Esta es la solución más estable.

---

# Solución recomendada (compatible con China)

Para fiabilidad:

```bash
export HF_HUB_DISABLE_XETHUB=1

export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"

python data/openwebtext_10k/prepare.py
```

---

Si quieres, puedo darte:

* Un script bash de un solo clic (`hf_proxy_on.sh`)
* Una configuración de proxy permanente en `.bashrc`
* Instrucciones para espejar OpenWebText localmente y evitar descargas futuras

Solo dime.