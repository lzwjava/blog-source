---
audio: false
generated: true
lang: fr
layout: post
title: Électronique analogique
translated: true
type: note
---

Super ! Voici un tutoriel complet sur **Partie I : Électronique Analogique** tiré de *Fondamentaux de la Technologie Électronique (III)*. Je vais le décomposer section par section avec des explications, des diagrammes (si utiles) et des liens avec le monde réel.

---

## 🔹 Partie I : Électronique Analogique

---

### **1. Fondamentaux de l'Analyse des Circuits**

#### a. **Concepts et Lois de Base des Circuits**
- **Tension (V)** : Différence de potentiel électrique entre deux points.
- **Courant (I)** : Flux de charge électrique ; mesuré en ampères (A).
- **Résistance (R)** : Opposition au courant ; mesurée en ohms (Ω).
- **Puissance (P)** : Énergie utilisée par unité de temps : \\( P = VI \\)

#### ⚡ **Loi d'Ohm**
\\[
V = IR
\\]
Simple et cruciale. Elle relie la tension, le courant et la résistance dans une résistance linéaire.

#### ⚡ **Lois de Kirchhoff**
- **LKC (Loi des Nœuds)** : Le courant total entrant dans un nœud est égal au courant total qui en sort.
  \\[
  \sum I_{entrant} = \sum I_{sortant}
  \\]
- **LKT (Loi des Mailles)** : La somme des tensions autour d'une maille fermée est nulle.
  \\[
  \sum V = 0
  \\]

#### b. **Méthodes d'Analyse des Circuits Linéaires**
- **Analyse Nodale** : Résoudre pour les tensions des nœuds en utilisant la LKC.
  - Choisir un nœud de référence (masse).
  - Écrire les équations de courant à chaque nœud.
- **Théorème de Superposition** :
  - Pour les circuits linéaires avec plusieurs sources, analyser une source à la fois.
  - Remplacer les autres sources de tension par des courts-circuits et les sources de courant par des circuits ouverts.

#### c. **Circuits Dynamiques et Analyse Transitoire**
- **Circuits RC et RL** : Comportement transitoire lors de la mise sous/hors tension.
  - Tension du condensateur : \\( V(t) = V_0 (1 - e^{-t/RC}) \\)
  - Courant de l'inductance : \\( I(t) = I_0 (1 - e^{-t/LR}) \\)
- **Constantes de Temps** : RC ou L/R ; indique la rapidité avec laquelle les circuits réagissent aux changements.

---

### **2. Principes des Circuits Amplificateurs**

#### a. **Composants Semiconducteurs**
- **Diodes** : Permettent au courant de passer dans une seule direction ; utilisées dans les redresseurs.
- **Transistors Bipolaires à Jonction (BJT)** :
  - Trois terminaux : Base, Collecteur, Émetteur.
  - **Mode actif** : Amplifie le courant.
  - **Courbes caractéristiques** : Montrent le courant de sortie en fonction de la tension collecteur-émetteur.

#### b. **Configurations de Base des Amplificateurs**
- **Émetteur Commun (CE)** :
  - Gain élevé.
  - Déphasage : 180°.
- **Collecteur Commun (CC)** (Suiveur d'Émetteur) :
  - Gain unitaire (≈1), mais excellent tampon.
- **Base Commune (CB)** :
  - Impédance d'entrée faible, applications haute fréquence.

#### c. **Réponse en Fréquence et Stabilité**
- **Bande Passante** : Plage de fréquence sur laquelle l'amplificateur fonctionne correctement.
- **Produit Gain-Bande Passante** : Compromis entre le gain et la vitesse.
- **Stabilité** : Éviter les oscillations, souvent contrôlée par la contre-réaction.

---

### **3. Amplificateurs Opérationnels (AOP) et Applications**

#### a. **Caractéristiques des AOP**
- **AOP Idéal** :
  - Gain infini
  - Impédance d'entrée infinie
  - Impédance de sortie nulle
- **Court-Circuit Virtuel** : \\( V_+ = V_- \\) en présence d'une contre-réaction négative.
- **Ouvert Virtuel** : Courant d'entrée ≈ 0

#### b. **Circuits Typiques à AOP**
- **Amplificateur Inverseur** :
  \\[
  V_{sortie} = -\left(\frac{R_f}{R_{entrée}}\right) V_{entrée}
  \\]
- **Amplificateur Non Inverseur** :
  \\[
  V_{sortie} = \left(1 + \frac{R_f}{R_1}\right) V_{entrée}
  \\]
- **Intégrateur/Dérivateur** : Utilise un condensateur dans la contre-réaction ou l'entrée.

#### c. **Applications Non Linéaires**
- **Comparateur** : Compare deux tensions, sort une valeur haute ou basse.
- **Trigger de Schmitt** : Ajoute une hystérésis au comparateur pour l'immunité au bruit.
- **Générateurs de Formes d'Onde** : Crée des signaux carrés, triangulaires ou sinusoïdaux en utilisant des AOP et de la contre-réaction.

---

### **4. Alimentations à Courant Continu**

#### a. **Circuits Redresseurs et Filtres**
- **Redresseur Demi-Onde** : Utilise une diode.
- **Redresseur Double Alternance** : Utilise quatre diodes (pont).
- **Filtre** : Généralement des condensateurs pour lisser la sortie.

#### b. **Régulateurs Linéaires vs. Régulateurs à Découpage**
- **Régulateur Linéaire** :
  - Simple, stable, mais peu efficace (pertes thermiques).
  - Exemple : 7805 (sortie 5V)
- **Régulateur à Découpage** :
  - Utilise une commutation à haute vitesse et des inductances/condensateurs.
  - Haute efficacité.
  - Types : Abaisseur (Buck), Élévateur (Boost), Abaisseur-Élévateur (Buck-Boost).

---

Souhaitez-vous des diagrammes, des exemples de problèmes ou des résumés pour chaque sujet ? Je peux également vous aider à vous tester ou créer une fiche de révision si vous révisez.