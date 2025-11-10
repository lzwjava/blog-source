---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Encapsuleur de Requête Java pour la Journalisation
translated: true
type: note
---

Dans les applications web Java, on utilise généralement un **`HttpServletRequestWrapper`** lorsqu'on souhaite décorer ou modifier le comportement de la `HttpServletRequest` standard sans toucher à l'implémentation du conteneur de servlets.

### Fonctionnement de `HttpServletRequestWrapper`

* C'est un **décorateur** autour de la `HttpServletRequest` originale.
* Vous créez une sous-classe de `HttpServletRequestWrapper` et vous redéfinissez des méthodes comme `getInputStream()`, `getReader()`, ou `getParameter()`.
* Ceci est utile lorsque vous souhaitez **lire ou mettre en cache le corps de la requête** (qui par défaut ne peut être lu qu'une seule fois) ou modifier/interroger les paramètres de la requête.

### Pourquoi il est nécessaire pour la journalisation

* Par défaut, le corps de la requête servlet (`InputStream`) ne peut être consommé qu'une seule fois. Si vous le journalisez directement dans un filtre, le contrôleur ne pourra plus le lire ensuite.
* L'encapsulation permet de **mettre en cache le corps** afin qu'il puisse être lu plusieurs fois : une fois pour la journalisation, une fois pour le traitement en aval.
* Les paramètres d'URL peuvent être journalisés en accédant à `request.getParameterMap()` ou `request.getQueryString()`.

---

### Exemple : Journalisation du corps et des paramètres d'URL

Voici un filtre utilisant un wrapper personnalisé :

```java
public class CachedBodyHttpServletRequest extends HttpServletRequestWrapper {
    private byte[] cachedBody;

    public CachedBodyHttpServletRequest(HttpServletRequest request) throws IOException {
        super(request);
        InputStream requestInputStream = request.getInputStream();
        this.cachedBody = requestInputStream.readAllBytes();
    }

    @Override
    public ServletInputStream getInputStream() {
        ByteArrayInputStream byteArrayInputStream = new ByteArrayInputStream(this.cachedBody);
        return new ServletInputStream() {
            @Override
            public int read() {
                return byteArrayInputStream.read();
            }
            @Override
            public boolean isFinished() {
                return byteArrayInputStream.available() == 0;
            }
            @Override
            public boolean isReady() {
                return true;
            }
            @Override
            public void setReadListener(ReadListener readListener) {}
        };
    }

    @Override
    public BufferedReader getReader() {
        return new BufferedReader(new InputStreamReader(this.getInputStream()));
    }

    public String getBody() {
        return new String(this.cachedBody, StandardCharsets.UTF_8);
    }
}
```

Puis utilisez-le dans un filtre :

```java
@WebFilter("/*")
public class LoggingFilter implements Filter {
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {

        CachedBodyHttpServletRequest wrappedRequest = new CachedBodyHttpServletRequest((HttpServletRequest) request);

        // Journaliser l'URL
        String url = wrappedRequest.getRequestURL().toString();
        String query = wrappedRequest.getQueryString();

        // Journaliser les paramètres
        Map<String, String[]> params = wrappedRequest.getParameterMap();

        // Journaliser le corps
        String body = wrappedRequest.getBody();

        System.out.println("Request URL: " + url + (query != null ? "?" + query : ""));
        System.out.println("Parameters: " + params);
        System.out.println("Body: " + body);

        // Poursuivre la chaîne de filtres
        chain.doFilter(wrappedRequest, response);
    }
}
```

---

### Points Clés

* **`HttpServletRequestWrapper`** permet de lire le corps en toute sécurité plusieurs fois.
* Pour les paramètres d'URL : `getParameterMap()` ou `getQueryString()` suffit.
* Soyez prudent avec les **corps de grande taille** (vous pouvez envisager le streaming ou des limites de taille).
* En production, utilisez un framework de journalisation (SLF4J + Logback/Log4J2) au lieu de `System.out`.

---

Souhaitez-vous que je vous montre également une solution de type **Spring Boot** (utilisant `OncePerRequestFilter` et `ContentCachingRequestWrapper`), car elle est beaucoup plus simple ?