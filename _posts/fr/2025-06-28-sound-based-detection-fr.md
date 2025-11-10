---
audio: false
generated: true
lang: fr
layout: post
title: Détection sonore pour laveuse Maytag
translated: true
type: note
---

Utiliser le son pour détecter l'arrêt de votre lave-linge Maytag MHW8630HW est une alternative viable à l'approche basée sur une caméra. En plaçant un capteur de son près du lave-linge, vous pouvez surveiller le bruit généré pendant le fonctionnement (par exemple, le ronronnement du moteur, l'écoulement de l'eau ou la rotation du tambour) et détecter quand il s'arrête, ce qui indique la fin du cycle de lavage. Ci-dessous, je vais expliquer comment adapter le projet précédent pour utiliser un capteur de son au lieu d'une caméra, en me concentrant sur le matériel, l'algorithme et les modifications du code tout en conservant le système de notification Telegram.

---

### Tech Stack
#### Matériel
1. **Carte Arduino** :
   - **ESP32-CAM** (toujours utilisable) – Conserve le Wi-Fi pour l'intégration Telegram, bien que la caméra ne soit pas nécessaire.
   - Alternative : **ESP8266 NodeMCU** ou **Arduino Uno** avec un module ESP8266 pour le Wi-Fi (plus simple si vous n'avez pas besoin de la caméra).
2. **Capteur de son** :
   - **Capteur de son microphone KY-038** ou similaire – Abordable, détecte les niveaux sonores via une sortie analogique.
   - Alternative : **Amplificateur microphone à électret MAX9814** – Plus sensible, avec un gain réglable pour une meilleure détection.
3. **Alimentation** :
   - Adaptateur d'alimentation USB 5V ou batterie externe pour l'ESP32 ou une autre carte.
4. **Montage** :
   - Placez le capteur de son près du lave-linge (par exemple, collé sur le côté ou le dessus) où il peut détecter les sons de fonctionnement, mais évitez toute exposition directe à l'eau.
   - Utilisez un petit boîtier pour protéger le capteur et la carte.
5. **Routeur Wi-Fi** :
   - Pour la connectivité Internet afin d'envoyer les notifications Telegram.

#### Logiciel
- **Arduino IDE** : Pour programmer l'ESP32 ou une autre carte.
- **Bibliothèques** :
  - **Universal Arduino Telegram Bot Library** par Brian Lough – Pour l'intégration Telegram.
  - **ArduinoJson** – Pour gérer les données JSON dans la communication avec l'API Telegram.
- **Bot Telegram** : Identique à avant, utilisez BotFather pour obtenir un jeton de bot et un ID de chat.
- **Langage de programmation** : C++ (sketch Arduino).

---

### Algorithme pour détecter l'état du lave-linge avec le son
Le capteur de son détectera le niveau de bruit produit par le lave-linge. Lorsque la machine fonctionne, elle génère des sons constants (par exemple, moteur, eau ou tambour). Lorsqu'elle s'arrête, le niveau sonore baisse significativement. L'algorithme traite ces niveaux sonores pour déterminer l'état de la machine.

#### Algorithme de détection
1. **Échantillonnage du son** :
   - Lire continuellement la sortie analogique du capteur de son pour mesurer les niveaux de bruit.
2. **Traitement du signal** :
   - **Moyennage** : Calculez le niveau sonore moyen sur une courte fenêtre (par exemple, 1-2 secondes) pour lisser les bruits transitoires (par exemple, un coup de porte).
   - **Seuillage** : Comparez le niveau sonore moyen à un seuil prédéfini. Un niveau élevé indique que la machine fonctionne, tandis qu'un niveau faible suggère qu'elle est arrêtée.
3. **Machine à états** :
   - Suivez l'état de la machine (ON ou OFF) en fonction des niveaux sonores.
   - Si le niveau sonore dépasse le seuil pendant plusieurs cycles, supposez que la machine fonctionne.
   - Si le niveau sonore descend en dessous du seuil et reste faible pendant une période définie (par exemple, 5 minutes), supposez que le cycle de lavage est terminé.
4. **Antirebond** :
   - Implémentez un délai (par exemple, 5 minutes) pour confirmer que la machine s'est arrêtée, évitant ainsi les fausses notifications pendant les phases silencieuses (par exemple, le trempage ou les pauses dans le cycle).
5. **Notification** :
   - Lorsque l'arrêt de la machine est confirmé, envoyez un message Telegram (par exemple, "Le lave-linge s'est arrêté ! C'est le moment d'étendre le linge.").

#### Pourquoi la détection sonore ?
- La détection sonore est plus simple que le traitement d'image, car elle ne nécessite pas d'algorithmes complexes ou de grandes ressources computationnelles.
- Elle est moins sensible aux changements de lumière ambiante par rapport à la détection par caméra.
- Cependant, elle peut être affectée par le bruit de fond (par exemple, une télévision forte), donc le placement et le réglage du seuil sont critiques.

---

### Guide de mise en œuvre
#### Étape 1 : Configurer le bot Telegram
- Suivez les mêmes étapes que dans le guide original :
  - Créez un bot en utilisant **@BotFather** pour obtenir un **Jeton de Bot**.
  - Obtenez votre **ID de Chat** en utilisant **@GetIDsBot** ou en vérifiant les messages entrants.
  - Assurez-vous que Telegram est configuré sur votre téléphone pour recevoir les notifications.

#### Étape 2 : Configuration matérielle
1. **Choisissez un capteur de son** :
   - **KY-038** : Fournit une sortie analogique (0-1023 pour l'ADC 10 bits de l'ESP32) proportionnelle à l'intensité sonore. Il a également une sortie numérique, mais l'analogique est meilleure pour une détection nuancée.
   - **MAX9814** : Plus sensible, avec un gain réglable via un potentiomètre. Connectez-le à une broche analogique.
2. **Connectez le capteur de son** :
   - Pour KY-038 :
     - **VCC** à 5V (ou 3.3V, selon la carte).
     - **GND** à GND.
     - **Sortie Analogique (A0)** à une broche analogique de l'ESP32 (par exemple, GPIO 4).
   - Pour MAX9814 :
     - Connexions similaires, mais ajustez le gain à l'aide du potentiomètre intégré pour une sensibilité optimale.
3. **Positionnez le capteur** :
   - Placez le capteur près du lave-linge (par exemple, sur le côté ou le dessus) où il peut détecter le bruit du moteur ou du tambour. Évitez les zones exposées à l'eau.
   - Testez le placement en surveillant les niveaux sonores pendant un cycle de lavage (utilisez le Moniteur Série pour logger les valeurs).
4. **Alimentez la carte** :
   - Connectez un adaptateur d'alimentation USB 5V ou une batterie externe à l'ESP32 ou à une autre carte.
   - Assurez-vous d'une alimentation stable, car la communication Wi-Fi nécessite une tension constante.
5. **Montage** :
   - Utilisez un petit boîtier ou du ruban adhésif pour fixer le capteur et la carte, en vous assurant que le microphone est exposé pour capter le son.

#### Étape 3 : Configuration logicielle
- **Arduino IDE** : Installez-le comme décrit dans le guide original.
- **Support de la carte ESP32** : Ajoutez le package de la carte ESP32 via le Gestionnaire de cartes (même URL qu'avant).
- **Bibliothèques** :
  - Installez **Universal Arduino Telegram Bot Library** et **ArduinoJson** comme décrit.
- **Wi-Fi** : Assurez-vous que la carte peut se connecter à votre réseau Wi-Fi 2.4GHz.

#### Étape 4 : Écrire le code Arduino
Voici un exemple de sketch Arduino pour l'ESP32 (ou ESP8266) afin de détecter les niveaux sonores et d'envoyer des notifications Telegram. Ceci suppose un capteur de son KY-038 connecté à GPIO 4.

```cpp
#include <WiFi.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>

// Identifiants Wi-Fi
#define WIFI_SSID "votre_ssid_wifi"
#define WIFI_PASSWORD "votre_mot_de_passe_wifi"

// Identifiants du bot Telegram
#define BOT_TOKEN "votre_bot_token"
#define CHAT_ID "votre_chat_id"

// Broche du capteur de son
#define SOUND_PIN 4 // GPIO 4 pour l'entrée analogique

// Paramètres de détection sonore
#define SOUND_THRESHOLD 300 // Ajustez sur la base des tests (0-1023)
#define SAMPLE_WINDOW 2000 // 2 secondes pour le moyennage
#define STOP_DELAY 300000 // 5 minutes en millisecondes

WiFiClientSecure client;
UniversalTelegramBot bot(BOT_TOKEN, client);

bool machineRunning = false;
unsigned long lastOnTime = 0;

void setup() {
  Serial.begin(115200);

  // Connexion au Wi-Fi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");

  // Configuration du client Telegram
  client.setInsecure(); // Par souci de simplicité ; envisagez un SSL approprié en production

  // Configurer la broche du capteur de son
  pinMode(SOUND_PIN, INPUT);
}

void loop() {
  // Échantillonner le niveau sonore sur une fenêtre
  unsigned long startMillis = millis();
  uint32_t totalSound = 0;
  uint16_t sampleCount = 0;

  while (millis() - startMillis < SAMPLE_WINDOW) {
    totalSound += analogRead(SOUND_PIN);
    sampleCount++;
    delay(10); // Petit délai entre les échantillons
  }

  float avgSound = sampleCount > 0 ? (float)totalSound / sampleCount : 0;
  Serial.print("Niveau sonore moyen : ");
  Serial.println(avgSound);

  // Machine à états
  if (avgSound > SOUND_THRESHOLD) {
    if (!machineRunning) {
      machineRunning = true;
      Serial.println("Machine en marche");
    }
    lastOnTime = millis();
  } else {
    if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
      machineRunning = false;
      Serial.println("Machine arrêtée");
      bot.sendMessage(CHAT_ID, "Le lave-linge s'est arrêté ! C'est le moment d'étendre le linge.", "");
    }
  }

  delay(10000); // Vérifier toutes les 10 secondes
}
```

#### Étape 5 : Personnaliser le code
1. **Mettre à jour les identifiants** :
   - Remplacez `votre_ssid_wifi`, `votre_mot_de_passe_wifi`, `votre_bot_token` et `votre_chat_id` par vos valeurs réelles.
2. **Ajuster `SOUND_THRESHOLD`** :
   - Faites fonctionner le lave-linge et surveillez les niveaux sonores via le Moniteur Série (`Serial.println(analogRead(SOUND_PIN));`).
   - Définissez `SOUND_THRESHOLD` à une valeur supérieure au bruit ambiant mais inférieure au bruit de fonctionnement de la machine (par exemple, 200-500, selon votre configuration).
3. **Ajuster `SAMPLE_WINDOW`** :
   - Une fenêtre de 2 secondes (`2000` ms) lisse les bruits transitoires. Augmentez-la si le bruit de fond provoque de fausses lectures.
4. **Ajuster `STOP_DELAY`** :
   - Définissez à `300000` (5 minutes) pour éviter les fausses notifications pendant les phases silencieuses comme le trempage.

#### Étape 6 : Tester et déployer
1. **Téléverser le code** :
   - Connectez l'ESP32 à votre ordinateur via un adaptateur USB-série.
   - Sélectionnez **ESP32 Wrover Module** (ou **NodeMCU** pour ESP8266) dans l'IDE Arduino et téléversez le sketch.
2. **Tester le système** :
   - Démarrez le lave-linge et surveillez le Moniteur Série pour les niveaux sonores et les changements d'état.
   - Vérifiez les notifications Telegram lorsque la machine s'arrête.
3. **Ajustements fins** :
   - Ajustez `SOUND_THRESHOLD` ou `STOP_DELAY` si des faux positifs/négatifs se produisent.
   - Testez dans différentes conditions (par exemple, avec du bruit de fond) pour assurer la fiabilité.
4. **Installation permanente** :
   - Fixez le capteur et la carte dans un boîtier près de la machine, en vous assurant que le microphone est exposé mais protégé de l'eau.

---

### Avantages de la détection sonore
- **Traitement plus simple** : Aucun traitement d'image, réduisant la charge computationnelle sur l'ESP32.
- **Économique** : Les capteurs de son comme le KY-038 sont peu coûteux (souvent moins de 5 $).
- **Non invasif** : Pas besoin d'attacher quoi que ce soit directement au voyant du panneau de la machine.

### Défis et atténuations
- **Bruit de fond** : Les bruits domestiques (par exemple, télévision, conversations) peuvent interférer. Atténuez en :
  - Plaçant le capteur près du moteur ou du tambour de la machine.
  - Ajustant `SOUND_THRESHOLD` pour ignorer le bruit ambiant.
  - Utilisant un microphone directionnel ou en ajustant le gain sur le MAX9814.
- **Phases silencieuses** : Certains cycles de lavage ont des pauses (par exemple, trempage). Le `STOP_DELAY` garantit que les notifications sont envoyées seulement après un silence prolongé.
- **Exposition à l'eau** : Assurez-vous que le capteur est dans un boîtier résistant à l'eau, car les lave-linge peuvent provoquer des éclaboussures ou de l'humidité.

### Améliorations optionnelles
- **Analyse de fréquence** : Si le bruit de fond est un problème persistant, analysez les fréquences sonores (par exemple, le ronronnement du moteur à 50-200 Hz) en utilisant une bibliothèque FFT comme `arduinoFFT`. Cela nécessite plus de puissance de traitement et peut ne pas être réalisable sur un ESP32 basique sans optimisation.
- **Capteurs doubles** : Combinez des capteurs de son et de vibration (par exemple, SW-420) pour la redondance. Si les deux indiquent que la machine est éteinte, la confiance dans la détection augmente.
- **Alimentation par batterie** : Pour la portabilité, utilisez une batterie LiPo rechargeable avec un module de charge (par exemple, TP4056) au lieu d'un adaptateur USB.

---

### Dépannage
- **Aucune détection sonore** : Vérifiez le câblage du capteur, testez avec le Moniteur Série et assurez-vous que le capteur est près de la source de bruit de la machine.
- **Fausses notifications** : Augmentez `STOP_DELAY` ou ajustez `SOUND_THRESHOLD` pour filtrer le bruit de fond ou les pauses du cycle.
- **Problèmes Wi-Fi** : Vérifiez les identifiants Wi-Fi 2.4GHz et la force du signal près de la machine.
- **Aucun message Telegram** : Confirmez le jeton du bot et l'ID de chat, vérifiez le Moniteur Série pour les erreurs.

Cette approche basée sur le son est plus simple et plus robuste dans des conditions d'éclairage variables par rapport à la méthode par caméra, ce qui la rend idéale pour un moniteur de lave-linge. Faites-moi savoir si vous avez besoin d'aide pour des étapes spécifiques, l'étalonnage du capteur ou l'intégration de fonctionnalités supplémentaires !