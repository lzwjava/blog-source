---
audio: false
generated: false
image: false
lang: fr
layout: post
title: Comment fonctionne un réseau de neurones
translated: true
usemathjax: true
---

Parlons directement du cœur du fonctionnement des réseaux de neurones. À savoir, l'algorithme de rétropropagation :

1. Entrée x : Définir l'activation correspondante $$a^{1}$$ pour la couche d'entrée.
2. Propagation avant : Pour chaque l=2,3,…,L, calculer $$z^{l} = w^l a^{l-1}+b^l$$ et $$a^{l} = \sigma(z^{l})$$
3. Erreur de sortie $$\delta^{L}$$ : Calculer le vecteur $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$
4. Rétropropagation de l'erreur : Pour chaque l=L−1,L−2,…,2, calculer $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$
5. Sortie : Le gradient de la fonction de coût est donné par $$\frac{\partial C}{\partial w^l_{jk}} = a^{l-1}_k \delta^l_j$$ et $$\frac{\partial C}{\partial b^l_j} = \delta^l_j $$

Ceci est copié du livre *Neural Networks and Deep Learning* de Michael Nelson. Est-ce accablant ? Cela pourrait l'être la première fois que vous le voyez. Mais ce ne l'est plus après un mois d'étude autour de ce sujet. Laissez-moi vous expliquer.

## Entrée

Il y a 5 phases. La première phase est l'**Entrée**. Ici, nous utilisons des chiffres manuscrits comme entrée. Notre tâche est de les reconnaître. Un chiffre manuscrit est composé de 784 pixels, soit 28*28. Dans chaque pixel, il y a une valeur en niveaux de gris qui varie de 0 à 255. L'activation signifie que nous utilisons une fonction pour l'activer, afin de transformer sa valeur d'origine en une nouvelle valeur pour faciliter le traitement.

Supposons que nous ayons maintenant 1000 images de 784 pixels. Nous les utilisons pour entraîner un modèle à reconnaître le chiffre qu'elles représentent. Nous avons également 100 images pour tester l'efficacité de cet apprentissage. Si le programme parvient à reconnaître correctement les chiffres sur 97 images, nous disons que sa précision est de 97 %.

Nous allons donc parcourir les 1000 images pour entraîner les poids et les biais. Nous rendons les poids et les biais plus précis à chaque fois que nous lui donnons une nouvelle image à apprendre.

Le résultat d'un entraînement par lot doit être reflété dans 10 neurones. Ici, les 10 neurones représentent les chiffres de 0 à 9, et leur valeur varie de 0 à 1 pour indiquer leur niveau de confiance quant à la précision de leur prédiction.

Et l'entrée est composée de 784 neurones. Comment pouvons-nous réduire 784 neurones à 10 neurones ? Voici la chose. Supposons que nous ayons deux couches. Que signifie une couche ? C'est-à-dire que dans la première couche, nous avons 784 neurones. Dans la deuxième couche, nous avons 10 neurones.

Nous attribuons à chaque neurone parmi les 784 neurones un poids, disons,

$$w_1, w_2, w_3, w_4, ... , w_{784}$$

Et donnez à la première couche un biais, c'est-à-dire $$b_1$$.

Et donc, pour le premier neurone de la deuxième couche, sa valeur est :

$$w_1*a_1 + w_2*a_2+...+ w_{784}*a_{784}+b_1$$

Mais ces poids et ce biais sont pour $$neuron^2_{1}$$ (le premier neurone de la deuxième couche). Pour $$neuron^2_{2}$$, nous avons besoin d'un autre ensemble de poids et d'un biais.

Et la fonction sigmoïde ? Nous utilisons la fonction sigmoïde pour mapper la valeur ci-dessus entre 0 et 1.

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

Nous utilisons également la fonction sigmoïde pour activer la première couche. Cela dit, nous transformons cette valeur en niveaux de gris pour qu'elle soit comprise entre 0 et 1. Ainsi, chaque neurone dans chaque couche a maintenant une valeur comprise entre 0 et 1.

Ainsi, pour notre réseau à deux couches, la première couche compte 784 neurones, et la deuxième couche en compte 10. Nous l'entraînons pour obtenir les poids et les biais.

