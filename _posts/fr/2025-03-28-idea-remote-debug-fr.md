---
audio: false
generated: true
lang: fr
layout: post
title: Débogage à distance intégré d'IntelliJ IDEA
translated: true
type: note
---

Pour connecter IntelliJ IDEA au port de débogage d'un serveur WebSphere Liberty que vous avez démarré avec `server debug default`, sans utiliser le plugin WebSphere Liberty, vous pouvez exploiter la fonctionnalité de débogage distant intégrée d'IntelliJ IDEA. Cette approche fonctionne car WebSphere Liberty, lorsqu'il est démarré en mode débogage, expose un port de débogage (généralement 7777 par défaut) auquel tout débogueur JVM, y compris IntelliJ IDEA, peut se connecter. Voici les étapes détaillées pour y parvenir :

---

### Étape 1 : Démarrer le serveur WebSphere Liberty en mode débogage
Lorsque vous exécutez `server debug default` (en supposant que "default" est le nom de votre serveur ; remplacez-le par le nom réel de votre serveur si différent), WebSphere Liberty démarre avec le débogage activé. Par défaut, cette commande configure le serveur pour écouter les connexions de débogage sur le port **7777**.

- **Commande** :
  ```bash
  server debug default
  ```
- **Ce que cela fait** : Cela démarre le serveur "default" en mode débogage, activant automatiquement les options de débogage JVM (par exemple, `-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=7777`).
- **Vérification** : Après avoir exécuté la commande, vérifiez la sortie de la console du serveur ou les journaux (par exemple, `messages.log`) pour confirmer que le serveur écoute sur le port de débogage. Recherchez un message indiquant le port de débogage (généralement 7777 sauf s'il a été remplacé ou n'est pas disponible).

---

