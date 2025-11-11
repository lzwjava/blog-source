---
audio: false
generated: true
lang: fr
layout: post
title: Correction du Formatage des Matrices dans un Blog Jekyll
translated: true
type: note
---

Le problème que vous rencontrez est lié à la façon dont Markdown (kramdown) traite le contenu avant que MathJax ne le rende. Les doubles barres obliques inverses (`\\`) dans votre matrice sont interprétées par Markdown avant que MathJax ne les atteigne, ce qui casse le formatage de la matrice.

Voici quelques solutions pour résoudre ce problème :

### Solution 1 : Échapper les barres obliques inverses
Vous pouvez échapper chaque barre oblique inverse avec une autre barre oblique inverse :

```latex
$A - I = \begin{pmatrix} 1 & -3 & 0 \\\ 2 & 1 & 0 \\\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\\ 0 & 1 & 0 \\\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\\ 2 & 0 & 0 \\\ 0 & 0 & 1 \end{pmatrix}$
```

### Solution 2 : Utiliser `\\` dans les blocs mathématiques
Pour les mathématiques en mode display (et non en ligne), utilisez `$$` ou `\\\[ \\\]` :

```latex
$$
A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
```

### Solution 3 : Utiliser des balises HTML pour empêcher le traitement Markdown
Encadrez vos mathématiques avec des balises HTML `div` pour empêcher le traitement Markdown :

```html
<div>
$$
A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$
</div>
```

### Solution 4 : Modifier votre configuration kramdown
Ajoutez ceci à votre `_config.yml` pour empêcher kramdown de traiter les blocs mathématiques :

```yaml
kramdown:
  math_engine: mathjax
  syntax_highlighter: rouge
```

Ensuite, vous pouvez utiliser :

```latex
$$ A - I = \begin{pmatrix} 1 & -3 & 0 \\ 2 & 1 & 0 \\ 0 & 0 & 2 \end{pmatrix} - \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -3 & 0 \\ 2 & 0 & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
```

Essayez ces solutions une par une pour voir laquelle fonctionne le mieux avec votre configuration Jekyll. La solution la plus fiable est généralement d'utiliser les mathématiques en mode display (`$$` ou `\\\[ \\\]`) au lieu des mathématiques en ligne (`$`) pour les matrices et autres équations complexes.