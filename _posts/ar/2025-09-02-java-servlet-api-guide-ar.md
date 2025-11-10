---
audio: false
generated: true
image: false
lang: ar
layout: post
title: أساسيات دليل واجهة برمجة تطبيقات سيرفلت جافا
translated: true
type: note
---

إليك دليلًا عمليًا وشاملًا لواجهة برمجة تطبيقات **Servlet** في جافا ضمن النطاق الكلاسيكي **`javax.servlet.*`** (حقبة Servlet 2.x–4.x). سأذكر أيضًا ما الذي تغيّر بعد الانتقال إلى **`jakarta.servlet.*`** لتكون مستعدًا للمستقبل.

# 1) ما هو الـ Servlet؟

الـ **Servlet** هو فئة جافا تعمل داخل **حاوية Servlet** (مثل Tomcat، Jetty، WebSphere، WebLogic، إلخ) وتتعامل مع طلبات وردود HTTP. الحاوية تدير:

* دورة الحياة (التحميل، التهيئة init، الخدمة service، الإنهاء destroy)
* تعدد المسارات (Multithreading) وتوجيه الطلبات
* الجلسات، الأمان، الموارد، والإعدادات

# 2) الحزم الأساسية والواجهات الرئيسية (javax.\*)

* `javax.servlet.Servlet`, `ServletConfig`, `ServletContext`
* `javax.servlet.http.HttpServlet`, `HttpServletRequest`, `HttpServletResponse`, `HttpSession`, `Cookie`
* `javax.servlet.Filter`, `FilterChain`, `FilterConfig`
* `javax.servlet.ServletRequestListener` والمستمعين الآخرين
* `javax.servlet.annotation.*` (بدءًا من الإصدار 3.0: `@WebServlet`, `@WebFilter`, `@WebListener`, `@MultipartConfig`)
* بدءًا من الإصدار 3.0: **الغير متزامن (async)** (`AsyncContext`)، التسجيل البرمجي (programmatic registration)
* بدءًا من الإصدار 3.1: **الإدخال/الإخراج غير المعيق (non-blocking I/O)** (`ServletInputStream`/`ServletOutputStream` مع `ReadListener`/`WriteListener`)
* بدءًا من الإصدار 4.0: دعم HTTP/2 (مثل `PushBuilder`)

> الانتقال إلى Jakarta: بدءًا من **Servlet 5.0** (Jakarta EE 9)، تمت إعادة تسمية الحزم إلى `jakarta.servlet.*`. معظم واجهات برمجة التطبيقات (APIs) تبقى كما هي؛ قم بتحديث عبارات الاستيراد (imports) والتبعيات (dependencies) عند الترحيل.

# 3) دورة حياة الـ Servlet ونموذج المسارات (Threading)

* **التحميل**: تقوم الحاوية بتحميل الفئة، وإنشاء نسخة واحدة لكل تعريف.
* **`init(ServletConfig)`**: تُستدعى مرة واحدة. اقرأ معاملات التهيئة (init params)، واحتفظ بالموارد الثقيلة في الذاكرة المؤقتة (cache).
* **`service(req, res)`**: تُستدعى لكل طلب. يقوم `HttpServlet` بتفويض المهمة إلى `doGet`، `doPost`، إلخ.
* **`destroy()`**: تُستدعى مرة واحدة عند الإغلاق أو إعادة النشر.

**المسارات (Threading)**: تقوم الحاوية باستدعاء `service` بشكل متزامن (concurrently) على نفس النسخة.
**القاعدة**: تجنب الحقول (fields) القابلة للتغيير (mutable) على مستوى النسخة (instance fields)؛ إذا اضطررت لذلك، استخدم هياكل آمنة للمسارات (thread-safe) أو التزامن المناسب (proper synchronization). يُفضّل استخدام المتغيرات المحلية (locals).

# 4) Servlet بسيط (باستخدام التعليقات التوضيحية - annotations)

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

# 5) `web.xml` مقابل التعليقات التوضيحية (Annotations)

