---
audio: false
generated: true
image: false
lang: es
layout: post
title: Guía Esencial de la API de Servlets de Java
translated: true
type: note
---

Aquí tienes una guía práctica y completa sobre la API **Servlet** de Java en el espacio de nombres clásico **`javax.servlet.*`** (era Servlet 2.x–4.x). También mencionaré lo que cambió después del cambio a **`jakarta.servlet.*`** para que estés preparado para el futuro.

# 1) ¿Qué es un Servlet?

Un **Servlet** es una clase Java que se ejecuta dentro de un **contenedor de Servlets** (Tomcat, Jetty, WebSphere, WebLogic, etc.) y maneja peticiones y respuestas HTTP. El contenedor gestiona:

* El ciclo de vida (carga, init, service, destroy)
* La multihilos y el enrutamiento de peticiones
* Las sesiones, seguridad, recursos y configuración

# 2) Paquetes Principales e Interfaces Clave (javax.\*)

* `javax.servlet.Servlet`, `ServletConfig`, `ServletContext`
* `javax.servlet.http.HttpServlet`, `HttpServletRequest`, `HttpServletResponse`, `HttpSession`, `Cookie`
* `javax.servlet.Filter`, `FilterChain`, `FilterConfig`
* `javax.servlet.ServletRequestListener` y otros listeners
* `javax.servlet.annotation.*` (desde 3.0: `@WebServlet`, `@WebFilter`, `@WebListener`, `@MultipartConfig`)
* Desde 3.0: **async** (`AsyncContext`), registro programático
* Desde 3.1: **E/S no bloqueante** (`ServletInputStream`/`ServletOutputStream` con `ReadListener`/`WriteListener`)
* Desde 4.0: soporte para HTTP/2 (ej., `PushBuilder`)

> Cambio a Jakarta: a partir de **Servlet 5.0** (Jakarta EE 9), los paquetes se renombraron a `jakarta.servlet.*`. La mayoría de las APIs son las mismas; actualiza las importaciones y dependencias al migrar.

# 3) Ciclo de Vida del Servlet y Modelo de Hilos

* **Carga**: El contenedor carga la clase, crea una única instancia por declaración.
* **`init(ServletConfig)`**: Se llama una vez. Lee parámetros de inicialización, almacena en caché recursos pesados.
* **`service(req, res)`**: Se llama por petición. `HttpServlet` deriva a `doGet`, `doPost`, etc.
* **`destroy()`**: Se llama una vez al apagar/redesplegar.

**Hilos**: El contenedor llama a `service` concurrentemente en la misma instancia.
**Regla**: Evita campos de instancia mutables; si es necesario, usa estructuras seguras para hilos o sincronización adecuada. Prefiere variables locales.

# 4) Servlet Mínimo (anotaciones)

```java
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.*;
import javax.servlet.ServletException;
import java.io.IOException;

@WebServlet(name = "HelloServlet", urlPatterns = "/hello")
public class HelloServlet extends HttpServlet {
  @Override protected void doGet(HttpServletRequest req, HttpServletResponse resp)
      throws ServletException, IOException {
    resp.setContentType("text/plain;charset=UTF-8");
    resp.getWriter().println("Hello, Servlet!");
  }
}
```

# 5) `web.xml` vs Anotaciones

Las **anotaciones (3.0+)** son más fáciles para aplicaciones simples.
**`web.xml`** sigue siendo útil para orden, anulaciones o contenedores legacy.

`web.xml` mínimo:

```xml
<web-app xmlns="http://java.sun.com/xml/ns/javaee" version="3.0">
  <servlet>
    <servlet-name>HelloServlet</servlet-name>
    <servlet-class>com.example.HelloServlet</servlet-class>
    <init-param>
      <param-name>greeting</param-name>
      <param-value>Hi</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
  </servlet>
  <servlet-mapping>
    <servlet-name>HelloServlet</servlet-name>
    <url-pattern>/hello</url-pattern>
  </servlet-mapping>
</web-app>
```

# 6) Lo Esencial de la Petición/Respuesta HTTP

## Leyendo datos de la petición

```java
String q = req.getParameter("q");        // campo de consulta/formulario
Enumeration<String> names = req.getParameterNames();
BufferedReader reader = req.getReader(); // cuerpo en texto plano
ServletInputStream in = req.getInputStream(); // cuerpo binario
String header = req.getHeader("X-Token");
```

**Consejo**: Establece siempre la codificación antes de leer parámetros:

```java
req.setCharacterEncoding("UTF-8");
```

## Escribiendo respuestas

```java
resp.setStatus(HttpServletResponse.SC_OK);
resp.setContentType("application/json;charset=UTF-8");
resp.setHeader("Cache-Control", "no-store");
try (PrintWriter out = resp.getWriter()) {
  out.write("{\"ok\":true}");
}
```

# 7) doGet vs doPost vs otros

