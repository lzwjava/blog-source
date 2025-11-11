---
audio: false
generated: true
lang: fr
layout: post
title: Comment utiliser Spring Boot CLI
translated: true
type: note
---

Spring Boot CLI (Command Line Interface) est un outil puissant qui vous permet de développer, tester et prototyper rapidement des applications Spring Boot directement depuis la ligne de commande. Il est particulièrement utile pour exécuter des scripts Groovy sans configurer une structure de projet complète, générer de nouveaux projets ou expérimenter avec les fonctionnalités de Spring Boot. Voici un guide complet sur la façon d'installer et d'utiliser efficacement Spring Boot CLI.

---

## Installation
Avant de pouvoir utiliser Spring Boot CLI, vous devez l'installer. Il existe deux méthodes principales selon votre système d'exploitation :

### 1. Utilisation de SDKMAN ! (Recommandé pour les systèmes de type Unix comme Linux ou macOS)
SDKMAN ! est un outil de gestion de kits de développement logiciel, ce qui facilite l'installation de Spring Boot CLI.

- **Étape 1 : Installer SDKMAN !**
  Ouvrez votre terminal et exécutez :
  ```bash
  curl -s "https://get.sdkman.io" | bash
  ```
  Suivez les invites pour initialiser SDKMAN ! en sourçant le script :
  ```bash
  source "$HOME/.sdkman/bin/sdkman-init.sh"
  ```

- **Étape 2 : Installer Spring Boot CLI**
  Exécutez la commande suivante :
  ```bash
  sdk install springboot
  ```

### 2. Installation manuelle (Pour Windows ou configuration manuelle)
Si vous êtes sous Windows ou préférez une installation manuelle :
- Téléchargez le fichier ZIP de Spring Boot CLI depuis le [site web officiel de Spring](https://spring.io/projects/spring-boot).
- Extrayez le fichier ZIP dans un répertoire de votre choix.
- Ajoutez le répertoire `bin` du dossier extrait à la variable d'environnement PATH de votre système.

### Vérifier l'installation
Pour confirmer que Spring Boot CLI est installé correctement, exécutez cette commande dans votre terminal :
```bash
spring --version
```
Vous devriez voir la version installée de Spring Boot CLI (par exemple, `Spring CLI v3.3.0`). Si cela fonctionne, vous êtes prêt à l'utiliser !

---

## Principales façons d'utiliser Spring Boot CLI
Spring Boot CLI offre plusieurs fonctionnalités qui le rendent idéal pour le développement rapide et le prototypage. Voici les principales façons de l'utiliser :

### 1. Exécution de scripts Groovy
L'une des fonctionnalités marquantes de Spring Boot CLI est sa capacité à exécuter directement des scripts Groovy sans nécessiter une configuration de projet complète. C'est parfait pour le prototypage rapide ou l'expérimentation avec Spring Boot.

- **Exemple : Créer une application web simple**
  Créez un fichier nommé `hello.groovy` avec le contenu suivant :
  ```groovy
  @RestController
  class HelloController {
      @RequestMapping("/")
      String home() {
          "Hello, World!"
      }
  }
  ```

- **Exécuter le script**
  Dans votre terminal, naviguez vers le répertoire contenant `hello.groovy` et exécutez :
  ```bash
  spring run hello.groovy
  ```
  Cela démarre un serveur web sur le port 8080. Ouvrez un navigateur et visitez `http://localhost:8080` pour voir "Hello, World !" affiché.

- **Ajouter des dépendances**
  Vous pouvez inclure des dépendances directement dans le script en utilisant l'annotation `@Grab`. Par exemple :
  ```groovy
  @Grab('org.springframework.boot:spring-boot-starter-data-jpa')
  @RestController
  class HelloController {
      @RequestMapping("/")
      String home() {
          "Hello, World!"
      }
  }
  ```
  Cela ajoute Spring Data JPA à votre script sans avoir besoin d'un fichier de build.

- **Exécuter plusieurs scripts**
  Pour exécuter tous les scripts Groovy du répertoire courant, utilisez :
  ```bash
  spring run *.groovy
  ```

### 2. Création de nouveaux projets Spring Boot
Spring Boot CLI peut générer une nouvelle structure de projet avec les dépendances de votre choix, vous faisant gagner du temps lors du démarrage d'une application complète.

- **Exemple : Générer un projet**
  Exécutez cette commande pour créer un nouveau projet avec les dépendances web et data-jpa :
  ```bash
  spring init --dependencies=web,data-jpa my-project
  ```
  Cela crée un répertoire appelé `my-project` contenant une application Spring Boot configurée avec Spring Web et Spring Data JPA.

- **Options de personnalisation**
  Vous pouvez spécifier des options supplémentaires comme :
  - Outil de build : `--build=maven` ou `--build=gradle`
  - Langage : `--language=java`, `--language=groovy` ou `--language=kotlin`
  - Packaging : `--packaging=jar` ou `--packaging=war`

  Par exemple :
  ```bash
  spring init --dependencies=web --build=gradle --language=kotlin my-kotlin-project
  ```

### 3. Empaquetage d'applications
Spring Boot CLI vous permet de packager vos scripts dans des fichiers JAR ou WAR exécutables pour le déploiement.

- **Créer un fichier JAR**
  ```bash
  spring jar my-app.jar *.groovy
  ```
  Cela empaquette tous les scripts Groovy du répertoire courant dans `my-app.jar`.

- **Créer un fichier WAR**
  ```bash
  spring war my-app.war *.groovy
  ```
  Cela génère un fichier `my-app.war` adapté au déploiement sur un conteneur de servlets.

### 4. Exécution de tests
Si vous avez des scripts de test Groovy, vous pouvez les exécuter avec :
```bash
spring test *.groovy
```
Cela exécute tous les scripts de test du répertoire courant.

### 5. Utilisation du shell interactif
Pour une expérience interactive, lancez le shell Spring Boot CLI :
```bash
spring shell
```
À l'intérieur du shell, vous pouvez exécuter des commandes comme `run`, `grab` ou `jar` de manière interactive, ce qui est excellent pour l'expérimentation.

---

## Résumé
Spring Boot CLI est un outil excellent pour les développeurs qui souhaitent travailler avec Spring Boot rapidement et efficacement depuis la ligne de commande. Voici comment l'utiliser en bref :

1. **Installez-le** en utilisant SDKMAN ! (`sdk install springboot`) ou manuellement en téléchargeant le ZIP et en mettant à jour votre PATH.
2. **Exécutez des scripts Groovy** avec `spring run <script.groovy>` pour un prototypage rapide.
3. **Créez de nouveaux projets** avec `spring init --dependencies=<deps> <project-name>`.
4. **Packagez les applications** en fichiers JAR ou WAR en utilisant `spring jar` ou `spring war`.
5. **Expérimentez de manière interactive** avec `spring shell`.

Que vous prototypiez une idée, appreniez Spring Boot ou automatisiez des tâches, Spring Boot CLI offre une manière légère et flexible de commencer sans la surcharge d'un IDE complet ou d'une configuration de projet.