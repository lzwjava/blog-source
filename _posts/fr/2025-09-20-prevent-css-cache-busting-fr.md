---
audio: false
generated: true
image: false
lang: fr
layout: post
model: openai/gpt-5
title: Prévenir l'expiration du cache CSS de Jekyll
translated: true
type: note
---

Ce que vous voyez, c’est Jekyll (via le thème ou le pipeline `jekyll-assets`/`jekyll-feed`/`minima`) qui ajoute automatiquement une **empreinte (hash)** à l’URL de votre feuille de style pour le cache busting. C’est pourquoi le même fichier CSS se retrouve avec des chaînes de requête `?v=...` différentes après une reconstruction.

Si vous ne voulez pas que Jekyll modifie cette chaîne de requête à chaque construction, vous pouvez désactiver ou remplacer le comportement de « cache busting » / « digest » :

### Option 1. Utiliser un lien fixe

Au lieu de la balise d’aide de Jekyll (par exemple `{{ "/assets/css/style.css" | relative_url }}` ou `{{ "/assets/css/style.css" | asset_path }}`), codez en dur :

```html
<link rel="stylesheet" href="/assets/css/style.css">
```

De cette façon, aucune empreinte n’est injectée.

### Option 2. Désactiver le digest des assets

Si vous utilisez **jekyll-assets** ou un thème qui génère des empreintes pour les fichiers, vous pouvez désactiver le digest dans `_config.yml` :

```yml
assets:
  digest: false
```

### Option 3. Utiliser `relative_url` sans digest

Si votre thème utilise quelque chose comme :

```liquid
<link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
```

assurez-vous de ne pas le faire passer par `asset_path` ou `absolute_url` avec le digest activé. Utilisez simplement `relative_url`.

---

👉 En bref :

* Si vous voulez qu’il **ne change jamais**, codez le chemin en dur.
* Si vous voulez le contrôler via la configuration, définissez `assets.digest: false`.
* Si vous voulez toujours une version mais la garder stable, vous devriez gérer votre propre `?v=...` manuellement.

Voulez-vous qu’il soit **complètement statique** (ne change jamais), ou voulez-vous simplement empêcher Jekyll de **générer de nouveaux hash à chaque construction** ?