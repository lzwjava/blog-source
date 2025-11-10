---
audio: false
generated: true
lang: fr
layout: post
title: Conception et test d'une bascule JK
translated: true
type: note
---

Dans une vidéo précédente, nous avons exploré la bascule JK et son fonctionnement, en notant sa similitude avec la bascule SR mais avec l'ajout d'un mécanisme de rétroaction. Cette rétroaction permet à la sortie de basculer lorsque les deux entrées sont à l'état haut sur un front montant d'horloge, au lieu d'entrer dans un état indéfini. Dans cette vidéo, je vise à la construire et à observer son fonctionnement pratique.

J'ai construit une bascule JK en suivant le schéma de circuit fourni. Pendant la construction, j'ai réalisé une erreur d'étiquetage dans le schéma : ceci est en fait l'entrée K, et ceci est l'entrée J. J correspond à la mise à 1 (Set), ce qui signifie que lorsqu'elle passe à l'état haut, la sortie Q devrait également passer à l'état haut. Inversement, K correspond à la remise à zéro (Reset), donc lorsqu'elle passe à l'état haut, la sortie Q devrait passer à l'état bas. À part cette correction d'étiquetage mineure, le reste du circuit est exact.

Pour les portes NOR, j'utilise la puce 74LS02, plus précisément les deux portes NOR sur son côté supérieur. L'autre puce, le 74LS11, est une porte ET triple à 3 entrées. J'utilise deux de ces portes ET à trois entrées pour le circuit.

Après avoir mis le circuit sous tension, celui-ci se stabilise dans un état, la sortie Q semblant être "allumée". J'ai ensuite connecté mon circuit d'horloge. Les deux interrupteurs que vous voyez sont maintenus à l'état bas via des résistances de rappel (pull-down) ; appuyer sur un bouton fait passer l'entrée à l'état haut. Ces interrupteurs sont connectés par des fils verts aux deux portes ET, servant d'entrées K et J.

Le signal d'horloge alimente également les portes ET. Il passe par un circuit RC, constitué d'un condensateur de 0,0001 microfarad et d'une résistance de 1000 ohms. La sortie de ce circuit RC, transportée par deux fils blancs, va vers une autre entrée sur les deux portes ET. Les sorties de ces portes ET sont représentées par des fils bleus, qui se connectent à deux des entrées des portes NOR. Les autres entrées des portes NOR reçoivent une rétroaction de leurs propres sorties via des fils jaunes. Ces fils jaunes bouclent également vers les portes ET. Enfin, les sorties des portes NOR pilotent deux LED : une pour Q et une pour le complément de Q.

Lorsque l'entrée K est maintenue à l'état haut, la bascule devrait se réinitialiser, et la sortie Q devrait s'éteindre, ce qu'elle fait. De même, maintenir l'entrée J à l'état haut devrait mettre la bascule à 1, allumant la sortie Q, ce qu'elle fait également. Il est important de noter que le changement n'est pas instantané lors de l'appui sur le bouton ; il se produit avec le prochain signal d'horloge, car cette opération est conditionnée par le front montant de l'horloge.

Maintenant, comme il s'agit d'une bascule JK, si les deux entrées J et K sont maintenues à l'état haut, nous nous attendons à ce que la sortie bascule à chaque impulsion d'horloge. Cependant, elle ne bascule pas de manière cohérente. Parfois, elle le fait, surtout si je manipule légèrement le circuit, mais c'est très irrégulier. Pour m'assurer que j'appuie sur les deux boutons, je vais insérer des cavaliers, fournissant effectivement une entrée haute continue à la fois à J et K. Cela *devrait* la faire basculer à chaque front montant d'horloge. Bien que cela fonctionne mieux maintenant, c'est encore irrégulier.

Ce comportement inconstant a une explication claire, et la meilleure façon de le comprendre est d'utiliser un oscilloscope pour examiner les signaux.

D'abord, regardons l'entrée d'horloge pour référence. L'oscilloscope montre le signal d'horloge s'activant et se désactivant, environ deux fois par seconde. Chaque division sur l'oscilloscope représente 100 millisecondes, donc sur 10 divisions, il y a deux impulsions par seconde.

Ensuite, je veux observer la sortie, car c'est ce que nous attendons de voir basculer à chaque impulsion d'horloge. L'horloge pulse bien à environ deux impulsions par seconde. Actuellement, la sortie ne bascule pas, mais avec un léger ajustement, elle bascule, bien qu'inconstant. Quand elle bascule, elle le fait sur les fronts montants de l'horloge, comme souhaité.

