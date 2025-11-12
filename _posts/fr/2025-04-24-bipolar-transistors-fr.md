---
audio: false
generated: true
lang: fr
layout: post
title: Transistors bipolaires à jonction
translated: true
type: note
---

Les transistors bipolaires à jonction (BJT) sont des dispositifs semi-conducteurs fondamentaux utilisés dans l'amplification, la commutation et le traitement du signal. Ce sont des dispositifs à trois bornes avec une structure qui permet le contrôle et l'amplification du courant, ce qui les rend essentiels en électronique analogique et numérique. Approfondissons leur structure, leur fonctionnement, leurs modes et leurs courbes caractéristiques, comme demandé, tout en gardant l'explication complète mais accessible.

---

### **1. Structure et bornes d'un BJT**
Un BJT est constitué de trois régions de semi-conducteur dopées, formant deux jonctions p-n, et est classé en deux types : **NPN** et **PNP**. Les trois bornes sont :

- **Base (B)** : Une région mince et faiblement dopée qui contrôle le fonctionnement du transistor. Elle agit comme le "gardien" du flux de courant.
- **Collecteur (C)** : Une région modérément dopée qui collecte les porteurs de charge (électrons dans le NPN, trous dans le PNP) en provenance de l'émetteur.
- **Émetteur (E)** : Une région fortement dopée qui émet les porteurs de charge dans la base.

**BJT NPN** : Composé de deux régions de type n (collecteur et émetteur) entourant une fine base de type p. Les électrons sont les principaux porteurs de charge.
**BJT PNP** : Composé de deux régions de type p (collecteur et émetteur) entourant une fine base de type n. Les trous sont les principaux porteurs de charge.

Les deux jonctions p-n sont :
- **Jonction Base-Émetteur** : Entre la base et l'émetteur.
- **Jonction Base-Collecteur** : Entre la base et le collecteur.

La région mince de la base est critique, car elle permet au BJT de contrôler de grands courants avec un faible courant de base, permettant ainsi l'amplification.

---

### **2. Modes de fonctionnement d'un BJT**
Les BJT fonctionnent selon trois modes principaux, déterminés par le polarisation (tension appliquée) des jonctions base-émetteur et base-collecteur :

