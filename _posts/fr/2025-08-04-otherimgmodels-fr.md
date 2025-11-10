---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Autres modèles d'image sur Vertex AI
translated: true
type: note
---

Bien qu'Imagen soit la famille phare de modèles de génération d'images de Google sur Vertex AI, d'autres options sont disponibles, en particulier si vous recherchez des capacités différentes ou des alternatives open-source.

Voici un aperçu des autres modèles liés à l'image que vous pouvez utiliser sur Vertex AI :

### Modèles Gemini (pour les cas d'utilisation multimodaux)
La famille de modèles Gemini est multimodale, ce qui signifie qu'elle peut traiter et comprendre plusieurs types de données, y compris le texte, les images, la vidéo et l'audio. Bien qu'ils soient principalement connus pour leurs sorties textuelles, certains modèles Gemini ont des fonctionnalités spécifiques pour les tâches liées à l'image. Par exemple, certains modèles Gemini peuvent :
* **Générer des images** à partir d'une invite textuelle.
* **Modifier des images** en utilisant des instructions conversationnelles.
* **Effectuer des réponses à des questions visuelles (VQA)**, où vous pouvez poser une question sur une image et recevoir une réponse textuelle.
* **Générer des descriptions** pour une image donnée (légende d'image).

C'est une excellente option si vous construisez une application qui doit gérer à la fois du texte et des images de manière conversationnelle ou intégrée, plutôt que de simplement générer une image à partir d'une invite simple.

### Modèles Open-Source du Model Garden
Le **Model Garden** de Vertex AI est un hub centralisé où vous pouvez découvrir, tester, personnaliser et déployer un large éventail de modèles, y compris les modèles propriétaires de Google et une sélection organisée de modèles open-source. C'est ici que vous trouverez des alternatives à Imagen, telles que :

* **Llama 3-Vision** : Une famille de modèles multimodaux optimisés pour la reconnaissance visuelle, le raisonnement sur image et la génération de légendes.
* **Flux** : Un modèle transformer à flux rectifié qui génère des images de haute qualité à partir de descriptions textuelles.
* **Instant ID** : Un modèle de génération d'images texte-à-image préservant l'identité. Il est utile pour générer de nouvelles images d'une personne ou d'un sujet spécifique tout en conservant ses caractéristiques identitaires clés.

Ces modèles open-source s'accompagnent souvent de conditions de licence, de caractéristiques de performance et d'options de personnalisation différentes, vous offrant ainsi plus de flexibilité pour des cas d'utilisation spécifiques.

### Autres Modèles liés à la Vision
Au-delà de la génération d'images, Vertex AI propose des modèles pré-entraînés pour diverses tâches de vision, que vous pourriez trouver utiles :

* **Embeddings Multimodaux** : Génère des représentations vectorielles d'images, que vous pouvez utiliser pour des tâches comme la recherche d'images (trouver des images similaires), la classification ou le clustering.
* **Vertex AI AutoML Image** : Vous permet d'entraîner vos propres modèles de machine learning personnalisés pour la classification d'images, la détection d'objets et la segmentation d'images sans écrire de code.
* **Modèles vidéo (Veo)** : Bien que ce ne soit pas un modèle d'image, Veo vous permet de générer des vidéos de haute qualité à partir de prompts texte ou image. C'est un outil puissant pour la création de médias qui va au-delà des images fixes.