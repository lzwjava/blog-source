---
audio: false
generated: true
lang: es
layout: post
title: Módulo Spring Data REST
translated: true
type: note
---

Para usar **spring-data-rest-core**, puedes aprovechar el módulo Spring Data REST para exponer tus repositorios de Spring Data como endpoints RESTful en tu aplicación. A continuación, una guía completa paso a paso para comenzar:

---

### 1. Agregar la Dependencia de Spring Data REST
Para usar Spring Data REST, necesitas incluir su dependencia en tu proyecto. Si estás usando **Spring Boot** (un escenario común), agrega la siguiente dependencia a tu archivo de construcción:

- **Maven**:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-data-rest</artifactId>
  </dependency>
  ```

- **Gradle**:
  ```gradle
  implementation 'org.springframework.boot:spring-boot-starter-data-rest'
  ```

Este starter incluye `spring-data-rest-core` junto con otros componentes necesarios. Para proyectos que no usan Spring Boot, puedes incluir `spring-data-rest-core` directamente, pero se recomienda el starter de Spring Boot por su simplicidad.

---

### 2. Definir tus Entidades
Crea tu modelo de dominio definiendo clases de entidad usando una tecnología de persistencia como JPA (Java Persistence API). Por ejemplo:

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

    // Constructores
    public User() {}
    public User(String name) {
        this.name = name;
    }

    // Getters y Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
}
```

Esta entidad `User` representa una tabla simple en tu base de datos con un `id` y un `name`.

---

### 3. Crear Interfaces de Repositorio
Define una interfaz de repositorio para tu entidad extendiendo una de las interfaces de repositorio de Spring Data, como `JpaRepository`. Por ejemplo:

```java
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
```

Al extender `JpaRepository`, obtienes operaciones CRUD (Crear, Leer, Actualizar, Eliminar) básicas de forma gratuita. Spring Data REST expondrá automáticamente este repositorio como un endpoint RESTful.

---

### 4. Ejecutar tu Aplicación
Con la dependencia agregada y tus entidades y repositorios definidos, inicia tu aplicación Spring Boot. Spring Data REST generará automáticamente endpoints REST basados en tu repositorio. Para el `UserRepository` anterior, puedes acceder a:

- **GET /users**: Recuperar una lista de todos los usuarios.
- **GET /users/{id}**: Recuperar un usuario específico por ID.
- **POST /users**: Crear un nuevo usuario (con un payload JSON, ej. `{"name": "Alice"}`).
- **PUT /users/{id}**: Actualizar un usuario existente.
- **DELETE /users/{id}**: Eliminar un usuario.

Por ejemplo, si tu aplicación se ejecuta en `localhost:8080`, puedes usar una herramienta como `curl` o un navegador para probar:

```bash
curl http://localhost:8080/users
```

La respuesta incluirá enlaces HATEOAS, permitiendo a los clientes navegar dinámicamente por los recursos relacionados.

---

### 5. (Opcional) Personalizar los Endpoints REST
Puedes personalizar cómo se exponen tus repositorios usando anotaciones o configuración:

- **Cambiar la Ruta del Endpoint**:
  Usa la anotación `@RepositoryRestResource` para especificar una ruta personalizada:
  ```java
  import org.springframework.data.rest.core.annotation.RepositoryRestResource;

  @RepositoryRestResource(path = "people")
  public interface UserRepository extends JpaRepository<User, Long> {
  }
  ```
  Ahora, el endpoint será `/people` en lugar de `/users`.

- **Configurar Ajustes Globales**:
  Personaliza la ruta base u otros ajustes implementando `RepositoryRestConfigurer`:
  ```java
  import org.springframework.data.rest.webmvc.config.RepositoryRestConfigurer;
  import org.springframework.context.annotation.Configuration;
  import org.springframework.data.rest.core.config.RepositoryRestConfiguration;

  @Configuration
  public class RestConfig implements RepositoryRestConfigurer {
      @Override
      public void configureRepositoryRestConfiguration(RepositoryRestConfiguration config) {
          config.setBasePath("/api"); // Todos los endpoints comenzarán con /api
      }
  }
  ```
  Con esto, tus usuarios serían accesibles en `/api/users`.

---

### Características Clave de Spring Data REST
- **Soporte HATEOAS**: Las respuestas incluyen enlaces de hipermedia a recursos relacionados.
- **Paginación y Ordenación**: Usa parámetros de consulta como `?page=0&size=10&sort=name,asc` para paginar y ordenar resultados.
- **Filtrado**: Agrega métodos de consulta personalizados a tu repositorio (ej. `findByName(String name)`) para exponer endpoints adicionales.

---

### Resumen
Para usar `spring-data-rest-core`:
1. Incluye la dependencia de Spring Data REST (ej. `spring-boot-starter-data-rest` para Spring Boot).
2. Define tus entidades con las anotaciones apropiadas (ej. `@Entity` para JPA).
3. Crea interfaces de repositorio que extiendan las interfaces de Spring Data (ej. `JpaRepository`).
4. Ejecuta tu aplicación para acceder a los endpoints REST generados automáticamente.
5. Opcionalmente, personaliza las rutas de los endpoints o el comportamiento según sea necesario.

Este enfoque te permite construir rápidamente una API RESTful con código mínimo, aprovechando la funcionalidad central de Spring Data REST.