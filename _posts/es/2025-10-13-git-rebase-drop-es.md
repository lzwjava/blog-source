---
audio: false
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Git Rebase Drop Elimina Commits
translated: true
type: note
---

Sí — exactamente.

Cuando usas **`drop`** durante un `git rebase -i` interactivo, significa **“eliminar esta confirmación completamente del historial.”**

Esto es lo que sucede:

* Git **omitirá aplicar** esa confirmación mientras repite las otras.
* La rama resultante lucirá como si esa confirmación **nunca hubiera existido** — tanto sus cambios como su mensaje de confirmación desaparecerán.
* Las siguientes confirmaciones seguirán siendo aplicadas (si no dependen de los cambios eliminados).

Ejemplo:

```bash
git rebase -i HEAD~4
```

Podrías ver algo como:

```
pick a1b2c3d Corregir error tipográfico
pick b2c3d4e Agregar README
pick c3d4e5f Implementar inicio de sesión
pick d4e5f6g Agregar registro de depuración
```

Si cambias la última línea a:

```
drop d4e5f6g Agregar registro de depuración
```

entonces, después de guardar y cerrar el editor, Git reorganizará la rama y **excluirá esa confirmación**.

Así que sí — “drop” = **eliminar la confirmación del historial de la rama.**

¿Te gustaría que explique cómo esto se diferencia de `revert` (que *deshace* una confirmación pero mantiene un registro de ella)?