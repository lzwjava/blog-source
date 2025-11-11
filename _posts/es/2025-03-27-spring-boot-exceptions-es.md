---
audio: false
generated: true
lang: es
layout: post
title: Excepciones De Spring Boot
translated: true
type: note
---

Al trabajar con Spring Boot o el framework Spring en general, los desarrolladores frecuentemente encuentran excepciones debido a problemas de configuración, errores en tiempo de ejecución o uso incorrecto de las APIs. A continuación se presenta una lista de excepciones comunes que podrías enfrentar, junto con sus causas típicas y posibles resoluciones. Estas excepciones están agrupadas por categoría para mayor claridad.

---

### **1. Excepciones Relacionadas con la Configuración**

- **`org.springframework.beans.factory.BeanCreationException`**:
  - **Causa**: Un bean no pudo ser creado debido a dependencias faltantes, mala configuración o errores de instanciación.
  - **Ejemplo**: Falta la anotación `@Component`, `@Service` o dependencia `@Autowired` no encontrada.
  - **Resolución**: Revisar las definiciones de los beans, asegurar que las dependencias estén disponibles y verificar las anotaciones.

- **`org.springframework.beans.factory.NoSuchBeanDefinitionException`**:
  - **Causa**: Spring no puede encontrar un bean del tipo o nombre solicitado en el contexto de la aplicación.
  - **Ejemplo**: Intentar usar `@Autowired` en un bean que no está definido o escaneado.
  - **Resolución**: Asegurar que el bean esté anotado (ej., `@Component`) y dentro de la ruta de escaneo de componentes.

- **`org.springframework.context.ApplicationContextException`**:
  - **Causa**: Fallo general al inicializar el contexto de la aplicación de Spring.
  - **Ejemplo**: Configuración inválida en `application.properties` o error de sintaxis en una clase `@Configuration`.
  - **Resolución**: Revisar el stack trace para encontrar la causa raíz (ej., propiedad inválida o recurso faltante).

- **`org.springframework.beans.factory.UnsatisfiedDependencyException`**:
  - **Causa**: Una dependencia requerida por un bean no puede ser satisfecha.
  - **Ejemplo**: Dependencia circular o implementación faltante para una interfaz.
  - **Resolución**: Romper las dependencias circulares (ej., usar `@Lazy`) o proporcionar la dependencia faltante.

---

### **2. Excepciones Relacionadas con Web y REST**

- **`org.springframework.web.bind.MissingServletRequestParameterException`**:
  - **Causa**: Falta un parámetro obligatorio en una petición HTTP.
  - **Ejemplo**: Se especifica `@RequestParam("id")`, pero el cliente no envió `id`.
  - **Resolución**: Hacer el parámetro opcional (`required = false`) o asegurar que el cliente lo incluya.

- **`org.springframework.http.converter.HttpMessageNotReadableException`**:
  - **Causa**: El cuerpo de la petición no puede ser deserializado (ej., JSON malformado).
  - **Ejemplo**: Enviar JSON inválido a un endpoint con `@RequestBody`.
  - **Resolución**: Validar el payload de la petición y asegurar que coincida con la estructura del objeto objetivo.

- **`org.springframework.web.method.annotation.MethodArgumentTypeMismatchException`**:
  - **Causa**: Un argumento de método no puede ser convertido al tipo esperado.
  - **Ejemplo**: Pasar un string como `"abc"` a un parámetro que espera un `int`.
  - **Resolución**: Validar la entrada o usar convertidores personalizados.

- **`org.springframework.web.servlet.NoHandlerFoundException`**:
  - **Causa**: No existe un mapeo de controlador para la URL solicitada.
  - **Ejemplo**: Un error tipográfico en `@RequestMapping` o controlador faltante.
  - **Resolución**: Verificar los mapeos de los endpoints y asegurar que los controladores sean escaneados.

---

### **3. Excepciones de Acceso a Datos (Spring Data/JPA/Hibernate)**

- **`org.springframework.dao.DataIntegrityViolationException`**:
  - **Causa**: Una operación de base de datos viola una restricción (ej., clave única o clave foránea).
  - **Ejemplo**: Insertar un valor de clave primaria duplicado.
  - **Resolución**: Revisar los datos por unicidad o manejar la excepción apropiadamente.

- **`org.springframework.orm.jpa.JpaSystemException`**:
  - **Causa**: Error general en tiempo de ejecución relacionado con JPA, a menudo envolviendo una excepción de Hibernate.
  - **Ejemplo**: Violación de restricción o problema de conexión.
  - **Resolución**: Inspeccionar la excepción anidada (ej., `SQLException`) para obtener detalles.

- **`org.hibernate.LazyInitializationException`**:
  - **Causa**: Intentar acceder a una entidad cargada de forma perezosa fuera de una sesión activa.
  - **Ejemplo**: Acceder a una relación `@OneToMany` después de que termina la transacción.
  - **Resolución**: Usar carga eager, cargar en la consulta (ej., `JOIN FETCH`) o asegurar una sesión abierta.

