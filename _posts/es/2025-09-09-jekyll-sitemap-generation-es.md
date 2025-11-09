---
audio: false
date: 2025-09-09
generated: true
image: false
lang: es
layout: post
model: openai/gpt-5
title: Generación de Archivos de Mapa del Sitio para Jekyll
translated: true
type: note
---

Un **sitemap.xml** es un archivo XML que informa a los motores de búsqueda como Google y Bing sobre las páginas de tu sitio web. Ayuda a los rastreadores a descubrir e indexar la estructura de tu sitio de manera más eficiente. Para un blog de Jekyll, esto significa que los motores de búsqueda pueden encontrar todas tus publicaciones, páginas y traducciones (como tu `index-zh.html`, `index-fr.html`, etc.) incluso si no están enlazadas en todas partes.

### Qué hace un Sitemap

* Enumera todas las URL importantes de tu sitio.
* Proporciona metadatos como la fecha de última modificación (`<lastmod>`), la frecuencia de cambio (`<changefreq>`) y la prioridad (`<priority>`).
* Mejora el SEO al garantizar que los rastreadores no pasen por alto páginas.

### Cómo generarlo para Jekyll

Tienes un par de enfoques:

#### 1. Usa el plugin `jekyll-sitemap` (recomendado)

1. En el `Gemfile` de tu proyecto de Jekyll, añade:

   ```ruby
   gem 'jekyll-sitemap'
   ```
2. En tu `_config.yml`, añade:

   ```yaml
   plugins:
     - jekyll-sitemap
   ```

   (Si estás en GitHub Pages, `jekyll-sitemap` ya está en la lista blanca, por lo que funciona directamente).
3. Cuando construyas (`jekyll build` o mediante `make` si lo tienes configurado), Jekyll generará automáticamente un `sitemap.xml` en tu carpeta `_site/`.

#### 2. Crear manualmente una plantilla de sitemap

Si prefieres tener más control:

1. Crea un archivo en la raíz del proyecto: `/sitemap.xml`.
2. Añade esta plantilla de Liquid:

   ```xml
   ---
   layout: nil
   ---
   <?xml version="1.0" encoding="UTF-8"?>
   <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
     {% for page in site.pages %}
       {% if page.sitemap != false %}
         <url>
           <loc>{{ site.url }}{{ page.url | replace:'index.html','' }}</loc>
           <lastmod>{{ page.date | date_to_xmlschema }}</lastmod>
         </url>
       {% endif %}
     {% endfor %}
     {% for post in site.posts %}
       <url>
         <loc>{{ site.url }}{{ post.url }}</loc>
         <lastmod>{{ post.date | date_to_xmlschema }}</lastmod>
       </url>
     {% endfor %}
   </urlset>
   ```
3. Asegúrate de que tu `_config.yml` tenga `url: "https://tudominio.com"` para que los enlaces se generen correctamente.

#### 3. Verificar

* Después de construir, revisa `_site/sitemap.xml`.
* Envíalo a Google Search Console para una mejor indexación.

---

👉 Dado que ya tienes `_config.yml` y `_plugins/`, lo más fácil es simplemente habilitar `jekyll-sitemap`. De esa manera, no tendrás que mantener el XML manualmente.

¿Quieres que redacte la adición exacta para tu `_config.yml` (basándome en tus archivos actuales), para que puedas pegarla directamente?