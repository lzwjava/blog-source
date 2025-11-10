---
audio: false
generated: true
lang: fr
layout: post
title: VSCode pour Raspberry Pi Pico MicroPython
translated: true
type: note
---

Oui, vous pouvez utiliser Visual Studio Code (VSCode) pour écrire, télécharger et exécuter des programmes MicroPython sur votre Raspberry Pi Pico, de la même manière que vous le feriez avec Thonny. VSCode est un éditeur puissant, et avec les bonnes extensions et outils, il peut gérer efficacement le développement MicroPython. Voici un guide étape par étape pour configurer VSCode afin de télécharger un programme MicroPython simple sur votre Pico, en supposant que MicroPython est déjà installé (comme vous l'avez fait avec le fichier `.uf2`).

---

### Prérequis
1. **MicroPython Installé** : Votre Pico a MicroPython installé (par exemple, à partir du fichier `RPI_PICO-20250415-v1.25.0.uf2`).
2. **VSCode Installé** : Téléchargez et installez VSCode depuis [code.visualstudio.com](https://code.visualstudio.com) si vous ne l'avez pas déjà fait.
3. **Python Installé** : Installez Python (nécessaire pour les outils MicroPython) via :
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
4. **Connexion USB** : Le Pico est connecté à votre ordinateur via un câble USB capable de transférer des données.

---

### Guide Étape par Étape pour Utiliser VSCode avec MicroPython sur Raspberry Pi Pico

1. **Installer les Extensions VSCode Requises** :
   - Ouvrez VSCode.
   - Allez dans la vue Extensions (`Ctrl+Shift+X` ou `Cmd+Shift+X` sur macOS).
   - Installez les extensions suivantes :
     - **Python** (par Microsoft) : Pour la coloration syntaxique et IntelliSense Python et MicroPython.
     - **Pico-W-Go** (optionnel mais recommandé) : Une extension dédiée au développement Raspberry Pi Pico avec MicroPython. Recherchez "Pico-W-Go" et installez-la.
       - Remarque : Pico-W-Go simplifie les transferts de fichiers et l'accès au REPL mais nécessite une configuration supplémentaire (décrite ci-dessous).
     - Alternativement, vous pouvez utiliser des extensions plus générales comme **Remote-SSH** ou **Serial Monitor** si vous préférez un contrôle manuel.

2. **Configurer Pico-W-Go (Recommandé)** :
   - **Installer les Dépendances** : Pico-W-Go nécessite `pyserial` et `esptool`. Installez-les via pip :
     ```bash
     pip3 install pyserial esptool
     ```
   - **Configurer Pico-W-Go** :
     - Ouvrez la Palette de Commandes de VSCode (`Ctrl+Shift+P` ou `Cmd+Shift+P`).
     - Tapez et sélectionnez **Pico-W-Go > Configure Project**.
     - Suivez les invites pour configurer votre projet :
       - Choisissez le port série du Pico (par exemple, `/dev/ttyACM0`). Exécutez `ls /dev/tty*` dans un terminal pour le trouver.
       - Sélectionnez MicroPython comme interpréteur.
       - Créez un nouveau dossier de projet ou utilisez un dossier existant.
     - Pico-W-Go crée un espace de travail avec un fichier de configuration `.picowgo`.

3. **Écrire un Programme MicroPython Simple** :
   - Dans VSCode, créez un nouveau fichier (par exemple, `main.py`) dans votre dossier de projet.
   - Écrivez un programme simple, comme faire clignoter la LED intégrée :
     ```python
     from machine import Pin
     import time

     led = Pin(25