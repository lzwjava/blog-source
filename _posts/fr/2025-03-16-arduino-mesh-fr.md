---
audio: false
generated: true
lang: fr
layout: post
title: Vérification de l'analyse maillée avec Arduino
translated: true
type: note
---

Vérifier l'analyse des mailles avec un Arduino implique de construire un circuit avec plusieurs boucles, d'appliquer théoriquement l'analyse des mailles pour prédire les courants, puis d'utiliser l'Arduino pour mesurer les tensions aux bornes des résistances afin de calculer les courants réels pour comparaison. L'analyse des mailles est une méthode en théorie des circuits où vous attribuez des courants de maille à chaque maille indépendante et utilisez la Loi des Tensions de Kirchhoff (KVL) pour établir des équations. L'Arduino vous aidera à mesurer le comportement réel pour confirmer vos calculs.

Ci-dessous, je vais vous guider pour concevoir un circuit simple à deux mailles, effectuer manuellement l'analyse des mailles et utiliser un Arduino pour vérifier les résultats en mesurant les tensions et en déduisant les courants (puisque l'Arduino ne peut pas mesurer le courant directement, nous utiliserons la Loi d'Ohm: \\( I = V/R \\)).

---

### **Étape 1 : Concevoir un circuit à deux mailles**

#### **Description du circuit**
- **Composants :**
  - Arduino (ex. Uno)
  - 3 résistances (ex. R1 = 330Ω, R2 = 470Ω, R3 = 680Ω)
  - Plaque d'essai et fils de liaison
  - Source d'alimentation (broche 5V de l'Arduino)
- **Câblage :**
  - Connectez 5V au Nœud A.
  - Depuis le Nœud A, connectez R1 au Nœud B.
  - Depuis le Nœud B, connectez R2 au Nœud C (GND).
  - Depuis le Nœud A, connectez R3 au Nœud C (GND).
- **Topologie :**
  - Maille 1 : 5V → R1 → R2 → GND (boucle de gauche).
  - Maille 2 : 5V → R3 → GND (boucle de droite).
  - R1 est uniquement dans la Maille 1, R3 est uniquement dans la Maille 2, et R2 est partagée entre les deux mailles.
- **Points de mesure :**
  - A0 : Tension aux bornes de R1 (Nœud A au Nœud B).
  - A1 : Tension aux bornes de R2 (Nœud B au Nœud C).
  - A2 : Tension aux bornes de R3 (Nœud A au Nœud C).

#### **Concept schématique**
```
5V ---- Nœud A ---- R1 ---- Nœud B ---- R2 ---- Nœud C (GND)
       |                        |
       +--------- R3 -----------+
```

---

### **Étape 2 : Effectuer l'analyse des mailles théoriquement**

#### **Définir les courants de maille**
- \\( I_1 \\) : Courant dans la Maille 1 (horaire à travers 5V, R1, R2, GND).
- \\( I_2 \\) : Courant dans la Maille 2 (horaire à travers 5V, R3, GND).

#### **Appliquer KVL à chaque maille**
1. **Maillev 1 (5V → R1 → R2 → GND) :**
   - Source de tension : +5V (en allant de GND à 5V dans le sens de la boucle).
   - Chute de tension aux bornes de R1 : \\( -R1 \cdot I_1 \\).
   - Chute de tension aux bornes de R2 : \\( -R2 \cdot (I_1 - I_2) \\) (le courant à travers R2 est \\( I_1 - I_2 \\)).
   - Équation : \\( 5 - R1 \cdot I_1 - R2 \cdot (I_1 - I_2) = 0 \\).

2. **Maillev 2 (5V → R3 → GND) :**
   - Source de tension : +5V.
   - Chute de tension aux bornes de R3 : \\( -R3 \cdot I_2 \\).
   - Chute de tension aux bornes de R2 (sens opposé) : \\( +R2 \cdot (I_1 - I_2) \\) (le courant à travers R2 est \\( I_1 - I_2 \\)).
   - Équation : \\( 5 - R3 \cdot I_2 + R2 \cdot (I_1 - I_2) = 0 \\).

#### **Substituer les valeurs**
- R1 = 330Ω, R2 = 470Ω, R3 = 680Ω.
- Maille 1 : \\( 5 - 330 I_1 - 470 (I_1 - I_2) = 0 \\)
  - Simplifier : \\( 5 - 330 I_1 - 470 I_1 + 470 I_2 = 0 \\)
  - \\( 5 - 800 I_1 + 470 I_2 = 0 \\) → (1)
- Maille 2 : \\( 5 - 680 I_2 + 470 (I_1 - I_2) = 0 \\)
  - Simplifier : \\( 5 + 470 I_1 - 680 I_2 - 470 I_2 = 0 \\)
  - \\( 5 + 470 I_1 - 1150 I_2 = 0 \\) → (2)

