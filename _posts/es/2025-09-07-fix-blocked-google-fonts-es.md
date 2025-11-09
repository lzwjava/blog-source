---
audio: false
date: 2025-09-07
generated: true
image: false
lang: es
layout: post
title: Cómo solucionar las solicitudes bloqueadas de Google Fonts
translated: true
type: note
---

Esa solicitud es tu página intentando cargar una hoja de estilos de fuentes web de Google Fonts:

* **Qué es:** `https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap` es el CSS que define las fuentes **Open Sans**. Tu tema o CSS personalizado lo está incluyendo para que el sitio se pueda renderizar con Open Sans.
* **Por qué ves “Status: — / 0 B / no headers”:** DevTools muestra eso cuando la solicitud es **bloqueada o cancelada** (por ejemplo, por un bloqueador de anuncios/privacidad, una Política de Seguridad de Contenido (CSP) estricta, una red inestable o un bloqueo a nivel de país). La página aún *intenta* solicitarla, de ahí la fila en la red.

### De dónde probablemente viene en un blog de Jekyll

Uno de estos suele ser cierto:

1. **El tema lo incluye en el `<head>`**
   Busca una línea como
   `<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap" rel="stylesheet">`
   en `_layouts/default.html` o `_includes/head.html` (o el equivalente del tema si usas `remote_theme`).

2. **SCSS lo importa**
   Revisa `/assets/css/*.scss` o `/_sass/**` buscando
   `@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,700&display=swap");`

3. **Tema remoto** (por ejemplo, jekyll-theme-cayman) incluye Google Fonts directamente en su include del head. Sobrescribir el head/layout del tema en tu repositorio te permitirá eliminarlo.

### Cómo encontrarlo rápidamente

Desde la raíz del repositorio de tu sitio, prueba cualquiera de estos comandos:

```
rg -n "fonts.googleapis.com"
rg -n "Open Sans"
rg -n "display=swap"
```

### Opciones para corregirlo o cambiarlo

**A) Eliminar Google Fonts y usar una pila de fuentes del sistema (más rápido y respetuoso con la privacidad)**

1. Elimina el `<link>` (o el `@import` de SCSS) que carga Google Fonts.
2. En tu hoja de estilos principal, establece una pila del sistema:

   ```css
   html, body {
     font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Ubuntu,
                  "Helvetica Neue", Arial, "Noto Sans", sans-serif,
                  "Apple Color Emoji", "Segoe UI Emoji";
   }
   ```

   (En Jekyll, coloca esto en `assets/css/style.scss` con líneas de front-matter `---` en la parte superior.)

**B) Mantener Open Sans pero auto-alojarla (self-host)**

1. Descarga los archivos WOFF2 para Open Sans (400 & 700) y colócalos en `assets/fonts/`.
2. Añade a tu CSS:

   ```css
   @font-face {
     font-family: "Open Sans";
     font-style: normal;
     font-weight: 400;
     font-display: swap;
     src: url("/assets/fonts/OpenSans-400.woff2") format("woff2");
   }
   @font-face {
     font-family: "Open Sans";
     font-style: normal;
     font-weight: 700;
     font-display: swap;
     src: url("/assets/fonts/OpenSans-700.woff2") format("woff2");
   }
   body { font-family: "Open Sans", system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; }
   ```
3. Elimina el `<link>`/`@import` de Google Fonts.

**C) Dejarlo como está pero evitar que la solicitud falle**

* Deshabilita la extensión bloqueadora para tu sitio, o relaja tu CSP para permitir `https://fonts.googleapis.com` y `https://fonts.gstatic.com`.
* Si estás en una región donde esos dominios están bloqueados, prefiere la opción A o B.

### Consejos específicos de Jekyll para sobrescribir

* **Tema remoto:** copia el `/_includes/head.html` o `/_layouts/default.html` del tema en tu repositorio con la misma ruta, elimina la línea de Google Fonts, y Jekyll usará tu versión sobrescrita.
* **Inclusión de head minificada:** a veces el tema inyecta las fuentes mediante una variable. Si es así, establece esa variable como vacía o sobrescribe el include para excluir las fuentes.

Si pegas el nombre de tu tema (o tu `theme` / `remote_theme` de `_config.yml`) puedo mostrarte el archivo exacto a sobrescribir y la diferencia mínima.