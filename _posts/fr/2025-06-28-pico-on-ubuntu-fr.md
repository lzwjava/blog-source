---
audio: false
generated: true
lang: fr
layout: post
title: Configuration de Raspberry Pi Pico sur Ubuntu
translated: true
type: note
---

Pour utiliser un **Raspberry Pi Pico** sur **Ubuntu**, vous devez configurer l'environnement de développement, installer les logiciels nécessaires et configurer les outils pour programmer le Pico. Le Pico prend en charge la programmation en **MicroPython**, **C/C++** ou **CircuitPython**. Ci-dessous, je décris les étapes et les logiciels requis pour chaque approche, en me concentrant sur les configurations les plus courantes.

### Prérequis généraux
- **Raspberry Pi Pico** (ou Pico W) avec un câble USB (Micro-USB pour le Pico, USB-C pour le Pico 2).
- Système **Ubuntu** (par exemple, Ubuntu 20.04, 22.04 ou version ultérieure ; ces instructions supposent une version récente comme 24.04).
- Connaissance de base du terminal.

### Option 1 : Programmation avec MicroPython
MicroPython est le moyen le plus simple pour les débutants de programmer le Pico. C'est une implémentation légère de Python conçue pour les microcontrôleurs.

#### Logiciels à installer
1. **Firmware MicroPython**
   - Téléchargez le dernier fichier de firmware MicroPython UF2 pour le Raspberry Pi Pico depuis le [site officiel MicroPython](https://micropython.org/download/rp2-pico/) ou la [page Raspberry Pi Pico](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).
   - Pour le Pico W ou le Pico 2, assurez-vous de sélectionner le firmware approprié (par exemple, `rp2-pico-w` pour le Pico W).

2. **Python 3**
   - Ubuntu inclut généralement Python 3 par défaut. Vérifiez avec :
     ```bash
     python3 --version
     ```
   - S'il n'est pas installé, installez-le :
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```

3. **IDE Thonny** (Recommandé pour les débutants)
   - Thonny est un IDE simple pour programmer le Pico avec MicroPython.
   - Installez Thonny :
     ```bash
     sudo apt install thonny
     ```
   - Alternativement, utilisez `pip` pour la dernière version :
     ```bash
     pip3 install thonny
     ```

4. **Optionnel : `picotool` (pour la gestion avancée)**
   - Utile pour gérer le firmware MicroPython ou inspecter le Pico.
   - Installez `picotool` :
     ```bash
     sudo apt install picotool
     ```

#### Étapes de configuration
1. **Installer le firmware MicroPython**
   - Connectez le Pico à votre machine Ubuntu via USB tout en maintenant le bouton **BOOTSEL** enfoncé (cela place le Pico en mode bootloader).
   - Le Pico apparaît comme un périphérique de stockage USB (par exemple, `RPI-RP2`).
   - Glissez-déposez le fichier MicroPython `.uf2` téléchargé sur le stockage du Pico. Le Pico redémarre automatiquement avec MicroPython installé.

2. **Configurer Thonny**
   - Ouvrez Thonny : `thonny` dans le terminal ou via le menu des applications.
   - Allez dans **Outils > Options > Interpréteur**.
   - Sélectionnez **MicroPython (Raspberry Pi Pico)** comme interpréteur.
   - Choisissez le port correct (par exemple, `/dev/ttyACM0`). Exécutez `ls /dev/tty*` dans le terminal pour identifier le port si nécessaire.
   - Thonny devrait maintenant être connecté au Pico, vous permettant d'écrire et d'exécuter des scripts Python.

3. **Tester un programme**
   - Dans Thonny, écrivez un script simple, par exemple :
     ```python
     from machine import Pin
     led = Pin(25, Pin.OUT)  # LED intégrée (GP25 pour Pico)
     led.toggle()  # Activer/désactiver la LED
     ```
   - Cliquez sur le bouton **Exécuter** pour exécuter le code sur le Pico.

4. **Optionnel : Utiliser `picotool`**
   - Vérifiez l'état du Pico :
     ```bash
     picotool info
     ```
   - Assurez-vous que le Pico est connecté et en mode bootloader si nécessaire.

### Option 2 : Programmation avec C/C++
Pour les utilisateurs avancés, le Pico peut être programmé en C/C++ en utilisant le **Pico SDK** officiel.

#### Logiciels à installer
1. **Pico SDK et Toolchain**
   - Installez les outils requis pour compiler les programmes C/C++ :
     ```bash
     sudo apt update
     sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential git
     ```

2. **Pico SDK**
   - Clonez le dépôt du Pico SDK :
     ```bash
     git clone -b master https://github.com/raspberrypi/pico-sdk.git
     cd pico-sdk
     git submodule update --init
     ```
   - Définissez la variable d'environnement `PICO_SDK_PATH` :
     ```bash
     export PICO_SDK_PATH=~/pico-sdk
     echo 'export PICO_SDK_PATH=~/pico-sdk' >> ~/.bashrc
     ```

3. **Optionnel : Exemples Pico**
   - Clonez les exemples Pico pour référence :
     ```bash
     git clone -b master https://github.com/raspberrypi/pico-examples.git
     ```

4. **Visual Studio Code (Optionnel)**
   - Pour une meilleure expérience de développement, installez VS Code :
     ```bash
     sudo snap install code --classic
     ```
   - Installez les extensions **CMake Tools** et **C/C++** dans VS Code.

#### Étapes de configuration
1. **Configurer un projet**
   - Créez un nouveau répertoire pour votre projet, par exemple, `my-pico-project`.
   - Copiez un exemple de `CMakeLists.txt` depuis `pico-examples` ou créez-en un :
     ```cmake
     cmake_minimum_required(VERSION 3.13)
     include($ENV{PICO_SDK_PATH}/pico_sdk_init.cmake)
     project(my_project C CXX ASM)
     pico_sdk_init()
     add_executable(my_project main.c)
     pico_add_extra_outputs(my_project)
     target_link_libraries(my_project pico_stdlib)
     ```
   - Écrivez un programme C simple (par exemple, `main.c`) :
     ```c
     #include "pico/stdlib.h"
     int main() {
         const uint LED_PIN = 25;
         gpio_init(LED_PIN);
         gpio_set_dir(LED_PIN, GPIO_OUT);
         while (true) {
             gpio_put(LED_PIN, 1);
             sleep_ms(500);
             gpio_put(LED_PIN, 0);
             sleep_ms(500);
         }
     }
     ```

2. **Compiler et flasher**
   - Accédez au répertoire de votre projet :
     ```bash
     cd my-pico-project
     mkdir build && cd build
     cmake ..
     make
     ```
   - Cela génère un fichier `.uf2` (par exemple, `my_project.uf2`).
   - Maintenez le bouton **BOOTSEL** sur le Pico, connectez-le via USB, et copiez le fichier `.uf2` sur le stockage du Pico :
     ```bash
     cp my_project.uf2 /media/$USER/RPI-RP2/
     ```

3. **Débogage (Optionnel)**
   - Installez `openocd` pour le débogage :
     ```bash
     sudo apt install openocd
     ```
   - Utilisez un débogueur (par exemple, un autre Pico comme sonde de débogage) et exécutez :
     ```bash
     openocd -f interface/raspberrypi-swd.cfg -f target/rp2040.cfg
     ```

### Option 3 : Programmation avec CircuitPython
CircuitPython est une autre option basée sur Python, similaire à MicroPython mais axée sur l'écosystème d'Adafruit.

#### Logiciels à installer
1. **Firmware CircuitPython**
   - Téléchargez le fichier UF2 CircuitPython pour le Pico depuis le [site Web Adafruit CircuitPython](https://circuitpython.org/board/raspberry_pi_pico/).
   - Pour le Pico W ou le Pico 2, sélectionnez le firmware approprié.

2. **Python 3 et outils**
   - Identique à MicroPython (Python 3, Thonny, etc.).

#### Étapes de configuration
1. **Installer le firmware CircuitPython**
   - Similaire à MicroPython : maintenez **BOOTSEL**, connectez le Pico, et copiez le fichier CircuitPython `.uf2` sur le stockage du Pico.
   - Le Pico redémarre en tant que lecteur USB nommé `CIRCUITPY`.

2. **Programmer avec Thonny ou un éditeur de texte**
   - Utilisez Thonny comme décrit dans la section MicroPython, en sélectionnant **CircuitPython** comme interpréteur.
   - Alternativement, éditez `code.py` directement sur le lecteur `CIRCUITPY` en utilisant n'importe quel éditeur de texte.
   - Exemple de `code.py` :
     ```python
     import board
     import digitalio
     import time
     led = digitalio.DigitalInOut(board.LED)
     led.direction = digitalio.Direction.OUTPUT
     while True:
         led.value = True
         time.sleep(0.5)
         led.value = False
         time.sleep(0.5)
     ```

### Notes supplémentaires
- **Permissions** : Si le port du Pico (par exemple, `/dev/ttyACM0`) n'est pas accessible, ajoutez votre utilisateur au groupe `dialout` :
  ```bash
  sudo usermod -a -G dialout $USER
  ```
  Déconnectez-vous et reconnectez-vous pour appliquer.

- **Considérations pour le Pico W** : Pour le Pico W, assurez-vous d'utiliser un firmware spécifique à celui-ci (par exemple, MicroPython avec prise en charge Wi-Fi). La programmation Wi-Fi nécessite des bibliothèques supplémentaires, comme `network` pour MicroPython.

- **Pico 2** : Le nouveau Raspberry Pi Pico 2 (avec RP2350) peut nécessiter des versions mises à jour du firmware ou du SDK. Vérifiez la documentation officielle de Raspberry Pi pour la compatibilité.

- **Dépannage** :
  - Si le Pico n'apparaît pas en mode bootloader, vérifiez le câble USB (il doit prendre en charge les données, pas seulement l'alimentation).
  - Exécutez `lsusb` ou `dmesg` pour confirmer que le Pico est détecté par Ubuntu.
  - Pour les compilations C/C++, assurez-vous que le chemin du Pico SDK est correctement défini.

### Approche recommandée
- Pour les **débutants** : Utilisez **MicroPython avec Thonny** pour sa simplicité et sa configuration rapide.
- Pour les **utilisateurs avancés** : Utilisez **C/C++ avec le Pico SDK** pour les performances et le contrôle de bas niveau.
- Pour les **utilisateurs de l'écosystème Adafruit** : Utilisez **CircuitPython** si vous prévoyez d'utiliser des bibliothèques ou du matériel Adafruit.

Si vous avez un projet spécifique ou une préférence de programmation, faites-le-moi savoir et je pourrai adapter les instructions davantage !