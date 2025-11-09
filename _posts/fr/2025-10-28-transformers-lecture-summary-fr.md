---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: 'Introduction aux transformateurs : résumé du cours'
translated: true
type: note
---

### Résumé du cours « Introduction aux Transformers » d'Andrej Karpathy

Le cours d'Andrej Karpathy, faisant partie du cours CS25 de Stanford « Transformers United », est une plongée approfondie et accessible pour les débutants dans l'architecture Transformer—la colonne vertébrale des modèles d'IA modernes comme GPT et BERT. D'une durée d'environ une heure, il utilise des visuels intuitifs, des analogies et des extraits de code (incluant une démo en direct de son implémentation « NanoGPT ») pour démystifier le fonctionnement des Transformers. Karpathy retrace leur histoire, décompose la mécanique et explore leur polyvalence au-delà du langage. Voici un aperçu structuré des points clés :

#### Contexte du cours et vue d'ensemble
- **Pourquoi les Transformers sont importants** : Introduits dans l'article de 2017 « Attention is All You Need », les Transformers ont révolutionné l'IA depuis, dominant le traitement du langage naturel (NLP), la vision par ordinateur, la biologie (par ex., AlphaFold), la robotique, et plus encore. Ils ne sont pas seulement pour le texte—ils constituent un cadre flexible pour toute donnée séquentielle.
- **Objectifs du cours** : Il s'agit de la leçon d'introduction d'une série sur les bases des Transformers, l'auto-attention et les applications. Les sessions futures couvriront des modèles comme BERT/GPT et des interventions d'invités sur les utilisations en conditions réelles. Karpathy présente les Transformers comme un algorithme d'apprentissage « unifié », faisant converger les sous-domaines de l'IA vers des modèles évolutifs et pilotés par les données.

#### Évolution historique
- **Des premiers modèles aux goulots d'étranglement** : L'IA linguistique a commencé avec de simples réseaux de neurones (2003) prédisant les mots suivants via des perceptrons multicouches. Les RNN/LSTM (2014) ont ajouté la gestion des séquences pour des tâches comme la traduction mais ont atteint des limites : les goulots d'étranglement fixes des « encodeurs » comprimaient l'intégralité des entrées en un seul vecteur, perdant les détails sur les longues séquences.
- **L'essor de l'Attention** : Les mécanismes d'attention (terme popularisé par Yann LeCun) ont résolu ce problème en permettant aux décodeurs d'effectuer une « recherche douce » des parties pertinentes de l'entrée via des sommes pondérées. La percée de 2017 a abandonné les RNN entièrement, en pariant que « l'attention est tout ce dont vous avez besoin » pour un traitement parallèle—plus rapide et plus puissant.

