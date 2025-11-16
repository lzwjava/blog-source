---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Configuración del Proxy de Hugging Face XetHub
translated: true
type: note
---

Sí — **Rust reqwest admite absolutamente una configuración explícita de proxy**, y el cliente XetHub de Hugging Face (escrito en Rust) también lo permite.
PERO: Hugging Face **no expone** una API de Python para que pases la configuración del proxy directamente.
En su lugar, XetHub depende de **variables de entorno** que reqwest lee automáticamente.

Así que la configuración explícita de proxy para reqwest se ve así:

---

# ✔ Cómo reqwest detecta proxies (oficial)

Reqwest utiliza automáticamente las siguientes **variables de entorno**:

* `https_proxy`
* `http_proxy`
* `all_proxy`

La parte importante es que estén en minúsculas.
Reqwest **ignora** las variables en mayúsculas (`HTTPS_PROXY`) a menos que se habilite un flag específico en tiempo de compilación.

**Hugging Face XetHub usa el reqwest por defecto → solo minúsculas.**

Esto significa:

```
export https_proxy="http://127.0.0.1:7890"
export http_proxy="http://127.0.0.1:7890"
```

es la única configuración de proxy explícita garantizada para funcionar con XetHub.

---

# ✔ Cómo HuggingFace XetHub carga la configuración del proxy

Cuando Python ejecuta `load_dataset`, activa un binario en Rust que:

1. Busca las variables de entorno de proxy en minúsculas
2. Reescribe las URLs
3. Abre conexiones a través de reqwest
4. Descarga fragmentos de archivos desde `https://transfer.xethub.hf.co`

Si esas variables de entorno no están configuradas, o no son accesibles → conexión rechazada.

---

# ✔ Forzar manualmente a reqwest para que use proxy (código de referencia)

Solo para mostrar lo que reqwest haría internamente:

```rust
let proxy = reqwest::Proxy::https("http://127.0.0.1:7890")?;
let client = reqwest::Client::builder()
    .proxy(proxy)
    .build()?;
```

El cliente XetHub de Hugging Face *hace algo equivalente*, pero activado por variables de entorno.

---

# ✔ Configuración de proxy explícita completa que siempre funciona con reqwest (compatible con HF)

Ejecuta **todas** estas:

```bash
export http_proxy="http://127.0.0.1:7890"
export https_proxy="http://127.0.0.1:7890"
export all_proxy="http://127.0.0.1:7890"
```

Usa proxy `http`, no `socks5`, porque:

* El soporte para socks en reqwest es opcional
* El binario cliente de XetHub no fue compilado con él para HF

Así que socks puede fallar silenciosamente.

---

# ✔ Verifica que tu proxy se está usando

Prueba con:

```bash
env | grep proxy
```

Si ves minúsculas → bien.

Luego:

```bash
curl -I https://transfer.xethub.hf.co --proxy http://127.0.0.1:7890
```

Si curl tiene éxito → reqwest tendrá éxito.

---

# Resumen

* Los datasets de Hugging Face a veces se descargan a través de **XetHub** (cliente Rust reqwest)
* Reqwest solo respeta las variables de proxy en **minúsculas** por defecto
* Debes configurarlas explícitamente
* Usa proxy **HTTP**, no SOCKS
* `HF_HUB_DISABLE_XETHUB=1` puede evitar reqwest por completo si es necesario

---

Si quieres, puedo preparar un:

* script de "solución de proxy para HF" de un solo comando
* configuración persistente para tu `.bashrc`
* detección automática para confirmar si reqwest está usando el proxy

Solo házmelo saber.