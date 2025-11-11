---
audio: false
generated: true
lang: fr
layout: post
title: Module Spring Data REST
translated: true
type: note
---

Pour utiliser **spring-data-rest-core**, vous pouvez exploiter le module Spring Data REST pour exposer vos repositories Spring Data en tant que points de terminaison RESTful dans votre application. Voici un guide complet, étape par étape, pour commencer :

---

### 1. Ajouter la dépendance Spring Data REST
Pour utiliser Spring Data REST, vous devez inclure sa dépendance dans votre projet. Si vous utilisez **Spring Boot** (un scénario courant), ajoutez la dépendance suivante à votre fichier de build :

- **Maven** :
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-data-rest</artifactId>
  </dependency>
  ```

- **Gradle** :
  ```gradle
  implementation 'org.springframework.boot:spring-boot-starter-data-rest'
  ```

Ce starter inclut `spring-data-rest-core` ainsi que d'autres composants nécessaires. Pour les projets non Spring Boot, vous pouvez inclure `spring-data-rest-core` directement, mais le starter Spring Boot est recommandé pour sa simplicité.

---

### 2. Définir vos entités
Créez votre modèle de domaine en définissant des classes d'entité à l'aide d'une technologie de persistance comme JPA (Java Persistence API). Par exemple :

```java
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.GeneratedValue;

@Entity
public class User {
    @Id
    @GeneratedValue
    private Long id;
    private String name;

    // Constructeurs
    public User() {}
    public User(String name) {
        this.name = name;
    }

    // Getters et Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

Cette entité `User` représente une table simple dans votre base de données avec un `id` et un `name`.

---

### 3. Créer les interfaces de repository
Définissez une interface de repository pour votre entité en étendant l'une des interfaces de repository de Spring Data, telle que `JpaRepository`. Par exemple :

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
```

En étendant `JpaRepository`, vous obtenez gratuitement les opérations CRUD (Create, Read, Update, Delete) de base. Spring Data REST exposera automatiquement ce repository en tant que point de terminaison RESTful.

---

### 4. Exécuter votre application
Une fois la dépendance ajoutée et vos entités et repositories définis, démarrez votre application Spring Boot. Spring Data REST générera automatiquement des points de terminaison REST basés sur votre repository. Pour le `UserRepository` ci-dessus, vous pouvez accéder à :

- **GET /users** : Récupérer une liste de tous les utilisateurs.
- **GET /users/{id}** : Récupérer un utilisateur spécifique par son ID.
- **POST /users** : Créer un nouvel utilisateur (avec un payload JSON, par exemple `{"name": "Alice"}`).
- **PUT /users/{id}** : Mettre à jour un utilisateur existant.
- **DELETE /users/{id}** : Supprimer un utilisateur.

Par exemple, si votre application s'exécute sur `localhost:8080`, vous pouvez utiliser un outil comme `curl` ou un navigateur pour tester :

```bash
curl http://localhost:8080/users
```

La réponse inclura des liens HATEOAS, permettant aux clients de naviguer dynamiquement vers les ressources associées.

---

### 5. (Optionnel) Personnaliser les points de terminaison REST
Vous pouvez personnaliser la façon dont vos repositories sont exposés en utilisant des annotations ou de la configuration :

- **Changer le chemin du point de terminaison** :
  Utilisez l'annotation `@RepositoryRestResource` pour spécifier un chemin personnalisé :
  ```java
  import org.springframework.data.rest.core.annotation.RepositoryRestResource;

  @RepositoryRestResource(path = "people")
  public interface UserRepository extends JpaRepository<User, Long> {
  }
  ```
  Désormais, le point de terminaison sera `/people` au lieu de `/users`.

- **Configurer les paramètres globaux** :
  Personnalisez le chemin de base ou d'autres paramètres en implémentant `RepositoryRestConfigurer` :
  ```java
  import org.springframework.data.rest.webmvc.config.RepositoryRestConfigurer;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.data.rest.core.config.RepositoryRestConfiguration;

  @Configuration
  public class RestConfig implements RepositoryRestConfigurer {
      @Override
      public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config) {
          config.setBasePath("/api"); // Tous les points de terminaison commenceront par /api
      }
  }
  ```
  Avec cela, vos utilisateurs seraient accessibles à l'adresse `/api/users`.

---

### Fonctionnalités clés de Spring Data REST
- **Support HATEOAS** : Les réponses incluent des liens hypermédia vers les ressources associées.
- **Pagination et Tri** : Utilisez des paramètres de requête comme `?page=0&size=10&sort=name,asc` pour paginer et trier les résultats.
- **Filtrage** : Ajoutez des méthodes de requête personnalisées à votre repository (par exemple, `findByName(String name)`) pour exposer des points de terminaison supplémentaires.

---

### Résumé
Pour utiliser `spring-data-rest-core` :
1. Incluez la dépendance Spring Data REST (par exemple, `spring-boot-starter-data-rest` pour Spring Boot).
2. Définissez vos entités avec les annotations appropriées (par exemple, `@Entity` pour JPA).
3. Créez des interfaces de repository étendant les interfaces Spring Data (par exemple, `JpaRepository`).
4. Exécutez votre application pour accéder aux points de terminaison REST générés automatiquement.
5. Optionnellement, personnalisez les chemins des points de terminaison ou le comportement selon les besoins.

Cette approche vous permet de construire rapidement une API RESTful avec un code minimal, en tirant parti de la fonctionnalité principale de Spring Data REST.