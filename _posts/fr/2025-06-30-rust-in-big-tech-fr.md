---
audio: false
generated: true
lang: fr
layout: post
title: L'essor de Rust dans la grande technologie
translated: true
type: note
---

Rust gagne considérablement du terrain dans la grande tech grâce à sa forte concentration sur la sécurité de la mémoire, les performances et la concurrence. De nombreuses grandes entreprises technologiques adoptent Rust pour divers projets critiques. Voici une répartition de quelques exemples notables :

**1. Amazon (AWS)**
* **Firecracker :** Un microVM conçu pour exécuter en toute sécurité des charges de travail de conteneurs à grande échelle, alimentant AWS Lambda et Fargate.
* **AWS Nitro System :** Utilisé pour développer de nouveaux composants, y compris des environnements EC2 sécurisés et isolés.
* **Autres services :** Rust est utilisé dans des composants d'Amazon S3, Amazon EC2, Amazon CloudFront et Amazon Route 53.
* **Bottlerocket :** Un système d'exploitation pour conteneurs basé sur Linux et écrit en Rust.

**2. Microsoft**
* **Composants Windows :** Microsoft réécrit activement des parties de Windows, y compris des composants du noyau, en Rust pour améliorer la sécurité et la maintenabilité.
* **Services Azure :** Rust est intégré dans Azure IoT Edge et Kusto (le moteur de requête et de stockage principal pour Azure Data Explorer).
* **`windows-rs` :** Un projet qui permet d'appeler les API Windows en utilisant Rust.

**3. Meta (Facebook)**
* **Outils de contrôle de source internes :** Meta a reconstruit des parties de son système de contrôle de source interne (Mononoke) en Rust pour gérer son large monorepo avec une meilleure concurrence et une meilleure vitesse.
* **Blockchain Diem (anciennement Libra) :** La blockchain pour ce projet de cryptomonnaie était principalement écrite en Rust.

**4. Google**
* **Android Open Source Project (AOSP) :** Rust est de plus en plus utilisé pour écrire des composants système sécurisés dans Android, réduisant les bogues de mémoire dans des fonctions critiques comme le traitement des médias et l'accès au système de fichiers.
* **Fuchsia OS :** Une proportion significative du code interne de Fuchsia OS est écrite en Rust.
* **Chromium :** Il existe un support expérimental pour Rust dans Chromium.

**5. Dropbox**
* **Moteur de synchronisation :** Rust a remplacé d'anciens codes Python et C++ dans le moteur de synchronisation de fichiers de Dropbox, conduisant à une réduction de l'utilisation du CPU, une meilleure concurrence et une synchronisation plus fluide.
* **Système de stockage de fichiers principal :** Plusieurs composants de leur système de stockage de fichiers principal sont écrits en Rust.

**6. Discord**
* **Services backend :** Discord utilise Rust pour des services backend critiques comme le routage des messages et le suivi de présence, améliorant les performances et la fiabilité. Ils sont passés de Go à Rust pour leur service "Read States" pour éviter les pics de latence.
* **Côtés client et serveur :** Les côtés client et serveur de la base de code de Discord ont des composants Rust.

**7. Cloudflare**
* **Pingora :** Un proxy web haute performance écrit en Rust pour remplacer NGINX, entraînant une réduction de l'utilisation du CPU et une meilleure gestion des connexions.
* **Logique de périphérie principale :** Rust est utilisé dans la logique de périphérie principale de Cloudflare en remplacement de langages non sécurisés pour la mémoire comme le C.
* **Cloudflare Workers :** Prend en charge le déploiement de code serverless avec Rust.

**8. Mozilla**
* **Firefox (Stylo) :** Mozilla, le créateur original de Rust, a utilisé le langage pour construire Stylo, le moteur CSS de Firefox, améliorant significativement les performances et la sécurité.
* **Servo :** Un moteur de navigateur web prototype entièrement construit en Rust.

**9. npm (Node Package Manager)**
* **Services d'authentification :** npm a utilisé Rust pour réécrire des parties de ses services d'authentification afin d'améliorer la sécurité, de gérer la charge et de réduire les délais.

**Autres adoptants et projets notables :**
* **Noyau Linux :** Rust est désormais le deuxième langage officiel pour le développement du noyau Linux, permettant la création de pilotes de périphériques et d'autres modules plus sûrs.
* **Figma :** Leur moteur de synchronisation multijoueur a été réécrit de TypeScript vers Rust pour de meilleures performances.
* **1Password :** Alimente leurs dernières applications de bureau et mobiles avec une seule base de code Rust partagée.
* **Hugging Face :** De nombreux composants de leur écosystème d'IA, y compris `safetensors`, `tokenizer` et `candle`, sont implémentés en utilisant Rust.
* **Polkadot :** Cette plateforme blockchain est entièrement construite en Rust pour la sécurité et la vitesse.
* **Solana :** Une autre plateforme blockchain haute performance qui tire parti de Rust.
* **Navigateur Brave :** Utilise Rust dans certains de ses composants.
* **Atlassian :** Utilise Rust dans un service pour analyser des pétaoctets de code source.
* **Huawei :** A migré des parties de sa base de code vers Rust pour des équipements de télécommunications et des outils d'infrastructure.

L'adoption de Rust par ces grandes entreprises technologiques souligne son importance croissante pour construire des logiciels fiables, efficaces et sécurisés, en particulier pour la programmation au niveau du système, l'infrastructure et les applications haute performance.