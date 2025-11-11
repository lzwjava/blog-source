---
audio: false
generated: true
lang: fr
layout: post
title: API Java pour les services Web RESTful
translated: true
type: note
---

Pour utiliser `javax.ws.rs`, l'API Java pour les services web RESTful (communément appelée JAX-RS), vous devez suivre une série d'étapes pour configurer votre projet, définir les ressources RESTful, configurer votre application et la déployer. JAX-RS vous permet de créer des services web qui adhèrent au style architectural REST, en utilisant des annotations pour définir les points de terminaison et gérer les requêtes HTTP. Voici un guide complet pour commencer :

---

### **1. Configurer votre projet**
Pour utiliser `javax.ws.rs`, vous devez inclure l'API JAX-RS et une implémentation (puisque `javax.ws.rs` est une spécification, pas un runtime). Une implémentation populaire est Jersey. Si vous utilisez Maven, ajoutez les dépendances nécessaires à votre `pom.xml` :

#### **Dépendances**
```xml
<!-- API JAX-RS -->
<dependency>
    <groupId>javax.ws.rs</groupId>
    <artifactId>javax.ws.rs-api</artifactId>
    <version>2.1.1</version>
</dependency>

<!-- Implémentation Jersey (inclut les dépendances principales) -->
<dependency>
    <groupId>org.glassfish.jersey.bundles</groupId>
    <artifactId>jaxrs-ri</artifactId>
    <version>2.34</version>
</dependency>

<!-- Optionnel : Support JSON avec Jackson -->
<dependency>
    <groupId>org.glassfish.jersey.media</groupId>
    <artifactId>jersey-media-json-jackson</artifactId>
    <version>2.34</version>
</dependency>
```

- Le `javax.ws.rs-api` fournit les annotations et classes principales de JAX-RS.
- Le bundle `jaxrs-ri` inclut l'implémentation Jersey et ses dépendances.
- Le module `jersey-media-json-jackson` (optionnel) ajoute le support de la sérialisation/désérialisation JSON.

Assurez-vous que votre projet est configuré avec un conteneur de servlets (par exemple, Tomcat) ou un serveur Java EE, car les applications JAX-RS s'exécutent généralement dans de tels environnements. Alternativement, vous pouvez l'exécuter en mode autonome avec un serveur léger comme Grizzly (plus de détails plus tard).

---

### **2. Créer une ressource RESTful**
Les services RESTful dans JAX-RS sont définis à l'aide de classes de ressources annotées avec `@Path` et des annotations de méthodes HTTP comme `@GET`, `@POST`, etc. Voici un exemple d'une ressource simple :

#### **Exemple : HelloResource.java**
```java
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/hello")
public class HelloResource {

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String sayHello() {
        return "Hello, World!";
    }
}
```

- **`@Path("/hello")`** : Spécifie le chemin URI pour cette ressource (par exemple, `http://localhost:8080/api/hello`).
- **`@GET`** : Indique que cette méthode gère les requêtes HTTP GET.
- **`@Produces(MediaType.TEXT_PLAIN)`** : Spécifie que la réponse sera en texte brut.

Lorsqu'une requête GET est faite vers `/hello`, cette méthode retourne `"Hello, World!"`.

---

### **3. Configurer l'application JAX-RS**
Vous devez indiquer au runtime JAX-RS quelles ressources inclure. Cela peut être fait en créant une classe de configuration d'application qui étend `javax.ws.rs.core.Application`.

#### **Exemple : MyApplication.java**
```java
import javax.ws.rs.ApplicationPath;
import javax.ws.rs.core.Application;
import java.util.HashSet;
import java.util.Set;

@ApplicationPath("/api")
public class MyApplication extends Application {

    @Override
    public Set<Class<?>> getClasses() {
        Set<Class<?>> classes = new HashSet<>();
        classes.add(HelloResource.class);
        return classes;
    }
}
```

- **`@ApplicationPath("/api")`** : Définit le chemin URI de base pour toutes les ressources (par exemple, `/api/hello`).
- **`getClasses()`** : Retourne l'ensemble des classes de ressources à inclure dans l'application.

Avec les conteneurs de servlets modernes (Servlet 3.0+), cette configuration basée sur les annotations est souvent suffisante, et vous n'aurez peut-être pas besoin d'un fichier `web.xml`.

---

