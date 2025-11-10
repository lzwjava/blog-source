---
audio: false
generated: true
image: false
lang: ar
layout: post
title: غلاف طلب جافا للتسجيل
translated: true
type: note
---

في تطبيقات Java الويب، تستخدم عادةً **`HttpServletRequestWrapper`** عندما تريد تزيين أو تعديل سلوك `HttpServletRequest` القياسي دون المساس بتنفيذ حاوية الخدمة (servlet container).

### كيف تعمل `HttpServletRequestWrapper`

* إنها **أداة تزيين (decorator)** تغلف `HttpServletRequest` الأصلي.
* تقوم بإنشاء فئة فرعية من `HttpServletRequestWrapper وتجاوز طرق مثل `getInputStream()`, `getReader()`, أو `getParameter()`.
* هذا مفيد عندما تريد **قراءة أو تخزين جسم الطلب** (والذي يمكن قراءته مرة واحدة فقط بشكل افتراضي) أو تعديل/الاستعلام عن معلمات الطلب.

### لماذا تحتاجها للتسجيل (Logging)

* بشكل افتراضي، يمكن استهلاك جسم طلب الخدمة (`InputStream`) مرة واحدة فقط. إذا قمت بتسجيله مباشرة في مرشح (filter)، فل يتمكن المتحكم (controller) من قراءته لاحقًا.
* يسمح التغليف لك **بتخزين الجسم** مؤقتًا بحيث يمكن قراءته عدة مرات: مرة للتسجيل ومرة للمعالجة اللاحقة.
* يمكن تسجيل معلمات URL عن طريق الوصول إلى `request.getParameterMap()` أو `request.getQueryString()`.

---

### مثال: تسجيل الجسم ومعلمات URL

إليك مرشحًا يستخدم غلافًا مخصصًا:

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

ثم استخدمه في مرشح:

```java
@WebFilter("/*")
public class LoggingFilter implements Filter {
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {

        CachedBodyHttpServletRequest wrappedRequest = new CachedBodyHttpServletRequest((HttpServletRequest) request);

        // تسجيل URL
        String url = wrappedRequest.getRequestURL().toString();
        String query = wrappedRequest.getQueryString();

        // تسجيل المعلمات
        Map<String, String[]> params = wrappedRequest.getParameterMap();

        // تسجيل الجسم
        String body = wrappedRequest.getBody();

        System.out.println("Request URL: " + url + (query != null ? "?" + query : ""));
        System.out.println("Parameters: " + params);
        System.out.println("Body: " + body);

        // متابعة سلسلة المرشحات
        chain.doFilter(wrappedRequest, response);
    }
}
```

---

### النقاط الرئيسية

* **`HttpServletRequestWrapper`** تتيح لك قراءة الجسم عدة مرات بأمان.
* بالنسبة لمعلمات URL: `getParameterMap()` أو `getQueryString()` كافٍ.
* كن حذرًا مع **الأجسام كبيرة الحجم** (قد ترغب في استخدام التدفق (streaming) أو تحديد حدود الحجم).
* في بيئة الإنتاج، استخدم إطار عمل للتسجيل (مثل SLF4J + Logback/Log4J2) بدلاً من `System.out`.

---

هل تريد مني أيضًا أن أعرض لك **حلاً على نمط Spring Boot** (باستخدام `OncePerRequestFilter` و `ContentCachingRequestWrapper`)، نظرًا لأنه أبسط بكثير؟