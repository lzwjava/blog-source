---
audio: false
generated: true
lang: fr
layout: post
title: 'Démarrage avec JShell : Un guide rapide'
translated: true
type: note
---

JShell est un outil interactif REPL (Read-Eval-Print Loop) inclus dans le Java Development Kit (JDK) à partir de JDK 9. Il vous permet d'exécuter des extraits de code Java de manière interactive sans avoir à écrire un programme complet. Voici un guide concis sur l'utilisation de JShell :

### 1. **Démarrer JShell**
- **Vérifier l'installation du JDK** : Assurez-vous d'avoir JDK 9 ou une version ultérieure installé. Vous pouvez vérifier en exécutant `java -version` dans votre terminal ou invite de commande.
- **Lancer JShell** :
  - Ouvrez un terminal ou une invite de commande.
  - Tapez `jshell` et appuyez sur Entrée.
  - Vous verrez une invite comme `jshell>` indiquant que JShell est prêt.

### 2. **Utilisation de base**
- **Exécuter du code Java** :
  - Tapez des expressions, des instructions ou des déclarations Java directement à l'invite.
  - Exemple :
    ```java
    jshell> System.out.println("Hello, JShell!")
    Hello, JShell!
    ```
  - JShell évalue la saisie et affiche le résultat immédiatement.

- **Variables et expressions** :
  - Déclarez des variables ou évaluez des expressions :
    ```java
    jshell> int x = 10
    x ==> 10
    jshell> x * 2
    $2 ==> 20
    ```
  - JShell attribue automatiquement des noms temporaires (par exemple, `$2`) aux résultats d'expressions.

- **Définir des méthodes et des classes** :
  - Vous pouvez définir des méthodes ou des classes :
    ```java
    jshell> void sayHello() { System.out.println("Hello!"); }
    |  created method sayHello()
    jshell> sayHello()
    Hello!
    ```
    ```java
    jshell> class Test { int x = 5; }
    |  created class Test
    jshell> Test t = new Test()
    t ==> Test@7c417213
    jshell> t.x
    $5 ==> 5
    ```

### 3. **Commandes principales**
JShell fournit des commandes intégrées commençant par `/`. Voici quelques commandes essentielles :
- **Lister tout le code** : `/list` – Affiche tous les extraits saisis dans la session.
  ```java
  jshell> /list
  ```
- **Modifier le code** : `/edit <id>` – Ouvre un éditeur graphique pour l'extrait avec l'ID donné (provenant de `/list`).
- **Sauvegarder la session** : `/save myfile.java` – Sauvegarde tous les extraits dans un fichier.
- **Charger un fichier** : `/open myfile.java` – Charge et exécute le code d'un fichier.
- **Voir les variables** : `/vars` – Liste toutes les variables déclarées.
  ```java
  jshell> /vars
  |    int x = 10
  ```
- **Voir les méthodes** : `/methods` – Liste toutes les méthodes définies.
- **Quitter JShell** : `/exit` – Ferme la session JShell.
- **Aide** : `/help` – Affiche toutes les commandes disponibles.

### 4. **Importer des packages**
- JShell importe automatiquement les packages courants (par exemple, `java.util`, `java.io`). Pour en utiliser d'autres, importez-les manuellement :
  ```java
  jshell> import java.time.LocalDate
  jshell> LocalDate.now()
  $3 ==> 2025-06-27
  ```

### 5. **Modifier et corriger le code**
- **Modifier le code existant** :
  - Utilisez `/list` pour trouver l'ID d'un extrait.
  - Redéfinissez-le en tapant une nouvelle version. JShell écrase l'ancienne définition.
    ```java
    jshell> int x = 5
    x ==> 5
    jshell> int x = 10
    x ==> 10
    ```
- **Supprimer un extrait** : `/drop <id>` – Supprime un extrait spécifique par son ID.

### 6. **Complétion par tabulation**
- Appuyez sur `Tab` pour auto-compléter les noms de classes, de méthodes ou de commandes.
- Exemple :
  ```java
  jshell> System.out.pr<tab>
  ```
  Cela suggère `println`, `print`, etc.

### 7. **Exécuter des scripts externes**
- Chargez et exécutez un fichier Java :
  ```java
  jshell> /open MyScript.java
  ```
- Vous pouvez également démarrer JShell avec un script :
  ```bash
  jshell MyScript.java
  ```

### 8. **Personnaliser JShell**
- **Scripts de démarrage** : Créez un fichier (par exemple, `startup.jsh`) avec des imports ou du code commun, puis chargez-le avec `/open startup.jsh` ou définissez-le comme script de démarrage par défaut :
  ```bash
  jshell --start startup.jsh
  ```
- **Modes de feedback** : Ajustez la verbosité de la sortie avec `/set feedback <mode>` (par exemple, `normal`, `concise`, `verbose`).

### 9. **Conseils**
- **Prototypage rapide** : Utilisez JShell pour tester de petits extraits de code, expérimenter avec des APIs ou apprendre la syntaxe Java.
- **Gestion des erreurs** : JShell fournit des messages d'erreur clairs et vous permet de corriger les erreurs à la volée.
- **Saisie multi-lignes** : Pour du code complexe, JShell prend en charge l'édition multi-lignes. Terminez une ligne par un backslash (`\`) pour continuer :
  ```java
  jshell> int sum(int a, int b) { \
      ...> return a + b; \
      ...> }
  ```

### 10. **Dépannage**
- **JShell introuvable** : Assurez-vous que le répertoire `bin` du JDK est dans le PATH de votre système.
- **Démarrage lent** : Sur certains systèmes, JShell peut prendre un moment pour s'initialiser. Assurez-vous que votre JDK est à jour.
- **Réinitialiser la session** : Utilisez `/reset` pour effacer tous les extraits et recommencer à zéro.

Pour plus de détails, consultez la documentation officielle du JDK ou exécutez `/help` dans JShell. Si vous avez des tâches spécifiques ou du code que vous souhaitez essayer dans JShell, faites-le moi savoir et je pourrai vous guider davantage !