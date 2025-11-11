---
audio: false
generated: true
image: false
lang: es
layout: post
title: Limpiar Ramas Remotas Con Prune
translated: true
type: note
---

`git fetch --prune` es una forma de mantener tus referencias locales a las ramas remotas limpias y actualizadas.

### Qué hace

* **`git fetch`** normalmente actualiza tu copia local de las ramas remotas (como `origin/main`, `origin/feature-x`) sin tocar tus propias ramas locales.
* Con el tiempo, el repositorio remoto puede eliminar o renombrar algunas ramas. Sin una limpieza, tu repositorio local seguirá mostrando esas antiguas ramas de seguimiento remotas (ej., `origin/feature-old`).
* **Añadir `--prune`** le dice a Git: *"Si el remoto ya no tiene una rama, elimina mi correspondiente referencia de seguimiento remoto."*

Así, después de ejecutar `git fetch --prune`, tu lista local de ramas remotas coincide exactamente con lo que el remoto tiene actualmente.

### Ejemplo

1. El remoto tiene las ramas: `main`, `feature-a`.
2. Ejecutas `git fetch` → ahora tienes `origin/main`, `origin/feature-a`.
3. Alguien elimina `feature-a` en el remoto.
4. Si ejecutas `git fetch`, seguirás viendo `origin/feature-a` localmente (referencia obsoleta).
5. Si ejecutas `git fetch --prune`, Git notará que `feature-a` ha desaparecido y eliminará `origin/feature-a` de tu repositorio local.

### Por qué es útil

* Mantiene limpia la lista de `git branch -r` (ramas remotas).
* Evita confusiones al cambiar o fusionar con ramas que ya no existen en el repositorio ascendente (upstream).
* Se usa a menudo con alias (ej., `git fetch -p`) o se establece como predeterminado con:

  ```bash
  git config fetch.prune true
  ```

De esa manera, cada `git fetch` poda automáticamente las ramas obsoletas.

---

¿Quieres que también explique cómo **la poda interactúa con las etiquetas** (ya que `git fetch --prune` solo maneja ramas por defecto, pero las etiquetas se comportan de manera diferente)?