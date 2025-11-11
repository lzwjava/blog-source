---
audio: false
generated: true
lang: fr
layout: post
title: Dépannage des Problèmes MathJax
translated: true
type: note
---

Il semble que votre configuration MathJax ne fonctionne pas comme prévu. Identifions et résolvons le problème en nous basant sur le code que vous avez fourni.

### Votre Configuration Actuelle
Vous avez la configuration MathJax suivante :

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ["\\(","\\)"] ],
      displayMath: [ ['$$','$$'], ["\[","\]"] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

Cette configuration vise à :
- Rendre les mathématiques en ligne entre les délimiteurs `\( ... \)`.
- Rendre les mathématiques affichées entre les délimiteurs `$$ ... $$` ou `\[ ... \]`.
- Activer le retour à la ligne automatique pour les équations longues.
- Redimensionner la sortie mathématique à 85% de la taille en utilisant le processeur de sortie CommonHTML.
- Numéroter automatiquement les équations en utilisant le style AMS.

Cependant, vous avez signalé que cela "ne fonctionne pas", ce qui pourrait signifier que les mathématiques ne s'affichent pas, ou que des fonctionnalités spécifiques (comme le retour à la ligne) ne fonctionnent pas comme prévu.

### Le Problème
Le problème principal réside dans la configuration des délimiteurs `displayMath` :

```javascript
displayMath: [ ['$$','$$'], ["\[","\]"] ]
```

En JavaScript, la chaîne `"["` est interprétée littéralement comme `[`, car `\[` n'est pas une séquence d'échappement spéciale—c'est simplement un backslash suivi d'un crochet. De même, `"\]"` devient `]`. En conséquence, MathJax est configuré pour reconnaître `[ ... ]` comme délimiteurs de mathématiques affichées, **et non** `\[ ... \]`. Étant donné que vos expressions mathématiques (comme l'exemple `\[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]`) utilisent `\[ ... \]`, MathJax ne les reconnaîtra pas comme des mathématiques affichées avec la configuration actuelle.

Les délimiteurs de mathématiques en ligne `["\\(","\\)"]` sont corrects, car `\\(` et `\\)` dans une chaîne JavaScript représentent `\(` et `\)`—les délimiteurs LaTeX standard pour les mathématiques en ligne. Cependant, les délimiteurs de mathématiques affichées doivent être ajustés.

### La Solution
Pour corriger cela, mettez à jour la configuration `displayMath` afin que MathJax reconnaisse correctement `\[ ... \]` comme délimiteurs de mathématiques affichées. En JavaScript, pour représenter la chaîne `\[`, vous devez écrire `"\\["`, car chaque backslash doit être échappé. De même, `\]` devient `"\\]"`. Voici la configuration corrigée :

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ["\\(","\\)"] ],
      displayMath: [ ["$$","$$"], ["\\[","\\]"] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

#### Changement Clé
- Changé `["\[","\]"]` en `["\\[","\\]"]` dans le tableau `displayMath`.
- Cela garantit que les délimiteurs sont définis sur `\[ ... \]` (et `$$ ... $$`), correspondant à la notation LaTeX standard.

### Considérations Supplémentaires
1. **Problèmes de Retour à la Ligne** : Vous avez mentionné que certaines expressions sont trop longues et débordent, surtout sur les vues mobiles. Le paramètre `linebreaks: { automatic: true }` dans le processeur de sortie "CommonHTML" devrait gérer cela, mais il nécessite que les mathématiques soient à l'intérieur d'un conteneur avec une largeur définie (par exemple, `width: 100%`). Assurez-vous que votre structure HTML inclut quelque chose comme :

   ```html
   <div style="width: 100%; overflow-x: auto;">
     \[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]
   </div>
   ```

   Cela permet à MathJax de couper les lignes en fonction de la largeur du conteneur, en s'adaptant à la taille de l'écran.

2. **Processeur de Sortie** : Votre script charge `TeX-MML-AM_CHTML`, qui utilise CommonHTML par défaut. Les paramètres `"CommonHTML"` (par exemple, `scale: 85`, `linebreaks: { automatic: true }`) s'appliqueront, mais les paramètres `"HTML-CSS"` peuvent ne pas s'appliquer, car ce processeur de sortie n'est pas actif. Étant donné que CommonHTML est moderne et largement pris en charge, c'est bien—assurez-vous simplement que vos paramètres sont alignés avec lui.

3. **Test** : Après avoir mis à jour la configuration, testez avec votre expression exemple :

   ```html
   \[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]
   ```

   Elle devrait maintenant s'afficher correctement comme mathématiques affichées avec un retour à la ligne approprié si nécessaire.

4. **Compatibilité du Navigateur** : MathJax 2.7.7 devrait fonctionner dans la plupart des navigateurs modernes. Si des problèmes persistent, assurez-vous qu'il n'y a pas d'erreurs JavaScript dans la console ou de règles CSS conflictives (par exemple, `white-space: nowrap`) qui écrasent le rendu mathématique.

### Code Corrigé Final
Voici la configuration complète et corrigée :

```html
<!-- Configuration MathJax -->
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ["\\(","\\)"] ],
      displayMath: [ ["$$","$$"], ["\\[","\\]"] ],
      processEscapes: true
    },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<!-- Chargement de MathJax -->
<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

<!-- Exemple de Math -->
<div style="width: 100%; overflow-x: auto;">
  \[ \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bits per second (bps)} \]
</div>
```

### Pourquoi Cela Fonctionne
- **Correction des Délimiteurs** : `["\\[","\\]"]` garantit que MathJax reconnaît `\[ ... \]` comme des mathématiques affichées, correspondant à votre contenu.
- **Retour à la Ligne** : Les paramètres `CommonHTML` avec un conteneur approprié activent les retours à la ligne automatiques pour les expressions longues.
- **Rendu** : Le script CDN et la configuration ensemble assurent que les mathématiques sont traitées et affichées correctement.

Mettez à jour votre code avec cette correction, et votre configuration MathJax devrait fonctionner comme prévu ! Si des problèmes persistent, veuillez partager des exemples spécifiques d'expressions mathématiques qui échouent ou tout message d'erreur que vous rencontrez.

---

Pour configurer MathJax afin qu'il rende correctement les expressions mathématiques dans le contenu fourni, vous devez vous assurer qu'il gère correctement les expressions mathématiques en ligne comme \( T_p \) et \( 2 \times T_p \), qui sont encadrées par des délimiteurs de style LaTeX. Le contenu utilise `\( ... \)` pour les mathématiques en ligne, et bien qu'il n'inclue pas de mathématiques affichées (par exemple, des équations sur des lignes séparées), il est bon de configurer MathJax pour les deux types de mathématiques pour plus de flexibilité. Voici un guide étape par étape pour y parvenir.

### Étape 1 : Inclure MathJax dans votre HTML
Vous devez d'abord charger la bibliothèque MathJax. Vous pouvez utiliser un Content Delivery Network (CDN) pour l'inclure dans votre fichier HTML. Ajoutez la balise script suivante dans le `<head>` de votre HTML ou avant le contenu qui contient des mathématiques :

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS_CHTML"></script>
```

Cela charge MathJax version 2.7.9 avec la configuration `TeX-AMS_CHTML`, qui prend en charge la saisie LaTeX et rend les mathématiques en HTML avec CSS, adapté à la plupart des applications web.

### Étape 2 : Configurer les Délimiteurs MathJax
MathJax doit savoir quels délimiteurs reconnaître pour les expressions mathématiques. Le contenu utilise `\( ... \)` pour les mathématiques en ligne, ce qui est un délimiteur LaTeX standard. Pour s'assurer que MathJax les traite correctement, ajoutez un script de configuration avant le script de la bibliothèque MathJax. Voici une configuration de base :

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(', '\\)'] ],
      displayMath: [ ['$$', '$$'], ['\\[', '\\]'] ],
      processEscapes: true
    }
  });
</script>
```

- **`inlineMath`** : Indique à MathJax de traiter le texte entre `\( ... \)` comme des mathématiques en ligne. Les doubles crochets `[ ['\\(', '\\)'] ]` sont utilisés car MathJax accepte un tableau de paires de délimiteurs.
- **`displayMath`** : Configure MathJax pour reconnaître `$$ ... $$` et `\[ ... \]` comme des mathématiques affichées, même si le contenu actuel ne les utilise pas. Cela assure la compatibilité avec le contenu futur.
- **`processEscapes`** : Permet d'échapper les délimiteurs (par exemple, utiliser `\$` pour afficher un signe dollar littéral), bien que ce ne soit pas critique pour ce contenu spécifique.

### Étape 3 : Améliorer le Rendu pour la Réactivité
Pour rendre les mathématiques affichées adaptables à différentes tailles d'écran (par exemple, éviter le débordement sur les appareils mobiles), activez le retour à la ligne automatique pour les expressions longues. Mettez à jour la configuration comme ceci :

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(', '\\)'] ],
      displayMath: [ ['$$', '$$'], ['\\[', '\\]'] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    CommonHTML: { linebreaks: { automatic: true } },
    SVG: { linebreaks: { automatic: true } }
  });
</script>
```

- **`HTML-CSS`, `CommonHTML`, `SVG`** : Ce sont les processeurs de sortie que MathJax utilise pour rendre les mathématiques. Activer `linebreaks: { automatic: true }` garantit que les expressions longues se replient naturellement, bien que les expressions de ce contenu (\( T_p \), \( 2 \times T_p \)) soient courtes et n'aient probablement pas besoin de repli.

### Étape 4 : Tout Combiner
Voici la configuration complète à inclure dans votre fichier HTML avant le contenu :

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(', '\\)'] ],
      displayMath: [ ['$$', '$$'], ['\\[', '\\]'] ],
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    CommonHTML: { linebreaks: { automatic: true } },
    SVG: { linebreaks: { automatic: true } }
  });
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS_CHTML"></script>
```

### Étape 5 : Vérifier que le Contenu s'Affiche Correctement
Avec cette configuration, les mathématiques en ligne dans votre contenu—telles que \( T_p \) et \( 2 \times T_p \)—devraient s'afficher comme des expressions mathématiques correctement formatées. Par exemple :
- \( T_p \) devient une variable en indice.
- \( 2 \times T_p \) s'affiche avec un symbole de multiplication (×) et le \( T_p \) en indice.

### Notes Supplémentaires
- **Pas de Mathématiques Affichées** : Étant donné que votre contenu n'utilise que des mathématiques en ligne, les paramètres `displayMath` ne sont pas strictement nécessaires mais sont inclus pour être exhaustifs.
- **Style CSS** : Assurez-vous que le conteneur HTML pour votre contenu (par exemple, un `<div>`) a `width: 100%` ou un style approprié pour garder la mise en page réactive.
- **Test** : Après avoir ajouté cette configuration, chargez votre page dans un navigateur pour confirmer que \( T_p \) et \( 2 \times T_p \) s'affichent comme prévu.

Cette configuration garantit que MathJax rend les expressions mathématiques dans votre explication CSMA/CD de manière claire et professionnelle, améliorant la lisibilité pour les utilisateurs.

---

Pour corriger les problèmes de rendu MathJax avec les parenthèses `\(...\)` et autres délimiteurs LaTeX, ajustez votre configuration pour échapper correctement les backslashes dans les chaînes JavaScript. Voici la configuration corrigée :

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(','\\)'] ],  // Correctement échappé pour JavaScript
      displayMath: [ ['$$','$$'], ['\\[','\\]'] ],  // Échappement corrigé pour \[ et \]
      processEscapes: true
    },
    "HTML-CSS": { linebreaks: { automatic: true } },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