#### **Résoudre les équations**
- De (1) : \\( 5 = 800 I_1 - 470 I_2 \\) → \\( I_1 = \frac{5 + 470 I_2}{800} \\).
- Substituer dans (2) : \\( 5 + 470 \left( \frac{5 + 470 I_2}{800} \right) - 1150 I_2 = 0 \\).
- Multiplier par 800 pour éliminer la fraction :
  - \\( 4000 + 470 (5 + 470 I_2) - 1150 \cdot 800 I_2 = 0 \\)
  - \\( 4000 + 2350 + 220900 I_2 - 920000 I_2 = 0 \\)
  - \\( 6350 - 699100 I_2 = 0 \\)
  - \\( I_2 = \frac{6350}{699100} \approx 0.00908 \, \text{A} = 9.08 \, \text{mA} \\).
- Remplacer : \\( I_1 = \frac{5 + 470 \cdot 0.00908}{800} = \frac{5 + 4.2676}{800} \approx 0.01158 \, \text{A} = 11.58 \, \text{mA} \\).

#### **Calculer les tensions**
- \\( V_{R1} = R1 \cdot I_1 = 330 \cdot 0.01158 \approx 3.82 \, \text{V} \\).
- \\( V_{R2} = R2 \cdot (I_1 - I_2) = 470 \cdot (0.01158 - 0.00908) \approx 1.18 \, \text{V} \\).
- \\( V_{R3} = R3 \cdot I_2 = 680 \cdot 0.00908 \approx 6.17 \, \text{V} \\) (mais limitée à 5V à cause de la source).

---

### **Étape 3 : Vérifier avec Arduino**

#### **Code Arduino**
```cpp
void setup() {
  Serial.begin(9600); // Démarrer la communication série
}

void loop() {
  // Lire les tensions (0-1023 correspond à 0-5V)
  int sensorValueR1 = analogRead(A0); // Aux bornes de R1
  int sensorValueR2 = analogRead(A1); // Aux bornes de R2
  int sensorValueR3 = analogRead(A2); // Aux bornes de R3

  // Convertir en tension
  float VR1 = sensorValueR1 * (5.0 / 1023.0);
  float VR2 = sensorValueR2 * (5.0 / 1023.0);
  float VR3 = sensorValueR3 * (5.0 / 1023.0);

  // Valeurs des résistances
  float R1 = 330.0;
  float R2 = 470.0;
  float R3 = 680.0;

  // Calculer les courants (I = V/R)
  float I1 = VR1 / R1;              // Courant de la Maille 1 à travers R1
  float I2 = VR3 / R3;              // Courant de la Maille 2 à travers R3
  float IR2 = VR2 / R2;             // Courant à travers R2 (I1 - I2)

  // Afficher les résultats
  Serial.println("Valeurs mesurées :");
  Serial.print("VR1 (V) : "); Serial.println(VR1);
  Serial.print("VR2 (V) : "); Serial.println(VR2);
  Serial.print("VR3 (V) : "); Serial.println(VR3);
  Serial.print("I1 (mA) : "); Serial.println(I1 * 1000);
  Serial.print("I2 (mA) : "); Serial.println(I2 * 1000);
  Serial.print("I1 - I2 (mA) : "); Serial.println((I1 - I2) * 1000);
  Serial.println("---");

  delay(2000); // Attendre 2 secondes
}
```

#### **Notes de câblage**
- Connectez A0 entre le Nœud A (5V) et le Nœud B.
- Connectez A1 entre le Nœud B et le Nœud C (GND).
- Connectez A2 entre le Nœud A (5V) et le Nœud C (GND).
- Assurez-vous que toutes les masses sont communes avec la masse (GND) de l'Arduino.

---

### **Étape 4 : Comparer les résultats**

#### **Attendu vs. Mesuré**
- **Théorique (d'après l'analyse des mailles) :**
  - \\( I_1 \approx 11.58 \, \text{mA} \\)
  - \\( I_2 \approx 9.08 \, \text{mA} \\)
  - \\( I_1 - I_2 \approx 2.50 \, \text{mA} \\)
  - \\( V_{R1} \approx 3.82 \, \text{V} \\), \\( V_{R2} \approx 1.18 \, \text{V} \\), \\( V_{R3} \approx 5 \, \text{V} \\) (limitée).
- **Mesuré :** Ouvrez le Moniteur Série (9600 bauds) et comparez la sortie de l'Arduino à ces valeurs.

#### **Vérification**
- Vérifiez si \\( V_{R1} + V_{R2} \approx 5V \\) (boucle de la Maille 1).
- Vérifiez si \\( V_{R3} \approx 5V \\) (boucle de la Maille 2).
- Confirmez que \\( I_1 - I_2 \\) correspond au courant à travers R2.

---

### **Conseils et dépannage**
- **Précision :** L'ADC de l'Arduino a une résolution d'environ ~4.9mV, et les tolérances des résistances peuvent causer de légers écarts. Utilisez un multimètre pour une validation précise.
- **Ajustements :** Si les tensions dépassent 5V (peu probable ici), utilisez un diviseur de tension pour les réduire.
- **Extensions :** Ajoutez plus de mailles ou de composants pour complexifier, mais gardez à l'esprit les limites des broches (A0–A5).

Cette configuration confirme l'analyse des mailles en alignant les courants théoriques avec les courants mesurés. Faites-moi savoir si vous avez besoin d'aide pour peaufiner le circuit, déboguer ou ajouter plus de mailles !