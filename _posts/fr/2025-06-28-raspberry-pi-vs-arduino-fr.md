---
audio: false
generated: true
lang: fr
layout: post
title: Raspberry Pi contre Arduino pour la surveillance de lave-linge avec alertes
  Telegram
translated: true
type: note
---

Utiliser un Raspberry Pi au lieu d'un Arduino (comme l'ESP32-CAM) pour détecter l'arrêt de votre lave-linge Maytag MHW8630HW et envoyer une notification Telegram est une alternative viable, offrant plus de puissance de traitement et de flexibilité au prix d'une complexité et d'une consommation électrique accrues. Ci-dessous, je comparerai l'approche Raspberry Pi avec la solution Arduino, je décrirai d'autres options de microcontrôleurs et je fournirai un guide détaillé pour mettre en œuvre le système avec un Raspberry Pi. Je discuterai également d'approches alternatives (par exemple, d'autres matériels ou capteurs) pour assurer une réponse complète.

---

### Comparaison : Raspberry Pi vs. Arduino vs. Autres Options

| **Fonctionnalité**         | **Raspberry Pi**                                                                 | **Arduino (ESP32-CAM)**                                                  | **Autres Options (ex. NodeMCU, ESP8266)**                              |
|----------------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Puissance de traitement**| Élevée (CPU quad-core, 1-8 Go RAM) – Prend en charge le traitement d'image avancé, OpenCV. | Limitée (double cœur, 520 Ko SRAM) – Traitement d'image basique uniquement. | Très limitée – Non adaptée au traitement basé sur caméra.                 |
| **Support de la caméra**   | Facile avec webcams USB ou Pi Camera Module (ex. Pi Camera v2 8MP).             | Caméra intégrée OV2640 (2MP), mais résolution et qualité inférieures.     | Nécessite un module caméra externe, complexe à intégrer.                  |
| **Wi-Fi**                  | Intégré (la plupart des modèles, ex. Pi 4, Zero 2 W).                           | Intégré (ESP32-CAM).                                                    | Intégré (ex. ESP8266), mais pas de support natif pour la caméra.         |
| **Programmation**           | Python, OpenCV, polyvalent mais nécessite la configuration d'un OS (Raspberry Pi OS). | C++ dans l'IDE Arduino, plus simple pour les débutants.                 | C++ ou Lua (ex. NodeMCU), bibliothèques limitées pour le traitement d'image. |
| **Consommation électrique** | Plus élevée (~2,5W pour Pi Zero, ~5-10W pour Pi 4).                             | Plus faible (~1-2W pour ESP32-CAM).                                     | La plus faible (~0,5-1W pour ESP8266).                                  |
| **Coût**                   | 10 $ (Pi Zero W) à 35 $+ (Pi 4) + 15 $ pour Pi Camera.                          | ~10 $ (ESP32-CAM avec caméra).                                          | ~5-10 $ (ESP8266/NodeMCU) + coût des capteurs.                          |
| **Facilité d'installation**| Modérée (configuration de l'OS, codage Python).                                 | Facile (IDE Arduino, un seul sketch).                                   | Facile pour les capteurs simples, complexe pour les caméras.            |
| **Cas d'usage optimal**    | Traitement d'image avancé, flexible pour des extensions futures (ex. modèles de ML). | Détection lumineuse simple et peu coûteuse avec intégration Telegram.   | Solutions sans caméra (ex. capteurs de vibration ou de courant).        |

**Avantages du Raspberry Pi** :
- Traitement d'image supérieur avec OpenCV pour une détection lumineuse robuste.
- Plus facile à déboguer et à étendre (ex. ajouter une interface web ou plusieurs capteurs).
- Prend en charge des caméras de meilleure qualité pour une précision accrue dans diverses conditions d'éclairage.

