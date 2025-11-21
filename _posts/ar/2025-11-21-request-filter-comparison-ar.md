---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4.1-fast
title: 'مقارنة مرشح الطلبات: ويب سبير مقابل سبرينغ بوت'
translated: true
type: note
---

### نظرة عامة
كل من IBM WebSphere Application Server (WAS، التقليدي أو Liberty) و Spring Boot يدعمان مفهوم **سلسلة معالجة الطلبات** بناءً على واجهة برمجة تطبيقات Java Servlet القياسية `javax.servlet.Filter` و `FilterChain`. هنا تمر طلبات HTTP الواردة عبر سلسلة من المرشحات قبل الوصول إلى الخدمات (servlets) (أو وحدات التحكم/المعالجات)، ويمكن تعديل الاستجابات أثناء طريق العودة.

- تسمح المرشحات بالمعالجة المسبقة (مثل المصادقة، التسجيل، الضغط) والمعالجة اللاحقة للطلبات/الاستجابات.
- الآلية الأساسية — تنفيذ `Filter`، استدعاء `chain.doFilter(request, response)` للمتابعة — **متماثلة** لأن كليهما يعمل في حاوية Servlet (WAS لديها حاوية ويب Java EE كاملة خاصة بها؛ Spring Boot تضمّن Tomcat/Jetty/Undertow افتراضيًا).

لا يوجد فرق جوهري في كيفية عمل "مرشح سلسلة الطلبات" الأساسي. ومع ذلك، فإن طريقة تكوين وترتيب ودمج المرشحات تختلف بشكل كبير بسبب بنية كل منصة.

### مقارنة رئيسية

| الجانب                  | IBM WebSphere Application Server (تقليدي/Liberty) | Spring Boot |
|-------------------------|---------------------------------------------------------|-------------|
| **الآلية الأساسية** | مرشحات Servlet قياسية (`javax.servlet.Filter`). لدى WAS أيضًا امتدادات خاصة مثل `ChainedRequest`/`ChainedResponse` لإعادة توجيه/ربط الطلبات الداخلي في بعض السيناريوهات (مثل البوابة أو واجهات برمجة تطبيقات IBM المخصصة). | مرشحات Servlet قياسية. Spring Boot يسجل تلقائيًا أي مرشح مُعلّم بـ `@Component` أو يمكنك التسجيل explicitly عبر `FilterRegistrationBean`. |
| **التكوين**       | أساسيًا عبر `web.xml` (تصريحي) أو التسجيل البرمجي. للمرشحات العامة (عبر جميع التطبيقات): معقد — يتطلب مكتبات مشتركة، مستمعين مخصصين، أو امتدادات خاصة بـ IBM (لا يوجد ملف web.xml بسيط على مستوى الخادم مثل Tomcat). | الاتفاقية فوق التكوين: علّم بـ `@Component` + `@Order` للتسجيل التلقائي، أو استخدم `FilterRegistrationBean` للتحكم الدقيق (أنماط URL، أنواع المُرسِل). سهل الاستخدام للمطورين. |
| **الترتيب**            | مُعرّف في ترتيب `web.xml` أو عبر `@Order` إذا كان برمجيًا. الترتيب العام صعب. | سهل باستخدام `@Order(n)` (رقم أقل = تنفيذ أبكر) أو واجهة `Ordered`. Spring Boot يدير السلسلة تلقائيًا. |
| **سلسلة مرشحات الأمان** | يستخدم مرشحات Servlet قياسية أو أمان خاص بـ IBM (مثل TAI، أدوار JEE). لا توجد سلسلة أمان مدمجة مثل Spring Security. | Spring Security يوفر `SecurityFilterChain` قوي (عبر `FilterChainProxy`) بأكثر من 15 مرشح مرتبة (CSRF، المصادقة، إدارة الجلسة، إلخ). قابل للتخصيص بدرجة عالية مع سلاسل متعددة لكل مسار. |
| **سهولة إضافة مرشحات مخصصة** | أكثر تفصيلاً، خاصة للمرشحات العامة/عبر التطبيقات. غالبًا ما يتطلب تعديلات عبر وحدة تحكم المسؤول أو مكتبات مشتركة. | بسيط للغاية — مجرد حبة `@Component` أو فئة تكوين. يتم دمجها تلقائيًا في الحاوية المضمنة. |
| **نموذج النشر**    | خادم Java EE كامل تقليدي. التطبيقات تُنشر كـ WAR/EAR. يدعم ميزات enterprise متقدمة (التجميع، المعاملات، JMS). | حاوية مضمنة (قابل للتنفيذ JAR قائم بذاته افتراضيًا). يمكن نشره كـ WAR إلى خوادم خارجية (بما في ذلك WAS). خفيف الوزن/موجه نحو الخدمات المصغرة. |
| **الأداء/الحمل الزائد**| حمل زائد أعلى (خادم تطبيقات كامل). سلاسل النقل، قنوات حاوية الويب تضيف طبقات. | حمل زائد أقل (حاوية خفيفة الوزن مضمنة). بدء أسرع، استخدام أقل للموارد. |
| **متى يتم تشغيل المرشحات**     | في السلسلة الواردة لحاوية ويب WAS. يمكن أن يكون هناك مرشحات نقل على مستوى الخادم (مثل ترشيح IP على قنوات TCP). | في سلسلة مرشحات الحاوية المضمنة. Spring Boot يضيف مرشحاته الخاصة (معالجة الأخطاء، ترميز الأحرف، إلخ). |
| **حالات الاستخدام الشائعة**    | تطبيقات enterprise الضخمة، البوابات، تطبيقات Java EE القديمة التي تحتاج إلى أمان/تسجيل عام. | الخدمات المصغرة الحديثة، واجهات برمجة تطبيقات REST، التطوير السريع مع Spring Security. |

