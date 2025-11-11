---
audio: false
generated: true
lang: fr
layout: post
title: Bibliothèque JavaScript pour Markdown
translated: true
type: note
---

Il semble que vous demandiez comment utiliser la bibliothèque `marked`, version `^0.3.6`, qui est une bibliothèque JavaScript pour analyser le texte Markdown et le convertir en HTML. Étant donné que vous faites référence à une version spécifique avec la notation `^0.3.6` (probablement issue d'un fichier `package.json` dans un projet Node.js), je vais vous guider pour utiliser cette ancienne version de `marked`. Notez que la version `0.3.6` est assez ancienne (publiée vers 2016), et la bibliothèque a considérablement évolué depuis. Cependant, je m'en tiendrai à ce qui fonctionne pour cette version.

### Étape 1 : Installation
Si vous travaillez dans un environnement Node.js, vous pouvez installer `marked` version `0.3.6` en utilisant npm :

```bash
npm install marked@0.3.6
```

Le `^0.3.6` dans un `package.json` signifie qu'il installera `0.3.6` ou toute mise à jour corrective compatible (par exemple, `0.3.7`), mais pour plus de clarté, la commande ci-dessus la verrouille exactement sur `0.3.6`.

### Étape 2 : Utilisation de base
Voici comment utiliser `marked` version `0.3.6` dans différents environnements :

#### Dans Node.js
1. **Importer la bibliothèque** :
   Créez un fichier (par exemple, `index.js`) et ajoutez ce qui suit :

   ```javascript
   var marked = require('marked');
   ```

2. **Convertir le Markdown en HTML** :
   Utilisez la fonction `marked()` en lui passant une chaîne Markdown. Par exemple :

   ```javascript
   var markdownString = '# Hello World\nCeci est un texte en **gras**.';
   var html = marked(markdownString);
   console.log(html);
   ```

   **Sortie** :
   ```html
   <h1>Hello World</h1>
   <p>Ceci est un texte en <strong>gras</strong>.</p>
   ```

#### Dans le navigateur
1. **Inclure la bibliothèque** :
   Vous pouvez utiliser un CDN ou télécharger `marked@0.3.6` et l'inclure via une balise `<script>`. Par exemple, en utilisant un lien CDN historique (s'il est disponible) ou un fichier local :

   ```html
   <script src="https://cdn.jsdelivr.net/npm/marked@0.3.6"></script>
   ```

2. **L'utiliser en JavaScript** :
   Après avoir inclus le script, `marked` sera disponible globalement :

   ```html
   <script>
     var markdownString = '# Hello World\nCeci est un texte en **gras**.';
     var html = marked(markdownString);
     console.log(html);
   </script>
   ```

### Étape 3 : Options (pour la version 0.3.6)
La version `0.3.6` prend en charge certaines options de personnalisation. Vous pouvez passer un objet d'options comme second argument à `marked()`. Voici un exemple :

```javascript
var markdownString = '# Hello\nCeci est du *texte* avec du `code`.';
var html = marked(markdownString, {
  gfm: true,         // Activer GitHub Flavored Markdown
  tables: true,      // Activer les tables GFM
  breaks: false,     // Si true, ajoute <br> sur les sauts de ligne simples
  pedantic: false,   // Si true, suit strictement la spécification Markdown
  sanitize: false,   // Si true, supprime les balises HTML pour la sécurité
  smartLists: true,  // Améliore le rendu des listes
  smartypants: false // Si true, utilise une typographie "intelligente" (ex : guillemets courbes)
});
console.log(html);
```

### Fonctionnalités clés dans la version 0.3.6
- **Markdown de base** : Prend en charge les titres (`#`), le gras (`**`), l'italique (`*`), les listes, les blocs de code (```), etc.
- **Support GFM** : GitHub Flavored Markdown (comme les tables et les listes de tâches) est disponible si `gfm: true` est défini.
- **Aucune personnalisation du rendu** : Contrairement aux versions plus récentes, `0.3.6` ne prend pas en charge les rendus personnalisés, vous êtes donc limité à sa sortie par défaut.

### Exemple avec plus de Markdown
Voici un exemple plus complet dans Node.js :

```javascript
var marked = require('marked');

var markdown = `
# Mon Titre
## Sous-titre

- Élément 1
- Élément 2

\`\`\`
console.log("Hello");
\`\`\`

| Nom   | Âge |
|-------|-----|
| Alice | 25  |
| Bob   | 30  |
`;

var html = marked(markdown, { gfm: true, tables: true });
console.log(html);
```

**Sortie** :
```html
<h1>Mon Titre</h1>
<h2>Sous-titre</h2>
<ul>
<li>Élément 1</li>
<li>Élément 2</li>
</ul>
<pre><code>console.log("Hello");
</code></pre>
<table>
<thead>
<tr>
<th>Nom</th>
<th>Âge</th>
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
- **Assainissement (Sanitization)** : Si vous affichez une entrée utilisateur, définissez `sanitize: true` pour supprimer le HTML brut pour des raisons de sécurité (par exemple, les balises `<script>`). Cependant, ceci est basique dans `0.3.6` et moins robuste que les alternatives modernes.
- **Limitations** : Cette version manque de fonctionnalités ajoutées dans les versions ultérieures (par exemple, l'analyse asynchrone, les tokeniseurs personnalisés), donc si vous avez besoin de plus, envisagez de passer à une version plus récente comme `5.x`.
- **Débogage** : Si cela ne fonctionne pas, assurez-vous que la bibliothèque est chargée correctement et vérifiez la syntaxe Markdown.