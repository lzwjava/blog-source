---
audio: false
generated: true
image: false
lang: es
layout: post
title: Conflictos y Soluciones de Cherry Pick
translated: true
type: note
---

El comando **cherry-pick** de Git te permite tomar un *commit* de una rama y aplicarlo en otra, sin fusionar todo el historial de la rama.

---

### Cómo funciona

* Cuando ejecutas `git cherry-pick <commit-hash>`, Git:

  1. Localiza los cambios introducidos por ese *commit* (un *diff* contra su *commit* padre).
  2. Vuelve a aplicar esos cambios en tu rama actual, creando un nuevo *commit* con un nuevo *hash*.
  3. Esto significa que el contenido del *commit* se reutiliza, pero no mantiene la ascendencia del *commit* original.

Es como decir:
*"Toma solo el parche de este *commit* y colócalo justo donde estoy ahora."*

---

### Por qué ocurren conflictos

Los conflictos surgen porque *cherry-pick* aplica los cambios **fuera de su contexto original**. Algunas razones comunes:

1. **Deriva del código**
   Si la rama destino ha cambiado en las mismas áreas de código desde el *commit* original, Git no puede aplicar el parche limpiamente. Por ejemplo:

   * El *commit* original añadió una función en `archivoA`.
   * En la rama destino, alguien renombró o eliminó esa función.
     → Conflicto al hacer *cherry-pick*.

2. **Faltan commits dependientes**
   A veces un *commit* depende de *commits* anteriores (por ejemplo, refactorizaciones, renombrado de variables). Si lo aplicas con *cherry-pick* sin esos *commits*, el contexto es diferente y aparecen conflictos.

3. **Cambios superpuestos**
   Si ambas ramas modificaron las mismas líneas de código (incluso por diferentes razones), Git no puede decidir automáticamente y se detiene para una resolución manual.

---

### Escenario de ejemplo

* La rama `rama-caracteristica` tiene los *commits* A → B → C.
* Quieres el *commit* B en `main`.
* Ejecutas `git checkout main && git cherry-pick B`.
* Si `main` ya había tocado el mismo archivo/líneas que B, Git reporta un conflicto. Debes abrir el archivo, resolver las diferencias, hacer `git add` y luego `git cherry-pick --continue`.

---

👉 En resumen: **El *cherry-pick* reproduce un parche en un nuevo contexto. Los conflictos ocurren cuando ese contexto ha divergido demasiado del original.**

¿Te gustaría que también te explicara las **mejores prácticas para reducir conflictos al usar *cherry-pick*** (como secuenciar *commits*, usar `-x*, o hacer *rebase* primero)?