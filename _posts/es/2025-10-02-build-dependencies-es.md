---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-code-fast-1
title: Dependencias de Desarrollo y Herramientas de Compilación
translated: true
type: note
---

### DevDependencies
Estos son paquetes utilizados durante el desarrollo, no incluidos en la build final.

- **babel-core** (6.13.0): Compilador principal de Babel para transpilar JavaScript moderno (ES6+) a ES5 para una mayor compatibilidad con navegadores.
- **babel-loader** (6.2.5): Loader de Webpack que integra Babel para la transformación de JavaScript en los procesos de build.
- **babel-plugin-transform-runtime** (6.12.0): Plugin de Babel que reutiliza ayudantes de runtime para reducir el tamaño del bundle en el código transpilado.
- **babel-preset-es2015** (6.13.2): Preset de Babel para compilar características de ES2015 (ES6) a ES5.
- **babel-runtime** (6.11.6): Librería de runtime que proporciona polyfills y ayudantes para el código transpilado con Babel.
- **cross-env** (^1.0.8): Establece variables de entorno multiplataforma (ej. NODE_ENV) sin diferencias de shell.
- **css-loader** (^0.23.1): Carga y procesa archivos CSS, resolviendo imports y dependencias.
- **detect-indent** (4.0.0): Detecta el estilo de indentación (espacios/tabs) de los archivos para un formato consistente.
- **exports-loader** (^0.6.3): Hace que las exportaciones de módulos estén disponibles en diferentes contextos (ej. para módulos no AMD).
- **extract-text-webpack-plugin** (^1.0.1): Extrae CSS de los bundles de JavaScript en archivos separados para un mejor rendimiento.
- **file-loader** (0.9.0): Maneja la carga de archivos (ej. imágenes) emitiéndolos al directorio de salida y devolviendo URLs.
- **html-webpack-plugin** (^2.22.0): Genera archivos HTML e inyecta los assets empaquetados, simplificando la configuración de aplicaciones de una sola página.
- **rimraf** (^2.5.4): Eliminación recursiva de archivos multiplataforma (como rm -rf en Unix).
- **style-loader** (^0.13.1): Inyecta CSS en el DOM a través de etiquetas style para carga dinámica.
- **stylus** (^0.54.5): Preprocesador de CSS con sintaxis expresiva, compilado a CSS.
- **stylus-loader** (^2.1.1): Loader de Webpack para procesar archivos Stylus a CSS.
- **url-loader** (0.5.7): Codifica archivos pequeños (ej. imágenes) en base64 en línea o emite los más grandes; recurre a file-loader.
- **vue-hot-reload-api** (^1.2.0): Habilita el reemplazo de módulos en caliente para componentes Vue.js durante el desarrollo.
- **vue-html-loader** (^1.0.0): Loader de Webpack para analizar plantillas HTML en componentes de un solo archivo de Vue.
- **vue-loader** (8.5.3): Carga y procesa componentes de un solo archivo de Vue (.vue) en JavaScript y CSS.
- **vue-style-loader** (^1.0.0): Maneja el CSS de los componentes Vue, integrándose con style-loader.
- **webpack** (1.13.2): Empaquetador de módulos para construir y optimizar assets web como JS, CSS e imágenes.
- **webpack-dev-server** (1.14.0): Servidor de desarrollo con recarga en vivo y reemplazo de módulos en caliente.

### Dependencies
Estos son paquetes de runtime incluidos en la build final de la aplicación.

- **debug** (^2.2.0): Utilidad de depuración con registro de logs con espacios de nombres y salida condicional (solo se habilita mediante la variable de entorno DEBUG).
- **es6-promise** (^3.0.2): Polyfill para la API Promise de ES6 en navegadores/entornos antiguos.
- **font-awesome** (^4.6.3): Librería de iconos popular que proporciona iconos vectoriales escalables a través de clases CSS.
- **github-markdown-css** (^4.6.3): CSS para estilizar Markdown al estilo de GitHub.
- **highlight.js** (^9.6.0): Resaltador de sintaxis para bloques de código en múltiples lenguajes.
- **hls.js** (^0.7.6): Librería JavaScript para reproducir vídeos HTTP Live Streaming (HLS) con video HTML5.
- **inherit** (^2.2.6): Utilidad para herencia clásica y prototípica en objetos JavaScript.
- **jquery** (^3.1.0): Librería JavaScript rápida y rica en funciones para manipulación del DOM, AJAX y eventos.
- **json-loader** (^0.5.4): Carga archivos JSON como módulos JavaScript.
- **leancloud-realtime** (^3.2.3): SDK para el servicio de mensajería en tiempo real y sincronización de datos de LeanCloud.
- **marked** (^0.3.6): Analizador de Markdown que convierte Markdown a HTML.
- **moment** (^2.14.1): Librería de manipulación de fecha/hora para analizar, validar y formatear fechas.
- **moment-timezone** (^0.5.7): Extensión para Moment.js para manejar zonas horarias y horario de verano.
- **qiniu-js-sdk** (0.0.2): SDK de JavaScript para interactuar con el almacenamiento en la nube de Qiniu (subir/descargar archivos).
- **raw-loader** (^0.5.1): Loader de Webpack que carga archivos como cadenas de texto crudas (ej. plantillas de texto).
- **rupture** (^0.6.1): Extensión de media queries para Stylus, proporcionando breakpoints para diseño responsivo.
- **sprintf-js** (^1.0.3): Implementación de sprintf en JavaScript para formateo de cadenas con marcadores de posición.
- **vue** (^1.0.26): Framework MVVM progresivo para construir interfaces de usuario (v1.x, que es más antigua).
- **vue-resource** (^0.6.1): Cliente HTTP para Vue.js para simplificar peticiones AJAX/API.
- **vue-router** (^0.7.13): Router oficial para Vue.js, que permite la navegación en aplicaciones de una sola página.
- **vue-spinner** (^1.0.2): Librería de componentes spinner/loading para Vue.js.
- **vue-weui** (^0.3.2): Wrappers de Vue.js para componentes WeUI (librería de UI para interfaces al estilo WeChat).
- **weixin-js-sdk** (^1.2.0): SDK de JavaScript de WeChat para integrar funciones web de WeChat (ej. compartir, escanear).
- **weui** (^0.4.3): Framework CSS WeUI para construir interfaces móviles inspiradas en el diseño de WeChat.
- **word-color** (^1.2.0): Librería para colorear palabras basándose en factores como hash o idioma, probablemente para efectos tipo mapa de calor.