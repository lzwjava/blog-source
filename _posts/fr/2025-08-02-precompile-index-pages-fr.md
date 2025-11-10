---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Précompilation des Pages d'Index par Langue
translated: true
type: note
---

Oui, vous pouvez précompiler des pages d'index séparées pour différentes langues (par exemple, `index-zh.html`, `index-en.html`) pour améliorer les performances et l'expérience utilisateur, surtout si votre site comporte un grand nombre d'articles ou si vous souhaitez réduire le traitement JavaScript côté client. Cette approche consiste à générer des fichiers HTML statiques pour chaque langue pendant le processus de build, plutôt que de compter sur JavaScript pour filtrer et trier les articles dynamiquement côté client.

Ci-dessous, je vais décrire comment y parvenir avec Jekyll, en me concentrant sur la création de pages d'index séparées pour chaque langue (`index-zh.html`, `index-en.html`, etc.) tout en conservant la fonctionnalité de votre configuration actuelle. Cela utilisera le système de build de Jekyll pour précalculer les listes d'articles filtrées pour chaque langue, réduisant ainsi le besoin d'un JavaScript côté client complexe.

---

### Approche pour précompiler `index-zh.html`, `index-en.html`, etc.

Pour précompiler des pages d'index spécifiques à une langue, vous pouvez créer des modèles de page Jekyll séparés pour chaque langue et utiliser Liquid pour filtrer les articles par langue pendant le processus de build. Ainsi, chaque page (`index-en.html`, `index-zh.html`, etc.) ne contiendra que les articles pertinents, et la logique de tri/filtrage sera gérée au moment du build plutôt que dans le navigateur.

Voici comment procéder :

---

#### 1. Créer des modèles de page spécifiques à la langue

Créez des fichiers de page séparés dans le répertoire racine de votre projet Jekyll pour chaque langue, tels que :

- `index-en.html`
- `index-zh.html`
- `index-ja.html`
- ... et ainsi de suite pour les autres langues (`es`, `hi`, `fr`, `de`, `ar`, `hant`, etc.).

Chaque fichier utilisera une structure similaire à votre code fourni mais filtrera les articles pour une langue spécifique en utilisant Liquid. Voici un exemple pour `index-en.html` :

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

Pour `index-zh.html`, vous remplaceriez le filtre `lang` et `where` :

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
  <!-- Même sort-select que ci-dessus -->
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