### Corrections Clés :
1. **Backslashes Échappés** :
   - Changé `["\\(","\\)"]` en `['\\(','\\)']` (les guillemets simples évitent un échappement supplémentaire).
   - Corrigé `["\[","\]"]` en `['\\[','\\]']` pour garantir que `\[...\]` fonctionne pour les équations affichées.

2. **Recommandations** :
   - Utilisez `'$$...$$'` ou `\\[...\\]` pour les équations affichées.
   - Utilisez `\\(...\\)` pour les équations en ligne.
   - Assurez-vous qu'il n'y a pas de processeurs Markdown conflictuels modifiant votre LaTeX.

### Exemple d'Utilisation :
```html
<p>Math en ligne : \( E = mc^2 \).</p>

<p>Math affichée :</p>
\[
  \int_{-\infty}^\infty e^{-x^2} dx = \sqrt{\pi}
\]
```

Cette configuration garantit que MathJax analyse correctement tous les délimiteurs LaTeX.

---

Je comprends que vous utilisez Jekyll avec Kramdown pour rendre les posts Markdown et que vous souhaitez configurer MathJax pour afficher correctement les expressions mathématiques. Vous avez fourni une configuration MathJax et noté que vous rendez les mathématiques dans les posts Markdown, pas dans les balises HTML. Assurons-nous que MathJax fonctionne parfaitement avec votre configuration.

