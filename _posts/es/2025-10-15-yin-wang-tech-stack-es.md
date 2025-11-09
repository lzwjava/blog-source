---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Análisis de la Pila Tecnológica del Blog de Yin Wang
translated: true
type: note
---

El sitio web (https://www.yinwang.org/, titulado "当然我在扯淡") parece ser un blog personalizado. Basado en el código HTML proporcionado:

- **Framework**: Está construido principalmente con **Vue.js** (probablemente versión 3), evidente por atributos específicos de Vue como `data-v-app`, `data-v-[hash]` para CSS con alcance, y referencias a componentes (por ejemplo, `HomeView`, `PostView`, `router-link-active` para Vue Router manejando la navegación).
- **Herramienta de build**: Se utiliza **Vite** para el empaquetado y desarrollo, mostrado por el favicon (`/vite.svg`), scripts precargados como módulos con nombres de archivo con hash (por ejemplo, `/assets/index-DS_1rR7p.js`), y la estructura general de assets típica de la salida de Vite.
- **Estilos**: **Tailwind CSS** para clases de utilidad-first (por ejemplo, `bg-gray-50 dark:bg-gray-900`, `flex items-center`, prefijos responsivos como `sm:px-4`).
- **Otras notas**: No hay indicadores de renderizado del lado del servidor (por ejemplo, no hay rastros de Nuxt.js), por lo que es probablemente un sitio estático o una SPA renderizada en el cliente. El contenido (publicaciones, etiquetas, paginación) sugiere una configuración personalizada simple para un blog personal, posiblemente con Markdown para el contenido de las publicaciones.

**No está todo escrito manualmente**—el HTML se genera automáticamente durante el proceso de build a partir de componentes y plantillas de Vue. La lógica central (enrutamiento, componentes) está codificada en JS/TS, pero la salida final son archivos estáticos optimizados. No hay evidencia de un generador de sitios estáticos completo como Hugo o Jekyll; es más bien un proyecto ligero de Vue + Vite.

[当然我在扯淡](https://www.yinwang.org/)