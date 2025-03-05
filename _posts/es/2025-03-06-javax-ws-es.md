---
audio: false
generated: true
lang: es
layout: post
title: API de Java para Servicios Web RESTful
translated: true
---

Para usar `javax.ws.rs`, la API de Java para servicios web RESTful (comúnmente conocida como JAX-RS), debes seguir una serie de pasos para configurar tu proyecto, definir recursos RESTful, configurar tu aplicación y desplegarla. JAX-RS te permite crear servicios web que cumplen con el estilo arquitectónico REST, utilizando anotaciones para definir puntos finales y manejar solicitudes HTTP. A continuación, se presenta una guía completa para comenzar:

---

### **1. Configurar tu Proyecto**
Para usar `javax.ws.rs`, debes incluir la API JAX-RS y una implementación (ya que `javax.ws.rs` es una especificación, no un tiempo de ejecución). Una implementación popular es Jersey. Si estás usando Maven, agrega las dependencias necesarias a tu `pom.xml`:

#### **Dependencias**
```xml
<!-- API JAX-RS -->
<dependency>
    <groupId>javax.ws.rs</groupId>
    <artifactId>javax.ws.rs-api</artifactId>
    <version>2.1.1</version>
</dependency>

<!-- Implementación de Jersey (incluye dependencias principales) -->
<dependency>
    <groupId>org.glassfish.jersey.bundles</groupId>
    <artifactId>jaxrs-ri</artifactId>
    <version>2.34</version>
</dependency>

<!-- Opcional: Soporte JSON con Jackson -->
<dependency>
    <groupId>org.glassfish.jersey.media</groupId>
    <artifactId>jersey-media-json-jackson</artifactId>
    <version>2.34</version>
</dependency>
```

- La `javax.ws.rs-api` proporciona las anotaciones y clases principales de JAX-RS.
- El paquete `jaxrs-ri` incluye la implementación de Jersey y sus dependencias.
- El módulo `jersey-media-json-jackson` (opcional) agrega soporte para la serialización/deserialización JSON.

Asegúrate de que tu proyecto esté configurado con un contenedor de servlets (por ejemplo, Tomcat) o un servidor Java EE, ya que las aplicaciones JAX-RS generalmente se ejecutan en tales entornos. Alternativamente, puedes ejecutar de forma independiente con un servidor ligero como Grizzly (más sobre eso más adelante).

---

### **2. Crear un Recurso RESTful**
Los servicios RESTful en JAX-RS se definen utilizando clases de recursos anotadas con `@Path` y anotaciones de métodos HTTP como `@GET`, `@POST`, etc. Aquí tienes un ejemplo de un recurso simple:

#### **Ejemplo: HelloResource.java**
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
        return "¡Hola, Mundo!";
    }
}
```

- **`@Path("/hello")`**: Especifica la ruta URI para este recurso (por ejemplo, `http://localhost:8080/api/hello`).
- **`@GET`**: Indica que este método maneja las solicitudes HTTP GET.
- **`@Produces(MediaType.TEXT_PLAIN)`**: Especifica que la respuesta será texto plano.

Cuando se realiza una solicitud GET a `/hello`, este método devuelve `"¡Hola, Mundo!"`.

---

### **3. Configurar la Aplicación JAX-RS**
Debes informar al tiempo de ejecución de JAX-RS qué recursos incluir. Esto se puede hacer creando una clase de configuración de aplicación que extienda `javax.ws.rs.core.Application`.

#### **Ejemplo: MyApplication.java**
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

- **`@ApplicationPath("/api")`**: Define la ruta URI base para todos los recursos (por ejemplo, `/api/hello`).
- **`getClasses()`**: Devuelve el conjunto de clases de recursos a incluir en la aplicación.

Con contenedores de servlets modernos (Servlet 3.0+), esta configuración basada en anotaciones es a menudo suficiente y es posible que no necesites un archivo `web.xml`.

