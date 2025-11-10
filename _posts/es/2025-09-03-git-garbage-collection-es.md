---
audio: false
generated: true
image: false
lang: es
layout: post
title: Recolección de Basura de Git Explicada
translated: true
type: note
---

`git gc` significa **Git garbage collection** (recolección de basura de Git). Es un comando de mantenimiento que limpia y optimiza tu repositorio local.

### Qué hace

* **Comprime el historial de archivos**: Git almacena objetos (commits, árboles, blobs) en una base de datos. Con el tiempo, se acumulan muchos objetos sueltos. `git gc` los empaqueta juntos en un archivo binario compacto, ahorrando espacio en disco.
* **Elimina objetos inalcanzables**: Si eliminaste ramas o hiciste un rebase, es posible que algunos commits ya no sean alcanzables desde ninguna referencia. Git los mantiene por seguridad, pero `git gc` eventualmente los limpia.
* **Optimiza las referencias**: Reescribe y empaqueta refs como etiquetas y ramas para que las búsquedas sean más rápidas.
* **Poda los reflogs**: Las entradas antiguas del reflog (registros de cambios de HEAD) que superan el período de caducidad se eliminan.

### Por qué a veces sucede automáticamente

* Git ejecuta un **`gc` automático en segundo plano** cuando la cantidad de objetos sueltos o archivos de paquete cruza un umbral. Por ejemplo, si has hecho muchos commits, rebases o merges, Git puede activarlo.
* Muchos comandos de Git (como `git fetch`, `git merge` o `git rebase`) verifican si es recomendable ejecutar un `gc` y lo ejecutan automáticamente si es necesario.
* Esto ayuda a mantener tu repositorio con buen rendimiento sin que tengas que pensar en ello.

### Cuándo ejecutarlo manualmente

* Si tu repositorio se siente **lento** o **hinchado** (por ejemplo, una carpeta `.git` grande).
* Después de hacer una **gran limpieza** (como eliminar ramas o quitar archivos grandes del historial).
* Si quieres forzar una limpieza inmediata:

  ```bash
  git gc --prune=now --aggressive
  ```

  *(ten cuidado: `--aggressive` puede tomar mucho tiempo, especialmente en repositorios grandes)*

---

¿Quieres que también explique cómo **verificar cuándo Git ejecutó `gc` automáticamente por última vez** y qué umbrales lo activan?