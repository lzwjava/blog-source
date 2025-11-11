---
audio: false
generated: true
lang: fr
layout: post
title: Installation de paquets .deb sur Ubuntu
translated: true
type: note
---

Si vous avez téléchargé un fichier `.deb` sur votre système Ubuntu et que vous souhaitez l'installer, il existe quelques méthodes simples pour le faire. Ci-dessous, je vais expliquer l'approche la plus recommandée en utilisant le terminal, ainsi qu'une option graphique si vous préférez une solution par point-and-click.

### **Méthode 1 : Installation via le terminal (Recommandée)**
La façon la plus simple et la plus fiable d'installer un fichier `.deb` dans Ubuntu est d'utiliser la commande `apt`, qui non seulement installe le paquet mais résout également automatiquement toutes les dépendances requises. Voici comment procéder :

1. **Ouvrez le Terminal** : Vous pouvez le faire en appuyant sur `Ctrl + Alt + T` ou en recherchant "Terminal" dans le menu des applications.
2. **Accédez à l'emplacement du fichier** (optionnel) : Si votre fichier `.deb` se trouve dans un dossier spécifique (par exemple, le dossier Téléchargements), utilisez la commande `cd` pour vous y rendre. Par exemple :
   ```bash
   cd ~/Téléchargements
   ```
   Si vous ne souhaitez pas changer de répertoire, vous pouvez spécifier le chemin complet du fichier à l'étape suivante.
3. **Exécutez la commande d'installation** : Utilisez la commande suivante, en remplaçant `nom_du_paquet.deb` par le nom réel de votre fichier `.deb` :
   ```bash
   sudo apt install ./nom_du_paquet.deb
   ```
   - Si le fichier se trouve dans un autre répertoire, fournissez le chemin complet, comme ceci :
     ```bash
     sudo apt install /home/nom_utilisateur/Téléchargements/nom_du_paquet.deb
     ```
   - Le `./` avant le nom du fichier indique à `apt` de rechercher un fichier local plutôt qu'un paquet dans les dépôts.
4. **Entrez votre mot de passe** : Lorsque vous y êtes invité, tapez votre mot de passe utilisateur et appuyez sur Entrée. La commande `sudo` nécessite des privilèges administratifs.
5. **Attendez la fin de l'installation** : `apt` installera le fichier `.deb` et téléchargera toutes les dépendances nécessaires depuis les dépôts Ubuntu. S'il y a des problèmes (par exemple, des dépendances manquantes non trouvées dans les dépôts), il vous en informera.

Cette méthode fonctionne sur Ubuntu 16.04 et versions ultérieures, car elle utilise une fonctionnalité de `apt` introduite dans la version 1.1. Elle est recommandée car elle allie simplicité et gestion des dépendances.

### **Méthode 2 : Installation via l'interface graphique**
Si vous préférez ne pas utiliser le terminal, les outils graphiques d'Ubuntu peuvent également gérer les fichiers `.deb` :
1. **Localisez le fichier** : Ouvrez votre gestionnaire de fichiers (par exemple, Nautilus) et accédez au dossier contenant le fichier `.deb` (probablement Téléchargements).
2. **Double-cliquez sur le fichier** : Cela devrait automatiquement ouvrir le fichier avec le Logicial Ubuntu (ou une application similaire, selon votre version d'Ubuntu).
3. **Cliquez sur Installer** : Dans la fenêtre du Logicial Ubuntu, cliquez sur le bouton "Installer". Il vous sera peut-être demandé de saisir votre mot de passe.
4. **Attendez la fin de l'opération** : L'installation se déroulera et vous verrez une confirmation une fois terminée.

Cette méthode est conviviale mais nécessite un environnement de bureau et peut ne pas fournir de retour d'information détaillé en cas de problème.

### **Notes importantes**
- **Sources de confiance** : N'installez des fichiers `.deb` qu'à partir de sources de confiance, car ils peuvent potentiellement nuire à votre système s'ils contiennent du code malveillant.
- **Vérifier l'installation** : Après l'installation, vous pouvez vérifier que le logiciel est installé en exécutant :
  ```bash
  dpkg -l | grep nom_du_paquet
  ```
  (Remplacez `nom_du_paquet` par le nom du logiciel, et non par le nom complet du fichier `.deb`.)
- **Problèmes de dépendances** : Si `apt` ne peut pas résoudre les dépendances, vous devrez peut-être les trouver et les installer manuellement ou utiliser une version différente du fichier `.deb` compatible avec votre système.

### **Exemple**
Supposons que vous ayez téléchargé un fichier nommé `vscode.deb` dans votre dossier Téléchargements. Ouvrez un terminal et exécutez :
```bash
sudo apt install ~/Téléchargements/vscode.deb
```
Cela installera Visual Studio Code (ou quel que soit le contenu du paquet) ainsi que ses dépendances.

C'est tout ! Vous avez maintenant installé votre fichier `.deb` sur Ubuntu. Faites-moi savoir si vous rencontrez des problèmes !