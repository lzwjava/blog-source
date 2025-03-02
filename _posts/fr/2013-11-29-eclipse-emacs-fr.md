---
audio: false
generated: false
lang: fr
layout: post
title: Transformer Eclipse en Emacs
translated: true
---

En tant qu'utilisateur d'Emacs depuis six mois, je ne peux tout simplement pas imaginer comment j'ai pu coder auparavant, en éloignant mes mains de la position standard pour cliquer avec la souris ou appuyer sur les touches fléchées sans trouver cela inconfortable et insupportable. Maintenant, lorsque je dis à mes amis que j'ai configuré les raccourcis Alt+P et Alt+N pour passer rapidement entre les fichiers XML et la mise en page graphique, leur réponse est simplement "d'accord", sous-entendant que l'utilisation de la souris pour passer est aussi bien.
Pour moi, c'est un cauchemar ; ce n'est tout simplement pas assez rapide ! Si vous êtes un utilisateur d'Emacs, vous comprenez...

Cet article décrit des techniques simples pour créer un environnement d'édition "Eclipse" rapide. En gros, vos mains peuvent rester dans la position standard, vous permettant de coder avec une efficacité maximale !

La chose la plus importante est d'installer le plugin Emacs+. Consultez "Emacs+ : Emacs Experience in Eclipse".

Pour bien utiliser l'assistant de code, vous devez l'activer pour qu'il soit déclenché par n'importe quel caractère et empêcher la complétion automatique lorsque vous appuyez sur la barre d'espace ou =. Je recommande de télécharger ce fichier jar depuis CSDN. Avec cela, et une rapide recherche sur Google, vous pouvez importer des packages en un rien de temps.

Ensuite, personnalisons quelques raccourcis :

1) Assignez Alt+P à "Previous Sub-Tab" et Alt+N à "Next Sub-Tab."

Le sous-onglet est la barre d'onglets en dessous d'un éditeur, comme les onglets "Graphical Layout" et "XML" lors de l'édition d'un fichier XML. Cela vous permet de voir instantanément la mise en page.

2) Assignez Ctrl+C, Ctrl+C à "Run."

Cela est copié de la configuration de sbcl. La valeur par défaut est Ctrl+F11, qui est trop loin pour un raccourci aussi fréquemment utilisé, ce qui rend les utilisateurs d'Emacs malheureux ! J'ai stupidement appuyé sur Ctrl+F11 pendant quelques jours avant de le changer.

3) Assignez Ctrl+X, Ctrl+O à "Next View." When In Windows and In Editing Text.

Cela vous permet de passer instantanément de l'éditeur à la console lors de la rédaction de code Java.

4) Assignez Ctrl+X, O à "Next Editor." When In Windows and In Editing Text.

Cela vous permet de passer rapidement entre les fichiers Java.

5) Assignez Ctrl+Q à "Quick Fix."

Ainsi, lorsque vous tapez `@string/xx`, avec le curseur sur `xx`, appuyez sur Ctrl+Q puis sur Entrée pour passer instantanément à `string.xml`, avec le curseur positionné au niveau du `TODO` dans `<string name="xx">TODO</string>`.

6) Assignez Ctrl+Shift+W à "Close" (lorsque dans les fenêtres) et supprimez l'assignation originale (fermer tout).
Le raccourci de fermeture d'origine est Ctrl+W, ce qui correspond à nos habitudes dans les navigateurs, les boîtes de discussion et les explorateurs de fichiers. Cependant, cela entre en conflit avec la commande de coupe d'Emacs. En réalité, appuyer sur Ctrl+Shift+W pendant une seconde peut fermer de nombreux fichiers. Donc, changer Ctrl+Shift+W de "fermer tout" à "fermer" ne fait perdre rien.

Il y a un problème : après avoir installé Emacs+, lors de l'édition de code et de l'apparition de l'assistant de code, l'appui sur les touches fléchées haut et bas ne sélectionne pas les éléments dans la liste des candidats de l'assistant de code ; au lieu de cela, cela déplace le code en cours d'édition vers le haut et vers le bas. La valeur par défaut est de l'activer avec F2. L'activation de l'assistant de code met le focus sur l'assistant de code, mais ensuite, vous ne pouvez utiliser les touches fléchées haut et bas que pour sélectionner. Ce serait formidable si nous pouvions utiliser Ctrl+P et Ctrl+N ! L'édition de code serait incroyablement rapide ! Mais le problème est que, après avoir installé le plugin Emacs+, bien qu'Eclipse ressemble plus à Emacs, cette fonctionnalité est perdue. Dans un Eclipse propre, avec le clavier Emacs (et non Emacs+Scheme) sélectionné, vous pouvez utiliser Ctrl+N et Ctrl+P pour sélectionner les éléments de complétion lorsque l'assistant de code apparaît. Quelqu'un a demandé cela sur Stack Overflow, mais il n'y a pas encore de réponse.

Si nous pouvions utiliser Ctrl+P et Ctrl+N pour sélectionner les éléments de complétion, ce serait vraiment génial !