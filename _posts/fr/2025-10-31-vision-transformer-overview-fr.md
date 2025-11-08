---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Aperçu du transformeur de vision
translated: true
type: note
---

### Introduction au Vision Transformer (ViT)

Le Vision Transformer (ViT) est une architecture de réseau neuronal qui adapte le modèle transformer—conçu à l'origine pour le traitement du langage naturel (NLP)—aux tâches de vision par ordinateur, en particulier la classification d'images. Introduit en 2020 par Alexey Dosovitskiy et ses collègues chez Google dans l'article *An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale*, ViT traite les images comme des séquences de patches plutôt que de les traiter avec des réseaux neuronaux convolutifs (CNN) traditionnels. Cela lui permet de tirer parti des forces du transformer dans la gestion des dépendances à longue portée et du calcul parallèle.

ViT a démontré des performances compétitives ou supérieures à celles des CNN sur des jeux de données à grande échelle comme ImageNet, en particulier lorsqu'il est pré-entraîné sur des quantités massives de données (par exemple, JFT-300M). Des variantes comme DeiT (Data-efficient Image Transformers) le rendent plus efficace pour les jeux de données plus petits. Aujourd'hui, des modèles inspirés de ViT alimentent de nombreuses tâches de vision dans des modèles comme DALL-E, Stable Diffusion et les classifieurs modernes.

### Fonctionnement de ViT : Architecture globale et processus

L'idée centrale de ViT est de "tokeniser" une image en une séquence de patches de taille fixe, similaire à la manière dont un texte est décomposé en mots ou tokens. Cette séquence est ensuite traitée par un encodeur transformer standard (pas de décodeur, contrairement aux modèles de texte génératifs). Voici une explication étape par étape de son fonctionnement :

1. **Prétraitement de l'image et extraction des patches** :
   - Commencez avec une image d'entrée de taille \\(H \times W \times C\\) (hauteur × largeur × canaux, par exemple 224 × 224 × 3 pour RVB).
   - Divisez l'image en patches non chevauchants de taille fixe \\(P \times P\\) (par exemple, 16 × 16 pixels). Cela donne \\(N = \frac{HW}{P^2}\\) patches (par exemple, 196 patches pour une image 224×224 avec des patches 16×16).
   - Chaque patch est aplati en un vecteur 1D de longueur \\(P^2 \cdot C\\) (par exemple, 768 dimensions pour 16×16×3).
   - Pourquoi des patches ? Les pixels bruts créeraient une séquence impraticablement longue (par exemple, des millions pour une image haute résolution), donc les patches agissent comme des "mots visuels" pour réduire la dimensionnalité.

2. **Embedding des patches** :
   - Appliquez une projection linéaire apprenable (une simple couche entièrement connectée) à chaque vecteur de patch aplati, le mappant à une dimension d'embedding fixe \\(D\\) (par exemple, 768, correspondant aux transformers de type BERT).
   - Cela produit \\(N\\) vecteurs d'embedding, chacun de taille \\(D\\).
   - Optionnellement, ajoutez un embedding de token [CLS] spécial (un vecteur apprenable de taille \\(D\\)) préfixé à la séquence, similaire à BERT pour les tâches de classification.

3. **Embeddings positionnels** :
   - Ajoutez des embeddings positionnels 1D apprenables aux embeddings des patches pour encoder l'information spatiale (les transformers sont permutation-invariants sans cela).
   - La séquence d'entrée complète est maintenant : \\([ \text{[CLS]}, \text{patch}_1, \text{patch}_2, \dots, \text{patch}_N ] + \text{positions}\\), une matrice de forme \\((N+1) \times D\\).

4. **Blocs de l'encodeur Transformer** :
   - Introduisez la séquence dans \\(L\\) couches d'encodeur transformer empilées (par exemple, 12 couches).
   - Chaque couche consiste en :
     - **Auto-attention multi-têtes (MSA)** : Calcule les scores d'attention entre toutes les paires de patches (y compris [CLS]). Cela permet au modèle de capturer des relations globales, comme "cette oreille du chat est liée à la moustache 100 patches plus loin", contrairement aux champs récepteurs locaux des CNN.
       - Formule : Attention(Q, K, V) = \\(\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V\\), où Q, K, V sont des projections de l'entrée.
     - **Perceptron multicouche (MLP)** : Un réseau feed-forward (deux couches linéaires avec activation GELU) appliqué position par position.
     - Normalisation de couche et connexions résiduelles : Entrée + MSA → Norm → MLP → Norm + Entrée.
   - Sortie : Une séquence d'embeddings raffinés, toujours de forme \\((N+1) \times D\\).

5. **Tête de classification** :
   - Pour la classification d'images, extrayez la sortie du token [CLS] (ou prenez la moyenne de tous les embeddings de patches).
   - Passez-la à travers une simple tête MLP (par exemple, une ou deux couches linéaires) pour produire les logits de classe.
   - Pendant l'entraînement, utilisez la perte d'entropie croisée sur des données étiquetées. Le pré-entraînement implique souvent la prédiction de patches masqués ou d'autres tâches auto-supervisées.

