---
audio: false
generated: true
image: false
lang: es
layout: post
title: 'Jekyll i18n: Complemento Políglota y Método de Carpetas'
translated: true
type: note
---

Tienes tres buenas opciones para i18n en un blog de Jekyll, desde "baterías incluidas" hasta "mínima configuración". Así es como funciona cada una y cómo configurarlas.

# 1) La más fácil: usar un plugin (jekyll-polyglot)

**Mejor opción si puedes construir localmente o con CI.** El constructor integrado de GitHub Pages no permite la mayoría de los plugins de terceros, así que o construyes localmente (`jekyll build`) y subes la carpeta `_site/` generada, o usas GitHub Actions para construir y publicar.

**Instalación**

```bash
gem install jekyll-polyglot
# o añade al Gemfile:
# gem 'jekyll-polyglot'
```

**\_config.yml**

```yml
plugins:
  - jekyll-polyglot

languages: ["en", "zh", "ja"]   # tus idiomas
default_lang: "en"
exclude_from_localization: ["assets", "images", "CNAME"]  # mantén las rutas estáticas compartidas
parallel_localization: true
```

**Estructura del contenido**

```
_index.md               # página de inicio opcional
_posts/
  2024-05-01-hello.en.md
  2024-05-01-hello.zh.md
pages/
  about.en.md
  about.zh.md
```

Polyglot construye URLs con ámbito de idioma como `/en/about/` y `/zh/about/`. También expone `site.active_lang`.

**Selector de idioma (en tu layout)**

```liquid
<nav class="lang-switch">
  {% for lang in site.languages %}
    {% if lang == site.active_lang %}
      <span>{{ lang }}</span>
    {% else %}
      <a href="{{ page.url | prepend:'/' | replace_first:'/' | prepend:'/' | absolute_url | replace: '/' | relative_url | prepend:'/' }}">
        {%- comment -%}
        Reconstruiremos la URL actual para cada idioma:
        {%- endcomment -%}
      </a>
    {% endif %}
  {% endfor %}
</nav>
```

Un enfoque más simple con Polyglot es:

```liquid
<nav>
  {% for lang in site.languages %}
    <a href="{{ site.baseurl_root }}/{{ lang }}{{ page.permalink | default: page.url }}">{{ lang }}</a>
  {% endfor %}
</nav>
```

**Cadenas de UI mediante archivos de datos**
Crea `_data/i18n.yml`:

```yml
en:
  nav:
    home: "Home"
    posts: "Posts"
zh:
  nav:
    home: "主页"
    posts: "文章"
```

Uso en las plantillas:

```liquid
{{ site.data.i18n[site.active_lang].nav.home }}
```

**SEO (hreflang)**
En el `<head>` de tu layout:

```liquid
{% assign langs = site.languages %}
{% for l in langs %}
  <link rel="alternate" hreflang="{{ l }}" href="{{ site.url }}/{{ l }}{{ page.url }}" />
{% endfor %}
<link rel="alternate" hreflang="x-default" href="{{ site.url }}/{{ site.default_lang }}{{ page.url }}" />
```

# 2) Sin plugin: carpetas por idioma + Liquid

**Mejor opción si debes usar el constructor integrado de GitHub Pages.**

**Estructura**

```
_en/
  index.md
  about.md
_zh/
  index.md
  about.md
_posts/
  en/
    2024-05-01-hello.md
  zh/
    2024-05-01-hello.md
```

**\_config.yml**

```yml
defaults:
  - scope: { path: "_posts/en" }
    values: { lang: "en", permalink: "/en/:categories/:year/:month/:day/:title/" }
  - scope: { path: "_posts/zh" }
    values: { lang: "zh", permalink: "/zh/:categories/:year/:month/:day/:title/" }
  - scope: { path: "_en" }
    values: { lang: "en", permalink: "/en/:path/" }
  - scope: { path: "_zh" }
    values: { lang: "zh", permalink: "/zh/:path/" }
```

**Establecer un idioma actual**
Añade en el front matter de cada página:

```yml
---
layout: default
lang: en
---
```

o infiérelo desde la ruta:

```liquid
{% assign current_lang = page.lang | default: page.path | split:'/' | first | remove:'_' %}
```

**Enlaces cruzados entre traducciones**
Usa un identificador compartido en el front matter:

```yml
---
layout: post
lang: en
ref: hello-post
---
```

En la versión en chino:

```yml
---
layout: post
lang: zh
ref: hello-post
---
```

Luego, en el layout, encuentra las versiones hermanas:

```liquid
{% assign siblings = site.pages | concat: site.posts | where:"ref", page.ref %}
{% for s in siblings %}
  {% unless s.url == page.url %}
    <a href="{{ s.url }}">{{ s.lang }}</a>
  {% endunless %}
{% endfor %}
```

**Cadenas de UI sin plugins**
Usa `_data/i18n.yml` como se mostró anteriormente, y elige el idioma mediante `current_lang`.

**Redirección de idioma por defecto (opcional)**
Crea `index.html` en la raíz:

```html
<!doctype html>
<meta charset="utf-8">
<script>
  const lang = (navigator.language || '').toLowerCase().startsWith('zh') ? 'zh' : 'en';
  location.replace('/' + lang + '/');
</script>
<noscript><a href="/en/">English</a> · <a href="/zh/">中文</a></noscript>
```

# 3) Híbrido: un conjunto de posts, traducir solo la UI

**Mejor opción si no traduces los artículos, solo la interfaz (navegación, pie de página).**
Mantén un único conjunto de `/posts/`, añade `_data/i18n.yml`, y renderiza las etiquetas por idioma. Proporciona páginas de índice por idioma que listen los mismos posts, pero con fechas y UI localizadas.

**Fechas localizadas**

```liquid
{% assign locale = page.lang | default: site.default_lang %}
{{ page.date | date: "%B %-d, %Y" }}  {# o usa filtros/plugins si los tienes #}
```

(El `date` integrado de Jekyll no es completamente consciente de la configuración regional; para un formateo verdadero de locale necesitarás un plugin o cadenas preformateadas en los datos.)

---

## Consejos prácticos

* **Slugs:** Mantén el mismo `ref` para las contrapartes traducidas; deja que los títulos varíen por idioma.
* **Imágenes:** Coloca las imágenes compartidas en `/assets/` y exclúyelas de la localización para que las URLs permanezcan estables.
* **Sitemaps & SEO:** Genera sitemaps por idioma o asegúrate de que tu sitemap liste todas las URLs de idiomas; añade etiquetas canónicas dentro de cada versión de idioma.
* **Feeds:** Crea feeds por idioma delimitando las colecciones: filtra los posts por `lang` en tu plantilla de feed.

---

## Ejemplo mínimo funcional (sin plugin)

1. `_data/i18n.yml` con las cadenas.
2. `_en/index.md` y `_zh/index.md` con `lang` en el front matter.
3. Posts bajo `_posts/en/` y `_posts/zh/` con `lang` y un `ref` compartido.
4. El layout usa `site.data.i18n[current_lang]` y el fragmento de código de búsqueda de versiones hermanas mostrado arriba.

Si me indicas la estructura actual de tu repositorio (y si estás construyendo directamente en GitHub Pages o mediante Actions), puedo adaptar una configuración lista para usar y un par de layouts de inicio.