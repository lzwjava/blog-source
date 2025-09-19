---
audio: false
generated: false
image: true
lang: fr
layout: post
title: Utilisation avancée de Markdown
translated: true
---

## Références

Référence [^1].

Dans les notes de bas de page, n'oubliez pas d'ajouter un `:` après le `[numéro]` pour un bon parsing.

---

## Classe d'Image

Vous pouvez appliquer des classes aux images en Markdown comme ceci :

```markdown
{: .centered }
![](assets/images/pin/pin.jpg){: .responsive }
*Source : Telegram*{: .caption }
```

Cela affichera l'image avec les classes spécifiées :

{: .centered }  
![](assets/images/pin/pin.jpg){: .responsive }  
*Source : Telegram*{: .caption }

## Table des matières

- [Introduction](#introduction)
- [Chapitre 1](#chapter-1)
- [Conclusion](#conclusion)

---

### Introduction

Voici l'introduction.

---

### Chapitre 1

Voici le Chapitre 1.

---

### Conclusion

Voici la conclusion.

## Mermaid

```mermaid
graph TD
    A[Chargeur Box] --> B[Power Bank]
    A --> C[Enceinte Bluetooth]
    A --> D[Téléphone Portable]
    A --> E[Lampe Électrique]
    A --> F[Ordinateur Portable]
    A --> G[Montre Connectée]
    A --> H[Cloud Server]
    B --> H
    C --> H
    D --> H
    E --> H
    F --> H
    G --> H
```

Ce n'est toujours pas rendu ici, mais cela fonctionne bien et peut être généré dans Mistral. Trouvons un moment pour en apprendre davantage.

---

[^1]: En voici un.
`