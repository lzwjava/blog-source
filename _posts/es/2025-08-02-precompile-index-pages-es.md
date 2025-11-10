---
audio: false
generated: true
image: false
lang: es
layout: post
title: Precompilar Páginas de Índice Específicas del Idioma
translated: true
type: note
---

Sí, puedes precompilar páginas de índice separadas para diferentes idiomas (por ejemplo, `index-zh.html`, `index-en.html`) para mejorar el rendimiento y la experiencia del usuario, especialmente si tu sitio tiene una gran cantidad de publicaciones o si deseas reducir el procesamiento de JavaScript del lado del cliente. Este enfoque implicaría generar archivos HTML estáticos para cada idioma durante el proceso de compilación, en lugar de depender de JavaScript para filtrar y ordenar las publicaciones dinámicamente en el lado del cliente.

A continuación, describiré cómo puedes lograr esto con Jekyll, centrándote en crear páginas de índice separadas para cada idioma (`index-zh.html`, `index-en.html`, etc.) manteniendo la funcionalidad de tu configuración actual. Esto aprovechará el sistema de compilación de Jekyll para precalcular las listas de publicaciones filtradas para cada idioma, reduciendo la necesidad de un JavaScript complejo en el lado del cliente.

---

### Enfoque para precompilar `index-zh.html`, `index-en.html`, etc.

Para precompilar páginas de índice específicas por idioma, puedes crear plantillas de página de Jekyll separadas para cada idioma y usar Liquid para filtrar las publicaciones por idioma durante el proceso de compilación. De esta manera, cada página (`index-en.html`, `index-zh.html`, etc.) contendrá solo las publicaciones relevantes, y la lógica de ordenación/filtrado se manejará en el momento de la compilación en lugar de en el navegador.

Así es como puedes hacerlo:

---

#### 1. Crear Plantillas de Página Específicas por Idioma

Crea archivos de página separados en el directorio raíz de tu proyecto de Jekyll para cada idioma, tales como:

- `index-en.html`
- `index-zh.html`
- `index-ja.html`
- ...y así sucesivamente para otros idiomas (`es`, `hi`, `fr`, `de`, `ar`, `hant`, etc.).

Cada archivo utilizará una estructura similar a tu código proporcionado, pero filtrará las publicaciones para un idioma específico usando Liquid. Aquí hay un ejemplo para `index-en.html`:

```html
---
layout: page
lang: en
permalink: /en/
---

<div class="sort-container">
  <span id="post-number" class="post-number">
    {% assign en_posts = site.posts | where: "lang", "en" %}
    {{ en_posts.size }} posts
    ({{ en_posts | where: "translated", true | size }} by <a href="https://mistral.ai">AI</a>)
  </span>

  <select id="sort-select">
    <option value="author-picks|en">Picks</option>
    <option value="date-desc|all">All</option>
    <option value="date-desc|original">Original</option>
    <option value="date-desc|en" selected>English</option>
    <option value="date-desc|zh">中文</option>
    <option value="date-desc|ja">日本語</option>
    <option value="date-desc|es">Español</option>
    <option value="date-desc|hi">हिंदी</option>
    <option value="date-desc|fr">Français</option>
    <option value="date-desc|de">Deutsch</option>
    <option value="date-desc|ar">العربية</option>
    <option value="date-desc|hant">繁體中文</option>
  </select>
</div>

<ul class="post-list">
  {% if en_posts.size > 0 %}
    {% for post in en_posts %}
      <li class="list-group-item post-item lang-en" data-top="{{ post.top | default: 0 }}" data-translated="{{ post.translated | default: false }}" data-generated="{{ post.generated | default: false }}">
        <a href="{{ post.url }}">
          <span class="date">{{ post.date | date: "%Y.%m.%d" }}</span>
          <span class="type">{% if post.image %}image{% else %}text{% endif %}</span>
          <span class="title">{{ post.title }}</span>
        </a>
      </li>
    {% endfor %}
  {% else %}
    <li class="list-group-item post-item">No posts available.</li>
  {% endif %}
</ul>

<footer class="site-footer">
  <span class="site-footer-credits">
    Powered by <a href="https://jekyllrb.com/">Jekyll</a><br>
    Ignited by <a href="https://mistral.ai">Mistral</a><br>
    Updated at <a href="https://github.com/lzwjava/lzwjava.github.io/commit/{{ site.release }}">{{ site.release | slice: 0, 6 }}</a><br>
    Copyright©{{ site.starting_year }}–{{ site.time | date: "%Y" }}
  </span>
</footer>
```

