---
audio: false
generated: true
lang: es
layout: post
title: 'Git Avanzado: Rebase, Merge, Resolución de Conflictos y Squash'
translated: true
type: note
---

Esta guía cubre el uso avanzado de `git rebase` y `git merge`, la resolución de conflictos, el uso de las estrategias `ours` y `theirs`, y la combinación (squashing) de commits. Proporcionaré explicaciones concisas y ejemplos prácticos para cada tema, centrándome en flujos de trabajo avanzados que asumen familiaridad con los comandos básicos de Git.

## 1. Git Merge: Uso Avanzado
`git merge` combina múltiples secuencias de desarrollo en un único historial unificado. El uso avanzado incluye manejar fusiones complejas, usar estrategias de fusión y gestionar commits de fusión.

### Estrategias de Fusión Clave
- **Recursiva (por defecto)**: Maneja múltiples ancestros comunes y es adecuada para la mayoría de las fusiones.
  - Ejemplo: `git merge --strategy=recursive nombre-rama`
- **Ours**: Mantiene los cambios de la rama actual, descartando los cambios de la rama fusionada.
  - Ejemplo: `git merge --strategy=ours rama-caracteristica`
- **Theirs**: No es una estrategia verdadera pero puede emularse (ver más abajo para resolución de conflictos).
- **Octopus**: Fusiona múltiples ramas a la vez (usada para >2 ramas).
  - Ejemplo: `git merge rama1 rama2 rama3`

### Opciones Avanzadas de Fusión
- `--no-ff`: Fuerza un commit de fusión incluso si es posible un avance rápido (fast-forward), preservando el historial de la rama.
  - Ejemplo: `git merge --no-ff rama-caracteristica`
- `--squash`: Combina todos los commits de la rama fusionada en un solo commit en la rama actual.
  - Ejemplo: `git merge --squash rama-caracteristica && git commit`
- `--allow-unrelated-histories`: Fusiona ramas sin historial común.
  - Ejemplo: `git merge --allow-unrelated-histories rama-repo-externo`

### Ejemplo: Fusionar Sin Avance Rápido
```bash
git checkout main
git merge --no-ff rama-caracteristica
# Crea un commit de fusión, preservando el historial de rama-caracteristica
```

## 2. Git Rebase: Uso Avanzado
`git rebase` reescribe el historial moviendo o modificando commits para crear un historial lineal. Es potente para limpiar ramas pero altera el historial, así que úsalo con precaución en ramas compartidas.

### Tipos de Rebase
- **Rebase Estándar**: Reproduce los commits de la rama actual sobre la rama base.
  - Ejemplo: `git rebase main` (estando en `rama-caracteristica`)
- **Rebase Interactivo**: Permite editar, combinar o reordenar commits.
  - Ejemplo: `git rebase -i main`

### Comandos de Rebase Interactivo
Ejecuta `git rebase -i <base>` (ej., `git rebase -i HEAD~3` para los últimos 3 commits). Esto abre un editor con comandos como:
- `pick`: Mantener el commit tal cual.
- `reword`: Editar el mensaje del commit.
- `edit`: Pausar el rebase para modificar el commit.
- `squash`: Combinar con el commit anterior.
- `fixup`: Como squash, pero descarta el mensaje del commit.
- `drop`: Eliminar el commit.

### Ejemplo: Rebase Interactivo
Para combinar los últimos 3 commits:
```bash
git rebase -i HEAD~3
# En el editor, cambia "pick" a "squash" o "fixup" para los commits a combinar
# Guarda y sale para completar
```

### Rebase sobre una Base Diferente
Para mover una rama a una nueva base (ej., mover `rama-caracteristica` de `base-antigua` a `main`):
```bash
git rebase --onto main base-antigua rama-caracteristica
```

### Rebase con Commits de Fusión
Por defecto, el rebase aplana los commits de fusión. Para preservarlos:
```bash
git rebase -i --preserve-merges main
```

### Abortar un Rebase
Si algo sale mal:
```bash
git rebase --abort
```

## 3. Resolver Conflictos de Merge/Rebase
Los conflictos ocurren cuando Git no puede reconciliar cambios automáticamente. Tanto `merge` como `rebase` pueden resultar en conflictos, que se resuelven de manera similar.

### Pasos para Resolver Conflictos
1. **Identificar Conflictos**: Git se pausa y lista los archivos en conflicto.
   - Para merge: `git status` muestra archivos con conflictos.
   - Para rebase: Los conflictos se resuelven commit por commit durante `git rebase -i`.
2. **Editar Archivos en Conflicto**: Abre los archivos y busca los marcadores de conflicto:
   ```text
   <<<<<<< HEAD
   Tus cambios
   =======
   Cambios entrantes
   >>>>>>> nombre-rama
   ```
   Edita manualmente para mantener los cambios deseados, luego elimina los marcadores.
3. **Marcar como Resuelto**:
   - Para merge: `git add <archivo>`
   - Para rebase: `git add <archivo>`, luego `git rebase --continue`
4. **Completar el Proceso**:
   - Merge: `git commit` (Git puede generar automáticamente un mensaje de commit).
   - Rebase: `git rebase --continue` hasta que todos los commits sean aplicados.

### Ejemplo: Resolver un Conflicto de Fusión
```bash
git checkout main
git merge rama-caracteristica
# Ocurre un conflicto
git status  # Lista archivos en conflicto
# Edita archivos para resolver conflictos
git add archivo-resuelto.txt
git commit  # Finalizar la fusión
```

