---
audio: false
date: 2025-09-09
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Génération de Fichiers de Plan de Site pour Jekyll
translated: true
type: note
---

Un fichier **sitemap.xml** est un fichier XML qui indique aux moteurs de recherche comme Google et Bing quelles pages se trouvent sur votre site web. Il aide les robots d'indexation à découvrir et à indexer la structure de votre site plus efficacement. Pour un blog Jekyll, cela signifie que les moteurs de recherche peuvent trouver tous vos articles, pages et traductions (comme vos `index-zh.html`, `index-fr.html`, etc.) même s'ils ne sont pas liés partout.

### Utilité d'un Sitemap

* Liste toutes les URL importantes de votre site.
* Fournit des métadonnées telles que la date de dernière modification (`<lastmod>`), la fréquence de changement (`<changefreq>`) et la priorité (`<priority>`).
* Améliore le SEO en s'assurant que les robots d'indexation ne manquent aucune page.

### Comment le générer pour Jekyll

Vous avez plusieurs approches :

#### 1. Utiliser le plugin `jekyll-sitemap` (recommandé)

1. Dans le `Gemfile` de votre projet Jekyll, ajoutez :

   ```ruby
   gem 'jekyll-sitemap'
   ```
2. Dans votre `_config.yml`, ajoutez :

   ```yaml
   plugins:
     - jekyll-sitemap
   ```

   (Si vous utilisez GitHub Pages, `jekyll-sitemap` est déjà sur la liste blanche, donc il fonctionne directement.)
3. Lorsque vous effectuez la construction (`jekyll build` ou via `make` si vous l'avez configuré), Jekyll générera automatiquement un `sitemap.xml` dans votre dossier `_site/`.

#### 2. Créer manuellement un modèle de sitemap

Si vous préférez un contrôle plus fin :

1. Créez un fichier à la racine du projet : `/sitemap.xml`.
2. Ajoutez ce modèle Liquid :

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
3. Assurez-vous que votre `_config.yml` contient `url: "https://votredomaine.com"` pour que les liens soient générés correctement.

#### 3. Vérification

* Après la construction, vérifiez `_site/sitemap.xml`.
* Soumettez-le à la Google Search Console pour une meilleure indexation.

---

👉 Étant donné que vous avez déjà `_config.yml` et `_plugins/`, le plus simple est d'activer `jekyll-sitemap`. Ainsi, vous n'aurez pas à maintenir le XML manuellement.

Voulez-vous que je rédige l'ajout exact pour votre `_config.yml` (en me basant sur vos fichiers actuels), afin que vous puissiez le coller directement ?