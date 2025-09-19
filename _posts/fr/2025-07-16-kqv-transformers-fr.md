---
audio: false
generated: false
image: false
lang: fr
layout: post
title: KQV, Transformateurs et GPT
translated: true
---

```markdown
## Comment j'ai compris le mécanisme KQV dans les Transformers

*2025.07.16*

Après avoir lu [Mécanisme K, Q, V dans les Transformers](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en), j'ai plus ou moins compris comment fonctionnent K, Q et V.

Q signifie *Query* (Requête), K signifie *Key* (Clé) et V signifie *Value* (Valeur). Pour une phrase, la Requête est une matrice qui stocke la valeur d'un token qui doit interroger les autres tokens. La Clé représente la description des tokens, et la Valeur représente la matrice de signification réelle des tokens.

Ils ont des formes spécifiques, il faut donc connaître leurs dimensions et leurs détails.

J'ai compris cela début juin 2025. J'en avais entendu parler pour la première fois fin 2023. À l'époque, j'avais lu des articles comme [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), mais je n'avais pas bien compris.

Après environ deux ans, je trouve que c'est plus facile à comprendre maintenant. Pendant ces deux années, je me suis concentré sur le développement backend et la préparation de mes examens de licence, et je n'ai pas beaucoup lu ou appris sur le *machine learning*. Cependant, j'y ai réfléchi de temps en temps en conduisant ou en faisant autre chose.

Cela me rappelle l'effet du temps. Nous pouvons apprendre beaucoup de choses en un premier contact, même si nous ne comprenons pas grand-chose. Mais d'une certaine manière, cela déclenche un point de départ pour notre réflexion.

Avec le temps, j'ai remarqué que pour les connaissances et les découvertes, il est difficile de réfléchir ou de comprendre les choses dès la première fois. Mais plus tard, il semble plus facile d'apprendre et de savoir.

Une des raisons est qu'à l'ère de l'IA, il est plus facile d'apprendre car on peut approfondir n'importe quel détail ou aspect pour résoudre ses doutes. Il y a aussi plus de vidéos sur l'IA disponibles. Plus important encore, on voit que tant de gens apprennent et construisent des projets sur cette base, comme [llama.cpp](https://github.com/ggml-org/llama.cpp).

L'histoire de Georgi Gerganov est inspirante. En tant que nouvel apprenant en *machine learning* depuis environ 2021, il a eu un impact puissant dans la communauté de l'IA.

Ce genre de chose se reproduira encore et encore. Donc, pour l'apprentissage par renforcement et les dernières connaissances en IA, même si je ne peux pas encore y consacrer beaucoup de temps, je pense pouvoir trouver un peu de temps pour apprendre rapidement et essayer d'y réfléchir souvent. Le cerveau fera son travail.

---

## Des réseaux de neurones à GPT

*2023.09.28*

### Vidéos YouTube

Andrej Karpathy - Construisons GPT : de zéro, en code, expliqué en détail.

Umar Jamil - L'attention est tout ce dont vous avez besoin (Transformer) - Explication du modèle (y compris les mathématiques), Inférence et Entraînement

StatQuest avec Josh Starmer - Réseaux de neurones Transformers, fondements de ChatGPT, Expliqué clairement !!!

Pascal Poupart - CS480/680 Cours 19 : Attention et réseaux Transformers

The A.I. Hacker - Michael Phi - Guide illustré des réseaux de neurones Transformers : une explication étape par étape

### Comment j'apprends

Après avoir lu la moitié du livre *Neural Networks and Deep Learning*, j'ai commencé à reproduire l'exemple de réseau de neurones pour la reconnaissance de chiffres manuscrits. J'ai créé un dépôt sur GitHub, [https://github.com/lzwjava/neural-networks-and-zhiwei-learning](https://github.com/lzwjava/neural-networks-and-zhiwei-learning).

C'est là la partie vraiment difficile. Si quelqu'un peut l'écrire de zéro sans copier de code, c'est qu'il comprend très bien.

Mon code de réplication manque encore de l'implémentation de *update_mini_batch* et de la rétropropagation. Cependant, en observant attentivement les variables lors des phases de chargement des données, de propagation avant et d'évaluation, j'ai beaucoup mieux compris les vecteurs, la dimensionnalité, les matrices et les formes des objets.

Et j'ai commencé à apprendre l'implémentation de GPT et des Transformers. Grâce à l'encodage des mots et à l'encodage positionnel, le texte est transformé en nombres. Ensuite, en essence, cela ne diffère pas d'un simple réseau de neurones pour reconnaître des chiffres manuscrits.

La conférence d'Andrej Karpathy *« Let's build GPT »* est très bonne. Il explique bien les choses.

La première raison est qu'il part vraiment de zéro. On voit d'abord comment générer du texte. C'est un peu flou et aléatoire. La deuxième raison est qu'Andrej peut expliquer les choses de manière très intuitive. Andrej a travaillé sur le projet nanoGPT pendant plusieurs mois.

J'ai eu une nouvelle idée pour juger de la qualité d'une conférence. L'auteur peut-il vraiment écrire ces codes ? Pourquoi est-ce que je ne comprends pas et quel sujet l'auteur a-t-il omis ? En plus de ces beaux schémas et animations, quels sont leurs défauts et leurs lacunes ?

Revenons au sujet du *machine learning* lui-même. Comme le mentionne Andrej, le *dropout*, les connexions résiduelles, l'*auto-attention*, l'*attention multi-têtes*, l'*attention masquée*.

En regardant plus de vidéos comme celles-ci, j'ai commencé à comprendre un peu.

Grâce à l'encodage positionnel avec les fonctions sin et cos, nous obtenons certains poids. Grâce à l'encodage des mots, nous transformons les mots en nombres.

$$
    PE_{(pos,2i)} = \sin(pos/10000^{2i/d_{model}}) \\
    PE_{(pos,2i+1)} = \cos(pos/10000^{2i/d_{model}})
$$

> La pizza est sortie du four et elle avait bon goût.

Dans cette phrase, comment l'algorithme sait-il si cela fait référence à la pizza ou au four ? Comment calculons-nous les similarités pour chaque mot de la phrase ?

Nous voulons un ensemble de poids. Si nous utilisons le réseau Transformer pour faire de la traduction, chaque fois que nous entrons une phrase, il peut sortir la phrase correspondante dans une autre langue.

À propos du produit scalaire ici. Une raison pour laquelle nous utilisons le produit scalaire est qu'il prend en compte chaque nombre dans le vecteur. Que se passerait-il si nous utilisions le produit scalaire au carré ? Nous calculerions d'abord le carré des nombres, puis nous ferions le produit scalaire. Que se passerait-il si nous faisions un produit scalaire inversé ?

En ce qui concerne le masquage, nous changeons les nombres de la moitié de la matrice en moins l'infini. Ensuite, nous utilisons la fonction *softmax* pour que les valeurs soient comprises entre 0 et 1. Que se passerait-il si nous changions les nombres en bas à gauche en moins l'infini ?

### Plan

Continuer à lire du code et des articles, et regarder des vidéos. Juste s'amuser et suivre ma curiosité.

[https://github.com/karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)

[https://github.com/jadore801120/attention-is-all-you-need-pytorch](https://github.com/jadore801120/attention-is-all-you-need-pytorch)
```