### Votre Configuration Actuelle
Vous utilisez :
- **Jekyll avec Kramdown** : Kramdown est l'analyseur Markdown par défaut pour Jekyll et prend en charge les expressions mathématiques de style LaTeX.
- **MathJax** : Votre configuration spécifie les délimiteurs pour les mathématiques en ligne et affichées :
  - En ligne : `\( ... \)`
  - Affichée : `$$ ... $$` et `\[ ... \]`

Vous avez également inclus un script `marked.min.js`, bien qu'il ne soit probablement pas pertinent car Jekyll rend le Markdown côté serveur avec Kramdown, pas côté client.

### Pourquoi le Rendu Peut Ne Pas Fonctionner
Kramdown et MathJax doivent s'aligner sur la façon dont les délimiteurs mathématiques sont gérés. Votre configuration MathJax reconnaît `\( ... \)` pour les mathématiques en ligne et à la fois `$$ ... $$` et `\[ ... \]` pour les mathématiques affichées. Cependant, le comportement par défaut de Kramdown pourrait ne pas passer tous ces délimiteurs à MathJax correctement à moins d'être configuré correctement, surtout si des problèmes d'échappement surviennent dans Markdown.

### Solution : Configurer MathJax avec Kramdown
Voici comment le faire fonctionner :

