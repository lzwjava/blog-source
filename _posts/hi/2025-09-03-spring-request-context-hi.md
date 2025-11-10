---
audio: false
generated: true
image: false
lang: hi
layout: post
title: वसंत अनुरोध संदर्भ कार्यान्वयन विकल्प
translated: true
type: note
---

Spring में एक छोटे "request context" के लिए बेहतरीन use-case। आपके पास कुछ साफ विकल्प हैं—अपने stack के आधार पर एक चुनें:

### 1) Request-scoped bean (सरल और सुरक्षित)

Test user id को एक request-scoped bean में संग्रहीत करें जिसे आपका `TestUserFilter` सेट करे, और कोई भी component इसे inject/read कर सकता है।

```java
// एक single HTTP request के lifetime के लिए value रखता है
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
    chain.doFilter(req, res); // request-scope bean request समाप्त होने के बाद auto-cleaned हो जाती है
  }
}
```

कहीं भी उपयोग करें:

```java
@Service
public class SomeService {
  private final TestUserContext ctx;
  public SomeService(TestUserContext ctx) { this.ctx = ctx; }
  public void doWork() {
    String testUserId = ctx.getUserId(); // null अगर प्रदान नहीं किया गया
  }
}
```

**क्यों:** कोई manual cleanup नहीं; एक ही request के भीतर controllers/services/DAOs में काम करता है।

---

### 2) Spring Security context (अनुशंसित यदि आप पहले से Spring Security का उपयोग करते हैं)

Filter एक `Authentication` सेट करे ताकि सभी components इसे `SecurityContextHolder` या `@AuthenticationPrincipal` के माध्यम से read कर सकें।

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

कहीं भी उपयोग करें:

```java
String testUserId = (String) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
```

या controllers में `Principal`/`Authentication` inject करें।

**क्यों:** method security, auditing, logs आदि के साथ अच्छी तरह से काम करता है।

---

### 3) ThreadLocal holder (web/security dependencies के बिना काम करता है; clear करना याद रखें)

यदि आप request scope या Security का उपयोग नहीं कर रहे हैं:

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
      TestUserHolder.clear(); // pooled threads के लिए CRITICAL
    }
  }
}
```

यदि आप async tasks चलाते हैं और propagation की आवश्यकता है, तो ThreadLocal को copy करने के लिए एक `TaskDecorator` जोड़ें।

---

### Quick tips

* Id को `X-Test-User-Id` जैसे header में रखें (Postman/MockMvc से pass करना आसान) या local testing के लिए एक query parameter में।
* MockMvc के साथ unit tests के लिए: `.header("X-Test-User-Id", "u123")`।
* **विकल्प 1** को प्राथमिकता दें यदि आप एक ही HTTP request में किसी भी bean के लिए दिखाई देने वाला एक सरल "bag" चाहते हैं।
* **विकल्प 2** को प्राथमिकता दें यदि आप पहले से ही Spring Security का उपयोग करते हैं या authorization/auditing integration चाहते हैं।
* **विकल्प 3** का उपयोग केवल तभी करें जब आप Spring scopes/security नहीं चाहते हैं; leaks से बचने के लिए clearing के प्रति सतर्क रहें।