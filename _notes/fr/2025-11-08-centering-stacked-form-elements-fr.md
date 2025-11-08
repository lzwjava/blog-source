---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Centrer des éléments de formulaire empilés avec Flexbox
translated: true
type: note
---

```css
.sort-container {
    display: flex;
    flex-direction: column; /* Ajoute ceci pour empiler les éléments verticalement */
    align-items: center; /* Centre les éléments horizontalement dans la colonne */
    justify-content: center; /* Centre la colonne verticalement */
    gap: 10px;
    margin-bottom: 1rem;
}

.sort-container select {
    padding: 5px;
    font-size: 16px;
}

.sort-container .post-number {
    font-size: 16px;
}
```

### Explication
- **flex-direction: column** : Change l'axe principal de horizontal (row) à vertical, empilant les éléments `select` et `.post-number` de haut en bas.
- **align-items: center** : Maintient le centrage horizontal des éléments enfants.
- **justify-content: center** : Centre l'ensemble de l'empilement vertical dans le conteneur.
- J'ai également corrigé la syntaxe des sélecteurs imbriqués (j'ai déplacé `select` et `.post-number` en dehors du bloc principal pour une meilleure pratique, en supposant qu'ils sont des enfants directs—ajuster si nécessaire). Le `gap` s'applique maintenant verticalement entre les éléments.