---
audio: false
date: 2025-09-07
generated: true
image: false
lang: es
layout: post
title: Importación de Google Fonts en el Tema Cayman
translated: true
type: note
---

Sí — esa es muy probablemente la razón.

Cuando escribes:

```scss
@import "jekyll-theme-cayman";
```

no solo estás importando un archivo SCSS local — estás importando **la hoja de estilos completa del tema**, que a su vez contiene (o enlaza a) la importación de Google Fonts. Cayman usa **Open Sans** como su fuente predeterminada, y la obtiene de `https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap`.

Así que el flujo es el siguiente:

1. Tu SCSS dice `@import "jekyll-theme-cayman";`.
2. Jekyll expande eso en los archivos `_sass` del tema.
3. Dentro del SCSS de Cayman, hay una línea como:

   ```scss
   @import url("https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap");
   ```
4. Esa es la solicitud de red que ves en DevTools.

---

### Cómo eliminar o reemplazar

* **Reemplazar la importación de la fuente**: Copia el SCSS principal del tema en tu proyecto (por ejemplo, `assets/css/style.scss`), elimina la línea de Google Fonts y dile a Jekyll que no la importe.

* **Simplemente reemplazar la familia de fuentes**: Mantén el resto de Cayman pero fuerza una pila de fuentes del sistema en tu propio CSS:

  ```css
  html, body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu,
                 "Helvetica Neue", Arial, "Noto Sans", sans-serif;
  }
  ```

  Incluso si la solicitud a Google Fonts ocurre, el navegador no la usará.

* **Alojar Open Sans localmente**: Si te gusta Open Sans pero no quieres la llamada externa, descarga los archivos de la fuente y defínelos con `@font-face` en tu propio CSS, luego elimina el `@import url(...)` de Cayman.

---

👉 Si quieres, puedo mostrarte exactamente qué archivo SCSS de Cayman tiene la línea de Google Fonts y cómo reemplazarlo de forma limpia en tu configuración de Jekyll. ¿Quieres que te lo explique paso a paso?