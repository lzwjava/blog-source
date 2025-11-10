---
audio: false
generated: true
image: false
lang: de
layout: post
title: Implementierungsoptionen für den Spring Request Context
translated: true
type: note
---

Hervorragender Anwendungsfall für einen kleinen "Request Context" in Spring. Sie haben einige saubere Optionen – wählen Sie eine basierend auf Ihrem Stack:

### 1) Request-scoped Bean (einfach & sicher)

Speichern Sie die Testbenutzer-ID in einer Request-scoped Bean, die Ihr `TestUserFilter` setzt und die jede Komponente injizieren/lesen kann.

```java
// Hält den Wert für die Lebensdauer einer einzelnen HTTP-Anfrage
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
    chain.doFilter(req, res); // Request-scope Bean wird automatisch nach Ende der Anfrage bereinigt
  }
}
```

Verwendung überall:

```java
@Service
public class SomeService {
  private final TestUserContext ctx;
  public SomeService(TestUserContext ctx) { this.ctx = ctx; }
  public void doWork() {
    String testUserId = ctx.getUserId(); // null, falls nicht angegeben
  }
}
```

**Warum:** Keine manuelle Bereinigung; funktioniert übergreifend in Controllern, Services und DAOs innerhalb derselben Anfrage.

---

### 2) Spring Security Context (empfohlen, falls Sie bereits Spring Security verwenden)

Lassen Sie den Filter eine `Authentication` setzen, damit alle Komponenten sie über `SecurityContextHolder` oder `@AuthenticationPrincipal` lesen können.

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

Verwendung überall:

```java
String testUserId = (String) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
```

oder injizieren Sie `Principal`/`Authentication` in Controller.

**Warum:** Funktioniert gut mit Method Security, Auditing, Logs etc.

---

### 3) ThreadLocal Holder (funktioniert ohne Web/Security Abhängigkeiten; unbedingt bereinigen)

Falls Sie Request Scope oder Security nicht verwenden:

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
      TestUserHolder.clear(); // KRITISCH für gepoolte Threads
    }
  }
}
```

Falls Sie asynchrone Tasks ausführen und Propagation benötigen, fügen Sie einen `TaskDecorator` hinzu, um das ThreadLocal zu kopieren.

---

### Kurze Tipps

*   Legen Sie die ID in einen Header wie `X-Test-User-Id` (einfach von Postman/MockMvc aus zu übergeben) oder einen Query Parameter für lokale Tests.
*   Für Unit-Tests mit MockMvc: `.header("X-Test-User-Id", "u123")`.
*   Bevorzugen Sie **Option 1**, wenn Sie einen einfachen "Behälter" möchten, der für jede Bean in derselben HTTP-Anfrage sichtbar ist.
*   Bevorzugen Sie **Option 2**, wenn Sie bereits Spring Security verwenden oder eine Integration in Authorization/Auditing wünschen.
*   Verwenden Sie **Option 3** nur, wenn Sie keine Spring Scopes/Security verwenden möchten; seien Sie akribisch bei der Bereinigung, um Leaks zu vermeiden.