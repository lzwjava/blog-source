---
audio: false
generated: true
image: false
lang: fr
layout: post
model: x-ai/grok-4-fast
title: Charge Utile Drone Scanner WiFi Arduino
translated: true
type: note
---

### Aperçu de la faisabilité
Lier directement un Arduino à un DJI Mini 3 pour contrôler son vol (par exemple, pour des patrouilles autonomes dans le quartier) tout en scannant les signaux WiFi n'est pas simple ou nativement pris en charge. L'écosystème de DJI est propriétaire, et le contrôleur de vol du Mini 3 n'est pas exposé pour une intégration facile avec un microcontrôleur comme Arduino. Cependant, une configuration hybride est possible avec des solutions de contournement : utiliser des applications tierces pour un vol autonome de base, et monter un scanner WiFi séparé basé sur Arduino comme charge utile. Je vais décomposer cela étape par étape, en incluant les défis techniques, une approche viable et des ébauches de code.

### Défis principaux
- **Contrôle de vol** : Le DJI Mini 3 supporte le Mobile SDK pour des applications personnalisées (Android/iOS) qui permettent des missions par points de passage ou un contrôle par joystick virtuel pour un vol semi-autonome. Mais ce SDK ne fonctionne pas sur du matériel embarqué comme Arduino — il est réservé aux mobiles. Il n'y a pas de Onboard SDK pour le Mini 3 (celui-ci est pour les drones professionnels comme la série Matrice). Le piratage du contrôleur de vol (par exemple, via le reverse-engineering du protocole OcuSync) existe pour des déverrouillages comme les limites d'altitude, mais il n'y a pas d'intégrations documentées d'Arduino pour une autonomie de vol complète.
- **Liaison matérielle** : Vous ne pouvez pas câbler directement un Arduino aux composants internes du Mini 3 sans risquer des dommages ou annuler la garantie. Le drone pèse moins de 250g pour la réglementation, donc l'ajout d'une charge utile (Arduino + module WiFi) doit rester léger (~10-20g max pour éviter les problèmes).
- **Scan WiFi** : C'est la partie facile — Arduino excelle ici avec des modules additionnels comme l'ESP32.
- **Aspects légaux/éthiques** : Scanner le WiFi (wardriving) via un drone pourrait violer les lois sur la vie privée (par exemple, la FCC aux États-Unis) ou les réglementations sur les drones (VLOS requis). Restez sur votre propriété ou obtenez les autorisations.

### Approche viable : Configuration hybride
1.  **Vol autonome via une application** : Utilisez des applications comme Litchi, Dronelink, ou DroneDeploy (via le Mobile SDK) pour des vols basés sur des points de passage autour du quartier. Préparez un itinéraire dans l'application (par exemple, un motif en grille à 50m d'altitude). Cela gère le décollage, la navigation et le retour à la maison — aucun Arduino n'est nécessaire pour le vol.
2.  **Monter l'Arduino comme charge utile** : Fixez un Arduino léger (par exemple, une carte Nano ou ESP32) sous le drone avec des attaches zip ou un support imprimé en 3D. Alimentez-le via le port USB du drone ou une petite batterie LiPo.
3.  **Scan WiFi sur Arduino** : Programmez l'ESP32 (programmable via l'IDE Arduino) pour scanner les SSID, le RSSI (force du signal), les canaux, le chiffrement et des estimations du débit. Enregistrez les données sur une carte SD ou transmettez-les via Bluetooth/WiFi vers votre téléphone/station au sol.
4.  **Synchronisation** : Déclenchez les scans périodiquement (par exemple, toutes les 10s) pendant le vol. Utilisez un module GPS sur l'Arduino (par exemple, NEO-6M) pour géolocaliser les scans, ou synchronisez les horodatages avec la télémétrie du drone si elle est accessible via l'application SDK.
5.  **Coût/Poids total** : ~20-30$ pour les pièces ; maintient un total sous 249g.

De cette façon, l'Arduino "accumule" les données indépendamment pendant que le drone vole de manière autonome via le logiciel.

### Exemple de code Arduino pour le scanner WiFi
Utilisez une carte ESP32 (elle est compatible Arduino et intègre le WiFi). Câblez un module de carte SD pour l'enregistrement. Installez les bibliothèques : `WiFi`, `SD`, `TinyGPS++` (pour le GPS si ajouté).

