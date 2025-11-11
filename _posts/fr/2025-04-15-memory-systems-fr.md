---
audio: false
generated: true
lang: fr
layout: post
title: Tutoriel sur les systèmes de mémoire
translated: true
type: note
---

Ce tutoriel couvre les concepts clés des systèmes de mémoire, en se concentrant sur la classification de la mémoire, les principes de la RAM/ROM et les techniques de décodage d'adresse. Décomposons cela en sections complètes.

## 1. Classification de la mémoire

La mémoire de l'ordinateur peut être classée en deux grandes catégories :

### 1.1 Par fonction
- **Mémoire primaire** : Accessible directement par le CPU
  - RAM (Random Access Memory) : Stockage temporaire
  - ROM (Read-Only Memory) : Stockage permanent
- **Mémoire secondaire** : Périphériques de stockage externes (disques durs, SSD, etc.)

### 1.2 Par rétention des données
- **Mémoire volatile** : Perd les données lorsque l'alimentation est coupée (la plupart des RAM)
- **Mémoire non volatile** : Conserve les données sans alimentation (ROM, Flash)

### 1.3 Par méthode d'accès
- **Accès aléatoire** : N'importe quel emplacement peut être accédé directement (RAM, ROM)
- **Accès séquentiel** : Les données sont accédées en séquence (bandes magnétiques)

## 2. Principes de fonctionnement de la RAM

La RAM (Random Access Memory) est la mémoire de travail principale de l'ordinateur.

### 2.1 DRAM (Dynamic RAM)
- Stocke chaque bit dans un minuscule condensateur et un transistor
- Nécessite un rafraîchissement périodique pour maintenir les données (généralement toutes les quelques millisecondes)
- Densité plus élevée, coût inférieur, plus courante dans la mémoire principale
- Cycle d'opération : row address strobe (RAS) → column address strobe (CAS) → accès aux données

### 2.2 SRAM (Static RAM)
- Utilise des circuits bascules pour stocker chaque bit
- N'a pas besoin de rafraîchissement, conserve les données tant que l'alimentation est fournie
- Plus rapide, mais plus chère et de densité inférieure à la DRAM
- Utilisée dans la mémoire cache

### 2.3 Organisation de la RAM
- Organisée sous forme de matrice de lignes et de colonnes
- Chaque cellule a une adresse unique (ligne + colonne)
- Les bits de données sont généralement organisés en longueurs de mots (8, 16, 32, 64 bits)

## 3. Principes de fonctionnement de la ROM

La ROM (Read-Only Memory) stocke des données permanentes ou semi-permanentes.

### 3.1 Types de ROM
- **Mask ROM** : Programmée pendant la fabrication, ne peut pas être modifiée
- **PROM (Programmable ROM)** : Peut être programmée une fois par l'utilisateur
- **EPROM (Erasable PROM)** : Peut être effacée par la lumière UV et reprogrammée
- **EEPROM (Electrically EPROM)** : Peut être effacée et reprogrammée électriquement
- **Flash Memory** : Forme moderne d'EEPROM, permet l'effacement par blocs

### 3.2 Opération de la ROM
- Contient des données pré-écrites au moment de la fabrication ou de la programmation
- Lecture : Adresse → décodeur → amplificateur de détection → tampons de sortie
- Écriture (pour les types inscriptibles) : Une tension plus élevée est utilisée pour modifier les cellules de stockage

## 4. Extension de la mémoire

À mesure que les programmes deviennent plus complexes, l'extension de la mémoire est souvent nécessaire.

### 4.1 Extension de capacité
- **Sélection de puce** : Utilisation de plusieurs puces de mémoire pour augmenter la mémoire totale
- **Extension de la longueur des mots** : Combinaison de puces pour augmenter la largeur du bus de données
- **Extension de l'espace d'adressage** : Augmentation de l'espace mémoire adressable

### 4.2 Banques de mémoire
- Mémoire organisée en banques pouvant être accédées indépendamment
- Permet l'entrelacement, réduisant le temps d'accès moyen
- Facilite les opérations parallèles dans les architectures modernes

## 5. Techniques de décodage d'adresse

Le décodage d'adresse est crucial pour accéder au bon emplacement mémoire.

### 5.1 Sélection linéaire (Décodage complet)
- Chaque ligne d'adresse se connecte directement à un emplacement mémoire
- Simple mais inefficace pour les grands espaces mémoire
- Exemple : Dans un système avec 16 lignes d'adresse, nous avons besoin de 2^16 (65 536) connexions individuelles

### 5.2 Sélection basée sur décodeur
- **Décodeurs d'adresse** : Convertissent l'adresse binaire en signaux de sélection one-hot
- **Décodeur 2-vers-4** : Prend 2 bits d'adresse, active une des 4 lignes de sortie
- **Décodeur 3-vers-8** : Prend 3 bits d'adresse, active une des 8 lignes de sortie
- CI courants : 74LS138 (3-vers-8), 74LS154 (4-vers-16)

### 5.3 Décodage partiel
- Tous les bits d'adresse ne sont pas décodés, économisant du matériel
- Plusieurs emplacements mémoire peuvent correspondre au même emplacement physique
- Crée des "ombres" ou "miroirs" mémoire

### 5.4 Mappage de la mémoire
- **Mappage contigu** : Blocs de mémoire arrangés séquentiellement
- **Mappage paginé** : Mémoire divisée en pages de taille fixe
- **Mappage segmenté** : Mémoire divisée en segments de taille variable

## 6. Exemples de mise en œuvre

### 6.1 Exemple simple d'extension de RAM

Pour étendre un système RAM 32K × 8 à 128K × 8 :
1. Utiliser quatre puces RAM 32K × 8
2. Utiliser 2 bits d'adresse de poids fort pour sélectionner parmi les quatre puces
3. Connecter les lignes d'adresse restantes à toutes les puces en parallèle
4. Utiliser un décodeur 2-vers-4 pour la sélection de puce

### 6.2 Circuit de décodage d'adresse

Pour un système avec de la mémoire mappée dans la plage d'adresses 0x8000-0x9FFF :
1. Les lignes d'adresse A15-A13 doivent être "100" (pour 0x8000-0x9FFF)
2. Utiliser des portes ET pour détecter ce motif
3. Activer la puce de mémoire appropriée lorsque ce motif est détecté

Ceci conclut notre aperçu des systèmes de mémoire, en se concentrant sur la classification, les principes de fonctionnement et les techniques d'extension. La compréhension de ces concepts est fondamentale pour concevoir et travailler efficacement avec les systèmes informatiques.