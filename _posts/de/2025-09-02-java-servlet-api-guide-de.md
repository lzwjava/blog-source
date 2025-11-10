---
audio: false
generated: true
image: false
lang: de
layout: post
title: Java Servlet API Leitfaden Grundlagen
translated: true
type: note
---

Hier ist eine praktische, end-to-end Anleitung zur Java **Servlet**-API im klassischen **`javax.servlet.*`**-Namespace (Servlet 2.x–4.x Ära). Ich werde auch erwähnen, was sich nach dem Wechsel zu **`jakarta.servlet.*`** geändert hat, damit Sie zukunftssicher sind.

# 1) Was ist ein Servlet?

Ein **Servlet** ist eine Java-Klasse, die in einem **Servlet-Container** (Tomcat, Jetty, WebSphere, WebLogic, etc.) läuft und HTTP-Anfragen/Antworten verarbeitet. Der Container verwaltet:

* Lebenszyklus (Laden, Init, Service, Zerstören)
* Multithreading und Request-Routing
* Sessions, Sicherheit, Ressourcen und Konfiguration

# 2) Kern-Packages & Wichtige Interfaces (javax.\*)

* `javax.servlet.Servlet`, `ServletConfig`, `ServletContext`
* `javax.servlet.http.HttpServlet`, `HttpServletRequest`, `HttpServletResponse`, `HttpSession`, `Cookie`
* `javax.servlet.Filter`, `FilterChain`, `FilterConfig`
* `javax.servlet.ServletRequestListener` und andere Listener
* `javax.servlet.annotation.*` (seit 3.0: `@WebServlet`, `@WebFilter`, `@WebListener`, `@MultipartConfig`)
* Seit 3.0: **Async** (`AsyncContext`), programmatische Registrierung
* Seit 3.1: **Non-blocking I/O** (`ServletInputStream`/`ServletOutputStream` mit `ReadListener`/`WriteListener`)
* Seit 4.0: HTTP/2 Support (z.B. `PushBuilder`)

> Jakarta-Wechsel: Ab **Servlet 5.0** (Jakarta EE 9) wurden die Packages in `jakarta.servlet.*` umbenannt. Die meisten APIs sind gleich; aktualisieren Sie Imports und Dependencies bei der Migration.

# 3) Servlet-Lebenszyklus & Threading-Modell

* **Laden**: Container lädt die Klasse, erstellt eine einzelne Instanz pro Deklaration.
* **`init(ServletConfig)`**: Einmal aufgerufen. Init-Parameter lesen, schwere Ressourcen cachen.
* **`service(req, res)`**: Pro Request aufgerufen. `HttpServlet` leitet an `doGet`, `doPost`, etc. weiter.
* **`destroy()`**: Einmal beim Herunterfahren/Neudeploy aufgerufen.

**Threading**: Der Container ruft `service` gleichzeitig auf derselben Instanz auf.
**Regel**: Vermeiden Sie veränderbare Instanzfelder; wenn nötig, verwenden Sie thread-sichere Strukturen oder ordentliche Synchronisation. Bevorzugen Sie lokale Variablen.

# 4) Minimales Servlet (Annotations)

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

# 5) `web.xml` vs Annotations

**Annotations (3.0+)** sind am einfachsten für einfache Apps.
**`web.xml`** ist immer noch nützlich für Reihenfolge, Overrides oder Legacy-Container.

Minimale `web.xml`:

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

# 6) Die HTTP Request/Response Grundlagen

## Request-Daten lesen

```java
String q = req.getParameter("q");        // Query-/Form-Feld
Enumeration<String> names = req.getParameterNames();
BufferedReader reader = req.getReader(); // Roher Body-Text
ServletInputStream in = req.getInputStream(); // Binärer Body
String header = req.getHeader("X-Token");
```

**Tipp**: Immer Encoding setzen, bevor Parameter gelesen werden:

```java
req.setCharacterEncoding("UTF-8");
```

## Responses schreiben

```java
resp.setStatus(HttpServletResponse.SC_OK);
resp.setContentType("application/json;charset=UTF-8");
resp.setHeader("Cache-Control", "no-store");
try (PrintWriter out = resp.getWriter()) {
  out.write("{\"ok\":true}");
}
```

# 7) doGet vs doPost vs andere