**التعليقات التوضيحية (3.0+)** هي الأسهل للتطبيقات البسيطة.
**`web.xml`** لا يزال مفيدًا للترتيب، التجاوز (overrides)، أو الحاويات القديمة (legacy containers).

`web.xml` بسيط:

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

# 6) أساسيات طلب ورد HTTP

## قراءة بيانات الطلب

```java
String q = req.getParameter("q");        // حقل استعلام أو نموذج (query/form field)
Enumeration<String> names = req.getParameterNames();
BufferedReader reader = req.getReader(); // نص الجسم الخام (raw body text)
ServletInputStream in = req.getInputStream(); // الجسم الثنائي (binary body)
String header = req.getHeader("X-Token");
```

**نصيحة**: ضع ترميز الأحرف (encoding) دائمًا قبل قراءة المعاملات (params):

```java
req.setCharacterEncoding("UTF-8");
```

## كتابة الردود

```java
resp.setStatus(HttpServletResponse.SC_OK);
resp.setContentType("application/json;charset=UTF-8");
resp.setHeader("Cache-Control", "no-store");
try (PrintWriter out = resp.getWriter()) {
  out.write("{\"ok\":true}");
}
```

# 7) doGet مقابل doPost مقابل غيرها

* `doGet`: عمليات قراءة لا تغير الحالة (idempotent)؛ استخدم سلسلة الاستعلام (query string).
* `doPost`: إنشاء/تحديث باستخدام نموذج (form) أو جسم JSON.
* `doPut`/`doDelete`/`doPatch`: دلالات RESTful (يجب أن يدعمها العميل - client).
* تحقق دائمًا من المدخلات (validate inputs) وتعامل مع أنواع المحتوى (content types) بشكل صريح.

# 8) الجلسات (Sessions) والكوكيز (Cookies)

```java
HttpSession session = req.getSession(); // ينشئ جلسة إذا لم تكن موجودة
session.setAttribute("userId", 123L);
Long userId = (Long) session.getAttribute("userId");
session.invalidate(); // تسجيل الخروج
```

قم بتكوين إعدادات كوكيز الجلسة عبر الحاوية أو برمجيًا:

* `HttpOnly` (للحماية من JavaScript)، `Secure` (لـ HTTPS)، `SameSite=Lax/Strict`
  فكر في استخدام الرموز (tokens) عديمة الحالة (stateless) للتوسع الأفقي (horizontal scaling)؛ وإلا فاستخدم جلسات مثبتة (sticky sessions) أو مخزن جلسات خارجي (external session store).

# 9) المرشحات (Filters) (الاهتمامات العابرة - cross-cutting concerns)

استخدم **المرشحات (Filters)** للتسجيل (logging)، المصادقة (auth)، CORS، الضغط (compression)، ترميز الأحرف (encoding)، إلخ.

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

# 10) المستمعون (Listeners) (خطافات التطبيق والطلب - app & request hooks)

الأشياء الشائعة:

* `ServletContextListener`: بدء/إيقاف التطبيق (مثل تهيئة مجمعات الاتصالات - init pools، تحضير الذاكرة المؤقتة - warm caches)
* `HttpSessionListener`: إنشاء/تدمير الجلسات (للقياسات - metrics، التنظيف)
* `ServletRequestListener`: خطافات لكل طلب (مثل معرفات التتبع - trace ids)

مثال:

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

# 11) الإدخال/الإخراج غير المتزامن (Async) وغير المعيق (Non-Blocking I/O)

## غير المتزامن (Async) (Servlet 3.0)

يسمح بتحرير مسارات (threads) الحاوية بينما تكون هناك مكالمة خلفية (backend call) قيد التشغيل.

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

## غير المعيق (Non-blocking) (Servlet 3.1)

سجل `ReadListener`/`WriteListener` على تدفقات البيانات (streams) للإدخال/الإخراج القائم على الأحداث (event-driven I/O). مفيد لبث (streaming) أجسام الطلبات الكبيرة دون عرقلة المسارات (blocking threads).

# 12) رفع الملفات (Multipart)

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

