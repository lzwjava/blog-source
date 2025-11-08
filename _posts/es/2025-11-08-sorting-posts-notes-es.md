---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4-fast
title: Clasificación de Publicaciones y Notas
translated: true
type: note
---

### `_includes/sort.html` modificado

Tu `sort.html` existente ya tiene el selector de idioma con 9 opciones, lo cual es perfecto. No se necesitan cambios importantes aquí, pero he añadido una pequeña nota en el `<span id="post-number">` para hacerlo más genérico (por ejemplo, "entradas" en lugar de "posts") ya que ahora incluimos notas. Esto puede ser actualizado dinámicamente por tu JS si es necesario. Aquí está la versión ajustada:

```html
<div class="sort-container">
  <span id="post-number" class="post-number">
    {{ site.posts.size | plus: site.notes.size }} entradas
    ({{ site.posts.size | plus: site.notes.size | divided_by: 7 | times: 6 }} Traducido por <a href="https://openrouter.ai">AI</a>)
  </span>
  <select id="sort-select">
    <option value="en" selected>English</option>
    <option value="zh">中文</option>
    <option value="ja">日本語</option>
    <option value="es">Español</option>
    <option value="hi">हिंदी</option>
    <option value="fr">Français</option>
    <option value="de">Deutsch</option>
    <option value="ar">العربية</option>
    <option value="hant">繁體中文</option>
  </select>
</div>
```

**Cambio clave**: Actualicé el conteo para incluir `site.notes.size` (lo definiremos más abajo). La fórmula se mantiene igual pero ahora tiene en cuenta las notas. Si tu JS (`index.js`) ya actualiza este span dinámicamente basándose en los elementos visibles, manejará los conteos específicos del idioma automáticamente.

### Paso 1: Configurar Notas como una Colección de Jekyll (en `_config.yml`)

Para tratar `_notes` como `_posts` (para que Jekyll procese los archivos Markdown y los exponga via `site.notes`), añade esto a tu `_config.yml`. Esto es esencial—sin ello, las notas no tendrán `url`, `title`, `date`, etc., como lo hacen los posts.

```yaml
collections:
  notes:
    output: true
    permalink: /notes/:path/
```

- `output: true` genera páginas para las notas (opcional si solo quieres datos).
- `permalink` asegura URLs como `/notes/es/2025-11-07-tidb-vs-cockroachdb-es/` (ajusta si es necesario).
- Reinicia tu servidor de Jekyll después de añadir esto.

Ahora `site.notes` funciona igual que `site.posts`, asumiendo que tus archivos de nota (por ejemplo, `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md`) tienen un frontmatter similar: `title:`, `date:`, `image:`, `top:`, `translated:`, `generated:`.

### Paso 2: Diseño de Página Modificado (por ejemplo, `index.md` o donde sea que esté tu `<ul class="post-list">`)

Tu bucle actual solo muestra posts en inglés. Para añadir notas y soportar los 9 idiomas:

- Define una lista de idiomas una vez.
- Itera sobre **todos** los idiomas.
- Para cada idioma, añade **posts** coincidentes (de `_posts/{lang}/`) y **notas** (de `_notes/{lang}/`) como elementos `<li>`.
- Cada `<li>` obtiene `class="... lang-{lang}"` para que tu JS pueda filtrarlos (por ejemplo, ocultar/mostrar basado en el valor de `#sort-select`).
- Esto llena toda la lista de una vez (oculta por JS), luego cambia los idiomas dinámicamente.
- ¿Ordenar por fecha? Añade `| sort: 'date' | reverse` a los bucles si quieres el más nuevo primero (asumiendo que las fechas son comparables).

Aquí está el diseño completo actualizado:

