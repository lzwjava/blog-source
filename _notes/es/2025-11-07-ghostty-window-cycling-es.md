---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Atajos de Ciclado de Ventanas de Ghostty
translated: true
type: note
---

Sí, lo entiendo completamente—Cmd + ` (tilde/backtick) para cambiar entre ventanas en Ghostty se siente ágil e intuitivo, especialmente si las tratas como sesiones ligeras e independientes en lugar de meterlo todo en pestañas. Tiene ese flujo cíclico agradable sin la carga mental del desorden de una barra de pestañas. La navegación predeterminada por pestañas con Cmd + Shift + [ / ] (o el enfoque de paneles con Cmd + [ / ]) sí se siente torpe en Mac, porque estás lidiando con Shift además de Cmd, y esos corchetes no son los más cómodos para el pulgar sin estirar.

Tienes toda la razón: una combinación simple de Cmd + una tecla es mucho más limpia para la mayoría de la gente—ergonómica, rápida de pulsar y con menos margen de error que las combinaciones con múltiples modificadores. Los valores predeterminados de Ghostty ya apuestan por eso para la selección de pestañas (Cmd + 1–8 salta directamente a unas específicas), pero si estás totalmente a favor de las ventanas sobre las pestañas, podrías reasignar el cambio a algo aún más simple como Cmd + J/K (estilo Vim) o Cmd + ←/→ para ventana anterior/siguiente. Es muy fácil de personalizar en el archivo de configuración—solo añade líneas como:

```
keybind = "cmd-j", "window:previous"
keybind = "cmd-k", "window:next"
```

Eso lo mantiene en un modificador + una tecla, sin complicaciones. ¿Qué configuración usas principalmente—múltiples ventanas de Ghostty en distintos espacios, o todas ancladas en un mismo escritorio? Si tienes una acción específica que quieras asignar (como cambios rápidos de panel), puedo pensar en más ajustes.