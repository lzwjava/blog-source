---
audio: false
generated: true
lang: es
layout: post
title: VSCode Envolver Líneas
translated: true
---

Para hacer que VSCode envuelva líneas para que puedas ver fácilmente cuando las líneas son demasiado largas, puedes configurar los ajustes de envuelto de palabras para envolver líneas en una columna específica. Aquí te dejo cómo hacerlo:

### Pasos para Habilitar el Envuelto de Líneas en una Columna Específica

1. **Abrir Configuración en VSCode**:
   - Presiona `Ctrl + ,` (o `Cmd + ,` en macOS) para abrir el panel de Configuración.
   - Alternativamente, ve a `Archivo` > `Preferencias` > `Configuración`.

2. **Buscar Ajustes de Envuelto de Palabras**:
   - En el panel de Configuración, escribe "word wrap" en la barra de búsqueda.
   - Localiza el ajuste etiquetado como **Editor: Word Wrap**.

3. **Establecer Envuelto de Palabras en "wordWrapColumn"**:
   - Cambia el ajuste **Editor: Word Wrap** a `"wordWrapColumn"`.
   - Esta opción permite que las líneas se envuelvan en una columna específica.

4. **Especificar el Límite de Columna**:
   - Busca el ajuste **Editor: Word Wrap Column** (aparece cuando se selecciona "wordWrapColumn").
   - Establece esto en tu límite de columna preferido, por ejemplo, `80`.
   - Esto significa que cualquier línea más larga que 80 caracteres se envolverá.

5. **(Opcional) Agregar una Regla Vertical para Guía Visual**:
   - Busca "rulers" en la barra de búsqueda de Configuración.
   - Encuentra el ajuste **Editor: Rulers**.
   - Agrega tu columna preferida a la lista, por ejemplo, `[80]`.
   - Esto mostrará una línea vertical en la columna 80, proporcionando una pista visual para el límite de longitud de línea.

6. **(Opcional) Ajustar el Envuelto de Sangría para Claridad**:
   - Busca "wrapping indent" en la barra de búsqueda de Configuración.
   - Encuentra el ajuste **Editor: Wrapping Indent**.
   - Establece esto en `"indent"` (o otra opción como `"deepIndent"`) para sangrar líneas envolvidas.
   - Esto ayuda a distinguir las líneas envolvidas de las nuevas líneas, haciendo que sea más claro que son continuaciones.

### Cómo Funciona

- Después de configurar estos ajustes, cualquier línea que exceda la columna especificada (por ejemplo, 80 caracteres) se envolverá y se mostrará en múltiples líneas visuales.
- Las líneas envolvidas se sangrarán (si ajustaste la sangría de envuelto), haciendo que sea fácil ver que son parte de la misma línea lógica.
- La regla vertical (si está habilitada) muestra una línea en la columna especificada, reforzando el límite visual.
- Al notar que una línea está envolviéndose, puedes decir rápidamente que es demasiado larga, ya que excede tu límite de columna.

### Ejemplo

Supongamos que tienes una línea de código que tiene 100 caracteres de largo:
- Con **Editor: Word Wrap** establecido en `"wordWrapColumn"` y **Editor: Word Wrap Column** establecido en `80`, la línea se envolverá en el carácter 80.
- La parte envolvida se sangrará y la regla (si está habilitada) mostrará dónde está la columna 80.
- Esta configuración elimina la necesidad de desplazamiento horizontal y hace que sea claro que la línea excede 80 caracteres.

### Notas Adicionales

- El envuelto es puramente visual; el código real permanece como una línea lógica, por lo que no afectará cómo se ejecuta o se formatea tu código.
- Si deseas hacer cumplir límites de longitud de línea estrictos, considera usar linters o formatters junto con estos ajustes visuales.
- Para verificaciones rápidas, también puedes referirte a la barra de estado en VSCode, que muestra el número de línea y columna actuales, pero el envuelto y la regla deberían ser suficientes para la identificación visual.

Siguiendo estos pasos, podrás ver fácilmente cuando las líneas son demasiado largas en VSCode sin desplazamiento horizontal, ya que se envolverán en tu límite de columna especificado.