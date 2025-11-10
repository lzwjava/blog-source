---
audio: false
generated: true
image: false
lang: ar
layout: post
title: خيارات تنفيذ سياق طلب سبرينغ
translated: true
type: note
---

حالة استخدام رائعة لـ"سياق الطلب" الصغير في Spring. لديك بعض الخيارات النظيفة — اختر واحدًا بناءً على مكدسك التقني:

### ١) فئة ذات نطاق طلب (بسيطة وآمنة)

قم بتخزين معرف مستخدم الاختبار في فئة ذات نطاق طلب يقوم `TestUserFilter` بتعيينها، ويمكن لأي مكون حقنها/قراءتها.

```java
// تحمل القيمة طوال مدة طلب HTTP واحد
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
    chain.doFilter(req, res); // يتم التنظيف التلقائي للفئة ذات نطاق الطلب بعد انتهاء الطلب
  }
}
```

استخدم في أي مكان:

```java
@Service
public class SomeService {
  private final TestUserContext ctx;
  public SomeService(TestUserContext ctx) { this.ctx = ctx; }
  public void doWork() {
    String testUserId = ctx.getUserId(); // null إذا لم يتم تقديمه
  }
}
```

**السبب:** لا حاجة للتنظيف اليدوي؛ يعمل عبر وحدات التحكم والخدمات وطبقات الوصول إلى البيانات ضمن نفس الطلب.

---

### ٢) سياق Spring Security (يُوصى به إذا كنت تستخدم Spring Security بالفعل)

دع الفلتر يقوم بتعيين `Authentication` حتى يتمكن جميع المكونات من قراءته عبر `SecurityContextHolder` أو `@AuthenticationPrincipal`.

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

استخدم في أي مكان:

```java
String testUserId = (String) SecurityContextHolder.getContext().getAuthentication().getPrincipal();
```

أو قم بحقن `Principal`/`Authentication` في وحدات التحكم.

**السبب:** يتكامل بشكل جيد مع أمان الطرق، والتقييد، والسجلات، إلخ.

---

### ٣) حامل ThreadLocal (يعمل بدون تبعيات ويب/أمان؛ تذكر المسح)

إذا كنت لا تستخدم نطاق الطلب أو Spring Security:

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
      TestUserHolder.clear(); // أمر حاسم للخيوط المجمعة
    }
  }
}
```

إذا كنت تقوم بمهام غير متزامنة وتحتاج إلى نشر القيمة، أضف `TaskDecorator` لنسخ الـ ThreadLocal.

---

### نصائح سريعة

* ضع المعرف في رأس مثل `X-Test-User-Id` (سهل التمرير من Postman أو MockMvc) أو في معلمة استعلام للاختبار المحلي.
* لاختبارات الوحدة مع MockMvc: `.header("X-Test-User-Id", "u123")`.
* **الخيار ١** مُفضل إذا كنت تريد "حقيبة" بسيطة مرئية لأي فئة ضمن نفس طلب HTTP.
* **الخيار ٢** مُفضل إذا كنت تستخدم Spring Security بالفعل أو تريد التكامل مع التفويض أو التقييد.
* استخدم **الخيار ٣** فقط عندما لا تريد استخدام نطاقات Spring أو أمانها؛ كن دقيقًا في عملية المسح لتجنب تسريبات الذاكرة.