---

### **4. Manejar Diferentes Métodos HTTP y Parámetros**
JAX-RS proporciona anotaciones para manejar varios métodos HTTP, tipos de medios y parámetros.

#### **Ejemplo: Manejar Solicitudes POST**
```java
import javax.ws.rs.POST;
import javax.ws.rs.Consumes;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@POST
@Consumes(MediaType.APPLICATION_JSON)
public Response createItem(MyItem item) {
    // Lógica para procesar el elemento
    return Response.status(Response.Status.CREATED).build();
}
```

- **`@POST`**: Maneja las solicitudes HTTP POST.
- **`@Consumes(MediaType.APPLICATION_JSON)`**: Espera una entrada JSON, que se deserializa en un objeto `MyItem`.
- **`Response`**: Devuelve un estado 201 Creado.

#### **Ejemplo: Parámetros de Ruta**
```java
import javax.ws.rs.PathParam;
import javax.ws.rs.Path;

@GET
@Path("/{id}")
@Produces(MediaType.APPLICATION_JSON)
public MyItem getItem(@PathParam("id") String id) {
    // Lógica para recuperar el elemento por ID
    return new MyItem(id);
}
```

- **`@Path("/{id}")`**: Define un parámetro de ruta (por ejemplo, `/hello/123`).
- **`@PathParam("id")`**: Inyecta el valor `id` de la URI.

#### **Ejemplo: Parámetros de Consulta**
```java
import javax.ws.rs.QueryParam;

@GET
@Produces(MediaType.APPLICATION_JSON)
public List<MyItem> getItems(@QueryParam("category") String category) {
    // Lógica para filtrar elementos por categoría
    return itemList;
}
```

- **`@QueryParam("category")`**: Recupera el valor `category` de la cadena de consulta (por ejemplo, `/hello?category=books`).

---

### **5. Desplegar la Aplicación**
Puedes desplegar tu aplicación JAX-RS en un contenedor de servlets como Tomcat:

1. Empaqueta tu proyecto como un archivo WAR (por ejemplo, usando `mvn package`).
2. Despliega el archivo WAR en tu contenedor.
3. Accede a tu servicio en la URI configurada (por ejemplo, `http://localhost:8080/your-app/api/hello`).

Alternativamente, para desarrollo o uso independiente, puedes ejecutar la aplicación programáticamente utilizando Jersey con Grizzly:

#### **Ejemplo: Main Independiente**
```java
import org.glassfish.jersey.grizzly2.httpserver.GrizzlyHttpServerFactory;
import org.glassfish.jersey.server.ResourceConfig;
import java.net.URI;

public class Main {
    public static void main(String[] args) {
        URI baseUri = URI.create("http://localhost:8080/api/");
        ResourceConfig config = new ResourceConfig(HelloResource.class);
        GrizzlyHttpServerFactory.createHttpServer(baseUri, config);
        System.out.println("Servidor en ejecución en " + baseUri);
    }
}
```

Esto inicia un servidor HTTP sin un contenedor de servlets completo.

---

### **6. Características Adicionales**
- **Manejo de Excepciones**: Usa `ExceptionMapper` para manejar excepciones de manera elegante.
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
- **Inyección de Dependencias**: Usa `@Context` para inyectar objetos como `UriInfo` o confía en el marco de inyección de dependencias de la implementación (por ejemplo, HK2 en Jersey).
- **Pruebas**: Usa herramientas como Postman o el marco de pruebas de Jersey para probar tus puntos finales.

---

### **Resumen**
Para usar `javax.ws.rs`, incluye la API JAX-RS y una implementación como Jersey en tu proyecto, define clases de recursos con anotaciones para rutas y métodos HTTP, configura la aplicación (a través de una subclase de `Application` o `web.xml`) y despliégala en un contenedor de servlets o ejecútala de forma independiente. Esto te permite construir servicios web RESTful de manera eficiente con Java.