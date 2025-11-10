---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía de Git Diff-Tree
translated: true
type: note
---

Aquí tienes una guía práctica y completa sobre `git diff-tree`: qué es, cuándo usarla y las opciones que realmente usarás en el trabajo real. Evitaré tablas extensas y me centraré en explicaciones concretas con ejemplos listos para copiar y pegar.

# Qué hace realmente `git diff-tree`

* Compara **objetos tree**. En el uso diario, eso suele significar: "muéstrame qué cambió en un **commit** comparado con su(s) padre(s)".
* Es **plumbing** (apto para scripts), a diferencia de `git show`/`git log` que son porcelain (orientados a humanos).
* Nunca mira tu directorio de trabajo; solo compara trees almacenados en el repositorio (commits, tags que apuntan a commits, o IDs de tree en bruto).

# Formas básicas que usarás

1. Diferenciar un commit contra su padre

```bash
git diff-tree -p <commit>
```

Si `<commit>` tiene un padre, verás un parche normal. Si es un commit de fusión (merge), no verás nada a menos que lo solicites (ver más abajo).

2. Diferenciar dos trees/commits explícitamente

```bash
git diff-tree -p <old-tree-or-commit> <new-tree-or-commit>
```

Excelente cuando quieres comparar dos puntos cualesquiera, no solo "commit vs padre".

3. Mostrar solo nombres de archivos (sin parche)

```bash
git diff-tree --name-only -r <commit>
```

Añade `-r` para recursar en subdirectorios y obtener una lista plana.

4. Mostrar nombres con tipo de cambio

```bash
git diff-tree --name-status -r <commit>
# Salida de líneas como:
# A path/to/newfile
# M path/to/modified
# D path/to/deleted
```

5. Mostrar un parche (diff completo)

```bash
git diff-tree -p <commit>            # diff unificado como `git show`
git diff-tree -U1 -p <commit>        # menos contexto (1 línea)
```

# Opciones que debes conocer (con por qué/cuándo)

* `-r` — Recursar en subtrees para ver todas las rutas anidadas. Sin esto, un directorio que cambió podría mostrarse como una sola línea.
* `--no-commit-id` — Suprimir la cabecera "commit <sha>" cuando estás generando salida por commit para scripts.
* `--root` — Cuando un commit **no tiene padre** (commit inicial), aún así mostrar sus cambios contra el tree vacío.
* `-m` — Para commits de fusión, mostrar diffs **contra cada padre** (produce múltiples diffs).
* `-c` / `--cc` — Diff combinado de fusión. `--cc` es una vista refinada (lo que usa `git show` para fusiones).
* `--name-only` / `--name-status` / `--stat` / `--numstat` — Diferentes estilos de resumen. `--numstat` es apto para scripts (recuentos de líneas añadidas/eliminadas).
* `--diff-filter=<set>` — Filtrar por tipos de cambio, ej. `--diff-filter=AM` (solo Añadidos o Modificados); letras comunes: `A`ñadido, `M`odificado, `E`liminado, `R`enombrado, `C`opiado, Tipo `T` cambiado.
* `-M` / `-C` — Detectar renombres y copias. Añade un umbral de similitud opcional, ej. `-M90%`.
* `--relative[=<path>]` — Restringir la salida a un subdirectorio; sin argumento, usa el directorio de trabajo actual.
* `-z` — **Terminar con NUL** las rutas para un análisis de máquina inequívoco (maneja nuevas líneas o tabuladores en nombres de archivo).
* `--stdin` — Leer una lista de commits (o pares) desde la entrada estándar. Esta es la clave para operaciones rápidas por lotes.

# Patrones canónicos para scripts

### 1) Listar archivos cambiados para un solo commit

```bash
git diff-tree --no-commit-id --name-status -r <commit>
```

### 2) Procesar por lotes muchos commits (¡rápido!)

```bash
git rev-list main --since="2025-08-01" |
  git diff-tree --stdin -r --no-commit-id --name-status
```

`--stdin` evita lanzar `git` por cada commit y es mucho más rápido para rangos grandes.

### 3) Solo adiciones y modificaciones en un directorio

```bash
git diff-tree -r --no-commit-id --name-status \
  --diff-filter=AM <commit> -- src/backend/
```

### 4) Contar líneas añadidas/eliminadas por archivo (apto para scripts)

