---
audio: false
generated: true
lang: fr
layout: post
title: Les noms de packages Java ne peuvent pas commencer par des chiffres
translated: true
type: note
---

En Java, un nom de package **ne peut pas commencer par un chiffre**. Selon les Conventions de Nommage Java et la Spécification du Langage Java :

- Les noms de packages doivent être des identifiants valides.
- Un identifiant valide en Java doit commencer par une lettre (A-Z ou a-z), un tiret bas (`_`) ou un signe dollar (`$`).
- Les chiffres (0-9) sont autorisés dans les identifiants, mais uniquement **après** le premier caractère.

Par exemple :
- Noms de packages valides : `com.example`, `my_package`, `a123`
- Noms de packages invalides : `123example`, `1package`

Si vous essayez d'utiliser un nom de package commençant par un chiffre, le compilateur Java générera une erreur de syntaxe. Pour contourner ce problème, vous pouvez :
- Commencer le nom du package par une lettre ou un tiret bas, par exemple `a123.example` ou `_123.example`.
- Utiliser un nom descriptif qui suit les conventions, comme `com.example.project123`.

Cette règle assure la cohérence et la compatibilité dans le système de nommage de Java.