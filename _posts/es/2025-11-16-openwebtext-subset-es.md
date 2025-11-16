---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Descargando una Porción de OpenWebText
translated: true
type: note
---

Ah, entiendo — quieres seguir usando **Hugging Face CLI** pero descargando solo una pequeña porción. El problema es: la CLI está diseñada para descargar **archivos completos**, no porciones. OpenWebText está dividido en 21 archivos `.tar`; si usas la CLI, descargará los tarballs completos, así que no puedes obtener exactamente "1%" sin descargar fragmentos grandes.

Aquí tienes un enfoque práctico:

---

### 1. Descargar solo un subconjunto de archivos

En lugar de los 21 archivos completos, elige solo unos pocos tarballs:

```bash
huggingface-cli download \
  --repo-type dataset openwebtext/subsets/urlsf_subset00.tar \
  --local-dir ./openwebtext
huggingface-cli download \
  --repo-type dataset openwebtext/subsets/urlsf_subset01.tar \
  --local-dir ./openwebtext
```

* Cada tarball tiene ~625MB, así que si descargas 1–2 de ellos, es aproximadamente 1–2% del dataset.
* Puedes ajustar qué subconjuntos eliges; HF no impone un orden secuencial.

---

### 2. Extraer solo lo que necesitas

Después de la descarga:

```bash
cd ./openwebtext
tar -xvf urlsf_subset00.tar
tar -xvf urlsf_subset01.tar
```

Luego puedes procesar solo algunos documentos de estos subconjuntos.

---

### 3. Opcional: Combinar con HF Transfer

Para acelerar las descargas de la CLI:

```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

Luego reintenta los comandos de la CLI — las descargas serán mucho más rápidas.

---

Si quieres, puedo crear un **pequeño fragmento de comando que automáticamente seleccione ~1% de OpenWebText usando solo la CLI**, para que no tengas que seleccionar manualmente los tarballs. ¿Quieres que lo haga?