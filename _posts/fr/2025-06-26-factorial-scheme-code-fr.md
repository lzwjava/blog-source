---
audio: false
generated: true
lang: fr
layout: post
title: Programme Factoriel en Chez Scheme
translated: true
type: note
---

Voici un programme simple en Chez Scheme qui calcule la factorielle d'un nombre. Enregistrez-le sous le nom `factorial.scm` :

```scheme
(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

(display "Factorielle de 5 est : ")
(display (factorial 5))
(newline)
```

Pour l'exécuter :
1.  Enregistrez le code dans un fichier nommé `factorial.scm`.
2.  Dans votre terminal, naviguez jusqu'au répertoire contenant le fichier.
3.  Exécutez : `scheme --script factorial.scm`

Cela affichera :
```
Factorielle de 5 est : 120
```

Le programme définit une fonction récursive `factorial` et calcule la factorielle de 5. L'option `--script` (comme indiqué dans la sortie de `scheme --help`) vous permet d'exécuter le fichier directement.