**Inconvénients du Raspberry Pi** :
- Nécessite plus de configuration (installation de l'OS, environnement Python).
- Consommation électrique plus élevée, moins idéal pour les configurations sur batterie.
- Plus coûteux que l'ESP32-CAM.

**Autres Options** :
- **NodeMCU/ESP8266** : Adapté pour les solutions sans caméra (ex. utilisation d'un capteur de vibration ou de courant). La puissance de traitement limitée rend l'intégration d'une caméra peu pratique.
- **Capteur de vibration** : Détecte les vibrations de la machine au lieu du témoin lumineux. Simple mais peut manquer des changements de cycle subtils.
- **Capteur de courant** : Mesure la consommation électrique (ex. module ACS712) pour détecter l'arrêt de la machine. Non invasif mais nécessite une installation électrique.

---

### Guide de mise en œuvre avec Raspberry Pi

#### Stack technique
**Matériel** :
1. **Raspberry Pi** :
   - **Raspberry Pi Zero 2 W** (15 $, compact, avec Wi-Fi) ou **Raspberry Pi 4** (35 $+, plus puissant).
2. **Caméra** :
   - **Raspberry Pi Camera Module v2** (15 $, 8MP) ou une webcam USB.
3. **Alimentation** :
   - 5V USB-C (Pi 4) ou micro-USB (Pi Zero) avec une sortie de 2-3A.
4. **Montage** :
   - Boîtier ou support adhésif pour positionner la caméra face au témoin lumineux du lave-linge.

**Logiciel** :
1. **OS** : Raspberry Pi OS (Lite pour l'efficacité, Full pour une installation plus facile).
2. **Langage de programmation** : Python.
3. **Bibliothèques** :
   - **OpenCV** : Pour le traitement d'image afin de détecter le témoin lumineux.
   - **python-telegram-bot** : Pour les notifications Telegram.
   - **picamera2** (pour Pi Camera) ou **fswebcam** (pour webcam USB).
4. **Bot Telegram** : Même configuration que pour Arduino (utilisez BotFather pour le token du bot et le chat ID).

#### Algorithme
L'algorithme est similaire à l'approche Arduino mais tire parti d'OpenCV pour un traitement d'image plus robuste :
1. **Capture d'image** : Utilisez la Pi Camera ou la webcam pour capturer des images périodiquement (ex. toutes les 10 secondes).
2. **Région d'intérêt (ROI)** : Définissez un rectangle autour du témoin lumineux dans l'image.
3. **Traitement d'image** :
   - Conversion en niveaux de gris.
   - Application d'un flou gaussien pour réduire le bruit.
   - Utilisation d'un seuillage adaptatif pour détecter le témoin lumineux brillant par rapport à l'arrière-plan.
   - Calcul de l'intensité moyenne des pixels dans la ROI ou comptage des pixels clairs.
4. **Machine à états** :
   - Si la ROI est claire (lumière ALLUMÉE), marquez la machine comme en marche.
   - Si la ROI est sombre (lumière ÉTEINTE) pendant 5 minutes, marquez la machine comme arrêtée et envoyez une notification Telegram.
5. **Antirebond** : Implémentez un délai de 5 minutes pour confirmer l'arrêt de la machine.

#### Étapes de mise en œuvre
1. **Configurez le Raspberry Pi** :
   - Téléchargez et flashez **Raspberry Pi OS** (Lite ou Full) sur une carte SD à l'aide de Raspberry Pi Imager.
   - Connectez le Pi au Wi-Fi en éditant `/etc/wpa_supplicant/wpa_supplicant.conf` ou via l'interface graphique.
   - Activez l'interface de la caméra via `raspi-config` (Options d'interfaçage > Camera).

2. **Installez les dépendances** :
   ```bash
   sudo apt update
   sudo apt install python3-opencv python3-picamera2 python3-pip
   pip3 install python-telegram-bot
   ```

3. **Positionnez la caméra** :
   - Montez la Pi Camera ou la webcam USB pour qu'elle soit face au témoin lumineux du lave-linge.
   - Testez la caméra avec :
     ```bash
     libcamera-still -o test.jpg
     ```
     ou pour une webcam USB :
     ```bash
     fswebcam test.jpg
     ```

4. **Script Python** :
Ci-dessous un exemple de script Python pour le Raspberry Pi afin de détecter le témoin lumineux et envoyer des notifications Telegram.

```python
import cv2
import numpy as np
from picamera2 import Picamera2
import telegram
import asyncio
import time

# Configuration du bot Telegram
BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"
bot = telegram.Bot(token=BOT_TOKEN)

# Configuration de la caméra
picam2 = Picamera2()
picam2.configure(picam2.create_still_configuration(main={"size": (640, 480)}))
picam2.start()

# Configuration de la ROI (ajuster en fonction de la vue de la caméra)
ROI_X, ROI_Y, ROI_WIDTH, ROI_HEIGHT = 200, 150, 50, 50
THRESHOLD = 150  # Seuil de luminosité (0-255)
STOP_DELAY = 300  # 5 minutes en secondes

machine_running = False
last_on_time = 0

async def send_telegram_message(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)

def is_light_on(frame):
    # Conversion en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Application d'un flou gaussien
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # Extraction de la ROI
    roi = gray[ROI_Y:ROI_Y+ROI_HEIGHT, ROI_X:ROI_X+ROI_WIDTH]
    # Calcul de la luminosité moyenne
    avg_brightness = np.mean(roi)
    return avg_brightness > THRESHOLD

async def main():
    global machine_running, last_on_time
    while True:
        # Capture d'image
        frame = picam2.capture_array()
        # Vérifier si la lumière est allumée
        if is_light_on(frame):
            if not machine_running:
                machine_running = True
                print("Machine is ON")
            last_on_time = time.time()
        else:
            if machine_running and (time.time() - last_on_time > STOP_DELAY):
                machine_running = False
                print("Machine stopped")
                await send_telegram_message("Washing machine stopped! Time to hang up clothes.")
        time.sleep(10)  # Vérifier toutes les 10 secondes

if __name__ == "__main__":
    asyncio.run(main())
```

5. **Personnalisez le script** :
   - Remplacez `BOT_TOKEN` et `CHAT_ID` par vos identifiants Telegram.
   - Ajustez `ROI_X`, `ROI_Y`, `ROI_WIDTH`, `ROI_HEIGHT` en capturant une image test et en l'analysant avec un outil comme GIMP ou Python pour localiser le témoin lumineux.
   - Ajustez `THRESHOLD` en fonction des images tests (plus élevé pour des lumières plus brillantes).
   - Modifiez `STOP_DELAY` si nécessaire.

6. **Exécutez le script** :
   ```bash
   python3 washer_monitor.py
   ```
   - Exécutez en arrière-plan avec `nohup python3 washer_monitor.py &` ou utilisez un service systemd pour la fiabilité.

7. **Testez et déployez** :
   - Démarrez le lave-linge et surveillez la sortie du script.
   - Vérifiez les notifications Telegram.
   - Fixez le Pi et la caméra dans une installation permanente.

---

### Autres Alternatives
1. **Capteur de vibration** :
   - **Matériel** : Utilisez un capteur de vibration (ex. SW-420) avec un ESP8266 ou un Raspberry Pi.
   - **Installation** : Fixez le capteur sur le lave-linge pour détecter les vibrations.
   - **Algorithme** : Surveillez l'absence soutenue de vibrations (ex. 5 minutes) pour détecter l'arrêt de la machine.
   - **Avantages** : Simple, peu coûteux, non affecté par la lumière ambiante.
   - **Inconvénients** : Peut manquer des cycles avec de longues pauses (ex. trempage).
   - **Exemple de code (ESP8266)** :
     ```cpp
     #include <ESP8266WiFi.h>
     #include <UniversalTelegramBot.h>
     #define VIBRATION_PIN D5
     #define BOT_TOKEN "your_bot_token"
     #define CHAT_ID "your_chat_id"
     WiFiClientSecure client;
     UniversalTelegramBot bot(BOT_TOKEN, client);
     bool machineRunning = false;
     unsigned long lastVibrationTime = 0;
     void setup() {
       pinMode(VIBRATION_PIN, INPUT);
       WiFi.begin("ssid", "password");
       while (WiFi.status() != WL_CONNECTED) delay(500);
       client.setInsecure();
     }
     void loop() {
       if (digitalRead(VIBRATION_PIN)) {
         machineRunning = true;
         lastVibrationTime = millis();
       } else if (machineRunning && (millis() - lastVibrationTime > 300000)) {
         machineRunning = false;
         bot.sendMessage(CHAT_ID, "Washing machine stopped!", "");
       }
       delay(1000);
     }
     ```

2. **Capteur de courant** :
   - **Matériel** : Utilisez un capteur de courant ACS712 avec un ESP8266 ou un Raspberry Pi.
   - **Installation** : Fixez le capteur de manière non invasive autour du câble d'alimentation du lave-linge.
   - **Algorithme** : Détectez quand le courant descend en dessous d'un seuil (ex. <0,5A) pendant 5 minutes.
   - **Avantages** : Précis, non invasif.
   - **Inconvénients** : Nécessite des connaissances en électricité, calibration pour la consommation de la machine.

3. **Microphones** :
   - **Matériel** : Utilisez un module microphone (ex. KY-038) avec un Raspberry Pi.
   - **Algorithme** : Analysez les niveaux sonores pour détecter l'arrêt du bruit de la machine.
   - **Avantages** : Non visuel, fonctionne en conditions de faible éclairage.
   - **Inconvénients** : Sensible au bruit ambiant, nécessite du traitement du signal.

---

### Recommandation
- **Raspberry Pi** : Meilleur pour un traitement d'image robuste et une extensibilité future. À utiliser si vous êtes à l'aise avec Python et souhaitez une grande fiabilité dans diverses conditions d'éclairage.
- **Arduino (ESP32-CAM)** : Meilleur pour une installation simple et peu coûteuse. Idéal si vous voulez une configuration minimale et êtes satisfait d'un traitement d'image basique.
- **Capteur de vibration ou de courant** : Meilleur pour les solutions sans caméra, surtout si le témoin lumineux est peu fiable (ex. faible ou obscurci). À utiliser avec un ESP8266 pour la simplicité.
- **Microphone** : Moins fiable à cause du bruit ambiant, mais viable comme capteur secondaire.

Pour votre maison à deux étages, le Raspberry Pi ou l'ESP32-CAM avec une caméra est idéal puisque vous êtes au deuxième étage et avez besoin de notifications à distance fiables via Telegram. Le Raspberry Pi offre une meilleure précision pour la détection lumineuse, tandis que l'ESP32-CAM est moins cher et plus simple à déployer. Si vous préférez une approche sans caméra, un capteur de vibration avec un ESP8266 est l'alternative la plus simple.

Faites-moi savoir si vous souhaitez approfondir une approche spécifique, si vous avez besoin d'aide pour la configuration ou si vous voulez du code pour un capteur alternatif !