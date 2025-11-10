---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Guide essentiel de l'API Servlet Java
translated: true
type: note
---

Voici un guide pratique et complet de l'API Java **Servlet** dans l'espace de noms classique **`javax.servlet.*`** (ère Servlet 2.x–4.x). Je noterai également ce qui a changé après le passage à **`jakarta.servlet.*`** pour que vous soyez prêt pour l'avenir.

# 1) Qu'est-ce qu'une Servlet ?

Une **Servlet** est une classe Java qui s'exécute à l'intérieur d'un **conteneur de Servlets** (Tomcat, Jetty, WebSphere, WebLogic, etc.) et gère les requêtes/réponses HTTP. Le conteneur gère :

* Le cycle de vie (chargement, init, service, destroy)
* Le multithreading et le routage des requêtes
* Les sessions, la sécurité, les ressources et la configuration

# 2) Packages principaux & Interfaces clés (javax.\*)

* `javax.servlet.Servlet`, `ServletConfig`, `ServletContext`
* `javax.servlet.http.HttpServlet`, `HttpServletRequest`, `HttpServletResponse`, `HttpSession`, `Cookie`
* `javax.servlet.Filter`, `FilterChain`, `FilterConfig`
* `javax.servlet.ServletRequestListener` et autres écouteurs
* `javax.servlet.annotation.*` (depuis 3.0 : `@WebServlet`, `@WebFilter`, `@WebListener`, `@MultipartConfig`)
* Depuis 3.0 : **async** (`AsyncContext`), enregistrement programmatique
* Depuis 3.1 : **E/S non bloquantes** (`ServletInputStream`/`ServletOutputStream` avec `ReadListener`/`WriteListener`)
* Depuis 4.0 : support HTTP/2 (ex: `PushBuilder`)

> Changement Jakarta : à partir de **Servlet 5.0** (Jakarta EE 9), les packages ont été renommés en `jakarta.servlet.*`. La plupart des API sont identiques ; mettez à jour les imports et les dépendances lors de la migration.

# 3) Cycle de vie de la Servlet & Modèle de Threading

* **Charger** : Le conteneur charge la classe, crée une seule instance par déclaration.
* **`init(ServletConfig)`** : Appelée une fois. Lire les paramètres d'initialisation, mettre en cache les ressources lourdes.
* **`service(req, res)`** : Appelée par requête. `HttpServlet` distribue vers `doGet`, `doPost`, etc.
* **`destroy()`** : Appelée une fois lors de l'arrêt/redéploiement.

**Threading** : Le conteneur appelle `service` concurremment sur la même instance.
**Règle** : Évitez les champs d'instance mutables ; si nécessaire, utilisez des structures thread-safe ou une synchronisation appropriée. Préférez les variables locales.

# 4) Servlet minimale (annotations)

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

Les **Annotations (3.0+)** sont plus faciles pour les applications simples.
**`web.xml`** reste utile pour l'ordre, les remplacements ou les conteneurs legacy.

`web.xml` minimal :

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

# 6) Les essentiels de la Requête/Réponse HTTP

## Lire les données de la requête

```java
String q = req.getParameter("q");        // champ query/form
Enumeration<String> names = req.getParameterNames();
BufferedReader reader = req.getReader(); // corps texte brut
ServletInputStream in = req.getInputStream(); // corps binaire
String header = req.getHeader("X-Token");
```

**Astuce** : Toujours définir l'encodage avant de lire les paramètres :

```java
req.setCharacterEncoding("UTF-8");
```

## Écrire les réponses

```java
resp.setStatus(HttpServletResponse.SC_OK);
resp.setContentType("application/json;charset=UTF-8");
resp.setHeader("Cache-Control", "no-store");
try (PrintWriter out = resp.getWriter()) {
  out.write("{\"ok\":true}");
}
```

# 7) doGet vs doPost vs autres

* `doGet` : lectures idempotentes ; utiliser la chaîne de requête.
* `doPost` : créer/mettre à jour avec un corps de formulaire ou JSON.
* `doPut`/`doDelete`/`doPatch` : sémantique RESTful (le client doit le supporter).
* Toujours valider les entrées et gérer les types de contenu explicitement.

# 8) Sessions & Cookies

