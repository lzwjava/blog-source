---
audio: false
generated: true
lang: fr
layout: post
title: Installation de l'IDE Arduino sur Ubuntu
translated: true
type: note
---

Pour installer l'IDE Arduino sur Ubuntu Linux, suivez ces étapes :

1. **Télécharger l'IDE Arduino** :
   - Rendez-vous sur le site officiel d'Arduino à l'adresse [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software).
   - Dans la section "Arduino IDE", sélectionnez l'option de téléchargement "Linux 64 bits" (ou la version appropriée pour votre système, par exemple Linux ARM pour Raspberry Pi).

2. **Extraire le fichier téléchargé** :
   - Le fichier téléchargé est une archive compressée `.tar.xz` (par exemple, `arduino-1.8.19-linux64.tar.xz`).
   - Ouvrez un terminal et naviguez jusqu'au répertoire de téléchargement (par exemple, `cd ~/Téléchargements`).
   - Extrayez le fichier en utilisant :
     ```bash
     tar -xf arduino-*.tar.xz
     ```
   - Ceci crée un dossier comme `arduino-1.8.19`.

3. **Déplacer vers un répertoire approprié (Optionnel)** :
   - Pour un accès système, déplacez le dossier extrait vers `/opt` (nécessite les privilèges superutilisateur) :
     ```bash
     sudo mv arduino-1.8.19 /opt/arduino
     ```

4. **Exécuter le script d'installation** :
   - Naviguez jusqu'au dossier Arduino :
     ```bash
     cd /opt/arduino
     ```
   - Exécutez le script d'installation :
     ```bash
     sudo ./install.sh
     ```
   - Ceci crée un raccourci sur le bureau et configure les permissions nécessaires.

5. **Ajouter votre utilisateur au groupe Dialout** :
   - Pour accéder à la carte Arduino via le port série, ajoutez votre utilisateur au groupe `dialout` :
     ```bash
     sudo usermod -a -G dialout $USER
     ```
   - Déconnectez-vous et reconnectez-vous, ou redémarrez pour que le changement de groupe prenne effet.

6. **Lancer l'IDE Arduino** :
   - Si vous avez exécuté le script `install.sh`, vous pouvez lancer l'IDE depuis le menu des applications ou en recherchant "Arduino IDE".
   - Alternativement, exécutez-le directement depuis le terminal :
     ```bash
     /opt/arduino/arduino
     ```

7. **Mettre à jour les permissions pour la carte Arduino (si nécessaire)** :
   - Lorsque vous connectez votre Arduino, assurez-vous qu'il est détecté (par exemple, `/dev/ttyACM0` ou `/dev/ttyUSB0`).
   - Si vous rencontrez des problèmes de permissions, définissez les permissions correctes :
     ```bash
     sudo chmod a+rw /dev/ttyACM0
     ```
   - Remplacez `/dev/ttyACM0` par le port approprié.

8. **Vérifier l'installation** :
   - Connectez votre carte Arduino via USB.
   - Ouvrez l'IDE, allez dans **Outils > Carte** et sélectionnez votre modèle Arduino (par exemple, Arduino Uno).
   - Allez dans **Outils > Port** et sélectionnez le port (par exemple, `/dev/ttyACM0`).
   - Essayez de téléverser un exemple de sketch (par exemple, **Fichier > Exemples > 01.Basics > Blink**) pour confirmer que tout fonctionne.

**Alternative : Installer via Snap ou Flatpak** :
- **Snap** :
  ```bash
  sudo snap install arduino
  ```
- **Flatpak** :
  ```bash
  sudo flatpak install flathub cc.arduino.ArduinoIDE
  ```
- Ces méthodes simplifient l'installation mais peuvent avoir des limitations avec les permissions ou la détection de carte.

**Notes** :
- Assurez-vous d'avoir Java installé, car l'IDE Arduino en a besoin. Installez-le si nécessaire :
  ```bash
  sudo apt update
  sudo apt install default-jre
  ```
