---
audio: false
generated: true
lang: fr
layout: post
title: Fonction Softmax dans l'Apprentissage Profond
translated: true
type: note
---

### Qu'est-ce que Softmax ?

La **fonction Softmax** est une fonction mathématique utilisée en apprentissage automatique, particulièrement en apprentissage profond, pour convertir un vecteur de scores bruts (souvent appelés logits) en une distribution de probabilité. Elle garantit que les valeurs de sortie sont positives et que leur somme est égale à 1, ce qui les rend interprétables comme des probabilités.

La fonction Softmax est définie comme suit pour un vecteur \\( z = [z_1, z_2, \dots, z_n] \\) :

\\[
\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^n e^{z_j}}
\\]

Où :
- \\( z_i \\) : Le score d'entrée (logit) pour la \\( i \\)-ème classe.
- \\( e^{z_i} \\) : L'exponentielle du score d'entrée, qui garantit la positivité.
- \\( \sum_{j=1}^n e^{z_j} \\) : La somme des exponentielles de tous les scores d'entrée, utilisée pour la normalisation.
- La sortie \\( \text{Softmax}(z_i) \\) représente la probabilité de la \\( i \\)-ème classe.

Propriétés clés :
- **Plage de sortie** : Chaque valeur de sortie est comprise entre 0 et 1.
- **Somme à 1** : La somme de toutes les valeurs de sortie est égale à 1, ce qui en fait une distribution de probabilité valide.
- **Amplifie les différences** : La fonction exponentielle dans Softmax met en évidence les valeurs d'entrée plus grandes, rendant les probabilités de sortie plus décisives pour les logits plus importants.

### Application de Softmax en Apprentissage Profond

La fonction Softmax est couramment utilisée dans la **couche de sortie** des réseaux de neurones pour les tâches de **classification multi-classes**. Voici comment elle est appliquée :

1. **Contexte dans les Réseaux de Neurones** :
   - Dans un réseau de neurone, la couche finale produit souvent des scores bruts (logits) pour chaque classe. Par exemple, dans un problème de classification avec 3 classes (ex. : chat, chien, oiseau), le réseau pourrait produire des logits comme \\([2.0, 1.0, 0.5]\\).
   - Ces logits ne sont pas directement interprétables comme des probabilités car ils peuvent être négatifs, non bornés et ne pas sommer à 1.

2. **Rôle de Softmax** :
   - La fonction Softmax transforme ces logits en probabilités. Pour l'exemple ci-dessus :
     \\[
     \text{Softmax}([2.0, 1.0, 0.5]) = \left[ \frac{e^{2.0}}{e^{2.0} + e^{1.0} + e^{0.5}}, \frac{e^{1.0}}{e^{2.0} + e^{1.0} + e^{0.5}}, \frac{e^{0.5}}{e^{2.0} + e^{1.0} + e^{0.5}} \right]
     \\]
     Cela pourrait donner des probabilités comme \\([0.665, 0.245, 0.090]\\), indiquant une probabilité de 66,5 % pour la classe 1 (chat), 24,5 % pour la classe 2 (chien) et 9,0 % pour la classe 3 (oiseau).

3. **Applications** :
   - **Classification multi-classes** : Softmax est utilisée dans des tâches comme la classification d'images (ex. : identifier des objets dans des images), le traitement du langage naturel (ex. : analyse de sentiment avec plusieurs catégories) ou tout problème où une entrée doit être assignée à l'une des plusieurs classes.
   - **Calcul de la perte** : Softmax est généralement associée à la fonction de perte **entropie croisée**, qui mesure la différence entre la distribution de probabilité prédite et la distribution réelle (étiquettes one-hot). Cette perte guide l'entraînement du réseau de neurones.
   - **Prise de décision** : Les probabilités de sortie peuvent être utilisées pour sélectionner la classe la plus probable (ex. : en prenant la classe avec la probabilité la plus élevée).

4. **Exemples en Apprentissage Profond** :
   - **Classification d'Images** : Dans un réseau de neurones convolutif (CNN) comme ResNet, la dernière couche entièrement connectée produit des logits pour chaque classe (ex. : 1000 classes dans ImageNet). Softmax les convertit en probabilités pour prédire l'objet dans une image.
   - **Traitement du Langage Naturel** : Dans des modèles comme les transformers (ex. : BERT), Softmax est utilisée dans la couche de sortie pour des tâches comme la classification de texte ou la prédiction du mot suivant, où des probabilités sont nécessaires sur un vocabulaire ou un ensemble de classes.
   - **Apprentissage par Renforcement** : Softmax peut être utilisée pour convertir des scores d'action en probabilités pour sélectionner des actions dans une méthode basée sur une politique.

