---
audio: false
generated: true
lang: fr
layout: post
title: Électronique numérique
translated: true
type: note
---

Absolument ! Voici un tutoriel complet et accessible pour **Partie II : Électronique numérique** des *Fondamentaux de la Technologie Électronique (III)*. Cette partie se concentre sur la manière dont les systèmes numériques représentent, traitent et manipulent l'information binaire.

---

## 🔹 Partie II : Électronique Numérique

---

### **5. Fondements des Circuits Numériques**

#### a. **Systèmes de Numération et Codes**
- **Binaire (Base-2)** : Utilise les chiffres 0 et 1. Le plus fondamental pour les systèmes numériques.
- **Octal (Base-8) et Hexadécimal (Base-16)** : Raccourcis pour les groupes binaires (3 ou 4 bits).
- **BCD (Binary-Coded Decimal)** : Chaque chiffre décimal est représenté séparément en binaire (0000–1001).
- **Code Gray** : Un seul bit change à la fois entre des valeurs successives — utilisé dans les codeurs de position.

#### b. **Algèbre de Boole et Portes Logiques**
- **Opérations Booléennes** :
  - **ET** : A·B = 1 si les deux sont à 1
  - **OU** : A + B = 1 si l'un ou l'autre est à 1
  - **NON** : 𝑨̅ = inverse de A
- **Portes Dérivées** :
  - **NON-ET**, **NON-OU**, **OU Exclusif**, **NON-OU Exclusif**
- **Logique Combinatoire** : La sortie dépend uniquement des entrées actuelles.
  - Utiliser les **tables de vérité** et les **Tableaux de Karnaugh (K-Map)** pour la simplification.

#### c. **Circuits Intégrés TTL et CMOS**
- **TTL (Transistor-Transistor Logic)** :
  - Plus rapide mais consomme plus de puissance.
  - Niveau logique 1 : ~5V ; niveau 0 : ~0V.
- **CMOS (Complementary Metal-Oxide-Semiconductor)** :
  - Faible consommation, vitesse plus lente, très courant dans les circuits intégrés modernes.
  - Compatible avec de larges plages de tension.

---

### **6. Circuits Logiques Combinatoires**

#### a. **Analyse et Conception**
- Commencer par une **table de vérité**.
- Déduire une **expression booléenne**.
- La simplifier (en utilisant les lois de Boole ou un K-Map).
- Dessiner le **circuit logique**.

#### b. **Modules Courants**
- **Encodeurs** : Convertissent 2ⁿ lignes d'entrée en une sortie de n bits (ex. : encodeur 8 vers 3).
- **Décodeurs** : Opposé de l'encodeur, utilisé dans le décodage d'adresses mémoire.
- **Multiplexeurs (MUX)** : Sélectionnent une entrée parmi plusieurs.
  - Ex. : MUX 4 vers 1 : 2 lignes de sélection, 4 entrées → 1 sortie.
- **Démultiplexeurs (DEMUX)** : Une entrée est acheminée vers une sortie parmi plusieurs.

#### c. **Aléas (Hazards)**
- **Aléa Statique** : La sortie change momentanément à cause des délais des portes.
- **Aléa Dynamique** : Plusieurs perturbations (glitches) en sortie dues à un décalage temporel.
- **Élimination** : Utiliser une logique redondante ou des conceptions synchrones.

---

### **7. Circuits Logiques Séquentiels**

#### a. **Basculements (Flip-Flops)**
- **Bascule RS** : Set-Reset, mémoire simple.
- **Bascule D** : Bascule Donnée ou à Retard, le plus courant.
- **Bascule JK** : Polyvalent ; évite l'état invalide du RS.
- **Bascule T** : Bascule sur l'horloge ; utilisé dans les compteurs.

#### b. **Compteurs et Registres à Décalage**
- **Compteurs** :
  - **Asynchrone (Ripple)** : L'horloge est propagée séquentiellement ; plus lent.
  - **Synchrone** : Tous les bascules sont horlogés ensemble ; plus rapide.
  - Types : Compteur Croissant, Décroissant, Réversible.
- **Registres à Décalage** :
  - Stockent et décalent les bits en série ou en parallèle.
  - Types : SISO, SIPO, PISO, PIPO.

#### c. **Analyse des Circuits Séquentiels**
- **Tables/Diagrammes d'État** : Montrent les transitions entre les états.
- Utiliser les tables d'excitation des bascules pour analyser et concevoir.
- Le synchrone est plus facile à contrôler et à déboguer que l'asynchrone.

---

### **8. Dispositifs Logiques Programmables (PLD)**

#### a. **Types de PLD**
- **PAL (Programmable Array Logic)** : OU fixe, ET programmable.
- **GAL (Generic Array Logic)** : PAL reprogrammable.
- **FPGA (Field Programmable Gate Array)** :
  - Hautement configurable.
  - Des milliers/millions de blocs logiques.
  - Utilisé dans les systèmes complexes comme le traitement du signal numérique, le traitement vidéo, etc.

#### b. **Introduction au HDL (VHDL/Verilog)**
- **HDL (Hardware Description Language)** :
  - VHDL : Verbeux et fortement typé.
  - Verilog : Syntaxe compacte et similaire au C.
- Utilisé pour modéliser les systèmes numériques à différents niveaux (porte, transfert de registre, comportemental).

#### c. **Exemples de Conception de Systèmes Logiques**
- Exemple 1 : Compteur binaire 4 bits en Verilog.
- Exemple 2 : Contrôleur simple de feux de circulation avec FSM (Finite State Machine).
- Exemple 3 : ALU (Arithmetic Logic Unit) avec des opérations de base.

---

Souhaitez-vous des diagrammes, des tables de vérité ou des extraits de code (par exemple, en Verilog ou VHDL) ? Je peux également vous proposer des problèmes d'entraînement, des aide-mémoire ou des quiz pour réviser. Dites-moi jusqu'où vous voulez aller !