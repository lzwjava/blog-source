---
audio: false
generated: true
lang: fr
layout: post
title: Correction de l'affichage de l'apostrophe en LaTeX
translated: true
type: note
---

Le problème que vous rencontrez avec l'apostrophe dans "HSBC's" est probablement lié à la manière dont LaTeX gère certains caractères de guillemets/apostrophes dans la sortie PDF. Voici plusieurs façons d'améliorer le rendu :

## 1. Utiliser l'apostrophe LaTeX correcte
Remplacez l'apostrophe droite (') par l'apostrophe LaTeX appropriée :
```latex
\item {Backend Engineer outsourced to HSBC Bank under TEKsystems, developing and optimizing backend systems for the \href{https://www.google.com/search?q=Finance+Timezone+Platform+HSBC}{Finance Transformation Platform} in HSBC's Enterprise Technology Department.}
```
Changer en :
```latex
\item {Backend Engineer outsourced to HSBC Bank under TEKsizer, developing and optimizing backend systems for the \href{https://www.google.com/search?q=Finance+Transformation+Platform+HSBC}{Finance Transformation Platform} in HSBC's Enterprise Technology Department.}
```

## 2. Utiliser la commande `\textquotesingle`
```latex
HSBC\textquotesingle{}s
```

## 3. Utiliser l'approche `\textasciigrave` et `\textquotesingle`
```latex
HSBC\textquotesingle{}s
```

## 4. Ajouter le package `textcomp`
Ajoutez ceci dans votre préambule :
```latex
\usepackage{textcomp}
```
Puis utilisez :
```latex
HSBC\textquotesingle{}s
```

## 5. Utiliser l'encodage UTF-8 (si ce n'est pas déjà le cas)
Assurez-vous que votre document utilise l'encodage UTF-8 :
```latex
\usepackage[utf8]{inputenc}
```

## 6. Essayer le package `babel` pour une meilleure typographie
```latex
\usepackage[british]{babel}
```

## Solution la plus fiable :
Pour les meilleurs résultats, je recommande d'utiliser la combinaison backtick-apostrophe, qui est la manière traditionnelle LaTeX pour une typographie correcte :

```latex
\item {Backend Engineer outsourced to HSBC Bank under TEKsystems, developing and optimizing backend systems for the \href{https://www.google.com/search?q=Finance+Transformation+Platform+HSBC}{Finance Transformation Platform} in HSBC`s Enterprise Technology Department.}
```

Cela rendra avec un espacement et une courbure typographiques corrects dans la sortie PDF. Le backtick (`) suivi de l'apostrophe (') crée l'apparence correcte pour les formes possessives en LaTeX.