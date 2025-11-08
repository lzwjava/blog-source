---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: La puissance surprenante des réseaux neuronaux récurrents
translated: true
type: note
---

Cet article de blog de 2015 par Andrej Karpathy est une introduction classique aux réseaux de neurones récurrents (RNN), mettant en lumière leur puissance surprenante pour gérer des séquences comme la génération de texte. Karpathy partage son enthousiasme après avoir entraîné des RNN pour des tâches comme la légende d'images, qui ont produit des résultats cohérents avec un réglage minimal. Il publie un code open-source pour des modèles de langage au niveau des caractères utilisant des LSTMs (un type de RNN) et démontre leur « magie » à travers diverses expériences de génération de texte. Ci-dessous se trouve un résumé structuré des sections clés.

## Introduction
Karpathy décrit les RNN comme « déraisonnablement efficaces » pour les données séquentielles, les contrastant avec les réseaux feedforward traditionnels qui gèrent des entrées/sorties de taille fixe. Il entraîne des RNN simples sur des corpus de texte pour prédire et générer des caractères, s'interrogeant sur leur capacité à capturer si bien les motifs du langage. L'article inclut du code sur GitHub pour reproduire les démonstrations.

## Concepts Clés : Fonctionnement des RNN
Les RNN excellent avec les séquences (par ex., phrases, vidéos) en maintenant un « état » interne (vecteur caché) qui transporte l'information à travers les pas de temps. Contrairement aux réseaux statiques, ils appliquent la même transformation de manière répétée :

- **Types d'Entrée/Sortie** : Entrée fixe vers sortie séquentielle (par ex., image vers légende) ; séquence vers sortie fixe (par ex., phrase vers sentiment) ; séquence-à-séquence (par ex., traduction).
- **Mécanisme Central** : À chaque pas, le nouvel état \\( h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t) \\), où \\( x_t \\) est l'entrée, et la sortie \\( y_t \\) est dérivée de l'état. Entraîné via la rétropropagation dans le temps (BPTT).
- **Profondeur et Variantes** : Empiler des couches pour la profondeur ; utiliser des LSTMs pour mieux gérer les dépendances à long terme que les RNN standards.
- **Note Philosophique** : Les RNN sont Turing-complets, essentiellement des « programmes apprenants » plutôt que de simples fonctions.

Un simple extrait Python illustre la fonction step :
```python
def step(self, x):
    self.h = np.tanh(np.dot(self.W_hh, self.h) + np.dot(self.W_xh, x))
    y = np.dot(self.W_hy, self.h)
    return y
```

## Modélisation du Langage au Niveau des Caractères
L'exemple central : Entraîner sur du texte pour prédire le caractère suivant (encodé one-hot), construisant des distributions de probabilité sur un vocabulaire (par ex., 65 caractères pour l'anglais). La génération fonctionne en échantillonnant à partir des prédictions et en les réinjectant. Le modèle apprend le contexte via les connexions récurrentes—par ex., prédire 'l' après "hel" vs. "he". Entraîné avec SGD par mini-lots et des optimiseurs comme RMSProp.

## Démonstrations : Texte Généré par RNN
Toutes utilisent le code char-rnn de l'auteur sur des fichiers texte uniques, montrant une progression du charabia vers une sortie cohérente.

- **Essais de Paul Graham** (~1 Mo) : Imite le style des conseils en startup. Exemple : "The surprised in investors weren’t going to raise money... Don’t work at first member to see the way kids will seem in advance of a bad successful startup."
- **Shakespeare** (4,4 Mo) : Produit des dialogues semblables à des pièces de théâtre. Exemple : "PANDARUS: Alas, I think he shall be come approached and the day When little srain would be attain'd into being never fed..."
- **Wikipedia** (96 Mo) : Génère un texte de type article avec markdown, liens et listes. Exemple : "Naturalism and decision for the majority of Arab countries' capitalide was grounded by the Irish language by [[John Clair]]..."
- **LaTeX de Géométrie Algébrique** (16 Mo) : Produit des preuves mathématiques presque compilables. Exemple : "\begin{proof} We may assume that $\mathcal{I}$ is an abelian sheaf on $\mathcal{C}$..."
- **Code C du Noyau Linux** (474 Mo) : Fonctions réalistes avec commentaires et syntaxe correcte. Exemple : "static int indicate_policy(void) { ... if (ss->segment < mem_total) unblock_graph_and_set_blocked(); ... }"
- **Prénoms de Bébé** (8 000 noms) : Inventions nouvelles comme "Rudi Levette" ou "Hany Mareanne".

La « température » contrôle l'échantillonnage : Basse pour un texte répétitif mais sûr ; élevée pour un texte créatif mais erratique.

## Défis et Limitations
- Dépendances à long terme : Oublie le contexte initial (par ex., balises LaTeX non appariées).
- Mémorisation plutôt que généralisation : Bon pour la syntaxe/structure mais hallucine le contenu.
- Calcul intensif : Nécessite des GPUs ; les RNN standards sont instables sans LSTMs.
- Correctifs futurs : Mémoire externe (Neural Turing Machines), mécanismes d'attention.

## Conclusion
Les RNN brillent en TAL (traduction, reconnaissance vocale), en vision (légendage d'images), et au-delà, évoluant du non-sens vers une génération structurée. Karpathy visualise les activations (par ex., des neurones détectant les guillemets) et taquine avec un RNN entraîné sur l'article lui-même, produisant un méta-texte comme "I've the RNN with and works...". Il recommande des lectures complémentaires et des ressources de code, prédisant le rôle des RNN dans une IA plus intelligente.

[The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)