```bash
git diff-tree -r --no-commit-id --numstat <commit>
# Salida: "<añadidas>\t<eliminadas>\t<ruta>"
```

### 5) Detectar y mostrar renombres en un commit

```bash
git diff-tree -r --no-commit-id -M --name-status <commit>
# Líneas como: "R100 old/name.txt\tnew/name.txt"
```

### 6) Parche para un commit de fusión

```bash
git diff-tree -m -p <merge-commit>     # parches por padre
git diff-tree --cc <merge-commit>      # vista combinada (parche único)
```

### 7) Commit inicial (sin padre)

```bash
git diff-tree --root -p <initial-commit>
```

# Entender el formato de registro en bruto (si analizas manualmente)

Usa `--raw` (usado implícitamente por algunos modos) para obtener registros mínimos y estables:

```
:100644 100644 <oldsha> <newsha> M<TAB>ruta
```

* Los números son modos de archivo: `100644` archivo regular, `100755` ejecutable, `120000` enlace simbólico, `160000` gitlink (submódulo).
* El estado es una sola letra (`A`, `M`, `D`, etc.), posiblemente con una puntuación (ej., `R100`).
* Para renombres/copias verás dos rutas. Con `-z`, los campos están separados por NUL; sin `-z`, están separados por tabuladores.

**Consejo:** Si estás construyendo herramientas confiables, siempre pasa `-z` y separa por NUL. Existen nombres de archivo con nuevas líneas.

# Comparar `git diff-tree` con comandos relacionados (para elegir el correcto)

* `git diff`: compara **índice/directorio de trabajo** vs HEAD o dos commits/trees cualesquiera; desarrollo interactivo.
* `git show <commit>`: un wrapper amigable para "diff vs padre + metadatos". Genial para humanos.
* `git log -p`: historial más parches. Para rangos, suele ser más conveniente que hacer un bucle manual con `diff-tree`.
* `git diff-tree`: plumbing para **diffs por commit precisos y scriptables**, procesables por lotes con `--stdin`.

# Ejemplos del mundo real

### "¿Qué cambió en este commit de fusión de PR?"

```bash
git diff-tree --cc <merge-commit> | less
```

Si necesitas detalle por padre:

```bash
git diff-tree -m -p <merge-commit> | less
```

### "Alimentar un paso de CI con una lista limpia de archivos modificados por el último commit"

```bash
git diff-tree --no-commit-id --name-only -r HEAD > changed.txt
```

### "Solo archivos Java añadidos o modificados en los últimos 20 commits"

```bash
git rev-list -n 20 HEAD |
  git diff-tree --stdin -r --no-commit-id --name-only --diff-filter=AM |
  grep -E '\.java$'
```

### "Resumir la actividad (líneas añadidas/eliminadas) para una etiqueta de release"

```bash
git diff-tree -r --no-commit-id --numstat v1.2.0..v1.3.0
```

### "Manejar nombres de archivo raros de forma segura"

```bash
git diff-tree -z -r --no-commit-id --name-status <commit> |
  awk -v RS='\0' 'NR%2{status=$0; next}{printf "%s %s\n", status, $0}'
```

# Notas de rendimiento

* Prefiere `--stdin` con `git rev-list` para rangos grandes; evita la sobrecarga de procesos.
* Omite los parches (`--name-only`/`--name-status`) cuando no necesites cambios de línea.
* Evita la detección de renombres (`-M`, `-C`) si te preocupa la velocidad sobre la precisión.

# Problemas y casos extremos

* **Sin salida para fusiones por defecto.** Debes pasar `-m` (por padre) o `--cc`/`-c` (combinado).
* **El commit inicial es "tree vacío vs tree".** Usa `--root` para forzar un diff.
* **Los submódulos** muestran modo `160000` y un SHA (gitlink). No verás diffs internos a menos que hagas diff dentro del repositorio del submódulo.
* **Los Pathspecs van después de `--`.** Si filtras por rutas, ponlas después de `--` para evitar ambigüedad.
* **Nombres de archivo con espacios en blanco/nuevas líneas.** Siempre añade `-z` si estás analizando.

# Fragmentos rápidos de "chuleta" que realmente reutilizarás

```bash
# Archivos cambiados (lista plana)
git diff-tree --no-commit-id --name-only -r <commit>
```