---
audio: false
generated: true
lang: fr
layout: post
title: Verrou SR et modifications de la bascule par Ben Eater
translated: true
type: note
---

Dans une vidéo précédente, j'ai parlé de la bascule SR, et je vous encourage à la revoir si vous ne la connaissez pas. Pour résumer, la bascule SR a deux entrées : **R** (Reset) et **S** (Set). Lorsque l'entrée Reset passe à l'état haut, la sortie **Q** passe à l'état bas (off), ce qui réinitialise la bascule. Lorsque l'entrée Set passe à l'état haut, la sortie **Q** passe à l'état haut (on), ce qui positionne la bascule. Il y a aussi une sortie complémentaire, **Q̅** (Q-bar), qui est toujours l'opposé de **Q**, sauf dans un cas : lorsque les deux entrées **R** et **S** sont simultanément à l'état haut. Dans ce scénario, **Q** et **Q̅** passent tous deux à l'état bas, ce qui est considéré comme un état invalide, car il ne faut pas positionner et réinitialiser la bascule en même temps. Si les deux entrées sont relâchées, l'état de la bascule devient imprévisible, car il dépend de l'entrée qui est relâchée en premier. Généralement, la bascule SR reste verrouillée dans l'un de ses deux états stables.

Dans cette vidéo, je vais parler des modifications apportées au circuit de base de la bascule SR. La première modification est la **bascule SR avec Enable**. Cette version ajoute des **portes ET** aux deux entrées **R** et **S**, contrôlées par un signal **Enable**. Lorsque le signal Enable est à l'état haut (1), les portes ET laissent passer les entrées **R** et **S** sans modification. Par exemple, si **Enable** est à 1 et **Reset** à 1, la porte ET sort un 1 ; si **Reset** est à 0, elle sort un 0. Cependant, si le signal **Enable** est à l'état bas (0), les sorties des portes ET sont toujours à 0, quelles que soient les entrées **R** et **S**. Cela amène la bascule à rester dans son dernier état, ignorant efficacement les entrées. Ainsi, le signal Enable permet soit d'activer la bascule pour qu'elle réagisse à ses entrées **R** et **S**, soit de la désactiver pour maintenir son état actuel.

Ensuite, nous pouvons étendre ce concept pour créer une **bascule SR (Flip-Flop)**. La différence clé entre une bascule (latch) et une bascule (flip-flop) est que les sorties d'une bascule changent chaque fois que ses entrées changent, tandis que les sorties d'une bascule (flip-flop) ne changent que sur un déclencheur spécifique, typiquement une impulsion d'horloge. Dans une bascule SR, une entrée **Horloge** (indiquée par un symbole triangulaire dans les schémas) contrôle la mise à jour des sorties. Plus précisément, les sorties **Q** et **Q̅** ne changent que lorsque l'horloge passe de bas à haut (un front montant). À tous les autres moments, les entrées **R** et **S** sont ignorées, et la bascule conserve son état précédent.

La bascule SR réalise cela en utilisant un condensateur dans le circuit d'horloge. Lorsque l'horloge passe de bas à haut, un courant bref traverse le condensateur pendant qu'il se charge, créant une courte impulsion de tension aux entrées des portes ET. Cette impulsion active efficacement la bascule SR avec Enable juste à ce moment-là, permettant aux entrées **R** et **S** d'affecter les sorties **Q** et **Q̅**. Une fois le condensateur complètement chargé, l'impulsion s'arrête, et la bascule ignore les changements d'entrée suivants jusqu'au prochain front montant.

Voici comment se comporte la bascule SR pendant un front montant d'horloge :
- Si **R** est haut et **S** est bas, **Q** passe à bas (reset), et **Q̅** passe à haut.
- Si **S** est haut et **R** est bas, **Q** passe à haut (set), et **Q̅** passe à bas.
- Si **R** et **S** sont tous deux bas, la bascule reste dans son état précédent.
- Si **R** et **S** sont tous deux hauts (l'état invalide de la bascule SR), le comportement est imprévisible. Semblable à la bascule SR, **Q** et **Q̅** peuvent tous deux passer à bas pendant l'impulsion, mais lorsque les entrées sont relâchées, la bascule se stabilise dans un état ou l'autre selon l'entrée qui baisse en premier. Cela rend la sortie incertaine, car elle dépend des différences de timing (par exemple, quelques nanosecondes), ce qui rend cet état invalide et imprévisible.

Pour résoudre cette imprévisibilité, nous pouvons utiliser une **bascule JK**, qui est similaire à la bascule SR mais inclut une rétroaction des sorties **Q** et **Q̅** vers les entrées. La bascule JK utilise des portes ET à trois entrées qui intègrent **J** (analogue à **S**), **K** (analogue à **R**), et les signaux de rétroaction **Q** et **Q̅**. Les lettres **J** et **K** sont arbitraires et ne représentent pas de termes spécifiques, mais elles distinguent ce circuit de la bascule SR.

La bascule JK fonctionne comme suit :
- Si **J** et **K** sont tous deux à 0, les sorties des portes ET sont à 0, donc la bascule reste dans son état précédent, même pendant une impulsion d'horloge.
- Si la bascule est actuellement positionnée (**Q** = 1, **Q̅** = 0) et que vous voulez la réinitialiser (**K** = 1, **J** = 0), la porte ET connectée à **K** sort un 1 pendant l'impulsion d'horloge (puisque **Q** = 1), ce qui réinitialise la bascule (**Q** = 0, **Q̅** = 1).
- Si la bascule est déjà réinitialisée (**Q** = 0, **Q̅** = 1) et que **K** = 1, **J** = 0, les sorties des portes ET restent à 0, donc la bascule reste réinitialisée, ce qui est le comportement souhaité.
- De même, si la bascule est réinitialisée (**Q** = 0, **Q̅** = 1) et que vous voulez la positionner (**J** = 1, **K** = 0), la porte ET connectée à **J** sort un 1 pendant l'impulsion d'horloge (puisque **Q̅** = 1), ce qui positionne la bascule (**Q** = 1, **Q̅** = 0).
- Si la bascule est déjà positionnée et que **J** = 1, **K** = 0, elle reste positionnée, comme prévu.

La caractéristique unique de la bascule JK apparaît lorsque **J** et **K** sont tous deux à 1. En raison de la rétroaction, une seule porte ET peut être active à la fois (puisque **Q** et **Q̅** ne peuvent pas être tous deux à 1). Si **Q** est à 1, la porte ET pour **K** est active, et la bascule se réinitialise à la prochaine impulsion d'horloge (**Q** = 0, **Q̅** = 1). Si **Q** est à 0, la porte ET pour **J** est active, et la bascule se positionne à la prochaine impulsion d'horloge (**Q** = 1, **Q̅** = 0). Cela crée un comportement de **basculement** (toggle) : si **J** = **K** = 1, la bascule change d'état à chaque impulsion d'horloge (**Q** passe de 0 à 1 ou de 1 à 0). Ce basculement prévisible élimine l'état invalide et imprévisible de la bascule SR, rendant la bascule JK plus robuste et polyvalente.