#### 1. Configurer Kramdown dans Jekyll
Assurez-vous que votre fichier Jekyll `_config.yml` active MathJax comme moteur mathématique pour Kramdown. Ajoutez ou vérifiez ce qui suit :

```yaml
markdown: kramdown
kramdown:
  math_engine: mathjax
```

Cela indique à Kramdown de traiter les expressions mathématiques et de les passer à MathJax. Par défaut, Kramdown reconnaît :
- `\( ... \)` pour les mathématiques en ligne.
- `$$ ... $$` pour les mathématiques affichées.

Bien que votre configuration MathJax prenne également en charge `\[ ... \]` pour les mathématiques affichées, Kramdown n'utilise pas nativement ce délimiteur, ce qui pourrait causer des problèmes à moins d'être géré correctement.

#### 2. Utiliser des Délimiteurs Mathématiques Cohérents dans Markdown
Pour éviter la confusion ou les problèmes d'échappement, respectez les délimiteurs par défaut de Kramdown dans vos posts Markdown :
- **Mathématiques en Ligne** : Utilisez `\( ... \)`.
  Exemple : `Ceci est en ligne : \( E = mc^2 \)` s'affiche comme "Ceci est en ligne : \( E = mc^2 \)".
- **Mathématiques Affichées** : Utilisez `$$ ... $$`.
  Exemple :
  ```markdown
  $$
  \int_0^1 x^2 \, dx = \frac{1}{3}
  $$
  ```
  Cela s'affiche comme une équation centrée : \( \int_0^1 x^2 \, dx = \frac{1}{3} \).

Si vous préférez `\[ ... \]`, vous pouvez l'utiliser, mais l'échappement par backslash de Markdown peut nécessiter une attention particulière (par exemple, `\\[ ... \\]`). Cependant, `$$ ... $$` est plus simple et correspond aux valeurs par défaut de Kramdown, réduisant les erreurs potentielles.

#### 3. Simplifier Votre Configuration MathJax
Étant donné que Kramdown prétraite les mathématiques, votre configuration MathJax peut se concentrer sur le rendu. Voici une version rationalisée basée sur votre configuration :

```html
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['\\(','\\)'] ],
      displayMath: [ ['$$','$$'] ], // S'en tenir à $$ pour la simplicité
      processEscapes: true
    },
    "CommonHTML": {
      linebreaks: { automatic: true },
      scale: 85
    },
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>

<script type="text/javascript" async
  src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

- J'ai supprimé `['\\[','\\]']` de `displayMath` pour correspondre à la préférence de Kramdown pour `$$ ... $$`. Si vous voulez toujours `\[ ... \]`, gardez-le, mais testez soigneusement.
- Supprimé `"HTML-CSS"` car `"CommonHTML"` est suffisant pour le rendu MathJax moderne.

Placez cela dans la section `<head>` de votre mise en page Jekyll.

#### 4. Supprimer les Scripts Inutiles
Vous avez inclus `<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>`, mais Jekyll utilise Kramdown côté serveur, donc Marked.js (un analyseur côté client) n'est pas nécessaire sauf si vous faites quelque chose de spécifique avec lui. Si ce n'est pas le cas, supprimez-le pour éviter les conflits ou la confusion potentiels.

#### 5. Tester Votre Configuration
Ajoutez ces exemples à un post Markdown pour confirmer que le rendu fonctionne :
- En ligne : `L'énergie est \( E = mc^2 \).`
- Affichée :
  ```markdown
  $$
  \text{Bit rate} = 2400 \, \text{baud} \times 3 \, \text{bits/symbol} = 7200 \, \text{bps}
  $$
  ```

Exécutez `jekyll serve`, ouvrez le site dans votre navigateur et vérifiez que les mathématiques s'affichent correctement. Sinon, inspectez la console du navigateur pour les erreurs MathJax.

### Notes Finales
- **Cohérence** : Utiliser `\( ... \)` et `$$ ... $$` assure la compatibilité entre Kramdown et MathJax sans tracas d'échappement supplémentaires.
- **Dépannage** : Si les mathématiques ne s'affichent toujours pas, vérifiez :
  - Les scripts MathJax se chargent sans erreurs (vérifiez la console du navigateur).
  - Votre build Jekyll se termine avec succès.
  - Il n'y a pas de fautes de frappe dans les délimiteurs ou la configuration.

Cette configuration devrait rendre vos expressions mathématiques magnifiquement dans les posts Markdown Jekyll ! Faites-moi savoir si vous rencontrez des problèmes spécifiques avec les exemples que vous essayez de rendre.