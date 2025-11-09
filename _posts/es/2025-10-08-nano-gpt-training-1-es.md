---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Iteraciones de Entrenamiento Predeterminadas de NanoGPT
translated: true
type: note
---

En la configuración predeterminada para nanoGPT (por ejemplo, al entrenar con el dataset de caracteres de Shakespeare), el modelo se ejecuta por un total de **5000 iteraciones**.

Esto está definido por `max_iters = 5000` en el archivo `config/train_shakespeare_char.py`. Puedes anularlo mediante la línea de comandos con `--max_iters=<valor>` al ejecutar `train.py`.

[config/train_shakespeare_char.py](https://huggingface.co/nindanaoto/nanoGPT-BitNet158b/blob/main/config/train_shakespeare_char.py)