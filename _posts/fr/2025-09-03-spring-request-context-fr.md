---
audio: false
generated: true
image: false
lang: fr
layout: post
title: Options de mise en œuvre du contexte de requête Spring
translated: true
type: note
---

Excellente utilisation d'un "contexte de requête" léger dans Spring. Vous avez plusieurs options propres — choisissez celle qui correspond à votre stack :

### 1) Bean à portée de requête (simple et sûr)

Stockez l'identifiant de l'utilisateur de test dans un bean à portée de requête que votre `TestUserFilter` définit, et que n'importe quel composant peut injecter/lire.

```java
// conserve la valeur pour la durée de vie d'une seule requête HTTP
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
    chain.doFilter(req, res); // le bean à portée de requête est automatiquement nettoyé après la fin de la requête
  }
}
```

Utilisez-le n'importe où :

```java
@Service
public class SomeService {
  private final TestUserContext ctx;
  public SomeService(TestUserContext ctx) { this.ctx = ctx; }
  public void doWork() {
    String testUserId = ctx.getUserId(); // null si non fourni
  }
}
```

**Pourquoi :** Aucun nettoyage manuel ; fonctionne à travers les contrôleurs, services et DAOs au sein de la même requête.

---

### 2) Contexte Spring Security (recommandé si vous utilisez déjà Spring Security)

Laissez le filtre définir une `Authentication` afin que tous les composants puissent la lire via `SecurityContextHolder` ou `@AuthenticationPrincipal`.

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

Utilisez-le n'importe où :

```java
String testUserId = (String) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
```

ou injectez `Principal`/`Authentication` dans les contrôleurs.

**Pourquoi :** S'intègre bien avec la sécurité méthodique, l'audit, les logs, etc.

---

### 3) Holder ThreadLocal (fonctionne sans dépendances web/security ; pensez à le vider)

Si vous n'utilisez ni la portée de requête ni Security :

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
      TestUserHolder.clear(); // CRITIQUE pour les threads poolés
    }
  }
}
```

Si vous exécutez des tâches asynchrones et avez besoin de la propagation, ajoutez un `TaskDecorator` pour copier le ThreadLocal.

---

### Conseils rapides

* Placez l'identifiant dans un en-tête comme `X-Test-User-Id` (facile à passer depuis Postman/MockMvc) ou dans un paramètre de requête pour les tests locaux.
* Pour les tests unitaires avec MockMvc : `.header("X-Test-User-Id", "u123")`.
* Préférez l'**Option 1** si vous voulez un simple "sac" visible par n'importe quel bean dans la même requête HTTP.
* Préférez l'**Option 2** si vous utilisez déjà Spring Security ou si vous voulez une intégration avec l'autorisation/l'audit.
* Utilisez l'**Option 3** seulement quand vous ne voulez pas des portées Spring/security ; soyez méticuleux sur le vidage pour éviter les fuites.