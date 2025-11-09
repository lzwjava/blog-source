---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: À la poursuite du mauvais octet
translated: true
type: note
---

### Pourquoi cela n'a pas trouvé le mauvais octet
La sortie `hexdump` que vous avez obtenue correspondait **à l'offset du fichier** (`000008d0`), et non à un octet `\x8D` dans le contenu réel. Grep effectue une recherche textuelle sur toute la ligne, et "8d" apparaît dans l'adresse hexadécimale (par exemple, `08d0`), donc il a récupéré cette ligne non pertinente. Les octets de données à cet endroit (`6f 67 20 ...`) sont juste de l'ASCII normal pour `"og = og_images[i"`, aucun problème.

### Meilleures méthodes pour traquer le `\x8D`
Essayez ces commandes dans votre répertoire de projet (à côté de `_layouts/default.html`). Elles analyseront directement les octets du fichier.

1. **Hexdump amélioré (Recherche d'octet dans les données)** :
   Ceci recherche ` 8d ` (avec des espaces autour pour correspondre aux octets hexadécimaux, pas aux offsets) :
   ```
   hexdump -C _layouts/default.html | grep ' 8d '
   ```
   - Si quelque chose est trouvé, vous verrez l'offset (colonne de gauche) et les octets environnants. Notez l'offset, puis allez à cette position dans votre éditeur (par exemple, VS Code : Ctrl+G > offset_octet / 16 pour une approximation de ligne).
   - Exemple de sortie en cas de succès : `00001234  ...  8d  20  61  62  ... |... ab...|`

2. **Utiliser `xxd` (Souvent mieux que Hexdump)** :
   macOS intègre `xxd` :
   ```
   xxd _layouts/default.html | grep 8d
   ```
   - Similaire : Recherche "8d" dans les octets hexadécimaux. Si aucune sortie, l'octet n'est pas présent (rare, mais possible s'il est dans un autre fichier).

3. **Grep binaire (Recherche directe d'octet)** :
   ```
   grep -a -o -P '\x8d' _layouts/default.html | hexdump -C
   ```
   - Ceci extrait les correspondances exactes de l'octet et les affiche en hexadécimal. Si vide, pas de `\x8D`.

4. **One-Liner Ruby (Position précise)** :
   Comme je l'ai suggéré précédemment — exécutez ceci pour obtenir l'index de l'octet :
   ```
   ruby -e "File.open('_layouts/default.html', 'rb') { |f| f.read.each_byte.with_index { |b, i| puts \"Found at byte #{i}: #{b.chr(Encoding::ASCII_8BIT).inspect}\" if b == 0x8D } }"
   ```
   - Sortie du type : `Found at byte 1234: "\x8D"`. Puis éditez : Ouvrez le fichier, allez au caractère ~1234 (ou ligne = 1234/80 environ), et supprimez le caractère invisible (il pourrait sembler vide ; sélectionnez/supprimez autour de lui).

### Si aucune correspondance ?
- Le `\x8D` pourrait être dans un **fichier différent** (par exemple, un article dans `_posts/` rendu via `{{ content }}` dans le layout). Scannez tout le site :
  ```
  find . -name "*.md" -o -name "*.html" | xargs grep -l $'\x8D'
  ```
  (Ou utilisez le script Ruby sur chaque fichier suspect.)
- Ou c'est un BOM/caractère invisible au début du fichier : Ouvrez dans l'éditeur, supprimez la première ligne si elle est vide, re-sauvegardez en UTF-8.

Une fois supprimé, exécutez `bundle exec jekyll serve --incremental` à nouveau. Si toujours bloqué, collez la sortie d'une de ces commandes (ou celle de Ruby), et nous le trouverons.

[Conseils Hexdump pour la chasse aux octets](https://unix.stackexchange.com/questions/38331/finding-bad-characters-in-hex-dump)