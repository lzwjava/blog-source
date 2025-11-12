---
audio: false
generated: true
lang: es
layout: post
title: Git Stash
translated: true
type: note
---

Aquí te mostramos cómo usar `git stash` de manera efectiva y cambiar de ramas/tags frecuentemente con cambios sin confirmar:

## Usando `git stash`

`git stash` es un comando poderoso que te permite guardar temporalmente tus cambios sin confirmar (tanto los preparados como los no preparados) y revertir tu directorio de trabajo al último commit. Esto es útil cuando necesitas cambiar de rama o trabajar en otra cosa sin confirmar tu trabajo actual sin terminar.

Aquí tienes un desglose de las operaciones comunes de `git stash`:

**1. Guardar tus cambios actuales:**

```bash
git stash
```

Este comando toma tus cambios sin confirmar, los guarda como un nuevo stash y limpia tu directorio de trabajo. Verás un mensaje como:

```
Saved working directory and index state WIP on <tu_rama>: <commit_hash> <commit_message>
```

**2. Guardar con un mensaje:**

Es útil agregar un mensaje descriptivo a tus stashes, especialmente si tienes varios:

```bash
git stash save "tu mensaje descriptivo"
# o
git stash push -m "tu mensaje descriptivo"
```

**3. Listar tus stashes:**

Para ver una lista de todos tus stashes guardados, usa:

```bash
git stash list
```

Esto mostrará una lista de stashes, generalmente en el formato:

```
stash@{0}: On <nombre_rama>: <commit_hash> <mensaje_stash>
stash@{1}: WIP on <otra_rama>: ...
```

`stash@{0}` es el stash más reciente.

**4. Aplicar un stash:**

Para recuperar los cambios de un stash, puedes usar `git stash apply`. Esto aplic