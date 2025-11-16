---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Cómo Arreglar Descargas Lentas de Hugging Face
translated: true
type: note
---

Este es un problema común al descargar grandes conjuntos de datos de HF a través de un proxy. La combinación de:

* Muchos archivos de varios cientos de MB
* Python `requests` / `huggingface_hub`
* Un proxy HTTP local (especialmente Clash, V2Ray o tun2socks)

a menudo resulta en un rendimiento extremadamente lento o restablecimientos de conexión.

A continuación se muestran las soluciones más útiles.

---

## 1. **Mejor solución: Usar `hf_transfer`**

Hugging Face tiene un descargador acelerado que ofrece velocidades **10×–50× más rápidas** y es más estable.

Instalar:

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

Ejecuta tu comando nuevamente.

Esto por sí solo suele solucionar las descargas lentas a través de proxies.

---

## 2. Usar `aria2c` con la CLI de Hugging Face (más rápido para archivos enormes)

Si descargas manualmente:

```bash
pip install huggingface_hub[cli]
sudo apt install aria2
```

Luego descarga:

```bash
huggingface-cli download --repo-type dataset openwebtext --local-dir ./openwebtext --local-dir-use-symlinks False
```

La CLI de HF usa automáticamente aria2, que maneja:

* conexiones paralelas
* reanudación
* proxies inestables

mucho mejor que `requests`.

---

## 3. Solución para la lentitud del proxy local: usar SOCKS a nivel del sistema en lugar de HTTP

Si estás usando algo como:

```
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890
```

Cambia a SOCKS5 si tu proxy lo admite:

```bash
export ALL_PROXY=socks5://127.0.0.1:7891
```

SOCKS es **mucho más estable** para la transmisión de archivos grandes.

---

## 4. Desactivar el proxy para archivos grandes

Si tu red directa está bien pero el proxy la ralentiza:

```bash
unset HTTP_PROXY
unset HTTPS_PROXY
unset ALL_PROXY
```

Luego reintenta. Algunos servidores de HF son rápidos incluso sin proxy, dependiendo de la región.

---

## 5. Usar un espejo de HF (a veces lento en China continental / TW)

Puedes forzar la CDN:

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

Luego ejecuta de nuevo.
Esto mejora drásticamente las velocidades para algunas regiones.

---

## 6. Reanudar descargas interrumpidas

Los conjuntos de datos de HF se almacenan en caché aquí:

```
~/.cache/huggingface/datasets/
```

Si algún archivo se descargó parcialmente, HF reanuda automáticamente; no es necesario empezar desde cero.

---

## 7. Si sigue lento: evitar el conjunto de datos completo, usar una porción pequeña

OpenWebText es >40GB.
Puedes cargar solo una pequeña parte:

```python
from datasets import load_dataset
ds = load_dataset("openwebtext", split="train[:1%]")
```

---

## Recomendación rápida

La más rápida + fácil:

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
python data/openwebtext_10k/prepare.py
```

Deberías ver inmediatamente un salto en las velocidades de descarga.

---

Si quieres, puedo mostrarte cómo modificar tu `prepare.py` para usar un descargador completamente personalizado con reintentos/backoff y obtención paralela, para que tu pipeline siempre descargue rápido y nunca se detenga.