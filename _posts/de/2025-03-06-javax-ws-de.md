---
audio: false
generated: true
lang: de
layout: post
title: Java-API für RESTful-Webdienste
translated: true
type: note
---

Um `javax.ws.rs`, die Java API für RESTful-Webdienste (häufig als JAX-RS bezeichnet), zu verwenden, müssen Sie eine Reihe von Schritten befolgen, um Ihr Projekt einzurichten, RESTful-Ressourcen zu definieren, Ihre Anwendung zu konfigurieren und sie bereitzustellen. JAX-RS ermöglicht es Ihnen, Webdienste zu erstellen, die dem REST-Architekturstil entsprechen, und verwendet Annotationen, um Endpunkte zu definieren und HTTP-Anfragen zu verarbeiten. Im Folgenden finden Sie eine umfassende Anleitung für den Einstieg:

---

### **1. Richten Sie Ihr Projekt ein**
Um `javax.ws.rs` zu verwenden, müssen Sie die JAX-RS-API und eine Implementierung einbinden (da `javax.ws.rs` eine Spezifikation und keine Laufzeitumgebung ist). Eine beliebte Implementierung ist Jersey. Wenn Sie Maven verwenden, fügen Sie die erforderlichen Abhängigkeiten zu Ihrer `pom.xml` hinzu:

#### **Abhängigkeiten**
```xml
<!-- JAX-RS API -->
<dependency>
    <groupId>javax.ws.rs</groupId>
    <artifactId>javax.ws.rs-api</artifactId>
    <version>2.1.1</version>
</dependency>

<!-- Jersey Implementation (includes core dependencies) -->
<dependency>
    <groupId>org.glassfish.jersey.bundles</groupId>
    <artifactId>jaxrs-ri</artifactId>
    <version>2.34</version>
</dependency>

<!-- Optional: JSON support with Jackson -->
<dependency>
    <groupId>org.glassfish.jersey.media</groupId>
    <artifactId>jersey-media-json-jackson</artifactId>
    <version>2.34</version>
</dependency>
```

- Die `javax.ws.rs-api` stellt die Kern-JAX-RS-Annotationen und -Klassen bereit.
- Das `jaxrs-ri`-Bundle enthält die Jersey-Implementierung und ihre Abhängigkeiten.
- Das Modul `jersey-media-json-jackson` (optional) fügt Unterstützung für JSON-Serialisierung/Deserialisierung hinzu.

Stellen Sie sicher, dass Ihr Projekt mit einem Servlet-Container (z.B. Tomcat) oder einem Java-EE-Server eingerichtet ist, da JAX-RS-Anwendungen typischerweise in solchen Umgebungen laufen. Alternativ können Sie sie auch eigenständig mit einem leichtgewichtigen Server wie Grizzly ausführen (mehr dazu später).

---

### **2. Erstellen Sie eine RESTful-Ressource**
RESTful-Dienste in JAX-RS werden mit Ressourcenklassen definiert, die mit `@Path` und HTTP-Methoden-Annotationen wie `@GET`, `@POST` usw. annotiert sind. Hier ist ein Beispiel für eine einfache Ressource:

#### **Beispiel: HelloResource.java**
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

- **`@Path("/hello")`**: Gibt den URI-Pfad für diese Ressource an (z.B. `http://localhost:8080/api/hello`).
- **`@GET`**: Zeigt an, dass diese Methode HTTP-GET-Anfragen verarbeitet.
- **`@Produces(MediaType.TEXT_PLAIN)`**: Gibt an, dass die Antwort Klartext sein wird.

Wenn eine GET-Anfrage an `/hello` gesendet wird, gibt diese Methode `"Hello, World!"` zurück.

---

### **3. Konfigurieren Sie die JAX-RS-Anwendung**
Sie müssen der JAX-RS-Laufzeitumgebung mitteilen, welche Ressourcen eingeschlossen werden sollen. Dies kann durch Erstellen einer Anwendungskonfigurationsklasse erfolgen, die `javax.ws.rs.core.Application` erweitert.

#### **Beispiel: MyApplication.java**
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

