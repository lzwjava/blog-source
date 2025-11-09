---
audio: false
date: 2025-09-07
generated: true
image: false
lang: es
layout: post
title: Cómo Elegir la Versión Correcta de IntelliJ
translated: true
type: note
---

Desde tu salida de `uname -a`:

```
Linux to 6.8.0-60-generic ... x86_64 x86_64 x86_64 GNU/Linux
```

Ese `x86_64` significa que la arquitectura de tu CPU es **Intel/AMD de 64 bits (x86-64)**, no ARM.

Así que, al descargar IntelliJ IDEA (o cualquier IDE de JetBrains), debes elegir la versión **Linux (x64 / x86-64)**, no la versión ARM64.

Las compilaciones **Linux ARM64** son solo para dispositivos con procesadores ARM (como los Macs con Apple Silicon, algunos servidores más nuevos o portátiles ARM).

👉 En resumen:

* **Tu máquina** → `x86_64` → usa **Linux x64**
* **No es tu máquina** → Chips ARM (Macs M1/M2, algunos servidores ARM) → usa **Linux ARM64**

¿Quieres que también te muestre un comando rápido para verificar tu tipo de CPU (por ejemplo, `lscpu` o `arch`) y así estar 100% seguro?