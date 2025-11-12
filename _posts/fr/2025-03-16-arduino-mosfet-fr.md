---
audio: false
generated: true
lang: fr
layout: post
title: MOSFET en tant qu'interrupteur contrôlé par Arduino
translated: true
type: note
---

Il semble y avoir un malentendu dans votre question. Un Arduino ne peut pas être utilisé pour *fabriquer* des transistors à effet de champ métal-oxyde-semiconducteur (MOSFET) car les MOSFETs sont des composants semiconducteurs fondamentaux manufacturés via des procédés complexes comme la photolithographie et le dopage dans un environnement de salle blanche. Cependant, je suppose que vous vouliez dire "comment utiliser un Arduino pour construire un circuit *utilisant* des MOSFETs" ou "comment utiliser des MOSFETs dans un projet Arduino". Si j'ai mal interprété, merci de clarifier !

Je vais poursuivre en expliquant comment utiliser un Arduino pour contrôler un MOSFET dans un circuit pratique, comme un simple interrupteur ou un amplificateur. Les MOSFETs sont des composants polyvalents, souvent utilisés comme interrupteurs ou dans des circuits d'amplification, et ils fonctionnent bien avec les sorties numériques d'un Arduino. Ci-dessous, je fournis un guide étape par étape pour une application courante : utiliser un MOSFET à canal N (par exemple, IRF540 ou 2N7000) comme interrupteur de puissance contrôlé par un Arduino.

---

### **Projet : MOSFET en tant qu'Interrupteur Contrôlé par Arduino**

#### **Aperçu**
- **Objectif :** Utiliser un Arduino pour allumer et éteindre une charge de puissance (par exemple, une bande LED, un moteur, ou une lampe) via un MOSFET.
- **Pourquoi un MOSFET ?** Contrairement aux BJT, les MOSFETs sont contrôlés en tension, nécessitant un courant minimal de la part de l'Arduino, et peuvent gérer des courants/tensions plus élevés que les broches de l'Arduino (max 40mA, 5V).

#### **Composants Nécessaires**
- Arduino (par exemple, Uno)
- MOSFET à canal N (par exemple, IRF540 ou 2N7000 ; IRF540 pour une puissance plus élevée)
- Résistances : R1 = 10kΩ (pull-down), R2 = 220Ω (protection de grille, optionnel)
- Charge : par exemple, bande LED 12V, moteur CC, ou lampe (avec alimentation appropriée)
- Diode (par exemple, 1N4007, pour les charges inductives comme les moteurs)
- Plaque d'essai, fils de liaison
- Alimentation externe (par exemple, 12V pour la charge)

#### **Schéma de Circuit**
```
Broche Arduino 9 ---- R2 (220Ω) ---- Grille (G)
                             |
                             |
V_charge (ex: 12V) ---- Charge ---- Drain (D)
                             | 
                             |
                            Source (S) ---- GND
                             |
                            R1 (10kΩ)
                             |
                            GND
```
- **Pour les Charges Inductives (ex: Moteur) :** Ajouter une diode de roue libre (1N4007) en parallèle de la charge (cathode vers V_charge, anode vers Drain) pour protéger le MOSFET des surtensions.
- **Alimentation :** Arduino alimenté via USB ou 5V ; charge alimentée par une source externe (ex: 12V). Connecter toutes les masses (GND) ensemble.

#### **Fonctionnement**
- **Rôle du MOSFET :** Agit comme un interrupteur entre le Drain et la Source, contrôlé par la tension de Grille.
- **Rôle de l'Arduino :** Émet un signal HIGH (5V) ou LOW (0V) vers la Grille via la broche 9.
- **Logique :**
  - HIGH (5V) sur la Grille → Le MOSFET s'active → La charge est alimentée.
  - LOW (0V) sur la Grille → Le MOSFET se désactive → La charge s'arrête.
- **R1 (Pull-down) :** Assure que la Grille est à LOW lorsque l'Arduino est éteint ou que la broche est en état flottant.
- **R2 (Optionnel) :** Limite le courant vers la Grille (généralement inutile pour les MOSFETs de niveau logique).

---

### **Étape 1 : Construire le Circuit**

1. **Connecter le MOSFET :**
   - **Grille (G) :** À la broche 9 de l'Arduino via R2 (220Ω, optionnel).
   - **Drain (D) :** Au côté négatif de la charge (par exemple, cathode de la bande LED).
   - **Source (S) :** À GND.
2. **Charge et Alimentation :**
   - Connecter le côté positif de la charge à V_charge (par exemple, alimentation 12V).
   - Connecter la masse (GND) de l'alimentation 12V à la masse (GND) de l'Arduino.
