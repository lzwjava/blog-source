---
audio: false
generated: true
lang: de
layout: post
title: Java-API für RESTful Webdienste
translated: true
---

Um `javax.ws.rs` zu verwenden, die Java-API für RESTful Webdienste (gemeinhin als JAX-RS bekannt), müssen Sie eine Reihe von Schritten befolgen, um Ihr Projekt einzurichten, RESTful-Ressourcen zu definieren, Ihre Anwendung zu konfigurieren und sie zu deployen. JAX-RS ermöglicht es Ihnen, Webdienste zu erstellen, die dem REST-Architekturstil entsprechen, indem Sie Annotationen verwenden, um Endpunkte zu definieren und HTTP-Anfragen zu verarbeiten. Hier ist eine umfassende Anleitung, um Ihnen den Einstieg zu erleichtern:

---

### **1. Projekt einrichten**
Um `javax.ws.rs` zu verwenden, müssen Sie die JAX-RS-API und eine Implementierung (da `javax.ws.rs` eine Spezifikation und keine Laufzeitumgebung ist) in Ihr Projekt einbinden. Eine beliebte Implementierung ist Jersey. Wenn Sie Maven verwenden, fügen Sie die erforderlichen Abhängigkeiten zu Ihrer `pom.xml` hinzu:

#### **Abhängigkeiten**
```xml
<!-- JAX-RS API -->
<dependency>
    <groupId>javax.ws.rs</groupId>
    <artifactId>javax.ws.rs-api</artifactId>
    <version>2.1.1</version>
</dependency>

<!-- Jersey-Implementierung (enthält Kernabhängigkeiten) -->
<dependency>
    <groupId>org.glassfish.jersey.bundles</groupId>
    <artifactId>jaxrs-ri</artifactId>
    <version>2.34</version>
</dependency>

<!-- Optional: JSON-Unterstützung mit Jackson -->
<dependency>
    <groupId>org.glassfish.jersey.media</groupId>
    <artifactId>jersey-media-json-jackson</artifactId>
    <version>2.34</version>
</dependency>
```

- Die `javax.ws.rs-api` stellt die Kern-JAX-RS-Annotationen und -Klassen bereit.
- Das `jaxrs-ri`-Bundle enthält die Jersey-Implementierung und deren Abhängigkeiten.
- Das `jersey-media-json-jackson`-Modul (optional) fügt Unterstützung für JSON-Serialisierung/Deserialisierung hinzu.

Stellen Sie sicher, dass Ihr Projekt mit einem Servlet-Container (z. B. Tomcat) oder einem Java EE-Server eingerichtet ist, da JAX-RS-Anwendungen normalerweise in solchen Umgebungen laufen. Alternativ können Sie mit einem leichten Server wie Grizzly im Standalone-Modus laufen (mehr dazu später).

---

### **2. Eine RESTful-Ressource erstellen**
RESTful-Dienste in JAX-RS werden mit Ressourcenklassen definiert, die mit `@Path` und HTTP-Methoden-Annotationen wie `@GET`, `@POST` usw. versehen sind. Hier ist ein Beispiel für eine einfache Ressource:

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

- **`@Path("/hello")`**: Gibt den URI-Pfad für diese Ressource an (z. B. `http://localhost:8080/api/hello`).
- **`@GET`**: Gibt an, dass diese Methode HTTP-GET-Anfragen verarbeitet.
- **`@Produces(MediaType.TEXT_PLAIN)`**: Gibt an, dass die Antwort einfacher Text ist.

Wenn eine GET-Anfrage an `/hello` gesendet wird, gibt diese Methode `"Hello, World!"` zurück.

---

### **3. Die JAX-RS-Anwendung konfigurieren**
Sie müssen der JAX-RS-Laufzeit mitteilen, welche Ressourcen enthalten sein sollen. Dies kann durch Erstellen einer Anwendungs-Konfigurationsklasse, die `javax.ws.rs.core.Application` erweitert, erfolgen.

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

