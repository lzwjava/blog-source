---
audio: false
generated: true
lang: es
layout: post
title: Habilitar Ajuste Suave en Zed
translated: true
type: note
---

Zed, como muchos editores de texto modernos, utiliza el concepto de "soft wrap" (ajuste suave) para ajustar las líneas. Esto significa que las líneas aparecerán ajustadas en el editor, pero no se insertan caracteres de nueva línea reales en tu archivo.

Aquí se explica cómo habilitar el ajuste de líneas en Zed:

1.  **Abre la Configuración de Zed:**

      * Presiona `Command + Shift + P` (macOS) o `Ctrl + Shift + P` (Windows/Linux) para abrir la Paleta de Comandos.
      * Escribe "local" y selecciona "zed: Open Local Settings". Esto abrirá tu archivo `settings.json`.

2.  **Añade la configuración `soft_wrap`:**

      * En tu archivo `settings.json`, añade o modifica la configuración `"soft_wrap"`. Tienes algunas opciones:

          * **`"editor_width"`:** Esta es la opción más común y generalmente recomendada. Ajustará las líneas para que se adapten al ancho actual de la ventana del editor.
            ```json
            {
              "soft_wrap": "editor_width"
            }
            ```
          * **`"preferred_line_length"`:** Esto ajustará las líneas basándose en una `preferred_line_length` especificada (por ejemplo, 80 caracteres). También necesitarás definir `preferred_line_length`.
            ```json
            {
              "soft_wrap": "preferred_line_length",
              "preferred_line_length": 80
            }
            ```
          * **`"bounded"`:** Esta opción proporciona un comportamiento de ajuste más avanzado, aunque `editor_width` o `preferred_line_length` suelen ser suficientes para la mayoría de usuarios.
          * **`"none"`:** Esto desactiva el ajuste de líneas.

3.  **Guarda el archivo:**

      * Presiona `Command + S` (macOS) o `Ctrl + S` (Windows/Linux) para guardar el archivo `settings.json`.

Zed ahora debería ajustar las líneas según tu configuración elegida.

**Notas Importantes:**

  * **Configuración a nivel de proyecto:** También puedes habilitar el ajuste de palabras a nivel de proyecto creando una carpeta `.zed` en el directorio de tu proyecto y colocando un archivo `settings.json` dentro de ella con la configuración `soft_wrap` deseada. Esto anulará tu configuración global para ese proyecto específico.
  * **Configuración específica del lenguaje:** Incluso puedes configurar `soft_wrap` para lenguajes específicos. Por ejemplo, para establecer el ajuste suave para archivos Markdown:
    ```json
    {
      "languages": {
        "Markdown": {
          "soft_wrap": "editor_width"
        }
      }
    }
    ```
  * **Comando "Rewrap":** Si estás buscando un comando para "ajustar" el texto (insertar nuevas líneas reales) en lugar de solo un ajuste visual, Zed también tiene un comando "Rewrap" (a menudo asignado a `Alt-Q` o `Alt-W`). Esto es útil para formatear comentarios o líneas largas de prosa.