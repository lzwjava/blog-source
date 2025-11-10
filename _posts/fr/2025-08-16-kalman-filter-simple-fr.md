---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Filtre de Kalman expliqué simplement
translated: true
type: note
---

Voici un **guide complet sur le filtre de Kalman (卡尔曼滤波)** en anglais, structuré pour la clarté :

---

# 1. Introduction

Le **filtre de Kalman** est un **algorithme** qui fournit des estimations de variables inconnues en combinant des mesures bruitées de capteurs avec des prédictions d'un modèle système. Il est largement utilisé dans les **systèmes de contrôle, la navigation, la robotique, la vision par ordinateur et la finance**.

Idée clé :
Il fonctionne de manière récursive — ce qui signifie qu'il met continuellement à jour son estimation à mesure que de nouvelles mesures arrivent, au lieu d'attendre l'ensemble complet des données.

---

# 2. Concepts fondamentaux

### État

L'ensemble des variables que nous souhaitons estimer (par exemple, la position, la vitesse).

### Modèle de processus

Décrit comment l'état évolue dans le temps, généralement avec une certaine incertitude.

### Modèle de mesure

Relie les mesures réelles des capteurs à l'état sous-jacent.

### Bruit

Le processus et les mesures ont tous deux une incertitude (bruit aléatoire). Le filtre de Kalman modélise explicitement cela en utilisant des probabilités.

---

# 3. Formulation mathématique

Le filtre de Kalman suppose un **système linéaire** avec un bruit gaussien.

* **Équation d'état (prédiction) :**

  $$
  x_k = A x_{k-1} + B u_k + w_k
  $$

  * $x_k$ : état au temps $k$
  * $A$ : matrice de transition d'état
  * $B u_k$ : entrée de commande
  * $w_k$ : bruit de processus (gaussien, covariance $Q$)

* **Équation de mesure (observation) :**

  $$
  z_k = H x_k + v_k
  $$

  * $z_k$ : mesure
  * $H$ : matrice d'observation
  * $v_k$ : bruit de mesure (gaussien, covariance $R$)

---

# 4. Les deux étapes principales

### Étape 1 : Prédiction

* Prédire l'état à l'avance dans le temps.
* Prédire l'incertitude (covariance de l'erreur).

### Étape 2 : Mise à jour (Correction)

* Comparer la mesure prédite à la mesure réelle.
* Calculer le **Gain de Kalman** (quantité de confiance à accorder à la mesure par rapport à la prédiction).
* Mettre à jour l'estimation et réduire l'incertitude.

---

# 5. Équations du filtre de Kalman (Cas linéaire)

1. **Prédire l'état :**

   $$
   \hat{x}_k^- = A \hat{x}_{k-1} + B u_k
   $$

2. **Prédire la covariance :**

   $$
   P_k^- = A P_{k-1} A^T + Q
   $$

3. **Gain de Kalman :**

   $$
   K_k = P_k^- H^T (H P_k^- H^T + R)^{-1}
   $$

4. **Mettre à jour l'état :**

   $$
   \hat{x}_k = \hat{x}_k^- + K_k (z_k - H \hat{x}_k^-)
   $$

5. **Mettre à jour la covariance :**

   $$
   P_k = (I - K_k H) P_k^-
   $$

Où :

* $\hat{x}_k^-$ : état prédit avant la mise à jour
* $\hat{x}_k$ : état mis à jour
* $P_k$ : matrice de covariance (incertitude dans l'estimation)

---

# 6. Intuition

* Si la mesure est **très bruitée** (grand $R$), le gain de Kalman devient faible → se fier davantage à la prédiction.
* Si le modèle est **incertain** (grand $Q$), le gain de Kalman augmente → se fier davantage aux mesures.
* Au fil du temps, il trouve le **juste équilibre** entre la confiance dans le modèle et la confiance dans les capteurs.

---

# 7. Variantes

* **Filtre de Kalman étendu (EKF) :** Pour les systèmes non linéaires, utilise la linéarisation (Jacobienne).
* **Filtre de Kalman à sigma-points (UKF) :** Pour les systèmes non linéaires, utilise un échantillonnage déterministe.
* **Filtre d'information :** Travaille avec la covariance inverse pour plus d'efficacité.
* **Filtre de Kalman d'ensemble :** Utilisé dans les prévisions météorologiques et les systèmes de grande dimension.

---

# 8. Applications

* **Navigation :** Fusion GPS + accéléromètre pour le suivi de position.
* **Robotique :** SLAM (Localisation et Cartographie Simultanées).
* **Finance :** Estimation de variables cachées comme la volatilité.
* **Vision par ordinateur :** Suivi d'objets dans les vidéos.
* **Systèmes de contrôle :** Stabilisation d'aéronefs et de véhicules spatiaux.

---

# 9. Exemple de scénario

Imaginez une voiture autonome estimant sa position :

* Le modèle prédit la position en utilisant la vitesse + l'état précédent.
* Le GPS fournit une mesure bruitée de la position.
* Le filtre de Kalman combine la prédiction et le GPS pour obtenir une position plus lisse et plus précise.

Au fil du temps, la voiture peut suivre sa position même si le GPS est brièvement interrompu.

---

# 10. Forces et limites principales

**Forces :**

* Récursif, efficace (n'a besoin que du dernier état, pas de l'historique complet).
* Optimal pour les systèmes linéaires gaussiens.
* Largement testé et robuste.

**Limites :**

* Nécessite des modèles précis de la dynamique et du bruit.
* Purement linéaire — les cas non linéaires nécessitent EKF/UKF.
* Peut diverger si les hypothèses sont violées.

---

✅ En bref : Le **filtre de Kalman** est une manière mathématiquement élégante de fusionner des prédictions et des mesures sous incertitude, équilibrant la confiance entre les modèles et les capteurs pour produire la meilleure estimation possible en temps réel.

---

Souhaitez-vous que je vous donne également un **exemple de mise en œuvre Python étape par étape** (comme le suivi de position avec du bruit), afin que vous puissiez voir comment cela fonctionne en pratique ?