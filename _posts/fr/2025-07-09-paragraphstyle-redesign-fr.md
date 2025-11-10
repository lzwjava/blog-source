---
audio: false
generated: true
lang: fr
layout: post
title: Redéfinir le style de paragraphe pour le poids moyen
translated: true
type: note
---

Pour modifier l'environnement `cvparagraph` entier afin qu'il utilise `\mdseries` au lieu de `\bodyfontlight`, vous devez redéfinir la commande `\paragraphstyle`. Ajoutez ceci dans votre préambule après avoir chargé la classe awesome-cv :

```latex
\renewcommand*{\paragraphstyle}{\fontsize{11pt}{1em}\mdseries\upshape\color{text}}
```

Cela changera le style de paragraphe de :
- `\bodyfontlight` (qui est une graisse légère)

vers :
- `\mdseries` (qui est une graisse moyenne, similaire au style de description)

De cette façon, votre environnement `cvparagraph` entier utilisera la série de police de graisse moyenne comme le fait `\descriptionstyle`.