---
audio: false
generated: true
image: false
lang: es
layout: post
title: Contenedor de Solicitud Java para Registro
translated: true
type: note
---

En aplicaciones web Java, normalmente usas un **`HttpServletRequestWrapper`** cuando quieres decorar o modificar el comportamiento del `HttpServletRequest` estándar sin tocar la implementación del contenedor de servlets.

### Cómo funciona `HttpServletRequestWrapper`

* Es un **decorador** que envuelve el `HttpServletRequest` original.
* Creas una subclase de `HttpServletRequestWrapper` y sobrescribes métodos como `getInputStream()`, `getReader()`, o `getParameter()`.
* Esto es útil cuando quieres **leer o almacenar en caché el cuerpo de la solicitud** (que por defecto solo se puede leer una vez) o modificar/consultar parámetros de la solicitud.

### Por qué lo necesitas para el registro (logging)

* Por defecto, el cuerpo de la solicitud del servlet (`InputStream`) solo se puede consumir una vez. Si lo registras directamente en un filtro, el controlador no podrá leerlo después.
* Envolver la solicitud te permite **almacenar en caché el cuerpo** para que pueda leerse múltiples veces: una para el registro y otra para el procesamiento posterior.
* Los parámetros de la URL se pueden registrar accediendo a `request.getParameterMap()` o `request.getQueryString()`.

---

### Ejemplo: Registrar el cuerpo y los parámetros de la URL

Aquí hay un filtro que usa un wrapper personalizado:

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

Luego úsalo en un filtro:

```java
@WebFilter("/*")
public class LoggingFilter implements Filter {
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {

        CachedBodyHttpServletRequest wrappedRequest = new CachedBodyHttpServletRequest((HttpServletRequest) request);

        // Registrar URL
        String url = wrappedRequest.getRequestURL().toString();
        String query = wrappedRequest.getQueryString();

        // Registrar parámetros
        Map<String, String[]> params = wrappedRequest.getParameterMap();

        // Registrar cuerpo
        String body = wrappedRequest.getBody();

        System.out.println("Request URL: " + url + (query != null ? "?" + query : ""));
        System.out.println("Parameters: " + params);
        System.out.println("Body: " + body);

        // Continuar la cadena de filtros
        chain.doFilter(wrappedRequest, response);
    }
}
```

---

### Puntos Clave

* **`HttpServletRequestWrapper`** te permite leer el cuerpo de forma segura múltiples veces.
* Para los parámetros de la URL: `getParameterMap()` o `getQueryString()` es suficiente.
* Ten cuidado con **cuerpos de solicitud grandes** (puedes querer usar streaming o límites de tamaño).
* En producción, usa un framework de logging (SLF4J + Logback/Log4J2) en lugar de `System.out`.

---

¿Quieres que también te muestre una solución al estilo **Spring Boot** (usando `OncePerRequestFilter` y `ContentCachingRequestWrapper`), ya que es mucho más simple?