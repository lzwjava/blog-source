---
audio: false
generated: true
lang: fr
layout: post
title: Bibliothèque JavaScript pour Markdown
translated: true
---

Il semble que vous demandiez comment utiliser la bibliothèque `marked`, version `^0.3.6`, qui est une bibliothèque JavaScript pour analyser du texte Markdown et le convertir en HTML. Comme vous faites référence à une version spécifique avec la notation `^0.3.6` (probablement à partir d'un fichier `package.json` dans un projet Node.js), je vais vous guider à travers l'utilisation de cette ancienne version de `marked`. Notez que la version `0.3.6` est assez ancienne (sortie autour de 2016), et la bibliothèque a beaucoup évolué depuis. Cependant, je vais me concentrer sur ce qui fonctionne pour cette version.

### Étape 1 : Installation
Si vous travaillez dans un environnement Node.js, vous pouvez installer `marked` version `0.3.6` en utilisant npm :

```bash
npm install marked@0.3.6
```

Le `^0.3.6` dans un fichier `package.json` signifie qu'il installera `0.3.6` ou toute mise à jour de correctif compatible (par exemple, `0.3.7`), mais pour plus de clarté, la commande ci-dessus le verrouille exactement à `0.3.6`.

### Étape 2 : Utilisation de base
Voici comment utiliser `marked` version `0.3.6` dans différents environnements :

#### Dans Node.js
1. **Requérir la bibliothèque** :
   Créez un fichier (par exemple, `index.js`) et ajoutez ce qui suit :

   ```javascript
   var marked = require('marked');
   ```

2. **Convertir Markdown en HTML** :
   Utilisez la fonction `marked()` en passant une chaîne Markdown. Par exemple :

   ```javascript
   var markdownString = '# Hello World\nThis is **bold** text.';
   var html = marked(markdownString);
   console.log(html);
   ```

   **Sortie** :
   ```html
   <h1>Hello World</h1>
   <p>This is <strong>bold</strong> text.</p>
   ```

#### Dans le navigateur
1. **Inclure la bibliothèque** :
   Vous pouvez utiliser un CDN ou télécharger `marked@0.3.6` et l'inclure via une balise `<script>`. Par exemple, en utilisant un lien CDN historique (si disponible) ou un fichier local :

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **L'utiliser en JavaScript** :
   Après avoir inclus le script, `marked` sera disponible globalement :

   ```html
   <script>
     var markdownString = '# Hello World\nThis is **bold** text.';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### Étape 3 : Options (pour la version 0.3.6)
La version `0.3.6` prend en charge certaines options de personnalisation. Vous pouvez passer un objet d'options en tant que deuxième argument à `marked()`. Voici un exemple :

```javascript
var markdownString = '# Hello\nThis is *text* with `code`.';
var html = marked(markdownString, {
  gfm: true,         // Activer le Markdown GitHub Flavored
  tables: true,      // Activer les tables GFM
  breaks: false,     // Si vrai, ajoute <br> sur les retours à la ligne simples
  pedantic: false,   // Si vrai, suit la spécification Markdown stricte
  sanitize: false,   // Si vrai, supprime les balises HTML pour la sécurité
  smartLists: true,  // Améliore le rendu des listes
  smartypants: false // Si vrai, utilise la typographie "intelligente" (par exemple, les guillemets courbes)
});
console.log(html);
```

### Fonctionnalités clés dans 0.3.6
- **Markdown de base** : Prend en charge les titres (`#`), le gras (`**`), l'italique (`*`), les listes, les blocs de code (```), etc.
- **Support GFM** : Le Markdown GitHub Flavored (comme les tables et les listes de tâches) est disponible si `gfm: true` est défini.
- **Pas de personnalisation du rendu** : Contrairement aux versions plus récentes, `0.3.6` ne prend pas en charge les rendus personnalisés, vous êtes donc limité à sa sortie par défaut.

### Exemple avec plus de Markdown
Voici un exemple plus complet dans Node.js :

```javascript
var marked = require('marked');

var markdown = `
# My Title
## Subtitle

- Item 1
- Item 2

\`\`\`
console.log("Hello");
\`\`\`

| Name  | Age |
|-------|-----|
| Alice | 25  |
| Bob   | 30  |
`;

var html = marked(markdown, { gfm: true, tables: true });
console.log(html);
```

**Sortie** :
```html
<h1>My Title</h1>
<h2>Subtitle</h2>
<ul>
<li>Item 1</li>
<li>Item 2</li>
</ul>
<pre><code>console.log("Hello");
</code></pre>
<table>
<thead>
<tr>
<th>Name</th>
<th>Age</th>
</tr>
</thead>
<tbody>
<tr>
<td>Alice</td>
<td>25</td>
</tr>
<tr>
<td>Bob</td>
<td>30</td>
</tr>
</tbody>
</table>
```

### Notes
- **Sanitisation** : Si vous rendez une entrée utilisateur, définissez `sanitize: true` pour supprimer le HTML brut pour la sécurité (par exemple, les balises `<script>`). Cependant, cela est basique dans `0.3.6` et pas aussi robuste que les alternatives modernes.
- **Limitations** : Cette version manque des fonctionnalités ajoutées dans les versions ultérieures (par exemple, l'analyse asynchrone, les tokenizers personnalisés), donc si vous en avez besoin, envisagez de mettre à jour vers une version plus récente comme `5.x`.
- **Débogage** : Si cela ne fonctionne pas, assurez-vous que la bibliothèque est chargée correctement et vérifiez la syntaxe Markdown.