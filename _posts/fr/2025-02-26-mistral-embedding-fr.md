---
audio: false
generated: true
lang: fr
layout: post
title: Intégrations Mistral IA
translated: true
type: note
---

Pour fournir des exemples d'incorporation (embeddings) avec Mistral AI, vous pouvez utiliser leur API d'incorporation pour générer des représentations numériques (embeddings) de texte qui capturent la signification sémantique. Ces embeddings sont utiles pour des tâches telles que la détection de similarité, le clustering, la classification ou la recherche. Ci-dessous, je vais démontrer comment générer des embeddings pour un ensemble de phrases et calculer leurs similarités en utilisant le point de terminaison d'incorporation de Mistral AI. Cet exemple s'appuie sur la structure du code fourni mais l'adapte spécifiquement pour les embeddings, comme décrit dans la documentation : [Mistral AI Embeddings](https://docs.mistral.ai/capabilities/embeddings/).

### Prérequis

Avant d'exécuter l'exemple, assurez-vous d'avoir :
1. **Clé API** : Une clé API Mistral AI valide stockée dans la variable d'environnement `MISTRAL_API_KEY`.
2. **Dépendances** : Les packages Python requis installés. Vous pouvez les installer avec :
   ```bash
   pip install requests numpy
   ```

### Exemple de Code

Voici un script Python complet qui génère des embeddings pour trois phrases et calcule leurs similarités deux à deux :

```python
import os
import requests
import numpy as np

def call_mistral_embeddings_api(texts, model="mistral-embed"):
    """
    Appelle l'API d'incorporation de Mistral AI pour générer des embeddings pour une liste de textes.
    
    Args:
        texts (list): Liste de chaînes de caractères à incorporer.
        model (str): Le modèle d'incorporation à utiliser (par défaut : "mistral-embed").
    
    Returns:
        list: Liste de vecteurs d'incorporation, ou None si la requête échoue.
    """
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        print("Error: MISTRAL_API_KEY environment variable not set.")
        return None
    
    url = "https://api.mistral.ai/v1/embeddings"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": model,
        "input": texts
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if response_json and "data" in response_json:
            embeddings = [item["embedding"] for item in response_json["data"]]
            return embeddings
        else:
            print(f"Mistral Embeddings API Error: Invalid response format: {response_json}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Mistral Embeddings API Error: {e}")
        if e.response:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response content: {e.response.text}")
        return None

def calculate_similarity(emb1, emb2):
    """
    Calcule la similarité entre deux embeddings en utilisant le produit scalaire.
    
    Args:
        emb1 (list): Premier vecteur d'incorporation.
        emb2 (list): Deuxième vecteur d'incorporation.
    
    Returns:
        float: Score de similarité (produit scalaire, équivalent à la similarité cosinus pour des vecteurs normalisés).
    """
    return np.dot(emb1, emb2)

if __name__ == "__main__":
    # Exemples de textes à incorporer
    texts = [
        "I love programming in Python.",
        "Python is a great programming language.",
        "The weather is sunny today."
    ]
    
    # Générer les embeddings
    embeddings = call_mistral_embeddings_api(texts)
    if embeddings:
        # Afficher la dimension de l'embedding
        print(f"Embedding dimension: {len(embeddings[0])}")
        
        # Calculer les similarités deux à deux
        sim_12 = calculate_similarity(embeddings[0], embeddings[1])
        sim_13 = calculate_similarity(embeddings[0], embeddings[2])
        sim_23 = calculate_similarity(embeddings[1], embeddings[2])
        
        # Afficher les résultats
        print(f"\nSimilarity Results:")
        print(f"Text 1: '{texts[0]}'")
        print(f"Text 2: '{texts[1]}'")
        print(f"Text 3: '{texts[2]}'")
        print(f"\nSimilarity between Text 1 and Text 2: {sim_12:.4f}")
        print(f"Similarity between Text 1 and Text 3: {sim_13:.4f}")
        print(f"Similarity between Text 2 and Text 3: {sim_23:.4f}")
```

### Comment Exécuter

1. **Définir la Clé API** :
   ```bash
   export MISTRAL_API_KEY="your_api_key_here"
   ```

2. **Sauvegarder et Exécuter** :
   Sauvegardez le script (par exemple, sous le nom `embedding_example.py`) et exécutez-le :
   ```bash
   python embedding_example.py
   ```

### Résultat Attendu

En supposant que l'appel API réussisse, vous verrez un résultat similaire à ceci (les valeurs exactes dépendent des embeddings retournés) :
```
Embedding dimension: 1024

Similarity Results:
Text 1: 'I love programming in Python.'
Text 2: 'Python is a great programming language.'
Text 3: 'The weather is sunny today.'

Similarity between Text 1 and Text 2: 0.9200
Similarity between Text 1 and Text 3: 0.6500
Similarity between Text 2 and Text 3: 0.6700
```

### Explication

- **Point de Terminaison API** : La fonction `call_mistral_embeddings_api` envoie une requête POST à `https://api.mistral.ai/v1/embeddings`, en passant une liste de textes et le modèle `"mistral-embed"`. L'API retourne une réponse JSON contenant les embeddings sous la clé `"data"`.

- **Embeddings** : Chaque embedding est un vecteur de dimension 1024 (selon la documentation de Mistral), représentant le contenu sémantique du texte d'entrée. Les embeddings sont normalisés à une norme de 1.

- **Calcul de Similarité** : Puisque les embeddings sont normalisés, le produit scalaire (`np.dot`) entre deux embeddings équivaut à leur similarité cosinus. Des valeurs plus élevées indiquent une plus grande similarité sémantique :
  - **Texte 1 et Texte 2** : Les deux traitent de la programmation en Python, donc leur similarité devrait être élevée (par exemple, ~0.92).
  - **Texte 1 et Texte 3** : L'un parle de programmation, l'autre de météo, donc leur similarité devrait être plus faible (par exemple, ~0.65).
  - **Texte 2 et Texte 3** : Même schéma, similarité plus faible en raison des sujets différents.

### Cas d'Utilisation Supplémentaires

Les embeddings de Mistral AI peuvent être appliqués au-delà de la détection de similarité :
- **Clustering** : Grouper des textes similaires en utilisant des algorithmes comme K-means (nécessite `scikit-learn`).
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=2).fit(np.array(embeddings))
  print(kmeans.labels_)
  ```
- **Recherche** : Incorporer une requête et trouver le texte le plus similaire :
  ```python
  query = "Tell me about Python."
  query_emb = call_mistral_embeddings_api([query])[0]
  similarities = [calculate_similarity(query_emb, emb) for emb in embeddings]
  most_similar = texts[np.argmax(similarities)]
  print(f"Most similar text: '{most_similar}'")
  ```
- **Classification** : Utiliser les embeddings comme caractéristiques dans un modèle de machine learning.

### Notes

- **Modèle** : Le modèle `"mistral-embed"` est optimisé pour les incorporations. Consultez la [documentation](https://docs.mistral.ai/capabilities/embeddings/) pour les mises à jour ou les modèles supplémentaires.
- **Traitement par Lots** : L'API traite plusieurs textes en un seul appel, améliorant l'efficacité.
- **Applications Avancées** : Pour la recherche de similarité à grande échelle, intégrez avec des bases de données vectorielles comme Faiss ou Milvus.

Cet exemple fournit une introduction pratique à l'utilisation des embeddings Mistral AI, adaptable à la structure du code de complétion de chat fourni en changeant le point de terminaison et le format des données.