**Hyperparamètres clés** (du modèle ViT-Base original) :
- Taille de patch \\(P\\) : 16
- Dimension d'embedding \\(D\\) : 768
- Couches \\(L\\) : 12
- Têtes : 12
- Paramètres : ~86M

ViT s'adapte bien : Les modèles plus grands (par exemple, ViT-Large avec \\(D=1024\\), \\(L=24\\)) performent mieux mais nécessitent plus de données/de calcul.

**Entraînement et Inférence** :
- **Entraînement** : De bout en bout sur des données étiquetées ; bénéficie énormément d'un pré-entraînement sur des milliards d'images.
- **Inférence** : Passe avant à travers l'encodeur (~O(N²) en temps à cause de l'attention, mais efficace avec des optimisations comme FlashAttention).
- Contrairement aux CNN, ViT n'a pas de biais inductifs comme l'invariance translationnelle—tout est appris.

### Comparaison avec les Transformers de Texte : Similitudes et Différences

ViT est fondamentalement la *même architecture* que la partie encodeur des transformers de texte (par exemple, BERT), mais adaptée pour des données visuelles 2D. Voici une comparaison côte à côte :

| Aspect              | Transformer de Texte (ex. BERT)                  | Vision Transformer (ViT)                       |
|---------------------|------------------------------------------------|------------------------------------------------|
| **Représentation de l'Entrée** | Séquences de tokens (mots/sous-mots) embeddés en vecteurs. | Séquences de patches d'image embeddés en vecteurs. Les patches sont comme des "tokens visuels". |
| **Longueur de Séquence** | Variable (ex. 512 tokens pour une phrase).   | Fixe, basée sur la taille de l'image/la taille des patches (ex. 197 avec [CLS]). |
| **Encodage Positionnel** | 1D (absolu ou relatif) pour l'ordre des mots.     | 1D (apprenable) pour l'ordre des patches (ex. aplatissement row-major). Aucune structure 2D intégrée. |
| **Mécanisme Central**  | Auto-attention sur les tokens pour modéliser les dépendances. | Auto-attention sur les patches—même calcul, mais fait attention aux "relations" spatiales au lieu des relations syntaxiques. |
| **Sortie/Tâches**    | Encodeur pour classification/LM masqué ; décodeur pour la génération. | Encodeur uniquement pour la classification ; peut être étendu pour la détection/segmentation. |
| **Points Forts**       | Gère les dépendances à longue portée dans le texte.         | Contexte global dans les images (ex. compréhension de scène entière). |
| **Points Faibles**      | Nécessite d'énormes corpus textuels.                      | Gourmand en données ; difficultés sur les petits jeux de données sans pré-entraînement CNN. |
| **Style de Prédiction**| Prédiction du token suivant dans les décodeurs (autoregressif). | Aucune prédiction "suivante" intrinsèquement—classifie l'image entière de manière holistique. |

En essence, ViT est un échange "plug-and-play" : Remplacez les embeddings de tokens par des embeddings de patches, et vous obtenez un modèle de vision. Les deux reposent sur l'attention pour pondérer les relations dans une séquence, mais le texte est intrinsèquement séquentiel/linéaire, tandis que les images sont spatiales (ViT apprend cela via l'attention).

### Aborder "Token Suivant" vs. "Pixel Suivant" dans ViT

Non, ViT ne prédit *pas* le "pixel suivant" comme un transformer de texte prédit le "token suivant" dans la génération autoregressive (par exemple, GPT). Voici pourquoi :

- **Transformers de Texte (Autoregressifs)** : Dans des modèles comme GPT, le décodeur génère séquentiellement—un token à la fois, en se conditionnant sur tous les précédents. C'est pixel par pixel pour les images dans certains modèles génératifs (par exemple, PixelRNN), mais inefficace.

- **Approche de ViT** : ViT est *non-autoregressif* et holistique. Il traite l'image *entière* (tous les patches) en parallèle via l'encodeur. Il n'y a pas de prédiction séquentielle "suivante" pendant l'inférence—l'attention calcule les relations entre *tous* les patches simultanément. Pour les tâches de génération (par exemple, l'inpainting), les variantes de ViT peuvent utiliser un décodeur pour prédire les patches masqués de manière autoregressive, mais le ViT de base est pour la classification, pas la génération.

- **Pourquoi pas des Pixels ?** Traiter les pixels individuels comme des tokens ferait exploser la longueur de la séquence (par exemple, 224×224×3 = ~150K tokens), rendant l'attention quadratique informatiquement irréalisable (O(N²) = billions d'opérations). Les patches regroupent ~256 pixels (16×16) en un seul "token", gardant N gérable (~200).

Si vous voulez de la vision générative (comme pixel suivant ou patch suivant), regardez des modèles comme VQ-VAE + Transformer ou Parti, qui s'appuient sur les idées de ViT.

Pour plus de détails, consultez l'article original : [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929). Si vous souhaitez des exemples de code (par exemple, en PyTorch) ou des comparaisons avec des variantes spécifiques, faites-le moi savoir !