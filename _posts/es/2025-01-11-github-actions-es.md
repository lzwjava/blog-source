---
audio: false
generated: false
image: false
lang: es
layout: post
title: Tiempo Máximo de Ejecución de un Trabajo en GitHub Actions
translated: true
type: post
---

He estado utilizando GitHub Actions para automatizar la traducción de mis publicaciones de blog. Inicialmente, intenté traducir todas las publicaciones en un solo trabajo, con los cambios confirmados en el repositorio solo después de que todas las traducciones estuvieran completas.

Era optimista y me fui a dormir, esperando que el proceso terminara. Sin embargo, después de 8 horas, me desperté y encontré el siguiente error:

> El trabajo que se ejecuta en el runner GitHub Actions 12 ha excedido el tiempo máximo de ejecución de 360 minutos.

Esto significaba que las 6 horas de trabajo de traducción se perdieron, ya que la confirmación solo ocurrió al final.

Para solucionar esto, modifiqué el flujo de trabajo para confirmar los cambios cada 10 archivos.

Además, implementé programación multihilo para reducir el tiempo total de traducción de 6 horas a aproximadamente una hora.

GitHub Actions ofrece mucha flexibilidad. Admite múltiples trabajos de flujo de trabajo, lo que permite la separación de tareas. Algunos trabajos pueden activarse en cada confirmación, mientras que otros pueden activarse por diferentes eventos.