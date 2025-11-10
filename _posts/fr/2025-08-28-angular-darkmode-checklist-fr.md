---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Liste de vérification de l'élément mode sombre Angular
translated: true
type: note
---

Lorsque vous implémentez un mode sombre dans une application Angular, vous commencez généralement par `body`, `select` et `option`, mais il existe pas mal d'autres éléments HTML courants que vous voudrez restyler pour que le thème soit cohérent. Voici une liste pratique :

### Niveau Page et Conteneurs

* `html`, `body` → couleur d'arrière-plan et de texte.
* `div`, `section`, `article`, `aside`, `header`, `footer`, `main`, `nav` → définir les couleurs d'arrière-plan et de texte (surtout s'ils ont un arrière-plan blanc par défaut).

### Texte et Titres

* `h1, h2, h3, h4, h5, h6` → assurez-vous que le texte est visible sur un fond sombre.
* `p`, `span`, `a` → ajustez la couleur du texte, les couleurs au survol des liens et les états des liens visités.

### Formulaires et Champs

* `input[type="text"], input[type="password"], input[type="email"], textarea` → arrière-plan, couleur du texte et bordure.
* `input[type="checkbox"], input[type="radio"]` → nécessitent parfois un traitement spécial pour la visibilité.
* `select, option` → comme vous l'avez mentionné, à la fois l'arrière-plan et la couleur du texte.
* `button` → arrière-plan, bordure et couleur du texte, ainsi que les états hover/active.
* `label` → assurez-vous que le texte contraste avec l'arrière-plan sombre.
* `fieldset, legend` → arrière-plan et bordure.

### Listes et Tableaux

* `ul, ol, li` → couleur du texte.
* `table` → arrière-plan, couleur des bordures et couleur du texte.
* `thead, tbody, tr, th, td` → ajustements individuels pour les arrière-plans et les bordures.

### Éléments Interactifs

* `details, summary` → arrière-plan et texte.
* `dialog` → arrière-plan et texte.
* `mark` → les couleurs de surlignage doivent fonctionner sur fond sombre (le jaune par défaut peut être trop vif).

### Média et Divers

* `hr` → couleur de la bordure (elle est souvent trop claire sur fond sombre par défaut).
* `code, pre` → arrière-plan et couleur du texte pour la lisibilité.
* `blockquote` → couleur d'arrière-plan et de bordure.
* `progress, meter` → couleurs de la piste et de la valeur.

---

💡 **Bonnes pratiques** : Au lieu d'utiliser `!important` partout, définissez des variables CSS pour les couleurs (`--bg-color`, `--text-color`, etc.) et échangez-les lorsque le mode sombre est actif (par exemple, ajoutez une classe `.dark-mode` au `body`). De cette façon, les composants Angular et les éléments personnalisés peuvent également s'intégrer proprement au thème.

Souhaitez-vous que je rédige un **snippet CSS de base** pour le mode sombre (avec des variables) que vous pouvez intégrer à votre projet Angular comme point de départ ?