### أمثلة عملية

**مرشح مخصص قياسي (نفس الكود يعمل في كليهما):**
```java
@Component  // Spring Boot فقط؛ في WAS عرّفه في web.xml
@Order(1)
public class LoggingFilter implements Filter {
    public void doFilter(ServletRequest req, ServletResponse res, FilterChain chain)
            throws IOException, ServletException {
        System.out.println("Request: " + ((HttpServletRequest) req).getRequestURI());
        chain.doFilter(req, res);  // حاسم: يمرر إلى المرشح/الخدمة التالي
    }
    // init/destroy...
}
```

**في Spring Boot (مسجل تلقائيًا):**
فقط الفئة أعلاه + `@Component`.

**في WAS:**
أضف في `web.xml`:
```xml
<filter>
    <filter-name>LoggingFilter</filter-name>
    <filter-class>com.example.LoggingFilter</filter-class>
</filter>
<filter-mapping>
    <filter-name>LoggingFilter</filter-name>
    <url-pattern>/*</url-pattern>
</filter-mapping>
```

### متى تختار أيهما
- **استخدم مرشحات WAS** إذا كنت في بيئة IBM قديمة، أو تحتاج إلى ميزات Java EE كاملة، أو يجب تطبيق مرشحات بشكل عام عبر العديد من التطبيقات دون تغييرات في الكود.
- **استخدم مرشحات Spring Boot** (خاصة مع Spring Security) للمشاريع الجديدة، أو الخدمات المصغرة، أو التكرار السريع، أو عندما تريد سلاسل أمان متعددة وترتيبًا سهلًا.

باختصار، **مفهوم مرشح سلسلة الطلبات هو نفسه** (مواصفات Servlet)، لكن **Spring Boot يجعله أبسط وأقوى بكثير** لمعظم حالات الاستخدام الحديثة، بينما WAS أكثر ثقلاً وتوجهًا لبيئات enterprise وأكثر كثافة في التكوين.

[توثيق ترشيح Servlet لـ IBM WAS](https://www.ibm.com/docs/en/was/9.0.5?topic=extensions-servlet-filtering)  
[مرشحات مخصصة في Spring Boot](https://www.baeldung.com/spring-boot-add-filter)  
[سلسلة مرشحات Spring Security](https://docs.spring.io/spring-security/reference/servlet/architecture.html)