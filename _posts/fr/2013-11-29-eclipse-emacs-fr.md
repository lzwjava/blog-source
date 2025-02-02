---
audio: false
lang: fr
layout: post
title: Transformer Eclipse en Emacs
translated: true
---

En tant qu'utilisateur d'Emacs depuis six mois, je ne peux tout simplement pas imaginer comment j'ai pu coder auparavant, en déplaçant mes mains de la position standard pour cliquer avec la souris ou appuyer sur les touches fléchées sans avoir l'impression que c'était gênant et insupportable. Maintenant, lorsque je dis à mes amis que j'ai configuré les raccourcis Alt+P et Alt+N pour passer rapidement entre les fichiers XML et la disposition graphique, leur réponse est juste "d'accord", ce qui implique que l'utilisation de la souris pour passer est également acceptable.
Pour moi, c'est un cauchemar; ce n'est tout simplement pas assez rapide ! Si vous êtes un utilisateur d'Emacs, vous comprenez...

Cet article décrit des techniques simples pour créer un environnement d'édition Eclipse rapide. En gros, vos mains peuvent rester en position standard, vous permettant de coder avec une efficacité maximale !

La chose la plus importante est d'installer le plugin Emacs+. Voir "Emacs+: Emacs Experience in Eclipse".

Pour bien utiliser l'assistant de code, vous devez le faire déclencher par n'importe quel caractère et empêcher l'auto-complétion lorsque vous appuyez sur l'espace ou =. Je recommande de télécharger ce fichier jar depuis CSDN. Avec celui-ci et une rapide recherche Google, vous pouvez importer des packages en un rien de temps.

Ensuite, personnalisons quelques raccourcis :

1) Associez Alt+P à "Précédent Sous-onglet" et Alt+N à "Suivant Sous-onglet."

Le sous-onglet est la barre d'onglets en dessous d'un éditeur, comme les onglets "Disposition Graphique" et "XML" lorsque vous éditez un fichier XML. Cela vous permet de visualiser instantanément la mise en page.

2) Associez Ctrl+C, Ctrl+C à "Exécuter."

C'est copié à partir de la configuration de sbcl. La valeur par défaut est Ctrl+F11, qui est trop loin pour un raccourci utilisé si fréquemment, ce qui fait que les utilisateurs d'Emacs se sentent mal ! J'ai stupidement appuyé sur Ctrl+F11 pendant quelques jours avant de le changer.

3) Associez Ctrl+X, Ctrl+O à "Vue suivante." En Windows et en éditant du texte.

Cela vous permet de passer instantanément de l'Éditeur à la Console lors de la rédaction de code Java.

4) Associez Ctrl+X, O à "Éditeur suivant." En Windows et en éditant du texte.

Cela vous permet de passer rapidement entre les fichiers Java.

5) Associez Ctrl+Q à "Correction Rapide."

Ainsi, lorsque vous tapez `@string/xx`, avec le curseur sur `xx`, appuyez sur Ctrl+Q puis Entrée pour passer instantanément à `string.xml`, avec le curseur positionné au niveau de `TODO` dans `<string name="xx">TODO</string>`.

6) Associez Ctrl+Shift+W à "Fermer" (en mode fenêtre) et supprimez l'association originale (fermer tout).
Le raccourci de fermeture d'origine est Ctrl+W, ce qui est en accord avec nos habitudes dans les navigateurs, les boîtes de discussion et les explorateurs de fichiers. Cependant, cela entre en conflit avec la commande de coupure d'Emacs. En réalité, en appuyant sur Ctrl+Shift+W pendant une seconde, vous pouvez fermer de nombreux fichiers. Donc, changer Ctrl+Shift+W de "fermer tout" à "fermer" ne perd rien.

Il y a un problème : après avoir installé Emacs+, lors de l'édition de code et de l'apparition de l'assistant de code, l'appui sur les touches de flèche haut et bas ne sélectionne pas d'éléments dans la liste de candidats de l'assistant de code ; au lieu de cela, il déplace vers le haut et vers le bas dans le code en cours d'édition. La valeur par défaut est de l'activer avec F2. L'activation de l'assistant de code met le focus sur l'assistant de code, mais ensuite vous ne pouvez utiliser les touches de flèche haut et bas que pour sélectionner. Ce serait merveilleux si nous pouvions utiliser Ctrl+P et Ctrl+N! L'édition de code serait fulgurante ! Mais le problème est que, après l'installation du plugin Emacs+, bien qu'Eclipse ressemble plus à Emacs, cette fonctionnalité est perdue. Dans un Eclipse propre, avec le clavier Emacs (et non Emacs+Scheme) sélectionné, vous pouvez utiliser Ctrl+N et Ctrl+P pour sélectionner les éléments de complétion lorsque l'assistant de code apparaît. Quelqu'un a posé la question sur Stack Overflow, mais il n'y a pas encore de réponse.

Si nous pouvions utiliser Ctrl+P et Ctrl+N pour sélectionner des éléments de complétion, ce serait vraiment génial !