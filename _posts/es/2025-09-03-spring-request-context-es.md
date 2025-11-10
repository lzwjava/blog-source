---
audio: false
generated: true
image: false
lang: es
layout: post
title: Opciones de Implementación del Contexto de Solicitud de Spring
translated: true
type: note
---

Excelente caso de uso para un pequeño "contexto de solicitud" en Spring. Tienes algunas opciones limpias—elige una según tu stack:

### 1) Bean con ámbito de solicitud (simple y seguro)

Almacena el ID de usuario de prueba en un bean con ámbito de solicitud que tu `TestUserFilter` establece, y cualquier componente puede inyectarlo/leerlo.

```java
// contiene el valor durante la vida útil de una única solicitud HTTP
@Component
@RequestScope
public class TestUserContext {
  private String userId;
  public String getUserId() { return userId; }
  public void setUserId(String userId) { this.userId = userId; }
}
```

```java
@Component
public class TestUserFilter extends OncePerRequestFilter {
  private final TestUserContext ctx;
  public TestUserFilter(TestUserContext ctx) { this.ctx = ctx; }

  @Override
  protected void doFilterInternal(HttpServletRequest req, HttpServletResponse res, FilterChain chain)
      throws ServletException, IOException {
    String id = req.getHeader("X-Test-User-Id");
    if (id == null) id = req.getParameter("testUserId");
    if (id != null && !id.isBlank()) ctx.setUserId(id);
    chain.doFilter(req, res); // el bean de ámbito de solicitud se limpia automáticamente después de que finaliza la solicitud
  }
}
```

Úsalo en cualquier lugar:

```java
@Service
public class SomeService {
  private final TestUserContext ctx;
  public SomeService(TestUserContext ctx) { this.ctx = ctx; }
  public void doWork() {
    String testUserId = ctx.getUserId(); // null si no se proporcionó
  }
}
```

**Por qué:** No requiere limpieza manual; funciona a través de controladores/servicios/DAOs dentro de la misma solicitud.

---

### 2) Contexto de Spring Security (recomendado si ya usas Spring Security)

Permite que el filtro establezca una `Authentication` para que todos los componentes puedan leerla via `SecurityContextHolder` o `@AuthenticationPrincipal`.

```java
@Component
public class TestUserFilter extends OncePerRequestFilter {
  @Override
  protected void doFilterInternal(HttpServletRequest req, HttpServletResponse res, FilterChain chain)
      throws IOException, ServletException {
    String id = req.getHeader("X-Test-User-Id");
    if (id == null) id = req.getParameter("testUserId");

    if (id != null && !id.isBlank()) {
      var auth = new UsernamePasswordAuthenticationToken(
          id, "N/A", List.of(new SimpleGrantedAuthority("ROLE_TEST")));
      SecurityContextHolder.getContext().setAuthentication(auth);
    }
    try {
      chain.doFilter(req, res);
    } finally {
      SecurityContextHolder.clearContext();
    }
  }
}
```

Úsalo en cualquier lugar:

```java
String testUserId = (String) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
```

o inyecta `Principal`/`Authentication` en los controladores.

**Por qué:** Funciona bien con seguridad a nivel de método, auditoría, logs, etc.

---

### 3) Contenedor ThreadLocal (funciona sin dependencias web/seguridad; recuerda limpiar)

Si no estás usando el ámbito de solicitud o Security:

```java
public final class TestUserHolder {
  private static final ThreadLocal<String> USER_ID = new InheritableThreadLocal<>();
  public static void set(String id) { USER_ID.set(id); }
  public static String get() { return USER_ID.get(); }
  public static void clear() { USER_ID.remove(); }
}
```

```java
@Component
public class TestUserFilter extends OncePerRequestFilter {
  @Override
  protected void doFilterInternal(HttpServletRequest req, HttpServletResponse res, FilterChain chain)
      throws IOException, ServletException {
    String id = req.getHeader("X-Test-User-Id");
    if (id == null) id = req.getParameter("testUserId");
    if (id != null && !id.isBlank()) TestUserHolder.set(id);
    try {
      chain.doFilter(req, res);
    } finally {
      TestUserHolder.clear(); // CRÍTICO para hilos agrupados (pooled threads)
    }
  }
}
```

Si ejecutas tareas asíncronas y necesitas propagación, añade un `TaskDecorator` para copiar el ThreadLocal.

---

### Consejos rápidos

* Coloca el ID en un header como `X-Test-User-Id` (fácil de pasar desde Postman/MockMvc) o en un query param para pruebas locales.
* Para pruebas unitarias con MockMvc: `.header("X-Test-User-Id", "u123")`.
* Prefiere la **Opción 1** si quieres una "bolsa" simple visible para cualquier bean en la misma solicitud HTTP.
* Prefiere la **Opción 2** si ya usas Spring Security o quieres integración con autorización/auditoría.
* Usa la **Opción 3** solo cuando no quieras ámbitos/seguridad de Spring; sé meticuloso con la limpieza para evitar fugas.