* `doGet`: Idempotente Lesevorgänge; Query-String verwenden.
* `doPost`: Erstellen/Aktualisieren mit Formular oder JSON-Body.
* `doPut`/`doDelete`/`doPatch`: RESTful-Semantik (Client muss unterstützen).
* Immer Inputs validieren und Content-Types explizit handhaben.

# 8) Sessions & Cookies

```java
HttpSession session = req.getSession(); // Erstellt falls abwesend
session.setAttribute("userId", 123L);
Long userId = (Long) session.getAttribute("userId");
session.invalidate(); // Logout
```

Session-Cookie-Flags via Container oder programmatisch konfigurieren:

* `HttpOnly` (Schutz vor JS), `Secure` (HTTPS), `SameSite=Lax/Strict`
  Ziehen Sie zustandslose Tokens für horizontale Skalierung in Betracht; sonst verwenden Sie Sticky Sessions oder externen Session-Store.

# 9) Filter (Cross-Cutting Concerns)

Verwenden Sie **Filter** für Logging, Auth, CORS, Kompression, Encoding, etc.

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
      req.getServletContext().log("Handled in " + ms + " ms");
    }
  }
}
```

# 10) Listener (App & Request Hooks)

Gängige Listener:

* `ServletContextListener`: App-Start/Shutdown (Pools initialisieren, Caches vorbereiten)
* `HttpSessionListener`: Session-Erstellung/Zerstörung (Metriken, Cleanup)
* `ServletRequestListener`: Per-Request-Hooks (Trace-IDs)

Beispiel:

```java
@WebListener
public class AppBoot implements javax.servlet.ServletContextListener {
  public void contextInitialized(javax.servlet.ServletContextEvent sce) {
    sce.getServletContext().log("App starting...");
  }
  public void contextDestroyed(javax.servlet.ServletContextEvent sce) {
    sce.getServletContext().log("App stopping...");
  }
}
```

# 11) Async & Non-Blocking I/O

## Async (Servlet 3.0)

Ermöglicht das Freigeben von Container-Threads, während ein Backend-Aufruf läuft.

```java
@WebServlet(urlPatterns="/async", asyncSupported=true)
public class AsyncDemo extends HttpServlet {
  protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
    AsyncContext ctx = req.startAsync();
    ctx.start(() -> {
      try {
        // call slow service...
        ctx.getResponse().getWriter().println("done");
      } catch (Exception e) {
        ctx.complete();
      } finally {
        ctx.complete();
      }
    });
  }
}
```

## Non-blocking (Servlet 3.1)

Registrieren Sie `ReadListener`/`WriteListener` auf den Streams für event-driven I/O. Nützlich für das Streamen großer Bodies ohne blockierende Threads.

# 12) Datei-Uploads (Multipart)

```java
import javax.servlet.annotation.MultipartConfig;

@MultipartConfig(maxFileSize = 10 * 1024 * 1024)
@WebServlet("/upload")
public class UploadServlet extends HttpServlet {
  protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException, ServletException {
    Part file = req.getPart("file");
    String filename = file.getSubmittedFileName();
    try (InputStream is = file.getInputStream()) {
      // save...
    }
    resp.getWriter().println("Uploaded " + filename);
  }
}
```

Stellen Sie sicher, dass der Client `Content-Type: multipart/form-data` sendet.

# 13) Dispatching & Templating

* **Forward**: Serverseitiger interner Dispatch; ursprüngliche URL bleibt.

  ```java
  req.getRequestDispatcher("/WEB-INF/view.jsp").forward(req, resp);
  ```
* **Include**: Ausgabe einer anderen Resource einbinden.

  ```java
  req.getRequestDispatcher("/fragment").include(req, resp);
  ```
* **Redirect**: Client 302/303/307 zu neuer URL.

  ```java
  resp.sendRedirect(req.getContextPath() + "/login");
  ```

# 14) Character Encoding & i18n

Ein kleiner **Encoding-Filter** verhindert Mojibake:

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

Verwenden Sie `Locale` von `HttpServletRequest#getLocale()` und Resource Bundles für i18n.

# 15) Sicherheitsgrundlagen

