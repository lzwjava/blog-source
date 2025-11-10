---
audio: false
generated: true
image: false
lang: es
layout: post
title: Orden de Compresión de Rebase de Git Explicado
translated: true
type: note
---

Cuando ejecutas `git rebase -i` (rebase interactivo) para combinar commits, Git sigue un orden y una lógica muy específicos:

---

### 1. Orden por Defecto

Cuando inicias un rebase interactivo (por ejemplo, `git rebase -i HEAD~5`), Git abre tu editor con los **commits listados del más antiguo al más reciente** (arriba = más antiguo, abajo = más reciente).
El orden importa: esta es la secuencia que Git intentará reproducir sobre la nueva base.

---

### 2. Pick vs. Squash

* **pick** → mantener el commit tal como está.
* **squash (o s)** → combinar este commit con el **commit anterior marcado como `pick`**.
* **fixup (o f)** → igual que squash, pero descarta el mensaje del commit (solo conserva el mensaje del primer commit).

Así que si escribes:

```
pick  a1b2c3  Funcionalidad inicial
squash d4e5f6  Corrección menor
squash g7h8i9  Pequeña limpieza
pick  j1k2l3  Otra funcionalidad
```

Git fusionará `d4e5f6` y `g7h8i9` en `a1b2c3`, produciendo un solo commit.

---

### 3. Reorganizar Commits

Puedes **reordenar los commits directamente en el editor de rebase** moviendo las líneas hacia arriba o hacia abajo.
Por ejemplo:

```
pick  a1b2c3  Funcionalidad inicial
pick  j1k2l3  Otra funcionalidad
squash d4e5f6  Corrección menor
squash g7h8i9  Pequeña limpieza
```

Aquí, Git aplicará primero `a1b2c3`, luego `j1k2l3`.
Los commits `squash` (`d4e5f6` y `g7h8i9`) ahora se combinarán en **`j1k2l3`**, ya que `squash` siempre fusiona en el `pick` precedente más reciente.

---

### 4. Editar Mensajes

Después de combinar, Git se pausa y te permite **editar el mensaje del commit** para el commit combinado. Puedes:

* Mantener todos los mensajes.
* Combinarlos manualmente.
* Conservar solo el primero.

---

### 5. Errores Comunes

* Si pones `squash` como el primer commit (sin un `pick` antes), Git arrojará un error—necesita un commit base en el cual combinar.
* Si los commits entran en conflicto después de reordenarlos, necesitarás resolver los conflictos manualmente durante el rebase.
* Reordenar puede cambiar el historial significativamente; solo hazlo en ramas que no hayas subido/compartido aún, a menos que estés seguro de que quieres reescribir el historial.

---

✅ En resumen:

* Los commits se listan **del más antiguo → al más reciente**.
* `pick` mantiene, `squash` fusiona en el **`pick` anterior más cercano**.
* Puedes reorganizar los commits manualmente en el editor; `squash` siempre adjunta los commits siguientes en el `pick` anterior.

---

¿Quieres que ilustre esto con un **ejemplo de historial de commits antes/después** (mostrando `git log --oneline` antes y después de combinar)? Eso suele aclarar el orden.