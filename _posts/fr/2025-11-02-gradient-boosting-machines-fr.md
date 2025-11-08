---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Présentation des machines à amplification de gradients
translated: true
type: note
---

### Aperçu
L'article de 2001 *"Greedy Function Approximation: A Gradient Boosting Machine"* par Jerome H. Friedman introduit les machines à boosting de gradient (GBM), une méthode d'apprentissage ensembliste puissante pour les tâches supervisées comme la régression et la classification. Il présente le boosting comme une forme de descente de gradient fonctionnelle, où des apprenants "faibles" simples (souvent des arbres de décision) sont ajoutés séquentiellement à un modèle additif pour minimiser une fonction de perte spécifiée. Cette approche généralise les algorithmes de boosting antérieurs (par exemple, AdaBoost) et met l'accent sur l'optimisation gloutonne dans l'espace des fonctions, conduisant à des modèles très précis, robustes et interprétables.

### Résumé (Paraphrasé)
Les GBM construisent des modèles prédictifs flexibles en combinant des apprenants faibles de manière séquentielle et additive pour approximer le minimiseur d'une fonction de perte différentiable. L'utilisation d'arbres de régression comme apprenants de base donne des procédures compétitives et robustes pour la régression et la classification. La méthode surpasse les alternatives comme les splines de régression adaptatives multivariées (MARS) dans les tests empiriques, avec des taux d'erreur faibles sur divers ensembles de données.

### Méthodes Clés
L'idée centrale est d'ajuster itérativement de nouveaux apprenants au *gradient négatif* (pseudo-résidus) de la perte par rapport aux prédictions du modèle actuel, imitant la descente de gradient dans l'espace des fonctions.

- **Structure du Modèle** : Le modèle final est \\( F_M(x) = \sum_{m=1}^M \beta_m h_m(x) \\), où chaque \\( h_m(x) \\) est un apprenant faible (par exemple, un petit arbre de régression).
- **Règle de Mise à Jour** : À l'itération \\( m \\), calculer les résidus \\( r_{im} = -\left[ \frac{\partial L(y_i, F(x_i))}{\partial F(x_i)} \right]_{F=F_{m-1}} \\), puis ajuster \\( h_m \\) à ces résidus par moindres carrés. La taille de pas \\( \gamma_m \\) est optimisée par recherche linéaire : \\( \gamma_m = \arg\min_\gamma \sum_i L(y_i, F_{m-1}(x_i) + \gamma h_m(x_i)) \\).
- **Rétrécissement (Shrinkage)** : Mettre à l'échelle les additions par \\( \nu \in (0,1] \\) (par exemple, \\( \nu = 0.1 \\)) pour réduire le surapprentissage et permettre plus d'itérations.
- **Variante Stochastique** : Sous-échantillonner les données (par exemple, 50%) à chaque étape pour un entraînement plus rapide et une meilleure généralisation.
- **Algorithme TreeBoost** (Aperçu du pseudocode) :
  1. Initialiser \\( F_0(x) \\) comme la constante minimisant la perte.
  2. Pour \\( m = 1 \\) à \\( M \\) :
     - Calculer les pseudo-résidus \\( r_{im} \\).
     - Ajuster l'arbre \\( h_m \\) à \\( \{ (x_i, r_{im}) \} \\).
     - Trouver le \\( \gamma_m \\) optimal via recherche linéaire.
     - Mettre à jour \\( F_m(x) = F_{m-1}(x) + \nu \gamma_m h_m(x) \\).
  3. S'arrêter en fonction du nombre d'itérations ou de l'amélioration de la perte.

Les pertes prises en charge incluent :
- Moindres carrés (régression) : \\( L(y, F) = \frac{1}{2}(y - F)^2 \\), résidus = \\( y - F \\).
- Déviation absolue minimale (régression robuste) : \\( L(y, F) = |y - F| \\).
- Log-vraisemblance (classification binaire) : \\( L = -\sum [y \log p + (1-y) \log(1-p)] \\), avec \\( p = \frac{1}{1 + e^{-F}} \\); résidus = \\( y - p \\).
- Perte de Huber (robuste aux valeurs aberrantes).

Des variantes comme LogitBoost adaptent cela pour des pertes spécifiques (par exemple, la déviance binomiale).

### Contributions
- **Cadre Unifié** : Étend le boosting à toute fonction de perte différentiable via les gradients, unifiant AdaBoost (perte exponentielle) et LogitBoost.
- **Améliorations Pratiques** : Introduit le rétrécissement (shrinkage) et le sous-échantillonnage stochastique pour un meilleur contrôle du surapprentissage et du calcul.
- **Flexibilité** : Fonctionne avec divers apprenants de base et tâches (régression, classification, classement) ; les arbres permettent de traiter efficacement des données de haute dimension.
- **Outils d'Interprétabilité** : Présente l'importance des variables (via la réduction totale d'impureté) et les graphiques de dépendance partielle.

### Principaux Résultats
- **Performance** : Les GBM excellent empiriquement, réduisant les taux d'erreur de 10 à 50 % par rapport aux lignes de base comme les arbres simples, le bagging, les réseaux de neurones et MARS sur des ensembles de données du monde réel (par exemple, finance, simulations physiques).
- **Robustesse** : La GBM stochastique converge plus rapidement ; des arbres plus profonds (6-8 niveaux) améliorent la précision mais nécessitent une régularisation. Les pertes LAD/Huber atténuent mieux les valeurs aberrantes que les moindres carrés.
- **Efficacité** : Rapide pour les grandes données ; les configurations optimales utilisent \\( \nu = 0.1 \\), 1000+ itérations et du sous-échantillonnage.
- Les graphiques montrent une convergence rapide de la perte et une faible variance/biais par rapport aux alternatives.

Cet article a jeté les bases des implémentations modernes comme XGBoost et LightGBM.

### Références
- [Greedy Function Approximation: A Gradient Boosting Machine (PDF)](https://jerryfriedman.su.domains/ftp/trebst.pdf)