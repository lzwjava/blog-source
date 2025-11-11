---
audio: false
generated: true
lang: fr
layout: post
title: Comment fonctionne AlphaFold
translated: true
type: note
---

Plongeons dans le fonctionnement d’**AlphaFold**, développé par DeepMind – un système d’IA révolutionnaire qui prédit les structures protéiques avec une précision remarquable. Je vais le décomposer en ses concepts fondamentaux, le problème qu'il résout, son architecture et les étapes qu'il suit pour passer de la séquence d'acides aminés d'une protéine à sa structure 3D. Ce sera complet mais digeste, avec suffisamment de détails pour satisfaire votre curiosité sans vous noyer dans le jargon.

---

### Le Problème : Le Repliement des Protéines

Les protéines sont les chevaux de bataille du vivant, constituées de chaînes d'acides aminés qui se replient en formes 3D spécifiques pour remplir leurs fonctions (par exemple, les enzymes, les anticorps). Le **problème du repliement des protéines** consiste à déterminer comment une séquence d'acides aminés (par exemple, "AGHKL...") se replie en sa structure 3D unique, déterminée par des interactions physiques et chimiques. Traditionnellement, cela était résolu expérimentalement (par exemple, par cristallographie aux rayons X), ce qui est lent et coûteux, ou par calcul, ce qui était imprécis pour les protéines complexes. AlphaFold change la donne en prédisant les structures à partir des seules séquences, rivalisant avec la précision expérimentale.

---

### L'Évolution d'AlphaFold

- **AlphaFold 1 (2018)** : A fait ses débuts à la CASP13 (Critical Assessment of Structure Prediction), utilisant un mélange de machine learning et de modélisation basée sur la physique. C'était performant mais limité.
- **AlphaFold 2 (2020)** : Un bond en avant à la CASP14, atteignant une précision quasi-expérimentale (score GDT_TS médian ~90). Il a largement abandonné l'approche basée sur la physique pour un système entièrement piloté par l'IA.
- **AlphaFold 3 (2024)** : S'étend à la prédiction des interactions protéine-ligand et d'autres biomolécules, mais nous nous concentrerons sur AlphaFold 2, car c'est le plus documenté et fondamental.

---

### Comment AlphaFold (2) Fonctionne : La Vue d'Ensemble

AlphaFold 2 prend une séquence d'acides aminés et produit une structure 3D en :
1. Exploitant les **données évolutives** pour comprendre comment les séquences sont liées aux structures.
2. Utilisant une **architecture de deep learning** pour modéliser les relations spatiales.
3. Affinant itérativement les prédictions pour optimiser la structure.

Il est construit autour de deux composants principaux : un **Evoformer** (traitant les données de séquence et évolutives) et un **Module de Structure** (construisant le modèle 3D). Décomposons cela étape par étape.

---

### Étape 1 : Les Données d'Entrée

AlphaFold commence avec :
- **La Séquence d'Acides Aminés** : La structure primaire de la protéine (par exemple, une chaîne de 100 acides aminés).
- **L'Alignement Multiple de Séquences (MSA)** : Une collection de séquences protéiques apparentées provenant de bases de données évolutives (par exemple, UniProt). Cela montre comment la séquence de la protéine varie selon les espèces, indiquant les régions conservées critiques pour sa structure.
- **Les Structures Modèles** : Structures 3D connues de protéines similaires (optionnelles, provenant de la PDB), bien qu'AlphaFold 2 en dépende moins que son prédécesseur.

Le MSA est crucial – il révèle les **modèles de coévolution**. Si deux acides aminés mutent toujours ensemble, ils sont probablement proches dans la structure repliée, même s'ils sont éloignés dans la séquence.

---

### Étape 2 : L'Evoformer

L'Evoformer est un réseau de neurones de type transformer qui traite les données MSA et de séquence pour construire une représentation riche de la protéine. Voici ce qu'il fait :

1. **Représentation par Paires** :
   - Crée une matrice codant les relations entre chaque paire d'acides aminés (par exemple, distance, probabilité d'interaction).
   - Initialisée à partir des données MSA : les mutations corrélées suggèrent une proximité spatiale.

2. **Représentation de la Séquence** :
   - Suit les caractéristiques de chaque acide aminé (par exemple, propriétés chimiques, position dans la chaîne).

3. **Mécanisme d'Attention** :
   - Utilise l'attention de type transformer pour affiner itérativement ces représentations.
   - Les "lignes" du MSA (séquences évolutives) et les "colonnes" (positions dans la protéine) communiquent via l'attention, capturant les dépendances à longue portée.
   - Voyez cela comme l'IA se demandant : "Quels acides aminés s'influencent mutuellement, et comment ?"

4. **Sortie** :
   - Une **représentation par paires** polie (une carte des relations spatiales probables) et une représentation de séquence mise à jour, prêtes pour la modélisation 3D.

Le génie de l'Evoformer est de distiller des données évolutives complexes sous une forme qui reflète les contraintes physiques sans simuler explicitement la physique.

---

### Étape 3 : Le Module de Structure

Le Module de Structure prend la sortie de l'Evoformer et construit la structure 3D. C'est un système de geometric deep learning qui prédit les positions des atomes (en se concentrant sur le squelette de la protéine : atomes Cα, N, C). Voici comment :

1. **Estimation Initiale** :
   - Commence par une structure 3D approximative pour la protéine, souvent aléatoire ou basée sur des indices de l'Evoformer.

