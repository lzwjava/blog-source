---
audio: false
generated: true
lang: fr
layout: post
title: Arbre de décision
translated: true
type: note
---

Un **arbre de décision** est un outil de modélisation prédictive utilisé en apprentissage automatique et en analyse de données pour prendre des décisions basées sur des données d'entrée. Il représente les décisions et leurs conséquences possibles, y compris les résultats d'événements aléatoires, dans une structure arborescente. Les arbres de décision sont largement utilisés pour des tâches comme la classification (par exemple, prédire si un client achètera un produit) et la régression (par exemple, prédire le prix des maisons). Ils sont intuitifs, faciles à interpréter et efficaces pour des ensembles de données simples et complexes.

Ce guide complet expliquera ce qu'est un arbre de décision, comment il fonctionne, ses composants, son processus de construction, ses avantages, ses limites et les considérations pratiques, accompagnés d'exemples.

---

### **Qu'est-ce qu'un Arbre de Décision ?**

Un arbre de décision est une représentation, semblable à un organigramme, des décisions et de leurs résultats possibles. Il se compose de nœuds et de branches :
- **Nœuds** : Représentent les décisions, les conditions ou les résultats.
- **Branches** : Représentent les résultats possibles d'une décision ou d'une condition.
- **Feuilles** : Représentent la sortie finale (par exemple, une étiquette de classe pour la classification ou une valeur numérique pour la régression).

Les arbres de décision sont utilisés en apprentissage supervisé, où le modèle apprend à partir de données d'entraînement étiquetées pour prédire les résultats pour de nouvelles données invisibles. Ils sont polyvalents et peuvent gérer à la fois des données catégorielles et numériques.

---

### **Composants d'un Arbre de Décision**

1. **Nœud Racine** :
   - Le nœud le plus haut de l'arbre.
   - Représente l'ensemble complet des données et le point de décision initial.
   - Il se divise en fonction de la caractéristique qui fournit le plus d'informations ou réduit le plus l'incertitude.

2. **Nœuds Internes** :
   - Nœuds situés entre la racine et les feuilles.
   - Représentent des points de décision intermédiaires basés sur des caractéristiques et des conditions spécifiques (par exemple, "L'âge > 30 ?").

3. **Branches** :
   - Connexions entre les nœuds.
   - Représentent le résultat d'une décision ou d'une condition (par exemple, "Oui" ou "Non" pour une division binaire).

4. **Nœuds Feuilles** :
   - Nœuds terminaux qui représentent la sortie finale.
   - En classification, les feuilles représentent les étiquettes de classe (par exemple, "Acheter" ou "Ne pas acheter").
   - En régression, les feuilles représentent des valeurs numériques (par exemple, un prix prédit).

---

### **Comment Fonctionne un Arbre de Décision ?**

Un arbre de décision fonctionne en divisant récursivement les données d'entrée en régions basées sur les valeurs des caractéristiques, puis en prenant une décision basée sur la classe majoritaire ou la valeur moyenne dans cette région. Voici une explication étape par étape de son fonctionnement :

1. **Données d'Entrée** :
   - L'ensemble de données contient des caractéristiques (variables indépendantes) et une variable cible (variable dépendante).
   - Par exemple, dans un ensemble de données prédisant si un client achètera un produit, les caractéristiques pourraient inclure l'âge, le revenu et le temps de navigation, la cible étant "Acheter" ou "Ne pas acheter".

2. **Division des Données** :
   - L'algorithme sélectionne une caractéristique et un seuil (par exemple, "Âge > 30") pour diviser les données en sous-ensembles.
   - L'objectif est de créer des divisions qui maximisent la séparation des classes (pour la classification) ou minimisent la variance (pour la régression).
   - Les critères de division incluent des métriques comme **l'impureté de Gini**, le **Gain d'Information** ou la **Réduction de la Variance** (expliqués ci-dessous).

3. **Division Récursive** :
   - L'algorithme répète le processus de division pour chaque sous-ensemble, créant de nouveaux nœuds et branches.
   - Cela continue jusqu'à ce qu'un critère d'arrêt soit atteint (par exemple, profondeur maximale, nombre minimum d'échantillons par nœud, ou aucune amélioration supplémentaire).

4. **Attribution des Sorties** :
   - Une fois la division arrêtée, chaque nœud feuille se voit attribuer une sortie finale.
   - Pour la classification, la feuille représente la classe majoritaire dans cette région.
   - Pour la régression, la feuille représente la moyenne (ou la médiane) des valeurs cibles dans cette région.

