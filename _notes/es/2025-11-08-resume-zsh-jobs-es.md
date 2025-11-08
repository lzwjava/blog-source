---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Reanudación de trabajos suspendidos en zsh
translated: true
type: note
---

Para reanudar un trabajo suspendido (como tu comando `bundle exec jekyll serve --incremental`, que probablemente fue pausado con Ctrl+Z) en zsh dentro de Ghostty, sigue estos pasos en la misma sesión de terminal:

1.  Lista todos los trabajos en segundo plano/suspendidos para confirmar que está ahí:
    ```
    jobs
    ```
    Esto mostrará algo como `[1]+  Suspended  bundle exec jekyll serve --incremental`.

2.  Reanúdalo en primer plano (volverá a tomar control de tu terminal):
    ```
    fg
    ```
    - Si tienes múltiples trabajos, especifica el que quieres con `fg %1` (reemplazando `1` con el número del trabajo de la salida del comando `jobs`).

Si prefieres ejecutarlo en segundo plano (para poder usar el terminal para otras cosas mientras sirve), usa `bg %1` (nuevamente, con el número del trabajo).

Una vez reanudado, Jekyll debería continuar desde donde se quedó, asumiendo que no hubo interrupciones mayores. Si el proceso parece atascado o genera errores, puede que necesites terminarlo con `kill %1` y reiniciarlo.