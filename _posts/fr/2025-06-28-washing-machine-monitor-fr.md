---
audio: false
generated: true
lang: fr
layout: post
title: Moniteur Intelligent de Lave‑Linge avec Arduino et Alertes Telegram
translated: true
type: note
---

Pour créer un système qui détecte quand votre lave-linge Maytag MHW8630HW s'arrête (en utilisant son témoin lumineux comme indicateur) et vous notifie via un bot Telegram pour suspendre vos vêtements, vous pouvez utiliser un Arduino avec un module caméra pour surveiller l'état de la machine. Voici un guide détaillé sur la pile technologique, la configuration matérielle, l'algorithme et les étapes de mise en œuvre.

---

### Pile Technologique
#### Matériel
1. **Carte Arduino** :
   - **ESP32-CAM** (recommandé) – Combine un microcontrôleur avec une caméra OV2640 intégrée et une capacité Wi-Fi, parfait pour le traitement d'image et l'intégration Telegram.
   - Alternative : Arduino Uno + module caméra séparé (ex. OV7670) et ESP8266 pour le Wi-Fi, mais c'est plus complexe à configurer.
2. **Module Caméra** :
   - OV2640 (inclus avec l'ESP32-CAM) – Caméra 2MP suffisante pour détecter le témoin lumineux.
3. **Capteur de Lumière (Optionnel)** :
   - Photorésistance (LDR) ou TSL2561 – Pour compléter la détection de lumière basée sur la caméra pour la redondance ou des configurations plus simples.
4. **Alimentation** :
   - Adaptateur d'alimentation USB 5V ou batterie portable pour l'ESP32-CAM.
5. **Montage** :
   - Petit boîtier ou boîtier imprimé en 3D pour maintenir l'ESP32-CAM, avec une vue dégagée sur le panneau de contrôle du lave-linge.
6. **Routeur Wi-Fi** :
   - Pour que l'ESP32-CAM se connecte à Internet et communique avec le bot Telegram.

#### Logiciel
1. **Arduino IDE** :
   - Pour programmer l'ESP32-CAM.
2. **Bibliothèques** :
   - **Universal Arduino Telegram Bot Library** par Brian Lough – Pour l'intégration du bot Telegram.
   - **ArduinoJson** – Pour gérer les données JSON pour la communication avec l'API Telegram.
   - **Bibliothèques Caméra ESP32-CAM** – Bibliothèques intégrées pour capturer et traiter les images.
3. **Bot Telegram** :
   - Utilisez BotFather sur Telegram pour créer un bot et obtenir un jeton de bot et un ID de chat.
4. **Langage de Programmation** :
   - C++ (sketch Arduino).
5. **Outils Optionnels** :
   - OpenCV (Python) pour prototyper les algorithmes de traitement d'image sur un ordinateur avant de les porter sur Arduino (simplifié pour l'ESP32-CAM).

---

### Algorithme pour Détecter l'État du Lave-linge
Étant donné que le Maytag MHW8630HW a un témoin lumineux qui indique quand la machine est allumée, vous pouvez utiliser la caméra pour détecter cette lumière. L'algorithme traitera les images pour déterminer si la lumière est allumée ou éteinte, indiquant l'état de la machine.

#### Algorithme de Détection
1. **Capture d'Image** :
   - Capturer périodiquement des images du panneau de contrôle du lave-linge en utilisant l'ESP32-CAM.
2. **Sélection de la Région d'Intérêt (ROI)** :
   - Définir une zone spécifique dans l'image où se trouve le témoin lumineux (ex. une région rectangulaire autour de l'indicateur de puissance).
3. **Traitement d'Image** :
   - **Conversion en Niveaux de Gris** : Convertir l'image capturée en niveaux de gris pour simplifier le traitement.
   - **Seuillage** : Appliquer un seuil de luminosité pour détecter la présence de la lumière. Le témoin lumineux produira une tache lumineuse lorsqu'il est allumé, comparé à une zone plus sombre lorsqu'il est éteint.
   - **Analyse de l'Intensité des Pixels** : Calculer l'intensité moyenne des pixels dans la ROI. Une intensité élevée indique que la lumière est allumée, tandis qu'une intensité faible indique qu'elle est éteinte.
