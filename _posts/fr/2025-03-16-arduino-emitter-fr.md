---
audio: false
generated: true
lang: fr
layout: post
title: Construction d'un amplificateur émetteur commun avec un Arduino
translated: true
type: note
---

Construire un amplificateur à émetteur commun (CE) en utilisant un Arduino est un projet intéressant, mais il est utile de clarifier les rôles : l'Arduino lui-même n'agira pas comme l'amplificateur (c'est un microcontrôleur numérique), mais il peut servir de source de signal ou d'outil de mesure pour un circuit amplificateur CE construit avec un transistor bipolaire (BJT). Un amplificateur CE est un circuit analogique classique qui utilise un transistor NPN ou PNP pour amplifier un petit signal d'entrée, offrant un gain en tension et un gain en courant modérés.

Ici, je vais vous guider dans la conception d'un amplificateur CE basique à base de NPN, en utilisant l'Arduino pour générer un signal d'entrée (via PWM) et mesurer la sortie. Cette configuration démontrera l'amplification tout en tirant parti des capacités de l'Arduino.

---

### **Aperçu d'un amplificateur à émetteur commun**
- **Objectif :** Amplifier un petit signal AC (par exemple, audio ou une onde sinusoïdale).
- **Caractéristiques principales :**
  - Le transistor fonctionne dans la région active.
  - Le signal d'entrée est appliqué à la base, la sortie est prise du collecteur.
  - Le gain en tension est déterminé par les rapports des résistances et les propriétés du transistor.
- **Composants :**
  - Transistor NPN (par exemple, 2N3904 ou BC547)
  - Résistances (pour le biais et la charge)
  - Condensateurs (pour le couplage des signaux AC)
  - Arduino (source de signal et mesure)

---

### **Étape 1 : Concevoir le circuit**

