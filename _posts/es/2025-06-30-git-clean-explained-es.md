---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Comando Git Clean Explicado
translated: true
type: note
---

### Qué hace el comando
El comando `git clean -f -d` (asumiendo que "clean clean" es un error tipográfico y querías decir `git clean`) elimina archivos y directorios no rastreados de tu directorio de trabajo de Git. Las banderas se desglosan así:
- `-f` (force): Requerida para eliminar archivos realmente, ya que Git no los eliminará por defecto para evitar pérdida accidental de datos.
- `-d` (directories): Extiende la limpieza para incluir directorios no rastreados, no solo archivos.

Escribiste `-fd -f`, que combina `-f -d -f`. Como `-f` aparece dos veces, es redundante pero inofensivo—las banderas pueden repetirse sin problema. Si quisiste decir algo diferente, ¡aclaralo!

### Cómo funciona
Git clean opera en el árbol de trabajo (tus archivos locales), no en el repositorio en sí. Aquí un desglose paso a paso de su comportamiento:

1. **Escanea el Directorio de Trabajo**: Identifica elementos "no rastreados"—archivos/directorios que no están en el índice de Git o rastreados por ningún commit. Ejemplos: archivos temporales como `*.log`, artefactos de compilación, o directorios vacíos de ramas eliminadas.

2. **Aplica Opciones**:
   - Sin `-f`, solo muestra lo que se eliminaría (modo de simulacro). Con `-f`, procede a eliminar.
   - Sin `-d`, omite directorios. Con `-d`, elimina directorios vacíos o recursivamente vacíos que contengan archivos no rastreados.
   - Respeta el archivo `.gitignore` por defecto: los archivos ignorados permanecen intactos a menos que agregues `-x` (eXcluir de las reglas de ignore) o `-X` (solo limpiar archivos ignorados).

3. **Medidas de Seguridad**: Git advierte si no se usa `-f`. No eliminará archivos en directorios ignorados a menos que se le indique explícitamente. Ejecuta `git clean --dry-run -f -d` primero para previsualizar los cambios.

4. **Ejemplo de Uso**:
   - Para limpiar interactivamente: `git clean -i` (pregunta por cada elemento).
   - Flujo de trabajo típico: Después de `git reset`, usa este comando para igualar exactamente tu último commit.

### Advertencias y Comprobación
- **Riesgo**: Eliminar archivos es irreversible sin copias de seguridad o `git reflog`. Siempre haz commit del trabajo importante primero.
- **Evidencia de la Documentación de Git**: La documentación oficial de Git (ej., `man git-clean` o docs en git-scm.com) confirma esto: `-f` fuerza la eliminación, `-d` incluye directorios. Usa operaciones del sistema de archivos como `unlink` y `rmdir`, pero solo en elementos no rastreados para evitar corromper datos rastreados.
- **Consejo de Prueba**: En un repositorio de prueba, crea un archivo y directorio no rastreados, luego ejecuta el comando—observa la salida y los cambios en el sistema de archivos.

Si esto no coincide con tu intención, ¡proporciona más contexto!