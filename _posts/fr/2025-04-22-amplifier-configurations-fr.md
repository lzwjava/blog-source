---
audio: false
generated: true
lang: fr
layout: post
title: Configurations d'amplificateur
translated: true
type: note
---

Voici une explication complète des **trois configurations d'amplificateur de base**—l'**Émetteur Commun (CE)**, le **Collecteur Commun (CC)** (aussi appelé **Suiveur d'Émetteur**), et la **Base Commune (CB)**—en se concentrant sur leur structure, leurs caractéristiques de signal, leurs avantages, leurs inconvénients et leurs applications typiques.

---

## 🔷 1. Amplificateur à Émetteur Commun (CE)

### 🔧 Configuration
- **Entrée** : Appliquée entre la base et l'émetteur.
- **Sortie** : Prélevée entre le collecteur et l'émetteur.
- **Terminal commun** : L'émetteur est commun à l'entrée et à la sortie.

### 🔍 Caractéristiques Clés

| Propriété                | Description                       |
|--------------------------|------------------------------------|
| **Gain en Tension**      | Élevé                              |
| **Gain en Courant**      | Modéré à élevé                     |
| **Gain en Puissance**    | Élevé                              |
| **Déphasage**            | 180° (sortie inversée)             |
| **Impédance d'Entrée**   | Modérée                            |
| **Impédance de Sortie**  | Modérée                            |

### ✅ Avantages
- Bon pour l'amplification de tension et de puissance.
- Configuration la plus largement utilisée.

### ❌ Inconvénients
- Inverse le signal (déphasage de 180°).
- Moins adapté pour l'adaptation d'impédance.

### 🧰 Applications
- Amplification de signal généraliste.
- Amplificateurs audio.
- Étages intermédiaires dans les amplificateurs.

---

## 🔷 2. Amplificateur à Collecteur Commun (CC) — *Suiveur d'Émetteur*

### 🔧 Configuration
- **Entrée** : Appliquée entre la base et le collecteur.
- **Sortie** : Prélevée entre l'émetteur et le collecteur.
- **Terminal commun** : Le collecteur est commun.

### 🔍 Caractéristiques Clés

| Propriété                | Description                           |
|--------------------------|----------------------------------------|
| **Gain en Tension**      | Environ 1 (gain unitaire)              |
| **Gain en Courant**      | Élevé                                  |
| **Gain en Puissance**    | Modéré                                 |
| **Déphasage**            | 0° (pas d'inversion)                   |
| **Impédance d'Entrée**   | Élevée                                 |
| **Impédance de Sortie**  | Faible                                 |

### ✅ Avantages
- Excellent étage tampon (buffer).
- Bon pour l'adaptation d'impédance (haute impédance d'entrée, faible impédance de sortie).
- Aucune inversion du signal.

### ❌ Inconvénients
- Aucun gain en tension.
- Ne convient pas comme amplificateur autonome lorsque l'amplification de tension est nécessaire.

### 🧰 Applications
- Tampon entre les étages.
- Pilotage de charges à faible impédance.
- Suiveurs de tension.

---

## 🔷 3. Amplificateur à Base Commune (CB)

### 🔧 Configuration
- **Entrée** : Appliquée entre l'émetteur et la base.
- **Sortie** : Prélevée entre le collecteur et la base.
- **Terminal commun** : La base est commune.

### 🔍 Caractéristiques Clés

| Propriété                | Description                             |
|--------------------------|------------------------------------------|
| **Gain en Tension**      | Élevé                                    |
| **Gain en Courant**      | Inférieur à 1                            |
| **Gain en Puissance**    | Modéré                                   |
| **Déphasage**            | 0° (pas d'inversion)                     |
| **Impédance d'Entrée**   | Très faible                              |
| **Impédance de Sortie**  | Élevée                                   |
| **Réponse en Fréquence** | Très large (bonne pour les hautes fréquences) |

### ✅ Avantages
- Excellente réponse aux hautes fréquences.
- Fonctionnement stable.

### ❌ Inconvénients
- Faible impédance d'entrée — nécessite une conception soigneuse de l'étage de pilotage.
- Gain en courant limité.

### 🧰 Applications
- Amplificateurs RF (radiofréquence).
- Amplification de signaux haute fréquence.
- Adaptation d'impédance (pour sources à faible impédance vers charges à haute impédance).

---

## 🧠 Tableau Récapitulatif

| Configuration            | Gain en Tension | Gain en Courant | Déphasage | Z Entrée | Z Sortie | Application                                |
|--------------------------|-----------------|-----------------|-----------|----------|----------|--------------------------------------------|
| **Émetteur Commun (CE)** | Élevé           | Élevé           | 180°      | Moyenne  | Moyenne  | Amplification générale                     |
| **Collecteur Commun (CC)**| ≈1 (unitaire)   | Élevé           | 0°        | Élevée   | Faible   | Tampon, adaptation d'impédance            |
| **Base Commune (CB)**    | Élevé           | <1              | 0°        | Faible   | Élevée   | Utilisation en hautes fréquences          |

---

Souhaitez-vous des schémas visuels de ces configurations ou une analyse de circuit exemple pour l'une d'entre elles ?