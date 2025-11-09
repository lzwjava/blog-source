---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Optimisation de l'entraînement des réseaux neuronaux profonds
translated: true
type: note
---

### Chapitre 8 : Optimisation pour l'entraînement des modèles profonds

Ce chapitre de *Deep Learning* par Ian Goodfellow, Yoshua Bengio et Aaron Courville se concentre sur les techniques d'optimisation basées sur le gradient conçues pour l'entraînement des réseaux de neurones profonds. Il s'appuie sur les concepts de base du chapitre 4 et met l'accent sur la minimisation d'une fonction de coût \\( J(\theta) \\) pour trouver les paramètres optimaux \\( \theta \\), où \\( J(\theta) \\) combine typiquement une perte sur les données d'entraînement et des termes de régularisation. L'objectif est d'approximer le risque réel \\( J^*(\theta) = \mathbb{E}_{(x,y) \sim p_{data}} L(f(x;\theta), y) \\), mais en pratique, cela se fait via le risque empirique sur l'ensemble d'entraînement.

#### En quoi l'apprentissage diffère de l'optimisation pure
L'optimisation en apprentissage automatique ne consiste pas à minimiser directement la fonction de coût, mais à améliorer indirectement les performances sur des données non vues (par exemple, la précision sur l'ensemble de test). Les différences clés incluent :
- **Objectifs indirects** : Le coût \\( J(\theta) \\) est un proxy pour une mesure intraitable comme la perte 0-1. Des fonctions de perte substitutives (par exemple, la log-vraisemblance négative pour la classification) sont utilisées car les pertes réelles manquent souvent de gradients utiles.
- **Décomposabilité** : \\( J(\theta) \\) est une moyenne sur les exemples, permettant la minimisation du risque empirique (ERM) : \\( J(\theta) \approx \frac{1}{m} \sum_{i=1}^m L(f(x^{(i)};\theta), y^{(i)}) \\).
- **Risques de surapprentissage** : Les modèles à haute capacité peuvent mémoriser les données d'entraînement, donc l'arrêt précoce (basé sur les performances de validation) est crucial, même si la perte d'entraînement continue de diminuer.
- **Stratégies de lot** :
  - **Méthodes par lot** : Utilisent l'ensemble de données complet pour des gradients exacts (déterministes mais lents pour les grandes données).
  - **Descente de gradient stochastique (SGD)** : Utilise des exemples individuels (mises à jour bruyantes mais rapides).
  - **Méthodes par mini-lot** : Équilibre entre les deux, courant en apprentissage profond (tailles comme 32–256). Le bruit des petits lots aide à la régularisation ; le mélange des données empêche les biais.

L'apprentissage en ligne (données en flux) approxime les gradients du risque réel sans répétition.

#### Défis de l'optimisation en apprentissage profond
L'entraînement de modèles profonds est intensif en calcul (jours à mois sur des clusters) et plus difficile que l'optimisation classique en raison de :
- **Intractabilité** : Pertes non différentiables et surapprentissage dans l'ERM.
- **Échelle** : Les grands jeux de données rendent les gradients par lot complet irréalisables ; l'échantillonnage introduit de la variance (l'erreur évolue comme \\( 1/\sqrt{n} \\)).
- **Problèmes de données** : Redondance, corrélations (corrigées par le mélange) et biais dû au rééchantillonnage.
- **Limites matérielles** : Les tailles de lot sont contraintes par la mémoire ; le parallélisme asynchrone aide mais peut introduire des incohérences.
- Obstacles spécifiques aux réseaux de neurones (détaillés plus loin) : Mauvais conditionnement, minima locaux, plateaux et gradients disparaissants/explosants.

Les méthodes du premier ordre (basées uniquement sur le gradient) tolèrent mieux le bruit que celles du second ordre (basées sur la Hessienne), qui amplifient les erreurs dans les petits lots.

#### Algorithmes d'optimisation
Le chapitre passe en revue les algorithmes pour minimiser \\( J(\theta) \\), en commençant par la SGD canonique et en étendant aux variantes :
- **Descente de gradient stochastique (SGD)** : Mise à jour de base par mini-lot : \\( \theta \leftarrow \theta - \epsilon \hat{g} \\), où \\( \hat{g} \\) est l'estimation du gradient du mini-lot et \\( \epsilon \\) est le taux d'apprentissage. Converge plus vite que les méthodes par lot grâce au bruit qui permet d'échapper aux mauvais minima locaux.
- **Momentum et variantes** : Ajoutent des termes de vitesse pour accélérer dans les régions plates et amortir les oscillations.
- **Méthodes adaptatives** : Ajustent les taux d'apprentissage par paramètre (par exemple, AdaGrad, RMSProp, Adam) pour gérer les gradients clairsemés et les échelles variables.
- **Approximations du second ordre** : Utilisent l'information de courbure (par exemple, gradient conjugué, gradient naturel) pour un meilleur conditionnement, mais sont coûteuses.
- **Descente de coordonnées et autres** : Pour des architectures spécifiques.

Les conseils pratiques incluent la planification du taux d'apprentissage, l'initialisation (par exemple, Xavier) et la combinaison de méthodes (par exemple, préconditionnement).

#### Autres parties majeures
- **Initialisation des paramètres** : Critique pour éviter les gradients disparaissants ; discute de l'initialisation symétrique/orthogonale et du pré-entraînement couche par couche.
- **Compromis** : Équilibre vitesse de convergence, stabilité et généralisation ; souligne le réglage piloté par la validation.
- **Sujets avancés** : Couvre les gradients retardés dans les contextes asynchrones, l'optimisation distribuée et les liens avec les méthodes évolutionnaires.

Globalement, le chapitre souligne qu'aucun algorithme unique ne domine – le succès repose sur un réglage spécifique au problème, avec la SGD et ses extensions comme chevaux de bataille pour l'apprentissage profond.

[Livre Deep Learning - Chapitre 8 : Optimisation](https://www.deeplearningbook.org/contents/optimization.html)