---
audio: false
generated: true
lang: es
layout: post
title: VSCode Ajuste de Líneas
translated: true
type: note
---

Para hacer que VSCode ajuste las líneas y así puedas ver fácilmente cuándo son demasiado largas, puedes configurar los ajustes de ajuste de línea para que se envuelvan en una columna específica. Aquí te explicamos cómo hacerlo:

### Pasos para habilitar el ajuste de línea en una columna específica

1. **Abrir Configuración en VSCode**:
   - Presiona `Ctrl + ,` (o `Cmd + ,` en macOS) para abrir el panel de Configuración.
   - Alternativamente, ve a `Archivo` > `Preferencias` > `Configuración`.

2. **Buscar los ajustes de Ajuste de Línea**:
   - En el panel de Configuración, escribe "word wrap" en la barra de búsqueda.
   - Localiza el ajuste llamado **Editor: Word Wrap**.

3. **Establecer Word Wrap a "wordWrapColumn"**:
   - Cambia el ajuste **Editor: Word Wrap** a `"wordWrapColumn"`.
   - Esta opción permite que las líneas se ajusten en una columna específica.

4. **Especificar el Límite de Columna**:
   - Busca el ajuste **Editor: Word Wrap Column** (aparece cuando se selecciona "wordWrapColumn").
   - Establécelo a tu límite de columna preferido, por ejemplo, `80`.
   - Esto significa que cualquier línea más larga de 80 caracteres se ajustará.

5. **(Opcional) Añadir una Regla Vertical para Guía Visual**:
   - Busca "rulers" en la barra de búsqueda de Configuración.
   - Encuentra el ajuste **Editor: Rulers**.
   - Añade tu columna preferida a la lista, por ejemplo, `[80]`.
   - Esto mostrará una línea vertical en la columna 80, proporcionando una referencia visual para el límite de longitud de línea.

6. **(Opcional) Ajustar la Sangría del Ajuste para Mayor Claridad**:
   - Busca "wrapping indent" en la barra de búsqueda de Configuración.
   - Encuentra el ajuste **Editor: Wrapping Indent**.
   - Establécelo a `"indent"` (u otra opción como `"deepIndent"`) para sangrar las líneas ajustadas.
   - Esto ayuda a distinguir las líneas ajustadas de las nuevas líneas, haciendo más claro que son continuaciones.

### Cómo Funciona

- Después de configurar estos ajustes, cualquier línea que exceda la columna especificada (ej. 80 caracteres) se ajustará y se mostrará en múltiples líneas visuales.
- Las líneas ajustadas se sangran (si ajustaste la sangría del ajuste), haciendo fácil ver que son parte de la misma línea lógica.
- La regla vertical (si está habilitada) muestra una línea en la columna especificada, reforzando el límite visual.
- Al notar que una línea se ha ajustado, puedes ver rápidamente que es demasiado larga, ya que excede tu límite de columna.

### Ejemplo

Supongamos que tienes una línea de código de 100 caracteres de longitud:
- Con **Editor: Word Wrap** establecido en `"wordWrapColumn"` y **Editor: Word Wrap Column** establecido en `80`, la línea se ajustará en el carácter 80.
- La parte ajustada se sangrará, y la regla (si está habilitada) mostrará dónde está la columna 80.
- Esta configuración elimina la necesidad de desplazamiento horizontal y deja claro que la línea excede los 80 caracteres.

### Notas Adicionales

- El ajuste es puramente visual; el código real permanece como una línea lógica, por lo que no afectará cómo se ejecuta o formatea tu código.
- Si deseas aplicar límites estrictos de longitud de línea, considera usar linters o formateadores junto con estos ajustes visuales.
- Para comprobaciones rápidas, también puedes consultar la barra de estado en VSCode, que muestra el número de línea y columna actual, pero el ajuste y la regla deberían ser suficientes para la identificación visual.

Siguiendo estos pasos, puedes ver fácilmente cuándo las líneas son demasiado largas en VSCode sin necesidad de desplazamiento horizontal, ya que se ajustarán en tu límite de columna especificado.