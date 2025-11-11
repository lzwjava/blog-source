---
audio: false
generated: true
lang: es
layout: post
title: Biblioteca JavaScript para Markdown
translated: true
type: note
---

Parece que estás preguntando sobre cómo usar la librería `marked`, versión `^0.3.6`, que es una librería de JavaScript para analizar texto Markdown y convertirlo a HTML. Ya que estás haciendo referencia a una versión específica con la notación `^0.3.6` (probablemente de un archivo `package.json` en un proyecto de Node.js), te guiaré sobre cómo usar esta versión antigua de `marked`. Ten en cuenta que la versión `0.3.6` es bastante antigua (lanzada alrededor del 2016), y la librería ha evolucionado significativamente desde entonces. Sin embargo, me ceñiré a lo que funciona para esa versión.

### Paso 1: Instalación
Si estás trabajando en un entorno de Node.js, puedes instalar `marked` versión `0.3.6` usando npm:

```bash
npm install marked@0.3.6
```

El `^0.3.6` en un `package.json` significa que instalará `0.3.6` o cualquier actualización de parche compatible (por ejemplo, `0.3.7`), pero para mayor claridad, el comando anterior la bloquea exactamente a `0.3.6`.

### Paso 2: Uso Básico
Aquí se explica cómo usar `marked` versión `0.3.6` en diferentes entornos:

#### En Node.js
1. **Requiere la librería**:
   Crea un archivo (por ejemplo, `index.js`) y agrega lo siguiente:

   ```javascript
   var marked = require('marked');
   ```

2. **Convierte Markdown a HTML**:
   Usa la función `marked()` pasándole una cadena de texto Markdown. Por ejemplo:

   ```javascript
   var markdownString = '# Hello World\nEste es un texto en **negrita**.';
   var html = marked(markdownString);
   console.log(html);
   ```

   **Salida**:
   ```html
   <h1>Hello World</h1>
   <p>Este es un texto en <strong>negrita</strong>.</p>
   ```

#### En el Navegador
1. **Incluye la librería**:
   Puedes usar un CDN o descargar `marked@0.3.6` e incluirla mediante una etiqueta `<script>`. Por ejemplo, usando un enlace histórico de CDN (si está disponible) o un archivo local:

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **Úsala en JavaScript**:
   Después de incluir el script, `marked` estará disponible globalmente:

   ```html
   <script>
     var markdownString = '# Hello World\nEste es un texto en **negrita**.';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### Paso 3: Opciones (para la versión 0.3.6)
La versión `0.3.6` admite algunas opciones de personalización. Puedes pasar un objeto de opciones como segundo argumento a `marked()`. Aquí hay un ejemplo:

```javascript
var markdownString = '# Hola\nEste es un *texto* con `código`.';
var html = marked(markdownString, {
  gfm: true,         // Habilitar GitHub Flavored Markdown
  tables: true,      // Habilitar tablas GFM
  breaks: false,     // Si es true, añade <br> en saltos de línea simples
  pedantic: false,   // Si es true, sigue la especificación estricta de Markdown
  sanitize: false,   // Si es true, elimina etiquetas HTML por seguridad
  smartLists: true,  // Mejora el renderizado de listas
  smartypants: false // Si es true, usa tipografía "inteligente" (por ejemplo, comillas curvas)
});
console.log(html);
```

### Características Clave en 0.3.6
- **Markdown Básico**: Admite encabezados (`#`), negrita (`**`), cursiva (`*`), listas, bloques de código (```), etc.
- **Soporte GFM**: GitHub Flavored Markdown (como tablas y listas de tareas) está disponible si se establece `gfm: true`.
- **Sin Personalización del Renderizador**: A diferencia de las versiones más nuevas, `0.3.6` no admite renderizadores personalizados, por lo que estás limitado a su salida predeterminada.

### Ejemplo con Más Markdown
Aquí hay un ejemplo más completo en Node.js:

```javascript
var marked = require('marked');

var markdown = `
# Mi Título
## Subtítulo

- Elemento 1
- Elemento 2

\`\`\`
console.log("Hola");
\`\`\`

| Nombre | Edad |
|--------|------|
| Alicia | 25   |
| Bob    | 30   |
`;

var html = marked(markdown, { gfm: true, tables: true });
console.log(html);
```

**Salida**:
```html
<h1>Mi Título</h1>
<h2>Subtítulo</h2>
<ul>
<li>Elemento 1</li>
<li>Elemento 2</li>
</ul>
<pre><code>console.log("Hola");
</code></pre>
<table>
<thead>
<tr>
<th>Nombre</th>
<th>Edad</th>
</tr>
</thead>
<tbody>
<tr>
<td>Alicia</td>
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
- **Saneamiento**: Si estás renderizando entrada de usuario, establece `sanitize: true` para eliminar HTML crudo por seguridad (por ejemplo, etiquetas `<script>`). Sin embargo, esto es básico en `0.3.6` y no es tan robusto como las alternativas modernas.
- **Limitaciones**: A esta versión le faltan características añadidas en lanzamientos posteriores (por ejemplo, análisis asíncrono, tokenizadores personalizados), así que si necesitas más, considera actualizar a una versión más nueva como `5.x`.
- **Depuración**: Si no funciona, asegúrate de que la librería se cargó correctamente y verifica la sintaxis de Markdown.