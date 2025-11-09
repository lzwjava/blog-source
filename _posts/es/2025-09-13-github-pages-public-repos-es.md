---
audio: false
date: 2025-09-13
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: GitHub Pages Requiere Repositorios Públicos
translated: true
type: note
---

Correcto — si haces privado tu repositorio de GitHub Pages, pierdes el alojamiento gratuito de GitHub Pages.

GitHub Pages solo funciona automáticamente cuando el repositorio es **público**. Si el repositorio es privado, el sitio `github.io` no se publicará a menos que estés en un **plan GitHub Enterprise con Pages para repositorios privados habilitado** (esa es una función de pago, no incluida en las cuentas personales gratuitas o estándar).

Así que para tu blog personal en `username.github.io`:

* **Repositorio público** → GitHub Pages lo construye y lo sirve en `https://username.github.io/`.
* **Repositorio privado (cuenta gratuita)** → GitHub Pages está deshabilitado.
* **Repositorio privado (Enterprise)** → Sigue funcionando, pero solo si tu organización habilita Pages para repositorios privados.

¿Quieres que también explique una alternativa (como mantener tu repositorio principal privado pero sincronizando solo la salida `_site` a un repositorio público separado para su publicación)?