- Pour la dernière version ou le dépannage, consultez les forums Arduino ou la [documentation officielle](https://www.arduino.cc/en/Guide/Linux).

Si vous rencontrez des problèmes, indiquez-moi votre version d'Ubuntu ou l'erreur spécifique pour une aide personnalisée !

---

Étant donné que votre Arduino Uno est détecté dans l'IDE Arduino sur Ubuntu et que vous voulez un exemple simple sans utiliser de plaque d'essai ou de composants externes, voici un sketch basique qui fait clignoter la LED intégrée sur l'Arduino Uno (connectée à la broche digitale 13). Cela ne nécessite aucun matériel supplémentaire.

```cpp
void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT); // Définir la broche de la LED intégrée (broche 13) comme sortie
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH); // Allumer la LED
  delay(1000);                     // Attendre 1 seconde
  digitalWrite(LED_BUILTIN, LOW);  // Éteindre la LED
  delay(1000);                     // Attendre 1 seconde
}
```

### Comment l'exécuter :
1. Ouvrez l'IDE Arduino.
2. Copiez et collez le code ci-dessus dans l'IDE.
3. Assurez-vous que votre Arduino Uno est connecté via USB et détecté :
   - Allez dans **Outils > Carte** et sélectionnez **Arduino Uno**.
   - Allez dans **Outils > Port** et sélectionnez le port (par exemple, `/dev/ttyACM0` ou `/dev/ttyUSB0`).
4. Cliquez sur le bouton **Téléverser** (icône de flèche droite) pour compiler et téléverser le sketch sur votre Arduino Uno.
5. Une fois téléversé, la LED intégrée (étiquetée "L" sur la carte) devrait clignoter, allumée pendant 1 seconde, puis éteinte pendant 1 seconde, de manière répétée.

### Ce que cela fait :
- Dans `setup()`, la fonction `pinMode` configure la broche de la LED intégrée comme une sortie.
- Dans `loop()`, la fonction `digitalWrite` allume la LED (`HIGH`) et l'éteint (`LOW`), avec `delay` qui fait une pause de 1 seconde entre chaque état, créant un effet de clignotement.

### Notes :
- Aucun composant externe n'est nécessaire puisque l'Arduino Uno a une LED intégrée sur la broche 13.
- Si la LED ne clignote pas, vérifiez la sélection du port ou assurez-vous que la carte est correctement connectée. Vous pouvez également ouvrir le **Moniteur Série** (Outils > Moniteur Série) pour déboguer si vous ajoutez `Serial.begin(9600);` dans `setup()` et imprimez des messages comme `Serial.println("Blink");` dans `loop()`.
- Si vous voulez modifier la vitesse de clignotement, ajustez les valeurs de `delay(1000)` (par exemple, `delay(500)` pour un clignotement plus rapide).

Faites-moi savoir si vous rencontrez des problèmes ou si vous voulez un autre exemple simple !

---

Le message d'erreur indique un problème de permission lors de la tentative de téléversement du sketch sur votre Arduino Uno sur Ubuntu. L'IDE Arduino ne peut pas accéder au port série `/dev/ttyUSB0` en raison de permissions insuffisantes. Voici comment résoudre ce problème :

### Solution : Corriger les permissions du port série

1. **Ajouter votre utilisateur au groupe `dialout`** :
   - Le groupe `dialout` contrôle généralement l'accès aux ports série dans Ubuntu. Ajoutez votre utilisateur à ce groupe :
     ```bash
     sudo usermod -a -G dialout $USER
     ```
   - Après avoir exécuté cette commande, déconnectez-vous et reconnectez-vous, ou redémarrez votre système pour que le changement prenne effet :
     ```bash
     sudo reboot
     ```

2. **Vérifier le port** :
   - Après le redémarrage, reconnectez votre Arduino Uno et ouvrez l'IDE Arduino.
   - Allez dans **Outils > Port** et assurez-vous que `/dev/ttyUSB0` (ou `/dev/ttyACM0` pour certaines cartes Arduino) est sélectionné. Si aucun port n'apparaît, vérifiez la connexion USB ou essayez un câble/port différent.

3. **Modifier temporairement les permissions du port (Optionnel)** :
   - Si le problème persiste après avoir ajouté votre utilisateur au groupe `dialout`, vous pouvez définir manuellement les permissions pour le port (c'est une solution temporaire, car les permissions sont réinitialisées au redémarrage) :
     ```bash
     sudo chmod a+rw /dev/ttyUSB0
     ```
   - Remplacez `/dev/ttyUSB0` par le port correct s'il est différent (par exemple, `/dev/ttyACM0`).

4. **Essayer de téléverser à nouveau** :
   - Dans l'IDE Arduino, cliquez sur le bouton **Téléverser** pour téléverser votre sketch (par exemple, le sketch de la LED clignotante précédent).
   - Si le téléversement réussit, la LED intégrée sur votre Arduino Uno devrait commencer à clignoter.

### Dépannage supplémentaire

- **Vérifier la carte Arduino et le câble** :
  - Assurez-vous que l'Arduino Uno est correctement connecté via USB et reconnu par Ubuntu. Exécutez cette commande pour lister les appareils connectés :
    ```bash
    ls /dev/tty*
    ```
    Recherchez `/dev/ttyUSB0` ou `/dev/ttyACM0` lorsque la carte est branchée.
  - Essayez un câble USB ou un port différent si la carte n'est pas détectée.

- **Vérifier les paramètres de la carte et du port** :
   - Dans l'IDE Arduino, confirmez que **Outils > Carte** est défini sur **Arduino Uno**.
   - Si `/dev/ttyUSB0` n'apparaît pas, essayez **Outils > Port** après avoir débranché et rebranché la carte.

- **Exécuter l'IDE Arduino en tant que root (Solution de contournement temporaire)** :
   - Si les étapes ci-dessus ne fonctionnent pas, vous pouvez exécuter l'IDE avec les privilèges superutilisateur pour contourner les problèmes de permission (non recommandé à long terme) :
     ```bash
     sudo arduino
     ```
     Remplacez `arduino` par le chemin vers votre exécutable Arduino IDE s'il n'est pas dans le PATH de votre système (par exemple, `/opt/arduino/arduino`).

- **Vérifier les logiciels conflictuels** :
   - D'autres logiciels (par exemple, `brltty`, un pilote d'affichage braille) peuvent interférer avec les ports série. Supprimez-le s'il est installé :
     ```bash
     sudo apt remove brltty
     ```

- **Problèmes de pilote** :
   - Certains clones Arduino utilisent la puce CH340/CH341, nécessitant un pilote. Installez-le si nécessaire :
     ```bash
     sudo apt install linux-modules-extra-$(uname -r)
     ```
     Puis, reconnectez la carte.

### Confirmer la résolution
Une fois les permissions résolues, essayez de téléverser à nouveau le sketch clignotant précédent :
```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

Si vous rencontrez toujours des problèmes, partagez le nouveau message d'erreur ou exécutez `ls -l /dev/ttyUSB0` dans le terminal et fournissez le résultat pour aider au diagnostic.

---

Il semble que vous rencontriez un problème lors de la tentative de téléversement d'un sketch sur votre Arduino Uno en utilisant l'IDE Arduino sur Ubuntu. Le message d'erreur que vous avez fourni est :

```
avrdude: ser_open(): can't open device "/dev/ttyUSB0": Permission denied
Failed uploading: uploading error: exit status 1
```

Cette erreur indique que l'IDE Arduino n'a pas les permissions nécessaires pour accéder au port série (`/dev/ttyUSB0`) où votre Arduino Uno est connecté. C'est un problème courant sur les systèmes Linux comme Ubuntu en raison de la façon dont l'accès au port série est géré. Voici un guide étape par étape pour résoudre ce problème.

---

### Solution : Corriger le problème de permission du port série

#### 1. Ajouter votre utilisateur au groupe `dialout`
Dans Ubuntu, le groupe `dialout` contrôle l'accès aux ports série. Pour résoudre le problème de permission, vous devez ajouter votre utilisateur à ce groupe.

- Ouvrez un terminal en appuyant sur `Ctrl + Alt + T`.
- Exécutez la commande suivante :
  ```bash
  sudo usermod -a -G dialout $USER
  ```
- Cette commande ajoute votre utilisateur actuel au groupe `dialout`. La variable `$USER` utilise automatiquement votre nom d'utilisateur.

#### 2. Se déconnecter et se reconnecter
Pour que le changement de groupe prenne effet, vous devez vous déconnecter de votre session actuelle et vous reconnecter. Alternativement, vous pouvez redémarrer votre système.

- **Pour se déconnecter et se reconnecter :**
  - Sauvegardez tout travail en cours.
  - Cliquez sur votre nom d'utilisateur dans le coin supérieur droit du bureau Ubuntu et sélectionnez "Se déconnecter".
  - Reconnectez-vous avec votre nom d'utilisateur et votre mot de passe.
- **Pour redémarrer (optionnel) :**
  - Exécutez cette commande dans le terminal :
    ```bash
    sudo reboot
    ```
  - Attendez que votre système redémarre.

#### 3. Vérifier le port série
Après vous être reconnecté, assurez-vous que votre Arduino Uno est correctement reconnu par le système.

- Reconnectez votre Arduino Uno au port USB.
- Ouvrez l'IDE Arduino.
- Allez dans **Outils > Port** dans le menu et vérifiez si `/dev/ttyUSB0` (ou `/dev/ttyACM0` pour certaines cartes Arduino) est listé et sélectionné.
- Si le port n'apparaît pas :
  - Débranchez et rebranchez l'Arduino Uno.
  - Vérifiez la connexion USB ou essayez un câble/port différent.

#### 4. Téléverser le sketch à nouveau
Avec le port correct sélectionné, essayez de téléverser votre sketch à nouveau :

```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT); // Définir la broche de la LED intégrée (broche 13) comme sortie
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH); // Allumer la LED
  delay(1000);                     // Attendre 1 seconde
  digitalWrite(LED_BUILTIN, LOW);  // Éteindre la LED
  delay(1000);                     // Attendre 1 seconde
}
```

- Cliquez sur le bouton **Téléverser** (l'icône de flèche droite) dans l'IDE Arduino.
- Si cela réussit, la LED intégrée sur votre Arduino Uno devrait commencer à clignoter (allumée pendant 1 seconde, éteinte pendant 1 seconde).

---

### Dépannage supplémentaire
Si les étapes ci-dessus ne résolvent pas le problème, essayez ces vérifications supplémentaires :

#### Vérifier l'appartenance au groupe
Vérifiez que votre utilisateur fait partie du groupe `dialout` :
- Exécutez cette commande dans le terminal :
  ```bash
  groups $USER
  ```
- Recherchez `dialout` dans la sortie. S'il est manquant, répétez l'Étape 1 et assurez-vous de vous déconnecter/connecter ou de redémarrer.

#### Correction temporaire des permissions (Non recommandée à long terme)
Si vous avez besoin d'une solution rapide, vous pouvez modifier manuellement les permissions du port série :
- Exécutez :
  ```bash
  sudo chmod a+rw /dev/ttyUSB0
  ```
- Ensuite, essayez de téléverser à nouveau. Note : Ceci est temporaire et sera réinitialisé après avoir débranché l'Arduino ou redémarré.

#### Vérifier les logiciels conflictuels
Certains logiciels, comme `brltty` (un pilote d'affichage braille), peuvent interférer avec les ports série. Pour le supprimer :
- Exécutez :
  ```bash
  sudo apt remove brltty
  ```
- Reconnectez votre Arduino et réessayez.

#### Vérifier la connexion Arduino
Assurez-vous qu'Ubuntu reconnaît votre Arduino :
- Exécutez :
  ```bash
  ls /dev/tty*
  ```
- Recherchez `/dev/ttyUSB0` ou `/dev/ttyACM0` lorsque l'Arduino est branché. S'il est manquant, vérifiez votre câble USB ou votre port.

#### Exécuter l'IDE Arduino en tant que root (Solution de contournement temporaire)
En dernier recours, vous pouvez exécuter l'IDE avec les privilèges superutilisateur :
- Fermez l'IDE Arduino.
- Ouvrez un terminal et exécutez :
  ```bash
  sudo arduino-ide
  ```
- Remplacez `arduino-ide` par la commande ou le chemin correct si nécessaire (par exemple, `/home/lzw/arduino-ide_2.3.6_Linux_64bit/arduino-ide`).
- Essayez de téléverser à nouveau. Évitez d'utiliser cette méthode régulièrement, car elle est moins sécurisée.

---

### Confirmer la résolution
Après avoir suivi ces étapes, votre sketch devrait être téléversé avec succès, et la LED sur votre Arduino Uno devrait clignoter comme prévu. Si vous rencontrez toujours des problèmes, veuillez fournir des détails supplémentaires, tels que :
- La sortie de `ls -l /dev/ttyUSB0` (pour vérifier les permissions).
- Tout nouveau message d'erreur de l'IDE Arduino.

Faites-moi savoir si vous avez besoin d'une aide supplémentaire !