### Ejemplo: Resolver un Conflicto de Rebase
```bash
git checkout rama-caracteristica
git rebase main
# Ocurre un conflicto
# Edita archivos en conflicto
git add archivo-resuelto.txt
git rebase --continue
# Repite hasta que el rebase se complete
```

## 4. Usar Ours y Theirs en la Resolución de Conflictos
Durante los conflictos, puedes querer favorecer los cambios de un lado (`ours` o `theirs`). El significado de `ours` y `theirs` depende de la operación.

### Merge: Ours vs. Theirs
- `ours`: Cambios de la rama actual (ej., `main`).
- `theirs`: Cambios de la rama que se está fusionando (ej., `rama-caracteristica`).
- Usa la bandera `--strategy-option` (`-X`):
  - Mantener `ours`: `git merge -X ours rama-caracteristica`
  - Mantener `theirs`: `git merge -X theirs rama-caracteristica`

### Rebase: Ours vs. Theirs
- `ours`: Cambios de la rama base (ej., `main`).
- `theirs`: Cambios de la rama que se está reubicando (ej., `rama-caracteristica`).
- Usa durante la resolución de conflictos del rebase:
  ```bash
  git checkout --ours archivo.txt  # Mantener la versión de la rama base
  git checkout --theirs archivo.txt  # Mantener la versión de la rama reubicada
  git add archivo.txt
  git rebase --continue
  ```

### Ejemplo: Merge con Theirs
Para fusionar `rama-caracteristica` en `main` y favorecer los cambios de `rama-caracteristica`:
```bash
git checkout main
git merge -X theirs rama-caracteristica
```

### Ejemplo: Rebase con Ours
Mientras reubicas `rama-caracteristica` sobre `main`, resuelve un conflicto manteniendo la versión de `main`:
```bash
git checkout rama-caracteristica
git rebase main
# Ocurre un conflicto
git checkout --ours archivo.txt
git add archivo.txt
git rebase --continue
```

## 5. Combinar (Squash) Commits
La combinación (squashing) une múltiples commits en uno, creando un historial más limpio. Esto se hace típicamente con rebase interactivo.

### Pasos para Combinar Commits
1. Inicia un rebase interactivo para los commits deseados:
   ```bash
   git rebase -i HEAD~n  # n = número de commits a combinar
   ```
2. En el editor, cambia `pick` a `squash` (o `fixup`) para los commits que quieras combinar en el commit anterior.
3. Guarda y sale. Git puede pedirte que edites el mensaje del commit combinado.
4. Empuja el historial actualizado (fuerza el push si ya se compartió):
   ```bash
   git push --force-with-lease
   ```

### Ejemplo: Combinar 3 Commits
```bash
git rebase -i HEAD~3
# El editor muestra:
# pick abc123 Commit 1
# pick def456 Commit 2
# pick ghi789 Commit 3
# Cambia a:
# pick abc123 Commit 1
# squash def456 Commit 2
# squash ghi789 Commit 3
# Guarda y sale
# Edita el mensaje del commit combinado si se solicita
git push --force-with-lease
```

### Combinar Durante una Fusión
Para combinar todos los commits de una rama durante una fusión:
```bash
git checkout main
git merge --squash rama-caracteristica
git commit  # Crea un único commit
```

## Mejores Prácticas y Consejos
- **Copia de Seguridad Antes del Rebase**: El rebase reescribe el historial. Crea una rama de respaldo:
  ```bash
  git branch rama-respaldo
  ```
- **Evita Rebase en Ramas Compartidas**: Reescribir el historial en ramas públicas puede causar problemas a los colaboradores. Usa `merge` en su lugar.
- **Usa `--force-with-lease` por Seguridad**: Al empujar historial reescrito, esto evita sobrescribir los cambios de otros.
- **Prueba Después de Resolver Conflictos**: Asegúrate de que tu proyecto se compile y pasen las pruebas después de resolver conflictos.
- **Usa Herramientas para Conflictos**: Las herramientas GUI como VS Code, SourceTree o `git mergetool` pueden simplificar la resolución de conflictos.
- **Comunícate con el Equipo**: Si trabajas en equipo, coordina los rebases para evitar conflictos.

## Errores Comunes
- **Perder Trabajo en el Rebase**: Siempre haz una copia de seguridad o usa `git reflog` para recuperar commits perdidos.
- **Mal uso de Ours/Theirs**: Verifica dos veces qué rama es `ours` vs. `theirs` en los contextos de merge vs. rebase.
- **Forzar Push Sin Coordinación**: Forzar el push en ramas compartidas puede interrumpir a los compañeros de equipo. Usa `--force-with-lease` y comunícate.

## Recuperarse de Errores
- **Ver Historial**: Usa `git reflog` para ver estados anteriores y recuperar commits perdidos:
  ```bash
  git reflog
  git checkout <hash-del-commit>
  ```
- **Resetear al Estado Pre-Fusión**:
  ```bash
  git reset --hard HEAD^  # Deshacer el último commit de fusión
  ```
- **Abortar Fusión**: Si una fusión sale mal:
  ```bash
  git merge --abort
  ```

Esta guía proporciona una base sólida para flujos de trabajo avanzados de Git. Para escenarios específicos o errores, ¡avísame y puedo profundizar o buscar soluciones en tiempo real!