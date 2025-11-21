---
audio: false
generated: true
image: false
lang: es
layout: post
model: x-ai/grok-4.1-fast
title: 'Comparación de Filtros de Solicitud: WebSphere frente a Spring Boot'
translated: true
type: note
---

### Resumen
Tanto IBM WebSphere Application Server (WAS, tradicional o Liberty) como Spring Boot admiten el concepto de una **cadena de procesamiento de solicitudes** basada en el `javax.servlet.Filter` y `FilterChain` de la API estándar de Java Servlet. Aquí, las solicitudes HTTP entrantes pasan a través de una serie de filtros antes de llegar a los servlets (o controladores/manejadores), y las respuestas pueden modificarse en el camino de regreso.

- Los filtros permiten el preprocesamiento (por ejemplo, autenticación, registro, compresión) y el postprocesamiento de solicitudes/respuestas.
- El mecanismo central —implementar `Filter`, llamar a `chain.doFilter(request, response)` para continuar— es **idéntico** porque ambos se ejecutan en un contenedor Servlet (WAS tiene su propio contenedor web Java EE completo; Spring Boot incorpora Tomcat/Jetty/Undertow por defecto).

No hay una diferencia fundamental en cómo funciona un "filtro de cadena de solicitudes" básico. Sin embargo, la forma en que se configuran, ordenan e integran los filtros difiere significativamente debido a la arquitectura de cada plataforma.

### Comparación Clave

| Aspecto                  | IBM WebSphere Application Server (Tradicional/Liberty) | Spring Boot |
|-------------------------|---------------------------------------------------------|-------------|
| **Mecanismo Subyacente** | Filtros Servlet estándar (`javax.servlet.Filter`). WAS también tiene extensiones propietarias como `ChainedRequest`/`ChainedResponse` para reenvío/encadenamiento interno de solicitudes en algunos escenarios (por ejemplo, portal o APIs personalizadas de IBM). | Filtros Servlet estándar. Spring Boot registra automáticamente cualquier bean Filter `@Component` o se registra explícitamente mediante `FilterRegistrationBean`. |
| **Configuración**       | Principalmente mediante `web.xml` (declarativo) o registro programático. Para filtros globales (en todas las aplicaciones): complejo — requiere bibliotecas compartidas, listeners personalizados o extensiones específicas de IBM (no hay un web.xml simple a nivel de servidor como en Tomcat). | Convención sobre configuración: Anotar con `@Component` + `@Order` para registro automático, o usar `FilterRegistrationBean` para control detallado (patrones de URL, tipos de despachador). Muy amigable para el desarrollador. |
| **Ordenación**            | Definida en el orden de `web.xml` o mediante `@Order` si es programático. La ordenación global es complicada. | Fácil con `@Order(n)` (menor = más temprano) o la interfaz `Ordered`. Spring Boot gestiona la cadena automáticamente. |
| **Cadena de Filtros de Seguridad** | Utiliza filtros Servlet estándar o seguridad específica de IBM (por ejemplo, TAI, roles JEE). No tiene una cadena de seguridad incorporada como Spring Security. | Spring Security proporciona una potente `SecurityFilterChain` (a través de `FilterChainProxy`) con 15+ filtros ordenados (CSRF, autenticación, gestión de sesiones, etc.). Altamente personalizable con múltiples cadenas por ruta. |
| **Facilidad para Añadir Filtros Personalizados** | Más verboso, especialmente para filtros globales/entre aplicaciones. A menudo requiere ajustes en la consola de administración o bibliotecas compartidas. | Extremadamente simple — solo un bean `@Component` o una clase de configuración. Se auto-integra en el contenedor embebido. |
| **Modelo de Despliegue**    | Servidor Java EE completo tradicional. Las aplicaciones se despliegan como WAR/EAR. Admite funciones empresariales pesadas (clustering, transacciones, JMS). | Contenedor embebido (JAR ejecutable independiente por defecto). Se puede desplegar como WAR en servidores externos (incluido WAS). Orientado a microservicios/ligero. |
| **Rendimiento/Sobrecarga**| Mayor sobrecarga (servidor de aplicaciones completo). Las cadenas de transporte, los canales del contenedor web añaden capas. | Menor sobrecarga (contenedor ligero embebido). Inicio más rápido, menor uso de recursos. |
| **Cuándo se Ejecutan los Filtros**     | En la cadena entrante del contenedor web de WAS. Puede tener filtros de transporte a nivel de servidor (por ejemplo, filtrado de IP en canales TCP). | En la cadena de filtros del contenedor embebido. Spring Boot añade sus propios filtros (manejo de errores, codificación de caracteres, etc.). |
| **Casos de Uso Comunes**    | Monolitos empresariales, portales, aplicaciones Java EE heredadas que necesitan seguridad/registro global. | Microservicios modernos, APIs REST, desarrollo rápido con Spring Security. |

### Ejemplos Prácticos

**Filtro Personalizado Estándar (el mismo código funciona en ambos):**
```java
@Component  // Solo para Spring Boot; en WAS declarar en web.xml
@Order(1)
public class LoggingFilter implements Filter {
    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
            throws IOException, ServletException {
        System.out.println("Solicitud: " + ((HttpServletRequest) req).getRequestURI());
        chain.doFilter(req, res);  // Crítico: pasa al siguiente filtro/servlet
    }
    // init/destroy...
}
```

**En Spring Boot (registrado automáticamente):**
Solo la clase de arriba + `@Component`.

**En WAS:**
Añadir en `web.xml`:
```xml
<filter>
    <filter-name>LoggingFilter</filter-name>
    <filter-class>com.example.LoggingFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>LoggingFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

### Cuándo Elegir Cuál
- **Usa filtros WAS** si estás en un entorno IBM heredado, necesitas funciones completas de Java EE o debes aplicar filtros globalmente en muchas aplicaciones sin cambios de código.
- **Usa filtros Spring Boot** (especialmente con Spring Security) para proyectos nuevos/desde cero, microservicios, iteración rápida, o cuando quieras múltiples cadenas de seguridad y ordenación fácil.

En resumen, el **concepto de filtro de cadena de solicitudes es el mismo** (especificación Servlet), pero **Spring Boot lo hace mucho más simple y potente** para la mayoría de los casos de uso modernos, mientras que WAS es más empresarial y intensivo en configuración.

[Documentación de Filtrado Servlet de IBM WAS](https://www.ibm.com/docs/en/was/9.0.5?topic=extensions-servlet-filtering)  
[Filtros Personalizados en Spring Boot](https://www.baeldung.com/spring-boot-add-filter)  
[Cadena de Filtros de Spring Security](https://docs.spring.io/spring-security/reference/servlet/architecture.html)