#### **Composants nécessaires**
- Transistor NPN (par exemple, 2N3904)
- Résistances : R1 = 47kΩ, R2 = 10kΩ (biais), RC = 1kΩ (collecteur), RE = 220Ω (émetteur)
- Condensateurs : C1 = 10µF (couplage entrée), C2 = 10µF (couplage sortie), CE = 100µF (bypass émetteur, optionnel pour un gain plus élevé)
- Arduino (par exemple, Uno)
- Plaque d'essai, fils de liaison
- Alimentation (broche 5V de l'Arduino ou externe 9V, ajusté si nécessaire)

#### **Schéma du circuit**
```
Vcc (5V) ---- R1 ----+---- RC ---- Collecteur (C)
             47kΩ     |     1kΩ          |
                      |                  |
Base (B) --- C1 -----+                  |
            10µF     |                  |
Arduino PWM (Pin 9)  R2                 |
                     10kΩ              Sortie --- C2 ---- Vers Arduino A0
                      |                  |         10µF
                      |                  |
                      +---- RE ---- Émetteur (E) --- CE (optionnel) --- GND
                           220Ω                   100µF
                      |
                     GND
```
- **Biais (R1, R2) :** Définit le point de fonctionnement du transistor.
- **RC :** Résistance de collecteur pour le signal de sortie.
- **RE :** Résistance d'émetteur pour la stabilité.
- **C1, C2 :** Bloquent le DC, laissent passer les signaux AC.
- **CE (optionnel) :** Met RE en court-circuit pour un gain AC plus élevé.

#### **Point de fonctionnement**
- Objectif : Polariser le transistor dans la région active (par exemple, VCE ≈ 2,5V pour une alimentation 5V).
- Diviseur de tension (R1, R2) : \\( V_B = V_{CC} \cdot \frac{R2}{R1 + R2} = 5 \cdot \frac{10k}{47k + 10k} \approx 0,88V \\).
- \\( V_E = V_B - V_{BE} \approx 0,88 - 0,7 = 0,18V \\).
- \\( I_E = \frac{V_E}{RE} = \frac{0,18}{220} \approx 0,82 \, \text{mA} \\).
- \\( V_C = V_{CC} - I_C \cdot RC \approx 5 - 0,82 \cdot 1k \approx 4,18V \\).
- \\( V_{CE} = V_C - V_E \approx 4,18 - 0,18 = 4V \\) (bon pour une alimentation 5V).

---

### **Étape 2 : Utiliser l'Arduino comme source de signal**

#### **Rôle de l'Arduino**
- Générer un petit signal AC en utilisant la PWM (Modulation de Largeur d'Impulsion) sur une broche comme la 9 (qui supporte la PWM).
- Filtrer la PWM pour approximer une onde sinusoïdale avec un simple filtre passe-bas RC (optionnel).

#### **Code pour générer un signal**
```cpp
const int pwmPin = 9; // Broche de sortie PWM

void setup() {
  pinMode(pwmPin, OUTPUT);
  // Définir la fréquence PWM (optionnel, par défaut ~490 Hz)
}

void loop() {
  // Simuler une onde sinusoïdale avec PWM (plage 0-255)
  for (int i = 0; i < 360; i += 10) {
    float sineValue = sin(radians(i)); // Onde sinusoïdale de -1 à 1
    int pwmValue = 127 + 127 * sineValue; // Mettre à l'échelle de 0 à 255
    analogWrite(pwmPin, pwmValue);
    delay(10); // Ajuster pour la fréquence (par exemple, ~100 Hz ici)
  }
}
```
- **Sortie :** Signal PWM ~0–5V, centré sur 2,5V avec ~2,5V crête à crête.
- **C1 :** Supprime l'offset DC, ne laissant passer que la composante AC (~1,25V crête) vers la base.

#### **Filtre optionnel**
Ajouter une résistance de 1kΩ et un condensateur de 0,1µF en série de la broche 9 à la masse, en prenant le signal avant C1, pour lisser la PWM en une onde sinusoïdale approximative.

---

### **Étape 3 : Mesurer la sortie**

#### **Mesure avec l'Arduino**
- Connecter la sortie de l'amplificateur (après C2) à A0.
- Utiliser l'Arduino pour lire le signal amplifié et l'afficher via le Moniteur Série.

#### **Code pour mesurer et afficher**
```cpp
const int inputPin = A0; // Mesurer la sortie ici

void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(inputPin); // 0-1023 correspond à 0-5V
  float voltage = sensorValue * (5.0 / 1023.0);
  Serial.print("Tension de sortie (V) : ");
  Serial.println(voltage);
  delay(100); // Ajuster la fréquence d'échantillonnage
}
```

#### **Gain attendu**
- Gain en tension \\( A_v = -\frac{RC}{RE} = -\frac{1k}{220} \approx -4,5 \\) (négatif en raison de l'inversion de phase).
- Entrée : ~1,25V crête (après couplage).
- Sortie : ~4,5 × 1,25 = 5,625V crête (mais écrêtée à 5V en raison de la limite d'alimentation).

---

### **Étape 4 : Construire et tester**

#### **Assemblage**
1. Câbler le circuit sur une plaque d'essai selon le schéma.
2. Téléverser le code de génération de signal sur l'Arduino et connecter la broche 9 à C1.
3. Alimenter le circuit via le 5V de l'Arduino (ou utiliser 9V avec des résistances ajustées).
4. Téléverser le code de mesure et ouvrir le Moniteur Série (9600 bauds).

#### **Vérification**
- **Signal d'entrée :** ~1–2V crête à crête après C1 (utiliser un multimètre ou un oscilloscope si disponible).
- **Signal de sortie :** Devrait être plus grand (par exemple, 4–5V crête à crête) et inversé.
- Vérifier VCE (~2–4V) avec un multimètre pour s'assurer du fonctionnement en région active.

---

### **Conseils et dépannage**
- **Gain trop faible :** Ajouter CE (100µF) aux bornes de RE pour augmenter le gain AC (supprime la dégénération de RE).
- **Écrêtage :** Si la sortie dépasse 5V, réduire l'amplitude d'entrée (ajuster la plage PWM) ou augmenter Vcc (par exemple, alimentation externe 9V).
- **Bruit :** La PWM est carrée ; une meilleure onde sinusoïdale (via un générateur externe ou un filtre) améliore les résultats.
- **Spécifications du transistor :** S'assurer que le 2N3904 supporte les courants (Ic < 200mA, sûr ici).

Cette configuration démontre le comportement principal d'un amplificateur CE—l'amplification de tension—tout en intégrant l'Arduino pour la génération et l'analyse du signal. Vous voulez ajuster le gain, ajouter un haut-parleur pour l'audio, ou améliorer le signal ? Faites-le moi savoir !