La partie intéressante apparaît lorsque nous zoomons sur le front montant de l'horloge. Nous y voyons une certaine activité. En zoomant davantage, cela devient assez clair : quand l'horloge passe à l'état haut, la sortie bascule bien, mais elle bascule d'avant en arrière plusieurs fois avant de finalement se stabiliser dans un état stable. C'est précisément la raison pour laquelle le comportement est si inconstant. La sortie bascule comme souhaité sur le front montant de l'horloge, mais ensuite elle bascule rapidement à nouveau peu de temps après. La période de ces bascules rapides est d'environ 82 nanosecondes.

Ce phénomène, connu sous le nom de "course" (racing), est logique lorsque nous réexaminons le schéma du circuit. L'impulsion d'horloge, même si nous avons l'intention de n'utiliser que son front montant, reste à l'état haut pendant une durée considérable (250 millisecondes dans ce cas). Si la sortie commute *avant* que cette impulsion ne revienne à zéro, la boucle de rétroaction la fait commuter à nouveau, et encore, conduisant à de multiples basculements. Ainsi, lorsque l'impulsion d'horloge passe à l'état haut, la sortie s'allume, mais s'éteint et se rallume immédiatement et répétitivement. Ce n'est que par chance qu'elle se stabilise parfois dans l'état souhaité.

La cause fondamentale de cette condition de course réside dans le circuit RC utilisé pour détecter le front montant. J'ai mentionné que le condensateur est de 0,0001 microfarads et la résistance de 1000 ohms. Multiplier ces valeurs donne la constante de temps du circuit RC, qui indique la largeur de l'impulsion. Cette constante de temps est d'environ 100 nanosecondes.

Mesurons l'impulsion d'entrée pour le circuit. Initialement, elle semble parfaite lorsqu'on dézoome – une impulsion rapide sur le front montant de l'horloge, comme souhaité. Le problème est que cette impulsion n'est pas assez *rapide*. C'est une impulsion d'1 microseconde, et pendant cette microseconde, la sortie bascule de manière répétée avant de finalement se stabiliser lorsque l'impulsion retombe à un niveau logique zéro.

Que peut-on faire à ce sujet ? Une option est de raccourcir l'impulsion. Étant donné que la période de basculement est d'environ 80 nanosecondes, nous avons besoin d'une impulsion nettement plus courte qu'1 microseconde. Nous pouvons essayer de changer la résistance de 1000 ohms pour une résistance de 100 ohms, ce qui devrait réduire la constante de temps à 100 nanosecondes.

Après avoir remplacé la résistance, nous observons une impulsion beaucoup plus petite. Cependant, cela ne fonctionne toujours pas de manière cohérente. À ce stade, nous atteignons les limites des plaques d'essais (breadboards). Les signaux haute vitesse dans la gamme des dizaines de nanosecondes sont difficiles à gérer sur les plaques d'essais en raison des capacités parasites, des inductances parasites et d'autres effets parasites. Cela explique pourquoi le simple fait d'agiter ma main près du circuit peut modifier son comportement, car ma main modifie la capacité en agissant comme un objet mis à la terre.

Vous pouvez voir que la sortie passe maintenant à l'état haut, puis à l'état bas, et reste basse. Mais encore une fois, si j'ajuste la position de ma main, elle pourrait se mettre à basculer. Je ne change aucune connexion, je bouge juste ma main, ce qui affecte la capacitance.

Même le front montant de notre horloge n'est pas parfaitement net à cette échelle de temps, encore une fois à cause des limitations de la plaque d'essais. L'impulsion que nous générons n'est pas aussi propre qu'avec la résistance plus grande. Finalement, tout cela indique que nous repoussons les limites de ce qui est réalisable sur une plaque d'essais. Cette méthode particulière de détection d'un front montant utilisant un circuit RC est intrinsèquement problématique dans une bascule JK en raison de la condition de course. Si l'impulsion n'est pas suffisamment étroite (idéalement juste quelques nanosecondes), la sortie se réinjectera et basculera plus d'une fois par front montant d'horloge.

Alors, quelle est la solution ? Dans la prochaine vidéo, je démontrerai une méthode bien supérieure pour construire une bascule JK qui élimine entièrement ce problème de course : la bascule JK maître-esclave. C'est une conception beaucoup plus robuste et devrait fonctionner sans aucun problème sur une plaque d'essais.