---
audio: false
generated: true
lang: fr
layout: post
title: Rendu Markdown avec MathJax ou KaTeX
translated: true
type: note
---

Pour combiner le rendu des mathématiques LaTeX avec le rendu **Markdown** sur une page web, vous utiliseriez généralement une bibliothèque JavaScript (comme **MathJax** ou **KaTeX**) conjointement avec un analyseur Markdown capable de traiter la syntaxe Markdown standard. L'objectif est de permettre aux utilisateurs d'écrire des formules mathématiques en LaTeX dans du Markdown et de les faire afficher correctement sur la page.

Voici comment y parvenir :

### 1. **Rendu Markdown avec MathJax ou KaTeX**

Vous pouvez utiliser un **analyseur Markdown** comme **marked.js** ou **remarkable.js** pour afficher le contenu Markdown de base. Ensuite, après le rendu du contenu Markdown, utilisez MathJax ou KaTeX pour afficher les mathématiques LaTeX qu'il contient.

Voici une approche étape par étape pour y parvenir.

---

### **Étape 1 : Inclure les bibliothèques**

Vous devez inclure à la fois un **analyseur Markdown** et une **bibliothèque de rendu mathématique** (MathJax ou KaTeX) dans votre fichier HTML.

Voici comment vous pouvez les inclure :

```html
<!-- Inclure KaTeX (ou MathJax) pour le rendu LaTeX -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.css">
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.js"></script>
<script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/contrib/auto-render.min.js"></script>

<!-- Inclure un analyseur Markdown (comme marked.js) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.0.10/marked.min.js"></script>
```

Alternativement, si vous préférez **MathJax** à KaTeX, vous pouvez l'inclure comme ceci :

```html
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

---

### **Étape 2 : Configurer le processus de rendu Markdown vers LaTeX**

Maintenant, vous pouvez écrire votre structure HTML et utiliser JavaScript pour afficher le Markdown, puis traiter toutes les formules LaTeX dans ce Markdown.

Voici un exemple simple :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rendu Markdown + Math</title>

  <!-- Inclure KaTeX pour le rendu mathématique -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/katex.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.15.3/contrib/auto-render.min.js"></script>

  <!-- Inclure marked.js pour le rendu Markdown -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/marked/4.0.10/marked.min.js"></script>
</head>
<body>

  <h1>Exemple de Rendu Markdown + Math</h1>

  <!-- Zone de texte pour la saisie Markdown -->
  <textarea id="markdownInput" rows="10" cols="50">
Ceci est un éditeur Markdown. Vous pouvez ajouter des formules mathématiques LaTeX comme ceci :

Math en ligne : \( E = mc^2 \)

Math en bloc :
\[
\int_0^1 x^2 \, dx = \frac{1}{3}
\]
  </textarea>

  <hr>

  <!-- Conteneur pour le Markdown rendu -->
  <div id="markdownOutput"></div>

  <script>
    // Fonction pour afficher Markdown + Math
    function renderMarkdown() {
      // Obtenir le Markdown saisi
      const markdownText = document.getElementById('markdownInput').value;

      // Afficher le contenu Markdown
      const htmlContent = marked(markdownText);

      // Insérer le HTML généré dans la div de sortie
      document.getElementById('markdownOutput').innerHTML = htmlContent;

      // Afficher les mathématiques dans le contenu HTML en utilisant KaTeX
      renderMathInElement(document.getElementById('markdownOutput'), {
        delimiters: [
          { left: "\\(", right: "\\)", display: false }, // math en ligne
          { left: "\\[", right: "\\]", display: true }   // math en bloc
        ]
      });
    }

    // Appeler la fonction renderMarkdown au chargement de la page et à chaque modification de la saisie
    renderMarkdown();
    document.getElementById('markdownInput').addEventListener('input', renderMarkdown);
  </script>
</body>
</html>
```

### **Explication du code :**

1. **Analyse Markdown :**
   - La bibliothèque `marked.js` est utilisée pour convertir le Markdown saisi (écrit dans la `<textarea>`) en HTML. La syntaxe Markdown sera traitée et convertie en HTML dans le conteneur `<div id="markdownOutput"></div>`.

2. **Rendu Mathématique :**
   - Les équations LaTeX dans le Markdown (en ligne `\( ... \)` et en bloc `\[ ... \]`) sont affichées en utilisant la fonction `renderMathInElement()` de **KaTeX**.
   - **KaTeX** recherche `\( ... \)` pour les math en ligne et `\[ ... \]` pour les math en bloc dans le contenu HTML et les affiche automatiquement.

3. **Éditeur Markdown Interactif :**
   - Lorsque l'utilisateur tape dans la `<textarea>`, la fonction `renderMarkdown` est appelée pour mettre à jour le contenu dynamiquement, en analysant le Markdown et en affichant les formules LaTeX.

---

### **Étape 3 : Personnalisation pour différents frameworks frontend**

Vous pouvez adapter cette solution pour qu'elle fonctionne avec n'importe quel framework frontend comme **React**, **Vue** ou **Angular**. Par exemple, voici une implémentation **React** pour le rendu en temps réel Markdown + LaTeX :

#### **Exemple React**

1. **Installer KaTeX et marked via npm :**

```bash
npm install katex marked
```

2. **Composant React pour le rendu Markdown + Math :**

```jsx
import React, { useState, useEffect } from 'react';
import marked from 'marked';
import katex from 'katex';
import 'katex/dist/katex.min.css';

const MarkdownEditor = () => {
  const [markdown, setMarkdown] = useState('');

  useEffect(() => {
    // Afficher les formules mathématiques en utilisant KaTeX après le montage du composant
    renderMath();
  }, [markdown]);

  const renderMath = () => {
    const renderedHTML = marked(markdown);
    document.getElementById('markdownOutput').innerHTML = renderedHTML;

    // Afficher les formules mathématiques LaTeX avec KaTeX
    katex.renderMathInElement(document.getElementById('markdownOutput'), {
      delimiters: [
        { left: "\\(", right: "\\)", display: false }, // math en ligne
        { left: "\\[", right: "\\]", display: true }   // math en bloc
      ]
    });
  };

  return (
    <div>
      <h1>Rendu Markdown + Math</h1>
      <textarea
        value={markdown}
        onChange={(e) => setMarkdown(e.target.value)}
        rows="10"
        cols="50"
      />
      <hr />
      <div id="markdownOutput"></div>
    </div>
  );
};

export default MarkdownEditor;
```

Dans la version React, nous utilisons la bibliothèque `marked` pour convertir le texte Markdown en HTML, et la fonction `renderMathInElement()` de KaTeX pour traiter et afficher toutes les formules mathématiques LaTeX dans le HTML.

---

### **Résumé**
- Utilisez un **analyseur Markdown** (comme `marked.js`) pour convertir la syntaxe Markdown en HTML.
- Utilisez **MathJax** ou **KaTeX** pour afficher les expressions mathématiques LaTeX intégrées dans le contenu Markdown.
- Combinez les deux en convertissant le Markdown en HTML et en traitant les formules mathématiques dynamiquement à l'aide de KaTeX/MathJax.

Cette approche permet aux utilisateurs d'écrire et de prévisualiser du contenu Markdown avec des équations mathématiques en temps réel, ce qui est parfait pour des applications comme les éditeurs de blog, les systèmes de base de connaissances ou les outils éducatifs !