### Étape 2 : Confirmer le port de débogage
Le port de débogage par défaut pour WebSphere Liberty est **7777**. Cependant, si ce port est utilisé ou a été personnalisé :
- Vérifiez la sortie de la console après le démarrage du serveur. Elle devrait afficher un message comme "Listening for debugger connections on port 7777."
- Si le port est différent (par exemple, un port aléatoire est attribué en raison d'un conflit), notez le numéro de port réel pour l'utiliser dans IntelliJ IDEA.

Pour ce guide, nous supposerons le port par défaut **7777** sauf indication contraire de votre configuration.

---

### Étape 3 : Configurer le débogage distant dans IntelliJ IDEA
La fonctionnalité de débogage distant d'IntelliJ IDEA vous permet de vous connecter à la JVM du serveur sans avoir besoin d'un plugin WebSphere spécifique. Voici comment la configurer :

1. **Ouvrir les Configurations d'exécution/débogage** :
   - Dans IntelliJ IDEA, allez dans le menu supérieur et sélectionnez **Run > Edit Configurations**.

2. **Ajouter une nouvelle configuration de débogage distant** :
   - Cliquez sur le bouton **+** (ou "Add New Configuration") dans le coin supérieur gauche.
   - Dans la liste, sélectionnez **Remote JVM Debug** (cela peut simplement dire "Remote" selon votre version d'IntelliJ).

3. **Définir les détails de la configuration** :
   - **Name** : Donnez-lui un nom significatif, par exemple "WebSphere Liberty Debug."
   - **Host** : Définissez-le sur `localhost` (en supposant que le serveur s'exécute sur la même machine qu'IntelliJ IDEA ; utilisez l'adresse IP du serveur s'il est distant).
   - **Port** : Définissez-le sur `7777` (ou le port de débogage réel si différent).
   - **Transport** : Assurez-vous qu'il est défini sur **Socket**.
   - **Debugger Mode** : Sélectionnez **Attach** (cela indique à IntelliJ de se connecter à une JVM déjà en cours d'exécution).
   - Laissez les autres paramètres (comme "Command line arguments for remote JVM") par défaut sauf si vous avez besoin d'options JVM spécifiques.

4. **Sauvegarder la configuration** :
   - Cliquez sur **Apply** puis sur **OK** pour sauvegarder.

---

### Étape 4 : Démarrer le débogage
Avec le serveur fonctionnant en mode débogage et la configuration mise en place :
- Allez dans **Run > Debug** (ou cliquez sur l'icône de punaise) et sélectionnez votre nouvelle configuration (par exemple, "WebSphere Liberty Debug").
- IntelliJ IDEA tentera de se connecter à la JVM du serveur sur l'hôte et le port spécifiés.
- En cas de succès, vous verrez un message dans la fenêtre Debug comme "Connected to the target VM, address: 'localhost:7777'."

---

### Étape 5 : Déboguer votre application
- **Définir des points d'arrêt** : Dans votre code source, cliquez dans la gouttière à côté des numéros de ligne pour ajouter des points d'arrêt où vous souhaitez que l'exécution s'interrompe.
- **Déclencher l'exécution** : Interagissez avec votre application (par exemple, envoyez une requête au serveur) pour atteindre les points d'arrêt.
- **Déboguer** : Une fois qu'un point d'arrêt est atteint, utilisez les outils de débogage d'IntelliJ (step over, step into, resume, etc.) pour inspecter les variables et contrôler l'exécution.

---

### Notes supplémentaires
- **Serveur Local vs. Distant** : Si WebSphere Liberty s'exécute sur une machine différente, remplacez `localhost` par l'adresse IP du serveur dans la configuration de débogage distant. Assurez-vous que le port de débogage (par exemple, 7777) est ouvert et non bloqué par un pare-feu.
- **Conflits de ports** : Si le port 7777 n'est pas disponible au démarrage du serveur, WebSphere Liberty peut choisir un port aléatoire. Vérifiez la sortie du serveur pour confirmer le port et mettez à jour la configuration IntelliJ en conséquence.
- **Aucun plugin nécessaire** : Cette méthode utilise la fonctionnalité de débogage distant standard d'IntelliJ IDEA, donc aucun plugin WebSphere Liberty n'est requis.

---

### Résumé
En démarrant votre serveur WebSphere Liberty avec `server debug default` (ce qui active le débogage sur le port 7777 par défaut) et en configurant une configuration de débogage distant dans IntelliJ IDEA, vous pouvez vous connecter au port de débogage du serveur sans le plugin WebSphere Liberty. Cela vous donne toutes les capacités de débogage — points d'arrêt, inspection des variables et exécution pas à pas — directement dans IntelliJ IDEA.

---

L'exécution et le débogage d'applications WebSphere Liberty dans IntelliJ IDEA sans le plugin dédié Liberty Tools sont réalisables en configurant manuellement le runtime Liberty et en configurant IntelliJ IDEA pour le débogage distant et l'exécution d'outils externes. Cette approche nécessite quelques étapes manuelles par rapport à l'utilisation du plugin intégré, mais elle fournit la fonctionnalité nécessaire pour développer et dépanner vos applications Liberty.

Voici une description du processus :

**1. Obtenir et installer le runtime WebSphere Liberty :**

Puisque vous n'avez pas le plugin pour gérer le runtime à votre place, vous devrez télécharger et installer le runtime WebSphere Liberty manuellement. Vous pouvez obtenir le runtime depuis le site web officiel d'IBM ou via d'autres méthodes de distribution comme Maven ou Gradle si vous gérez votre projet avec ces outils.

Typiquement, l'installation manuelle implique de télécharger un fichier ZIP ou JAR et de l'extraire dans un répertoire de votre système. Ce répertoire sera votre répertoire d'installation Liberty (`<LIBERTY_HOME>`).

**2. Configurer le serveur Liberty pour le débogage :**

Pour déboguer votre application, vous devez démarrer le serveur Liberty avec le débogage activé. Cela se fait en ajoutant des options JVM spécifiques au démarrage du serveur. Ces options indiquent à la Java Virtual Machine (JVM) d'écouter une connexion de débogueur sur un port spécifique.

Localisez le fichier `jvm.options` dans le répertoire de configuration de votre serveur Liberty (`<LIBERTY_HOME>/usr/servers/<your_server_name>/`). Si ce fichier n'existe pas, vous pouvez le créer. Ajoutez la ligne suivante au fichier `jvm.options` :

```
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005
```

  * `-agentlib:jdwp` : Charge la bibliothèque Java Debug Wire Protocol (JDWP).
  * `transport=dt_socket` : Spécifie que le débogueur se connectera en utilisant un socket.
  * `server=y` : Indique que la JVM agira comme le serveur, écoutant une connexion de débogueur.
  * `suspend=n` : Spécifie que la JVM ne doit pas attendre que le débogueur se connecte avant de démarrer. Vous pouvez changer ceci en `suspend=y` si vous devez déboguer du code qui s'exécute pendant le démarrage du serveur.
  * `address=5005` : Définit le numéro de port auquel le débogueur se connectera. Vous pouvez le changer pour n'importe quel port disponible.

**3. Configurer IntelliJ IDEA pour exécuter Liberty :**

Vous pouvez utiliser la configuration "External Tools" d'IntelliJ IDEA pour démarrer votre serveur Liberty depuis l'IDE.

  * Allez dans `File` > `Settings` (ou `IntelliJ IDEA` > `Preferences` sur macOS).
  * Naviguez vers `Tools` > `External Tools`.
  * Cliquez sur l'icône `+` pour ajouter un nouvel outil externe.
  * Configurez l'outil avec les détails suivants :
      * **Name :** Donnez-lui un nom descriptif, par exemple "Start Liberty Server".
      * **Program :** Parcourez jusqu'au script du serveur Liberty. Ce sera typiquement `<LIBERTY_HOME>/bin/server` pour Linux/macOS ou `<LIBERTY_HOME>\bin\server.bat` pour Windows.
      * **Arguments :** Ajoutez les arguments pour démarrer votre instance de serveur spécifique. C'est généralement `start <your_server_name>`, où `<your_server_name>` est le nom de votre répertoire de serveur dans `<LIBERTY_HOME>/usr/servers/`.
      * **Working directory :** Définissez-le sur `<LIBERTY_HOME>/bin`.

Maintenant, vous pouvez démarrer votre serveur Liberty en allant dans `Tools` > `External Tools` et en sélectionnant l'outil que vous venez de configurer.

**4. Configurer IntelliJ IDEA pour le débogage distant :**

Pour déboguer votre application s'exécutant sur le serveur Liberty démarré manuellement, vous utiliserez la configuration "Remote JVM Debug" d'IntelliJ IDEA.

  * Allez dans `Run` > `Edit Configurations`.
  * Cliquez sur l'icône `+` et sélectionnez `Remote JVM Debug`.
  * Configurez les paramètres :
      * **Name :** Donnez-lui un nom descriptif, par exemple "Debug Liberty Server".
      * **Debugger mode :** Sélectionnez `Attach to remote JVM`.
      * **Host :** Entrez `localhost` (ou l'adresse IP de la machine exécutant Liberty si elle n'est pas sur votre machine locale).
      * **Port :** Entrez le numéro de port que vous avez configuré dans le fichier `jvm.options` (par exemple, `5005`).
      * **Use module classpath of :** Sélectionnez le module dans votre projet IntelliJ IDEA qui contient le code de votre application Liberty. Cela aide IntelliJ IDEA à mapper le code en cours d'exécution à vos fichiers sources pour le débogage.

**5. Exécuter et déboguer :**

1.  Démarrez le serveur Liberty en utilisant la configuration "External Tools" que vous avez créée dans IntelliJ IDEA.
2.  Attendez que le serveur démarre et indique qu'il écoute le débogueur sur le port configuré (vous devriez voir un message dans la sortie de la console du serveur).
3.  Définissez des points d'arrêt dans le code de votre application dans IntelliJ IDEA.
4.  Allez dans `Run` > `Debug` et sélectionnez la configuration "Debug Liberty Server" que vous avez créée.

IntelliJ IDEA tentera de se connecter au serveur Liberty en cours d'exécution sur le port spécifié. Une fois connecté, vous pouvez utiliser toutes les fonctionnalités de débogage d'IntelliJ IDEA, telles que l'exécution pas à pas du code, l'inspection des variables et l'évaluation d'expressions.

En suivant ces étapes, vous pouvez exécuter et déboguer efficacement vos applications WebSphere Liberty dans IntelliJ IDEA sans dépendre du plugin dédié Liberty Tools, vous donnant un contrôle direct sur le cycle de vie du serveur et le processus de débogage.