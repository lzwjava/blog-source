---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Descripción General del Comando Git Check-Ignore
translated: true
type: note
---

### ¿Qué es `git check-ignore`?

El comando `git check-ignore` es una herramienta de Git utilizada para determinar si un archivo o ruta específica es ignorado por los mecanismos de ignorar de Git, como los archivos `.gitignore`, `.git/info/exclude` o los archivos de ignorar globales (a través de `core.excludesFile`). Es particularmente útil para depurar por qué un archivo no está siendo rastreado o añadido al repositorio.

Si la ruta es ignorada, el comando imprime la ruta (y opcionalmente el patrón coincidente). Si no es ignorada, no hay salida (código de salida 0). Esto lo hace apto para scripts y automatización.

### Uso Básico

Ejecútalo con una o más rutas para verificar:

```
git check-ignore <ruta>...
```

- **Ejemplo**: Verificar si un solo archivo es ignorado:
  ```
  git check-ignore ruta/a/miarchivo.txt
  ```
  - Salida: Si es ignorado, imprime `ruta/a/miarchivo.txt`. Si no, no imprime nada.

- **Ejemplo**: Verificar múltiples archivos:
  ```
  git check-ignore archivo1.txt archivo2.txt directorio/archivo3.txt
  ```
  - Imprime solo las rutas ignoradas, una por línea.

### Opciones Clave

| Opción | Descripción | Ejemplo |
|--------|-------------|---------|
| `-v`, `--verbose` | Muestra el patrón de ignorar que coincidió (ej., la línea de `.gitignore`). | `git check-ignore -v ruta/a/miarchivo.txt`<br>Salida: `ruta/a/miarchivo.txt: .gitignore:1:*.txt` (ruta + archivo:línea:patrón) |
| `-q`, `--quiet` | Suprime la salida, pero aún usa el código de salida (0 si no es ignorado, 1 si es ignorado). Útil en scripts. | `git check-ignore -q ruta/a/miarchivo.txt`<br>(Sin salida; verificar `$?` para el código de salida) |
| `--stdin` | Lee las rutas desde la entrada estándar en lugar de la línea de comandos. | `echo "archivo1.txt\narchivo2.txt" \| git check-ignore --stdin` |
| `--non-matching` | Invierte la salida: Muestra las rutas que *no* son ignoradas. | `git check-ignore --non-matching -v archivo1.txt archivo2.txt` |

### Casos de Uso Comunes

1. **Depurar Reglas de `.gitignore`**:
   - Si `git status` no muestra un archivo que esperas, ejecuta `git check-ignore -v <archivo>` para ver exactamente qué regla lo está ignorando.
   - Ejemplo de salida: `src/logs/app.log: .gitignore:5:logs/*` (indicando que la línea 5 en `.gitignore` coincide).

2. **En Scripts**:
   - Verificar si un archivo debería ser añadido:
     ```
     if git check-ignore -q miarchivo.txt; then
         echo "El archivo es ignorado, omitiendo..."
     else
         git add miarchivo.txt
     fi
     ```

3. **Verificación por Lotes**:
   - Listar todos los archivos ignorados en un directorio:
     ```
     find . -type f -print0 | xargs -0 git check-ignore
     ```

### Consejos
- Respeta la pila de ignorar de Git: `.gitignore` local, exclusiones globales, etc.
- Funciona en archivos no rastreados o aquellos ya en el repositorio (pero verifica contra las reglas de ignorar).
- Para más detalles, consulta la documentación oficial.

[Documentación de Git check-ignore](https://git-scm.com/docs/git-check-ignore)  
[Stack Overflow: Comando de Git para mostrar qué archivos específicos son ignorados](https://stackoverflow.com/questions/466764/git-command-to-show-which-specific-files-are-ignored-by-gitignore)  
[Usando git check-ignore para depurar tu .gitignore](https://alexwlchan.net/til/2020/using-git-check-ignore-to-debug-your-gitignore/)