1. **Mode Actif** (utilisé pour l'amplification) :
   - **Jonction Base-Émetteur** : Polarisation directe (allumée, permettant au courant de circuler).
   - **Jonction Base-Collecteur** : Polarisation inverse (bloque le courant, mais permet un flux contrôlé de porteurs).
   - Dans les BJT NPN, un petit courant de base (I_B) injecte des électrons de l'émetteur dans la base. La plupart de ces électrons diffusent à travers la base mince et sont entraînés dans le collecteur, produisant un courant de collecteur plus important (I_C).
   - **Amplification du Courant** : Le courant de collecteur est proportionnel au courant de base, avec un gain en courant (β) typiquement compris entre 20 et 1000. Mathématiquement :  
     \\[
     I_C = \beta \cdot I_B
     \\]
   - Le courant d'émetteur est la somme des courants de base et de collecteur :  
     \\[
     I_E = I_B + I_C
     \\]
   - Ce mode est utilisé dans les amplificateurs car un petit signal d'entrée (courant ou tension de base) contrôle un grand signal de sortie (courant ou tension de collecteur).

2. **Mode de Saturation** (utilisé pour la commutation, état "on") :
   - Les deux jonctions base-émetteur et base-collecteur sont en polarisation directe.
   - Le transistor agit comme un interrupteur fermé, permettant un courant de collecteur maximal avec une tension collecteur-émetteur minimale (V_CE ≈ 0,2V).
   - Utilisé dans les circuits numériques pour représenter un état logique "1".

3. **Mode de Blocage** (utilisé pour la commutation, état "off") :
   - Les deux jonctions sont en polarisation inverse.
   - Le transistor agit comme un interrupteur ouvert, sans courant de collecteur (I_C ≈ 0).
   - Utilisé dans les circuits numériques pour représenter un état logique "0".

D'autres modes moins courants incluent :
- **Mode Actif Inverse** : Les rôles du collecteur et de l'émetteur sont inversés, mais ce mode est rarement utilisé en raison de ses performances médiocres (β plus faible).
- **Mode de Claquage** : Se produit lorsque les tensions dépassent les limites du transistor, risquant de l'endommager.

---

### **3. Mode Actif : Mécanisme d'amplification**
En mode actif, la capacité du BJT à amplifier le courant découle de sa structure et de sa polarisation :
- **Jonction base-émetteur en polarisation directe** : Pour un BJT NPN, une tension positive (V_BE ≈ 0,7V pour le silicium) est appliquée, permettant aux électrons de circuler de l'émetteur vers la base.
- **Base mince** : La base est si mince que la plupart des électrons injectés par l'émetteur ne se recombinent pas avec les trous dans la base de type p. Au lieu de cela, ils diffusent vers la jonction base-collecteur en polarisation inverse.
- **Jonction base-collecteur en polarisation inverse** : Le champ électrique à cette jonction entraîne les électrons dans le collecteur, créant un important courant de collecteur.
- **Amplification** : Un petit courant de base (I_B) contrôle un courant de collecteur beaucoup plus important (I_C), la relation étant régie par le gain en courant (β). Par exemple, si β = 100, un courant de base de 1 µA peut produire un courant de collecteur de 100 µA.

Cette amplification rend les BJT idéaux pour des applications telles que les amplificateurs audio, les amplificateurs radiofréquence et les circuits amplificateurs opérationnels.

---

### **4. Courbes caractéristiques**
Le comportement d'un BJT en mode actif est mieux compris à travers ses **courbes caractéristiques**, qui tracent la relation entre les courants et les tensions. Il existe deux types principaux de courbes caractéristiques :

#### **a. Caractéristiques d'entrée**
- **Tracé** : Courant de base (I_B) en fonction de la tension base-émetteur (V_BE) pour une tension collecteur-émetteur (V_CE) fixe.
- **Comportement** : Ressemble à la courbe I-V d'une diode en polarisation directe, car la jonction base-émetteur est une jonction p-n.
- **Points clés** :
  - V_BE commence typiquement à ~0,6–0,7V (pour les BJT au silicium) pour initier un courant de base significatif.
  - De petits changements dans V_BE provoquent de grands changements dans I_B en raison de la relation exponentielle.
  - Utilisé pour concevoir le circuit de polarisation d'entrée.

#### **b. Caractéristiques de sortie**
- **Tracé** : Courant de collecteur (I_C) en fonction de la tension collecteur-émetteur (V_CE) pour différentes valeurs de courant de base (I_B).
- **Régions** :
  1. **Région Active** :
     - I_C est presque constant pour un I_B donné, même lorsque V_CE augmente.
     - I_C ≈ β · I_B, montrant l'amplification de courant du transistor.
     - Les courbes sont presque horizontales, indiquant que I_C est indépendant de V_CE (comportement de source de courant idéale).
  2. **Région de Saturation** :
     - À faible V_CE (par exemple, < 0,2V), le courant de collecteur chute et le transistor est complètement "ouvert".
     - Les courbes s'incurvent vers le bas lorsque la jonction base-collecteur devient polarisée en direct.
  3. **Région de Blocage** :
     - Lorsque I_B = 0, I_C ≈ 0 et le transistor est "fermé".
  4. **Région de Claquage** :
     - À haute V_CE, le transistor peut entrer en claquage, où I_C augmente de manière incontrôlable (non représenté sur les courbes standard).
- **Points clés** :
  - Chaque courbe correspond à un I_B fixe (par exemple, 10 µA, 20 µA, etc.).
  - L'espacement entre les courbes reflète le gain en courant (β).
  - Utilisé pour analyser le comportement du transistor dans les amplificateurs et les commutateurs.

#### **c. Caractéristiques de transfert**
- **Tracé** : Courant de collecteur (I_C) en fonction du courant de base (I_B) pour une V_CE fixe.
- **Comportement** : Montre la relation linéaire I_C = β · I_B dans la région active.
- **Utilisation** : Aide à déterminer le gain en courant (β) et à concevoir les circuits de polarisation.

---

### **5. Paramètres et équations clés**
- **Gain en Courant (β)** :
  \\[
  \beta = \frac{I_C}{I_B}
  \\]
  Typiquement 20–1000, selon le type de transistor et les conditions de fonctionnement.
- **Alpha (α)** : Gain en courant en base commune, rapport du courant de collecteur au courant d'émetteur :
  \\[
  \alpha = \frac{I_C}{I_E}
  \\]
  Puisque I_E = I_B + I_C, α est lié à β :
  \\[
  \alpha = \frac{\beta}{\beta + 1}
  \\]
  α est typiquement de 0,95–0,999, proche de 1.
- **Tension Base-Émetteur (V_BE)** :
  - ~0,7V pour les BJT au silicium en mode actif.
  - Suit l'équation de la diode :  
    \\[
    I_B \propto e^{V_{BE}/V_T}
    \\]
    où V_T est la tension thermique (~26 mV à température ambiante).
- **Tension Collecteur-Émetteur (V_CE)** :
  - En mode actif, V_CE > V_CE(sat) (~0,2V) pour éviter la saturation.
  - En saturation, V_CE ≈ 0,2V.
- **Dissipation de Puissance** :
  \\[
  P = V_{CE} \cdot I_C
  \\]
  Doit rester dans la limite maximale du transistor pour éviter tout dommage.

---

### **6. Applications des BJT**
- **Amplificateurs** :
  - **Amplificateur Émetteur Commun** : Gain en tension et en courant élevé, largement utilisé dans les circuits audio et RF.
  - **Amplificateur Base Commune** : Faible impédance d'entrée, utilisé dans les applications haute fréquence.
  - **Collecteur Commun (Suiveur d'Émetteur)** : Haute impédance d'entrée, utilisé pour l'adaptation d'impédance.
- **Commutateurs** :
  - Dans les circuits numériques, les BJT fonctionnent en saturation (on) ou en blocage (off) pour contrôler les états logiques.
- **Oscillateurs** : Utilisés dans les circuits RF pour générer des signaux sinusoïdaux.
- **Régulateurs de Tension** : Les BJT stabilisent les tensions de sortie dans les alimentations.
- **Traitement du Signal** : Utilisés dans les mélangeurs, modulateurs et démodulateurs.

---

### **7. Considérations pratiques**
- **Polarisation** : Une polarisation CC appropriée garantit que le BJT fonctionne dans le mode souhaité (actif pour l'amplification, saturation/blocage pour la commutation). Les circuits de polarisation courants incluent la polarisation fixe, la polarisation collecteur-base et la polarisation par diviseur de tension.
- **Emballement Thermique** : Une température excessive peut augmenter I_C, entraînant un échauffement supplémentaire et une destruction potentielle. Les circuits de polarisation incluent souvent une compensation thermique (par exemple, des résistances d'émetteur).
- **Modèles Petit Signal** : Pour la conception d'amplificateurs, les BJT sont modélisés à l'aide de modèles hybride-π ou en T pour analyser le comportement AC.
- **Limitations** :
  - Les BJT nécessitent un courant de base continu, contrairement aux MOSFETs, ce qui peut entraîner une perte de puissance.
  - Vitesse de commutation plus lente que les MOSFETs dans les applications haute fréquence.
  - Sensibles aux variations de température et au bruit.

---

### **8. Comparaison avec d'autres transistors**
- **Vs. MOSFETs** :
  - Les BJT sont contrôlés en courant, tandis que les MOSFETs sont contrôlés en tension.
  - Les BJT ont une consommation d'énergie plus élevée dans le circuit de contrôle en raison du courant de base.
  - Les MOSFETs sont préférés dans les circuits intégrés numériques modernes en raison d'une commutation plus rapide et d'une consommation d'énergie plus faible.
- **Vs. JFETs** :
  - Les JFETs sont contrôlés en tension et ont une impédance d'entrée plus élevée.
  - Les BJT offrent un gain en courant plus élevé et sont meilleurs pour les charges à faible impédance.

---

### **9. Courbes caractéristiques en détail (Visualisation des courbes de sortie)**
Pour clarifier davantage les **courbes caractéristiques de sortie** (I_C vs. V_CE pour différents I_B) :
- **Axe des X** : V_CE, allant de 0V à la tension maximale nominale (par exemple, 40V pour un BJT typique).
- **Axe des Y** : I_C, allant de 0 au courant de collecteur maximum (par exemple, 100 mA).
- **Courbes** : Chaque courbe représente un I_B fixe (par exemple, 10 µA, 20 µA, 30 µA).
- **Région Active** : La partie plate des courbes, où I_C est proportionnel à I_B et indépendant de V_CE.
- **Région de Saturation** : La partie abrupte près de V_CE = 0, où I_C chute lorsque V_CE diminue.
- **Région de Blocage** : La ligne horizontale à I_C = 0 lorsque I_B = 0.
- **Effet Early** : Dans la région active, les courbes montent légèrement en pente en raison de la modulation de largeur de base (un effet secondaire où l'augmentation de V_CE réduit la largeur effective de la base, augmentant I_C).

Ces courbes sont essentielles pour :
- **Analyse de la Ligne de Charge** : Déterminer le point de fonctionnement (point Q) du transistor dans un circuit.
- **Conception d'Amplificateur** : S'assurer que le transistor reste dans la région active pour une amplification linéaire.
- **Conception de Commutation** : S'assurer que le transistor entre pleinement en saturation ou en blocage.

---

### **10. Sujets avancés (Plongée approfondie facultative)**
- **Modèle d'Ebers-Moll** : Un modèle mathématique décrivant le comportement des BJT dans tous les modes de fonctionnement, basé sur des équations de diodes couplées.
- **Modèle de Gummel-Poon** : Un modèle plus complexe utilisé dans les simulateurs de circuits (par exemple, SPICE) pour tenir compte des effets non idéaux comme l'effet Early, l'injection à haut niveau et les capacités parasites.
- **Réponse en Fréquence** : Les BJT ont une fréquence de coupure (f_T) où le gain en courant tombe à 1, limitant leur utilisation dans les applications haute fréquence.
- **Bruit** : Les BJT introduisent du bruit de grenaille et du bruit thermique, qui doivent être pris en compte dans les applications à faible signal.
- **BJT de Puissance** : Des BJT spécialisés (par exemple, les paires Darlington) sont conçus pour des applications à fort courant comme le contrôle de moteurs.

---

### **Conclusion**
Les transistors bipolaires à jonction (BJT) sont des dispositifs polyvalents à trois bornes (base, collecteur, émetteur) qui excellent dans l'amplification et la commutation. En **mode actif**, ils amplifient le courant en utilisant un petit courant de base pour contrôler un grand courant de collecteur, régi par le gain en courant (β). Leurs **courbes caractéristiques** (d'entrée, de sortie et de transfert) fournissent une représentation graphique de leur comportement, les courbes de sortie (I_C vs. V_CE) étant particulièrement importantes pour comprendre l'amplification et la commutation. En tirant parti des propriétés uniques de leurs jonctions p-n et de leur base mince, les BJT permettent un large éventail d'applications, des amplificateurs à la logique numérique. Cependant, leurs performances dépendent d'une polarisation appropriée, d'une gestion thermique et de la compréhension de leurs limites par rapport aux dispositifs modernes comme les MOSFETs.

Si vous souhaitez une exploration plus approfondie d'un aspect spécifique (par exemple, les circuits de polarisation, les modèles petit signal ou les applications), ou si vous souhaitez que je génère un diagramme des courbes caractéristiques (avec confirmation de l'utilisateur), faites-le moi savoir !