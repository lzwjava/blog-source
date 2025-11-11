---
audio: false
generated: true
lang: es
layout: post
title: Anotaciones de Swagger
translated: true
type: note
---

Para usar el paquete `swagger-annotations` en tu proyecto Java, particularmente para documentar una API REST construida con Spring Boot, sigue estos pasos. Esta guía asume que estás usando Swagger 2.0, que comúnmente se integra con la librería `springfox`. El paquete `swagger-annotations` proporciona anotaciones para agregar metadatos a tus endpoints de API, permitiendo la generación automática de documentación de la API.

---

### Paso 1: Agregar las Dependencias Requeridas

Necesitas incluir el paquete `swagger-annotations` y una librería de integración de Swagger (ej., `springfox`) en tu proyecto. Si estás usando Maven, agrega las siguientes dependencias a tu `pom.xml`:

```xml
<!-- Swagger Annotations -->
<dependency>
    <groupId>io.swagger</groupId>
    <artifactId>swagger-annotations</artifactId>
    <version>1.6.2</version>
</dependency>

<!-- Springfox Swagger 2 para Integración con Swagger -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
</dependency>

<!-- Springfox Swagger UI para Documentación Interactiva -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.9.2</version>
</dependency>
```

- **`io.swagger:swagger-annotations`**: Proporciona las anotaciones para Swagger 2.0.
- **`springfox-swagger2`**: Integra Swagger con Spring Boot y procesa las anotaciones.
- **`springfox-swagger-ui`**: Agrega una interfaz web para ver la documentación generada.

> **Nota**: Consulta las versiones más recientes en [Maven Repository](https://mvnrepository.com/) ya que estas versiones (1.6.2 para `swagger-annotations` y 2.9.2 para `springfox`) pueden tener actualizaciones.

---

### Paso 2: Configurar Swagger en Tu Aplicación

Para habilitar Swagger y permitir que escanee tu API en busca de anotaciones, crea una clase de configuración con un bean `Docket`. Agrega esto a tu aplicación Spring Boot:

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
                .apis(RequestHandlerSelectors.any()) // Escanear todos los controladores
                .paths(PathSelectors.any())          // Incluir todas las rutas
                .build();
    }
}
```

- **`@EnableSwagger2`**: Activa el soporte para Swagger 2.0.
- **`Docket`**: Configura qué endpoints documentar. La configuración anterior escanea todos los controladores y rutas, pero puedes personalizarla (ej., `RequestHandlerSelectors.basePackage("com.example.controllers")`) para limitar el alcance.

---

### Paso 3: Usar las Anotaciones de Swagger en Tu Código

El paquete `swagger-annotations` proporciona anotaciones para describir tu API. Aplícalas a tus clases controlador, métodos, parámetros y modelos. A continuación se muestran anotaciones comunes con ejemplos:

#### Anotar un Controlador

Usa `@Api` para describir el controlador:

```java
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "User Controller", description = "Operaciones relacionadas con usuarios")
@RestController
@RequestMapping("/users")
public class UserController {
    // Los métodos van aquí
}
```

- **`value`**: Un nombre corto para la API.
- **`description`**: Una breve explicación de lo que hace el controlador.

#### Anotar Operaciones de la API

Usa `@ApiOperation` para describir endpoints individuales:

```java
import io.swagger.annotations.ApiOperation;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Obtener un usuario por ID", response = User.class)
@GetMapping("/{id}")
public ResponseEntity<User> getUserById(@PathVariable Long id) {
    // Implementación
    return ResponseEntity.ok(new User(id, "John Doe"));
}
```

- **`value`**: Un resumen de la operación.
- **`response`**: El tipo de retorno esperado.

#### Describir Parámetros

Usa `@ApiParam` para los parámetros del método:

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@ApiOperation(value = "Crear un nuevo usuario")
@PostMapping
public ResponseEntity<User> createUser(
        @ApiParam(value = "Objeto User a crear", required = true) 
        @RequestBody User user) {
    // Implementación
    return ResponseEntity.ok(user);
}
```

- **`value`**: Describe el parámetro.
- **`required`**: Indica si el parámetro es obligatorio.

#### Especificar Respuestas

Usa `@ApiResponses` y `@ApiResponse` para documentar posibles respuestas HTTP:

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.ApiResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Eliminar un usuario")
@ApiResponses(value = {
    @ApiResponse(code = 200, message = "Usuario eliminado exitosamente"),
    @ApiResponse(code = 404, message = "Usuario no encontrado")
})
@DeleteMapping("/{id}")
public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
    // Implementación
    return ResponseEntity.ok().build();
}
```

- **`code`**: Código de estado HTTP.
- **`message`**: Descripción de la respuesta.

#### Describir Modelos

Para los objetos de transferencia de datos (DTOs), usa `@ApiModel` y `@ApiModelProperty`:

```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(description = "Objeto de transferencia de datos de usuario")
public class User {
    @ApiModelProperty(notes = "El identificador único del usuario", example = "1")
    private Long id;

    @ApiModelProperty(notes = "El nombre del usuario", example = "John Doe")
    private String name;

    // Getters y setters
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

- **`@ApiModel`**: Describe el modelo.
- **`@ApiModelProperty`**: Detalla cada campo, con ejemplos opcionales.

---

### Paso 4: Ejecutar y Acceder a la Documentación

1. Inicia tu aplicación Spring Boot.
2. Abre un navegador y navega a:  
   **http://localhost:8080/swagger-ui.html**  
   Esta URL muestra la interfaz de usuario de Swagger, una interfaz interactiva que muestra la documentación de tu API basada en las anotaciones.

---

### Resumen de Cómo Usar `swagger-annotations`

1.  **Agregar Dependencias**: Incluye `swagger-annotations` y `springfox` en tu `pom.xml`.
2.  **Configurar Swagger**: Configura un bean `Docket` para habilitar el escaneo de Swagger.
3.  **Anotar Tu Código**:
    - `@Api` para controladores.
    - `@ApiOperation` para métodos.
    - `@ApiParam` para parámetros.
    - `@ApiResponses` y `@ApiResponse` para detalles de respuesta.
    - `@ApiModel` y `@ApiModelProperty` para DTOs.
4.  **Ver Documentación**: Accede a la interfaz de usuario de Swagger en `/swagger-ui.html`.

---

### Notas Adicionales

- **Swagger 2.0 vs. OpenAPI 3.0**: Esta guía usa Swagger 2.0 con `io.swagger:swagger-annotations`. Para OpenAPI 3.0, usa `io.swagger.core.v3:swagger-annotations` y una librería como `springdoc-openapi`, lo que cambia algunos nombres de anotaciones (ej., `@Tag` en lugar de `@Api`).
- **Personalización**: Ajusta la configuración de `Docket` para filtrar paquetes o rutas específicas para una documentación más enfocada.
- **Calidad**: Proporciona descripciones claras y detalladas en las anotaciones para mejorar la utilidad de la documentación generada.

Siguiendo estos pasos, puedes usar efectivamente el paquete `swagger-annotations` para documentar tu API REST, haciendo que sea más fácil para los desarrolladores y consumidores entender e interactuar con tus endpoints.