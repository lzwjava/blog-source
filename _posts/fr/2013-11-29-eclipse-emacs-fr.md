---
audio: false
lang: fr
layout: post
title: Transformer Eclipse en Emacs
translated: true
---

En tant qu'utilisateur d'Emacs depuis six mois, je ne peux tout simplement pas imaginer comment je pouvais coder auparavant, en éloignant mes mains de la position standard pour cliquer avec la souris ou presser les touches fléchées sans trouver cela fastidieux et insupportable. Maintenant, quand je dis à mes amis que j'ai configuré les raccourcis Alt+P et Alt+N pour passer rapidement entre les fichiers XML et la mise en page graphique, leur réponse est juste "d'accord", sous-entendant que l'utilisation de la souris pour passer est aussi acceptable.

Pour moi, c'est un cauchemar ; ce n'est tout simplement pas assez rapide ! Si vous êtes un utilisateur d'Emacs, vous comprenez...

Cet article décrit des techniques simples pour créer un environnement d'édition rapide dans Eclipse. En gros, vos mains peuvent rester dans la position standard, vous permettant de coder avec une efficacité maximale !

La chose la plus importante est d'installer le plugin Emacs+. Voir "Emacs+: Emacs Experience in Eclipse".

Pour bien utiliser l'assistant de code, vous devez l'activer pour qu'il se déclenche avec n'importe quel caractère et empêcher la complétion automatique lorsqu'on appuie sur la barre d'espace ou =. Je recommande de télécharger ce fichier jar depuis CSDN. Avec celui-ci et une rapide recherche sur Google, vous pouvez importer des packages en un rien de temps.

Ensuite, personnalisons quelques raccourcis :

1) Associez Alt+P à "Previous Sub-Tab" et Alt+N à "Next Sub-Tab."

Le sous-onglet est la barre d'onglets en dessous d'un éditeur, comme les onglets "Graphical Layout" et "XML" lors de l'édition d'un fichier XML. Cela vous permet de voir instantanément la mise en page.

2) Associez Ctrl+C, Ctrl+C à "Run."

Cela est copié depuis la configuration de sbcl. La valeur par défaut est Ctrl+F11, qui est trop éloignée pour un raccourci aussi fréquemment utilisé, ce qui donne l'impression qu'il manque quelque chose aux utilisateurs d'Emacs ! J'ai stupidement appuyé sur Ctrl+F11 pendant quelques jours avant de changer.

3) Associez Ctrl+X, Ctrl+O à "Next View." Lorsque dans Windows et en éditant du texte.

Cela vous permet de passer instantanément de l'Editeur à la Console lorsque vous écrivez du code Java.

4) Associez Ctrl+X, O à "Next Editor." Lorsque dans Windows et en éditant du texte.

Cela vous permet de basculer rapidement entre les fichiers Java.

5) Associez Ctrl+Q à "Quick Fix."

Ainsi, lorsque vous tapez `@string/xx`, avec le curseur sur `xx`, en appuyant sur Ctrl+Q puis Entrée, cela vous amènera instantanément à `string.xml`, avec le curseur positionné sur le `TODO` dans `<string name="xx">TODO</string>`.

6) Associez Ctrl+Shift+W à "Close" (lorsque dans les fenêtres) et supprimez l'association d'origine (fermer tout).
Le raccourci de fermeture d'origine est Ctrl+W, ce qui correspond à nos habitudes dans les navigateurs, les boîtes de discussion et les explorateurs de fichiers. Cependant, cela entre en conflit avec la commande de coupure d'Emacs. En réalité, en appuyant sur Ctrl+Shift+W pendant une seconde, vous pouvez fermer beaucoup de fichiers. Donc, changer Ctrl+Shift+W de "fermer tout" à "fermer" ne fait pas perdre quoi que ce soit.

Il y a un problème : après avoir installé Emacs+, lorsque vous éditez du code et que l'assistant de code apparaît, appuyer sur les touches de flèche haut et bas ne sélectionne pas les éléments dans la liste des candidats de l'assistant de code ; au lieu de cela, cela déplace le curseur vers le haut et vers le bas dans le code en cours d'édition. La valeur par défaut est de l'activer avec F2. Activer l'assistant de code place le focus sur l'assistant de code, mais ensuite, vous ne pouvez utiliser les touches de flèche haut et bas que pour sélectionner. Ce serait génial si nous pouvions utiliser Ctrl+P et Ctrl+N ! L'édition du code serait fulgurante ! Mais le problème est que, après avoir installé le plugin Emacs+, bien qu'Eclipse ressemble davantage à Emacs, cette fonctionnalité est perdue. Dans un Eclipse propre, avec le schéma de clavier Emacs (et non Emacs+Scheme) sélectionné, vous pouvez utiliser Ctrl+N et Ctrl+P pour sélectionner les éléments de complétion lorsque l'assistant de code apparaît. Quelqu'un a posé la question sur Stack Overflow, mais il n'y a pas encore de réponse.

Si nous pouvions utiliser Ctrl+P et Ctrl+N pour sélectionner les éléments de complétion, ce serait vraiment formidable !