### **4. Gérer les différentes méthodes HTTP et paramètres**
JAX-RS fournit des annotations pour gérer diverses méthodes HTTP, types de média et paramètres.

#### **Exemple : Gestion des requêtes POST**
```java
import javax.ws.rs.POST;
import javax.ws.rs.Consumes;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@POST
@Consumes(MediaType.APPLICATION_JSON)
public Response createItem(MyItem item) {
    // Logique pour traiter l'item
    return Response.status(Response.Status.CREATED).build();
}
```

- **`@POST`** : Gère les requêtes HTTP POST.
- **`@Consumes(MediaType.APPLICATION_JSON)`** : S'attend à une entrée JSON, qui est désérialisée en un objet `MyItem`.
- **`Response`** : Retourne un statut 201 Created.

#### **Exemple : Paramètres de chemin**
```java
import javax.ws.rs.PathParam;
import javax.ws.rs.Path;

@GET
@Path("/{id}")
@Produces(MediaType.APPLICATION_JSON)
public MyItem getItem(@PathParam("id") String id) {
    // Logique pour récupérer l'item par ID
    return new MyItem(id);
}
```

- **`@Path("/{id}")`** : Définit un paramètre de chemin (par exemple, `/hello/123`).
- **`@PathParam("id")`** : Injecte la valeur `id` de l'URI.

#### **Exemple : Paramètres de requête**
```java
import javax.ws.rs.QueryParam;

@GET
@Produces(MediaType.APPLICATION_JSON)
public List<MyItem> getItems(@QueryParam("category") String category) {
    // Logique pour filtrer les items par catégorie
    return itemList;
}
```

- **`@QueryParam("category")`** : Récupère la valeur `category` de la chaîne de requête (par exemple, `/hello?category=books`).

---

### **5. Déployer l'application**
Vous pouvez déployer votre application JAX-RS dans un conteneur de servlets comme Tomcat :

1. Packagez votre projet en tant que fichier WAR (par exemple, en utilisant `mvn package`).
2. Déployez le fichier WAR dans votre conteneur.
3. Accédez à votre service à l'URI configurée (par exemple, `http://localhost:8080/your-app/api/hello`).

Alternativement, pour le développement ou une utilisation autonome, vous pouvez exécuter l'application de manière programmatique en utilisant Jersey avec Grizzly :

#### **Exemple : Main autonome**
```java
import org.glassfish.jersey.grizzly2.httpserver.GrizzlyHttpServerFactory;
import org.glassfish.jersey.server.ResourceConfig;
import java.net.URI;

public class Main {
    public static void main(String[] args) {
        URI baseUri = URI.create("http://localhost:8080/api/");
        ResourceConfig config = new ResourceConfig(HelloResource.class);
        GrizzlyHttpServerFactory.createHttpServer(baseUri, config);
        System.out.println("Server running at " + baseUri);
    }
}
```

Cela démarre un serveur HTTP sans conteneur de servlets complet.

---

### **6. Fonctionnalités supplémentaires**
- **Gestion des exceptions** : Utilisez `ExceptionMapper` pour gérer les exceptions de manière élégante.
  ```java
  import javax.ws.rs.NotFoundException;
  import javax.ws.rs.core.Response;
  import javax.ws.rs.ext.ExceptionMapper;
  import javax.ws.rs.ext.Provider;

  @Provider
  public class NotFoundExceptionMapper implements ExceptionMapper<NotFoundException> {
      @Override
      public Response toResponse(NotFoundException exception) {
          return Response.status(Response.Status.NOT_FOUND).build();
      }
  }
  ```
- **Injection de dépendances** : Utilisez `@Context` pour injecter des objets comme `UriInfo` ou utilisez le framework d'injection de dépendances de l'implémentation (par exemple, HK2 dans Jersey).
- **Tests** : Utilisez des outils comme Postman ou le Jersey Test Framework pour tester vos points de terminaison.

---

### **Résumé**
Pour utiliser `javax.ws.rs`, incluez l'API JAX-RS et une implémentation comme Jersey dans votre projet, définissez des classes de ressources avec des annotations pour les chemins et les méthodes HTTP, configurez l'application (via une sous-classe `Application` ou `web.xml`), et déployez-la dans un conteneur de servlets ou exécutez-la en mode autonome. Cela vous permet de construire efficacement des services web RESTful avec Java.