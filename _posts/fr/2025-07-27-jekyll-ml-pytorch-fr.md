---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Amélioration du blog Jekyll avec PyTorch
translated: true
type: note
---

### Améliorer votre blog Jekyll avec le ML/IA en utilisant PyTorch

Étant donné que vous utilisez un blog Jekyll (un générateur de site statique), intégrer des fonctionnalités ML/IA comme des recommandations ou de la catégorisation demande un peu de créativité. Jekyll génère du HTML statique, donc les éléments dynamiques (par exemple, des recommandations en temps réel) pourraient nécessiter du JavaScript côté client ou un pré-calcul pendant le processus de build via des plugins ou des scripts Jekyll. Vous avez mentionné vouloir éviter les APIs LLM et vous concentrer sur vos propres réseaux de neurones avec PyTorch—excellent, car cela garde tout local et personnalisable. Je vais décrire des idées pratiques, en me concentrant sur les implémentations PyTorch. Celles-ci supposent que vous avez accès à des bibliothèques de base comme NumPy (pour la manipulation des données) et que vous pouvez gérer le prétraitement de texte manuellement ou avec une simple tokenisation (puisque les bibliothèques NLP avancées comme Hugging Face ne sont pas mentionnées dans votre configuration, mais vous pouvez les ajouter localement si nécessaire).

Vous créerez probablement des scripts Python (par exemple, dans votre répertoire `scripts/`) qui s'exécutent pendant le processus de build de Jekyll (via un hook Makefile ou GitHub Actions si déployé). Par exemple, traitez les articles Markdown dans `_posts/`, générez des données JSON et injectez-les dans votre site via les modèles Liquid.

#### 1. Catégorisation d'articles avec un classifieur PyTorch
Catégorisez automatiquement les articles (par exemple, en sujets comme "ML", "Notes", "Latex") en entraînant un simple classifieur à réseau de neurones. Il s'agit d'un apprentissage supervisé : vous devrez étiqueter manuellement un sous-ensemble de vos articles comme données d'entraînement. Si vous n'avez pas d'étiquettes, commencez par un clustering non supervisé (voir ci-dessous).

**Étapes :**
- **Préparation des données :** Analysez vos fichiers Markdown dans `_posts/`. Extrayez le contenu texte (ignorez le frontmatter). Créez un jeu de données : une liste de paires (texte, étiquette). Utilisez un CSV ou une liste pour ~50-100 exemples étiquetés initialement.
- **Prétraitement :** Tokenisez le texte (simple split sur les espaces/whitespace), construisez un vocabulaire, convertissez en indices numériques. Utilisez un encodage one-hot ou des embeddings de base.
- **Modèle :** Un réseau de neurones feedforward de base dans PyTorch pour la classification multi-classes.
- **Entraînement :** Entraînez sur votre machine locale. Utilisez la perte d'entropie croisée et l'optimiseur Adam.
- **Intégration :** Exécutez le script pendant le build pour classer tous les articles, générez un fichier `categories.json` et utilisez-le dans Jekyll pour étiqueter les pages ou créer des index de catégories.

**Exemple de code PyTorch (dans un script comme `scripts/categorize_posts.py`) :**
```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import os
from collections import Counter

# Étape 1 : Charger et prétraiter les données (simplifié)
def load_posts(posts_dir='_posts'):
    texts = []
    labels = []  # Suppose des étiquettes manuelles : 0=ML, 1=Notes, etc.
    for file in os.listdir(posts_dir):
        if file.endswith('.md'):
            with open(os.path.join(posts_dir, file), 'r') as f:
                content = f.read().split('---')[2].strip()  # Ignorer le frontmatter
                texts.append(content)
                # Espace réservé : charger l'étiquette depuis un dict ou CSV
                labels.append(0)  # Remplacer par les étiquettes réelles
    return texts, labels

texts, labels = load_posts()
# Construire le vocabulaire (top 1000 mots)
all_words = ' '.join(texts).lower().split()
vocab = {word: idx for idx, word in enumerate(Counter(all_words).most_common(1000))}
vocab_size = len(vocab)

# Convertir le texte en vecteurs (bag-of-words)
def text_to_vec(text):
    vec = np.zeros(vocab_size)
    for word in text.lower().split():
        if word in vocab:
            vec[vocab[word]] += 1
    return vec

X = np.array([text_to_vec(t) for t in texts])
y = torch.tensor(labels, dtype=torch.long)

# Étape 2 : Définir le modèle
class Classifier(nn.Module):
    def __init__(self, input_size, num_classes):
        super().__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, num_classes)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

model = Classifier(vocab_size, num_classes=3)  # Ajuster num_classes

# Étape 3 : Entraînement
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()
X_tensor = torch.tensor(X, dtype=torch.float32)

for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X_tensor)
    loss = loss_fn(outputs, y)
    loss.backward()
    optimizer.step()
    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# Étape 4 : Inférence sur un nouvel article
def classify_post(text):
    vec = torch.tensor(text_to_vec(text), dtype=torch.float32).unsqueeze(0)
    with torch.no_grad():
        pred = model(vec).argmax(1).item()
    return pred  # Convertir en nom de catégorie

# Sauvegarder le modèle : torch.save(model.state_dict(), 'classifier.pth')
# Dans le script de build : classer tous les articles et écrire en JSON
```

**Améliorations :** Pour une meilleure précision, utilisez des word embeddings (entraînez une simple couche Embedding dans PyTorch) ou ajoutez plus de couches. Si non étiqueté, passez au clustering (par exemple, KMeans sur les embeddings—voir section suivante). Exécutez ce script dans votre Makefile : `jekyll build && python scripts/categorize_posts.py`.