- **`@ApplicationPath("/api")`**: Definiert den Basis-URI-Pfad für alle Ressourcen (z. B. `/api/hello`).
- **`getClasses()`**: Gibt die Menge der Ressourcenklassen zurück, die in der Anwendung enthalten sein sollen.

Mit modernen Servlet-Containern (Servlet 3.0+) ist diese annotationsbasierte Konfiguration oft ausreichend, und Sie benötigen möglicherweise keine `web.xml`-Datei.

---

### **4. Verschiedene HTTP-Methoden und Parameter verarbeiten**
JAX-RS stellt Annotationen bereit, um verschiedene HTTP-Methoden, Medienarten und Parameter zu verarbeiten.

#### **Beispiel: Verarbeiten von POST-Anfragen**
```java
import javax.ws.rs.POST;
import javax.ws.rs.Consumes;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@POST
@Consumes(MediaType.APPLICATION_JSON)
public Response createItem(MyItem item) {
    // Logik zur Verarbeitung des Elements
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
    // Logik zum Abrufen des Elements nach ID
    return new MyItem(id);
}
```

- **`@Path("/{id}")`**: Definiert einen Pfadparameter (z. B. `/hello/123`).
- **`@PathParam("id")`**: Injektiert den `id`-Wert aus dem URI.

#### **Beispiel: Abfrageparameter**
```java
import javax.ws.rs.QueryParam;

@GET
@Produces(MediaType.APPLICATION_JSON)
public List<MyItem> getItems(@QueryParam("category") String category) {
    // Logik zum Filtern von Elementen nach Kategorie
    return itemList;
}
```

- **`@QueryParam("category")`**: Ruft den `category`-Wert aus der Abfragezeichenfolge ab (z. B. `/hello?category=books`).

---

### **5. Die Anwendung deployen**
Sie können Ihre JAX-RS-Anwendung in einem Servlet-Container wie Tomcat deployen:

1. Paketieren Sie Ihr Projekt als WAR-Datei (z. B. mit `mvn package`).
2. Deployen Sie die WAR-Datei in Ihren Container.
3. Greifen Sie auf Ihren Dienst über den konfigurierten URI zu (z. B. `http://localhost:8080/your-app/api/hello`).

Alternativ können Sie die Anwendung für die Entwicklung oder den Standalone-Betrieb programmgestützt mit Jersey und Grizzly ausführen:

#### **Beispiel: Standalone Main**
```java
import org.glassfish.jersey.grizzly2.httpserver.GrizzlyHttpServerFactory;
import org.glassfish.jersey.server.ResourceConfig;
import java.net.URI;

public class Main {
    public static void main(String[] args) {
        URI baseUri = URI.create("http://localhost:8080/api/");
        ResourceConfig config = new ResourceConfig(HelloResource.class);
        GrizzlyHttpServerFactory.createHttpServer(baseUri, config);
        System.out.println("Server läuft unter " + baseUri);
    }
}
```

Dies startet einen HTTP-Server ohne einen vollständigen Servlet-Container.

---

### **6. Zusätzliche Funktionen**
- **Ausnahmebehandlung**: Verwenden Sie `ExceptionMapper`, um Ausnahmen anmutig zu behandeln.
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
- **Abhängigkeitsinjektion**: Verwenden Sie `@Context`, um Objekte wie `UriInfo` zu injizieren, oder verlassen Sie sich auf das DI-Framework der Implementierung (z. B. HK2 in Jersey).
- **Testen**: Verwenden Sie Tools wie Postman oder das Jersey Test Framework, um Ihre Endpunkte zu testen.

---

### **Zusammenfassung**
Um `javax.ws.rs` zu verwenden, binden Sie die JAX-RS-API und eine Implementierung wie Jersey in Ihr Projekt ein, definieren Sie Ressourcenklassen mit Annotationen für Pfade und HTTP-Methoden, konfigurieren Sie die Anwendung (über eine `Application`-Unterklasse oder `web.xml`) und deployen Sie sie in einem Servlet-Container oder führen Sie sie im Standalone-Modus aus. Dies ermöglicht es Ihnen, RESTful Webdienste effizient mit Java zu erstellen.