```html
---
layout: page
---
{% include sort.html %}

<ul class="post-list">
  {% if site.posts.size == 0 and site.notes.size == 0 %}
    <li class="list-group-item post-item">No hay entradas disponibles.</li>
  {% else %}
    {% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}
    {% for lang in langs %}
      {% comment %} Posts para este idioma {% endcomment %}
      {% for post in site.posts | sort: 'date' | reverse %}
        {% if post.path contains "_posts/{{ lang }}/" %}
          {% assign translated = post.translated %}
          {% assign generated = post.generated %}
          {% if translated == nil %}{% assign translated = false %}{% endif %}
          {% if generated == nil %}{% assign generated = false %}{% endif %}
          <li class="list-group-item post-item lang-{{ lang }}" data-top="{{ post.top }}" data-translated="{{ translated }}" data-generated="{{ generated }}">
            <a href="{{ post.url }}">
              <span class="date">{{ post.date | date: "%Y.%m.%d" }}</span>
              <span class="type">{% if post.image %}image{% else %}text{% endif %}</span>
              <span class="title">{{ post.title }}</span>
            </a>
          </li>
        {% endif %}
      {% endfor %}

      {% comment %} Notas para este idioma (igual que los posts) {% endcomment %}
      {% for note in site.notes | sort: 'date' | reverse %}
        {% if note.path contains "_notes/{{ lang }}/" %}
          {% assign translated = note.translated %}
          {% assign generated = note.generated %}
          {% if translated == nil %}{% assign translated = false %}{% endif %}
          {% if generated == nil %}{% assign generated = false %}{% endif %}
          <li class="list-group-item post-item lang-{{ lang }}" data-top="{{ note.top }}" data-translated="{{ translated }}" data-generated="{{ generated }}">
            <a href="{{ note.url }}">
              <span class="date">{{ note.date | date: "%Y.%m.%d" }}</span>
              <span class="type">{% if note.image %}image{% else %}text{% endif %}</span>
              <span class="title">{{ note.title }}</span>
            </a>
          </li>
        {% endif %}
      {% endfor %}
    {% endfor %}
  {% endif %}
</ul>

{% include footer.html %}
<script src="/assets/js/index.js"></script>
```

**Cambios clave**:
- **Array de idiomas**: `{% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}`—coincide con las opciones de tu selector. Fácil de mantener.
- **Bucle de Posts**: Eliminó el filtro codificado `en`; ahora verifica `post.path contains "_posts/{{ lang }}/"` para cada idioma.
- **Bucle de Notas**: Añadido de forma idéntica, verificando `note.path contains "_notes/{{ lang }}/"`. Trata las notas exactamente igual que los posts (mismas clases, atributos, estructura).
- **Ordenación**: Añadido `| sort: 'date' | reverse` a ambos bucles para orden cronológico (más nuevo primero). Elimina si no es necesario.
- **Comprobación vacía**: Actualizada para incluir `site.notes.size`.
- **Rendimiento**: Esto genera todo el contenido de ~9 idiomas en tiempo de compilación. Bien para sitios pequeños; si es enorme, considera paginación o fetching por JS.

### Opcional: Añadir un Selector de Tipo (Posts/Notas/Ambos)

Mencionaste "añadir un selector/interruptor, dos opciones de selección o lo que sea". Si quieres un **segundo menú desplegable** para filtrar por tipo (por ejemplo, Solo Posts, Solo Notas, o Ambos), añade esto a `sort.html` después del selector de idioma:

```html
<select id="type-select">
  <option value="both" selected>Posts & Notes</option>
  <option value="posts">Posts Only</option>
  <option value="notes">Notes Only</option>
</select>
```

Luego, añade un atributo `data-type` a cada `<li>`:
- Para posts: `data-type="posts"`
- Para notas: `data-type="notes"`

Actualiza tu `index.js` para manejar los cambios de `#type-select` (por ejemplo, filtrar `.post-item[data-type="notes"]` para ocultar/mostrar). Esto lo mantiene simple sin cambiar Liquid.

### Próximos Pasos
- Probar: Añade una nota de ejemplo como `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md` con frontmatter (título, fecha, etc.), recompila y cambia a "Español" en el menú desplegable—debería aparecer.
- Ajustes de JS: Asegúrate de que `index.js` filtre por `.lang-{value}` y actualice `#post-number` (por ejemplo, contando los `<li>` visibles). Si aún no maneja las notas, añade `data-type` como se indicó arriba.
- Si las rutas difieren (por ejemplo, sin `/` final en los directorios), ajusta las comprobaciones `contains`.

Esto integra las notas sin problemas mientras mantiene tu configuración de 9 idiomas. ¡Avísame si necesitas fragmentos de JS o más ajustes!