5. **Prédiction** :
   - Pour prédire le résultat pour un nouveau point de données, l'arbre parcourt de la racine à une feuille, en suivant les règles de décision basées sur les valeurs des caractéristiques du point de données.
   - Le nœud feuille fournit la prédiction finale.

---

### **Critères de Division**

La qualité d'une division détermine la capacité de l'arbre à séparer les données. Les critères courants incluent :

1. **Impureté de Gini (Classification)** :
   - Mesure l'impureté d'un nœud (à quel point les classes sont mélangées).
   - Formule : \( \text{Gini} = 1 - \sum_{i=1}^n (p_i)^2 \), où \( p_i \) est la proportion de la classe \( i \) dans le nœud.
   - Une impureté de Gini plus faible indique une meilleure division (nœud plus homogène).

2. **Gain d'Information (Classification)** :
   - Basé sur **l'entropie**, qui mesure le caractère aléatoire ou l'incertitude dans un nœud.
   - Entropie : \( \text{Entropie} = - \sum_{i=1}^n p_i \log_2(p_i) \).
   - Gain d'Information = Entropie avant la division - Entropie moyenne pondérée après la division.
   - Un gain d'information plus élevé indique une meilleure division.

3. **Réduction de la Variance (Régression)** :
   - Mesure la réduction de la variance de la variable cible après une division.
   - Variance : \( \text{Variance} = \frac{1}{n} \sum_{i=1}^n (y_i - \bar{y})^2 \), où \( y_i \) est une valeur cible et \( \bar{y} \) est la moyenne.
   - L'algorithme sélectionne la division qui maximise la réduction de la variance.

4. **Chi-Carré (Classification)** :
   - Teste si la division améliore significativement la distribution des classes.
   - Utilisé dans certains algorithmes comme CHAID.

L'algorithme évalue toutes les divisions possibles pour chaque caractéristique et sélectionne celle avec le meilleur score (par exemple, l'impureté de Gini la plus faible ou le gain d'information le plus élevé).

---

### **Comment un Arbre de Décision est-il Construit ?**

La construction d'un arbre de décision implique les étapes suivantes :

