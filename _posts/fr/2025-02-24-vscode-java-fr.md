---
audio: false
lang: fr
layout: post
title: Configurer le compilateur Java dans Visual Studio Code
translated: true
---

Salut ! Pour configurer le compilateur Java dans Visual Studio Code (VSCode) version 1.96.4 sur Windows, surtout si vous avez déjà installé le pack d'extensions Java, vous devrez configurer le chemin du Java Development Kit (JDK). Le compilateur Java fait partie du JDK, et VSCode doit savoir où le trouver pour compiler votre code Java. Voici un guide étape par étape pour vous aider à configurer :

---

### Étape 1 : Assurez-vous d'avoir un JDK installé
Avant de configurer quoi que ce soit dans VSCode, assurez-vous d'avoir un JDK (et non un JRE) installé sur votre machine Windows. Le JDK inclut le compilateur Java (`javac`). Si vous ne l'avez pas encore installé, vous pouvez le télécharger auprès d'un fournisseur comme Oracle, OpenJDK ou Adoptium (par exemple, JDK 17 ou une autre version compatible avec votre projet). Après l'installation, notez le chemin d'installation (par exemple, `C:\Program Files\Java\jdk-17.0.1`).

---

### Étape 2 : Ouvrir les paramètres de VSCode
Pour indiquer à VSCode où se trouve votre JDK, vous devrez ajuster ses paramètres :

- **Via l'interface des paramètres :**
  - Appuyez sur `Ctrl + ,` pour ouvrir le panneau des paramètres.
  - Alternativement, allez dans `File > Preferences > Settings`.
- **Via settings.json (optionnel) :**
  - Appuyez sur `Ctrl + Shift + P` pour ouvrir la palette de commandes.
  - Tapez **"Open Settings (JSON)"** et sélectionnez-le pour éditer directement le fichier `settings.json`.

---

### Étape 3 : Définir le chemin du JDK avec `java.home`
Le pack d'extensions Java s'appuie sur le paramètre `java.home` pour localiser votre JDK pour la compilation et les fonctionnalités du langage (comme IntelliSense). Voici comment le configurer :

- **Dans l'interface des paramètres :**
  - Dans le panneau des paramètres, recherchez **"java.home"**.
  - Dans le champ "Java: Home", entrez le chemin complet de votre installation JDK. Par exemple :
    ```
    C:\Program Files\Java\jdk-17.0.1
    ```
  - Utilisez des barres obliques inverses (`\`) puisque vous êtes sous Windows, et assurez-vous que le chemin pointe vers le répertoire racine du JDK (il doit contenir un dossier `bin` avec `javac.exe`).

- **Dans settings.json :**
  - Si vous éditez `settings.json`, ajoutez cette ligne (remplacez le chemin par l'emplacement réel de votre JDK) :
    ```json
    "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    ```
  - Exemple complet de `settings.json` :
    ```json
    {
        "java.home": "C:\\Program Files\\Java\\jdk-17.0.1"
    }
    ```
  - Enregistrez le fichier après modification.

---

### Étape 4 : Vérifier le chemin
Double-checkez que :
- Le chemin pointe vers un JDK (et non un JRE). Le dossier `bin` du JDK doit inclure `javac.exe`.
- Il n'y a pas de fautes de frappe dans le chemin, et qu'il correspond à l'emplacement de votre installation JDK (par exemple, `C:\Program Files\Java\jdk-17.0.1`).

Si vous n'êtes pas sûr de l'emplacement de votre JDK, vous pouvez le trouver dans `C:\Program Files\Java` ou à l'endroit où vous l'avez choisi lors de l'installation.

---

### Étape 5 : Optionnel - Configurer plusieurs JDK
Si vous avez plusieurs versions de JDK installées et que vous souhaitez basculer entre elles (par exemple, JDK 8 pour un projet, JDK 17 pour un autre), vous pouvez utiliser le paramètre `java.configuration.runtimes` :

- Ajoutez ceci à votre `settings.json` :
  ```json
  "java.configuration.runtimes": [
      {
          "name": "JavaSE-1.8",
          "path": "C:\\Program Files\\Java\\jdk1.8.0_291"
      },
      {
          "name": "JavaSE-17",
          "path": "C:\\Program Files\\Java\\jdk-17.0.1",
          "default": true
      }
  ]
  ```
- L'option `default: true` définit le runtime par défaut pour exécuter votre code. Cependant, pour la compilation, l'extension Java utilise principalement le JDK spécifié dans `java.home`.

---

### Étape 6 : Relancer ou redémarrer VSCode
Après avoir défini `java.home`, vous devrez peut-être :
- Relancer la fenêtre VSCode (appuyez sur `Ctrl + Shift + P`, tapez **"Reload Window"**, et sélectionnez-le).
- Ou redémarrer complètement VSCode pour que les modifications prennent effet.

---

### Notes sur la compilation
- **Fichiers Java uniques :** Si vous travaillez avec des fichiers `.java` individuels (sans outils de construction), le pack d'extensions Java "Language Support for Java(TM) by Red Hat" utilise le JDK de `java.home` pour compiler et exécuter votre code. Vous pouvez utiliser le bouton "Run" ou la commande **"Java: Run"**.
- **Projets avec des outils de construction :** Si vous utilisez Maven, Gradle ou un autre outil de construction, le compilateur est géré par la configuration de l'outil de construction (par exemple, la variable d'environnement `JAVA_HOME`, `pom.xml` pour Maven, ou `build.gradle` pour Gradle). Cependant, la définition de `java.home` assure toujours que les fonctionnalités linguistiques de VSCode fonctionnent correctement.

---

### Dépannage
- **Problèmes de chemin :** Si VSCode ne trouve pas le JDK, vérifiez le chemin dans `java.home`. Évitez les espaces ou les guillemets supplémentaires sauf si nécessaire.
- **JDK non installé :** Si vous obtenez des erreurs concernant l'absence de `javac`, assurez-vous qu'un JDK est installé.
- **Compatibilité des versions :** Assurez-vous que la version de votre JDK correspond aux exigences de votre projet (par exemple, JDK 8, 11, 17).

---

C'est tout ! Vous devriez maintenant avoir le compilateur Java configuré dans VSCode. Si vous rencontrez des problèmes ou avez d'autres questions—comme travailler avec un outil de construction spécifique—n'hésitez pas à me le faire savoir, et je serai heureux de vous aider davantage ! 😊

---

Définissez `maven.terminal.userJavaHome` sur true. Vous pouvez vérifier la version de Java dans le terminal.