5. **Implémentation dans les Frameworks** :
   - Dans des frameworks comme **PyTorch** ou **TensorFlow**, Softmax est souvent implémentée comme une fonction intégrée :
     - PyTorch : `torch.nn.Softmax(dim=1)` ou `torch.nn.functional.softmax()`
     - TensorFlow : `tf.nn.softmax()`
   - De nombreux frameworks combinent Softmax avec la perte d'entropie croisée dans une seule opération (ex. : `torch.nn.CrossEntropyLoss` dans PyTorch) pour la stabilité numérique, car le calcul séparé de Softmax peut entraîner des problèmes comme le débordement avec des logits importants.

### Considérations Pratiques
- **Stabilité Numérique** : Le calcul direct de Softmax peut entraîner un débordement en raison de la fonction exponentielle. Une astuce courante consiste à soustraire la valeur du logit maximum de tous les logits (\\( z_i - \max(z) \\)) avant d'appliquer Softmax, ce qui ne change pas la sortie mais empêche les exponentielles trop grandes.
- **Softmax vs. Sigmoid** : Pour la **classification binaire**, la fonction sigmoïde est souvent utilisée à la place de Softmax, car elle gère deux classes plus efficacement. Softmax généralise la sigmoïde à plusieurs classes.
- **Limitations** :
  - Softmax suppose l'exclusivité mutuelle (une seule classe correcte). Pour la classification multi-labels (où plusieurs classes peuvent être vraies), la sigmoïde est préférée.
  - Softmax peut être excessivement confiante dans ses prédictions en raison de la fonction exponentielle, qui peut amplifier de petites différences dans les logits.

### Exemple de Calcul
Supposons qu'un réseau de neurones produise les logits \\([1.5, 0.8, -0.2]\\) pour un problème à 3 classes :
1. Calculer les exponentielles : \\( e^{1.5} \approx 4.482, e^{0.8} \approx 2.225, e^{-0.2} \approx 0.819 \\).
2. Somme des exponentielles : \\( 4.482 + 2.225 + 0.819 = 7.526 \\).
3. Calculer les probabilités :
   - Classe 1 : \\( \frac{4.482}{7.526} \approx 0.596 \\)
   - Classe 2 : \\( \frac{2.225}{7.526} \approx 0.296 \\)
   - Classe 3 : \\( \frac{0.819}{7.526} \approx 0.109 \\)
4. Sortie : \\([0.596, 0.296, 0.109]\\), une distribution de probabilité valide.

### Visualisation de Softmax
Pour illustrer comment Softmax transforme les logits en probabilités, considérez le graphique suivant montrant les logits et leurs probabilités Softmax correspondantes :

```chartjs
{
  "type": "bar",
  "data": {
    "labels": ["Class 1", "Class 2", "Class 3"],
    "datasets": [
      {
        "label": "Logits",
        "data": [1.5, 0.8, -0.2],
        "backgroundColor": "rgba(75, 192, 192, 0.6)",
        "borderColor": "rgba(75, 192, 192, 1)",
        "borderWidth": 1
      },
      {
        "label": "Softmax Probabilities",
        "data": [0.596, 0.296, 0.109],
        "backgroundColor": "rgba(255, 99, 132, 0.6)",
        "borderColor": "rgba(255, 99, 132, 1)",
        "borderWidth": 1
      }
    ]
  },
  "options": {
    "scales": {
      "y": {
        "beginAtZero": true,
        "title": {
          "display": true,
          "text": "Valeur"
        }
      },
      "x": {
        "title": {
          "display": true,
          "text": "Classes"
        }
      }
    },
    "plugins": {
      "legend": {
        "display": true
      },
      "title": {
        "display": true,
        "text": "Logits vs. Probabilités Softmax"
      }
    }
  }
}
```

Ce graphique compare les logits bruts avec les probabilités après application de Softmax, mettant en évidence comment Softmax normalise les valeurs en une distribution de probabilité.

### Résumé
La fonction Softmax est une pierre angulaire de la classification multi-classes en apprentissage profond, transformant les scores bruts en une distribution de probabilité. Elle est largement utilisée dans les couches de sortie des réseaux de neurones pour des tâches comme la classification d'images et de texte, permettant aux modèles d'attribuer des probabilités à plusieurs classes et de faciliter l'entraînement avec des fonctions de perte comme l'entropie croisée. Sa nature exponentielle la rend sensible aux différences dans les logits, et une implémentation minutieuse garantit la stabilité numérique.