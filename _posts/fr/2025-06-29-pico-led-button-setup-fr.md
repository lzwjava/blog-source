---
audio: false
generated: true
lang: fr
layout: post
title: Configuration de Bouton LED pour Raspberry Pi Pico
translated: true
type: note
---

Pour configurer un Raspberry Pi Pico afin d'exécuter le code MicroPython fourni, qui contrôle une LED en fonction de l'appui sur un bouton, suivez ces étapes :

### Matériel requis
- **Raspberry Pi Pico** (ou Pico W)
- **LED** (avec une résistance de limitation de courant appropriée, par exemple 220–330 ohms)
- **Bouton-poussoir**
- **Fils de liaison**
- **Plaque d'essai** (optionnelle, pour des connexions plus faciles)
- **Câble USB** (pour connecter le Pico à votre ordinateur)

### Configuration matérielle
1. **Connecter la LED** :
   - Connectez l'anode de la LED (patte la plus longue) à la broche **GPIO 25** (broche physique 30) sur le Pico.
   - Connectez la cathode de la LED (patte la plus courte) à une broche de **masse (GND)** (par exemple, broche physique 3) via une résistance de 220–330 ohms pour limiter le courant.

2. **Connecter le bouton** :
   - Connectez un côté du bouton-poussoir à la broche **GPIO 14** (broche physique 19).
   - Connectez l'autre côté du bouton à une broche **3.3V** (par exemple, broche physique 36, 3V3(OUT)).
   - Le code utilise une résistance de rappel interne (`Pin.PULL_DOWN`), donc aucune résistance de rappel externe n'est nécessaire. Lorsque le bouton est enfoncé, la broche GPIO 14 lira HIGH (1) ; lorsqu'il n'est pas enfoncé, elle lira LOW (0).

3. **Vérifier les connexions** :
   - Assurez-vous que toutes les connexions sont sécurisées. Utilisez une plaque d'essai ou un câblage direct, et vérifiez que la polarité de la LED est correcte et que la résistance est correctement placée.
   - Reportez-vous au diagramme des broches du Pico (disponible en ligne ou dans la datasheet du Pico) pour confirmer les assignations des broches.

### Configuration logicielle
1. **Installer MicroPython sur le Pico** :
   - Téléchargez le dernier firmware MicroPython UF2 pour le Raspberry Pi Pico depuis le [site officiel de MicroPython](https://micropython.org/download/rp2-pico/).
   - Connectez le Pico à votre ordinateur via un câble USB tout en maintenant le bouton **BOOTSEL** enfoncé.
   - Le Pico apparaîtra comme un lecteur USB (RPI-RP2). Glissez-déposez le fichier `.uf2` téléchargé sur ce lecteur.
   - Le Pico redémarrera automatiquement avec MicroPython installé.

2. **Configurer un environnement de développement** :
   - Installez un IDE compatible MicroPython, tel que **Thonny** (recommandé pour les débutants) :
     - Téléchargez et installez Thonny depuis [thonny.org](https://thonny.org).
     - Dans Thonny, allez dans **Outils > Options > Interpréteur**, sélectionnez **MicroPython (Raspberry Pi Pico)**, et choisissez le port approprié (par exemple, `COMx` sur Windows ou `/dev/ttyACM0` sur Linux/macOS).
   - Alternativement, vous pouvez utiliser des outils comme `rshell`, `ampy`, ou Visual Studio Code avec l'extension MicroPython.

3. **Téléverser et exécuter le code** :
   - Copiez le code fourni dans un fichier nommé `main.py` :
     ```python
     from machine import Pin
     import time

     led = Pin(25, Pin.OUT)
     button = Pin(14, Pin.IN, Pin.PULL_DOWN)

     while True:
         if button.value():
             led.on()
         else:
             led.off()
         time.sleep(0.05)
     ```
   - Dans Thonny :
     - Ouvrez un nouveau fichier, collez le code et enregistrez-le sur le Pico sous le nom `main.py` (MicroPython exécute automatiquement `main.py` au démarrage).
     - Cliquez sur le bouton **Exécuter** ou appuyez sur **F5** pour téléverser et exécuter le code.
   - Alternativement, utilisez `ampy` pour téléverser le fichier :
     ```bash
     ampy --port /dev/ttyACM0 put main.py
     ```
     Remplacez `/dev/ttyACM0` par le port de votre Pico.

4. **Tester le programme** :
   - Une fois le code téléversé, la LED devrait s'allumer lorsque le bouton est enfoncé et s'éteindre lorsqu'il est relâché. Le `time.sleep(0.05)` ajoute un délai de 50ms pour l'antirebond du bouton et réduire la charge du CPU.

### Dépannage
- **La LED ne s'allume pas** :
  - Vérifiez la polarité de la LED (anode vers GPIO 25, cathode vers GND via la résistance).
  - Vérifiez que la broche GPIO (25) correspond au code et à la connexion physique.
  - Assurez-vous que la LED et la résistance sont fonctionnelles (testez avec un multimètre ou un autre circuit).
- **Le bouton ne fonctionne pas** :
  - Confirmez que la broche GPIO 14 est correctement connectée et que le bouton se connecte au 3.3V lorsqu'il est enfoncé.
  - Vérifiez que `Pin.PULL_DOWN` est approprié ; si le bouton est câblé différemment (par exemple, vers GND), ajustez le code pour utiliser `Pin.PULL_UP` et inversez la logique (`if not button.value()`).
- **Le code ne s'exécute pas** :
  - Assurez-vous que MicroPython est correctement installé.
  - Vérifiez que le fichier est enregistré sous le nom `main.py` sur le Pico.
  - Vérifiez la connexion USB et les paramètres de port dans votre IDE.

### Notes
- Le code suppose que le bouton connecte la broche GPIO 14 au 3.3V lorsqu'il est enfoncé. Si votre bouton se connecte à la masse (GND) à la place, modifiez le code pour utiliser `Pin.PULL_UP` et inversez la logique :
  ```python
  button = Pin(14, Pin.IN, Pin.PULL_UP)
  while True:
      if not button.value():  # Bouton enfoncé = LOW
          led.on()
      else:
          led.off()
      time.sleep(0.05)
  ```
- Si vous rencontrez un effet de rebond (LED clignotante), augmentez la valeur de `time.sleep` ou implémentez un antirebond logiciel.
- Pour un Pico W, la configuration est identique, mais assurez-vous d'utiliser les bonnes broches GPIO, car le brochage est le même.

Si vous avez besoin de précisions supplémentaires ou d'aide pour des problèmes spécifiques, faites-le moi savoir !