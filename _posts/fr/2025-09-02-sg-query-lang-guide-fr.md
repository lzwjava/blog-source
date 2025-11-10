---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide du langage de requête Sourcegraph
translated: true
type: note
---

La recherche Sourcegraph possède son propre langage de requête, flexible et puissant. Voici un aperçu de la syntaxe courante que vous pouvez utiliser :

---

### 1. **Recherche par mot-clé basique**

* Tapez simplement les termes :

  ```
  http client
  ```

  Trouve les fichiers ou le code contenant les deux mots.

---

### 2. **Opérateurs logiques**

* `AND`, `OR`, `NOT` (doivent être en majuscules) :

  ```
  React AND useEffect
  React OR Vue
  logger NOT debug
  ```

---

### 3. **Filtres**

* `repo:` → limiter par dépôt

  ```
  repo:github.com/myorg/myrepo
  ```
* `file:` → correspondre au chemin du fichier (regex supporté)

  ```
  file:\.java$
  ```
* `lang:` → restreindre à un langage de programmation

  ```
  lang:python requests
  ```
* `content:` → forcer une recherche textuelle (ignore les correspondances structurelles)

  ```
  content:"SELECT * FROM"
  ```
* `case:yes` → rendre la recherche sensible à la casse

---

### 4. **Correspondance par expression régulière (Regex)**

* Par défaut, Sourcegraph supporte les regex.

  ```
  foo(bar|baz)
  ^class\s+\w+
  ```

---

### 5. **Recherche structurelle**

Utilisez des motifs avec des trous comme `:[var]` pour correspondre à des structures de code :

```
if (:[cond]) { :[body] }
```

---

### 6. **Recherche par révision / branche**

* Ajoutez `@branch`, `@commit`, ou `@tag` :

  ```
  repo:myrepo@main lang:go fmt.Println
  ```

---

### 7. **Symboles et définitions**

* `type:symbol` → rechercher des noms de symboles
* `type:commit` → rechercher dans les messages de commit
* `type:diff` → rechercher dans les diffs de code

---

### 8. **Exemples**

* Trouver tous les commentaires `TODO` dans les fichiers Go :

  ```
  TODO lang:go
  ```
* Rechercher uniquement dans le dossier `src/` pour les méthodes Java :

  ```
  file:^src/ lang:java "public static"
  ```
* Rechercher dans plusieurs dépôts :

  ```
  repo:github.com/org/.* file:\.ts$ "useState"
  ```

---

👉 Souhaitez-vous que je prépare un **aide-mémoire rapide des requêtes Sourcegraph les plus utilisées** (comme des requêtes d'une ligne que vous pouvez réutiliser quotidiennement), ou une **analyse approfondie avec des modèles avancés** ?