<!-- Même footer que ci-dessus -->
```

Répétez ceci pour chaque langue (`ja`, `es`, `hi`, `fr`, `de`, `ar`, `hant`, etc.), en ajustant le front matter `lang` et le filtre `where` en conséquence.

---

#### 2. Mettre à jour le Front Matter des articles

Assurez-vous que chaque article dans votre répertoire `_posts` a une variable front matter `lang` qui correspond à sa langue (par exemple, `en`, `zh`, `ja`, etc.). Par exemple :

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

Cela permet au filtre `where` d'identifier correctement les articles par langue.

Si vos articles sont organisés dans des sous-répertoires comme `_posts/en/`, `_posts/zh/`, etc., vous pouvez déduire la langue du chemin au lieu d'utiliser une variable `lang`. Par exemple, dans `index-en.html` :

```liquid
{% assign en_posts = site.posts | where_exp: "post", "post.path contains '_posts/en/'" %}
```

---

#### 3. Simplifier le JavaScript

Étant donné que le filtrage par langue est maintenant géré au moment du build, vous pouvez simplifier le JavaScript pour ne gérer que le tri (par exemple, par date ou par sélections de l'auteur) et la navigation entre les pages de langue. Voici une version mise à jour du JavaScript :

```javascript
window.addEventListener('load', function () {
  const sortSelect = document.getElementById('sort-select');
  const postNumber = document.getElementById('post-number');
  const postList = document.querySelector('.post-list');

  function updatePosts() {
    const selectedValue = sortSelect.value;
    const [sortOption, langFilter] = selectedValue.split('|');

    // Si la langue sélectionnée ne correspond pas à la page actuelle, rediriger
    const currentLang = '{{ page.lang }}';
    if (langFilter !== currentLang && langFilter !== 'all' && langFilter !== 'original' && sortOption !== 'author-picks') {
      window.location.href = `/${langFilter}/?sort=${selectedValue}`;
      return;
    }

    // Récupérer tous les articles
    const posts = document.querySelectorAll('.post-list li.post-item');
    let processedPosts = [];

    if (sortOption === 'author-picks') {
      // Filtrer les articles avec 'data-top' > 0
      processedPosts = Array.from(posts)
        .filter(post => parseInt(post.dataset.top || 0, 10) > 0)
        .map(post => ({ element: post }));
    } else if (sortOption === 'date-desc' && langFilter === 'original') {
      // Filtrer les articles originaux (non traduits, non générés)
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
      // Trier par date décroissante
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

    // Effacer la liste existante
    postList.innerHTML = '';

    // Ajouter les articles traités ou afficher un message
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

    // Mettre à jour le compteur d'articles
    const translatedCount = processedPosts.filter(item => item.element && item.element.dataset.translated === 'true').length;
    postNumber.innerHTML = `${processedPosts.length} posts (${translatedCount} by <a href="https://mistral.ai">AI</a>)`;

    // Afficher la liste
    postList.style.display = 'block';
  }

  // Restaurer depuis localStorage ou définir la valeur par défaut
  const savedSort = localStorage.getItem('sortOption');
  if (savedSort) {
    sortSelect.value = savedSort;
  } else {
    sortSelect.value = 'date-desc|{{ page.lang }}';
  }

  updatePosts();

  // Écouteur d'événement pour les changements du menu déroulant
  sortSelect.addEventListener('change', function () {
    localStorage.setItem('sortOption', sortSelect.value);
    updatePosts();
  });
});
```

Changements clés :
- Le script vérifie si la langue sélectionnée correspond à la langue de la page actuelle (`{{ page.lang }}`). Si ce n'est pas le cas, il redirige vers la page de langue appropriée (par exemple, `/zh/` pour le chinois).
- Le filtrage par langue n'est plus nécessaire car les articles sont pré-filtrés par le modèle Liquid.

---

#### 4. Configurer les Permaliens et la Navigation

Assurez-vous que chaque page spécifique à une langue a un permalien unique dans son front matter (par exemple, `permalink: /en/` pour `index-en.html`). Cela permet aux utilisateurs de naviguer directement vers `/en/`, `/zh/`, etc.

Vous pouvez également mettre à jour la navigation de votre site pour inclure des liens vers ces pages spécifiques à la langue. Par exemple, dans votre mise en page ou en-tête :

```html
<nav>
  <a href="/en/">English</a>
  <a href="/zh/">中文</a>
  <a href="/ja/">日本語</a>
  <!-- Ajouter d'autres langues -->
</nav>
```

---

#### 5. Gérer les Filtres "All" et "Original"

Pour les options "All" et "Original" dans le menu déroulant :
- **All** : Vous pouvez créer un `index.html` qui inclut tous les articles (similaire à votre configuration d'origine) ou rediriger vers l'une des pages spécifiques à la langue.
- **Original** : Vous pouvez créer un `index-original.html` qui filtre les articles avec `translated: false` et `generated: false` :

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
  <!-- Même sort-select -->
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

<!-- Même footer -->
```

---

#### 6. Avantages de la Précompilation

- **Performance** : Le filtrage des articles au moment du build réduit le traitement JavaScript côté client, rendant le site plus rapide, surtout pour les utilisateurs avec des appareils ou des connexions lents.
- **SEO** : Les moteurs de recherche peuvent mieux indexer les pages spécifiques à la langue (`/en/`, `/zh/`, etc.), améliorant la découvrabilité.
- **JavaScript plus simple** : Le JavaScript ne doit gérer que le tri et la navigation, pas le filtrage par langue.
- **Fiabilité** : Les pages précompilées évitent les bugs côté client (par exemple, le message "Known bug pending fix" dans votre code d'origine).

---

#### 7. Considérations

- **Temps de Build** : La précompilation de plusieurs pages d'index augmente le temps de build, surtout si vous avez beaucoup d'articles ou de langues. Cependant, cela est généralement négligeable sauf si vous avez des milliers d'articles.
- **Maintenance** : Vous devrez maintenir plusieurs fichiers d'index (`index-en.html`, `index-zh.html`, etc.). Pour réduire la duplication, vous pouvez utiliser des includes ou des layouts Jekyll pour partager le code commun.
- **Tri Dynamique** : Le JavaScript gère toujours le tri (par exemple, les sélections de l'auteur, date-desc), mais vous pourriez précalculer des versions triées de chaque page si vous voulez une sortie entièrement statique (bien que cela créerait plus de fichiers, par exemple, `index-en-picks.html`).

---

#### 8. Exemple de Structure de Répertoire

Votre projet Jekyll pourrait ressembler à ceci :

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

#### 9. Tests et Déploiement

- Testez localement avec `jekyll serve` pour vous assurer que chaque page de langue (`/en/`, `/zh/`, etc.) affiche les articles corrects.
- Vérifiez que la navigation par menu déroulant redirige correctement entre les pages de langue.
- Déployez sur votre plateforme d'hébergement (par exemple, GitHub Pages) et vérifiez que les permaliens fonctionnent comme prévu.

---

### Références
- [Documentation Jekyll](https://jekyllrb.com/docs/)
- [Mistral AI](https://mistral.ai)

Si vous avez d'autres questions ou besoin d'aide pour des parties spécifiques de la mise en œuvre, faites-le moi savoir !