- **`org.springframework.dao.InvalidDataAccessApiUsageException`**:
  - **Causa**: Uso incorrecto de las APIs de Spring Data o JDBC.
  - **Ejemplo**: Pasar un parámetro nulo a una consulta que espera un valor.
  - **Resolución**: Validar los parámetros de la consulta y el uso de la API.

---

### **4. Excepciones Relacionadas con la Seguridad**

- **`org.springframework.security.access.AccessDeniedException`**:
  - **Causa**: El usuario autenticado carece de permiso para un recurso.
  - **Ejemplo**: Acceder a un endpoint seguro sin el rol requerido.
  - **Resolución**: Revisar `@PreAuthorize` o la configuración de seguridad y ajustar los roles/autoridades.

- **`org.springframework.security.authentication.BadCredentialsException`**:
  - **Causa**: La autenticación falló debido a un nombre de usuario o contraseña incorrectos.
  - **Ejemplo**: El usuario ingresa credenciales erróneas en un formulario de inicio de sesión.
  - **Resolución**: Asegurar que las credenciales sean correctas; personalizar el manejo de errores para la retroalimentación del usuario.

- **`org.springframework.security.authentication.DisabledException`**:
  - **Causa**: La cuenta de usuario está deshabilitada.
  - **Ejemplo**: Una implementación de `UserDetails` retorna `isEnabled() == false`.
  - **Resolución**: Habilitar la cuenta o actualizar el estado del usuario.

---

### **5. Excepciones en Tiempo de Ejecución Varias**

- **`java.lang.IllegalStateException`**:
  - **Causa**: Spring encuentra un estado inválido durante la ejecución.
  - **Ejemplo**: Llamar a un método en un bean que no ha sido completamente inicializado.
  - **Resolución**: Revisar los métodos del ciclo de vida o el orden de inicialización de los beans.

- **`org.springframework.transaction.TransactionException`**:
  - **Causa**: Ocurrió un problema durante la gestión de transacciones.
  - **Ejemplo**: Reversión de una transacción debido a una excepción no manejada.
  - **Resolución**: Asegurar el uso correcto de `@Transactional` y manejar las excepciones dentro de la transacción.

- **`java.lang.NullPointerException`**:
  - **Causa**: Intentar acceder a una referencia de objeto nula.
  - **Ejemplo**: Una dependencia `@Autowired` no fue inyectada debido a una mala configuración.
  - **Resolución**: Agregar verificaciones de nulidad o depurar por qué falta la dependencia.

---

### **6. Excepciones Específicas de Spring Boot**

- **`org.springframework.boot.context.embedded.EmbeddedServletContainerException`** (versiones antiguas) o **`org.springframework.boot.web.server.WebServerException`** (versiones nuevas):
  - **Causa**: Fallo al iniciar el servidor web embebido (ej., Tomcat, Jetty).
  - **Ejemplo**: Puerto ya en uso (ej., `8080`).
  - **Resolución**: Cambiar el puerto en `application.properties` (`server.port=8081`) o liberar el puerto ocupado.

- **`org.springframework.boot.autoconfigure.jdbc.DataSourceProperties$DataSourceBeanCreationException`**:
  - **Causa**: Fallo al configurar el origen de datos.
  - **Ejemplo**: Faltan o son incorrectas las propiedades `spring.datasource.url/username/password`.
  - **Resolución**: Verificar las propiedades del origen de datos en `application.properties` o `application.yml`.

- **`org.springframework.boot.SpringApplication - Application run failed`**:
  - **Causa**: Fallo genérico durante el inicio de Spring Boot.
  - **Ejemplo**: Mala configuración, beans faltantes o conflictos de dependencias.
  - **Resolución**: Revisar el stack trace completo para encontrar la causa raíz.

---

### **Mejores Prácticas para Manejar Excepciones**

1. **Manejo Global de Excepciones**:
   - Usar `@ControllerAdvice` con `@ExceptionHandler` para capturar y manejar excepciones de manera consistente en toda la aplicación.
   - Ejemplo:
     ```java
     @ControllerAdvice
     public class GlobalExceptionHandler {
         @ExceptionHandler(DataIntegrityViolationException.class)
         public ResponseEntity<String> handleDataIntegrityViolation() {
             return ResponseEntity.status(HttpStatus.CONFLICT).body("Ocurrió una violación de integridad de datos.");
         }
     }
     ```

2. **Registro (Logging)**:
   - Registrar excepciones con un framework como SLF4J/Logback para ayudar en la depuración.

3. **Excepciones Personalizadas**:
   - Definir excepciones específicas de la aplicación y mapearlas a códigos de estado HTTP apropiados.

4. **Validación**:
   - Usar `@Valid` y Bean Validation (ej., `@NotNull`) para capturar errores temprano y evitar excepciones en tiempo de ejecución.

5. **Depuración**:
   - Habilitar registro detallado (`logging.level.org.springframework=DEBUG`) en `application.properties` para rastrear problemas.

---

### **Conclusión**

Estas excepciones se encuentran entre las más comunes que encontrarás al usar Spring Boot o el framework Spring. Comprender sus causas y resoluciones puede acelerar significativamente el desarrollo y la depuración. Si estás enfrentando una excepción específica y necesitas un análisis más profundo, ¡no dudes en compartir los detalles y proporcionaré una explicación adaptada