4. **Machine à États** :
   - Suivre l'état de la machine (ALLUMÉ ou ÉTEINT) sur la base de lectures consécutives.
   - Si la lumière est détectée comme ALLUMÉE pendant plusieurs cycles, supposer que la machine fonctionne.
   - Si la lumière passe à ÉTEINT et reste éteinte pendant une période définie (ex. 5 minutes), supposer que le cycle de lavage est terminé.
5. **Antirebond** :
   - Implémenter un délai (ex. 5 minutes) pour confirmer que la machine s'est arrêtée, évitant les fausses notifications pendant les pauses du cycle de lavage (ex. trempage ou remplissage).
6. **Notification** :
   - Lorsque l'arrêt de la machine est confirmé, envoyer un message Telegram (ex. "Le lave-linge s'est arrêté ! Il est temps de suspendre les vêtements.").

#### Pourquoi ne pas Utiliser des Algorithmes Plus Complexes ?
- Les algorithmes avancés comme l'apprentissage automatique (ex. les CNN pour la détection d'objet) sont excessifs pour cette tâche et trop gourmands en ressources pour la puissance de traitement limitée de l'ESP32-CAM.
- Un simple seuillage est suffisant puisque le témoin lumineux est un indicateur binaire clair (ALLUMÉ/ÉTEINT).

---

### Guide de Mise en Œuvre
#### Étape 1 : Configurer le Bot Telegram
1. **Créer un Bot Telegram** :
   - Ouvrez Telegram, recherchez **@BotFather** et démarrez une conversation.
   - Envoyez `/newbot`, nommez votre bot (ex. "WasherBot") et obtenez le **Jeton du Bot**.
   - Envoyez `/start` à votre bot et obtenez votre **ID de Chat** en utilisant un service comme `@GetIDsBot` ou en vérifiant les messages entrants dans votre code.
2. **Installer Telegram sur Votre Téléphone** :
   - Assurez-vous de pouvoir recevoir des messages de votre bot.