```cpp
#include <WiFi.h>
#include <SD.h>
#include <TinyGPS++.h>  // Optionnel pour la géolocalisation GPS

// Broche de sélection de la carte SD
const int chipSelect = 5;

// Configuration GPS (si utilisation de Serial1 pour le module GPS)
TinyGPSPlus gps;
HardwareSerial gpsSerial(1);

void setup() {
  Serial.begin(115200);
  gpsSerial.begin(9600, SERIAL_8N1, 16, 17);  // RX=16, TX=17 pour le GPS
  
  // Initialiser la carte SD
  if (!SD.begin(chipSelect)) {
    Serial.println("Échec de l'initialisation de la carte SD !");
    return;
  }
  Serial.println("Scanner WiFi prêt. Démarrage des scans...");
}

void loop() {
  // Scanner les réseaux WiFi
  int n = WiFi.scanNetworks();
  if (n == 0) {
    Serial.println("Aucun réseau trouvé");
  } else {
    File dataFile = SD.open("/wifi_log.txt", FILE_APPEND);
    if (dataFile) {
      dataFile.print("Scan à : " + String(millis()) + "ms | ");
      
      // Optionnel : Ajouter le GPS si disponible
      if (gpsSerial.available() > 0) {
        if (gps.encode(gpsSerial.read())) {
          if (gps.location.isValid()) {
            dataFile.print("Lat: " + String(gps.location.lat(), 6) + ", Lng: " + String(gps.location.lng(), 6) + " | ");
          }
        }
      }
      
      for (int i = 0; i < n; ++i) {
        dataFile.print("SSID: " + WiFi.SSID(i) + " | RSSI: " + String(WiFi.RSSI(i)) + "dBm | Ch: " + String(WiFi.channel(i)) + " | Enc: " + String(WiFi.encryptionType(i)) + " | ");
        // Estimation du débit : Calcul approximatif à partir du RSSI (pas précis, mais approximatif)
        int bitrate = map(WiFi.RSSI(i), -100, -30, 1, 100);  // Échelle approximative en Mbps
        dataFile.print("Débit estimé: " + String(bitrate) + "Mbps | ");
      }
      dataFile.println();
      dataFile.close();
      Serial.println("Données enregistrées sur la carte SD");
    }
  }
  
  WiFi.scanDelete();  // Effacer les résultats
  delay(10000);  // Scanner toutes les 10 secondes (ajuster selon la vitesse de vol)
}
```

- **Comment cela fonctionne** : Scanne tous les réseaux visibles, enregistre le SSID, la force du signal (RSSI), le canal, le chiffrement et une estimation approximative du débit. Ajoutez le GPS pour des données liées à la position.
- **Accumulation** : Ajoute les données dans `/wifi_log.txt` sur la carte SD. Après le vol, lisez-la sur votre ordinateur pour la cartographie (par exemple, avec Python et Folium).
- **Améliorations** : Ajoutez un module Bluetooth (HC-05) pour diffuser les données en direct sur votre téléphone pendant le vol.

### Limitations & Alternatives
- **Pas d'autonomie complète depuis Arduino** : Si vous insistez pour un pilotage par Arduino, construisez un drone personnalisé (par exemple, avec le firmware MultiWii sur Arduino) au lieu de pirater le Mini 3 — plus sûr et moins cher pour apprendre.
- **Portée/Sécurité** : La portée de 10 km du Mini 3 est excellente, mais le vent/les obstacles limitent les vols en quartier. Testez dans des zones dégagées.
- **Si vous améliorez** : Le Mini 3 Pro a un meilleur support SDK pour les missions avancées.

Cette configuration vous permet d'atteindre 80% de l'objectif sans piratage profond. Si vous partagez plus de détails (par exemple, le modèle exact d'Arduino), je peux affiner le code.

### Références
- [Documentation du DJI Mobile SDK](https://developer.dji.com/mobile-sdk)
- [Annonce du support SDK pour le DJI Mini 3](https://dronedj.com/2023/04/13/dji-sdk-mini-3-pro/)
- [Tutoriel de scanner WiFi ESP32](https://randomnerdtutorials.com/esp32-scanning-wifi-networks/)
- [Drone-Hacks pour les modifications DJI](https://www.youtube.com/watch?v=WiAWBjaUfeg)
- [Aperçu des projets de drone Arduino](https://www.instructables.com/How-to-Control-Any-Drone-From-Your-Arduino-Microco/)