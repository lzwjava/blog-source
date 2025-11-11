---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Optimización de la Recolección de Basura en Git Explicada
translated: true
type: note
---

### Qué hace Git GC

Git GC (recolección de basura) es un comando de mantenimiento que optimiza tu repositorio de Git limpiando archivos innecesarios y comprimiendo datos para ahorrar espacio y mejorar el rendimiento. Opera en el directorio `.git`, que almacena todo el historial, objetos y metadatos de un repositorio.

Acciones clave que realiza:

- **Poda de objetos inalcanzables**: Elimina commits, árboles y blobs que ya no están referenciados (por ejemplo, después de un rebase o eliminar ramas). Estos se convierten en "objetos sueltos" en `.git/objects`, y GC los limpia.
- **Reempaquetado de objetos**: Comprime los objetos sueltos (almacenados individualmente) en archivos pack (`.git/objects/pack`), que son más eficientes. Esto usa compresión delta para almacenar diferencias entre archivos similares, reduciendo el uso del disco.
- **Actualización de referencias**: Actualiza el estado interno del repositorio, como reescribir el índice del pack para búsquedas más rápidas.
- **Ejecución de herramientas relacionadas**: A menudo invoca comandos como `git prune`, `git repack` y `git rerere` (para reutilización de resolución) como parte del proceso.

Evidencia: Según la documentación oficial de Git (por ejemplo, `git gc --help`), GC está diseñado para el "mantenimiento" de los repositorios. Por ejemplo, un repositorio con 10,000 objetos sueltos podría reducirse de cientos de MB a una fracción una vez empaquetado, ya que la compresión delta aprovecha las similitudes (por ejemplo, entre versiones de archivos en un historial de código).

### Cómo funciona internamente

1.  **Disparadores**: GC se ejecuta manualmente mediante `git gc` o automáticamente cuando Git detecta ciertas condiciones (ver más abajo). No se ejecuta en cada comando para evitar ralentizaciones.
2.  **Proceso**:
    - Cuenta objetos sueltos y archivos pack.
    - Si se superan los umbrales (por ejemplo, >6,700 objetos sueltos por defecto, configurable mediante `gc.auto`), reempaqueta de forma agresiva.
    - Crea archivos temporales (por ejemplo, `.git/objects/tmp_*`) para evitar pérdida de datos, luego los intercambia atómicamente.
    - Los modos más suaves como `git gc --auto` solo podan sin un reempaquetado completo.
3.  **Detalles de compresión**: Utiliza zlib para la compresión. El reempaquetado construye archivos pack donde los objetos se almacenan como deltas (diferencias) de objetos base, haciéndolo eficiente para repositorios con código en evolución; por ejemplo, agregar una línea a un archivo en una base de código grande crea un delta pequeño en lugar de duplicar el archivo completo.

Esto está respaldado por el código fuente de Git (disponible en GitHub), que implementa GC como una serie de llamadas a shell a utilidades de poda y empaquetado para garantizar confiabilidad.

### Por qué se ejecuta de repente

GC a menudo se dispara "repentinamente" porque es automático, no en tiempo real, para equilibrar el rendimiento. Razones comunes:

- **Se alcanzan umbrales**: Después de acumular objetos sueltos (por ejemplo, de commits o fetches frecuentes sin empaquetar). Git verifica esto después de operaciones como `git commit`, `git merge` o `push`. Si los objetos sueltos exceden el límite `gc.auto` (por defecto: alrededor de 6,700), se ejecuta. Por eso puede ocurrir después de una ráfaga de actividad, pareciendo "repentino".
- **Programación de poda**: Si `gc.prune` está configurado, pode las refs obsoletas periódicamente, pero el auto-GC principal se basa en el recuento de objetos.
- **Operaciones grandes**: El rebase pesado o la clonación pueden generar muchos objetos sueltos rápidamente, disparándolo.
- **Hooks post-comando**: Algunos flujos de trabajo o herramientas (por ejemplo, hooks de Git o IDEs) pueden invocar `git gc` después de grandes cambios.

Para controlarlo: Ajusta configuraciones como `git config --global gc.auto 0` para desactivar el auto-GC si prefieres ejecuciones manuales, o aumenta el umbral para reducir las interrupciones. Ejecutarlo evita que los repositorios se inflen; por ejemplo, el repositorio del kernel de Linux usa GC para mantener el historial manejable a pesar de su escala masiva. Si los problemas persisten, verifica `git count-objects -v` para ver estadísticas de objetos sueltos.