---
audio: false
generated: true
lang: es
layout: post
title: Estilo de Markdown de GitHub
translated: true
type: note
---

### Puntos Clave
- Parece probable que para usar el paquete npm "github-markdown-css", primero lo instales con `npm install github-markdown-css`.
- La investigación sugiere que luego importes el archivo CSS a tu proyecto y envuelvas tu contenido Markdown en un div con la clase "markdown-body".
- La evidencia indica que es recomendable establecer un ancho y un padding opcionales para igualar el estilo de GitHub, y asegurar un DOctype para evitar problemas de estilos.

### Instalación
Comienza instalando el paquete usando npm en el directorio de tu proyecto:
- Ejecuta `npm install github-markdown-css` para agregarlo a tus dependencias.

### Uso
Después de la instalación, integra el CSS en tu proyecto:
- Importa el archivo CSS, por ejemplo, en JavaScript/React con `import 'github-markdown-css';`.
- Envuelve tu contenido Markdown renderizado en un `<div class="markdown-body">...</div>` para aplicar los estilos.
- Opcionalmente, agrega CSS para el ancho y el padding para imitar el aspecto de GitHub:
  ```css
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  ```
- Asegúrate de que tu HTML incluya un DOctype (por ejemplo, `<!DOCTYPE html>`) para evitar problemas de modo de compatibilidad (quirks mode), que podrían afectar el estilo.

### Detalle Inesperado
Podría sorprenderte que el paquete también admite la generación de CSS personalizado a través de un paquete relacionado, [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css), si necesitas estilos a medida.

---

### Nota de Estudio: Guía Completa para Usar el Paquete npm github-markdown-css

Esta guía detallada explora el uso del paquete npm "github-markdown-css", diseñado para replicar el estilo de Markdown de GitHub en proyectos web. Proporciona un enfoque paso a paso para la instalación e integración, junto con consideraciones adicionales para un uso óptimo, especialmente en varios contextos de desarrollo como React o HTML plano. La información se deriva de la documentación oficial del paquete, repositorios de GitHub y recursos web relacionados, asegurando una comprensión exhaustiva para desarrolladores de todos los niveles.

