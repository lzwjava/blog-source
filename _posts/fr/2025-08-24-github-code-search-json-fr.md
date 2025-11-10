---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Conseils pour la Recherche de Code GitHub JSON
translated: true
type: note
---

Vous pouvez écrire une requête de recherche de code GitHub comme ceci :

```
"deepseek/deepseek-chat-v3.1" language:JSON
```

### Notes :

* Les guillemets garantissent que GitHub recherche la chaîne exacte `deepseek/deepseek-chat-v3.1`.
* `language:JSON` (ou `lang:json`, les deux fonctionnent) limite les résultats aux fichiers JSON.
* Si vous souhaitez inclure des configurations de type JSON qui ne sont pas dans des fichiers `.json` (comme `.ipynb` ou `.eslintrc`), vous pouvez supprimer le filtre `lang:`.

Exemples :

* Rechercher uniquement les fichiers JSON :

  ```
  "deepseek/deepseek-chat-v3.1" lang:json
  ```

* Rechercher tous les types de fichiers tout en mettant en évidence les résultats JSON :

  ```
  "deepseek/deepseek-chat-v3.1"
  ```

Souhaitez-vous également que je vous montre comment affiner cette recherche davantage — par exemple, en recherchant uniquement dans les dépôts, les issues ou le code ?