---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Deep Learning par Goodfellow Bengio Courville
translated: true
type: note
---

**Ian Goodfellow**  
**Yoshua Bengio**  
**Aaron Courville**

## Table des matières

- Site Web viii  
- Remerciements ix  
- Notation xiii  

### 1 Introduction 1

- 1.1 À qui ce livre est-il destiné ? 8  
- 1.2 Tendances historiques de l'apprentissage profond 12  

## I Mathématiques appliquées et bases de l'apprentissage automatique 27

### 2 Algèbre linéaire 29

- 2.1 Scalaires, vecteurs, matrices et tenseurs 29  
- 2.2 Multiplication de matrices et de vecteurs 32  
- 2.3 Matrices identité et inverse 34  
- 2.4 Dépendance linéaire et espace vectoriel 35  
- 2.5 Normes 37  
- 2.6 Types particuliers de matrices et de vecteurs 38  
- 2.7 Décomposition en valeurs propres 40  
- 2.8 Décomposition en valeurs singulières 42  
- 2.9 Pseudo-inverse de Moore-Penrose 43  
- 2.10 Opérateur trace 44  
- 2.11 Déterminant 45  
- 2.12 Exemple : Analyse en composantes principales 45  

### 3 Probabilités et théorie de l'information 51

- 3.1 Pourquoi les probabilités ? 52  
- 3.2 Variables aléatoires 54  
- 3.3 Distributions de probabilité 54  
- 3.4 Probabilité marginale 56  
- 3.5 Probabilité conditionnelle 57  
- 3.6 Règle de chaînage des probabilités conditionnelles 57  
- 3.7 Indépendance et indépendance conditionnelle 58  
- 3.8 Espérance, variance et covariance 58  
- 3.9 Distributions de probabilité courantes 60  
- 3.10 Propriétés utiles des fonctions courantes 65  
- 3.11 Règle de Bayes 68  
- 3.12 Détails techniques sur les variables continues 69  
- 3.13 Théorie de l'information 71  
- 3.14 Modèles probabilistes structurés 73  

### 4 Calcul numérique 78

- 4.1 Dépassement et sous-dépassement de capacité 78  
- 4.2 Mauvais conditionnement 80  
- 4.3 Optimisation basée sur le gradient 80  
- 4.4 Optimisation sous contrainte 91  
- 4.5 Exemple : Moindres carrés linéaires 94  

### 5 Bases de l'apprentissage automatique 96

- 5.1 Algorithmes d'apprentissage 97  
- 5.2 Capacité, sur-apprentissage et sous-apprentissage 108  
- 5.3 Hyperparamètres et ensembles de validation 118  
- 5.4 Estimateurs, biais et variance 120  
- 5.5 Estimation du maximum de vraisemblance 129  
- 5.6 Statistiques bayésiennes 133  
- 5.7 Algorithmes d'apprentissage supervisé 137  
- 5.8 Algorithmes d'apprentissage non supervisé 142  
- 5.9 Descente de gradient stochastique 149  
- 5.10 Construction d'un algorithme d'apprentissage automatique 151  
- 5.11 Défis motivant l'apprentissage profond 152  

## II Réseaux profonds : Pratiques modernes 162

### 6 Réseaux feedforward profonds 164

- 6.1 Exemple : Apprentissage du XOR 167  
- 6.2 Apprentissage basé sur le gradient 172  
- 6.3 Unités cachées 187  
- 6.4 Conception d'architecture 193  
- 6.5 Rétropropagation et autres algorithmes de différenciation 200  
- 6.6 Notes historiques 220  

### 7 Régularisation pour l'apprentissage profond 224

- 7.1 Pénalités de norme des paramètres 226  
- 7.2 Pénalités de norme comme optimisation sous contrainte 233  
- 7.3 Régularisation et problèmes sous-contraints 235  
- 7.4 Augmentation des données 236  
- 7.5 Robustesse au bruit 238  
- 7.6 Apprentissage semi-supervisé 240  
- 7.7 Apprentissage multi-tâches 241  
- 7.8 Arrêt précoce 241  
- 7.9 Liaison et partage de paramètres 249  
- 7.10 Représentations parcimonieuses 251  
- 7.11 Bagging et autres méthodes d'ensemble 253  
- 7.12 Dropout 255  
- 7.13 Apprentissage antagoniste 265  
- 7.14 Distance tangente, Tangent Prop et classifieur par variété tangente 267  

### 8 Optimisation pour l'entraînement de modèles profonds 271

- 8.1 Différence entre l'apprentissage et l'optimisation pure 272  
- 8.2 Défis de l'optimisation des réseaux de neurones 279  
- 8.3 Algorithmes de base 290  
- 8.4 Stratégies d'initialisation des paramètres 296  
- 8.5 Algorithmes à taux d'apprentissage adaptatif 302  
- 8.6 Méthodes du second ordre approximatives 307  
- 8.7 Stratégies d'optimisation et méta-algorithmes 313  

### 9 Réseaux convolutionnels 326

- 9.1 L'opération de convolution 327  
- 9.2 Motivation 329  
- 9.3 Mise en commun (Pooling) 335  
- 9.4 Convolution et pooling comme prior infiniment fort 339  
- 9.5 Variantes de la fonction de convolution de base 342  
- 9.6 Sorties structurées 352  
- 9.7 Types de données 354  
- 9.8 Algorithmes de convolution efficaces 356  
- 9.9 Caractéristiques aléatoires ou non supervisées 356  
- 9.10 Base neuroscientifique des réseaux convolutionnels 358  
- 9.11 Réseaux convolutionnels et historique de l'apprentissage profond 365  