```java
HttpSession session = req.getSession(); // crée si absent
session.setAttribute("userId", 123L);
Long userId = (Long) session.getAttribute("userId");
session.invalidate(); // déconnexion
```

Configurer les flags des cookies de session via le conteneur ou programmatiquement :

* `HttpOnly` (protège de JS), `Secure` (HTTPS), `SameSite=Lax/Strict`
  Envisagez des tokens sans état pour la mise à l'échelle horizontale ; sinon, utilisez des sessions collantes ou un stockage de session externe.

# 9) Filtres (préoccupations transversales)

Utilisez les **Filtres** pour la journalisation, l'authentification, CORS, la compression, l'encodage, etc.

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
      req.getServletContext().log("Traité en " + ms + " ms");
    }
  }
}
```

# 10) Écouteurs (hooks d'application et de requête)

Les plus courants :

* `ServletContextListener` : démarrage/arrêt de l'application (initialiser les pools, préchauffer les caches)
* `HttpSessionListener` : création/destruction de sessions (métriques, nettoyage)
* `ServletRequestListener` : hooks par requête (ids de traçage)

Exemple :

```java
@WebListener
public class AppBoot implements javax.servlet.ServletContextListener {
  public void contextInitialized(javax.servlet.ServletContextEvent sce) {
    sce.getServletContext().log("Démarrage de l'application...");
  }
  public void contextDestroyed(javax.servlet.ServletContextEvent sce) {
    sce.getServletContext().log("Arrêt de l'application...");
  }
}
```

# 11) Async & E/S Non-Bloquantes

## Async (Servlet 3.0)

Permet de libérer les threads du conteneur pendant l'exécution d'un appel backend.

```java
@WebServlet(urlPatterns="/async", asyncSupported=true)
public class AsyncDemo extends HttpServlet {
  protected void doGet(HttpServletRequest req, HttpServletResponse resp) {
    AsyncContext ctx = req.startAsync();
    ctx.start(() -> {
      try {
        // appeler un service lent...
        ctx.getResponse().getWriter().println("terminé");
      } catch (Exception e) {
        ctx.complete();
      } finally {
        ctx.complete();
      }
    });
  }
}
```

## Non-bloquant (Servlet 3.1)

Enregistrez `ReadListener`/`WriteListener` sur les flux pour des E/S événementielles. Utile pour diffuser des corps de grande taille sans bloquer les threads.

# 12) Téléchargement de Fichiers (Multipart)

```java
import javax.servlet.annotation.MultipartConfig;

@MultipartConfig(maxFileSize = 10 * 1024 * 1024)
@WebServlet("/upload")
public class UploadServlet extends HttpServlet {
  protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException, ServletException {
    Part file = req.getPart("file");
    String filename = file.getSubmittedFileName();
    try (InputStream is = file.getInputStream()) {
      // sauvegarder...
    }
    resp.getWriter().println("Téléchargé " + filename);
  }
}
```

Assurez-vous que le client envoie `Content-Type: multipart/form-data`.

# 13) Dispatch & Templating

* **Forward** : dispatch interne côté serveur ; l'URL originale reste.

  ```java
  req.getRequestDispatcher("/WEB-INF/view.jsp").forward(req, resp);
  ```
* **Include** : inclut la sortie d'une autre ressource.

  ```java
  req.getRequestDispatcher("/fragment").include(req, resp);
  ```
* **Redirect** : client 302/303/307 vers une nouvelle URL.

  ```java
  resp.sendRedirect(req.getContextPath() + "/login");
  ```

# 14) Encodage des Caractères & i18n

Un petit **filtre d'encodage** évite le mojibake :

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

Utilisez `Locale` depuis `HttpServletRequest#getLocale()` et les Resource Bundles pour l'i18n.

# 15) Bases de la Sécurité

* **Transport** : toujours HTTPS ; définir les cookies `Secure`.
* **Auth** : gérée par le conteneur (FORM/BASIC/DIGEST), ou filtre personnalisé avec JWT/session.
* **CSRF** : générer un token par session ; valider sur les requêtes modifiant l'état.
* **XSS** : échapper les sorties HTML ; définir `Content-Security-Policy`.
* **Clickjacking** : `X-Frame-Options: DENY` ou CSP `frame-ancestors 'none'`.
* **CORS** : ajouter les en-têtes dans un filtre :

  ```java
  resp.setHeader("Access-Control-Allow-Origin", "https://example.com");
  resp.setHeader("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE");
  resp.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
  ```