Nous avons 784 * 10 poids et 10 biais. Dans la deuxième couche, pour chaque neurone, nous utiliserons 784 poids et 1 biais pour calculer sa valeur. Le code ici ressemble à,

```python
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
```

## Réseau Feedforward

> Propagation avant : Pour chaque l=2,3,…,L, calculez $$z^{l} = w^l a^{l-1}+b^l$$ et $$a^{l} = \sigma(z^{l})$$

Remarquez ici que nous utilisons la valeur de la dernière couche, c'est-à-dire $$a^{l-1}$$, ainsi que le poids de la couche actuelle, $$w^l$$, et son biais $$b^l$$, pour appliquer la fonction sigmoïde et obtenir la valeur de la couche actuelle, $$a^{l}$$.

Code :

```python
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # propagation avant
        activation = x
        activations = [x] 
        zs = [] 
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
```
## Erreur de sortie

> Erreur de sortie $$\delta^{L}$$ : Calculez le vecteur $$\delta^{L} = \nabla_a C \odot \sigma'(z^L)$$

Voyons ce que signifie le $$\nabla$$.

> Del, ou nabla, est un opérateur utilisé en mathématiques (notamment en calcul vectoriel) comme un opérateur différentiel vectoriel, généralement représenté par le symbole nabla ∇.

$$
\begin{eqnarray}
  w_k & \rightarrow & w_k' = w_k-\eta \frac{\partial C}{\partial w_k} \\
  b_l & \rightarrow & b_l' = b_l-\eta \frac{\partial C}{\partial b_l}
\end{eqnarray}
$$

Ici, $$\eta $$ représente le taux d'apprentissage. Nous utilisons la dérivée de C par rapport aux poids et au biais, c'est-à-dire le taux de changement entre eux. Cela correspond à `sigmoid_prime` dans le code ci-dessous.

Code :

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

*Remarque : Le code est en anglais et ne nécessite pas de traduction, car il s'agit d'une fonction Python qui calcule la dérivée du coût entre les activations de sortie (`output_activations`) et les valeurs cibles (`y`).*

## Rétropropager l'erreur

> Rétropropager l'erreur : Pour chaque \( l = L-1, L-2, \ldots, 2 \), calculer $$\delta^{l} = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^{l})$$

```python
     for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)
```

## Sortie

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

## Final

C'est un article court. Et pour la plupart, il montre simplement le code et des formules mathématiques. Mais cela me convient. Avant de l'écrire, je ne comprenais pas clairement. Après l'avoir écrit, ou simplement en copiant des extraits de code et de livre, j'ai compris la plupart des concepts. Après avoir gagné en confiance grâce à l'enseignant Yin Wang, en lisant environ 30% du livre *Neural Networks and Deep Learning*, en écoutant les cours de Stanford d'Andrej Karpathy et les cours d'Andrew Ng, en discutant avec mon ami Qi, et en bidouillant avec Anaconda, numpy, et les bibliothèques Theano pour faire fonctionner le code d'il y a des années, je comprends maintenant.

L'un des points clés est la dimension. Nous devons connaître les dimensions de chaque symbole et variable. Et il effectue simplement le calcul différentiable. Terminons par les citations de Yin Wang :

> L'apprentissage automatique est vraiment utile, on pourrait même dire que c'est une théorie magnifique, car ce n'est rien d'autre que du calcul différentiel après une métamorphose ! C'est l'ancienne et grande théorie de Newton et Leibniz, sous une forme plus simple, élégante et puissante. L'apprentissage automatique consiste essentiellement à utiliser le calcul pour dériver et ajuster certaines fonctions, et l'apprentissage profond consiste à ajuster des fonctions plus complexes.

> Il n'y a pas d'« intelligence » dans l'intelligence artificielle, pas de « neurone » dans les réseaux de neurones, pas d'« apprentissage » dans l'apprentissage automatique, et pas de « profondeur » dans l'apprentissage profond. Ce qui fonctionne vraiment dans ce domaine s'appelle le « calcul ». Je préfère donc appeler ce domaine le « calcul différentiable », et le processus de construction de modèles est appelé « programmation différentiable ».