1. **Sélectionner la Meilleure Caractéristique** :
   - Évaluez toutes les caractéristiques et tous les points de division possibles en utilisant le critère choisi (par exemple, Gini, Gain d'Information).
   - Choisissez la caractéristique et le seuil qui séparent le mieux les données.

2. **Diviser les Données** :
   - Divisez l'ensemble de données en sous-ensembles basés sur la caractéristique et le seuil sélectionnés.
   - Créez des nœuds enfants pour chaque sous-ensemble.

3. **Répéter Récursivement** :
   - Appliquez le même processus à chaque nœud enfant jusqu'à ce qu'une condition d'arrêt soit atteinte :
     - Profondeur maximale de l'arbre atteinte.
     - Nombre minimum d'échantillons dans un nœud.
     - Aucune amélioration significative du critère de division.
     - Tous les échantillons d'un nœud appartiennent à la même classe (pour la classification) ou ont des valeurs similaires (pour la régression).

4. **Élaguer l'Arbre (Optionnel)** :
   - Pour éviter le surajustement, réduisez la complexité de l'arbre en supprimant les branches qui contribuent peu à la précision prédictive.
   - L'élagage peut être **pré-élagage** (arrêt précoce pendant la construction) ou **post-élagage** (suppression des branches après la construction).

---

### **Exemple : Arbre de Décision de Classification**

**Ensemble de données** : Prédire si un client achètera un produit basé sur l'Âge, le Revenu et le Temps de Navigation.

| Âge | Revenu | Temps de Navigation | Acheter ? |
|-----|--------|---------------------|-----------|
| 25  | Faible | Court               | Non       |
| 35  | Élevé  | Long                | Oui       |
| 45  | Moyen  | Moyen               | Oui       |
| 20  | Faible | Court               | Non       |
| 50  | Élevé  | Long                | Oui       |

**Étape 1 : Nœud Racine** :
- Évaluez toutes les caractéristiques (Âge, Revenu, Temps de Navigation) pour la meilleure division.
- Supposons que "Revenu = Élevé" donne le Gain d'Information le plus élevé.
- Divisez les données :
  - Revenu = Élevé : Tous "Oui" (nœud pur, arrêtez ici).
  - Revenu = Faible ou Moyen : Mixte (continuez la division).

**Étape 2 : Nœud Enfant** :
- Pour le sous-ensemble "Revenu Faible ou Moyen", évaluez les caractéristiques restantes.
- Supposons que "Âge > 30" donne la meilleure division :
  - Âge > 30 : Principalement "Oui".
  - Âge ≤ 30 : Tous "Non".

**Étape 3 : Arrêt** :
- Tous les nœuds sont purs (contiennent une seule classe) ou répondent aux critères d'arrêt.
- L'arbre ressemble à :
  - Racine : "Le revenu est-il élevé ?"
    - Oui → Feuille : "Acheter"
    - Non → "L'âge > 30 ?"
      - Oui → Feuille : "Acheter"
      - Non → Feuille : "Ne pas acheter"

**Prédiction** :
- Nouveau client : Âge = 40, Revenu = Moyen, Temps de Navigation = Court.
- Chemin : Revenu ≠ Élevé → Âge = 40 > 30 → Prédire "Acheter".

---

### **Exemple : Arbre de Décision de Régression**

**Ensemble de données** : Prédire le prix des maisons basé sur la Taille et l'Emplacement.

| Taille (m²) | Emplacement | Prix (k€) |
|-------------|-------------|-----------|
| 1000        | Urbain      | 300       |
| 1500        | Périurbain  | 400       |
| 2000        | Urbain      | 600       |
| 800         | Rural       | 200       |

**Étape 1 : Nœud Racine** :
- Évaluez les divisions (par exemple, Taille > 1200, Emplacement = Urbain).
- Supposons que "Taille > 1200" minimise la variance.
- Division :
  - Taille > 1200 : Prix = {400, 600} (moyenne = 500).
  - Taille ≤ 1200 : Prix = {200, 300} (moyenne = 250).

**Étape 2 : Arrêt** :
- Les nœuds sont suffisamment petits ou la réduction de variance est minimale.
- Arbre :
  - Racine : "Taille > 1200 ?"
    - Oui → Feuille : Prédire 500 k€.
    - Non → Feuille : Prédire 250 k€.

**Prédiction** :
- Nouvelle maison : Taille = 1800, Emplacement = Urbain → Taille > 1200 → Prédire 500 k€.

---

### **Avantages des Arbres de Décision**

1. **Interprétabilité** :
   - Faciles à comprendre et à visualiser, ce qui les rend idéaux pour expliquer les décisions à des parties prenantes non techniques.
2. **Gère les Données Mixtes** :
   - Fonctionne avec des caractéristiques catégorielles et numériques sans prétraitement extensif.
3. **Non Paramétrique** :
   - Aucune hypothèse sur la distribution sous-jacente des données.
4. **Importance des Caractéristiques** :
   - Identifie les caractéristiques qui contribuent le plus aux prédictions.
5. **Prédiction Rapide** :
   - Une fois entraînés, les prédictions sont rapides car elles impliquent de simples comparaisons.

---

### **Limitations des Arbres de Décision**

1. **Surajustement** :
   - Les arbres profonds peuvent mémoriser les données d'entraînement, conduisant à une mauvaise généralisation.
   - Solution : Utiliser l'élagage, limiter la profondeur maximale ou définir un nombre minimum d'échantillons par nœud.
2. **Instabilité** :
   - De petits changements dans les données peuvent conduire à des arbres entièrement différents.
   - Solution : Utiliser des méthodes d'ensemble comme les Forêts Aléatoires ou le Gradient Boosting.
3. **Biais envers les Classes Dominantes** :
   - Difficultés avec les ensembles de données déséquilibrés où une classe domine.
   - Solution : Utiliser des techniques comme la pondération des classes ou le suréchantillonnage.
4. **Approche Gourmande** :
   - Les divisions sont choisies sur la base d'une optimisation locale, ce qui peut ne pas conduire à l'arbre globalement optimal.
5. **Mauvaise Gestion des Relations Linéaires** :
   - Moins efficaces pour les ensembles de données où les relations entre les caractéristiques et la cible sont linéaires ou complexes.

---

### **Considérations Pratiques**

1. **Hyperparamètres** :
   - **Profondeur Max** : Limite la profondeur de l'arbre pour éviter le surajustement.
   - **Échantillons Min par Division** : Nombre minimum d'échantillons requis pour diviser un nœud.
   - **Échantillons Min par Feuille** : Nombre minimum d'échantillons dans un nœud feuille.
   - **Caractéristiques Max** : Nombre de caractéristiques à considérer pour chaque division.

2. **Élagage** :
   - Pré-élagage : Définir des contraintes pendant la construction de l'arbre.
   - Post-élagage : Supprimer les branches après la construction de l'arbre basé sur les performances de validation.

3. **Gestion des Valeurs Manquantes** :
   - Certains algorithmes (par exemple, CART) attribuent les valeurs manquantes à la branche qui minimise l'erreur.
   - Alternativement, imputer les valeurs manquantes avant l'entraînement.

4. **Évolutivité** :
   - Les arbres de décision sont efficaces sur le plan computationnel pour les petits à moyens ensembles de données, mais peuvent être lents pour les très grands ensembles de données avec de nombreuses caractéristiques.

5. **Méthodes d'Ensemble** :
   - Pour surmonter les limitations, les arbres de décision sont souvent utilisés dans des ensembles :
     - **Forêt Aléatoire** : Combine plusieurs arbres entraînés sur des sous-ensembles aléatoires de données et de caractéristiques.
     - **Gradient Boosting** : Construit des arbres séquentiellement, chacun corrigeant les erreurs des précédents.

---

### **Applications des Arbres de Décision**

1. **Entreprise** :
   - Prédiction de l'attrition des clients, scoring de crédit, segmentation marketing.
2. **Santé** :
   - Diagnostic de maladie, prédiction des risques (par exemple, maladie cardiaque).
3. **Finance** :
   - Détection de fraude, prédiction de défaut de prêt.
4. **Traitement du Langage Naturel** :
   - Classification de texte (par exemple, analyse de sentiment).
5. **Tâches de Régression** :
   - Prédiction de résultats continus comme les prix des maisons ou les prévisions de ventes.

---

### **Exemple de Visualisation**

Pour illustrer comment un arbre de décision divise les données, considérons un simple ensemble de données de classification avec deux caractéristiques (par exemple, Âge et Revenu) et deux classes (Acheter, Ne pas acheter). Ci-dessous un schéma conceptuel montrant comment l'arbre de décision partitionne l'espace des caractéristiques.

```
chartjs
{
  "type": "scatter",
  "data": {
    "datasets": [
      {
        "label": "Acheter",
        "data": [
          {"x": 35, "y": 50000},
          {"x": 45, "y": 60000},
          {"x": 50, "y": 80000}
        ],
        "backgroundColor": "#4CAF50",
        "pointRadius": 6
      },
      {
        "label": "Ne pas acheter",
        "data": [
          {"x": 20, "y": 20000},
          {"x": 25, "y": 30000}
        ],
        "backgroundColor": "#F44336",
        "pointRadius": 6
      }
    ]
  },
  "options": {
    "scales": {
      "x": {
        "title": { "display": true, "text": "Âge" },
        "min": 15,
        "max": 60
      },
      "y": {
        "title": { "display": true, "text": "Revenu ($)" },
        "min": 10000,
        "max": 100000
      }
    },
    "plugins": {
      "title": { "display": true, "text": "Espace des Caractéristiques d'un Arbre de Décision" },
      "legend": { "display": true }
    }
  }
}
```

Ce graphique montre les points de données dans un espace de caractéristiques 2D. Un arbre de décision pourrait diviser cet espace (par exemple, à Âge = 30 ou Revenu = 40000) pour séparer "Acheter" de "Ne pas acheter".

---

### **Mise en Œuvre en Pratique**

Les arbres de décision peuvent être implémentés en utilisant des bibliothèques comme :
- **Python** : Scikit-learn (`DecisionTreeClassifier`, `DecisionTreeRegressor`), XGBoost, LightGBM.
- **R** : `rpart`, `party`.
- **Autres Outils** : Weka, MATLAB, ou Spark MLlib.

Exemple en Python (Scikit-learn) :
```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Données d'exemple
X = [[25, 20000], [35, 50000], [45, 60000], [20, 30000], [50, 80000]]  # Caractéristiques: Âge, Revenu
y = [0, 1, 1, 0, 1]  # Étiquettes: 0 = Ne pas acheter, 1 = Acheter

# Diviser les données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner l'arbre de décision
clf = DecisionTreeClassifier(max_depth=3, random_state=42)
clf.fit(X_train, y_train)

# Prédire
y_pred = clf.predict(X_test)

# Évaluer
print("Précision :", accuracy_score(y_test, y_pred))
```

---

### **Conclusion**

Les arbres de décision sont des modèles puissants et interprétables pour les tâches de classification et de régression. Ils fonctionnent en divisant récursivement les données basées sur des conditions de caractéristiques, en utilisant des critères comme l'impureté de Gini ou le gain d'information. Bien qu'ils soient faciles à utiliser et à visualiser, ils peuvent surajuster et être instables, ce qui est souvent atténué par l'élagage ou l'utilisation de méthodes d'ensemble comme les Forêts Aléatoires.

Pour approfondir, expérimentez avec les arbres de décision en utilisant de vrais ensembles de données, ajustez les hyperparamètres et combinez-les avec des méthodes d'ensemble pour améliorer les performances. Si vous avez un ensemble de données spécifique ou un cas d'utilisation en tête, je peux fournir un exemple ou une visualisation adaptée !