---
audio: false
generated: true
lang: es
layout: post
title: Biblioteca de JavaScript para Markdown
translated: true
---

Parece que estás preguntando cómo usar la biblioteca `marked`, versión `^0.3.6`, que es una biblioteca de JavaScript para analizar texto Markdown y convertirlo a HTML. Dado que estás haciendo referencia a una versión específica con la notación `^0.3.6` (probablemente de un archivo `package.json` en un proyecto Node.js), te guiaré en el uso de esta versión más antigua de `marked`. Ten en cuenta que la versión `0.3.6` es bastante antigua (lanzada alrededor de 2016) y la biblioteca ha evolucionado significativamente desde entonces. Sin embargo, me ceñiré a lo que funciona para esa versión.

### Paso 1: Instalación
Si estás trabajando en un entorno Node.js, puedes instalar `marked` versión `0.3.6` usando npm:

```bash
npm install marked@0.3.6
```

El `^0.3.6` en un `package.json` significa que instalará `0.3.6` o cualquier actualización de parche compatible (por ejemplo, `0.3.7`), pero para mayor claridad, el comando anterior lo bloquea exactamente en `0.3.6`.

### Paso 2: Uso Básico
Aquí tienes cómo usar `marked` versión `0.3.6` en diferentes entornos:

#### En Node.js
1. **Requerir la biblioteca**:
   Crea un archivo (por ejemplo, `index.js`) y agrega lo siguiente:

   ```javascript
   var marked = require('marked');
   ```

2. **Convertir Markdown a HTML**:
   Usa la función `marked()` pasando una cadena de Markdown. Por ejemplo:

   ```javascript
   var markdownString = '# Hello World\nThis is **bold** text.';
   var html = marked(markdownString);
   console.log(html);
   ```

   **Salida**:
   ```html
   <h1>Hello World</h1>
   <p>This is <strong>bold</strong> text.</p>
   ```

#### En el Navegador
1. **Incluir la biblioteca**:
   Puedes usar un CDN o descargar `marked@0.3.6` e incluirlo a través de una etiqueta `<script>`. Por ejemplo, usando un enlace de CDN histórico (si está disponible) o un archivo local:

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **Usarlo en JavaScript**:
   Después de incluir el script, `marked` estará disponible globalmente:

   ```html
   <script>
     var markdownString = '# Hello World\nThis is **bold** text.';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### Paso 3: Opciones (para la versión 0.3.6)
La versión `0.3.6` admite algunas opciones de personalización. Puedes pasar un objeto de opciones como el segundo argumento a `marked()`. Aquí tienes un ejemplo:

```javascript
var markdownString = '# Hello\nThis is *text* with `code`.';
var html = marked(markdownString, {
  gfm: true,         // Habilita GitHub Flavored Markdown
  tables: true,      // Habilita tablas GFM
  breaks: false,     // Si es verdadero, agrega <br> en saltos de línea simples
  pedantic: false,   // Si es verdadero, sigue la especificación de Markdown estricta
  sanitize: false,   // Si es verdadero, elimina las etiquetas HTML para seguridad
  smartLists: true,  // Mejora el renderizado de listas
  smartypants: false // Si es verdadero, usa tipografía "inteligente" (por ejemplo, comillas curvas)
});
console.log(html);
```

### Características Clave en 0.3.6
- **Markdown Básico**: Soporta encabezados (`#`), negrita (`**`), cursiva (`*`), listas, bloques de código (```), etc.
- **Soporte GFM**: GitHub Flavored Markdown (como tablas y listas de tareas) está disponible si `gfm: true` está configurado.
- **Sin Personalización del Renderizador**: A diferencia de las versiones más nuevas, `0.3.6` no soporta renderizadores personalizados, por lo que estás limitado a su salida predeterminada.

### Ejemplo con Más Markdown
Aquí tienes un ejemplo más completo en Node.js:

```javascript
var marked = require('marked');

var markdown = `
# My Title
## Subtitle

- Item 1
- Item 2

\`\`\`
console.log("Hello");
\`\`\`

| Name  | Age |
|-------|-----|
| Alice | 25  |
| Bob   | 30  |
`;

var html = marked(markdown, { gfm: true, tables: true });
console.log(html);
```

**Salida**:
```html
<h1>My Title</h1>
<h2>Subtitle</h2>
<ul>
<li>Item 1</li>
<li>Item 2</li>
</ul>
<pre><code>console.log("Hello");
</code></pre>
<table>
<thead>
<tr>
<th>Name</th>
<th>Age</th>
</tr>
</thead>
<tbody>
<tr>
<td>Alice</td>
<td>25</td>
</tr>
<tr>
<td>Bob</td>
<td>30</td>
</tr>
</tbody>
</table>
```

### Notas
- **Sanitización**: Si estás renderizando entrada de usuario, establece `sanitize: true` para eliminar HTML crudo por seguridad (por ejemplo, etiquetas `<script>`). Sin embargo, esto es básico en `0.3.6` y no tan robusto como las alternativas modernas.
- **Limitaciones**: Esta versión carece de características añadidas en versiones posteriores (por ejemplo, análisis asíncrono, tokenizadores personalizados), por lo que si necesitas más, considera actualizar a una versión más nueva como `5.x`.
- **Depuración**: Si no funciona, asegúrate de que la biblioteca se haya cargado correctamente y verifica la sintaxis de Markdown.