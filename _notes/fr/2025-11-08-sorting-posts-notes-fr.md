---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Tri des publications et des notes
translated: true
---

### `_includes/sort.html` modifié

Votre `sort.html` existant a déjà le sélecteur de langue avec 9 options, ce qui est parfait. Aucun changement majeur n'est nécessaire ici, mais j'ai ajouté une petite note dans le `<span id="post-number">` pour le rendre plus générique (par exemple, "entrées" au lieu de "posts") puisque nous incluons maintenant des notes. Ceci peut être mis à jour dynamiquement par votre JS si nécessaire. Voici la version ajustée :

```html
<div class="sort-container">
  <span id="post-number" class="post-number">
    {{ site.posts.size | plus: site.notes.size }} entrées
    ({{ site.posts.size | plus: site.notes.size | divided_by: 7 | times: 6 }} Traduit par <a href="https://openrouter.ai">IA</a>)
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

**Changement clé** : Mise à jour du compteur pour inclure `site.notes.size` (nous le définirons ci-dessous). La formule reste la même mais prend maintenant en compte les notes. Si votre JS (`index.js`) met déjà à jour dynamiquement ce span en fonction des éléments visibles, il gérera automatiquement les comptes spécifiques à la langue.

### Étape 1 : Configurer les Notes comme une Collection Jekyll (dans `_config.yml`)

Pour traiter `_notes` comme `_posts` (afin que Jekyll traite les fichiers Markdown et les expose via `site.notes`), ajoutez ceci à votre `_config.yml`. Ceci est essentiel—sans cela, les notes n'auront pas `url`, `title`, `date`, etc., comme le font les posts.

```yaml
collections:
  notes:
    output: true
    permalink: /notes/:path/
```

- `output: true` génère des pages pour les notes (optionnel si vous voulez seulement les données).
- `permalink` assure des URLs comme `/notes/es/2025-11-07-tidb-vs-cockroachdb-es/` (à ajuster si nécessaire).
- Redémarrez votre serveur Jekyll après avoir ajouté ceci.

Maintenant `site.notes` fonctionne exactement comme `site.posts`, en supposant que vos fichiers de note (par exemple, `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md`) ont un frontmatter similaire : `title:`, `date:`, `image:`, `top:`, `translated:`, `generated:`.

### Étape 2 : Mise en Page de Page Modifiée (par exemple, `index.md` ou là où se trouve votre `<ul class="post-list">`)

Votre boucle actuelle ne montre que les posts en anglais. Pour ajouter des notes et supporter les 9 langues :

- Définissez une liste de langues une fois.
- Bouclez sur **toutes** les langues.
- Pour chaque langue, ajoutez les **posts** correspondants (de `_posts/{lang}/`) et les **notes** correspondantes (de `_notes/{lang}/`) comme éléments `<li>`.
- Chaque `<li>` reçoit `class="... lang-{lang}"` pour que votre JS puisse les filtrer (par exemple, masquer/afficher en fonction de la valeur `#sort-select`).
- Ceci remplit la liste entière dès le départ (masquée par JS), puis change les langues dynamiquement.
- Trier par date ? Ajoutez `| sort: 'date' | reverse` aux boucles si vous voulez le plus récent en premier (en supposant que les dates soient comparables).

Voici la mise en page complète mise à jour :

```html
---
layout: page
---
{% include sort.html %}

<ul class="post-list">
  {% if site.posts.size == 0 and site.notes.size == 0 %}
    <li class="list-group-item post-item">Aucune entrée disponible.</li>
  {% else %}
    {% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}
    {% for lang in langs %}
      {% comment %} Posts pour cette langue {% endcomment %}
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

      {% comment %} Notes pour cette langue (comme les posts) {% endcomment %}
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

**Changements clés** :
- **Tableau des langues** : `{% assign langs = "en,zh,ja,es,hi,fr,de,ar,hant" | split: "," %}`—correspond à vos options de sélection. Facile à maintenir.
- **Boucle des posts** : Supprimé le filtre codé en dur `en` ; vérifie maintenant `post.path contains "_posts/{{ lang }}/"` pour chaque langue.
- **Boucle des notes** : Ajoutée de manière identique, vérifiant `note.path contains "_notes/{{ lang }}/"`. Traite les notes exactement comme les posts (mêmes classes, attributs, structure).
- **Tri** : Ajouté `| sort: 'date' | reverse` aux deux boucles pour l'ordre chronologique (le plus récent en premier). À supprimer si non nécessaire.
- **Vérification vide** : Mise à jour pour inclure `site.notes.size`.
- **Performance** : Ceci génère le contenu de ~9 langues au moment de la construction. Correct pour les petits sites ; si énorme, envisagez la pagination ou la récupération par JS.

### Optionnel : Ajouter un Sélecteur de Type (Posts/Notes/Les Deux)

Vous avez mentionné "ajouter un sélecteur/interrupteur, deux options ou autre". Si vous voulez un **deuxième menu déroulant** pour filtrer par type (par exemple, Posts seulement, Notes seulement, ou Les Deux), ajoutez ceci à `sort.html` après le sélecteur de langue :

```html
<select id="type-select">
  <option value="both" selected>Posts & Notes</option>
  <option value="posts">Posts Only</option>
  <option value="notes">Notes Only</option>
</select>
```

Ensuite, ajoutez un attribut `data-type` à chaque `<li>` :
- Pour les posts : `data-type="posts"`
- Pour les notes : `data-type="notes"`

Mettez à jour votre `index.js` pour gérer les changements de `#type-select` (par exemple, filtrer `.post-item[data-type="notes"]` pour masquer/afficher). Ceci garde la simplicité sans changer le Liquid.

### Prochaines Étapes
- Test : Ajoutez un exemple de note comme `_notes/es/2025-11-07-tidb-vs-cockroachdb-es.md` avec frontmatter (title, date, etc.), reconstruisez, et passez à "Español" dans le menu déroulant—il devrait apparaître.
- Ajustements JS : Assurez-vous que `index.js` filtre par `.lang-{value}` et met à jour `#post-number` (par exemple, compte les `<li>` visibles). S'il ne gère pas encore les notes, ajoutez `data-type` comme ci-dessus.
- Si les chemins diffèrent (par exemple, pas de `/` final dans les répertoires), ajustez les vérifications `contains`.

Ceci intègre les notes de manière transparente tout en conservant votre configuration à 9 langues. Faites-moi savoir si vous avez besoin d'extraits JS ou d'autres ajustements !