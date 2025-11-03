---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Réseau neuronal, Transformer et GPT
translated: true
---

### Table des matières

1. [Comment j'ai appris le mécanisme KQV dans les Transformers](#how-i-learned-the-kqv-mechanism-in-transformers)
   - Les matrices Query, Key, Value représentent les interactions de tokens
   - La compréhension nécessite de connaître les dimensions et les formes
   - Les concepts initiaux deviennent plus clairs avec le temps
   - L'ère de l'IA offre d'abondantes ressources d'apprentissage
   - Des histoires inspirantes motivent la poursuite de l'apprentissage

2. [Du réseau neuronal à GPT](#from-neural-network-to-gpt)
   - Répliquer des réseaux neuronaux à partir de zéro pour la compréhension
   - Les Transformers traitent le texte via l'embedding et l'encodage
   - L'auto-attention calcule les similarités entre les mots
   - Regarder des conférences fondamentales et lire le code
   - Suivre la curiosité à travers des projets et des articles

3. [Comment fonctionne un réseau neuronal](#how-neural-network-works)
   - L'algorithme de rétropropagation met à jour les poids et les biais
   - Les données d'entrée s'activent à travers les couches du réseau
   - Le feedforward calcule les sorties des couches via la sigmoïde
   - Le calcul de l'erreur guide les ajustements d'apprentissage
   - La compréhension dimensionnelle est cruciale pour la compréhension


## Comment j'ai appris le mécanisme KQV dans les Transformers

*16.07.2025*

Après avoir lu [K, Q, V Mechanism in Transformers](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en), j'ai en quelque sorte compris comment K, Q et V fonctionnent.

Q signifie Query, K signifie Key, et V signifie Value. Pour une phrase, la Query est une matrice qui stocke la valeur d'un token dont elle a besoin pour interroger d'autres tokens. La Key représente la description des tokens, et la Value représente la matrice de sens réelle des tokens.

Ils ont des formes spécifiques, il faut donc connaître leurs dimensions et leurs détails.

J'ai compris cela vers début juin 2025. J'en ai appris la première fois vers fin 2023. À cette époque, j'ai lu des articles comme [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), mais je n'ai pas compris grand-chose.

Après environ deux ans, j'ai trouvé cela plus facile à comprendre maintenant. Au cours de ces deux années, je me suis concentré sur le travail de backend et la préparation de mes examens de DEUG, et je n'ai pas beaucoup lu ou appris sur le machine learning. Cependant, j'ai ruminé ces concepts de temps en temps quand je conduisais ou faisais d'autres choses.

Cela me rappelle l'effet du temps. Nous pouvons apprendre beaucoup de choses à première vue, même si nous ne comprenons pas grand-chose. Mais d'une manière ou d'une autre, cela déclenche un point de départ pour notre réflexion.

Avec le temps, j'ai constaté que pour la connaissance et la découverte, il est difficile de penser ou de comprendre les choses la première fois. Mais plus tard, il semble plus facile d'apprendre et de savoir.

Une des raisons est que dans l'ère de l'IA, il est plus facile d'apprendre parce que vous pouvez approfondir n'importe quel détail ou aspect pour résoudre vos doutes. Il y a aussi plus de vidéos d'IA connexes disponibles. Plus important encore, vous voyez que tant de gens apprennent et construisent des projets par-dessus, comme [llama.cpp](https://github.com/ggml-org/llama.cpp).

L'histoire de Georgi Gerganov est inspirante. En tant que nouvel apprenti en machine learning commençant vers 2021, il a eu un impact puissant dans la communauté de l'IA.

Ce genre de chose se reproduira encore et encore. Ainsi, pour l'apprentissage par renforcement et les dernières connaissances en IA, même si je ne peux toujours pas leur consacrer beaucoup de temps, je pense que je peux trouver du temps pour apprendre rapidement et essayer d'y penser beaucoup. Le cerveau fera son travail.


---

## Du réseau neuronal à GPT

*28.09.2023*

### Vidéos YouTube

Andrej Karpathy - Let's build GPT: from scratch, in code, spelled out.

Umar Jamil - Attention is all you need (Transformer) - Model explanation (including math), Inference and Training

StatQuest with Josh Starmer - Transformer Neural Networks, ChatGPT's foundation, Clearly Explained!!!

Pascal Poupart - CS480/680 Lecture 19: Attention and Transformer Networks

The A.I. Hacker - Michael Phi - Illustrated Guide to Transformers Neural Network: A step-by-step explanation

### Comment j'apprends

Une fois que j'avais lu la moitié du livre "Neural Networks and Deep Learning", j'ai commencé à reproduire l'exemple de réseau neuronal de reconnaissance de chiffres manuscrits. J'ai créé un dépôt sur GitHub, https://github.com/lzwjava/neural-networks-and-zhiwei-learning.

C'est la partie la plus difficile. Si on peut l'écrire à partir de zéro sans copier de code, on comprend très bien.

Mon code répliqué manque encore l'implémentation de update_mini_batch et backprop. Cependant, en observant attentivement les variables dans la phase de chargement des données, de feedforward et d'évaluation, j'ai obtenu une bien meilleure compréhension des vecteurs, de la dimensionnalité, des matrices et de la forme des objets.

Et j'ai commencé à apprendre l'implémentation du GPT et du transformer. Par l'embedding de mots et l'encodage de position, le texte se transforme en nombres. Ensuite, en substance, il n'y a pas de différence avec le réseau neuronal simple pour reconnaître les chiffres manuscrits.

La conférence d'Andrej Karpathy "Let's build GPT" est très bonne. Il explique bien les choses.

La première raison est que c'est vraiment à partir de zéro. Nous voyons d'abord comment générer du texte. C'est un peu flou et aléatoire. La deuxième raison est qu'Andrej a su dire les choses de manière très intuitive. Andrej a réalisé le projet nanoGPT pendant plusieurs mois.

J'ai juste eu une nouvelle idée pour juger la qualité de la conférence. L'auteur peut-il vraiment écrire ces codes ? Pourquoi je ne comprends pas et quel sujet l'auteur manque-t-il ? Outre ces diagrammes et animations élégants, quels sont leurs lacunes et leurs défauts ?

Retour au sujet du machine learning lui-même. Comme le mentionne Andrej, le dropout, la connexion résiduelle, l'auto-attention, l'attention multi-tête, l'attention masquée.

En regardant plus de vidéos ci-dessus, j'ai commencé à comprendre un peu.

Par l'encodage positionnel avec des fonctions sin et cos, nous obtenons des poids. Par l'embedding de mots, nous transformons les mots en nombres.

$$
    PE_{(pos,2i)} = sin(pos/10000^{2i/d_{model}}) \\
    PE_{(pos,2i+1)} = cos(pos/10000^{2i/d_{model}})
$$

> La pizza est sortie du four et elle était délicieuse.

Dans cette phrase, comment l'algorithme sait-il si "elle" fait référence à la pizza ou au four ? Comment calculons-nous les similarités pour chaque mot de la phrase ?

Nous voulons un ensemble de poids. Si nous utilisons le réseau transformateur pour faire la tâche de traduction, chaque fois que nous entrons une phrase, il peut produire la phrase correspondante d'une autre langue.

À propos du produit scalaire ici. Une des raisons pour lesquelles nous utilisons le produit scalaire ici est que le produit scalaire prendra en compte chaque nombre du vecteur. Que se passe-t-il si nous utilisons le produit scalaire carré ? Nous calculons d'abord le carré des nombres, puis nous les laissons faire le produit scalaire. Que se passe-t-il si nous faisons un produit scalaire inversé ?

À propos du masquage ici, nous changeons les nombres de la moitié de la matrice en l'infini négatif. Et ensuite nous utilisons softmax pour que les valeurs soient comprises entre 0 et 1. Que faire si nous changeons les nombres en bas à gauche en l'infini négatif ?

### Plan

Continuer à lire le code et les papiers et à regarder des vidéos. Amusez-vous et suivez ma curiosité.

https://github.com/karpathy/nanoGPT

https://github.com/jadore801120/attention-is-all-you-need-pytorch

---

## Comment fonctionne un réseau neuronal

*30.05.2023*

Discutons directement du cœur du travail neuronal. C'est-à-dire, l'algorithme de rétropropagation :

1. Entrée x : Définir l'activation correspondante $$a^{1}$$ pour la couche d'entrée.
2. Propagation avant (Feedforward) : Pour chaque l=2,3,…,L calculer $$z^{l} = w^l a^{l-1}+b^l$$ et $$a^{l} = \sigma(z^{l})$$
3. Erreur de sortie $$\delta^{L}$$ : Calculer le vecteur $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$
4. Rétropropager l'erreur : Pour chaque l=L−1,L−2,…,2, calculer $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$
5. Sortie : Le gradient de la fonction de coût est donné par $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$ et $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$

Ceci est copié du livre de Michael Nelson *Neural Networks and Deep Learning*. Est-ce accablant ? Cela pourrait l'être la première fois que vous le voyez. Mais ce n'est plus le cas après un mois d'étude autour de cela. Laissez-moi vous expliquer.

### Entrée

Il y a 5 phases. La première phase est l'Entrée. Ici, nous utilisons des chiffres manuscrits comme entrée. Notre tâche est de les reconnaître. Un chiffre manuscrit a 784 pixels, ce qui est 28*28. Dans chaque pixel, il y a une valeur de niveau de gris qui varie de 0 à 255. Donc l'activation signifie que nous utilisons une fonction pour l'activer, pour changer sa valeur originale en une nouvelle valeur pour la commodité du traitement.

Disons, nous avons maintenant 1000 images de 784 pixels. Nous l'entraînons maintenant à reconnaître le chiffre qu'elles montrent. Nous avons maintenant 100 images pour tester cet effet d'apprentissage. Si le programme peut reconnaître les chiffres de 97 images, nous disons que sa précision est de 97%.

Nous allons donc parcourir les 1000 images, pour entraîner les poids et les biais. Nous rendons les poids et les biais plus corrects chaque fois que nous lui donnons une nouvelle image à apprendre.

Le résultat d'un entraînement par lot doit être reflété dans 10 neurones. Ici, les 10 neurones représentent de 0 à 9 et leur valeur est comprise entre 0 et 1 pour indiquer leur confiance quant à leur précision.

Et l'entrée est de 784 neurones. Comment pouvons-nous réduire 784 neurones à 10 neurones ? Voici comment. Supposons que nous ayons deux couches. Que signifie la couche ? C'est la première couche, nous avons 784 neurones. Dans la deuxième couche, nous avons 10 neurones.

Nous donnons à chaque neurone des 784 neurones un poids, disons,

$$w_1, w_2, w_3, w_4, ..., w_{784}$$

Et nous donnons à la première couche, un biais, c'est-à-dire, $$b_1$$.

Et ainsi pour le premier neurone de la deuxième couche, sa valeur est :

$$w_1*a_1 + w_2*a_2+...+ w_{784}*a_{784}+b_1$$

Mais ces poids et un biais sont pour $$neuron^2_{1}$$ (le premier de la deuxième couche). Pour le $$neuron^2_{2}$$, nous avons besoin d'un autre ensemble de poids et d'un biais.

Que diriez-vous de la fonction sigmoïde ? Nous utilisons la fonction sigmoïde pour mapper la valeur de ce qui précède de 0 à 1.

$$
\begin{eqnarray}
  \sigma(z) \equiv \frac{1}{1+e^{-z}}
\end{eqnarray}
$$

$$
\begin{eqnarray}
  \frac{1}{1+\exp(-\sum_j w_j x_j-b)}
\end{eqnarray}
$$

Nous utilisons également la fonction sigmoïde pour activer la première couche. C'est-à-dire que nous changeons cette valeur de niveau de gris en une plage de 0 à 1. Ainsi, maintenant, chaque neurone dans chaque couche a une valeur de 0 à 1.

Ainsi, pour notre réseau à deux couches, la première couche a 784 neurones, et la deuxième couche a 10 neurones. Nous l'entraînxons pour obtenir les poids et les biais.

Nous avons 784 * 10 poids et 10 biais. Dans la deuxième couche, pour chaque neurone, nous utiliserons 784 poids et 1 biais pour calculer sa valeur. Le code ressemble à ceci :

```python
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
```

### Feedforward (Propagation avant)

> Feedforward : Pour chaque l=2,3,…,L calculer $$z^{l} = w^l a^{l-1}+b^l$$ et $$a^{l} = \sigma(z^{l})$$

Notez ici que nous utilisons la valeur de la dernière couche, c'est-à-dire $$a^{l-1}$$, et le poids de la couche actuelle, $$w^l$$, et son biais $$b^l$$ pour effectuer la sigmoïde afin d'obtenir la valeur de la couche actuelle, $$a^{l}$$.

Code :

```python
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x]
        zs = []
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
```
### Erreur de sortie

> Erreur de sortie $$\delta^{L}$$ : Calculer le vecteur $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$

Voyons ce que signifie $$\nabla$$.

> Del, ou nabla, est un opérateur utilisé en mathématiques (particulièrement en calcul vectoriel) comme opérateur différentiel vectoriel, généralement représenté par le symbole nabla ∇.

$$
\begin{eqnarray}
  w_k & \rightarrow & w_k' = w_k-\eta \frac{\partial C}{\partial w_k} \\
  b_l & \rightarrow & b_l' = b_l-\eta \frac{\partial C}{\partial b_l}
\end{eqnarray}
$$

Ici $$\eta $$ est le taux d'apprentissage. Nous utilisons la dérivée du coût C par rapport aux poids et au biais, qui est le taux de changement entre eux. C'est `sigmoid_prime` ci-dessous.

Code:

```python
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
```

```python
    def cost_derivative(self, output_activations, y):
        return (output_activations-y)
```

### Rétropropagation de l'erreur

> Rétropropagation de l'erreur : Pour chaque l=L−1,L−2,…,2, calculer $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$

```python
     for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)
```

### Sortie

> Sortie : Le gradient de la fonction de coût est donné par $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$
et $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$

```python
    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]
```

### Final

C'est un court article. Et pour la plupart, il ne fait que montrer le code et les formules mathématiques. Mais cela me convient. Avant de l'écrire, je ne comprenais pas clairement. Après l'avoir écrit ou simplement copié des extraits de code et de livre, je le comprends en grande partie. Après avoir gagné la confiance du professeur Yin Wang, lu environ 30% du livre *Neural Networks and Deep Learning*, écouté les conférences de Stanford d'Andrej Karpathy et les cours d'Andrew Ng, discuté avec mon ami Qi, et travaillé avec les bibliothèques Anaconda, numpy et Theano pour faire fonctionner le code d'il y a des années, je le comprends maintenant.

L'un des points clés est les dimensions. Nous devons connaître les dimensions de chaque symbole et variable. Et cela ne fait que le calcul différentiable. Terminons par les citations de Yin Wang :

> Le machine learning est vraiment utile, on pourrait même dire une belle théorie, car c'est simplement du calcul après un relooking ! C'est l'ancienne et grande théorie de Newton, Leibniz, sous une forme plus simple, élégante et puissante. Le machine learning est fondamentalement l'utilisation du calcul pour dériver et ajuster certaines fonctions, et le deep learning est l'ajustement de fonctions plus complexes.

> Il n'y a pas d'"intelligence" dans l'intelligence artificielle, pas de "neuronal" dans les réseaux neuronaux, pas d'"apprentissage" dans le machine learning, et pas de "profondeur" dans le deep learning. Il n'y a pas de "profondeur" dans le deep learning. Ce qui fonctionne vraiment dans ce domaine s'appelle le "calcul différentiel". Je préfère donc appeler ce domaine "calcul différentiable", et le processus de construction de modèles s'appelle "programmation différentiable".