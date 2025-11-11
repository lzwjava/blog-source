---
audio: false
generated: true
lang: fr
layout: post
title: Débogage d'Applications Spring Boot dans Visual Studio Code
translated: true
type: note
---

Pour déboguer un projet Maven Spring Boot dans Visual Studio Code (VSCode), vous pouvez suivre ces étapes simples pour configurer et exécuter votre application en mode débogage. Ce guide suppose que vous avez un projet Maven Spring Boot basique avec un fichier `pom.xml` et une classe principale annotée avec `@SpringBootApplication`. Voici comment procéder :

### Étape 1 : Installer les Extensions Nécessaires
Avant de commencer, assurez-vous que VSCode est équipé des extensions requises pour le développement Java et Spring Boot :
- **Java Extension Pack** : Cela inclut des outils essentiels comme Language Support for Java par Red Hat, qui fournit des capacités de débogage, ainsi que d'autres utilitaires pour le développement Java.
- **Spring Boot Extension Pack** : Ce pack améliore le développement Spring Boot avec des fonctionnalités comme le Spring Boot Dashboard, Spring Boot Tools, et plus encore.

Pour les installer :
1. Ouvrez VSCode.
2. Allez dans la vue Extensions (`Ctrl+Shift+X` ou `Cmd+Shift+X` sur macOS).
3. Recherchez "Java Extension Pack" et "Spring Boot Extension Pack", puis cliquez sur **Installer** pour chacun.

### Étape 2 : Ouvrir Votre Projet Maven Spring Boot
- Lancez VSCode et ouvrez votre dossier de projet en sélectionnant **Fichier > Ouvrir un dossier** et en choisissant le répertoire contenant votre fichier `pom.xml`.
- VSCode détectera le `pom.xml`, et le Java Extension Pack indexera automatiquement le projet et résoudra les dépendances. Cela peut prendre un moment, alors attendez que le processus se termine (vous verrez la progression dans la barre d'état en bas à droite).

### Étape 3 : Créer ou Modifier le Fichier `launch.json`
Pour configurer le débogage, vous devez créer un fichier `launch.json` dans VSCode :
1. Ouvrez la vue **Exécuter et Déboguer** en cliquant sur l'icône de punaise et de lecture dans la barre latérale ou en appuyant sur `Ctrl+Shift+D`.
2. Si aucune configuration de débogage n'existe, cliquez sur **"create a launch.json file"**. Si une configuration existe déjà, cliquez sur l'icône d'engrenage pour la modifier.
3. Lorsque vous y êtes invité, sélectionnez **Java** comme environnement. VSCode générera un fichier `launch.json` par défaut dans un dossier `.vscode` de votre projet.
4. Ajoutez ou modifiez une configuration de débogage pour votre application Spring Boot. Voici un exemple de configuration :

    ```json
    {
        "type": "java",
        "name": "Debug Spring Boot",
        "request": "launch",
        "mainClass": "com.example.demo.DemoApplication",
        "projectName": "demo"
    }
    ```

    - Remplacez `"com.example.demo.DemoApplication"` par le nom qualifié complet de votre classe principale (par exemple, `com.yourcompany.yourapp.YourApplication`).
    - Remplacez `"demo"` par le nom de votre projet, généralement le `<artifactId>` de votre `pom.xml`.

5. Enregistrez le fichier `launch.json`.

#### Optionnel : Ajouter des Arguments
Si votre application nécessite des arguments spécifiques (par exemple, des profils Spring), vous pouvez les inclure :
```json
{
    "type": "java",
    "name": "Debug Spring Boot",
    "request": "launch",
    "mainClass": "com.example.demo.DemoApplication",
    "projectName": "demo",
    "args": "--spring.profiles.active=dev"
}
```

### Étape 4 : Démarrer le Débogage
- Dans la vue **Exécuter et Déboguer**, sélectionnez **"Debug Spring Boot"** dans le menu déroulant en haut.
- Cliquez sur le bouton de lecture vert (ou appuyez sur `F5`) pour lancer l'application en mode débogage.
- VSCode compilera le projet en utilisant Maven, démarrera l'application Spring Boot et attachera automatiquement le débogueur.

### Étape 5 : Définir des Points d'Arrêt et Déboguer
- Ouvrez un fichier Java dans votre projet (par exemple, une classe de contrôleur ou de service).
- Définissez des points d'arrêt en cliquant dans la gouttière à gauche des numéros de ligne, où un point rouge apparaîtra.
- Interagissez avec votre application (par exemple, via un navigateur ou un client API). Lorsque l'exécution atteint un point d'arrêt, VSCode se mettra en pause, vous permettant de :
  - Inspecter les variables dans le panneau **Variables**.
  - Parcourir le code pas à pas en utilisant des contrôles comme **Step Over** (`F10`), **Step Into** (`F11`), ou **Continue** (`F5`).
  - Voir la pile d'appels et plus dans la barre latérale de débogage.

### Méthodes Alternatives
Bien que la méthode `launch.json` soit recommandée pour sa flexibilité, vous pouvez également déboguer en utilisant :
- **Vue Maven** :
  1. Ouvrez la vue Maven dans la barre latérale (recherchez l'icône "M" ou activez-la via Extensions).
  2. Développez votre projet, naviguez vers `spring-boot` sous Plugins, faites un clic droit sur `spring-boot:run`, et sélectionnez **Debug**.
  3. L'application démarrera et le débogueur s'attachera.
- **Spring Boot Dashboard** :
  1. Ouvrez le Spring Boot Dashboard (généralement dans la vue Explorateur ou via la palette de commandes : `Spring Boot Dashboard`).
  2. Localisez votre application, faites un clic droit dessus, et sélectionnez **Debug** (si disponible).

### Prérequis et Notes
- Assurez-vous que **Maven** est installé sur votre système et accessible via la ligne de commande, ou utilisez le Maven intégré de VSCode (configuré via les paramètres si nécessaire).
- Vérifiez que votre projet se construit avec succès (`mvn clean install`) pour éviter les erreurs d'exécution pendant le débogage.
- Utilisez une version de Java compatible comme spécifié dans votre `pom.xml` (par exemple, via `<java.version>`).

En suivant ces étapes, vous pouvez déboguer efficacement votre projet Maven Spring Boot dans VSCode, en tirant parti de ses outils de débogage puissants pour identifier et résoudre les problèmes dans votre code.