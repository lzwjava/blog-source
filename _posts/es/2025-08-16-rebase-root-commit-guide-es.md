---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía Esencial de la Confirmación Raíz de Rebase
translated: true
type: note
---

`git rebase --root` es una forma especial de rebase que te permite reescribir el **primer commit absoluto** de tu repositorio. Normalmente, `git rebase` necesita un commit padre sobre el cual hacer el rebase, pero la opción `--root` trata el commit raíz (el primer commit, sin padre) como si también fuera sometido a rebase.

Así es como funciona en la práctica:

### 1. Rebase estándar vs. rebase de raíz

* **`git rebase` normal**: Reaplicas commits sobre otra rama o commit, cambiando el historial después de una base elegida.
* **`git rebase --root`**: En lugar de comenzar después de la raíz, reescribe la raíz misma. Puedes dividirla, combinarla (squash) con commits posteriores, o incluso reemplazarla por completo.

### 2. Casos de uso típicos

* **Editar el mensaje del primer commit**
  Si quieres reescribir el mensaje del primer commit absoluto de tu proyecto, puedes ejecutar:

  ```bash
  git rebase --root -i
  ```

  y cambiar `pick` a `reword` para el primer commit.

* **Combinar (squash) la raíz con commits posteriores**
  Por ejemplo, si tu primer commit era solo un scaffolding (como un `README`), puedes combinarlo con el siguiente commit para limpiar el historial.

* **Dividir el commit raíz**
  Si tu primer commit contenía demasiado (por ejemplo, una descarga completa del código del proyecto), puedes dividirlo en múltiples commits lógicos durante un rebase interactivo.

### 3. Qué sucede internamente

* Git crea un commit padre "falso" temporal para el commit raíz, para poder aplicar las operaciones de rebase desde cero.
* Cada commit es reproducido (rebaseado) como si el repositorio hubiera comenzado de manera diferente.
* Esencialmente, estás reescribiendo los cimientos del historial de tu repositorio.

### 4. Flujo de trabajo de ejemplo

```bash
git rebase --root -i
```

Obtendrás un editor como este:

```
pick a1b2c3d Initial commit
pick d4e5f6g Add feature A
pick h7i8j9k Add feature B
```

Desde aquí puedes:

* Cambiar `pick` a `reword` para el commit raíz → cambiar su mensaje.
* Cambiar `pick` a `squash` → fusionar la raíz con el siguiente commit.
* Reordenar o dividir según sea necesario.

### ⚠️ Nota importante

`git rebase --root` **reescribe el historial**, por lo que solo debe hacerse en ramas que no han sido enviadas (push)/compartidas, o debes forzar el envío (force-push) posteriormente. En ramas compartidas, puede causar confusión y conflictos para los colaboradores.

---

¿Te gustaría que también te muestre un **ejemplo concreto de historial antes y después** (con hashes de commit) para que puedas ver exactamente cómo `git rebase --root` cambia el registro?