- **`@ApplicationPath("/api")`**: Definiert den Basis-URI-Pfad für alle Ressourcen (z.B. `/api/hello`).
- **`getClasses()`**: Gibt die Menge der Ressourcenklassen zurück, die in die Anwendung aufgenommen werden sollen.

Bei modernen Servlet-Containern (Servlet 3.0+) ist diese annotationsbasierte Konfiguration oft ausreichend, und Sie benötigen möglicherweise keine `web.xml`-Datei.

---

### **4. Verschiedene HTTP-Methoden und Parameter behandeln**
JAX-RS bietet Annotationen zur Behandlung verschiedener HTTP-Methoden, Medientypen und Parameter.

#### **Beispiel: Behandlung von POST-Anfragen**
```java
import javax.ws.rs.POST;
import javax.ws.rs.Consumes;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@POST
@Consumes(MediaType.APPLICATION_JSON)
public Response createItem(MyItem item) {
    // Logik zur Verarbeitung des Items
    return Response.status(Response.Status.CREATED).build();
}
```

- **`@POST`**: Verarbeitet HTTP-POST-Anfragen.
- **`@Consumes(MediaType.APPLICATION_JSON)`**: Erwartet JSON-Eingabe, die in ein `MyItem`-Objekt deserialisiert wird.
- **`Response`**: Gibt einen 201 Created-Status zurück.

#### **Beispiel: Pfadparameter**
```java
import javax.ws.rs.PathParam;
import javax.ws.rs.Path;

@GET
@Path("/{id}")
@Produces(MediaType.APPLICATION_JSON)
public MyItem getItem(@PathParam("id") String id) {
    // Logik zum Abrufen des Items anhand der ID
    return new MyItem(id);
}
```

- **`@Path("/{id}")`**: Definiert einen Pfadparameter (z.B. `/hello/123`).
- **`@PathParam("id")`**: Injiziert den `id`-Wert aus dem URI.

#### **Beispiel: Abfrageparameter**
```java
import javax.ws.rs.QueryParam;

@GET
@Produces(MediaType.APPLICATION_JSON)
public List<MyItem> getItems(@QueryParam("category") String category) {
    // Logik zum Filtern von Items nach Kategorie
    return itemList;
}
```

- **`@QueryParam("category")`**: Holt den `category`-Wert aus der Abfragezeichenkette (z.B. `/hello?category=books`).

---

### **5. Stellen Sie die Anwendung bereit**
Sie können Ihre JAX-RS-Anwendung in einem Servlet-Container wie Tomcat bereitstellen:

1. Packen Sie Ihr Projekt als WAR-Datei (z.B. mit `mvn package`).
2. Stellen Sie die WAR-Datei in Ihrem Container bereit.
3. Greifen Sie auf Ihren Dienst unter der konfigurierten URI zu (z.B. `http://localhost:8080/your-app/api/hello`).

Alternativ können Sie die Anwendung für Entwicklungszwecke oder eigenständige Verwendung programmgesteuert mit Jersey und Grizzly ausführen:

#### **Beispiel: Eigenständige Main**
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

Dies startet einen HTTP-Server ohne einen vollständigen Servlet-Container.

---

### **6. Zusätzliche Funktionen**
- **Ausnahmebehandlung**: Verwenden Sie `ExceptionMapper`, um Ausnahmen elegant zu behandeln.
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
- **Dependency Injection**: Verwenden Sie `@Context`, um Objekte wie `UriInfo` zu injizieren, oder verlassen Sie sich auf das DI-Framework der Implementierung (z.B. HK2 in Jersey).
- **Testing**: Verwenden Sie Tools wie Postman oder das Jersey Test Framework, um Ihre Endpunkte zu testen.

---

### **Zusammenfassung**
Um `javax.ws.rs` zu verwenden, binden Sie die JAX-RS-API und eine Implementierung wie Jersey in Ihr Projekt ein, definieren Sie Ressourcenklassen mit Annotationen für Pfade und HTTP-Methoden, konfigurieren Sie die Anwendung (über eine `Application`-Unterklasse oder `web.xml`) und stellen Sie sie in einem Servlet-Container bereit oder führen Sie sie eigenständig aus. Dies ermöglicht es Ihnen, effizient RESTful-Webdienste mit Java zu erstellen.