### 10 Modélisation de séquences : Réseaux récurrents et récursifs 367

- 10.1 Dépliement des graphes de calcul 369  
- 10.2 Réseaux de neurones récurrents 372  
- 10.3 RNN bidirectionnels 388  
- 10.4 Architectures encodeur-décodeur séquence à séquence 390  
- 10.5 Réseaux récurrents profonds 392  
- 10.6 Réseaux de neurones récursifs 394  
- 10.7 Le défi des dépendances à long terme 396  
- 10.8 Réseaux à écho (Echo State Networks) 399  
- 10.9 Unités à fuite et autres stratégies pour multiples échelles de temps 402  
- 10.10 LSTM et autres RNN à portes 404  
- 10.11 Optimisation pour les dépendances à long terme 408  
- 10.12 Mémoire explicite 412  

### 11 Méthodologie pratique 416

- 11.1 Métriques de performance  
- 11.2 Modèles de référence par défaut  
- 11.3 Déterminer s'il faut collecter plus de données  
- 11.4 Sélection des hyperparamètres  
- 11.5 Stratégies de débogage  
- 11.6 Exemple : Reconnaissance de nombres à plusieurs chiffres  

## III Recherche en apprentissage profond 482

### 12 Modèles linéaires à facteurs 485

- 12.1 ACP probabiliste et analyse factorielle  
- 12.2 Analyse en composantes indépendantes (ICA)  
- 12.3 Analyse à caractéristiques lentes (Slow Feature Analysis)  
- 12.4 Codage parcimonieux (Sparse Coding)  
- 12.5 Interprétation par variété de l'ACP  

### 13 Autoencodeurs 500

- 13.1 Autoencodeurs sous-complets  
- 13.2 Autoencodeurs régularisés  
- 13.3 Puissance de représentation, taille des couches et profondeur  
- 13.4 Encodeurs et décodeurs stochastiques  
- 13.5 Autoencodeurs débruiteurs  
- 13.6 Apprentissage de variétés avec des autoencodeurs  
- 13.7 Autoencodeurs contractifs  
- 13.8 Décomposition prédictive parcimonieuse  
- 13.9 Applications des autoencodeurs  

### 14 Apprentissage de représentations 525

- 14.1 Pré-entraînement non supervisé couche par couche glouton  
- 14.2 Transfert d'apprentissage et adaptation de domaine  
- 14.3 Démêlage semi-supervisé des facteurs causaux  
- 14.4 Représentation distribuée  
- 14.5 Gains exponentiels de la profondeur  
- 14.6 Fournir des indices pour découvrir les causes sous-jacentes  

### 15 Modèles probabilistes structurés pour l'apprentissage profond 540

- 15.1 Le défi de la modélisation non structurée  
- 15.2 Utilisation de graphes pour décrire la structure du modèle  
- 15.3 Échantillonnage à partir de modèles graphiques  
- 15.4 Avantages de la modélisation structurée  
- 15.5 Apprentissage des dépendances  
- 15.6 Inférence et inférence approximative  
- 15.7 L'approche de l'apprentissage profond pour les modèles probabilistes structurés  

### 16 Méthodes de Monte Carlo 557

- 16.1 Échantillonnage et méthodes de Monte Carlo  
- 16.2 Échantillonnage par importance  
- 16.3 Méthodes de Monte Carlo par chaîne de Markov  
- 16.4 Échantillonnage de Gibbs  
- 16.5 Le défi du mélange entre modes séparés  

### 17 Affronter la fonction de partition 567

- 17.1 Le gradient de la log-vraisemblance  
- 17.2 Maximum de vraisemblance stochastique et divergence contrastive  
- 17.3 Pseudo-vraisemblance  
- 17.4 Appariement des scores (Score Matching) et appariement des ratios (Ratio Matching)  
- 17.5 Appariement des scores par débruitage (Denoising Score Matching)  
- 17.6 Estimation par contraste de bruit (Noise-Contrastive Estimation)  
- 17.7 Estimation de la fonction de partition  

### 18 Inférence approximative 579

- 18.1 Inférence comme optimisation  
- 18.2 Espérance-maximisation  
- 18.3 Inférence MAP et codage parcimonieux  
- 18.4 Inférence et apprentissage variationnels  
- 18.5 Inférence approximative apprise  

### 19 Modèles génératifs profonds 594

- 19.1 Machines de Boltzmann  
- 19.2 Machines de Boltzmann restreintes  
- 19.3 Réseaux de croyance profonds (Deep Belief Networks)  
- 19.4 Machines de Boltzmann profondes  
- 19.5 Machines de Boltzmann pour données à valeurs réelles  
- 19.6 Machines de Boltzmann convolutionnelles  
- 19.7 Machines de Boltzmann pour sorties structurées ou séquentielles  
- 19.8 Autres machines de Boltzmann  
- 19.9 Rétropropagation à travers des opérations aléatoires  
- 19.10 Réseaux génératifs dirigés  
- 19.11 Tirage d'échantillons à partir d'autoencodeurs  
- 19.12 Réseaux génératifs stochastiques  
- 19.13 Autres schémas de génération  
- 19.14 Évaluation des modèles génératifs  
- 19.15 Conclusion  

[Table des matières de Deep Learning](https://www.deeplearningbook.org/contents/toc.html)