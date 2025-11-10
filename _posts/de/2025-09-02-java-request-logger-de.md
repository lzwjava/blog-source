---
audio: false
generated: true
image: false
lang: de
layout: post
title: Java-Anfragen-Wrapper für die Protokollierung
translated: true
type: note
---

In Java-Webanwendungen verwenden Sie typischerweise einen **`HttpServletRequestWrapper`**, wenn Sie das Verhalten der standardmäßigen `HttpServletRequest` dekorieren oder modifizieren möchten, ohne die Implementierung des Servlet-Containers zu verändern.

### Wie `HttpServletRequestWrapper` funktioniert

* Es handelt sich um einen **Dekorierer** (Decorator) um die ursprüngliche `HttpServletRequest`.
* Sie erstellen eine Unterklasse von `HttpServletRequestWrapper` und überschreiben Methoden wie `getInputStream()`, `getReader()` oder `getParameter()`.
* Dies ist nützlich, wenn Sie den **Request-Body lesen oder zwischenspeichern** möchten (der standardmäßig nur einmal gelesen werden kann) oder Request-Parameter modifizieren/abfragen möchten.

### Warum man ihn für Logging benötigt

* Standardmäßig kann der Servlet-Request-Body (`InputStream`) nur einmal konsumiert werden. Wenn Sie ihn direkt in einem Filter loggen, kann der Controller ihn anschließend nicht mehr lesen.
* Durch das Wrappen können Sie den **Body zwischenspeichern**, sodass er mehrfach gelesen werden kann: einmal für das Logging und einmal für die weitere Verarbeitung.
* URL-Parameter können durch Aufruf von `request.getParameterMap()` oder `request.getQueryString()` geloggt werden.

---

### Beispiel: Logging von Body und URL-Parametern

Hier ist ein Filter, der einen benutzerdefinierten Wrapper verwendet:

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

Verwenden Sie ihn dann in einem Filter:

```java
@WebFilter("/*")
public class LoggingFilter implements Filter {
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {

        CachedBodyHttpServletRequest wrappedRequest = new CachedBodyHttpServletRequest((HttpServletRequest) request);

        // URL loggen
        String url = wrappedRequest.getRequestURL().toString();
        String query = wrappedRequest.getQueryString();

        // Parameter loggen
        Map<String, String[]> params = wrappedRequest.getParameterMap();

        // Body loggen
        String body = wrappedRequest.getBody();

        System.out.println("Request URL: " + url + (query != null ? "?" + query : ""));
        System.out.println("Parameters: " + params);
        System.out.println("Body: " + body);

        // Filterkette fortsetzen
        chain.doFilter(wrappedRequest, response);
    }
}
```

---

### Wichtige Punkte

* **`HttpServletRequestWrapper`** ermöglicht es Ihnen, den Body sicher mehrfach zu lesen.
* Für URL-Parameter reichen `getParameterMap()` oder `getQueryString()` aus.
* Seien Sie vorsichtig bei **großen Bodys** (hier möchten Sie vielleicht Streaming oder Größenbeschränkungen verwenden).
* Verwenden Sie in Produktionsumgebungen ein Logging-Framework (SLF4J + Logback/Log4J2) anstelle von `System.out`.

---

Möchten Sie, dass ich Ihnen auch eine **Spring Boot–artige Lösung** zeige (unter Verwendung von `OncePerRequestFilter` und `ContentCachingRequestWrapper`), da diese viel einfacher ist?