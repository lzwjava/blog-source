---
audio: false
generated: true
lang: fr
layout: post
title: VSCode Pico-W-Go pour MicroPython
translated: true
type: note
---

Utiliser l'extension **Raspberry Pi Pico** dans Visual Studio Code (VSCode) est un excellent choix pour le développement MicroPython sur votre Raspberry Pi Pico, car elle offre un flux de travail rationalisé similaire à Thonny mais dans l'environnement d'édition puissant de VSCode. L'extension à laquelle vous faites probablement référence est **Pico-W-Go** (ou une extension similaire comme **Pico-Go**), qui est spécialement conçue pour le développement avec MicroPython sur Raspberry Pi Pico et Pico W. Ci-dessous, je vais vous guider pour configurer et utiliser l'extension **Pico-W-Go** (l'option la plus populaire et maintenue) afin de téléverser un programme MicroPython simple sur votre Pico, en supposant que MicroPython est déjà installé (via le fichier `RPI_PICO-20250415-v1.25.0.uf2` que vous avez utilisé).

---

### Prérequis
1. **MicroPython Installé** : Votre Pico a MicroPython d'installé, comme vous l'avez déjà flashé.
2. **VSCode Installé** : Assurez-vous que VSCode est installé ([code.visualstudio.com](https://code.visualstudio.com)).
3. **Python Installé** : Requis pour les dépendances de Pico-W-Go :
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
4. **Connexion USB** : Le Pico est connecté via un câble USB capable de transférer des données.

---

### Guide Étape par Étape pour Utiliser l'Extension Raspberry Pi Pico (Pico-W-Go) dans VSCode

1. **Installer l'Extension Pico-W-Go** :
   - Ouvrez VSCode.
   - Allez dans la vue Extensions (`Ctrl+Shift+X` ou `Cmd+Shift+X` sur macOS).
   - Recherchez **Pico-W-Go** et installez-la (développée par Paul Obermeier et d'autres).
   - Remarque : Si vous pensiez à une autre extension (par exemple, Pico-Go), faites-le moi savoir, mais Pico-W-Go est la plus couramment utilisée pour le développement MicroPython sur Pico.

2. **Installer les Dépendances de Pico-W-Go** :
   - Pico-W-Go nécessite `pyserial` et `esptool` pour la communication série et le flashing :
     ```bash
     pip3 install pyserial esptool
     ```
   - Assurez-vous qu'elles sont installées dans votre environnement Python (utilisez `pip3 list` pour vérifier).

3. **Configurer Pico-W-Go** :
   - Ouvrez la Palette de commandes dans VSCode (`Ctrl+Shift+P` ou `Cmd+Shift+P`).
   - Tapez et sélectionnez **Pico-W-Go > Configure Project**.
   - Suivez les invites :
     - **Port Série** : Sélectionnez le port du Pico (par exemple, `/dev/ttyACM0`). Trouvez-le en exécutant :
       ```bash
       ls /dev/tty*
       ```
       Cherchez `/dev/ttyACM0` ou similaire, qui apparaît lorsque le Pico est connecté.
     - **Interpréteur** : Choisissez MicroPython (Raspberry Pi Pico).
     - **Dossier du Projet** : Sélectionnez ou créez un dossier pour votre projet (par exemple, `~/PicoProjects/MonProjet`).
   - Pico-W-Go crée un fichier de configuration `.picowgo` dans votre dossier de projet pour stocker les paramètres.

4. **Écrire un Programme MicroPython Simple** :
   - Dans VSCode, ouvrez votre dossier de projet (Fichier > Ouvrir un dossier).
   - Créez un nouveau fichier nommé `main.py` (MicroPython exécute `main.py` automatiquement au démarrage).
   - Ajoutez un programme simple, par exemple, pour faire clignoter la LED intégrée :
     ```python
     from machine import Pin
     import time

     led = Pin(25, Pin.OUT)  # Utilisez "LED" pour Pico W
     while True:
         led.on()
         time.sleep(0.5)
         led.off()
         time.sleep(0.5)
     ```
   - Enregistrez le fichier (`Ctrl+S`).

5. **Téléverser le Programme sur le Pico** :
   - Assurez-vous que le Pico est connecté et que le port correct est sélectionné (relancez **Pico-W-Go > Configure Project** si nécessaire).
   - Ouvrez la Palette de commandes (`Ctrl+Shift+P`).
   - Sélectionnez **Pico-W-Go > Upload Project to Pico**.
     - Cela téléverse tous les fichiers de votre dossier de projet (par exemple, `main.py`) vers le système de fichiers du Pico.
   - Alternativement, pour téléverser un seul fichier :
     - Faites un clic droit sur `main.py` dans l'explorateur de fichiers de VSCode.
     - Sélectionnez **Pico-W-Go > Upload File to Pico**.
   - Le fichier est transféré vers le Pico, et s'il s'agit de `main.py`, il s'exécutera automatiquement au démarrage.

6. **Exécuter et Tester le Programme** :
   - **Exécution Automatique** : Si vous avez téléversé `main.py`, réinitialisez le Pico (débranchez et rebranchez, ou appuyez sur le bouton RESET si disponible). La LED devrait commencer à clignoter.
   - **Exécution Manuelle** :
     - Ouvrez la Palette de commandes et sélectionnez **Pico-W-Go > Run**.
     - Cela exécute le fichier actuel sur le Pico.
   - **Utiliser le REPL** :
     - Ouvrez la Palette de commandes et sélectionnez **Pico-W-Go > Open REPL**.
     - Le REPL apparaît dans le terminal de VSCode, où vous pouvez tester des commandes :
       ```python
       from machine import Pin
       led = Pin(25, Pin.OUT)
       led.on()
       ```
     - Appuyez sur `Ctrl+C` pour arrêter un programme en cours d'exécution dans le REPL.

7. **Gérer les Fichiers sur le Pico** :
   - **Lister les Fichiers** : Utilisez **Pico-W-Go > Download Project from Pico** pour visualiser ou récupérer des fichiers du système de fichiers du Pico.
   - **Supprimer des Fichiers** : Ouvrez la Palette de commandes et sélectionnez **Pico-W-Go > Delete All Files** pour effacer le système de fichiers du Pico, ou utilisez le REPL :
     ```python
     import os
     os.remove('main.py')
     ```
   - **Vérifier la Sortie** : La sortie du programme (par exemple, les instructions `print`) apparaît dans le REPL ou le terminal de VSCode si configuré.

---

### Dépannage
- **Port Non Détecté** :
  - Exécutez `ls /dev/tty*` pour confirmer le port du Pico (par exemple, `/dev/ttyACM0`).
  - Assurez-vous que le câble USB supporte le transfert de données et essayez un port différent.
  - Reconfigurez le port dans **Pico-W-Go > Configure Project**.
- **Échec du Téléversement** :
  - Vérifiez que `pyserial` et `esptool` sont installés (`pip3 list`).
  - Vérifiez que MicroPython est en cours d'exécution (le REPL devrait être accessible).
  - Reflashez MicroPython si nécessaire en réactivant le mode BOOTSEL et en copiant le fichier `.uf2`.
- **La LED Ne Clignote Pas** :
  - Confirmez la broche GPIO correcte (`25` pour Pico, `"LED"` pour Pico W).
  - Testez dans le REPL :
    ```python
    from machine import Pin
    led = Pin(25, Pin.OUT)
    led.on()
    ```
- **Commandes Pico-W-Go Manquantes** : Assurez-vous que l'extension est installée et activée. Redémarrez VSCode si nécessaire.

---

### Avantages de Pico-W-Go dans VSCode
- **Flux de Travail Intégré** : Combine l'édition de code, la gestion des fichiers et l'accès au REPL dans VSCode.
- **Fonctionnalités Avancées** : Tire parti de l'intégration Git, des extensions et de la personnalisation de VSCode.
- **Multiplateforme** : Fonctionne sur Linux, Windows et macOS.

### Limitations par Rapport à Thonny
- La configuration est légèrement plus complexe (par exemple, installation de `pyserial`, configuration du port).
- L'intégration du REPL peut sembler moins transparente que l'interface tout-en-un de Thonny.
- Moins convivial pour les débutants en MicroPython.

---

### Extensions Alternatives
Si vous pensiez à une autre extension (par exemple, **Pico-Go**), notez que Pico-Go est une alternative plus ancienne à Pico-W-Go et pourrait avoir moins de fonctionnalités ou de mises à jour. La configuration est similaire, mais Pico-W-Go est recommandée pour son développement actif et son support pour Pico et Pico W. Si vous utilisez une autre extension spécifique, veuillez préciser, et je pourrai adapter les instructions.

---

### Exemple de Flux de Travail
1. Installez Pico-W-Go et les dépendances.
2. Configurez le projet avec le port série correct (`/dev/ttyACM0`).
3. Écrivez et enregistrez `main.py` avec le code de clignotement de LED.
4. Utilisez **Pico-W-Go > Upload Project to Pico** pour téléverser.
5. Réinitialisez le Pico ou utilisez **Pico-W-Go > Run** pour voir la LED clignoter.
6. Utilisez le REPL pour tester ou déboguer de manière interactive.

Si vous avez besoin d'aide avec des commandes spécifiques de Pico-W-Go, un autre exemple de programme ou du dépannage (par exemple, problèmes de port, erreurs d'extension), faites-le moi savoir !