Para `index-zh.html`, reemplazarías el `lang` y el filtro `where`:

```html
---
layout: page
lang: zh
permalink: /zh/
---
<div class="sort-container">
  <span id="post-number" class="post-number">
    {% assign zh_posts = site.posts | where: "lang", "zh" %}
    {{ zh_posts.size }} posts
    ({{ zh_posts | where: "translated", true | size }} by <a href="https://mistral.ai">AI</a>)
  </span>
  <!-- Same sort-select as above -->
</div>

<ul class="post-list">
  {% if zh_posts.size > 0 %}
    {% for post in zh_posts %}
      <li class="list-group-item post-item lang-zh" data-top="{{ post.top | default: 0 }}" data-translated="{{ post.translated | default: false }}" data-generated="{{ post.generated | default: false }}">
        <a href="{{ post.url }}">
          <span class="date">{{ post.date | date: "%Y.%m.%d" }}</span>
          <span class="type">{% if post.image %}image{% else %}text{% endif %}</span>
          <span class="title">{{ post.title }}</span>
        </a>
      </li>
    {% endfor %}
  {% else %}
    <li class="list-group-item post-item">No posts available.</li>
  {% endif %}
</ul>

<!-- Same footer as above -->
```

Repite esto para cada idioma (`ja`, `es`, `hi`, `fr`, `de`, `ar`, `hant`, etc.), ajustando el front matter `lang` y el filtro `where` en consecuencia.

---

#### 2. Actualizar el Front Matter de las Publicaciones

Asegúrate de que cada publicación en tu directorio `_posts` tenga una variable de front matter `lang` que corresponda a su idioma (por ejemplo, `en`, `zh`, `ja`, etc.). Por ejemplo:

```yaml
---
title: My English Post
lang: en
date: 2025-08-01
translated: true
generated: false
top: 1
---
```

Esto permite que el filtro `where` identifique correctamente las publicaciones por idioma.

Si tus publicaciones están organizadas en subdirectorios como `_posts/en/`, `_posts/zh/`, etc., puedes inferir el idioma desde la ruta en lugar de usar una variable `lang`. Por ejemplo, en `index-en.html`:

```liquid
{% assign en_posts = site.posts | where_exp: "post", "post.path contains '_posts/en/'" %}
```

---

#### 3. Simplificar el JavaScript

Dado que el filtrado por idioma ahora se maneja en el momento de la compilación, puedes simplificar el JavaScript para que solo maneje la ordenación (por ejemplo, por fecha o por selecciones del autor) y la navegación entre las páginas de idiomas. Aquí hay una versión actualizada del JavaScript:

