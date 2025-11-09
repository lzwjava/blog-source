---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Transformers à décodeur uniquement contre encodeur-décodeur
translated: true
type: note
---

### Principales différences entre les Transformers à décodeur uniquement et les Transformers encodeur-décodeur

Les Transformers sont des architectures de réseaux neuronaux largement utilisées dans le traitement du langage naturel (NLP) et au-delà. Le Transformer original (introduit dans l'article de 2017 « Attention is All You Need ») utilise une configuration **encodeur-décodeur**, tandis que les modèles de langage étendus (LLM) modernes comme GPT utilisent souvent une conception à **décodeur uniquement**. La tendance vers les modèles à décodeur uniquement a été motivée par leur simplicité et leur efficacité pour les tâches autorégressives (par exemple, la génération de texte). Ci-dessous, je détaillerai les principales différences.

#### Différences architecturales fondamentales
- **Encodeur-Décodeur** :
  - Se compose de deux piles symétriques : un **encodeur** (traite l'intégralité de la séquence d'entrée en parallèle, en utilisant l'auto-attention pour capturer le contexte bidirectionnel) et un **décodeur** (génère la sortie de manière autorégressive, en utilisant l'auto-attention avec masquage causal plus l'attention croisée vers la sortie de l'encodeur).
  - Idéal pour les tâches de **séquence à séquence (seq2seq)** où l'entrée et la sortie sont distinctes (par exemple, la traduction automatique : Anglais → Français).
  - Gère le contexte bidirectionnel dans l'entrée mais unidirectionnel (de gauche à droite) dans la sortie.

- **Décodeur uniquement** :
  - N'utilise que le composant décodeur, avec l'auto-attention modifiée par un **masquage causal** (chaque token ne peut prêter attention qu'aux tokens précédents, l'empêchant de « regarder » les tokens futurs).
  - Traite l'intégralité de la séquence (entrée + sortie) comme un seul flux pour la prédiction autorégressive (par exemple, la prédiction du token suivant dans la modélisation du langage).
  - Idéal pour les **tâches génératives** comme les chatbots, la complétion d'histoires ou la génération de code, où le modèle prédit un token à la fois en fonction du contexte antérieur.

#### Tableau comparatif

| Aspect              | Transformers à Décodeur Uniquement         | Transformers Encodeur-Décodeur               |
|---------------------|--------------------------------------------|-----------------------------------------------|
| **Composants**      | Pile unique de couches de décodeur (auto-attention + masque causal). | Piles doubles : encodeur (auto-attention bidirectionnelle) + décodeur (auto-attention, masque causal, attention croisée). |
| **Types d'Attention**| Auto-attention masquée uniquement (unidirectionnelle). | Auto-attention (bidirectionnelle dans l'encodeur), auto-attention masquée (dans le décodeur) et attention croisée (le décodeur prête attention à l'encodeur). |
| **Gestion Entrée/Sortie** | Entrée et sortie dans une seule séquence ; génération autorégressive. | Séparer les séquences d'entrée (encodées) et de sortie (décodées) ; permet un encodage parallèle. |
| **Complexité**      | Plus simple : Moins de paramètres, plus facile à mettre à l'échelle et à entraîner sur des données non étiquetées massives. | Plus complexe : Nombre de paramètres plus élevé, nécessite des données d'entrée-sortie appariées pour l'entraînement. |
| **Objectif d'Entraînement** | Typiquement la prédiction du token suivant (modélisation du langage causale). | Souvent une perte d'entropie croisée sur la séquence de sortie, utilisant le *teacher forcing*. |
| **Points Forts**    | Excelle dans la génération ouverte ; s'adapte bien à la mise à l'échelle (par exemple, GPT-3/4). Efficace pour la modélisation de contexte long. | Mieux adapté aux tâches structurées avec des mappages entrée-sortie clairs (par exemple, résumé, traduction). Gère le décodage non autorégressif. |
| **Points Faibles**  | Contexte bidirectionnel limité (ne peut pas « voir » l'intégralité de l'entrée en une fois) ; plus difficile pour les tâches nécessitant un encodage explicite de l'entrée. | Plus coûteux en calcul ; moins flexible pour le pré-entraînement purement génératif. |
| **Exemples**        | Série GPT, LLaMA, PaLM.                    | T5, BART, Transformer original pour la traduction. |

#### Pourquoi la préférence pour le décodeur uniquement ?
Les modèles à décodeur uniquement ont gagné en popularité car ils sont plus faciles à pré-entraîner sur de vastes quantités de données textuelles (il suffit de prédire le mot suivant) et à affiner pour diverses tâches en aval. Cette approche « un modèle pour tous les gouverner » simplifie le développement par rapport aux encodeurs-décodeurs, qui sont plus spécialisés. Cependant, les encodeurs-décodeurs excellent dans les scénarios nécessitant un alignement fort entre l'entrée et la sortie (par exemple, la génération conditionnelle).

Si vous implémentez cela ou avez un cas d'utilisation spécifique en tête, faites-le-moi savoir pour des conseils plus adaptés !

#### Références
- [Attention is All You Need (Article original sur le Transformer)](https://arxiv.org/abs/1706.03762)
- [Language Models are Few-Shot Learners (GPT-3, Exemple de décodeur uniquement)](https://arxiv.org/abs/2005.14165)
- [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5, Exemple encodeur-décodeur)](https://arxiv.org/abs/1910.10683)