تأكد من أن العميل (client) يرسل `Content-Type: multipart/form-data`.

# 13) التوجيه (Dispatching) والقوالب (Templating)

* **التوجيه (Forward)**: توجيه داخلي من جانب الخادم؛ يبقى عنوان URL الأصلي.

  ```java
  req.getRequestDispatcher("/WEB-INF/view.jsp").forward(req, resp);
  ```
* **الإدراج (Include)**: إدراج مخرجات مورد آخر.

  ```java
  req.getRequestDispatcher("/fragment").include(req, resp);
  ```
* **إعادة التوجيه (Redirect)**: إعادة توجيه العميل برمز 302/303/307 إلى عنوان URL جديد.

  ```java
  resp.sendRedirect(req.getContextPath() + "/login");
  ```

# 14) ترميز الأحرف (Character Encoding) والتوطين (i18n)

**مرشح ترميز (encoding filter)** بسيط يمنع حدوث فوضى في الأحرف (mojibake):

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

استخدم `Locale` من `HttpServletRequest#getLocale()` وحزم الموارد (resource bundles) للتوطين (i18n).

# 15) أساسيات الأمان

* **النقل (Transport)**: استخدم دائمًا HTTPS؛ عيّن كوكيز `Secure`.
* **المصادقة (Auth)**: إما مدعومة من الحاوية (FORM/BASIC/DIGEST)، أو مرشح مخصص (custom filter) باستخدام JWT/جلسة.
* **CSRF**: أنشئ رمزًا (token) لكل جلسة (per-session)； تحقق منه في الطلبات التي تغير الحالة (state-changing requests).
* **XSS**: اهرب من (escape) مخرجات HTML؛ عيّن `Content-Security-Policy`.
* **التصيد بالنقر (Clickjacking)**: `X-Frame-Options: DENY` أو CSP `frame-ancestors 'none'`.
* **CORS**: أضف العناوين في مرشح:

  ```java
  resp.setHeader("Access-Control-Allow-Origin", "https://example.com");
  resp.setHeader("Access-Control-Allow-Methods", "GET,POST,PUT,DELETE");
  resp.setHeader("Access-Control-Allow-Headers", "Content-Type, Authorization");
  ```

# 16) معالجة الأخطاء

* اربط صفحات الأخطاء في `web.xml` أو عبر إطار العمل (framework):

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

* في الكود، عيّن رموز الحالة (status codes) وقم بعرض مخطط (schema) خطأ JSON متناسق لواجهات برمجة التطبيقات (APIs).

# 17) التسجيل (Logging) والمراقبة (Observability)

* استخدم `ServletContext#log`، أو الأفضل: SLF4J + Logback/Log4j2.
* أضف معرف طلب (request-ID) (مثل UUID) في مرشح؛ قم بتضمينه في سجلات النظام (logs) وعناوين الاستجابة (response headers).
* اعرض نقاط نهاية الصحة (health endpoints)؛ ادمج مع Prometheus عبر مرشح أو servlet.

# 18) التغليف (Packaging) والنشر (Deployment)

**هيكل WAR**:

```
myapp/
  WEB-INF/
    web.xml
    classes/            # ملفات .class المترجمة
    lib/                # ملفات jar الطرف الثالث
  index.html
  static/...
```

ابنِ باستخدام Maven/Gradle، أنتج **WAR**، وانشره في مجلد `webapps` الخاص بالحاوية (Tomcat) أو عبر وحدة التحكم الإدارية (admin console). لأسلوب المضمن (embedded style)، استخدم **Jetty** أو **Tomcat المضمن (embedded)** مع دالة `main()` تقوم بتهيئة الخادم (bootstrapping the server).

# 19) اختبار Servlets

* **اختبار الوحدة (Unit)**: استخدم محاكاة (mock) لـ `HttpServletRequest/Response`.

  * `org.springframework.mock.web.*` التابع لـ Spring مناسب حتى بدون استخدام Spring.
  * أو استخدم Mockito لإنشاء استعلاماتك الخاصة (stubs).