```javascript
window.addEventListener('load', function () {
  const sortSelect = document.getElementById('sort-select');
  const postNumber = document.getElementById('post-number');
  const postList = document.querySelector('.post-list');

  function updatePosts() {
    const selectedValue = sortSelect.value;
    const [sortOption, langFilter] = selectedValue.split('|');

    // Si el idioma seleccionado no coincide con la página actual, redirigir
    const currentLang = '{{ page.lang }}';
    if (langFilter !== currentLang && langFilter !== 'all' && langFilter !== 'original' && sortOption !== 'author-picks') {
      window.location.href = `/${langFilter}/?sort=${selectedValue}`;
      return;
    }

    // Tomar todas las publicaciones
    const posts = document.querySelectorAll('.post-list li.post-item');
    let processedPosts = [];

    if (sortOption === 'author-picks') {
      // Filtrar publicaciones con 'data-top' > 0
      processedPosts = Array.from(posts)
        .filter(post => parseInt(post.dataset.top || 0, 10) > 0)
        .map(post => ({ element: post }));
    } else if (sortOption === 'date-desc' && langFilter === 'original') {
      // Filtrar publicaciones originales (no traducidas, no generadas)
      processedPosts = Array.from(posts)
        .filter(post => post.dataset.translated === 'false' && post.dataset.generated === 'false')
        .map(post => {
          const dateElement = post.querySelector('.date');
          const dateStr = dateElement ? dateElement.textContent.trim().replace(/\./g, '-') : null;
          return { element: post, date: dateStr ? new Date(dateStr) : null };
        })
        .filter(item => item.date)
        .sort((a, b) => b.date - a.date);
    } else {
      // Ordenar por fecha descendente
      processedPosts = Array.from(posts)
        .map(post => {
          const dateElement = post.querySelector('.date');
          const dateStr = dateElement ? dateElement.textContent.trim().replace(/\./g, '-') : null;
          const aElement = post.querySelector('a');
          const href = aElement ? aElement.getAttribute('href') : '';
          const fileName = href ? href.split('/').pop() : '';
          return { element: post, date: dateStr ? new Date(dateStr) : null, fileName };
        })
        .filter(item => item.date)
        .sort((a, b) => {
          const dateComparison = b.date - a.date;
          return dateComparison !== 0 ? dateComparison : a.fileName.localeCompare(b.fileName);
        });
    }

    // Limpiar la lista existente
    postList.innerHTML = '';

    // Añadir las publicaciones procesadas o mostrar un mensaje
    if (processedPosts.length > 0) {
      processedPosts.forEach(item => {
        if (item.element) {
          postList.appendChild(item.element);
        }
      });
    } else {
      const noPostsMessage = document.createElement('li');
      noPostsMessage.className = 'list-group-item post-item';
      noPostsMessage.textContent = 'No posts available. Please refresh the page.';
      postList.appendChild(noPostsMessage);
    }

    // Actualizar el recuento de publicaciones
    const translatedCount = processedPosts.filter(item => item.element && item.element.dataset.translated === 'true').length;
    postNumber.innerHTML = `${processedPosts.length} posts (${translatedCount} by <a href="https://mistral.ai">AI</a>)`;

    // Mostrar la lista
    postList.style.display = 'block';
  }

  // Restaurar desde localStorage o establecer el valor por defecto
  const savedSort = localStorage.getItem('sortOption');
  if (savedSort) {
    sortSelect.value = savedSort;
  } else {
    sortSelect.value = 'date-desc|{{ page.lang }}';
  }

  updatePosts();

  // Event listener para cambios en el menú desplegable
  sortSelect.addEventListener('change', function () {
    localStorage.setItem('sortOption', sortSelect.value);
    updatePosts();
  });
});
```

Cambios clave:
- El script verifica si el idioma seleccionado coincide con el idioma de la página actual (`{{ page.lang }}`). Si no es así, redirige a la página de idioma apropiada (por ejemplo, `/zh/` para chino).
- Ya no se necesita el filtrado por idioma ya que las publicaciones están pre-filtradas por la plantilla de Liquid.

---

#### 4. Configurar Permalinks y Navegación

Asegúrate de que cada página específica por idioma tenga un permalink único en su front matter (por ejemplo, `permalink: /en/` para `index-en.html`). Esto permite a los usuarios navegar directamente a `/en/`, `/zh/`, etc.

También es posible que desees actualizar la navegación de tu sitio para incluir enlaces a estas páginas específicas por idioma. Por ejemplo, en tu diseño o encabezado:

```html
<nav>
  <a href="/en/">English</a>
  <a href="/zh/">中文</a>
  <a href="/ja/">日本語</a>
  <!-- Añadir otros idiomas -->
</nav>
```

---

#### 5. Manejar los Filtros "All" y "Original"