* **Transport**: Immer HTTPS; setzen Sie `Secure` Cookies.
* **Auth**: Container-gemanaged (FORM/BASIC/DIGEST), oder benutzerdefinierter Filter mit JWT/Session.
* **CSRF**: Generieren Sie pro-Session-Token; validieren Sie bei zustandsändernden Requests.
* **XSS**: HTML-escape Outputs; setzen Sie `Content-Security-Policy`.
* **Clickjacking**: `X-Frame-Options: DENY` oder CSP `frame-ancestors 'none'`.
* **CORS**: Header in einem Filter hinzufügen:

  ```java
  resp.setHeader("Access-Control-Allow-Origin", "https://example.com");
  resp.setHeader("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE");
  resp.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
  ```

# 16) Fehlerbehandlung

* Fehlerseiten in `web.xml` oder via Framework mappen:

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

* Im Code Statuscodes setzen und ein konsistentes JSON-Fehlschema für APIs rendern.

# 17) Logging & Observability

* Verwenden Sie `ServletContext#log`, oder besser: SLF4J + Logback/Log4j2.
* Fügen Sie eine Request-ID (UUID) in einem Filter hinzu; in Logs und Response-Headers aufnehmen.
* Health-Endpoints bereitstellen; via Filter/Servlet mit Prometheus integrieren.

# 18) Packaging & Deployment

**WAR-Layout**:

```
myapp/
  WEB-INF/
    web.xml
    classes/            # kompilierte .class-Dateien
    lib/                # Third-Party-Jars
  index.html
  static/...
```

Mit Maven/Gradle bauen, ein **WAR** produzieren, im Container `webapps` (Tomcat) oder via Admin-Konsole deployen. Für embedded Style verwenden Sie **Jetty** oder **Tomcat embedded** mit einem `main()`-Method, der den Server bootstrappt.

# 19) Servlets testen

* **Unit**: Mock `HttpServletRequest/Response`.

  * Spring’s `org.springframework.mock.web.*` ist bequem, auch ohne Spring.
  * Oder Mockito für eigene Stubs.
* **Integration**: Embedded Jetty/Tomcat starten und Endpoints mit HTTP-Client (REST Assured/HttpClient) anfragen.
* **End-to-End**: Browser-Automatisierung (Selenium/WebDriver) für vollständige Abläufe.

# 20) Performance-Tipps

* Wiederverwenden teurer Ressourcen (DB-Pools via `DataSource`); in `destroy()` aufräumen.
* Caching-Header für statische Inhalte setzen; statische Assets an Reverse-Proxy/CDN auslagern.
* GZIP-Kompression verwenden (Container-Einstellung oder ein Filter).
* Blockierende I/O für lange Operationen vermeiden; Async oder Queueing in Betracht ziehen.
* Allokationen und GC profilen; Responses für große Payloads streamen.

# 21) Häufige Fallstricke

* **Instanzfelder** nicht thread-safe → Race Conditions.
* `req.setCharacterEncoding("UTF-8")` vergessen, bevor Parameter gelesen werden.
* Den Body zweimal lesen ohne Buffering.
* Exceptions verschlucken ohne `5xx`-Status zu setzen.
* `getWriter()` und `getOutputStream()` in derselben Response mischen.

# 22) Von `javax.servlet.*` zu `jakarta.servlet.*`

Wenn Sie auf Jakarta EE 9+ upgraden:

* Ändern Sie Imports `javax.servlet.*` → `jakarta.servlet.*`.
* Verwenden Sie einen Container, der Jakarta unterstützt (Tomcat 10+, Jetty 11+).
* Neu bauen; die meisten Codeänderungen sind Import-Umbenennungen.
* Libraries müssen auch Jakarta-kompatibel sein (auf transitive Dependencies achten).

# 23) Minimales REST-style Beispiel

```java
@WebServlet(name="UsersApi", urlPatterns="/api/users/*")
public class UsersApi extends HttpServlet {
  @Override protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    resp.setContentType("application/json;charset=UTF-8");
    String id = pathParam(req, 1); // z.B. /api/users/42
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

# 24) Build Dependencies (klassisches `javax.servlet`)

**Provided** Scope in Maven, weil der Container die API zur Laufzeit bereitstellt:

```xml
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

Für **Jakarta**:

```xml
<dependency>
  <groupId>jakarta.servlet</groupId>
  <artifactId>jakarta.servlet-api</artifactId>
  <version>6.0.0</version>
  <scope>provided</scope>
</dependency>
```