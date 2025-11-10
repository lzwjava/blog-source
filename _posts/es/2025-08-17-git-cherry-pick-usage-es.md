---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Descripción General y Uso de Git Cherry-Pick
translated: true
type: note
---

### ¿Qué es Git Cherry-Pick?

Git cherry-pick es un comando que te permite aplicar los cambios de una confirmación específica (o un conjunto de confirmaciones) a tu rama actual, creando una nueva confirmación con esos cambios. Es útil cuando quieres tomar una corrección o característica particular de una rama sin fusionar la rama completa. A diferencia de un merge, que integra todo el historial, cherry-pick copia los cambios de forma selectiva.

### Cómo funciona Git Cherry-Pick internamente

1. **Seleccionar la Confirmación**: Especificas un hash de confirmación (por ejemplo, mediante `git log` para encontrarlo) que contiene los cambios que deseas.

2. **Aplicar Cambios**: Git toma el diff (los cambios reales de código) de esa confirmación e intenta aplicarlo al directorio de trabajo de tu rama actual, utilizando la lógica de fusión de tres vías de Git cuando es posible.

3. **Crear Nueva Confirmación**: Si tiene éxito, se realiza una nueva confirmación en tu rama con:
   - Los mismos cambios que la confirmación original.
   - Un nuevo hash de confirmación (porque es una confirmación nueva).
   - Un mensaje de confirmación que hace referencia al original (por ejemplo, mediante la bandera -x para añadir "cherry picked from commit <hash>").

   Si hay conflictos de fusión (por ejemplo, la rama destino tiene cambios incompatibles), Git se pausa y te permite resolverlos manualmente antes de confirmar.

El proceso no altera el historial de la confirmación original—solo copia los cambios. Esto hace que cherry-pick sea excelente para backporting de correcciones de errores o para aplicar características de forma selectiva.

### Pasos de uso básico

1. Asegúrate de estar en la rama destino (cambia con `git checkout <rama>`).
2. Encuentra el hash de la confirmación que deseas (por ejemplo, `git log --oneline`).
3. Ejecuta: `git cherry-pick <hash-de-confirmación>`
   - Para múltiples: `git cherry-pick <hash1> <hash2>`
   - Con opciones como `-n` (sin confirmar, para staging) o `-x` (referenciar el original).

4. Si surgen conflictos, edita los archivos, añádelos al staging con `git add`, y luego `git cherry-pick --continue`.
5. Si abortas a mitad de camino: `git cherry-pick --abort`.

### Escenario de ejemplo

Supón que tienes una rama de características con las confirmaciones A -> B -> C, y quieres hacer cherry-pick de la confirmación B a la rama main.

- En main: `git checkout main`
- `git cherry-pick B` (reemplazando B con el hash real)

Esto añade los cambios de B como una nueva confirmación D en main, sin incorporar A o C. La confirmación B original permanece en la rama de características.

### Advertencias y consejos

- Evita hacer cherry-pick de merges (confirmaciones con múltiples padres), ya que puede causar problemas—usa `git cherry-pick -m 1 <merge-commit>` para especificar un padre.
- No conserva los metadatos de la confirmación, como la fecha del autor, pero `git cherry-pick --edit` te permite modificar el mensaje.
- Para cambios en secuencia, haz cherry-pick de múltiples confirmaciones en orden para evitar dependencias faltantes.
- Siempre prueba después de hacer cherry-pick, ya que podría introducir errores si los contextos son diferentes.

Para más detalles, la documentación oficial de Git proporciona una guía completa: https://git-scm.com/docs/git-cherry-pick. Si tienes problemas específicos, ¡comparte la salida de tu `git log`!