Para las opciones "All" y "Original" en el menú desplegable:
- **All**: Puedes crear un `index.html` que incluya todas las publicaciones (similar a tu configuración original) o redirigir a una de las páginas específicas por idioma.
- **Original**: Puedes crear un `index-original.html` que filtre las publicaciones con `translated: false` y `generated: false`:

```html
---
layout: page
lang: original
permalink: /original/
---
<div class="sort-container">
  <span id="post-number" class="post-number">
    {% assign original_posts = site.posts | where: "translated", false | where: "generated", false %}
    {{ original_posts.size }} posts
    (0 by <a href="https://mistral.ai">AI</a>)
  </span>
  <!-- Same sort-select -->
</div>

<ul class="post-list">
  {% if original_posts.size > 0 %}
    {% for post in original_posts %}
      <li class="list-group-item post-item lang-{{ post.lang }}" data-top="{{ post.top | default: 0 }}" data-translated="false" data-generated="false">
        <a href="{{ post.url }}">
          <span class="date">{{ post.date | date: "%Y.%m.%d" }}</span>
          <span class="type">{% if post.image %}image{% else %}text{% endif %}</span>
          <span class="title">{{ post.title }}</span>
        </a>
      </li>
    {% endfor %}
  {% else %}
    <li class="list-group-item post-item">No posts available.</li>
  {% endif %}
</ul>

<!-- Same footer -->
```

---

#### 6. Beneficios de la Precompilación

- **Rendimiento**: Filtrar las publicaciones en el momento de la compilación reduce el procesamiento de JavaScript en el lado del cliente, haciendo que el sitio sea más rápido, especialmente para usuarios con dispositivos o conexiones más lentas.
- **SEO**: Los motores de búsqueda pueden indexar mejor las páginas específicas por idioma (`/en/`, `/zh/`, etc.), mejorando la descubribilidad.
- **JavaScript más simple**: El JavaScript solo necesita manejar la ordenación y la navegación, no el filtrado por idioma.
- **Fiabilidad**: Las páginas precompiladas evitan errores del lado del cliente (por ejemplo, el mensaje "Known bug pending fix" en tu código original).

---

#### 7. Consideraciones

- **Tiempo de Compilación**: Precompilar múltiples páginas de índice aumenta el tiempo de compilación, especialmente si tienes muchas publicaciones o idiomas. Sin embargo, esto suele ser insignificante a menos que tengas miles de publicaciones.
- **Mantenimiento**: Necesitarás mantener múltiples archivos de índice (`index-en.html`, `index-zh.html`, etc.). Para reducir la duplicación, puedes usar includes o layouts de Jekyll para compartir código común.
- **Ordenación Dinámica**: El JavaScript aún maneja la ordenación (por ejemplo, selecciones del autor, fecha-desc), pero podrías precalcular versiones ordenadas de cada página si deseas una salida completamente estática (aunque esto crearía más archivos, por ejemplo, `index-en-picks.html`).

---

#### 8. Ejemplo de Estructura de Directorios

Tu proyecto de Jekyll podría verse así:

```
├── _posts/
│   ├── en/
│   │   ├── 2025-08-01-post1.md
│   │   ├── 2025-08-02-post2.md
│   ├── zh/
│   │   ├── 2025-08-01-post1-zh.md
│   ├── ja/
│   └── ...
├── _layouts/
│   ├── page.html
├── index-en.html
├── index-zh.html
├── index-ja.html
├── index-original.html
├── _includes/
│   ├── header.html
│   ├── footer.html
├── assets/
│   ├── js/
│   │   ├── sort.js
```

---

#### 9. Pruebas y Despliegue

- Prueba localmente con `jekyll serve` para asegurarte de que cada página de idioma (`/en/`, `/zh/`, etc.) muestre las publicaciones correctas.
- Verifica que la navegación del menú desplegable redirija correctamente entre las páginas de idiomas.
- Despliega en tu plataforma de hosting (por ejemplo, GitHub Pages) y comprueba que los permalinks funcionen como se espera.

---

### Referencias
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Mistral AI](https://mistral.ai)

Si tienes más preguntas o necesitas ayuda con partes específicas de la implementación, ¡avísame!