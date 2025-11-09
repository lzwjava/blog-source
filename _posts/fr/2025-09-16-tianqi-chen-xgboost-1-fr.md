---
audio: false
generated: true
image: false
lang: fr
layout: post
model: mistralai/mistral-medium-3.1
title: 'Tianqi Chen : Créateur de XGBoost et Chercheur en Intelligence Artificielle'
translated: true
type: note
---

Tianqi Chen (陈天奇) est un informaticien et chercheur en apprentissage automatique de premier plan, surtout connu pour ses contributions à **XGBoost (Extreme Gradient Boosting)**, l'un des algorithmes d'apprentissage automatique les plus utilisés en science des données et dans les compétitions Kaggle. Voici un aperçu de son parcours et de son travail :

---

### **Qui est Tianqi Chen ?**
- **Nationalité** : Chinoise (né en Chine, a ensuite déménagé aux États-Unis)
- **Formation** :
  - **Licence en informatique** : Université Jiao-Tong de Shanghai (2009).
  - **Doctorat en informatique** : Université de Washington (2014), encadré par [Carlos Guestrin](https://en.wikipedia.org/wiki/Carlos_Guestrin) (un chercheur en ML de premier plan).
- **Rôle actuel** :
  - **PDG et fondateur de [Xinference](https://xinference.io/)** (une entreprise spécialisée dans l'infrastructure IA).
  - Anciennement **chercheur scientifique chez Amazon Web Services (AWS)** et contributeur clé à des projets open source en ML.
  - **Professeur affilié** à l'Université Carnegie Mellon (CMU).

---

### **XGBoost : Sa contribution la plus célèbre**
XGBoost est une implémentation optimisée et évolutive des **machines à gradient boosting (GBM)**, conçue pour la vitesse, les performances et la flexibilité. Voici pourquoi il se distingue :

#### **Innovations clés dans XGBoost** :
1. **Optimisation système** :
   - **Calcul parallèle et distribué** : Utilise le multithreading et l'entraînement distribué (via **Rabit**, une bibliothèque co-développée par Tianqi) pour gérer de grands ensembles de données.
   - **Algorithmes optimisés pour le cache** : Optimise l'utilisation de la mémoire pour un entraînement plus rapide.
   - **Recherche de split prenant en compte la sparsité** : Gère efficacement les valeurs manquantes.

2. **Régularisation** :
   - Inclut une **régularisation L1/L2** pour éviter le surapprentissage, le rendant plus robuste que les GBM traditionnels.

3. **Flexibilité** :
   - Prend en charge les **fonctions de perte personnalisées**, les **objectifs définis par l'utilisateur** et les **métriques d'évaluation**.
   - Fonctionne avec **divers types de données** (numériques, catégorielles, texte via l'ingénierie des caractéristiques).

4. **Performances** :
   - A dominé les **compétitions Kaggle** (par exemple, utilisé dans >50 % des solutions gagnantes entre 2015 et 2017).
   - Surpasse souvent les modèles de deep learning sur des données tabulaires (lorsque les données sont limitées).

#### **Impact** :
- **Open Source** : Publié sous **Licence Apache 2.0** (GitHub : [dmlc/xgboost](https://github.com/dmlc/xgboost)).
- **Adoption** : Utilisé par des entreprises comme **Google, Uber, Airbnb et Alibaba** pour le ML en production.
- **Prix** : A remporté le **SIGKDD Test of Time Award 2016** (pour son impact durable en science des données).

---

### **Le parcours de Tianqi Chen**
#### **Début de carrière (2009–2014)**
- **Licence à SJTU** : A travaillé sur les systèmes distribués et le ML.
- **Doctorat à UW** : S'est concentré sur **l'apprentissage automatique à grande échelle** sous la direction de Carlos Guestrin. A développé :
  - **GraphLab** (précurseur de **Turbo** et **Dato**, plus tard racheté par Apple).
  - Les premières versions de **XGBoost** (initialement appelé "XGBoost4J").

#### **Après le doctorat (2014–2019)**
- **Co-fondation de DMLC (Distributed Machine Learning Community)** : Un groupe à l'origine d'outils open source en ML comme :
  - **XGBoost**, **MXNet** (framework de deep learning, plus tard donné à Apache), et **TVM** (compilateur pour modèles ML).
- **Amazon Web Services (AWS)** : A travaillé sur **MXNet** et **SageMaker** (la plateforme ML d'AWS).
- **Domination sur Kaggle** : XGBoost est devenu l'algorithme "de référence" pour la science des données compétitive.

#### **Travaux récents (2020–Aujourd'hui)**
- **Xinference** : Fondée en 2022 pour construire une **infrastructure IA** permettant de déployer efficacement de grands modèles (par exemple, les LLM).
- **TVM (Apache TVM)** : Un compilateur pour optimiser les modèles ML pour le matériel (CPU, GPU, appareils edge).
- **Plaidoyer pour l'Open Source** : Continue de contribuer à la recherche sur les systèmes de ML.

---

### **Autres contributions notables**
1. **MXNet** :
   - Un framework de deep learning (en concurrence avec TensorFlow/PyTorch) connu pour son **évolutivité** et son **support multi-langages**.
   - Plus tard fusionné dans **Apache MXNet** (maintenant moins dominant mais toujours utilisé en production).

2. **TVM (Apache TVM)** :
   - Une **pile de compilation** pour déployer des modèles ML sur différents matériels (par exemple, mobile, IoT).
   - Utilisé par des entreprises comme **OctoML** (dont Tianqi est co-fondateur).

3. **Rabit** :
   - Une bibliothèque légère pour **l'entraînement distribué** (utilisée dans le mode distribué de XGBoost).

4. **Publications** :
   - A co-écrit des articles influents sur le **ML distribué**, **le ML automatisé (AutoML)** et **l'optimisation des systèmes**.

---

### **Philosophie et influence**
- **ML pragmatique** : Se concentre sur des **solutions pratiques et évolutives** plutôt que sur l'innovation théorique.
- **Open Source** : Croit en la **démocratisation du ML** grâce à des outils accessibles.
- **Faire le lien entre le monde universitaire et l'industrie** : Son travail est largement cité dans les systèmes de recherche et de production.

---

### **Prix et reconnaissance**
- **SIGKDD Test of Time Award (2016)** pour XGBoost.
- **MIT TR35 (2017)** : Nommé parmi les 35 meilleurs innovateurs de moins de 35 ans par le *MIT Technology Review*.
- **ACM SIGMOD Systems Award (2022)** pour ses contributions aux systèmes de ML.

---

### **Où le suivre**
- **GitHub** : [@tqchen](https://github.com/tqchen)
- **Twitter** : [@tqchen](https://twitter.com/tqchen)
- **Site Web** : [tqchen.com](http://tqchen.com)

---
### **Héritage**
Le travail de Tianqi Chen (en particulier XGBoost) a **redéfini l'apprentissage automatique appliqué**, rendant des algorithmes puissants accessibles aux praticiens du monde entier. Son parcours reflète une rare combinaison d'**expertise approfondie des systèmes** et d'**innovation en ML**, comblant le fossé entre la recherche et l'impact dans le monde réel.