---
audio: false
generated: true
lang: fr
layout: post
title: Rendu LaTeX dans Hugo
translated: true
type: note
---

Le problème que vous décrivez se produit dans **Jekyll** lors de l'utilisation de **Kramdown** avec **MathJax** comme moteur mathématique. Kramdown, lorsqu'il est configuré avec `math_engine: mathjax`, interprète les parenthèses `( )` dans le contenu Markdown comme des délimiteurs LaTeX pour les mathématiques en ligne (par exemple, `\( \)`), ce qui peut interrompre le texte normal contenant des parenthèses. Cela se produit parce que MathJax est configuré pour analyser `\( \)` ou `$ $` pour les mathématiques en ligne, comme indiqué dans votre configuration.

Dans **Hugo**, ce problème est moins susceptible de se produire par défaut, mais cela dépend de la façon dont vous configurez le processeur Markdown de Hugo et l'intégration MathJax. Ci-dessous, j'expliquerai pourquoi Hugo évite ce problème dans la plupart des cas, comment le prévenir ou le corriger dans Jekyll, et comment s'assurer qu'il ne se produise pas dans Hugo.

---

### **Hugo a-t-il ce problème ?**
Hugo évite généralement ce problème car :
1.  **Processeur Markdown** : Hugo utilise **Goldmark** (ou optionnellement Blackfriday) comme rendu Markdown par défaut, qui n'active pas MathJax ou l'analyse LaTeX par défaut. À moins que vous ne configuriez explicitement Hugo pour utiliser MathJax et que vous définissiez des délimiteurs de mathématiques en ligne comme `\( \)`, les parenthèses normales `( )` dans votre contenu ne seront pas interprétées à tort comme du LaTeX.
2.  **Intégration MathJax** : Hugo n'analyse pas nativement le LaTeX. Si vous voulez la prise en charge de MathJax, vous devez ajouter manuellement les scripts MathJax (comme celui que vous avez fourni) aux modèles de votre thème (par exemple, dans `layouts/partials/head.html`) et configurer les délimiteurs. La flexibilité de Hugo vous permet de contrôler la façon dont MathJax traite le contenu, évitant ainsi l'analyse automatique de `( )` sauf si elle est explicitement activée.
3.  **Shortcodes pour les mathématiques** : Les utilisateurs de Hugo implémentent souvent le rendu LaTeX en utilisant des shortcodes (par exemple, `{{< math >}}...{{< /math >}}`), qui désignent explicitement le contenu mathématique, empêchant ainsi les parenthèses normales d'être confondues avec du LaTeX.

En résumé, Hugo n'aura pas ce problème à moins que vous ne configuriez MathJax avec les mêmes délimiteurs en ligne (`\( \)`) et que vous n'activiez l'analyse automatique sans les protections appropriées. En utilisant des shortcodes ou en évitant `\( \)` comme délimiteurs, Hugo peut éviter complètement ce problème.

---

### **Corriger le problème dans Jekyll**
Dans Jekyll, le problème se produit parce que le paramètre `math_engine: mathjax` de Kramdown, combiné à votre configuration MathJax, entraîne l'analyse de `( )` comme du LaTeX. Voici comment le corriger :

#### **1. Changer les délimiteurs en ligne de MathJax**
Modifiez la configuration MathJax pour utiliser différents délimiteurs de mathématiques en ligne, tels que `$ $`, au lieu de `\( \)` pour éviter les conflits avec les parenthèses normales. Mettez à jour le script dans le HTML de votre site Jekyll (par exemple, dans `_includes/head.html`) :

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [['$','$']], // Utiliser $ $ pour les mathématiques en ligne
      displayMath: [['$$','$$'], ['\[','\]']],
      processEscapes: true // Permettre d'échapper $ pour l'utiliser littéralement
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": { linebreaks: { automatic: true } },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```

-   **Pourquoi cela fonctionne** : En supprimant `['\(','\)']` de `inlineMath`, MathJax n'interprète plus `( )` comme des délimiteurs LaTeX, les préservant ainsi pour le texte normal. Le paramètre `processEscapes: true` vous permet d'écrire `\$` dans Markdown pour afficher un `$` littéral si nécessaire.
-   **Dans votre Markdown** : Utilisez `$x^2$` pour les mathématiques en ligne au lieu de `\(x^2\)`. Par exemple :
    ```markdown
    Voici une formule : $x^2 + y^2 = z^2$. Texte normal (non analysé).
    ```

