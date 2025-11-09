---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: التكرارات الافتراضية لتدريب نانو جي بي تي
translated: true
type: note
---

في الإعداد الافتراضي لـ nanoGPT (مثل التدريب على مجموعة بيانات شخصيات شكسبير)، يعمل النموذج لمجموع **5000 تكرار**.

يتم تعيين هذا بواسطة `max_iters = 5000` في ملف `config/train_shakespeare_char.py`. يمكنك تجاوزه عبر سطر الأوامر باستخدام `--max_iters=<value>` عند تشغيل `train.py`.

[config/train_shakespeare_char.py](https://huggingface.co/nindanaoto/nanoGPT-BitNet158b/blob/main/config/train_shakespeare_char.py)