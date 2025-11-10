---
audio: false
generated: true
lang: fr
layout: post
title: Téléverser MicroPython sur Pico
translated: true
type: note
---

Après avoir flashé MicroPython sur votre Raspberry Pi Pico (en utilisant le fichier `.uf2` comme décrit), vous pouvez télécharger et exécuter un programme MicroPython simple en utilisant un outil comme Thonny IDE, qui est convivial pour les débutants et largement utilisé pour le développement MicroPython. Ci-dessous se trouvent les étapes pour configurer MicroPython et télécharger un programme simple sur votre Pico.

---

### Prérequis
1.  **MicroPython Flashé** : Vous avez déjà copié `RPI_PICO-20250415-v1.25.0.uf2` sur le lecteur `RPI-RP2`, et le Pico a redémarré (le lecteur `RPI-RP2` ne devrait plus apparaître).
2.  **Connexion USB** : Le Pico est connecté à votre ordinateur via un câble USB qui prend en charge le transfert de données.
3.  **Thonny IDE** : Installez Thonny si vous ne l'avez pas déjà fait :
    *   **Linux** : Installez Thonny en utilisant votre gestionnaire de paquets ou téléchargez-le depuis [thonny.org](https://thonny.org).
      ```bash
      sudo apt update
      sudo apt install thonny
      ```
    *   Alternativement, utilisez `pip` :
      ```bash
      pip install thonny
      ```
    *   Pour Windows/macOS, téléchargez et installez depuis [thonny.org](https://thonny.org).

---

### Guide Étape par Étape pour Télécharger un Programme MicroPython Simple

1.  **Connectez le Pico et Ouvrez Thonny** :
    *   Branchez votre Pico sur le port USB de votre ordinateur.
    *   Ouvrez Thonny IDE.

2.  **Configurez Thonny pour MicroPython** :
    *   Dans Thonny, allez dans **Outils > Options > Interpréteur** (ou **Exécuter > Sélectionner l'interpréteur**).
    *   Sélectionnez **MicroPython (Raspberry Pi Pico)** dans la liste déroulante de l'interpréteur.
    *   Si le port série du Pico (par exemple, `/dev/ttyACM0` sur Linux) n'apparaît pas automatiquement :
        *   Vérifiez les ports disponibles dans la liste déroulante ou exécutez `ls /dev/tty*` dans un terminal pour identifier le port du Pico (généralement `/dev/ttyACM0` ou similaire).
        *   Sélectionnez manuellement le port correct.
    *   Cliquez sur **OK** pour sauvegarder.

3.  **Vérifiez que MicroPython Fonctionne** :
    *   Dans le **Shell** de Thonny (panneau inférieur), vous devriez voir une invite REPL MicroPython comme :
      ```
      >>>
      ```
    *   Testez-la en tapant une commande simple, par exemple :
      ```python
      print("Hello, Pico!")
      ```
      Appuyez sur Entrée, et vous devriez voir la sortie dans le Shell.

4.  **Écrivez un Programme MicroPython Simple** :
    *   Dans l'éditeur principal de Thonny, créez un nouveau fichier et écrivez un programme simple. Par exemple, un programme pour faire clignoter la LED intégrée du Pico (sur GPIO 25 pour Pico, ou "LED" pour Pico W) :
      ```python
      from machine import Pin
      import time

      # Initialiser la LED intégrée
      led = Pin(25, Pin.OUT)  # Utilisez "LED" au lieu de 25 pour Pico W

      # Faire clignoter la LED
      while True:
          led.on()           # Allumer la LED
          time.sleep(0.5)    # Attendre 0.5 secondes
          led.off()          # Éteindre la LED
          time.sleep(0.5)    # Attendre 0.5 secondes
      ```
    *   Note : Si vous utilisez un Pico W, remplacez `Pin(25, Pin.OUT)` par `Pin("LED", Pin.OUT)`.

5.  **Sauvegardez le Programme sur le Pico** :
    *   Cliquez sur **Fichier > Enregistrer sous**.
    *   Dans la boîte de dialogue, sélectionnez **Raspberry Pi Pico** comme destination (et non votre ordinateur).
    *   Nommez le fichier `main.py` (MicroPython exécute `main.py` automatiquement au démarrage) ou un autre nom comme `blink.py`.
    *   Cliquez sur **OK** pour sauvegarder le fichier sur le système de fichiers du Pico.

6.  **Exécutez le Programme** :
    *   Cliquez sur le bouton vert **Exécuter** (ou appuyez sur **F5**) dans Thonny pour exécuter le programme.
    *   Alternativement, si vous l'avez sauvegardé sous `main.py`, réinitialisez le Pico (débranchez et rebranchez, ou appuyez sur le bouton RESET si disponible), et le programme s'exécutera automatiquement.
    *   Vous devriez voir la LED intégrée clignoter toutes les 0.5 secondes.

7.  **Arrêtez le Programme** (si nécessaire) :
    *   Pour arrêter le programme, appuyez sur **Ctrl+C** dans le Shell de Thonny pour interrompre le script en cours d'exécution.
    *   Pour empêcher `main.py` de s'exécuter automatiquement, supprimez-le du Pico :
        *   Dans Thonny, allez dans **Affichage > Fichiers**, sélectionnez le système de fichiers du Pico, faites un clic droit sur `main.py` et choisissez **Supprimer**.

---

### Test et Dépannage
*   **Aucune Invite REPL** : Si Thonny n'affiche pas le REPL MicroPython :
    *   Assurez-vous que le port correct est sélectionné dans les paramètres de l'interpréteur.
    *   Vérifiez que MicroPython a été flashé correctement. Sinon, re-flashez le fichier `.uf2` comme décrit précédemment.
    *   Vérifiez le câble USB (doit prendre en charge les données) et essayez un port différent.
*   **La LED ne Clignote Pas** : Assurez-vous d'utiliser la broche GPIO correcte (`25` pour Pico, `"LED"` pour Pico W). Si cela ne fonctionne toujours pas, testez la LED avec une commande REPL simple :
  ```python
  from machine import Pin
  led = Pin(25, Pin.OUT)
  led.on()
  ```
*   **Fichier Non Sauvegardé** : Assurez-vous que Thonny est connecté au Pico et que l'interpréteur est défini sur MicroPython (Raspberry Pi Pico).

---

### Conseils Supplémentaires
*   **Utiliser d'Autres Outils** : Outre Thonny, vous pouvez utiliser `rshell` ou `ampy` pour gérer les fichiers sur le Pico :
  ```bash
  pip install rshell
  rshell --port /dev/ttyACM0
  cp blink.py /pyboard/main.py
  ```
*   **Plus d'Exemples de Programmes** :
    *   Lire l'état d'un bouton (par exemple, sur GPIO 14) :
      ```python
      from machine import Pin
      button = Pin(14, Pin.IN, Pin.PULL_UP)
      while True:
          print(button.value())
      ```
    *   Contrôler une LED externe ou d'autres périphériques en ajustant le numéro de broche GPIO.
*   **Exécution Automatique** : Sauvegarder un fichier sous `main.py` lui permet de s'exécuter automatiquement au démarrage. Utilisez `boot.py` pour le code d'initialisation qui s'exécute avant `main.py`.

Si vous rencontrez des problèmes spécifiques (par exemple, détection de port, erreurs dans Thonny ou problèmes matériels), ou si vous souhaitez essayer un programme différent, faites-le moi savoir et je vous guiderai davantage !