#### Mécanismes de base : Auto-attention et échange de messages
- **Les Tokens comme des nœuds** : Considérez les données d'entrée (par ex., les mots) comme des « tokens » dans un graphe. L'auto-attention est comme des nœuds échangeant des messages : chaque token crée des **requêtes** (ce que je cherche), des **clés** (ce que j'offre) et des **valeurs** (ma charge utile de données). La similarité par produit scalaire entre les requêtes et les clés détermine les poids d'attention (via softmax), puis les poids multiplient les valeurs pour une mise à jour contextuelle.
- **Attention Multi-Têtes** : Exécutez ceci en parallèle dans des « têtes » avec des poids différents pour des perspectives plus riches, puis concaténez les résultats.
- **Masquage Causal** : Dans les décodeurs (pour la génération), masquez les tokens futurs pour empêcher la « triche » lors de la prédiction.
- **Encodage Positionnel** : Les Transformers traitent des ensembles, pas des séquences, donc ajoutez des encodages basés sur des sinus aux plongements pour injecter l'information d'ordre.
- **Intuition** : C'est une communication dépendante des données—les tokens « discutent » librement (encodeur) ou causalement (décodeur), capturant des dépendances à longue portée sans goulots d'étranglement séquentiels.

#### L'Architecture complète : Communication + Calcul
- **Configuration Encodeur-Décodeur** : L'encodeur connecte entièrement les tokens pour un flux bidirectionnel ; le décodeur ajoute une attention croisée vers les sorties de l'encodeur et une auto-attention causale pour la génération autorégressive.
- **Structure par Blocs** : Empilez des couches en alternance :
  - **Phase de Communication** : Auto-attention/attention croisée multi-têtes (échange de messages).
  - **Phase de Calcul** : MLP feed-forward (traitement individuel des tokens avec non-linéarité ReLU).
- **Extras pour la Stabilité** : Connexions résiduelles (ajout de l'entrée à la sortie), normalisation de couche.
- **Pourquoi ça marche** : Parallélisable sur les GPU, expressif pour les motifs complexes, et évolutif avec les données/la puissance de calcul.

#### Mise en pratique : Construire et entraîner avec NanoGPT
- **Implémentation Minimale** : Karpathy fait une démo de NanoGPT—un minuscule Transformer uniquement décodeur en PyTorch. Il s'entraîne sur du texte (par ex., Shakespeare) pour prédire les caractères/mots suivants.
  - **Préparation des Données** : Tokeniser en entiers, regrouper en lots de contextes de taille fixe (par ex., 1024 tokens).
  - **Passe Forward** : Plongement des tokens + encodages positionnels → blocs Transformer → logits → perte d'entropie croisée (cibles = entrées décalées).
  - **Génération** : Commencez avec un prompt, échantillonnez les tokens suivants de manière autorégressive, en respectant les limites du contexte.
- **Conseils d'Entraînement** : Taille du lot × longueur de séquence pour l'efficacité ; s'adapte à d'énormes modèles comme GPT-2.
- **Variantes** : Encodeur uniquement (BERT pour la classification via masquage) ; encodeur-décodeur complet pour la traduction.

#### Applications et Superpouvoirs
- **Au-delà du Texte** : Transformez les images/audio en patches tokenisés—l'auto-attention gère la « communication » non-euclidienne entre les patches, permettant les Vision Transformers (ViT).
- **Apprentissage en Contexte** : Fournissez des exemples dans le prompt ; les modèles « apprennent » les tâches à la volée (méta-apprentissage), sans besoin de réglage fin. Avec des données massives, les biais minimaux ressortent.
- **Flexibilité** : Traitez les états/actions d'apprentissage par renforcement comme un « langage », ou ajoutez une mémoire externe pour des contextes plus longs. Hybrides avec les modèles de diffusion pour les tâches itératives comme la génération d'images.

#### Défis et Perspectives futures
- **Obstacles** : Calcul quadratique (attention O(n²)), contrôle des hallucinations, gestion des longs contextes, alignement avec le cerveau.
- **Impact** : Les Transformers comme « ordinateurs à usage général » pour le texte—entraînés sur des données complexes pour exécuter des « programmes » comme le raisonnement ou la génération de code.
- **Et ensuite** : Modèles spécifiques à un domaine (par ex., GPTs pour la finance), intégration multimodale, meilleurs outils pour le raisonnement/l'audio/l'art. Karpathy évoque des ajustements pour l'efficacité et des ambitions de « GPT++ ».

Ce cours brille par ses analogies visuelles (par ex., l'attention comme un « curseur » en traduction) et ses explications de code, rendant les idées abstraites concrètes. Il est salué comme une excellente introduction car il construit l'intuition sans submerger de mathématiques—idéal pour les nouveaux venus.

[Stanford CS25 : Résumé du cours Transformers United](https://www.deciphr.ai/podcast/stanford-cs25-v2-i-introduction-to-transformers-w-andrej-karpathy-2)  
[Notes sur l'Introduction aux Transformers](https://ersantana.com/llm/stanford_cs25_transformers/02_intro_to_transformers)  
[Vidéo YouTube](https://www.youtube.com/watch?v=XfpMkf4rD6E)