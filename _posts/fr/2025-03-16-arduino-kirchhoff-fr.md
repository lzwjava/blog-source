---
audio: false
generated: true
lang: fr
layout: post
title: Les lois de Kirchhoff avec Arduino
translated: true
type: note
---

Utiliser un Arduino pour vérifier les lois de Kirchhoff—spécifiquement la Loi des Courants de Kirchhoff (LCK) et la Loi des Tensions de Kirchhoff (LTK)—est une excellente façon d'allier théorie électronique et expérimentation pratique. La LCK stipule que le courant total entrant dans un nœud est égal au courant total qui en sort, tandis que la LTK stipule que la somme des chutes de tension autour d'une boucle fermée est égale à la tension fournie. Voici comment vous pouvez concevoir des circuits simples et utiliser un Arduino pour mesurer les courants et les tensions afin de confirmer ces lois.

Puisque l'Arduino ne peut pas mesurer directement le courant, nous le déduirons en mesurant la tension aux bornes des résistances (en utilisant la Loi d'Ohm : \\( I = V/R \\)), et il peut mesurer la tension via ses broches analogiques (plage 0–5V). Ci-dessous, je décrirai deux expériences—une pour la LCK et une pour la LTK—avec des instructions étape par étape, le câblage et le code.

---

### **Expérience 1 : Vérification de la Loi des Courants de Kirchhoff (LCK)**

#### **Objectif**
Démontrer que le courant entrant dans un nœud est égal au courant qui en sort.

#### **Configuration du circuit**
- **Composants :**
  - Arduino (par exemple, Uno)
  - 3 résistances (par exemple, R1 = 330Ω, R2 = 470Ω, R3 = 680Ω)
  - Plaque d'essai et fils de liaison
  - Source d'alimentation 5V (broche 5V de l'Arduino)
