---
audio: false
generated: true
lang: fr
layout: post
title: Georgi Guerganov
translated: true
type: note
---

Georgi Gerganov, un développeur bulgare ayant une formation en physique médicale, est devenu une figure clé dans la démocratisation de l'IA grâce à sa création de **llama.cpp**, une bibliothèque C/C++ très efficace pour exécuter de grands modèles de langage (LLM) comme le LLaMA de Meta AI. Son parcours a commencé par un scepticisme envers les réseaux de neurones, mais sa curiosité technique et son sens de l'optimisation ont conduit à des contributions révolutionnaires dans l'inférence IA sur appareil.

### Parcours et Travaux Précoces
- **Formation et Réussites** : Gerganov a étudié à la Faculté de Physique de l'Université de Sofia, se spécialisant en physique médicale. Il a montré un talent précoce en remportant une médaille d'argent aux Olympiades Internationales de Physique de 2006 et un concours de programmation en 2008 organisé par l'Association Bulgare des Sociétés de Logiciels.
- **Scepticisme Initial envers l'IA** : Avant 2022, Gerganov se décrivait comme un « non-croyant de l'IA », sceptique quant au potentiel des réseaux de neurones, privilégiant une vision conservatrice de la technologie.
- **Whisper.cpp** : Son premier projet d'IA majeur fut **whisper.cpp** (2022), un portage C/C++ de Whisper d'OpenAI, un modèle de reconnaissance vocale. Ce projet, inspiré par un bon timing et de la chance, a optimisé Whisper pour fonctionner sur des CPU, le rendant accessible sur des appareils sans GPU, comme les ordinateurs portables ou même les smartphones. Il a gagné en popularité pour permettre une transcription et une traduction audio efficaces.

### La Naissance de llama.cpp
- **Contexte** : En février 2023, Meta AI a publié LLaMA, une famille de LLM efficaces (de 7B à 65B paramètres) pour la recherche, mais leur exécution nécessitait des ressources computationnelles importantes, typiquement des GPU.
- **Le Défi** : Inspiré par son succès avec whisper.cpp, Gerganov s'est lancé pour faire fonctionner LLaMA sur du matériel grand public, spécifiquement un MacBook, « pour le plaisir ». En mars 2023, il a développé **llama.cpp**, une implémentation minimaliste en C/C++ du code d'inférence de LLaMA sans dépendances externes.
- **Innovation Clé** : Gerganov a tiré parti de sa bibliothèque **GGML** (Georgi Gerganov Model Language), un framework d'algèbre tensorielle en C qu'il a commencé en septembre 2022, inspiré par LibNC de Fabrice Bellard. GGML mettait l'accent sur une gestion stricte de la mémoire et le multi-threading, permettant une inférence efficace sur CPU.
- **Percée de la Quantification** : Une fonctionnalité centrale de llama.cpp était la quantification 4-bit, qui compresse les poids du modèle pour réduire l'utilisation de la mémoire et accélérer l'inférence, avec une perte de précision minimale (par exemple, seulement 4% d'augmentation de la perplexité en 4-bit). Cela a permis au modèle LLaMA 7B de fonctionner sur des appareils avec aussi peu que 4 Go de RAM, y compris les téléphones Android et les Raspberry Pis.

### Impact et Croissance
- **Accessibilité** : llama.cpp a rendu les LLM accessibles aux amateurs et aux développeurs sans matériel spécialisé. Il pouvait fonctionner sur des MacBooks, des téléphones Pixel et même des Raspberry Pi 4 (bien que lentement, à ~1 jeton/seconde). Cela a déclenché une vague d'expérimentations, avec des hackers et des chercheurs exécutant LLaMA sur diverses plateformes.
- **Communauté et Échelle** : Le projet a explosé en popularité, accumulant plus de 69 000 étoiles sur GitHub, plus de 2 600 releases et plus de 900 contributeurs. Sa nature open-source et sa simplicité (par exemple, le backend CUDA dans un seul fichier C++) ont favorisé la collaboration, incluant des fonctionnalités comme la prise en charge de ROCm pour les appareils AMD et l'inférence distribuée via MPI.
- **Format GGUF** : En août 2023, Gerganov a introduit le format **GGUF** (GGML Universal File), succédant à GGML. GGUF a consolidé les poids du modèle, les métadonnées et les tokens dans un seul fichier binaire, prenant en charge la quantification de 2 à 8 bits et assurant la rétrocompatibilité. Cela a encore optimisé le stockage et le chargement des modèles.
- **Support Multimodal** : En octobre 2023, llama.cpp a ajouté la prise en charge de modèles multimodaux comme LLaVA, élargissant son champ d'application au-delà du texte vers des tâches basées sur la vision.

### Contributions Techniques
- **Techniques d'Optimisation** : L'utilisation par Gerganov des instructions vectorielles SIMD (par exemple, AVX2/AVX-512) a transformé les CPU en « mini-GPU » pour les opérations matricielles, boostant les performances. Ses benchmarks sur Apple Silicon ont mis en évidence ses avantages en matière de bande passante mémoire pour l'inférence LLM.
- **Changement Philosophique** : Llama.cpp a déplacé la compétition en IA des performances brutes des modèles vers l'optimisation et l'accessibilité, permettant l'inférence locale et réduisant la dépendance aux GPU basés dans le cloud.
- **IA de Pointe (Edge AI)** : Le projet s'est aligné sur la vision de l'IA sur appareil, avec des expériences comme l'inférence distribuée de LLaMA 65B sur six Raspberry Pis démontrant son potentiel pour une IA décentralisée et à faible coût.

### Influence Plus Large
- **ggml.ai** : Gerganov a fondé **ggml.ai**, soutenu par Nat Friedman et Daniel Gross, pour soutenir le développement de GGML et llama.cpp. L'entreprise embauche des contributeurs pour faire avancer l'inférence sur appareil.
- **Impact Culturel** : Surnommé le « codeur alpha européen » sur X, le développement rapide de Gerganov (par exemple, le piratage de llama.cpp en une soirée) et son éthique open-source en ont fait un héros populaire dans la communauté IA. Son travail a inspiré des comparaisons avec la sortie ouverte de Stable Diffusion, marquant un « moment Stable Diffusion » pour les LLM.
- **Démocratisation** : En permettant aux LLM de fonctionner sur des appareils grand public, llama.cpp a abaissé les barrières à l'expérimentation IA, favorisant l'innovation dans l'IA de pointe et remettant en cause la domination des frameworks centrés sur les GPU.

### L'Histoire dans son Essence
L'histoire de Georgi Gerganov avec llama.cpp est une histoire d'ingéniosité technique et de timing opportun. Parti d'un scepticisme envers l'IA, il a saisi le moment où LLaMA a été publié, appliquant son expertise en C/C++ et en optimisation tensorielle pour faire fonctionner des LLM de pointe sur du matériel quotidien. À travers llama.cpp, il a non seulement résolu un défi technique mais a aussi catalysé un mouvement vers une IA accessible et locale, prouvant qu'un seul développeur de Bulgarie pouvait remodeler le paysage de l'IA. Son travail continue d'évoluer, et llama.cpp reste un témoignage de la puissance de l'innovation open-source.