---
audio: false
generated: true
lang: fr
layout: post
title: Les grands modèles de langage confirment mes intuitions sur la CFA
translated: true
type: note
---

https://weibo.com/6347862377/5183994120372979

https://substack.com/inbox/post/167355695

---

Comme mentionné dans mon précédent post Weibo, j'aime utiliser les LLM pour traiter des choses complexes et fastidieuses que je n'aime pas faire ou lire. Cela inclut de nombreux articles académiques.

Plus de dix ans après avoir créé PySonar2 (un outil d'inférence de types et d'analyse statique pour Python) en 2009-2010, je me suis retrouvé à discuter d'analyse de flux de contrôle (CFA) avec ChatGPT, ce qui a ravivé le souvenir d'un débat que j'avais eu avec un certain "étudiant en CFA" il y a dix ans.

https://www.yinwang.org/blog-cn/2016/04/07/cfa

(Les captures d'écran que j'avais uploadées sur un site web à l'époque ont maintenant disparu. Il faudra vous contenter de ce qui reste.)

C'est assez intéressant — des choses que je voyais clairement il y a plus de dix ans sont maintenant "confirmées" par ChatGPT.

Il y a quinze ans, lorsque PySonar2 a été créé, il dépassait déjà toutes les recherches académiques sur la CFA de l'époque (y compris la dernière CFA2). Pour un langage quasi-fonctionnel comme Python avec des fermetures lambda, c'était le premier à réaliser une telle précision dans l'inférence de types. Non seulement il était très précis, mais ses performances étaient également suffisamment correctes pour analyser tous les projets Python à grande échelle sur GitHub.

Le fondateur de Sourcegraph, le plus grand utilisateur de PySonar2, m'avait dit à l'époque que l'analyse de PySonar2 était étonnamment précise. Sur le moment, je n'y avais pas trop réfléchi parce que mon approche était si simple que je supposais que n'importe qui aurait pu y penser. Ce n'est que lorsque j'ai réalisé que personne d'autre ne l'avait fait auparavant que j'ai pensé que je devrais peut-être en souligner la valeur.

Même aujourd'hui, l'IDE PyCharm de JetBrains ne peut pas réaliser une analyse aussi précise ou une fonctionnalité de "recherche de définition" aussi performante. Par exemple, si vous définissez une variable globale initialisée à `None` et que vous lui assignez plus tard une structure dans une certaine "fonction d'initialisation", vous ne pourrez pas trouver les membres de cette structure. Je ne dis pas que vous devriez écrire un code aussi mauvais, mais c'est un exemple.

Si vous saviez ce que j'ai accompli à l'Université de l'Indiana, vous comprendriez que PySonar2 n'était vraiment pas grand-chose pour moi — cela n'a pris qu'une petite fraction de mes efforts. À l'époque, je ne m'intéressais pas beaucoup au langage Python. Et ces articles sur la CFA étaient si obscurs que je n'avais aucun intérêt à m'y plonger. Je les ai seulement parcourus et j'ai pu voir qu'ils étaient pour la plupart absurdes. J'ai donc construit PySonar2 en quelques mois, je l'ai laissé les autres l'utiliser librement, et je n'ai pas pris la peine d'écrire un article. Je pouvais expliquer ses principes en quelques phrases seulement.

J'étais trop modeste. Regardez tous ces articles sur la CFA, k-CFA, CFA2 — une pile, et pourtant ils ne pouvaient pas résoudre les problèmes du monde réel et n'ont jamais été mis en pratique. La k-CFA avait même un problème fondamental où les "appels et retours ne pouvaient pas correspondre", quelque chose que je n'aurais jamais imaginé pouvoir arriver. PySonar2 n'a jamais eu ce problème. Comment quelqu'un a-t-il pu faire une conception aussi stupide, publier un article là-dessus et avoir des successeurs qui continuent à "l'améliorer" ?

La CFA2 de Matt Might a introduit une sorte "d'automate à pile", qui n'était qu'un moyen de retrouver la pile d'appels de fonctions à partir des conceptions défectueuses des travaux précédents. PySonar2 a toujours eu un "automate à pile" parce qu'une pile apparaît naturellement lors de l'interprétation des appels de fonctions.

Matt Might avait un blog où il expliquait fièrement comment la "transformation CPS automatique" était née, comme s'il était le seul à la comprendre. Mais ses idées ont clairement évolué à partir d'articles CPS excessivement complexes et n'étaient pas le fruit d'une réflexion indépendante, portant beaucoup de bagages historiques. Son écriture semble souvent profonde mais est difficile à suivre — pouvez-vous réellement la comprendre ? Ses idées ne peuvent pas rivaliser avec mon approche des "40 lignes de code". Je riais en lisant son blog, mais par politesse et "modestie", je suis resté silencieux. Je pense que Matt Might manque de substance réelle, et que ce groupe de personnes ne faisait que débiter des absurdités. C'est la vérité, que je peux révéler après toutes ces années.

Est-ce que ces articles ne produisent pas que du charabia ? Oui, je le savais il y a plus de dix ans. Mais qui pouvait comprendre ce qui se passait ? Maintenant, vous pouvez vérifier avec ChatGPT :)

En fait, ChatGPT a également confirmé autre chose : l'utilisation de CPS dans l'article fondateur sur la CFA d'Olin Shivers était à l'origine de tous les problèmes :

PySonar2 a été construit entièrement de manière indépendante, sans référence à aucun travail académique. Il s'est attaqué directement au problème racine sans aucun bagage académique. C'est la valeur d'une pensée simple. Ce n'était pas la première fois que je dépassais indépendamment à la fois le monde académique et l'industrie avec un résultat aussi tranchant.

Après que j'ai créé PySonar2, une équipe de Google a passé plus de deux ans à essayer de construire quelque chose de mieux, mais ils n'ont abouti à rien, et Google a dû continuer à utiliser mon code open-source amélioré. Pourquoi ? Parce que leur stratégie était erronée dès le départ. Ils voulaient utiliser un langage de programmation logique comme Prolog pour l'inférence de types de Python, et j'ai su tout de suite que c'était voué à l'échec. Comment le savais-je ? Parce que j'avais déjà implémenté ces méthodes et que je comprenais les limites du système de Hindley-Milner et de Prolog. Et comment le savais-je ? Parce que j'avais implémenté et amélioré des langages de programmation logique à IU.

Je dois remercier ChatGPT pour avoir clairement articulé les faits que j'avais observés, m'évitant ainsi de lire ces articles obscurs. Je suis reconnaissant pour sa validation de la valeur de mes idées. Je sens que les LLM vont grandement contribuer au progrès humain.

Maintenant, je partage une conversation que j'ai eue avec ChatGPT à propos de la CFA, en espérant que cela aidera les chercheurs dans ce domaine :

https://chatgpt.com/share/6864e9a1-66c8-8002-b9f5-55e845fde7ae