* **اختبار التكامل (Integration)**: ابدأ بـ Jetty/Tomcat المضمن واختر نقاط النهاية (endpoints) باستخدام عميل HTTP (مثل REST Assured/HttpClient).
* **اختبار من البداية للنهاية (End-to-End)**: أتمتة المتصفح (مثل Selenium/WebDriver) للمسارات الكاملة (full flows).

# 20) نصائح الأداء

* أعد استخدام الموارد مكلفة الإنشاء (مثل مجمعات قواعد البيانات - DB pools عبر `DataSource`)؛ نظفها في `destroy()`.
* عيّن عناوين التخزين المؤقت (caching headers) للمحتوى الثابت (static content)؛ فوّض الأصول الثابتة (static assets) إلى خادم وكيل عكسي (reverse proxy) أو شبكة توصيل المحتوى (CDN).
* استخدم ضغط GZIP (إعداد في الحاوية أو عبر مرشح).
* تجنب الإدخال/الإخراج المعيق (blocking I/O) للعمليات الطويلة؛ فكر في استخدام غير المتزامن (async) أو الطابور (queueing).
* حلل تخصيص الذاكرة (allocations) وجامع القمامة (GC)؛ حافظ على تدفق الردود (streaming responses) للحِمل الكبير (large payloads).

# 21) الأخطاء الشائعة

* **الحقول على مستوى النسخة (Instance fields)** ليست آمنة للمسارات (thread-safe) → تؤدي إلى ظروف التنافس (race conditions).
* نسيان `req.setCharacterEncoding("UTF-8")` قبل قراءة المعاملات (params).
* قراءة جسم الطلب (body) مرتين دون استخدام الذاكرة المؤقتة (buffering).
* كبت (swallowing) الاستثناءات (exceptions) دون تعيين حالة `5xx`.
* خلط استخدام `getWriter()` و `getOutputStream()` في نفس الرد.

# 22) من `javax.servlet.*` إلى `jakarta.servlet.*`

إذا قمت بالترقية إلى Jakarta EE 9+:

* غيّر عبارات الاستيراد (imports) من `javax.servlet.*` → `jakarta.servlet.*`.
* استخدم حاوية تدعم Jakarta (Tomcat 10+, Jetty 11+).
* أعد البناء (Rebuild)؛ معظم تغييرات الكود هي إعادة تسمية لعبارات الاستيراد.
* يجب أن تكون المكتبات (Libraries) متوافقة مع Jakarta أيضًا (انتبه للتبعيات المتسلسلة - transitive dependencies).

# 23) مثال بسيط على نمط REST

```java
@WebServlet(name="UsersApi", urlPatterns="/api/users/*")
public class UsersApi extends HttpServlet {
  @Override protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
    resp.setContentType("application/json;charset=UTF-8");
    String id = pathParam(req, 1); // e.g. /api/users/42
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

# 24) تبعيات البناء (لـ `javax.servlet` الكلاسيكي)

نطاق **Provided** في Maven لأن الحاوية توفر واجهة برمجة التطبيقات (API) في وقت التشغيل:

```xml
<dependency>
  <groupId>javax.servlet</groupId>
  <artifactId>javax.servlet-api</artifactId>
  <version>4.0.1</version>
  <scope>provided</scope>
</dependency>
```

لـ **Jakarta**:

```xml
<dependency>
  <groupId>jakarta.servlet</groupId>
  <artifactId>jakarta.servlet-api</artifactId>
  <version>6.0.0</version>
  <scope>provided</scope>
</dependency>
```

---

إذا أخبرتني بالحاوية المستهدفة (Tomcat/Jetty/Liberty)، وإصدار جافا، وما إذا كنت تريد الإدخال/الإخراج المتزامن (synchronous)، أو غير المتزامن (async)، أو غير المعيق (non-blocking I/O)، يمكنني رسم هيكل جاهز للإنتاج (production-ready skeleton) مخصص لمكدسك (stack) (يشمل التسجيل، CORS، عناوين الأمان، وتخطيط Maven/Gradle نظيف) — دون جداول، فقط كود وخطوات مركزة.