#### 2. Système de recommandation avec les embeddings PyTorch
Recommandez des articles similaires aux lecteurs (par exemple, "Vous aimerez peut-être aussi..."). Utilisez une recommandation basée sur le contenu : apprenez des embeddings pour chaque article, puis calculez la similarité (distance cosinus). Aucune donnée utilisateur n'est nécessaire—juste le contenu des articles.

**Étapes :**
- **Données :** Identique à ci-dessus—extrayez le texte des articles.
- **Modèle :** Entraînez un autoencodeur dans PyTorch pour compresser le texte en embeddings de faible dimension (par exemple, des vecteurs de 64 dimensions).
- **Entraînement :** Minimisez la perte de reconstruction pour apprendre des représentations significatives.
- **Recommandations :** Pour un article donné, trouvez les plus proches voisins dans l'espace des embeddings.
- **Intégration :** Précalculez les embeddings pendant le build, stockez-les en JSON. Utilisez JS sur le site pour afficher les recommandations (ou Liquid pour des listes statiques).

**Exemple de code PyTorch (dans `scripts/recommend_posts.py`) :**
```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
# Réutiliser load_posts et text_to_vec depuis ci-dessus

texts, _ = load_posts()  # Ignorer les étiquettes
X = np.array([text_to_vec(t) for t in texts])
X_tensor = torch.tensor(X, dtype=torch.float32)

# Modèle autoencodeur
class Autoencoder(nn.Module):
    def __init__(self, input_size, embedding_size=64):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_size, 256),
            nn.ReLU(),
            nn.Linear(256, embedding_size)
        )
        self.decoder = nn.Sequential(
            nn.Linear(embedding_size, 256),
            nn.ReLU(),
            nn.Linear(256, input_size)
        )
    
    def forward(self, x):
        emb = self.encoder(x)
        return self.decoder(emb)

model = Autoencoder(vocab_size)
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.MSELoss()

for epoch in range(200):
    optimizer.zero_grad()
    reconstructed = model(X_tensor)
    loss = loss_fn(reconstructed, X_tensor)
    loss.backward()
    optimizer.step()
    if epoch % 20 == 0:
        print(f'Epoch {epoch}, Loss: {loss.item()}')

# Obtenir les embeddings
with torch.no_grad():
    embeddings = model.encoder(X_tensor).numpy()

# Recommander : pour l'article i, trouver les 3 plus similaires
similarities = cosine_similarity(embeddings)
for i in range(len(texts)):
    rec_indices = similarities[i].argsort()[-4:-1][::-1]  # Top 3 excluant soi-même
    print(f'Recs pour l article {i}: {rec_indices}')

# Sauvegarder les embeddings en JSON pour Jekyll
import json
with open('embeddings.json', 'w') as f:
    json.dump({'embeddings': embeddings.tolist(), 'posts': [f'post_{i}' for i in range(len(texts))]}, f)
```

**Améliorations :** Utilisez un autoencodeur variationnel pour de meilleurs embeddings. Si vous avez des données de vues utilisateur (via analytics), ajoutez du filtrage collaboratif avec un modèle de factorisation de matrice dans PyTorch. Côté client : Chargez le JSON en JS et calculez les similarités à la volée pour la personnalisation.

#### 3. Autres idées avec PyTorch
- **Clustering non supervisé pour l'auto-étiquetage :** Si l'étiquetage est fastidieux, utilisez les embeddings (de l'autoencodeur ci-dessus) + le clustering KMeans pour grouper les articles par sujets. PyTorch pour les embeddings, NumPy/SciPy pour le clustering.
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=5)
  clusters = kmeans.fit_predict(embeddings)
  # Assigner des étiquettes basées sur les clusters
  ```
  Intégration : Générez les étiquettes dans le frontmatter via un script.

- **Amélioration de la recherche sémantique :** Embeddez les requêtes et les articles de manière similaire, puis utilisez la similarité cosinus pour une barre de recherche. Précalculez les embeddings des articles ; utilisez JS pour l'embedding des requêtes (mais puisque PyTorch est en Python, exportez le modèle vers ONNX pour l'inférence JS via ONNX.js, ou gardez la recherche statique).

- **Résumé d'article :** Entraînez un modèle seq2seq (RNN/LSTM dans PyTorch) sur des données appariées (texte complet, résumé manuel). Difficile sans grands jeux de données, mais commencez petit avec vos articles. Utilisez pour générer des extraits.

**Conseils généraux :**
- **Évolutivité :** Pour un petit blog, entraînez sur le CPU ; PyTorch le gère bien. Sauvegardez les modèles avec `torch.save` et chargez-les pour l'inférence.
- **Intégration au build :** Ajoutez au Makefile : `train: python scripts/train_models.py` puis `build: jekyll build && python scripts/generate_features.py`.
- **Limitations :** Sans NLP avancé (par exemple, transformers), les résultats sont basiques—envisagez d'ajouter `torchtext` ou des embeddings GloVe manuels localement. Testez sur vos répertoires `ml/` ou `notes/`.
- **Déploiement :** Si sur GitHub Pages, exécutez les scripts en CI. Pour des éléments dynamiques, envisagez d'ajouter un backend Flask léger, mais cela s'écarte de Jekyll statique.

Si vous partagez plus de détails (par exemple, nombre d'articles, sujets), je peux affiner cela !