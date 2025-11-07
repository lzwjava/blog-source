---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Optimiser les coûts de traduction avec le Markdown basé sur les paragraphes
translated: true
type: post
---

Mon blog Jekyll utilise Markdown pour écrire des paragraphes. Après avoir écrit en anglais, j'utilise des outils d'IA comme DeepSeek ou Mistral pour traduire dans huit autres langues. Bien qu'ils soient déjà peu coûteux, il y a encore place à l'amélioration.

Parfois, je n'édite qu'un mot ou un paragraphe, puis tout le texte d'un article est traduit dans les huit autres langues. Dans ce cas, l'utilisation de tokens est élevée. Si je ne traduisais que le paragraphe édité à nouveau, l'utilisation de tokens serait plus faible, surtout pour les longs articles.

Cependant, je veux toujours utiliser Markdown pour enregistrer mes idées. Utiliser une base de données pour maintenir et mettre à jour les articles n'est pas pratique. Utiliser YAML ou JSON pourrait être trop fastidieux.

L'essentiel est d'identifier les différences entre le texte avant et après l'édition. Si nous utilisons une approche par paragraphe, cela signifie diviser le texte en utilisant le caractère de nouvelle ligne "\n".

Je dois savoir quels paragraphes ont changé et lesquels n'ont pas changé après l'édition. Nous devons établir des correspondances un à un entre les paragraphes du texte avant et après l'édition.

Nous utilisons une approche par paragraphe car nous voulons mettre à jour les traductions faites par les modèles d'IA. Si nous utilisons des phrases, cela pourrait ne pas être aussi précis.

Pour Markdown, il pourrait être plus important d'utiliser un parsing Markdown pour synchroniser les traductions en fonction des éléments Markdown.

Mais si aucun bloc de code ou syntaxe Markdown spéciale n'est présent, nous pouvons utiliser une approche par paragraphe.

Pour une approche simple par paragraphe, nous avons deux tableaux de paragraphes et nous devons savoir comment ils correspondent.

Lors de la comparaison de n'importe quel paragraphe dans ces deux tableaux, il y a deux résultats possibles : ils sont identiques ou différents. S'ils sont différents, il y a plusieurs cas : les deux sont nouvellement ajoutés, le gauche est nouvellement ajouté, ou le droit est nouvellement ajouté.

Je veux simplement économiser des coûts, donc je vise à réduire l'utilisation des tokens. Je n'ai besoin de rien d'autre. Je dois simplement traduire chaque paragraphe, mettre le résultat en cache, et la prochaine fois, pour chaque paragraphe, je chercherai d'abord le résultat de la traduction. S'il n'existe pas, alors je devrai le traduire à nouveau.

Pour Markdown, c'est un peu plus compliqué. Je ne veux pas traduire les blocs de code. Donc, nous pouvons utiliser une bibliothèque de parsing Markdown pour traiter les blocs de code et le texte normal différemment.

Dans quelques semaines, je vais implémenter cela avec Python et Grok car c'est un problème réel. Je dois le résoudre.

Un design concerne les fichiers de cache. Je stocke le cache dans un répertoire de cache avec des fichiers comme `lang.json`, comme `zh.json`, etc.