2. **Invariant Point Attention (IPA)** :
   - Un mécanisme d'attention novateur qui respecte la géométrie 3D (les rotations et translations ne le perturbent pas).
   - Met à jour les positions des atomes en considérant les relations par paires provenant de l'Evoformer, garantissant la plausibilité physique (par exemple, angles de liaison, distances).

3. **Affinage Itératif** :
   - Ajuste répétitivement la structure sur plusieurs cycles.
   - Chaque cycle affine les coordonnées, guidé par la représentation par paires et les contraintes géométriques.

4. **Sortie** :
   - Un ensemble de coordonnées 3D pour tous les atomes du squelette de la protéine, plus les chaînes latérales ajoutées ultérieurement.

Le Module de Structure "sculpte" essentiellement la protéine, transformant des relations abstraites en une forme concrète.

---

### Étape 4 : Score de Confiance et Affinage

AlphaFold ne se contente pas de prédire une structure – il vous indique son niveau de confiance :
- **pLDDT (Predicted Local Distance Difference Test)** : Un score de confiance par résidu (0-100). Les scores élevés (par exemple, >90) indiquent des prédictions fiables.
- **Recyclage** : Le modèle réinjecte sa sortie dans l'Evoformer 3 à 5 fois, affinant les prédictions à chaque passage.
- **Dernières Retouches** : Les chaînes latérales sont ajoutées en utilisant une méthode géométrique plus simple, car le squelette dicte leur placement.

---

### Étape 5 : Entraînement et Fonction de Coût

AlphaFold 2 a été entraîné sur :
- **Données de la PDB** : ~170 000 structures protéiques connues.
- **Bases de données MSA** : Des milliards de séquences protéiques.

La fonction de coût d'entraînement combine :
- **FAPE (Frame-Aligned Point Error)** : Mesure à quel point les positions atomiques prédites correspondent à la structure réelle de manière physiquement significative.
- **Pertes Auxiliaires** : Imposent des contraintes comme des longueurs de liaison réalistes et l'évitement des collisions.
- **Perte de Distogramme** : Garantit que les distances par paires prédites s'alignent avec la réalité (héritage d'AlphaFold 1).

Cet apprentissage de bout en bout permet à AlphaFold d'apprendre implicitement à la fois les modèles évolutifs et les règles structurales.

---

### Innovations Clés

1. **Apprentissage de Bout en Bout** : Contrairement à AlphaFold 1, qui prédisait les distances puis les optimisait, AlphaFold 2 prédit directement la structure.
2. **Transformers et Géométrie** : L'attention de l'Evoformer et l'IPA combinent l'analyse de séquence avec le raisonnement 3D.
3. **Pas de Moteur Physique** : Il apprend les règles physiques à partir des données, évitant les simulations lentes.

---

### Quelle est sa Précision ?

Lors de la CASP14, AlphaFold 2 a atteint un score GDT_TS médian de 92,4 (sur 100), où un score >90 est considéré comme de qualité expérimentale. Pour de nombreuses protéines, il correspond aux résultats de la diffraction aux rayons X ou de la cryo-ME, bien qu'il ait des difficultés avec les régions désordonnées ou les repliements nouveaux manquant de données évolutives.

---

### Points Forts

- **Vitesse** : Prédit les structures en heures, pas en mois.
- **Précision** : Rivalise avec les méthodes expérimentales pour la plupart des protéines.
- **Évolutivité** : Gère des protéines de tailles variées (bien que les plus grandes nécessitent plus de puissance de calcul).

---

### Limites

- **Régions Désordonnées** : Difficultés avec les segments protéiques flexibles et non structurés.
- **Protéines Nouvelles** : Moins précis si aucune séquence similaire n'existe dans le MSA.
- **Structures Statiques** : Prédit une seule conformation, pas le comportement dynamique.
- **Calcul Intensif** : L'entraînement et les prédictions importantes nécessitent des ressources substantielles (par exemple, des TPUs).

---

### Applications

- **Découverte de Médicaments** : Prédit les structures des protéines cibles pour concevoir des médicaments.
- **Recherche en Biologie** : Accélère la compréhension des fonctions des protéines.
- **Biologie Synthétique** : Guide l'ingénierie des protéines en prédisant les conceptions pouvant se replier.

---

### AlphaFold 3 (Note Brève)

Annoncé en 2024, AlphaFold 3 s'étend à la liaison protéine-ligand et à d'autres molécules (par exemple, ADN, ARN). Il utilise un modèle de diffusion pour affiner les prédictions, mais ses mécanismes détaillés sont moins publics. Son noyau s'appuie sur les fondations d'AlphaFold 2.

---

### Conclusion

AlphaFold 2 est un chef-d'œuvre d'IA, alliant les perspectives évolutives, la magie des transformers et la finesse géométrique pour résoudre une énigme biologique vieille de 50 ans. Il ne simule pas le repliement étape par étape comme la nature – il reverse-engineer le résultat final à partir des données. Voyez-le comme un cartographe super-intelligent cartographiant le paysage 3D d'une protéine à partir d'indices épars.

Si vous le souhaitez, je peux approfondir le mécanisme d'attention de l'Evoformer, les mathématiques derrière l'IPA, ou même comment utiliser le code open-source d'AlphaFold (disponible sur GitHub). Quelle est votre prochaine question ?