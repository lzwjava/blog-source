---
audio: false
generated: true
image: false
lang: de
layout: post
model: x-ai/grok-4-fast
title: Standardmäßige nanoGPT-Trainingsiterationen
translated: true
type: note
---

In der Standardkonfiguration für nanoGPT (z. B. beim Training auf dem Shakespeare-Character-Datensatz) läuft das Modell für insgesamt **5000 Iterationen**.

Dies wird durch `max_iters = 5000` in der Datei `config/train_shakespeare_char.py` festgelegt. Sie können diesen Wert über die Befehlszeile mit `--max_iters=<Wert>` überschreiben, wenn Sie `train.py` ausführen.

[config/train_shakespeare_char.py](https://huggingface.co/nindanaoto/nanoGPT-BitNet158b/blob/main/config/train_shakespeare_char.py)