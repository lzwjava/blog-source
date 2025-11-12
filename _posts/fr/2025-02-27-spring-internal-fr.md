---
audio: false
generated: true
lang: fr
layout: post
title: Fonctionnement Interne de Spring
translated: true
type: note
---

Plongeons dans Spring et son fonctionnement interne. Spring est un framework robuste pour construire des applications Java, et je vais aborder chaque partie de votre requête étape par étape avec des explications claires.

### Comment fonctionne Spring ?
Spring opère sur le principe de **l'Inversion de Contrôle (IoC)**. Cela signifie qu'au lieu que votre code d'application contrôle la création et la gestion des objets, Spring en prend la charge. Il le fait grâce à un composant appelé **le conteneur IoC**. Le conteneur IoC est responsable de :

- **Instancier** les objets (appelés beans dans Spring).
- **Les configurer** selon vos spécifications.
- **Les assembler** en gérant leurs dépendances.

Cette approche réduit le couplage fort dans votre code, le rendant plus modulaire et plus facile à maintenir.

### Comment Spring gère-t-il les Beans ?
Dans Spring, les **beans** sont les objets gérés par le conteneur IoC. Voici comment Spring les traite :

1. **Définition** : Vous définissez les beans soit dans :
   - **Des fichiers de configuration XML**.
   - **Une configuration basée sur Java** en utilisant des annotations comme `@Bean`, `@Component`, `@Service`, etc.
2. **Création** : Lorsque l'application démarre, le conteneur IoC lit ces définitions et crée les beans.
3. **Injection de Dépendances (DI)** : Spring injecte automatiquement les dépendances (d'autres beans) dans un bean là où c'est nécessaire, en utilisant :
   - **L'injection par constructeur**.
   - **L'injection par setter**.
   - **L'injection par champ** (via `@Autowired`).

Le conteneur gère l'intégralité du cycle de vie de ces beans—de la création à la destruction—et s'assure qu'ils sont disponibles quand c'est nécessaire.

### Différence entre un Service et un Controller
Dans le contexte de **Spring MVC** (le framework web de Spring), ces deux composants ont des objectifs distincts :

- **Controller** :
  - Gère les **requêtes HTTP** des utilisateurs.
  - Traite les entrées, invoque la logique métier et décide quelle **vue** (par exemple, une page web) renvoyer.
  - Annoté avec `@Controller` ou `@RestController`.
  - Réside dans la **couche web**.

- **Service** :
  - Encapsule la **logique métier** de l'application.
  - Exécute des tâches comme des calculs, le traitement de données ou l'interaction avec les bases de données.
  - Annoté avec `@Service`.
  - Réside dans la **couche métier**.

**Exemple** :
- Un controller peut recevoir une requête pour afficher le profil d'un utilisateur et appeler un service pour récupérer les données de l'utilisateur.
- Le service récupère les données depuis une base de données et les renvoie au controller, qui les envoie ensuite à la vue.

En bref : **Les controllers gèrent les interactions web**, tandis que **les services gèrent la fonctionnalité principale**.

### Qu'est-ce que Spring fournit ?
Spring est un framework complet offrant une large gamme d'outils pour les applications d'entreprise. Les fonctionnalités clés incluent :

- **L'Injection de Dépendances** : Simplifie la gestion des dépendances entre objets.
- **La Programmation Orientée Aspect (AOP)** : Ajoute des préoccupations transversales comme la journalisation ou la sécurité.
- **La Gestion des Transactions** : Garantit la cohérence des données à travers les opérations.
- **Spring MVC** : Construit des applications web robustes.
- **Spring Boot** : Simplifie la configuration avec des paramètres par défaut préconfigurés et des serveurs embarqués.
- **Spring Data** : Rationalise l'accès aux bases de données.
- **Sécurité** : Fournit des outils d'authentification et d'autorisation.

La conception modulaire de Spring vous permet de ne choisir que les fonctionnalités dont vous avez besoin.

### Comment Spring recherche-t-il les objets ou les Beans ?
Lorsqu'une application Spring démarre :

1. Le **conteneur IoC** s'initialise.
2. Il scanne à la recherche des **définitions de beans** dans :
   - Les fichiers XML.
   - Les classes annotées (par exemple, `@Component`, `@Bean`).
3. Le conteneur crée les beans et les stocke dans une **map**, indexée par nom ou par type.
4. Lorsqu'un bean est nécessaire (par exemple, pour une injection ou une récupération directe), le conteneur le fournit en utilisant :
   - **La recherche par nom**.
   - **La recherche par type** (par exemple, via `@Autowired`).

Ce processus garantit que les beans sont facilement disponibles dans toute l'application.

### Comment utiliser Tomcat ou Netty comme serveur ?
Spring Boot, une extension de Spring, simplifie la configuration du serveur en embarquant directement les serveurs dans votre application. Voici comment cela fonctionne avec **Tomcat** et **Netty** :

- **Tomcat** (Basé sur Servlet) :
  - Serveur par défaut dans la dépendance `spring-boot-starter-web` de Spring Boot.
  - Ajoutez ceci à votre `pom.xml` :
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    ```
  - Spring Boot embarque Tomcat, et votre application s'exécute comme un JAR exécutable autonome.

- **Netty** (Non basé sur Servlet) :
  - Utilisé pour les applications web réactives (par exemple, avec Spring WebFlux).
  - Remplacez Tomcat en l'excluant et en ajoutant Netty :
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-webflux</artifactId>
    </dependency>
    ```
  - Spring Boot embarque Netty à la place, supportant les E/S asynchrones et non bloquantes.

Vous configurez le serveur via `application.properties` (par exemple, en définissant le port avec `server.port=8080`). Aucun déploiement de serveur externe n'est nécessaire—Spring Boot gère tout.

### Résumé
- **Le Cœur de Spring** : Utilise un conteneur IoC pour la gestion des objets.
- **Gestion des Beans** : Définis via XML ou annotations, avec les dépendances injectées automatiquement.
- **Service vs. Controller** : Les services gèrent la logique métier ; les controllers gèrent les requêtes web.
- **Fonctionnalités** : Offre DI, AOP, le support web, et plus encore.
- **Recherche de Beans** : Le conteneur trouve et fournit les beans à partir des configurations.
- **Serveurs** : Spring Boot embarque Tomcat ou Netty avec de simples changements de dépendances.