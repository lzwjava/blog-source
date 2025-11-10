---
audio: false
generated: true
lang: fr
layout: post
title: Installation de Selenium GeckoDriver sur Ubuntu
translated: true
type: note
---

Pour installer le pilote Firefox pour Selenium (geckodriver) sur Ubuntu, suivez ces étapes :

1. **Installer Firefox** (s'il n'est pas déjà installé) :
   ```bash
   sudo apt update
   sudo apt install firefox
   ```

2. **Télécharger geckodriver** :
   - Visitez la [page des releases de geckodriver](https://github.com/mozilla/geckodriver/releases).
   - Choisissez la dernière version compatible avec votre version de Firefox. Pour Ubuntu, téléchargez la version Linux 64 bits (par exemple, `geckodriver-vX.XX.X-linux64.tar.gz`).
   - Exemple de commande pour télécharger (remplacez `X.XX.X` par la dernière version) :
     ```bash
     wget https://github.com/mozilla/geckodriver/releases/download/vX.XX.X/geckodriver-vX.XX.X-linux64.tar.gz
     ```

3. **Extraire le fichier téléchargé** :
   ```bash
   tar -xvzf geckodriver-vX.XX.X-linux64.tar.gz
   ```

4. **Déplacer geckodriver vers un chemin système** :
   - Déplacez le fichier `geckodriver` extrait vers `/usr/local/bin` pour le rendre accessible globalement :
     ```bash
     sudo mv geckodriver /usr/local/bin/
     ```
   - Rendez-le exécutable :
     ```bash
     sudo chmod +x /usr/local/bin/geckodriver
     ```

5. **Installer Selenium pour Python** (si vous utilisez Python) :
   ```bash
   pip install selenium
   ```

6. **Vérifier l'installation** :
   - Vérifiez la version de geckodriver :
     ```bash
     geckodriver --version
     ```
   - Testez avec un script Python simple :
     ```python
     from selenium import webdriver

     driver = webdriver.Firefox()
     driver.get("https://www.example.com")
     print(driver.title)
     driver.quit()
     ```

**Notes** :
- Assurez-vous que votre version de Firefox est compatible avec la version de geckodriver (vérifiez les notes de release sur la page GitHub de geckodriver).
- Si vous rencontrez des problèmes, assurez-vous que `python3-pip` est installé :
  ```bash
  sudo apt install python3-pip
  ```
- Si geckodriver n'est pas trouvé, ajoutez `/usr/local/bin` à votre `PATH` :
  ```bash
  export PATH=$PATH:/usr/local/bin
  ```

Cela devrait configurer le pilote Firefox pour Selenium sur Ubuntu. Faites-moi savoir si vous rencontrez des problèmes !

---

La différence entre `geckodriver-v0.36.0-linux-aarch64.tar.gz` et `geckodriver-v0.36.0-linux64.tar.gz` réside dans l'architecture CPU cible :

- **linux-aarch64** : Ceci est pour les architectures ARM 64 bits (par exemple, ARMv8-A), couramment utilisées dans des appareils comme le Raspberry Pi, certains serveurs ou les systèmes Linux modernes basés sur ARM. Le terme "aarch64" désigne l'architecture ARM 64 bits.

- **linux64** : Ceci est pour les architectures x86 64 bits (également appelées x86_64 ou AMD64), qui sont standard pour la plupart des PC de bureau et serveurs exécutant Linux.

**Points clés** :
- Choisissez `linux-aarch64` si votre système possède un processeur ARM 64 bits.
- Choisissez `linux64` si votre système possède un processeur x86 64 bits.
- Vous pouvez vérifier l'architecture de votre système sous Linux en exécutant `uname -m`. Si la commande retourne `aarch64`, utilisez la version ARM ; si elle retourne `x86_64`, utilisez la version linux64.

Les fichiers `.asc` sont des signatures GPG pour vérifier l'intégrité et l'authenticité des fichiers `.tar.gz` correspondants.