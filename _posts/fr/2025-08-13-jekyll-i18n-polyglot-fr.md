---
audio: false
generated: true
image: false
lang: fr
layout: post
title: 'Jekyll i18n : Extension Polyglot et Méthode par Dossier'
translated: true
type: note
---

Vous avez trois bonnes approches pour l'i18n dans un blog Jekyll, allant de la solution "clé en main" à la solution "minimaliste". Voici comment chacune fonctionne et comment la mettre en place.

# 1) Le plus simple : utiliser un plugin (jekyll-polyglot)

**Idéal si vous pouvez builder localement ou avec CI.** Le builder intégré de GitHub Pages n'autorise pas la plupart des plugins tiers, donc vous devez soit builder localement (`jekyll build`) et pousser le contenu généré `_site/`, soit utiliser GitHub Actions pour builder et publier.

**Installation**

```bash
gem install jekyll-polyglot
# ou ajouter au Gemfile :
# gem 'jekyll-polyglot'
```

**\_config.yml**

```yml
plugins:
  - jekyll-polyglot

languages: ["en", "zh", "ja"]   # vos langues
default_lang: "en"
exclude_from_localization: ["assets", "images", "CNAME"]  # garder les chemins statiques partagés
parallel_localization: true
```

**Structure du contenu**

```
_index.md               # page d'accueil optionnelle
_posts/
  2024-05-01-hello.en.md
  2024-05-01-hello.zh.md
pages/
  about.en.md
  about.zh.md
```

Polyglot construit des URLs spécifiques à chaque langue comme `/en/about/` et `/zh/about/`. Il expose aussi `site.active_lang`.

**Sélecteur de langue (dans votre layout)**

```liquid
<nav class="lang-switch">
  {% for lang in site.languages %}
    {% if lang == site.active_lang %}
      <span>{{ lang }}</span>
    {% else %}
      <a href="{{ page.url | prepend:'/' | replace_first:'/' | prepend:'/' | absolute_url | replace: '/' | relative_url | prepend:'/' }}">
        {%- comment -%}
        Nous allons reconstruire l'URL actuelle pour chaque langue :
        {%- endcomment -%}
      </a>
    {% endif %}
  {% endfor %}
</nav>
```

Une approche plus simple avec Polyglot est :

```liquid
<nav>
  {% for lang in site.languages %}
    <a href="{{ site.baseurl_root }}/{{ lang }}{{ page.permalink | default: page.url }}">{{ lang }}</a>
  {% endfor %}
</nav>
```

**Chaînes de l'interface via les fichiers de données**
Créez `_data/i18n.yml` :

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

Utilisation dans les templates :

```liquid
{{ site.data.i18n[site.active_lang].nav.home }}
```

**SEO (hreflang)**
Dans la section `<head>` de votre layout :

```liquid
{% assign langs = site.languages %}
{% for l in langs %}
  <link rel="alternate" hreflang="{{ l }}" href="{{ site.url }}/{{ l }}{{ page.url }}" />
{% endfor %}
<link rel="alternate" hreflang="x-default" href="{{ site.url }}/{{ site.default_lang }}{{ page.url }}" />
```

# 2) Sans plugin : dossiers par langue + Liquid

**Idéal si vous devez utiliser le builder intégré de GitHub Pages.**

**Structure**

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

**Définir une langue courante**
Ajoutez dans le front matter de chaque page :

```yml
---
layout: default
lang: en
---
```

ou déduisez-la du chemin :

```liquid
{% assign current_lang = page.lang | default: page.path | split:'/' | first | remove:'_' %}
```

**Liens croisés entre les traductions**
Utilisez un identifiant partagé dans le front matter :

```yml
---
layout: post
lang: en
ref: hello-post
---
```

Dans la version chinoise :

```yml
---
layout: post
lang: zh
ref: hello-post
---
```

Ensuite, dans le layout, trouvez les pages sœurs :

```liquid
{% assign siblings = site.pages | concat: site.posts | where:"ref", page.ref %}
{% for s in siblings %}
  {% unless s.url == page.url %}
    <a href="{{ s.url }}">{{ s.lang }}</a>
  {% endunless %}
{% endfor %}
```

**Chaînes de l'interface sans plugins**
Utilisez `_data/i18n.yml` comme ci-dessus, et choisissez la langue via `current_lang`.

**Redirection vers la langue par défaut (optionnelle)**
Créez `index.html` à la racine :

```html
<!doctype html>
<meta charset="utf-8">
<script>
  const lang = (navigator.language || '').toLowerCase().startsWith('zh') ? 'zh' : 'en';
  location.replace('/' + lang + '/');
</script>
<noscript><a href="/en/">English</a> · <a href="/zh/">中文</a></noscript>
```

# 3) Hybride : un seul ensemble d'articles, traduisez seulement l'interface

**Idéal si vous ne traduisez pas les articles, seulement l'interface (navigation, pied de page).**
Gardez un seul ensemble `/posts/`, ajoutez `_data/i18n.yml`, et affichez les libellés par langue. Fournissez des pages d'index par langue qui listent les mêmes articles, mais avec des dates et une interface localisées.

**Dates localisées**

```liquid
{% assign locale = page.lang | default: site.default_lang %}
{{ page.date | date: "%B %-d, %Y" }}  {# ou utilisez des filtres/plugins si vous en avez #}
```

(La fonction `date` intégrée de Jekyll n'est pas entièrement sensible aux paramètres régionaux ; pour un formatage véritablement localisé, vous aurez besoin d'un plugin ou de chaînes préformatées dans les données.)

---

## Conseils pratiques

* **Slugs :** Gardez le même `ref` pour les versions traduites correspondantes ; laissez les titres varier par langue.
* **Images :** Placez les images partagées dans `/assets/` et excluez-les de la localisation pour que les URLs restent stables.
* **Sitemaps & SEO :** Générez des sitemaps par langue ou assurez-vous que votre sitemap liste toutes les URLs des différentes langues ; ajoutez des balises canoniques dans chaque version linguistique.
* **Flux :** Créez des flux par langue en ciblant les collections : filtrez les articles par `lang` dans votre template de flux.

---

## Exemple minimal fonctionnel (sans plugin)

1.  `_data/i18n.yml` avec les chaînes.
2.  `_en/index.md` et `_zh/index.md` avec le front matter `lang`.
3.  Les articles sous `_posts/en/` et `_posts/zh/` avec `lang` et un `ref` partagé.
4.  Le layout utilise `site.data.i18n[current_lang]` et l'extrait de code de recherche de pages sœurs ci-dessus.

Si vous me donnez la structure actuelle de votre dépôt (et si vous build directement sur GitHub Pages ou via Actions), je peux adapter une configuration prête à l'emploi et quelques layouts de démarrage.