3. **Sécurité :**
   - Ajouter R1 (10kΩ) entre la Grille et GND.
   - Pour les moteurs, ajouter la diode en parallèle de la charge.

---

### **Étape 2 : Code Arduino**

#### **Interrupteur Marche/Arrêt Simple**
```cpp
const int mosfetPin = 9; // Broche capable de PWM

void setup() {
  pinMode(mosfetPin, OUTPUT); // Définir la broche comme sortie
}

void loop() {
  digitalWrite(mosfetPin, HIGH); // Activer le MOSFET
  delay(1000);                   // Attendre 1 seconde
  digitalWrite(mosfetPin, LOW);  // Désactiver le MOSFET
  delay(1000);                   // Attendre 1 seconde
}
```
- **Sortie :** La charge s'allume et s'éteint toutes les secondes.

#### **Variation d'intensité PWM (pour LEDs/Moteurs)**
```cpp
const int mosfetPin = 9;

void setup() {
  pinMode(mosfetPin, OUTPUT);
}

void loop() {
  for (int brightness = 0; brightness <= 255; brightness += 5) {
    analogWrite(mosfetPin, brightness); // Augmenter l'intensité
    delay(50);
  }
  for (int brightness = 255; brightness >= 0; brightness -= 5) {
    analogWrite(mosfetPin, brightness); // Diminuer l'intensité
    delay(50);
  }
}
```
- **Sortie :** La charge (par exemple, une LED) s'éclaire et s'assombrit progressivement.

---

### **Étape 3 : Tester et Vérifier**

1. **Téléverser le Code :** Utiliser l'IDE Arduino pour téléverser l'un ou l'autre sketch.
2. **Mettre sous tension :** Connecter l'Arduino via USB et l'alimentation externe à la charge.
3. **Observer :**
   - Pour le code marche/arrêt, la charge devrait basculer toutes les secondes.
   - Pour le PWM, la charge devrait s'éclaircir et s'assombrir progressivement.
4. **Mesurer :** Utiliser un multimètre pour vérifier :
   - La tension à la Grille (0V ou 5V).
   - La tension aux bornes de la charge (0V ou V_charge).

---

### **Choisir le Bon MOSFET**
- **MOSFET de Niveau Logique (ex: IRL540, 2N7000) :** S'active complètement avec 5V de l'Arduino. Préféré pour ce projet.
- **MOSFET Standard (ex: IRF540) :** Nécessite ~10V à la Grille pour s'activer complètement. Avec 5V, il peut conduire partiellement—utiliser un transistor ou un pilote (par exemple, BJT ou CI comme TC4420) pour augmenter la tension de Grille si vous utilisez ceux-ci.
- **Spécifications :** Vérifier que V_DS (tension max) et I_D (courant max) correspondent à votre charge (par exemple, IRF540 : 100V, 33A).

---

### **Alternative : Amplificateur à MOSFET**
Si vous pensiez à un amplificateur à base de MOSFET (par exemple, Amplificateur Source Commune), voici un aperçu rapide :
- **Configuration :** Similaire à l'amplificateur EC mais avec un MOSFET (par exemple, 2N7000).
- **Schéma :** Vcc → RD (résistance de Drain) → Drain ; Source → GND ; Grille → Signal d'entrée (via un condensateur).
- **Rôle de l'Arduino :** Générer un petit signal AC (comme dans l'exemple de l'amplificateur EC).
- **Gain :** \\( A_v = -g_m \cdot R_D \\), où \\( g_m \\) est la transconductance.
- **Défi :** Nécessite un polarisation précise ; moins courant pour les débutants que les amplificateurs à BJT.

Faites-moi savoir si vous souhaitez plutôt vous orienter vers cela !

---

### **Conseils et Dépannage**
- **Chaleur :** Si le MOSFET chauffe, il n'est pas complètement activé (vérifier la compatibilité niveau logique) ou la charge dépasse sa capacité—ajouter un dissipateur thermique ou réduire le courant.
- **Aucune Réponse :** Vérifier les connexions, le brochage du MOSFET (GDS) et l'alimentation.
- **Bruit :** La commutation PWM peut être audible avec les moteurs—ajuster la fréquence si nécessaire (réglage avancé).
- **Tension plus Élevée :** Pour des charges >5V, s'assurer que le seuil V_GS du MOSFET est atteint.

Ce projet montre comment intégrer un MOSFET avec un Arduino pour un contrôle pratique. Vous voulez le faire évoluer (par exemple, contrôle de vitesse de moteur) ou explorer l'amplification à la place ? Dites-le simplement !