---
audio: false
generated: true
lang: fr
layout: post
title: Annotations Swagger
translated: true
---

Pour utiliser le package `swagger-annotations` dans votre projet Java, notamment pour documenter une API REST construite avec Spring Boot, suivez ces étapes. Ce guide suppose que vous utilisez Swagger 2.0, qui est couramment intégré avec la bibliothèque `springfox`. Le package `swagger-annotations` fournit des annotations pour ajouter des métadonnées à vos points de terminaison API, permettant la génération automatique de la documentation de l'API.

---

### Étape 1 : Ajouter les Dépendances Nécessaires

Vous devez inclure le package `swagger-annotations` et une bibliothèque d'intégration Swagger (par exemple, `springfox`) dans votre projet. Si vous utilisez Maven, ajoutez les dépendances suivantes à votre `pom.xml` :

```xml
<!-- Swagger Annotations -->
<dependency>
    <groupId>io.swagger</groupId>
    <artifactId>swagger-annotations</artifactId>
    <version>1.6.2</version>
</dependency>

<!-- Springfox Swagger 2 pour l'intégration Swagger -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
</dependency>

<!-- Springfox Swagger UI pour la documentation interactive -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.9.2</version>
</dependency>
```

- **`io.swagger:swagger-annotations`** : Fournit les annotations pour Swagger 2.0.
- **`springfox-swagger2`** : Intègre Swagger avec Spring Boot et traite les annotations.
- **`springfox-swagger-ui`** : Ajoute une interface web pour visualiser la documentation générée.

> **Note** : Vérifiez les dernières versions sur [Maven Repository](https://mvnrepository.com/) car ces versions (1.6.2 pour `swagger-annotations` et 2.9.2 pour `springfox`) peuvent avoir des mises à jour.

---

### Étape 2 : Configurer Swagger dans Votre Application

Pour activer Swagger et lui permettre de scanner votre API pour les annotations, créez une classe de configuration avec un bean `Docket`. Ajoutez ceci à votre application Spring Boot :

```java
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@EnableSwagger2
public class SwaggerConfig {
    @Bean
    public Docket api() {
        return new Docket(DocumentationType.SWAGGER_2)
                .select()
                .apis(RequestHandlerSelectors.any()) // Scanner tous les contrôleurs
                .paths(PathSelectors.any())          // Inclure tous les chemins
                .build();
    }
}
```

- **`@EnableSwagger2`** : Active le support Swagger 2.0.
- **`Docket`** : Configure quels points de terminaison documenter. La configuration ci-dessus scanne tous les contrôleurs et chemins, mais vous pouvez la personnaliser (par exemple, `RequestHandlerSelectors.basePackage("com.example.controllers")`) pour limiter la portée.

---

### Étape 3 : Utiliser les Annotations Swagger dans Votre Code

Le package `swagger-annotations` fournit des annotations pour décrire votre API. Appliquez-les à vos classes de contrôleur, méthodes, paramètres et modèles. Voici des annotations courantes avec des exemples :

#### Annoter un Contrôleur

Utilisez `@Api` pour décrire le contrôleur :

```java
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "User Controller", description = "Opérations concernant les utilisateurs")
@RestController
@RequestMapping("/users")
public class UserController {
    // Méthodes ici
}
```

- **`value`** : Un nom court pour l'API.
- **`description`** : Une brève explication de ce que fait le contrôleur.

#### Annoter les Opérations API

Utilisez `@ApiOperation` pour décrire les points de terminaison individuels :

```java
import io.swagger.annotations.ApiOperation;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Obtenir un utilisateur par ID", response = User.class)
@GetMapping("/{id}")
public ResponseEntity<User> getUserById(@PathVariable Long id) {
    // Implémentation
    return ResponseEntity.ok(new User(id, "John Doe"));
}
```

- **`value`** : Un résumé de l'opération.
- **`response`** : Le type de retour attendu.

#### Décrire les Paramètres

Utilisez `@ApiParam` pour les paramètres de méthode :

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@ApiOperation(value = "Créer un nouvel utilisateur")
@PostMapping
public ResponseEntity<User> createUser(
        @ApiParam(value = "Objet utilisateur à créer", required = true)
        @RequestBody User user) {
    // Implémentation
    return ResponseEntity.ok(user);
}
```

- **`value`** : Décrit le paramètre.
- **`required`** : Indique si le paramètre est obligatoire.

#### Spécifier les Réponses

Utilisez `@ApiResponses` et `@ApiResponse` pour documenter les réponses HTTP possibles :

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.ApiResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Supprimer un utilisateur")
@ApiResponses(value = {
    @ApiResponse(code = 200, message = "Utilisateur supprimé avec succès"),
    @ApiResponse(code = 404, message = "Utilisateur non trouvé")
})
@DeleteMapping("/{id}")
public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
    // Implémentation
    return ResponseEntity.ok().build();
}
```

- **`code`** : Code de statut HTTP.
- **`message`** : Description de la réponse.

#### Décrire les Modèles

Pour les objets de transfert de données (DTO), utilisez `@ApiModel` et `@ApiModelProperty` :

```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(description = "Objet de transfert de données utilisateur")
public class User {
    @ApiModelProperty(notes = "L'identifiant unique de l'utilisateur", example = "1")
    private Long id;

    @ApiModelProperty(notes = "Le nom de l'utilisateur", example = "John Doe")
    private String name;

    // Getters et setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public User(Long id, String name) {
        this.id = id;
        this.name = name;
    }
}
```

- **`@ApiModel`** : Décrit le modèle.
- **`@ApiModelProperty`** : Détaille chaque champ, avec des exemples optionnels.

---

### Étape 4 : Exécuter et Accéder à la Documentation

1. Démarrez votre application Spring Boot.
2. Ouvrez un navigateur et accédez à :
   **http://localhost:8080/swagger-ui.html**
   Cette URL affiche l'interface utilisateur Swagger, une interface interactive montrant la documentation de votre API basée sur les annotations.

---

### Résumé de l'utilisation de `swagger-annotations`

1. **Ajouter des Dépendances** : Incluez `swagger-annotations` et `springfox` dans votre `pom.xml`.
2. **Configurer Swagger** : Configurez un bean `Docket` pour activer le scan Swagger.
3. **Annoter Votre Code** :
   - `@Api` pour les contrôleurs.
   - `@ApiOperation` pour les méthodes.
   - `@ApiParam` pour les paramètres.
   - `@ApiResponses` et `@ApiResponse` pour les détails de réponse.
   - `@ApiModel` et `@ApiModelProperty` pour les DTO.
4. **Voir la Documentation** : Accédez à l'interface utilisateur Swagger à `/swagger-ui.html`.

---

### Notes Supplémentaires

- **Swagger 2.0 vs. OpenAPI 3.0** : Ce guide utilise Swagger 2.0 avec `io.swagger:swagger-annotations`. Pour OpenAPI 3.0, utilisez `io.swagger.core.v3:swagger-annotations` et une bibliothèque comme `springdoc-openapi`, ce qui change certains noms d'annotations (par exemple, `@Tag` au lieu de `@Api`).
- **Personnalisation** : Ajustez la configuration `Docket` pour filtrer des packages ou des chemins spécifiques pour une documentation plus ciblée.
- **Qualité** : Fournissez des descriptions claires et détaillées dans les annotations pour améliorer l'utilité de la documentation générée.

En suivant ces étapes, vous pouvez utiliser efficacement le package `swagger-annotations` pour documenter votre API REST, rendant ainsi plus facile pour les développeurs et les consommateurs de comprendre et d'interagir avec vos points de terminaison.