#### Antecedentes y Propósito
El paquete "github-markdown-css", mantenido por [sindresorhus](https://github.com/sindresorhus), ofrece un conjunto mínimo de CSS para emular el estilo de renderizado de Markdown de GitHub. Esto es particularmente útil para desarrolladores que desean que su contenido Markdown, como documentación o publicaciones de blog, aparezca consistente con la presentación familiar y limpia de GitHub. El paquete es ampliamente utilizado, con más de 1,168 otros proyectos en el registro de npm utilizándolo, lo que indica su popularidad y confiabilidad según actualizaciones recientes.

#### Proceso de Instalación
Para comenzar, necesitas instalar el paquete a través de npm, el administrador de paquetes de Node.js. El comando es sencillo:
- Ejecuta `npm install github-markdown-css` en el directorio de tu proyecto. Esto agrega el paquete a tu carpeta `node_modules` y actualiza tu `package.json` con la dependencia.

La última versión del paquete, según verificaciones recientes, es la 5.8.1, publicada por última vez hace unos tres meses, lo que sugiere un mantenimiento y actualizaciones activos. Esto asegura la compatibilidad con las prácticas y frameworks modernos de desarrollo web.

#### Integración y Uso
Una vez instalado, el siguiente paso es integrar el CSS en tu proyecto. El paquete proporciona un archivo llamado `github-markdown.css`, que puedes importar dependiendo de la configuración de tu proyecto:

- **Para JavaScript/Frameworks Modernos (por ejemplo, React, Vue):**
  - Usa una sentencia de importación en tus archivos JavaScript o TypeScript, como `import 'github-markdown-css';`. Esto funciona bien con empaquetadores como Webpack o Vite, que manejan las importaciones de CSS sin problemas.
  - Para React, podrías ver ejemplos donde los desarrolladores lo importan en un archivo de componente, asegurando que los estilos estén disponibles globalmente o con el alcance necesario.

- **Para HTML Plano:**
  - Enlaza el archivo CSS directamente en la sección head de tu HTML:
    ```html
    <link rel="stylesheet" href="node_modules/github-markdown-css/github-markdown.css">
    ```
  - Ten en cuenta que la ruta puede variar según la estructura de tu proyecto; asegúrate de que la ruta relativa apunte correctamente al directorio `node_modules`.

Después de importar, aplica los estilos envolviendo tu contenido Markdown renderizado en un `<div>` con la clase "markdown-body". Por ejemplo:
```html
<div class="markdown-body">
  <h1>Unicorns</h1>
  <p>All the things</p>
</div>
```
Esta clase es crucial ya que el CSS apunta a los elementos dentro de `.markdown-body` para aplicar un estilo similar al de GitHub, incluyendo tipografía, bloques de código, tablas y más.

#### Consideraciones de Estilo
Para replicar completamente la apariencia de Markdown de GitHub, considera establecer el ancho y el padding para la clase `.markdown-body`. La documentación sugiere:
- Un ancho máximo de 980px, con 45px de padding en pantallas más grandes, y 15px de padding en dispositivos móviles (pantallas ≤ 767px).
- Puedes lograr esto con el siguiente CSS:
  ```css
  .markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
  }
  @media (max-width: 767px) {
    .markdown-body {
      padding: 15px;
    }
  }
  ```
Esto asegura la capacidad de respuesta y se alinea con el diseño de GitHub, mejorando la legibilidad y la experiencia del usuario.

#### Notas Técnicas y Mejores Prácticas
- **Requisito de DOctype:** La documentación destaca posibles problemas de estilo, como que las tablas en modo oscuro se rendericen incorrectamente, si el navegador entra en modo de compatibilidad (quirks mode). Para evitar esto, incluye siempre un DOctype en la parte superior de tu HTML, como `<!DOCTYPE html>`. Esto asegura un renderizado compatible con los estándares y evita comportamientos inesperados.
- **Análisis de Markdown:** Si bien el paquete proporciona CSS, no analiza (parsea) Markdown a HTML. Necesitarás un analizador de Markdown como [marked.js](https://marked.js.org/) o [react-markdown](https://github.com/remarkjs/react-markdown) para proyectos en React para convertir texto Markdown a HTML, que luego puede ser estilizado con este CSS.
- **Generación de CSS Personalizado:** Para usuarios avanzados, el paquete relacionado [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) permite generar CSS personalizado, potencialmente útil para temas específicos o modificaciones. Este es un detalle inesperado para aquellos que podrían asumir que el paquete es solo para uso directo.

#### Uso en Contextos Específicos
- **Proyectos React:** En React, es común combinar `github-markdown-css` con `react-markdown`. Después de instalar ambos, importa el CSS y usa el componente:
  ```javascript
  import React from 'react';
  import ReactMarkdown from 'react-markdown';
  import 'github-markdown-css';

  const MarkdownComponent = () => (
    <div className="markdown-body">
      <ReactMarkdown># Hello, World!</ReactMarkdown>
    </div>
  );
  ```
  Asegúrate de también establecer el CSS de ancho y padding como se mostró anteriormente para el estilo completo de GitHub.

- **HTML Plano con CDN:** Para prototipos rápidos, puedes usar una versión CDN, disponible en [cdnjs](https://cdnjs.com/libraries/github-markdown-css), enlazando directamente:
  ```html
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.8.1/github-markdown.min.css">
  ```
  Luego aplica la clase `.markdown-body` como antes.

#### Posibles Problemas y Soluciones
- **Conflictos de Estilo:** Si tu proyecto utiliza otros frameworks CSS (por ejemplo, Tailwind, Bootstrap), asegúrate de que no haya conflictos de especificidad. La clase `.markdown-body` debería anular la mayoría de los estilos, pero prueba exhaustivamente.
- **Soporte para Modo Oscuro:** El paquete incluye soporte para modo oscuro, pero asegúrate de que tu analizador de Markdown y la configuración del proyecto manejen correctamente el cambio de tema, especialmente para bloques de código y tablas.
- **Compatibilidad del Navegador:** Dado el uso generalizado del paquete, la compatibilidad es generalmente buena, pero siempre prueba en los principales navegadores (Chrome, Firefox, Safari) para asegurar un renderizado consistente.

#### Análisis Comparativo
En comparación con otras opciones de CSS para Markdown, como [Markdown CSS](https://markdowncss.github.io/), "github-markdown-css" se destaca por su replicación directa del estilo de GitHub, lo que lo hace ideal para documentación que refleja la apariencia de GitHub. Sin embargo, carece de opciones de temas integrados sin personalización adicional, a diferencia de algunas alternativas que ofrecen múltiples temas listos para usar.

#### Tabla: Características Clave y Consideraciones

| Característica           | Descripción                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Comando de Instalación   | `npm install github-markdown-css`                                           |
| Método de Importación CSS| `import 'github-markdown-css';` o `<link>` en HTML                          |
| Clase Requerida          | `.markdown-body` para aplicar el estilo                                     |
| Ancho y Padding          | Máx. 980px, 45px padding (escritorio); 15px padding (móvil ≤ 767px)         |
| Requisito de DOctype     | Esencial para evitar el modo de compatibilidad y asegurar el renderizado correcto |
| Generación de CSS Personalizado | Posible vía [generate-github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css) |
| Compatibilidad           | Funciona con analizadores de Markdown como marked.js, react-markdown; amplio soporte de navegadores |

#### Conclusión
Usar "github-markdown-css" es sencillo para desarrolladores que buscan replicar el estilo de Markdown de GitHub. Siguiendo los pasos de instalación e integración, y considerando las notas técnicas y de estilo adicionales, puedes lograr un aspecto consistente y profesional para tu contenido Markdown. Para personalizaciones avanzadas, explora el paquete de generación, y siempre prueba para detectar problemas de compatibilidad y renderizado, especialmente en proyectos complejos.

#### Citas Clave
- [Página del paquete npm github-markdown-css](https://www.npmjs.com/package/github-markdown-css)
- [Repositorio de GitHub: La cantidad mínima de CSS para replicar el estilo de GitHub Markdown](https://github.com/sindresorhus/github-markdown-css)
- [Página de demostración de GitHub Markdown CSS](https://sindresorhus.com/github-markdown-css/)
- [Paquete npm para generar el CSS para github-markdown-css](https://www.npmjs.com/package/generate-github-markdown-css)
- [CDN de github-markdown-css por cdnjs](https://cdnjs.com/libraries/github-markdown-css)