- **Câblage :**
  - Connectez la broche 5V de l'Arduino à un nœud (appelons-le Nœud A).
  - À partir du Nœud A, connectez R1 à la masse (GND) (branche 1).
  - À partir du Nœud A, connectez R2 à la masse (GND) (branche 2, en parallèle avec R1).
  - À partir du Nœud A, connectez R3 à la masse (GND) (branche 3, en parallèle avec R1 et R2).
  - Utilisez les broches analogiques de l'Arduino pour mesurer la tension aux bornes de chaque résistance :
    - A0 aux bornes de R1 (une sonde au Nœud A, l'autre à la masse GND).
    - A1 aux bornes de R2.
    - A2 aux bornes de R3.
- **Note :** La masse (GND) est le point de référence commun.

#### **Théorie**
- Le courant total de la broche 5V vers le Nœud A (\\( I_{in} \\)) se divise en \\( I_1 \\), \\( I_2 \\), et \\( I_3 \\) à travers R1, R2 et R3.
- LCK : \\( I_{in} = I_1 + I_2 + I_3 \\).
- Mesurez la tension aux bornes de chaque résistance, puis calculez le courant : \\( I = V/R \\).

#### **Code Arduino**
```cpp
void setup() {
  Serial.begin(9600); // Démarrer la communication série
}

void loop() {
  // Lire les tensions (0-1023 correspond à 0-5V)
  int sensorValue1 = analogRead(A0); // Tension aux bornes de R1
  int sensorValue2 = analogRead(A1); // Tension aux bornes de R2
  int sensorValue3 = analogRead(A2); // Tension aux bornes de R3

  // Convertir en tension (référence 5V, ADC 10 bits)
  float V1 = sensorValue1 * (5.0 / 1023.0);
  float V2 = sensorValue2 * (5.0 / 1023.0);
  float V3 = sensorValue3 * (5.0 / 1023.0);

  // Valeurs des résistances (en ohms)
  float R1 = 330.0;
  float R2 = 470.0;
  float R3 = 680.0;

  // Calculer les courants (I = V/R)
  float I1 = V1 / R1;
  float I2 = V2 / R2;
  float I3 = V3 / R3;

  // Courant total entrant dans le nœud (en supposant Vsource = 5V)
  float totalResistance = 1.0 / ((1.0/R1) + (1.0/R2) + (1.0/R3)); // Parallèle
  float Iin = 5.0 / totalResistance;

  // Afficher les résultats
  Serial.print("I1 (mA): "); Serial.println(I1 * 1000);
  Serial.print("I2 (mA): "); Serial.println(I2 * 1000);
  Serial.print("I3 (mA): "); Serial.println(I3 * 1000);
  Serial.print("Iin (mA): "); Serial.println(Iin * 1000);
  Serial.print("Somme I1+I2+I3 (mA): "); Serial.println((I1 + I2 + I3) * 1000);
  Serial.println("---");

  delay(2000); // Attendre 2 secondes
}
```

#### **Vérification**
- Ouvrez le Moniteur Série (Ctrl+Maj+M dans l'IDE Arduino, réglé sur 9600 bauds).
- Comparez \\( I_{in} \\) (calculé à partir de la résistance totale) à \\( I_1 + I_2 + I_3 \\). Ils devraient être approximativement égaux, vérifiant ainsi la LCK.
- De petites divergences peuvent survenir en raison des tolérances des résistances ou de la précision de l'ADC de l'Arduino.

---

### **Expérience 2 : Vérification de la Loi des Tensions de Kirchhoff (LTK)**

#### **Objectif**
Montrer que la somme des chutes de tension autour d'une boucle fermée est égale à la tension d'alimentation.

#### **Configuration du circuit**
- **Composants :**
  - Arduino
  - 2 résistances (par exemple, R1 = 330Ω, R2 = 470Ω)
  - Plaque d'essai et fils de liaison
  - Source d'alimentation 5V (broche 5V de l'Arduino)
- **Câblage :**
  - Connectez la broche 5V à R1.
  - Connectez R1 à R2.
  - Connectez R2 à la masse (GND).
  - Mesurez les tensions :
    - A0 aux bornes de la boucle entière (5V à GND) pour confirmer la tension d'alimentation.
    - A1 aux bornes de R1 (5V à la jonction de R1 et R2).
    - A2 aux bornes de R2 (jonction à GND).
- **Note :** Utilisez un montage diviseur de tension ; assurez-vous que les tensions ne dépassent pas 5V (limite de l'Arduino).

#### **Théorie**
- LTK : \\( V_{source} = V_{R1} + V_{R2} \\).
- Mesurez chaque chute de tension et vérifiez si leur somme est égale à la tension source (5V).

#### **Code Arduino**
```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  // Lire les tensions
  int sensorValueSource = analogRead(A0); // Aux bornes de 5V à GND
  int sensorValueR1 = analogRead(A1);     // Aux bornes de R1
  int sensorValueR2 = analogRead(A2);     // Aux bornes de R2

  // Convertir en tension
  float Vsource = sensorValueSource * (5.0 / 1023.0);
  float VR1 = sensorValueR1 * (5.0 / 1023.0);
  float VR2 = sensorValueR2 * (5.0 / 1023.0);

  // Afficher les résultats
  Serial.print("Vsource (V): "); Serial.println(Vsource);
  Serial.print("VR1 (V): "); Serial.println(VR1);
  Serial.print("VR2 (V): "); Serial.println(VR2);
  Serial.print("VR1 + VR2 (V): "); Serial.println(VR1 + VR2);
  Serial.println("---");

  delay(2000);
}
```

#### **Vérification**
- Dans le Moniteur Série, vérifiez que \\( V_{source} \approx V_{R1} + V_{R2} \\).
- Pour R1 = 330Ω et R2 = 470Ω en série, attendez-vous à \\( V_{R1} \approx 2.1V \\) et \\( V_{R2} \approx 2.9V \\) (basé sur le diviseur de tension : \\( V_{R1} = 5 \cdot \frac{R1}{R1+R2} \\)), dont la somme est d'environ ~5V.

---

### **Conseils et considérations**
- **Précision :** L'ADC 10 bits de l'Arduino (0–1023) a une résolution d'environ ~4.9mV, donc attendez-vous à des erreurs mineures. Utilisez un multimètre pour recouper si nécessaire.
- **Sécurité :** Maintenez les tensions en dessous de 5V et les courants faibles pour éviter d'endommager l'Arduino.
- **Mise à l'échelle :** Pour des circuits plus complexes, ajoutez plus de résistances ou utilisez des capteurs externes (par exemple, INA219 pour la mesure directe du courant).
- **Débogage :** Si les résultats ne correspondent pas, vérifiez les valeurs des résistances, les connexions et l'uniformité de la masse (GND).

Ces expériences simplifient les conditions réelles mais démontrent efficacement les lois de Kirchhoff. Vous souhaitez modifier ces configurations ou avez besoin d'aide pour une partie spécifique (comme le câblage ou le code) ? Faites-le-moi savoir !