#### Étape 2 : Configuration Matérielle
1. **Positionner l'ESP32-CAM** :
   - Montez l'ESP32-CAM dans un petit boîtier ou avec du ruban adhésif, face au panneau de contrôle du lave-linge.
   - Assurez-vous que la caméra a une vue dégagée sur le témoin lumineux (testez avec une photo d'essai).
   - Fixez la configuration pour éviter les mouvements, car cela pourrait affecter la constance de la ROI.
2. **Alimenter l'ESP32-CAM** :
   - Connectez un adaptateur d'alimentation USB 5V ou une batterie portable à la broche 5V de l'ESP32-CAM.
   - Assurez-vous d'une source d'alimentation stable, car la caméra et le Wi-Fi consomment beaucoup d'énergie.
3. **Capteur de Lumière Optionnel** :
   - Si vous utilisez une photorésistance, connectez-la à une broche analogique de l'ESP32-CAM (ex. GPIO 4) avec un circuit diviseur de tension (ex. une résistance de 10kΩ à la masse).

#### Étape 3 : Configuration Logicielle
1. **Installer Arduino IDE** :
   - Téléchargez et installez Arduino IDE depuis [arduino.cc](https://www.arduino.cc/en/software).
2. **Ajouter le Support de la Carte ESP32** :
   - Dans Arduino IDE, allez dans **Fichier > Préférences**, ajoutez l'URL suivante aux URLs supplémentaires du Gestionnaire de Cartes :
     ```
     https://raw.githubusercontent.com/espressif/arduino-esp32/master/package_esp32_index.json
     ```
   - Allez dans **Outils > Carte > Gestionnaire de Cartes**, recherchez "ESP32" et installez le package ESP32.
3. **Installer les Bibliothèques** :
   - Installez **Universal Arduino Telegram Bot Library** :
     - Téléchargez depuis [GitHub](https://github.com/witnessmenow/Universal-Arduino-Telegram-Bot) et ajoutez via **Croquis > Inclure une bibliothèque > Ajouter la bibliothèque .ZIP**.
   - Installez **ArduinoJson** :
     - Allez dans **Croquis > Inclure une bibliothèque > Gérer les bibliothèques**, recherchez "ArduinoJson" et installez la version 6.x.x.
4. **Configurer le Wi-Fi** :
   - Assurez-vous que votre ESP32-CAM peut se connecter à votre réseau Wi-Fi domestique (2.4GHz, car le 5GHz n'est pas supporté).

#### Étape 4 : Écrire le Code Arduino
Voici un exemple de sketch Arduino pour l'ESP32-CAM afin de détecter le témoin lumineux et envoyer des notifications Telegram. Ce code suppose que vous avez identifié les coordonnées de la ROI pour le témoin lumineux.

```cpp
#include <WiFi.h>
#include <UniversalTelegramBot.h>
#include <ArduinoJson.h>
#include "esp_camera.h"

// Identifiants Wi-Fi
#define WIFI_SSID "votre_ssid_wifi"
#define WIFI_PASSWORD "votre_mot_de_passe_wifi"

// Identifiants du Bot Telegram
#define BOT_TOKEN "votre_bot_token"
#define CHAT_ID "votre_chat_id"

// Configuration de la caméra (pour ESP32-CAM)
#define PWDN_GPIO_NUM 32
#define RESET_GPIO_NUM -1
#define XCLK_GPIO_NUM 0
#define SIOD_GPIO_NUM 26
#define SIOC_GPIO_NUM 27
#define Y9_GPIO_NUM 35
#define Y8_GPIO_NUM 34
#define Y7_GPIO_NUM 39
#define Y6_GPIO_NUM 36
#define Y5_GPIO_NUM 21
#define Y4_GPIO_NUM 19
#define Y3_GPIO_NUM 18
#define Y2_GPIO_NUM 5
#define VSYNC_GPIO_NUM 25
#define HREF_GPIO_NUM 23
#define PCLK_GPIO_NUM 22

WiFiClientSecure client;
UniversalTelegramBot bot(BOT_TOKEN, client);

#define ROI_X 100 // Ajuster basé sur la vue de la caméra (coordonnée x de la ROI)
#define ROI_Y 100 // coordonnée y de la ROI
#define ROI_WIDTH 50 // Largeur de la ROI
#define ROI_HEIGHT 50 // Hauteur de la ROI
#define THRESHOLD 150 // Seuil de luminosité (0-255)
#define STOP_DELAY 300000 // 5 minutes en millisecondes

bool machineRunning = false;
unsigned long lastOnTime = 0;

void setup() {
  Serial.begin(115200);

  // Initialiser la caméra
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_GRAYSCALE; // Niveaux de gris pour la simplicité
  config.frame_size = FRAMESIZE_QVGA; // 320x240
  config.jpeg_quality = 12;
  config.fb_count = 1;

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Échec de l'initialisation de la caméra avec l'erreur 0x%x", err);
    return;
  }

  // Se connecter au Wi-Fi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connecté");

  // Configurer le client Telegram
  client.setInsecure(); // Pour la simplicité ; envisagez un SSL approprié en production
}

void loop() {
  // Capturer une image
  camera_fb_t *fb = esp_camera_framebuffer_get();
  if (!fb) {
    Serial.println("Échec de la capture de la caméra");
    return;
  }

  // Calculer la luminosité moyenne dans la ROI
  uint32_t totalBrightness = 0;
  uint16_t pixelCount = 0;
  for (int y = ROI_Y; y < ROI_Y + ROI_HEIGHT; y++) {
    for (int x = ROI_X; x < ROI_X + ROI_WIDTH; x++) {
      if (x < fb->width && y < fb->height) {
        totalBrightness += fb->buf[y * fb->width + x];
        pixelCount++;
      }
    }
  }
  esp_camera_framebuffer_return(fb);

  float avgBrightness = pixelCount > 0 ? (float)totalBrightness / pixelCount : 0;

  // Machine à états
  if (avgBrightness > THRESHOLD) {
    if (!machineRunning) {
      machineRunning = true;
      Serial.println("La machine est ON");
    }
    lastOnTime = millis();
  } else {
    if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
      machineRunning = false;
      Serial.println("La machine s'est arrêtée");
      bot.sendMessage(CHAT_ID, "Le lave-linge s'est arrêté ! Il est temps de suspendre les vêtements.", "");
    }
  }

  delay(10000); // Vérifier toutes les 10 secondes
}
```

#### Étape 5 : Personnaliser le Code
1. **Mettre à Jour les Identifiants** :
   - Remplacez `votre_ssid_wifi`, `votre_mot_de_passe_wifi`, `votre_bot_token` et `votre_chat_id` par vos valeurs réelles.
2. **Ajuster la ROI et le Seuil** :
   - Capturez une image de test en utilisant l'ESP32-CAM (modifiez le code pour sauvegarder une image sur une carte SD ou pour la diffuser).
   - Déterminez les coordonnées de la ROI (`ROI_X`, `ROI_Y`, `ROI_WIDTH`, `ROI_HEIGHT`) en analysant l'image pour vous concentrer sur le témoin lumineux.
   - Ajustez `THRESHOLD` en fonction des images de test (ex. plus lumineux quand ALLUMÉ, plus sombre quand ÉTEINT).
3. **Ajuster `STOP_DELAY`** :
   - Réglez à 300000 (5 minutes) pour éviter les fausses notifications pendant les pauses du cycle.

#### Étape 6 : Tester et Déployer
1. **Téléverser le Code** :
   - Connectez l'ESP32-CAM à votre ordinateur via un adaptateur USB-série (ex. module FTDI).
   - Sélectionnez **ESP32 Wrover Module** dans Arduino IDE et téléversez le sketch.
2. **Tester le Système** :
   - Démarrez le lave-linge et surveillez le Moniteur Série pour les changements d'état.
   - Vérifiez les notifications Telegram lorsque la machine s'arrête.
3. **Ajuster Finement** :
   - Ajustez la ROI, le seuil ou le délai si des faux positifs/négatifs se produisent.
4. **Installation Permanente** :
   - Fixez l'ESP32-CAM dans son boîtier et assurez-vous d'une alimentation stable.

---

### Approche Alternative : Capteur de Lumière
Si la détection basée sur la caméra est trop complexe ou peu fiable (ex. à cause de la lumière ambiante), utilisez une photorésistance :
- **Configuration** : Fixez une photorésistance au témoin lumineux (ex. avec du ruban adhésif) et connectez-la à une broche analogique.
- **Modification du Code** : Remplacez le traitement d'image par des lectures analogiques :
  ```cpp
  int lightValue = analogRead(A0); // Photorésistance sur GPIO 4
  if (lightValue > 500) { // Ajuster le seuil
    machineRunning = true;
    lastOnTime = millis();
  } else if (machineRunning && (millis() - lastOnTime > STOP_DELAY)) {
    machineRunning = false;
    bot.sendMessage(CHAT_ID, "Le lave-linge s'est arrêté ! Il est temps de suspendre les vêtements.", "");
  }
  ```
- **Avantages** : Plus simple, moins gourmand en ressources.
- **Inconvénients** : Nécessite une fixation physique à la lumière, moins flexible.

---

### Notes
- **Consommation d'Énergie** : L'ESP32-CAM consomme beaucoup d'énergie lors de l'utilisation de la caméra et du Wi-Fi. Assurez-vous d'une source d'alimentation fiable.
- **Lumière Ambiante** : La détection basée sur la caméra peut être affectée par l'éclairage de la pièce. Testez dans diverses conditions ou utilisez un capteur de lumière pour une meilleure robustesse.
- **Sécurité** : Le code exemple utilise `setInsecure()` pour la simplicité. Pour la production, configurez des certificats SSL appropriés pour la communication Telegram.
- **Références** : Cette approche est inspirée par des projets comme le système de sécurité ESP32-CAM Telegram et les moniteurs de linge utilisant des capteurs de vibration, adaptés pour la détection basée sur la lumière.[](https://www.instructables.com/Home-Security-System-Using-ESP32-CAM-and-Telegram-/)[](https://www.instructables.com/Arduino-Washer-Dryer-Alert-Push-Notification-to-Ph/)

---

### Dépannage
- **Échec de l'Initialisation de la Caméra** : Vérifiez le câblage, assurez une alimentation suffisante et vérifiez la configuration de la caméra.
- **Problèmes de Connexion Wi-Fi** : Confirmez le Wi-Fi 2.4GHz et les identifiants corrects.
- **Aucun Message Telegram** : Vérifiez le jeton du bot et l'ID de chat, vérifiez le Moniteur Série pour les erreurs.
- **Fausses Notifications** : Ajustez `THRESHOLD` ou `STOP_DELAY` pour tenir compte des pauses du cycle.

Cette solution tire parti des capacités de l'ESP32-CAM pour une manière économique et non invasive de surveiller votre lave-linge et de vous notifier via Telegram. Faites-moi savoir si vous avez besoin d'aide pour des étapes spécifiques ou du débogage !