* `doGet`: lecturas idempotentes; usa cadena de consulta.
* `doPost`: crear/actualizar con cuerpo de formulario o JSON.
* `doPut`/`doDelete`/`doPatch`: semántica RESTful (el cliente debe soportarlo).
* Valida siempre las entradas y maneja los tipos de contenido explícitamente.

# 8) Sesiones y Cookies

```java
HttpSession session = req.getSession(); // crea si está ausente
session.setAttribute("userId", 123L);
Long userId = (Long) session.getAttribute("userId");
session.invalidate(); // cerrar sesión
```

Configura las flags de la cookie de sesión mediante el contenedor o programáticamente:

* `HttpOnly` (protege de JS), `Secure` (HTTPS), `SameSite=Lax/Strict`
  Considera tokens sin estado para escalado horizontal; si no, usa sesiones sticky o almacén de sesiones externo.

# 9) Filtros (preocupaciones transversales)

Usa **Filtros** para logging, autenticación, CORS, compresión, codificación, etc.

```java
import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import java.io.IOException;

@WebFilter(urlPatterns = "/*")
public class LoggingFilter implements Filter {
  public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
      throws IOException, ServletException {
    long start = System.nanoTime();
    try {
      chain.doFilter(req, res);
    } finally {
      long ms = (System.nanoTime() - start) / 1_000_000;
      req.getServletContext().log("Manejado en " + ms + " ms");
    }
  }
}
```

# 10) Listeners (ganchos de aplicación y petición)

Los más comunes:

* `ServletContextListener`: inicio/parada de la aplicación (inicializar pools, calentar cachés)
* `HttpSessionListener`: crear/destruir sesiones (métricas, limpieza)
* `ServletRequestListener`: ganchos por petición (ids de traza)

Ejemplo:

```java
@WebListener
public class AppBoot implements javax.servlet.ServletContextListener {
  public void contextInitialized(javax.servlet.ServletContextEvent sce) {
    sce.getServletContext().log("Iniciando aplicación...");
  }
  public void contextDestroyed(javax.servlet.ServletContextEvent sce) {
    sce.getServletContext().log("Parando aplicación...");
  }
}
```

# 11) E/S Asíncrona y No Bloqueante

## Asíncrono (Servlet 3.0)

Permite liberar hilos del contenedor mientras se ejecuta una llamada de backend.

```java
@WebServlet(urlPatterns="/async", asyncSupported=true)
public class AsyncDemo extends HttpServlet {
  protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
    AsyncContext ctx = req.startAsync();
    ctx.start(() -> {
      try {
        // llamar a servicio lento...
        ctx.getResponse().getWriter().println("hecho");
      } catch (Exception e) {
        ctx.complete();
      } finally {
        ctx.complete();
      }
    });
  }
}
```

## No bloqueante (Servlet 3.1)

Registra `ReadListener`/`WriteListener` en los flujos para E/S dirigida por eventos. Útil para transmitir cuerpos grandes sin bloquear hilos.

# 12) Subida de Archivos (Multipart)

```java
import javax.servlet.annotation.MultipartConfig;

@MultipartConfig(maxFileSize = 10 * 1024 * 1024)
@WebServlet("/upload")
public class UploadServlet extends HttpServlet {
  protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException, ServletException {
    Part file = req.getPart("file");
    String filename = file.getSubmittedFileName();
    try (InputStream is = file.getInputStream()) {
      // guardar...
    }
    resp.getWriter().println("Subido " + filename);
  }
}
```

Asegúrate de que el cliente envíe `Content-Type: multipart/form-data`.

# 13) Despacho y Plantillas

* **Forward**: despacho interno del lado del servidor; la URL original permanece.

  ```java
  req.getRequestDispatcher("/WEB-INF/view.jsp").forward(req, resp);
  ```
* **Include**: incluir la salida de otro recurso.

  ```java
  req.getRequestDispatcher("/fragment").include(req, resp);
  ```
* **Redirect**: cliente 302/303/307 a nueva URL.

  ```java
  resp.sendRedirect(req.getContextPath() + "/login");
  ```

# 14) Codificación de Caracteres e i18n

Un pequeño **filtro de codificación** evita el mojibake:

```java
@WebFilter("/*")
public class Utf8Filter implements Filter {
  public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
      throws IOException, ServletException {
    req.setCharacterEncoding("UTF-8");
    res.setCharacterEncoding("UTF-8");
    chain.doFilter(req, res);
  }
}
```

Usa `Locale` de `HttpServletRequest#getLocale()` y paquetes de recursos para i18n.

# 15) Conceptos Básicos de Seguridad

* **Transporte**: siempre HTTPS; establece cookies `Secure`.
* **Autenticación**: gestionada por el contenedor (FORM/BASIC/DIGEST), o filtro personalizado con JWT/sesión.
* **CSRF**: genera token por sesión; valida en peticiones que cambian el estado.
* **XSS**: escapa salidas HTML; establece `Content-Security-Policy`.
* **Clickjacking**: `X-Frame-Options: DENY` o CSP `frame-ancestors 'none'`.
* **CORS**: añade cabeceras en un filtro:

  ```java
  resp.setHeader("Access-Control-Allow-Origin", "https://example.com");
  resp.setHeader("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE");
  resp.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
  ```

