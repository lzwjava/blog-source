---
audio: false
generated: true
lang: fr
layout: post
title: Fonctionnement interne du printemps
translated: true
---

Plongeons dans Spring et son fonctionnement interne. Spring est un framework robuste pour la construction d'applications Java, et j'aborderai chaque partie de votre requête étape par étape avec des explications claires.

### Comment fonctionne Spring ?
Spring fonctionne sur le principe de **l'Inversion de Contrôle (IoC)**. Cela signifie que, au lieu que votre code d'application contrôle la création et la gestion des objets, Spring prend en charge cette tâche. Il le fait grâce à un composant appelé le **conteneur IoC**. Le conteneur IoC est responsable de :

- **l'instantiation** des objets (appelés beans dans Spring).
- **leur configuration** en fonction de vos spécifications.
- **leur assemblage** en gérant leurs dépendances.

Cette approche réduit le couplage étroit dans votre code, le rendant plus modulaire et plus facile à maintenir.

### Comment Spring gère-t-il les beans ?
Dans Spring, les **beans** sont les objets gérés par le conteneur IoC. Voici comment Spring les gère :

1. **Définition** : Vous définissez les beans soit dans :
   - **des fichiers de configuration XML**.
   - **une configuration basée sur Java** en utilisant des annotations comme `@Bean`, `@Component`, `@Service`, etc.
2. **Création** : Lorsque l'application démarre, le conteneur IoC lit ces définitions et crée les beans.
3. **Injection de Dépendances (DI)** : Spring injecte automatiquement les dépendances (autres beans) dans un bean où cela est nécessaire, en utilisant :
   - **l'injection par constructeur**.
   - **l'injection par setter**.
   - **l'injection par champ** (via `@Autowired`).

Le conteneur gère l'ensemble du cycle de vie de ces beans, de leur création à leur destruction, et s'assure qu'ils sont disponibles lorsque nécessaire.

### Différence entre un Service et un Controller
Dans le contexte de **Spring MVC** (le framework web de Spring), ces deux composants servent des objectifs distincts :

- **Controller** :
  - Gère les **requêtes HTTP** des utilisateurs.
  - Traite les entrées, invoque la logique métier et décide quelle **vue** (par exemple, une page web) retourner.
  - Annoté avec `@Controller` ou `@RestController`.
  - Vit dans la **couche web**.

- **Service** :
  - Encapsule la **logique métier** de l'application.
  - Effectue des tâches comme des calculs, le traitement de données ou l'interaction avec des bases de données.
  - Annoté avec `@Service`.
  - Vit dans la **couche métier**.

**Exemple** :
- Un contrôleur pourrait recevoir une requête pour afficher le profil d'un utilisateur et appeler un service pour récupérer les données de l'utilisateur.
- Le service récupère les données dans une base de données et les retourne au contrôleur, qui les envoie ensuite à la vue.

En résumé : **les contrôleurs gèrent les interactions web**, tandis que **les services gèrent la fonctionnalité principale**.

### Que fournit Spring ?
Spring est un framework complet offrant une large gamme d'outils pour les applications d'entreprise. Les fonctionnalités clés incluent :

- **Injection de Dépendances** : Simplifie la gestion des dépendances d'objets.
- **Programmation Orientée Aspect (AOP)** : Ajoute des préoccupations transversales comme la journalisation ou la sécurité.
- **Gestion des Transactions** : Assure la cohérence des données à travers les opérations.
- **Spring MVC** : Construit des applications web robustes.
- **Spring Boot** : Simplifie la configuration avec des valeurs par défaut préconfigurées et des serveurs intégrés.
- **Spring Data** : Simplifie l'accès aux bases de données.
- **Sécurité** : Fournit des outils d'authentification et d'autorisation.

La conception modulaire de Spring vous permet de choisir uniquement les fonctionnalités dont vous avez besoin.

### Comment Spring recherche-t-il des objets ou des beans ?
Lorsqu'une application Spring démarre :

1. Le **conteneur IoC** s'initialise.
2. Il recherche des **définitions de beans** dans :
   - Des fichiers XML.
   - Des classes annotées (par exemple, `@Component`, `@Bean`).
3. Le conteneur crée les beans et les stocke dans une **map**, indexée par nom ou type.
4. Lorsque un bean est nécessaire (par exemple, pour une injection ou une récupération directe), le conteneur le fournit en utilisant :
   - **recherche par nom**.
   - **recherche par type** (par exemple, via `@Autowired`).

Ce processus garantit que les beans sont facilement disponibles dans toute l'application.

### Comment utiliser Tomcat ou Netty comme serveur ?
Spring Boot, une extension de Spring, simplifie la configuration du serveur en intégrant directement des serveurs dans votre application. Voici comment cela fonctionne avec **Tomcat** et **Netty** :

- **Tomcat** (basé sur Servlet) :
  - Serveur par défaut dans la dépendance `spring-boot-starter-web` de Spring Boot.
  - Ajoutez ceci à votre `pom.xml` :
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    ```
  - Spring Boot intègre Tomcat, et votre application s'exécute comme un exécutable JAR autonome.

- **Netty** (non basé sur Servlet) :
  - Utilisé pour les applications web réactives (par exemple, avec Spring WebFlux).
  - Remplacez Tomcat en l'excluant et en ajoutant Netty :
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-webflux</artifactId>
    </dependency>
    ```
  - Spring Boot intègre Netty à la place, supportant les E/S asynchrones et non bloquantes.

Vous configurez le serveur via `application.properties` (par exemple, en définissant le port avec `server.port=8080`). Aucune installation de serveur externe n'est nécessaire—Spring Boot s'en charge.

### Résumé
- **Noyau de Spring** : Utilise un conteneur IoC pour la gestion des objets.
- **Gestion des Beans** : Définis via XML ou annotations, avec des dépendances injectées automatiquement.
- **Service vs. Controller** : Les services gèrent la logique métier ; les contrôleurs gèrent les requêtes web.
- **Fonctionnalités** : Offre DI, AOP, support web, et plus encore.
- **Recherche de Beans** : Le conteneur trouve et fournit des beans à partir des configurations.
- **Serveurs** : Spring Boot intègre Tomcat ou Netty avec des changements de dépendances simples.