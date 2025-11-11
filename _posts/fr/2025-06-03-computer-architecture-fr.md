---
audio: false
generated: true
lang: fr
layout: post
title: Déterminer le Type d'Architecture Informatique
translated: true
type: note
---

Pour déterminer si votre ordinateur actuel utilise une architecture x86 64 bits (x64) ou ARM64, suivez ces instructions en fonction de votre système d'exploitation :

**Windows :**

1.  **Appuyez sur la touche Windows + R** pour ouvrir la boîte de dialogue Exécuter.
2.  **Tapez `msinfo32`** et appuyez sur Entrée. Cela ouvrira la fenêtre Informations système.
3.  Dans la fenêtre Informations système, recherchez l'entrée **"Type de système"**.
    * S'il est indiqué **"PC basé sur x64"**, votre ordinateur a un processeur x86 64 bits (x64).
    * S'il est indiqué **"PC basé sur ARM64"**, votre ordinateur a un processeur ARM 64 bits (ARM64).

**macOS :**

1.  Cliquez sur le **menu Pomme** dans le coin supérieur gauche de votre écran.
2.  Sélectionnez **"À propos de ce Mac"**.
3.  Dans l'onglet "Vue d'ensemble", recherchez les informations **"Processeur"** ou **"Puce"** :
    * S'il répertorie un **processeur Intel** (par exemple, Intel Core i7, Intel Core i9), votre Mac a un processeur x86 64 bits (x64).
    * S'il répertorie une **puce Apple silicon** (par exemple, Apple M1, Apple M2, Apple M3), votre Mac a un processeur ARM64.

**Linux :**

1.  Ouvrez une fenêtre **terminal**.
2.  Tapez la commande suivante et appuyez sur Entrée :
    ```bash
    uname -m
    ```
3.  La sortie indiquera l'architecture :
    * **`x86_64`** ou **`amd64`** : Cela indique un processeur x86 64 bits (x64).
    * **`aarch64`** ou **`arm64`** : Cela indique un processeur ARM 64 bits (ARM64).
    * D'autres sorties peuvent indiquer un système 32 bits (bien que moins courant aujourd'hui).

Sur la base des composants que vous avez listés pour votre nouvelle configuration, le processeur **Intel Core i9-13900KF** est un processeur d'architecture **x64 (x86 64 bits)**. Par conséquent, le nouvel ordinateur que vous assemblez sera un **système basé sur x64**.