# 16) Gestion des Erreurs

* Mapper les pages d'erreur dans `web.xml` ou via le framework :

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

* Dans le code, définir les codes de statut et rendre un schéma d'erreur JSON cohérent pour les APIs.

# 17) Journalisation & Observabilité

* Utilisez `ServletContext#log`, ou mieux : SLF4J + Logback/Log4j2.
* Ajoutez un ID de requête (UUID) dans un filtre ; incluez-le dans les logs et les en-têtes de réponse.
* Exposez des endpoints de santé ; intégrez avec Prometheus via un filtre/servlet.

# 18) Empaquetage & Déploiement

**Structure WAR** :

```
myapp/
  WEB-INF/
    web.xml
    classes/            # fichiers .class compilés
    lib/                # jars tiers
  index.html
  static/...
```

Construisez avec Maven/Gradle, produisez un **WAR**, déployez dans le répertoire `webapps` du conteneur (Tomcat) ou via la console d'administration. Pour un style embarqué, utilisez **Jetty** ou **Tomcat embarqué** avec une `main()` amorçant le serveur.

# 19) Tester les Servlets

* **Unité** : simulez `HttpServletRequest/Response`.

  * `org.springframework.mock.web.*` de Spring est pratique même sans Spring.
  * Ou créez vos propres stubs avec Mockito.
* **Intégration** : démarrez Jetty/Tomcat embarqué et appelez les endpoints avec un client HTTP (REST Assured/HttpClient).
* **End-to-End** : automatisation du navigateur (Selenium/WebDriver) pour les flux complets.

# 20) Conseils de Performance

* Réutilisez les ressources coûteuses (pools de DB via `DataSource`) ; nettoyez dans `destroy()`.
* Définissez les en-têtes de cache pour le contenu statique ; externalisez les assets statiques vers un reverse proxy/CDN.
* Utilisez la compression GZIP (paramètre du conteneur ou un filtre).
* Évitez les E/S bloquantes pour les opérations longues ; envisagez l'async ou la mise en file d'attente.
* Profilez les allocations et le GC ; gardez les réponses en streaming pour les charges utiles volumineuses.

# 21) Pièges Courants

* **Champs d'instance** non thread-safe → conditions de course.
* Oublier `req.setCharacterEncoding("UTF-8")` avant de lire les paramètres.
* Lire le corps deux fois sans mise en mémoire tampon.
* Absorber les exceptions sans définir le statut `5xx`.
* Mélanger `getWriter()` et `getOutputStream()` dans la même réponse.

# 22) De `javax.servlet.*` à `jakarta.servlet.*`

Si/vous mettez à niveau vers Jakarta EE 9+ :

* Changez les imports `javax.servlet.*` → `jakarta.servlet.*`.
* Utilisez un conteneur qui supporte Jakarta (Tomcat 10+, Jetty 11+).
* Recompilez ; la plupart des changements de code sont des renommages d'imports.
* Les bibliothèques doivent aussi être compatibles Jakarta (surveillez les dépendances transitives).

# 23) Exemple Minimal de style REST

```java
@WebServlet(name="UsersApi", urlPatterns="/api/users/*")
public class UsersApi extends HttpServlet {
  @Override protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    resp.setContentType("application/json;charset=UTF-8");
    String id = pathParam(req, 1); // ex: /api/users/42
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

# 24) Dépendances de Build (`javax.servlet` classique)

Scope **Provided** dans Maven car le conteneur fournit l'API à l'exécution :

```xml
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

Pour **Jakarta** :

```xml
<dependency>
  <groupId>jakarta.servlet</groupId>
  <artifactId>jakarta.servlet-api</artifactId>
  <version>6.0.0</version>
  <scope>provided</scope>
</dependency>
```

---

Si vous me dites votre conteneur cible (Tomcat/Jetty/Liberty), votre version de Java, et si vous voulez des E/S synchrones, async ou non bloquantes, je peux esquisser un squelette prêt pour la production adapté à votre stack (journalisation, CORS, en-têtes de sécurité, et une structure Maven/Gradle propre) — pas de tableaux, juste du code concis et des étapes.