# 16) Manejo de Errores

* Mapea páginas de error en `web.xml` o mediante el framework:

```xml
<error-page>
  <error-code>404</error-code>
  <location>/WEB-INF/errors/404.jsp</location>
</error-page>
<error-page>
  <exception-type>java.lang.Throwable</exception-type>
  <location>/WEB-INF/errors/500.jsp</location>
</error-page>
```

* En el código, establece códigos de estado y renderiza un esquema de error JSON consistente para las APIs.

# 17) Logging y Observabilidad

* Usa `ServletContext#log`, o mejor: SLF4J + Logback/Log4j2.
* Añade un ID de petición (UUID) en un filtro; inclúyelo en los logs y las cabeceras de respuesta.
* Expone endpoints de salud; integra con Prometheus mediante un filtro/servlet.

# 18) Empaquetado y Despliegue

**Estructura WAR**:

```
myapp/
  WEB-INF/
    web.xml
    classes/            # archivos .class compilados
    lib/                # jars de terceros
  index.html
  static/...
```

Compila con Maven/Gradle, produce un **WAR**, despliega en `webapps` del contenedor (Tomcat) o mediante consola de administración. Para estilo embebido, usa **Jetty** o **Tomcat embebido** con un `main()` que arranque el servidor.

# 19) Probando Servlets

* **Unitarias**: simula `HttpServletRequest/Response`.

  * `org.springframework.mock.web.*` de Spring es conveniente incluso sin Spring.
  * O crea tus stubs con Mockito.
* **Integración**: inicia Jetty/Tomcat embebido y accede a los endpoints con un cliente HTTP (REST Assured/HttpClient).
* **End-to-End**: automatización del navegador (Selenium/WebDriver) para flujos completos.

# 20) Consejos de Rendimiento

* Reutiliza recursos costosos (pools de BD via `DataSource`); límpialos en `destroy()`.
* Establece cabeceras de caché para contenido estático; descarga activos estáticos a un proxy inverso/CDN.
* Usa compresión GZIP (configuración del contenedor o un filtro).
* Evita E/S bloqueante para operaciones largas; considera async o colas.
* Perfila asignaciones y GC; mantén las respuestas en streaming para cargas útiles grandes.

# 21) Errores Comunes

* **Campos de instancia** no seguros para hilos → condiciones de carrera.
* Olvidar `req.setCharacterEncoding("UTF-8")` antes de leer parámetros.
* Leer el cuerpo dos veces sin buffering.
* Tragar excepciones sin establecer estado `5xx`.
* Mezclar `getWriter()` y `getOutputStream()` en la misma respuesta.

# 22) De `javax.servlet.*` a `jakarta.servlet.*`

Si actualizas a Jakarta EE 9+:

* Cambia las importaciones `javax.servlet.*` → `jakarta.servlet.*`.
* Usa un contenedor que soporte Jakarta (Tomcat 10+, Jetty 11+).
* Recompila; la mayoría de los cambios de código son renombrados de importaciones.
* Las librerías también deben ser compatibles con Jakarta (cuidado con las dependencias transitivas).

# 23) Ejemplo Mínimo Estilo REST

```java
@WebServlet(name="UsersApi", urlPatterns="/api/users/*")
public class UsersApi extends HttpServlet {
  @Override protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    resp.setContentType("application/json;charset=UTF-8");
    String id = pathParam(req, 1); // ej. /api/users/42
    if (id == null) {
      resp.getWriter().write("[{\"id\":1,\"name\":\"A\"}]");
    } else {
      resp.getWriter().write("{\"id\":"+id+",\"name\":\"A\"}");
    }
  }
  private String pathParam(HttpServletRequest req, int idx) {
    String path = req.getPathInfo();        // "/42"
    if (path == null) return null;
    String[] parts = path.split("/");
    return parts.length > idx ? parts[idx] : null;
  }
}
```

# 24) Dependencias de Construcción (clásico `javax.servlet`)

Scope **Provided** en Maven porque el contenedor suministra la API en tiempo de ejecución:

```xml
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

Para **Jakarta**:

```xml
<dependency>
  <groupId>jakarta.servlet</groupId>
  <artifactId>jakarta.servlet-api</artifactId>
  <version>6.0.0</version>
  <scope>provided</scope>
</dependency>
```

---

Si me indicas tu contenedor objetivo (Tomcat/Jetty/Liberty), versión de Java, y si quieres E/S síncrona, asíncrona o no bloqueante, puedo esbozar un esqueleto listo para producción adaptado a tu stack (logging, CORS, cabeceras de seguridad, y un diseño Maven/Gradle limpio) — sin tablas, solo código conciso y pasos.