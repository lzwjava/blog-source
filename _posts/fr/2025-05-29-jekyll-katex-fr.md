---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser KaTeX dans Jekyll
translated: true
type: note
---

Pour utiliser KaTeX au lieu de MathJax dans Jekyll avec votre configuration actuelle, vous devrez remplacer les scripts MathJax par KaTeX et ajuster votre configuration Jekyll. KaTeX est plus rapide et plus léger que MathJax, mais il nécessite une approche différente car il ne prend pas en charge toutes les fonctionnalités de MathJax (par exemple, la numérotation automatique des équations est plus manuelle). Voici un guide étape par étape pour passer à KaTeX sur votre site Jekyll :

### 1. Mettre à jour votre configuration Jekyll
Modifiez votre `_config.yml` pour utiliser KaTeX comme moteur mathématique pour Kramdown. Mettez à jour la section `kramdown` comme suit :

```yaml
kramdown:
  math_engine: katex
  input: GFM
  syntax_highlighter: rouge
```

Cela indique à Kramdown de rendre les expressions mathématiques LaTeX en utilisant KaTeX au lieu de MathJax.

### 2. Inclure KaTeX dans votre HTML
Supprimez les scripts MathJax de votre HTML et remplacez-les par KaTeX. Vous pouvez inclure KaTeX via un CDN. Ajoutez ce qui suit dans la section `<head>` de votre fichier de mise en page Jekyll (par exemple, `_layouts/default.html`) :

```html
<!-- KaTeX CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" integrity="sha384-nB0miv6/jRmo5SLY8cTjmnkA3wC7o1L0jOey4Cki5N3kdjdPD/mW59G1Qsxa8c3y" crossorigin="anonymous">

<!-- KaTeX JS -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" integrity="sha384-7zkKLzPD3M4y9W8FWsN4Z0yO5eLu8qUn0QHY6hZ2r3fDzqjk0McYc3vJrmE2h6cZ" crossorigin="anonymous"></script>

<!-- Extension Auto-render (optionnelle, pour le rendu automatique des mathématiques) -->
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" integrity="sha384-43gviWU0YVjaDtb/GhzOouOXtZMP/7XUzwPTL0xF3iS9Ho94fSc31UyUyIDgWvB4" crossorigin="anonymous"></script>

<!-- Configuration Auto-render -->
<script>
  document.addEventListener("DOMContentLoaded", function() {
    renderMathInElement(document.body, {
      delimiters: [
        {left: "$$", right: "$$", display: true}, // Mathématiques en bloc
        {left: "\\[", right: "\\]", display: true}, // Mathématiques en bloc
        {left: "\\(", right: "\\)", display: false}, // Mathématiques en ligne
        {left: "$", right: "$", display: false} // Mathématiques en ligne
      ],
      throwOnError: false
    });
  });
</script>
```

### 3. Supprimer la configuration MathJax
Supprimez le code lié à MathJax de votre fichier de mise en page, y compris le bloc `<script type="text/x-mathjax-config">` et le script CDN MathJax. KaTeX n'utilise pas de configuration comme `tex2jax` de MathJax, et le script auto-render ci-dessus gère une fonctionnalité similaire.

### 4. Écrire des mathématiques dans votre Markdown
Avec KaTeX et Kramdown configurés, vous pouvez écrire des mathématiques LaTeX dans vos fichiers Markdown en utilisant les mêmes délimiteurs qu'auparavant :

- **Mathématiques en ligne** : Utilisez `$...$` ou `\(...\)` (par exemple, `$E=mc^2$` ou `\(E=mc^2\)`).
- **Mathématiques affichées** : Utilisez `$$...$$` ou `\[...\]` (par exemple, `$$E=mc^2$$` ou `\[E=mc^2\]`).

Par exemple :

```markdown
Mathématiques en ligne : $E=mc^2$ ou \(E=mc^2\).

Mathématiques affichées :
$$E=mc^2$$

ou

\[E=mc^2\]
```

Kramdown avec le moteur mathématique KaTeX les transformera en HTML que KaTeX peut interpréter.

### 5. Notes sur KaTeX vs MathJax
- **Numérotation automatique des équations** : KaTeX ne prend pas en charge la numérotation automatique des équations comme `autoNumber: "AMS"` de MathJax. Si vous avez besoin de numéros d'équation, vous devez les ajouter manuellement en utilisant `\tag{}` dans votre code LaTeX (par exemple, `$$E=mc^2 \tag{1}$$`).
- **Performance** : KaTeX est significativement plus rapide que MathJax, ce qui est idéal pour les sites statiques comme Jekyll.
- **Ensemble de fonctionnalités** : KaTeX prend en charge moins de commandes LaTeX que MathJax. Consultez les [fonctions supportées par KaTeX](https://katex.org/docs/supported.html) pour vous assurer que vos expressions mathématiques sont compatibles.
- **Rendu** : Le script auto-render ci-dessus imite le comportement de MathJax en rendant automatiquement les expressions mathématiques dans les délimiteurs spécifiés. Ajustez le tableau `delimiters` dans le script si vous souhaitez modifier ou limiter les délimiteurs.

### 6. Tester votre configuration
Exécutez votre site Jekyll localement (`jekyll serve`) et vérifiez que les expressions mathématiques s'affichent correctement. Si vous rencontrez des problèmes :
- Vérifiez la console du navigateur pour des erreurs liées à KaTeX.
- Assurez-vous que les URLs CDN de KaTeX sont à jour (celles ci-dessus utilisent la version 0.16.11, la dernière à ma connaissance).
- Confirmez que vos fichiers Markdown utilisent une syntaxe LaTeX compatible avec KaTeX.

### 7. Optionnel : Fichiers KaTeX locaux
Si vous préférez héberger les fichiers KaTeX localement pour éviter la dépendance au CDN :
1. Téléchargez `katex.min.css`, `katex.min.js` et `auto-render.min.js` depuis les [versions GitHub de KaTeX](https://github.com/KaTeX/KaTeX/releases).
2. Placez-les dans votre dossier d'assets Jekyll (par exemple, `assets/katex/`).
3. Mettez à jour les balises `<link>` et `<script>` pour pointer vers vos fichiers locaux (par exemple, `/assets/katex/katex.min.css`).

### 8. Dépannage
- **Les mathématiques ne s'affichent pas** : Assurez-vous que les scripts KaTeX se chargent correctement et que `kramdown.math_engine` est défini sur `katex`.
- **Problèmes de délimiteurs** : Vérifiez que vos délimiteurs dans le script auto-render correspondent à ceux dans votre Markdown.
- **Commandes non supportées** : Si une commande LaTeX échoue, vérifiez la documentation de KaTeX pour les commandes supportées ou réécrivez l'expression.

Si vous avez besoin d'aide spécifique pour une expression mathématique ou une configuration particulière, partagez les détails et je pourrai vous fournir des conseils adaptés !