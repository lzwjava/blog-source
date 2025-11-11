---
audio: false
generated: true
lang: fr
layout: post
title: Débogage distant de VSCode
translated: true
type: note
---

Pour effectuer un débogage distant dans Visual Studio Code (VSCode) pour un serveur WebSphere Liberty exécuté en mode débogage, vous pouvez utiliser les fonctionnalités de débogage Java intégrées à VSCode. Vous trouverez ci-dessous les étapes détaillées pour configurer cela sans installer de plugins spécifiques à WebSphere Liberty, en supposant que vous avez le **Java Extension Pack** standard (qui inclut le **Debugger for Java**) déjà installé.

---

### Étape 1 : Démarrer le serveur WebSphere Liberty en mode débogage
1. Ouvrez un terminal ou une invite de commande.
2. Accédez à votre répertoire d'installation WebSphere Liberty.
3. Exécutez la commande suivante pour démarrer votre serveur en mode débogage :
   ```
   server debug default
   ```
   - Remplacez `default` par le nom de votre serveur s'il est différent.
4. Le serveur démarrera avec le débogage activé, écoutant généralement sur le port **7777**.
5. Vérifiez la sortie console ou les journaux du serveur pour un message tel que :
   ```
   Listening for transport dt_socket at address: 7777
   ```
   - Ceci confirme le port de débogage. S'il s'agit d'un port différent (par exemple, en raison d'un conflit), notez le numéro affiché.

---

### Étape 2 : Configurer le débogage distant dans VSCode
1. **Ouvrez votre projet dans VSCode** :
   - Assurez-vous que votre projet Java (contenant le code source déployé sur le serveur) est ouvert dans VSCode. Ceci permet au débogueur de mapper les points d'arrêt au code en cours d'exécution.

2. **Accédez à la vue Exécuter et Déboguer** :
   - Cliquez sur l'icône **Exécuter et Déboguer** dans la barre latérale gauche (un bouton play avec un insecte) ou appuyez sur `Ctrl+Shift+D` (Windows/Linux) ou `Cmd+Shift+D` (Mac).

3. **Créez ou modifiez le fichier `launch.json`** :
   - Dans la vue **Exécuter et Déboguer**, cliquez sur l'icône en forme de **roue dentée** à côté de la liste déroulante des configurations.
   - Si vous êtes invité à sélectionner un environnement, choisissez **Java**. Ceci crée un fichier `launch.json` dans le dossier `.vscode` de votre espace de travail.
   - Si le fichier existe déjà, il s'ouvre pour modification.

4. **Ajoutez une configuration de débogage** :
   - Dans le fichier `launch.json`, assurez-vous qu'il contient une configuration pour se connecter à la JVM distante. Voici un exemple :
     ```json
     {
         "version": "0.2.0",
         "configurations": [
             {
                 "type": "java",
                 "name": "Attach to WebSphere Liberty",
                 "request": "attach",
                 "hostName": "localhost",
                 "port": 7777
             }
         ]
     }
     ```
   - **Explication des champs** :
     - `"type": "java"` : Spécifie le débogueur Java.
     - `"name": "Attach to WebSphere Liberty"` : Un nom descriptif pour cette configuration.
     - `"request": "attach"` : Indique que VSCode se connectera à un processus JVM existant.
     - `"hostName": "localhost"` : Le nom d'hôte de la machine exécutant le serveur. Utilisez l'adresse IP ou le nom d'hôte du serveur s'il se trouve sur une machine différente.
     - `"port": 7777` : Le port de débogage de l'Étape 1. Mettez à jour ceci si le serveur utilise un port différent.

5. **Enregistrez le fichier** :
   - Enregistrez le fichier `launch.json` après avoir ajouté ou modifié la configuration.

---

### Étape 3 : Démarrer la session de débogage
1. **Assurez-vous que le serveur est en cours d'exécution** :
   - Vérifiez que le serveur WebSphere Liberty est toujours en cours d'exécution en mode débogage depuis l'Étape 1.

2. **Sélectionnez la configuration** :
   - Dans la vue **Exécuter et Déboguer**, sélectionnez **"Attach to WebSphere Liberty"** dans le menu déroulant en haut.

3. **Lancez le débogueur** :
   - Cliquez sur le bouton **play vert** ou appuyez sur `F5`. VSCode se connectera au processus JVM du serveur.

4. **Définissez des points d'arrêt** :
   - Ouvrez vos fichiers source Java dans VSCode.
   - Cliquez dans la gouttière (à gauche des numéros de ligne) pour définir des points d'arrêt où vous souhaitez que l'exécution s'interrompe.

5. **Interagissez avec l'application** :
   - Utilisez votre application (par exemple, envoyez des requêtes HTTP) pour déclencher les chemins de code avec des points d'arrêt. Lorsqu'un point d'arrêt est atteint, VSCode interrompra l'exécution, vous permettant d'inspecter les variables, d'exécuter le code pas à pas et de déboguer.

---

### Notes supplémentaires
- **Serveur local vs distant** :
  - Si le serveur s'exécute sur une machine différente, remplacez `"localhost"` par le nom d'hôte ou l'adresse IP du serveur dans le fichier `launch.json`. Assurez-vous que le port de débogage est accessible via le réseau (par exemple, qu'il n'est pas bloqué par un pare-feu).

- **Confirmation du port de débogage** :
  - Si vous n'êtes pas sûr du port, vérifiez toujours la sortie du serveur après avoir exécuté `server debug default`. Il indiquera explicitement le port sur lequel il écoute.

- **Correspondance du code source** :
  - Le code source dans VSCode doit correspondre au code exécuté sur le serveur pour que les points d'arrêt fonctionnent correctement. Assurez-vous que votre projet est à jour et compilé avec les informations de débogage (la valeur par défaut dans la plupart des builds Java).

- **Comportement du serveur** :
  - Avec `server debug default`, le serveur démarre immédiatement (sans attendre un débogueur). Vous pouvez connecter VSCode à tout moment pendant son exécution.

- **Prérequis** :
  - Le **Java Extension Pack** (ou au moins l'extension **Debugger for Java**) doit être installé dans VSCode. Il s'agit d'un outil standard pour le développement Java et fournit les capacités de débogage nécessaires.

---

En suivant ces étapes, vous pouvez déboguer efficacement votre serveur WebSphere Liberty à distance en utilisant les fonctionnalités intégrées de VSCode, sans avoir besoin de plugins supplémentaires spécifiques à WebSphere.