---
audio: false
generated: true
lang: fr
layout: post
title: Configuration de launch.json pour Spring Boot dans VSCode
translated: true
type: note
---

Pour configurer le fichier `launch.json` pour un projet Maven Spring Boot dans Visual Studio Code (VSCode), vous devez configurer une configuration de lancement qui permet à VSCode d'exécuter et de déboguer votre application en utilisant ses extensions Java. Voici un guide étape par étape pour vous aider à y parvenir.

### Prérequis
Avant de continuer, assurez-vous des points suivants :
- Vous avez le **Java Extension Pack** installé dans VSCode. Ce pack inclut des extensions essentielles comme "Debugger for Java" et "Language Support for Java" par Red Hat, qui fournissent le support pour exécuter et déboguer des applications Java, y compris les projets Spring Boot.
- Votre projet Spring Boot est un projet Maven avec un fichier `pom.xml` valide.
- Le projet a une classe principale annotée avec `@SpringBootApplication`, qui contient la méthode `main` pour démarrer l'application.

### Étapes pour configurer `launch.json`
1. **Localiser la classe principale**
   - Dans un projet Spring Boot typique, la classe principale se trouve dans le répertoire `src/main/java` et est annotée avec `@SpringBootApplication`. Par exemple, elle pourrait s'appeler `com.example.demo.DemoApplication`.
   - Ouvrez votre projet dans VSCode et identifiez le nom pleinement qualifié de cette classe (par exemple, `com.example.demo.DemoApplication`).

2. **Déterminer le nom du projet**
   - Le nom du projet dans un projet Maven correspond à l'`artifactId` défini dans votre fichier `pom.xml`.
   - Ouvrez votre fichier `pom.xml` et cherchez la balise `<artifactId>`. Par exemple :
     ```xml
     <artifactId>demo</artifactId>
     ```
     Ici, le nom du projet serait `demo`.

3. **Ouvrir la vue Débogage**
   - Dans VSCode, cliquez sur l'icône **Déboguer** dans la barre latérale gauche (ou appuyez sur `Ctrl+Shift+D` / `Cmd+Shift+D` sur Mac).
   - Cliquez sur l'icône d'engrenage ⚙️ à côté du menu déroulant "Exécuter et déboguer" pour configurer les paramètres de lancement. Si aucun `launch.json` n'existe, VSCode vous invitera à en créer un.

4. **Créer ou modifier `launch.json`**
   - Si vous êtes invité à sélectionner un environnement, choisissez **Java**. Cela générera un fichier `launch.json` basique dans le dossier `.vscode` de votre projet.
   - Ouvrez le fichier `launch.json`. S'il existe déjà, vous pouvez le modifier directement.

5. **Ajouter une configuration de lancement**
   - Ajoutez la configuration suivante à l'intérieur du tableau `"configurations"` dans `launch.json`. Remplacez les espaces réservés par les détails de votre projet :
     ```json
     {
         "type": "java",
         "name": "Lancer l'application Spring Boot",
         "request": "launch",
         "mainClass": "com.example.demo.DemoApplication",
         "projectName": "demo"
     }
     ```
     - **Explication des champs :**
       - `"type": "java"` : Spécifie qu'il s'agit d'une configuration de lancement Java.
       - `"name": "Lancer l'application Spring Boot"` : Un nom descriptif pour cette configuration, qui apparaîtra dans le menu déroulant de débogage.
       - `"request": "launch"` : Indique que VSCode doit lancer l'application (par opposition à s'attacher à un processus existant).
       - `"mainClass"` : Le nom pleinement qualifié de votre classe principale Spring Boot (par exemple, `com.example.demo.DemoApplication`).
       - `"projectName"` : L'`artifactId` de votre `pom.xml` (par exemple, `demo`), qui aide VSCode à localiser le projet dans une configuration multi-module.

   - Voici un exemple de fichier `launch.json` complet avec cette configuration :
     ```json
     {
         "version": "0.2.0",
         "configurations": [
             {
                 "type": "java",
                 "name": "Lancer l'application Spring Boot",
                 "request": "launch",
                 "mainClass": "com.example.demo.DemoApplication",
                 "projectName": "demo"
             }
         ]
     }
     ```

6. **Optionnel : Ajouter des arguments VM ou des arguments de programme**
   - Si votre application nécessite des paramètres supplémentaires (par exemple, activer un profil Spring), vous pouvez les ajouter en utilisant `"vmArgs"` ou `"args"` :
     - Exemple avec un profil Spring :
       ```json
       {
           "type": "java",
           "name": "Lancer l'application Spring Boot avec Profil",
           "request": "launch",
           "mainClass": "com.example.demo.DemoApplication",
           "projectName": "demo",
           "vmArgs": "-Dspring.profiles.active=dev"
       }
       ```
       Ceci définit la propriété `spring.profiles.active` sur `dev`.
     - Exemple avec des arguments de programme :
       ```json
       "args": ["arg1", "arg2"]
       ```

7. **Sauvegarder et exécuter**
   - Sauvegardez le fichier `launch.json`.
   - Retournez dans la vue Débogage, sélectionnez **"Lancer l'application Spring Boot"** dans le menu déroulant, et cliquez sur le bouton de lecture vert (ou appuyez sur `F5`).
   - VSCode construira et exécutera votre application Spring Boot en utilisant Maven et l'extension Java. Vous devriez voir les logs de démarrage de Spring Boot dans la Console de débogage.

### Vérification de la configuration
- Si votre application Spring Boot est une application web, ouvrez un navigateur et naviguez vers `http://localhost:8080` (ou le port spécifié dans votre fichier `application.properties` ou `application.yml`) pour confirmer qu'elle fonctionne.
- Vous pouvez également définir des points d'arrêt dans votre code et utiliser les contrôles de débogage (pause, pas à pas, etc.) pour déboguer votre application.

### Notes
- Les extensions Java dans VSCode gèrent automatiquement le classpath et le processus de build en fonction de votre `pom.xml`, donc vous n'avez généralement pas besoin d'exécuter manuellement `mvn clean install` au préalable.
- Si votre projet fait partie d'une configuration Maven multi-module, assurez-vous que `projectName` correspond à l'`artifactId` du module correct.
- Pour les configurations avancées (par exemple, les répertoires de travail personnalisés ou les tâches de pré-lancement), référez-vous à la [documentation de débogage Java de VSCode](https://code.visualstudio.com/docs/java/java-debugging).

Avec cette configuration, votre `launch.json` devrait être correctement configuré pour exécuter et déboguer votre projet Maven Spring Boot dans VSCode !