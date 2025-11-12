---
audio: false
generated: true
lang: es
layout: post
title: Spring Boot frente a Spring Framework
translated: true
type: note
---

Adentrémonos en las diferencias entre **Spring Boot** y **Spring** (a menudo denominado Spring Framework). Aunque están estrechamente relacionados, cumplen propósitos distintos dentro del ecosistema Java. Lo desglosaré en dimensiones clave como propósito, configuración, velocidad de desarrollo y casos de uso.

### 1. **Descripción general y propósito**
- **Spring Framework**: El framework original y fundamental para aplicaciones Java. Introducido en 2002, proporciona un modelo completo de programación y configuración para simplificar el desarrollo empresarial en Java. Es un ecosistema amplio con módulos como Spring MVC, Spring Security y Spring Data, que se centra en la inyección de dependencias y la modularidad.
- **Spring Boot**: Una capa construida sobre Spring Framework, lanzada en 2014. Está diseñado para simplificar el desarrollo con Spring ofreciendo una experiencia "listo para ejecutar" con una configuración mínima. Piensa en ello como Spring con las pilas incluidas—optimizado para el desarrollo rápido de aplicaciones y la preparación para producción.

### 2. **Configuración**
- **Spring**: Requiere configuración manual. Tú defines los beans, configuras las dependencias y los componentes (por ejemplo, mediante archivos XML o anotaciones Java). Esto te da un control detallado, pero puede ser lento y propenso a errores, especialmente para principiantes.
- **Spring Boot**: Hace hincapié en la **autoconfiguración**. Utiliza valores predeterminados sensatos basados en las dependencias que incluyes (por ejemplo, añadir Spring Web configura automáticamente un servidor web como Tomcat). Puedes anular estos valores predeterminados si es necesario, pero el objetivo es minimizar la configuración.

### 3. **Velocidad de desarrollo**
- **Spring**: Más lento para empezar porque necesitas conectar todo manualmente: dependencias, servidores, conexiones a bases de datos, etc. Es potente, pero requiere más esfuerzo para poner en marcha una aplicación básica.
- **Spring Boot**: Desarrollo más rápido gracias a su filosofía de "convención sobre configuración". Por ejemplo, una API REST simple puede estar funcionando en minutos con unas pocas líneas de código, gracias a los servidores embebidos y las dependencias starter.

### 4. **Gestión de dependencias**
- **Spring**: Depende de que gestiones las dependencias manualmente mediante Maven o Gradle. Tú eliges y seleccionas los módulos de Spring (por ejemplo, Spring Core, Spring MVC) y las librerías de terceros, lo que puede generar conflictos de versiones si no se maneja con cuidado.
- **Spring Boot**: Proporciona **dependencias starter** (por ejemplo, `spring-boot-starter-web`, `spring-boot-starter-data-jpa`) que agrupan versiones compatibles de las librerías. Esto reduce los problemas de la gestión de dependencias y garantiza la coherencia.

### 5. **Servidor embebido**
- **Spring**: No incluye un servidor embebido. Normalmente, despliegas las aplicaciones Spring en un servidor externo como Tomcat, JBoss o WebSphere, lo que requiere configuración adicional.
- **Spring Boot**: Viene con servidores embebidos (Tomcat, Jetty o Undertow) por defecto. Puedes ejecutar tu aplicación como un archivo JAR independiente con `java -jar`, lo que simplifica el despliegue y lo hace más portable (por ejemplo, para Docker).

### 6. **Preparación para producción**
- **Spring**: Ofrece herramientas como Spring Security y Spring Transaction Management, pero necesitas configurar tú mismo la monitorización, las comprobaciones de estado y las métricas.
- **Spring Boot**: Incluye **Spring Boot Actuator**, que añade características listas para producción de inmediato: endpoints de salud, métricas, registro, y más. Está diseñado para estar listo para el despliegue con ajustes mínimos.

### 7. **Flexibilidad vs. Simplicidad**
- **Spring**: Muy flexible y personalizable. Ideal cuando necesitas control total sobre cada aspecto de tu aplicación, pero esto tiene el coste de una mayor complejidad.
- **Spring Boot**: Intercambia parte de la flexibilidad por simplicidad. Es opiniado, lo que significa que impone convenciones (por ejemplo, estructura de proyecto, configuraciones predeterminadas) para agilizar el desarrollo, aunque aún puedes personalizarlo.

### 8. **Casos de uso**
- **Spring**: Lo mejor para aplicaciones empresariales grandes y complejas donde necesitas integrar diversos componentes o sistemas legacy y no te importa la sobrecarga de configuración.
- **Spring Boot**: Perfecto para escenarios de desarrollo moderno y rápido—microservicios, APIs REST, aplicaciones independientes o prototipos donde la velocidad y la simplicidad son importantes.

### Ejemplo de comparación
- **Spring (Configuración básica)**:
  ```java
  // Configuración manual con Spring MVC
  @Configuration
  @EnableWebMvc
  public class WebConfig implements WebMvcConfigurer {
      @Bean
      public ViewResolver viewResolver() {
          InternalResourceViewResolver resolver = new InternalResourceViewResolver();
          resolver.setPrefix("/WEB-INF/views/");
          resolver.setSuffix(".jsp");
          return resolver;
      }
  }
  ```
  Además, necesitarías configurar un `web.xml` o un inicializador de servlet y desplegar en un servidor externo.

- **Spring Boot (Equivalente)**:
  ```java
  @RestController
  public class HelloController {
      @GetMapping("/hello")
      public String sayHello() {
          return "Hello, World!";
      }
  }
  ```
  Añade `spring-boot-starter-web` a tu `pom.xml`, y listo—ejecútalo con un servidor embebido.

### Tabla resumen

| Aspecto              | Spring Framework            | Spring Boot                 |
|---------------------|-----------------------------|-----------------------------|
| **Propósito**       | Framework base para Java    | Uso simplificado de Spring  |
| **Configuración**   | Manual (XML/Anotaciones)    | Autoconfigurado             |
| **Servidor**        | Externo (ej. Tomcat)        | Embebido (Tomcat, Jetty)    |
| **Dependencias**    | Gestión manual              | Los starters lo simplifican |
| **Velocidad**       | Más lento para empezar      | Configuración rápida y prototipado |
| **Flexibilidad**    | Alta, totalmente personalizable | Opiniado, menos flexible  |
| **Ideal para**      | Apps empresariales complejas| Microservicios, apps rápidas|

### Conclusión
- **Spring** es la base—potente, flexible y adecuado para escenarios donde necesitas control total o trabajas con sistemas legacy.
- **Spring Boot** es Spring simplificado—ideal para el desarrollo moderno y ágil con un enfoque en microservicios y aplicaciones independientes.

Si estás iniciando un nuevo proyecto y valoras la velocidad, elige Spring Boot. Si estás manteniendo un sistema complejo o necesitas una personalización profunda, Spring podría ser la base mejor. ¿Quieres que profundice en alguna parte?