---
audio: false
generated: true
lang: fr
layout: post
title: Utiliser CUDA sous Windows
translated: true
type: note
---

Pour utiliser NVIDIA CUDA sur votre HP ZBook Studio 16 G11, vous devrez suivre ces étapes. CUDA permet aux développeurs d'accélérer les applications en exploitant la puissance du GPU pour le traitement parallèle. Voici comment commencer :

### Étape 1 : Vérifier la compatibilité matérielle
- Assurez-vous que votre HP ZBook Studio 16 G11 est équipé d'un GPU NVIDIA compatible. Le ZBook Studio 16 G11 peut être livré avec des GPU comme le NVIDIA RTX 3000 Ada Generation ou supérieur, qui prennent en charge CUDA.

### Étape 2 : Installer les pilotes NVIDIA
- **Télécharger les pilotes :** Rendez-vous sur la [page de téléchargement des pilotes NVIDIA](https://www.nvidia.com/Download/index.aspx) et téléchargez les derniers pilotes pour votre modèle de GPU spécifique.
- **Installer les pilotes :** Exécutez le programme d'installation et suivez les instructions à l'écran pour installer les pilotes sur votre système.

### Étape 3 : Installer le CUDA Toolkit
- **Télécharger le CUDA Toolkit :** Allez sur le [site web du NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) et téléchargez la version du CUDA Toolkit qui correspond à votre système d'exploitation.
- **Installer le CUDA Toolkit :** Exécutez le programme d'installation du CUDA Toolkit et suivez les instructions. Assurez-vous de sélectionner les options appropriées pour votre environnement de développement.

### Étape 4 : Configurer les variables d'environnement
- Pendant le processus d'installation, le programme d'installation devrait configurer automatiquement les variables d'environnement nécessaires. Cependant, vous devrez peut-être ajouter manuellement les binaires CUDA au PATH de votre système si cela n'est pas fait automatiquement.
- Sur Windows, vous pouvez le faire en allant dans `Panneau de configuration > Système et sécurité > Système > Paramètres système avancés > Variables d'environnement` et en ajoutant le chemin vers le répertoire bin de CUDA (par exemple, `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\vX.X\bin`).

### Étape 5 : Vérifier l'installation
- Ouvrez une invite de commande ou un terminal et tapez `nvidia-smi`. Cette commande devrait afficher des informations sur votre GPU, confirmant que les pilotes sont correctement installés.
- Tapez `nvcc --version` pour vérifier la version du compilateur CUDA. Cela confirme que le CUDA Toolkit est correctement installé.

### Étape 6 : Développer et exécuter des applications CUDA
- **Écrire du code CUDA :** Vous pouvez écrire des programmes CUDA en utilisant C, C++, Python ou Fortran. NVIDIA fournit une documentation étendue et des exemples de code pour vous aider à démarrer.
- **Compiler le code CUDA :** Utilisez le compilateur `nvcc` pour compiler vos programmes CUDA. Par exemple, si vous avez un programme CUDA nommé `my_program.cu`, vous pouvez le compiler avec la commande `nvcc my_program.cu -o my_program`.
- **Exécuter le code CUDA :** Exécutez votre programme compilé depuis la ligne de commande. Par exemple, `./my_program` sur Linux ou `my_program.exe` sur Windows.

### Étape 7 : Utiliser les bibliothèques CUDA
- NVIDIA fournit plusieurs bibliothèques optimisées pour CUDA, telles que cuBLAS pour l'algèbre linéaire, cuFFT pour les transformées de Fourier et cuDNN pour les réseaux neuronaux profonds. Vous pouvez inclure ces bibliothèques dans vos projets pour tirer parti de fonctions pré-construites et optimisées.

### Ressources supplémentaires
- **NVIDIA Developer Zone :** Visitez la [NVIDIA Developer Zone](https://developer.nvidia.com/) pour des tutoriels, de la documentation et un support communautaire.
- **Documentation CUDA :** Consultez la [Documentation CUDA](https://docs.nvidia.com/cuda/) pour des informations détaillées sur la programmation CUDA et les bonnes pratiques.

En suivant ces étapes, vous pouvez configurer et commencer à utiliser NVIDIA CUDA sur votre HP ZBook Studio 16 G11 pour accélérer vos applications et tirer parti du calcul GPU.