---
audio: false
generated: true
image: false
lang: fr
layout: post
model: anthropic/claude-sonnet-4
title: Guide de Tokenisation TikToken et Exemples
translated: true
type: note
---

Ce code démontre comment utiliser la bibliothèque **TikToken**, qui est le tokeniseur d'OpenAI pour compter et traiter les tokens dans un texte qui sera envoyé à des modèles de langage comme GPT-3.5, GPT-4, etc.

## Fonction de TikToken

TikToken convertit le texte en **tokens** - les unités de base que les modèles de langage traitent. Chaque token correspond approximativement à un mot ou à une partie de mot. Comprendre la tokenisation est crucial car :

- Les coûts de l'API sont basés sur le nombre de tokens
- Les modèles ont des limites de tokens pour l'entrée/sortie
- Le nombre de tokens affecte la vitesse de traitement

## Analyse du Code

### 1. Encodage de base (`basic_encoding()`)
```python
enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
tokens = enc.encode("Hello, how are you doing today?```
- Crée un tokeniseur pour GPT-3.5-turbo
- Convertit le texte en une liste d'IDs de tokens : `[9906, 11, 1268, 527, 499, 3815, 3432, 30]`
- Montre que "Hello, how are you doing today?" = 8 tokens
- Peut décoder les tokens pour retrouver le texte original

### 2. Comparaison de modèles (`different_models()`)
Compare comment différents modèles tokenisent le même texte :
- **GPT-4** : 10 tokens pour "The quick brown fox jumps over the lazy dog."
- **GPT-3.5-turbo** : 10 tokens (même encodage)
- **text-davinci-003** : 10 tokens (même encodage)

Différents modèles peuvent utiliser différents tokeniseurs, donc les décomptes de tokens peuvent varier.

### 3. Traitement par lots (`batch_processing()`)
Montre comment traiter efficacement plusieurs textes :
- Traite 3 messages de longueurs différentes
- Calcule le total de tokens sur tous les messages (15 au total)
- Utile pour estimer les coûts lors de l'envoi de multiples messages

### 4. Tokens spéciaux (`special_tokens()`)
Gère les tokens de contrôle spéciaux comme `<|endoftext|>` :
- Montre les tokens spéciaux disponibles pour le modèle
- Démontre l'encodage de texte contenant des tokens spéciaux
- Utilise `allowed_special="all"` pour traiter les tokens spéciaux

### 5. Comptage efficace (`count_tokens_efficiently()`)
Deux méthodes pour compter les tokens :
- **Méthode 1** : Stocker les tokens puis compter (`len(enc.encode(text))`)
- **Méthode 2** : Comptage direct (plus efficace en mémoire pour les grands textes)
- Calcule le ratio tokens-par-mot (1.29 dans cet exemple)

## Applications pratiques

1. **Estimation des coûts** : Calculer les coûts de l'API avant de faire des requêtes
2. **Validation des entrées** : S'assurer que le texte respecte les limites de tokens du modèle
3. **Optimisation des lots** : Grouper les messages efficacement pour les appels API
4. **Suivi des performances** : Surveiller l'utilisation des tokens dans les applications

## Principales observations de la sortie

- Les phrases simples utilisent moins de tokens que prévu
- Le décompte de tokens n'équivaut pas toujours au décompte de mots
- Différents modèles peuvent tokeniser différemment
- Les tokens spéciaux nécessitent une manipulation attentive

Cette bibliothèque est essentielle pour quiconque construit des applications avec les APIs d'OpenAI, car elle fournit un comptage de tokens précis qui correspond à ce que l'API vous facturera réellement.