#### **2. Échapper les parenthèses dans Markdown**
Si vous souhaitez conserver `\( \)` comme délimiteurs, échappez les parenthèses dans votre contenu Markdown pour empêcher Kramdown/MathJax de les analyser comme du LaTeX. Utilisez une barre oblique inverse `\` avant chaque parenthèse :

```markdown
Texte normal \(pas une formule\). Ceci est une vraie formule : \(x^2 + y^2\).
```

-   **Résultat** : Le texte échappé `\(pas une formule\)` s'affiche comme `(pas une formule)`, tandis que `\(x^2 + y^2\)` s'affiche comme une formule LaTeX.
-   **Inconvénient** : Cela nécessite d'échapper manuellement chaque instance de `( )` dans votre contenu, ce qui peut être fastidieux.

#### **3. Désactiver MathJax pour des pages spécifiques**
Si vous n'avez besoin de MathJax que sur certaines pages (par exemple, pour des articles à forte composante mathématique), désactivez-le par défaut et activez-le uniquement là où c'est nécessaire :
-   Supprimez le script MathJax de votre `_layouts/default.html` ou `_includes/head.html` global.
-   Ajoutez une inclusion conditionnelle dans votre mise en page ou le front matter de la page. Par exemple, dans `_layouts/post.html` :

```html
{% if page.mathjax %}
  <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      tex2jax: {
        inlineMath: [['$','$']],
        displayMath: [['$$','$$'], ['\[','\]']],
        processEscapes: true
      }
    });
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
{% endif %}
```

-   Dans le front matter de votre fichier Markdown, activez MathJax uniquement pour des pages spécifiques :
    ```yaml
    ---
    title: Mon Article de Maths
    mathjax: true
    ---
    ```

-   **Pourquoi cela fonctionne** : Les pages sans `mathjax: true` ne chargeront pas MathJax, donc `( )` ne seront pas analysés comme du LaTeX.

#### **4. Utiliser un autre moteur mathématique**
Passez de MathJax à un autre moteur mathématique pris en charge par Kramdown, comme **KaTeX**, qui est plus rapide et moins susceptible de mal interpréter les parenthèses à moins d'être explicitement configuré. Installez KaTeX dans votre site Jekyll :
-   Ajoutez les scripts KaTeX à `_includes/head.html` :
    ```html
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/auto-render.min.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false }
          ]
        });
      });
    </script>
    ```
-   Mettez à jour `_config.yml` :
    ```yaml
    kramdown:
      math_engine: katex
      input: GFM
      syntax_highlighter: rouge
    ```

-   **Pourquoi cela fonctionne** : KaTeX est plus strict concernant l'analyse et utilise par défaut `$ $` pour les mathématiques en ligne, réduisant les conflits avec `( )`. Il est également plus rapide que MathJax.

---

### **S'assurer que Hugo évite ce problème**
Pour utiliser MathJax dans Hugo sans rencontrer le problème d'analyse des `( )`, suivez ces étapes :

1.  **Ajouter MathJax à Hugo** :
    -   Placez le script MathJax dans les partiels de votre thème (par exemple, `layouts/partials/head.html`) :
        ```html
        {{ if .Params.mathjax }}
        <script type="text/x-mathjax-config">
          MathJax.Hub.Config({
            tex2jax: {
              inlineMath: [['$','$']],
              displayMath: [['$$','$$'], ['\[','\]']],
              processEscapes: true
            },
            "HTML-CSS": { linebreaks: { automatic: true } },
            "CommonHTML": { linebreaks: { automatic: true } },
            TeX: { equationNumbers: { autoNumber: "AMS" } }
          });
        </script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
        {{ end }}
        ```
    -   Activez MathJax dans des pages spécifiques en ajoutant au front matter :
        ```yaml
        ---
        title: Mon Article de Maths
        mathjax: true
        ---
        ```

2.  **Utiliser des Shortcodes pour les mathématiques** :
    Créez un shortcode (par exemple, `layouts/shortcodes/math.html`) pour encapsuler explicitement le contenu mathématique :
    ```html
    {{ if .IsNamedParams }}
      <span class="math">{{ .Get "content" | safeHTML }}</span>
    {{ else }}
      <span class="math">{{ .Inner | safeHTML }}</span>
    {{ end }}
    ```
    Utilisez-le dans votre Markdown :
    ```markdown
    Texte normal (non analysé). Formule : {{< math >}}$x^2 + y^2${{< /math >}}.
    ```
    -   **Pourquoi cela fonctionne** : Les shortcodes garantissent que seul le contenu explicitement marqué est traité comme des mathématiques, laissant les `( )` dans le texte normal intacts.

3.  **Utiliser KaTeX à la place** :
    Les utilisateurs de Hugo préfèrent souvent KaTeX pour sa rapidité. Ajoutez KaTeX à `layouts/partials/head.html` :
    ```html
    {{ if .Params.math }}
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/auto-render.min.js"></script>
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
          delimiters: [
            { left: "$$", right: "$$", display: true },
            { left: "$", right: "$", display: false }
          ]
        });
      });
    </script>
    {{ end }}
    ```
    Activez-le dans le front matter :
    ```yaml
    math: true
    ```
    Utilisez `$ $` pour les mathématiques en ligne pour éviter les conflits avec `( )`.

---

### **Recommandation**
-   **Pour Jekyll** : Passez aux délimiteurs `$ $` pour MathJax ou utilisez KaTeX pour éviter les problèmes d'analyse des `( )`. L'échappement des parenthèses est une solution de repli mais moins pratique pour les grands sites.
-   **Pour Hugo** : Il est peu probable que vous rencontriez ce problème à moins que vous ne configuriez explicitement MathJax avec les délimiteurs `\( )`. Utilisez des shortcodes ou KaTeX pour le rendu mathématique afin de garantir la sécurité des parenthèses normales.

Si vous migrez de Jekyll vers Hugo et souhaitez conserver votre contenu mathématique, je recommande d'utiliser KaTeX dans Hugo avec des shortcodes pour un contrôle explicite. Faites-moi savoir si vous avez besoin d'aide pour configurer l'intégration MathJax/KaTeX de Hugo ou pour convertir le contenu mathématique de votre site Jekyll !