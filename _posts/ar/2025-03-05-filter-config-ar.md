---
audio: false
generated: true
lang: ar
layout: post
title: تهيئة المرشح في سرفلات جافا
translated: true
type: note
---

### كيف يعمل `javax.servlet.FilterConfig`؟

في تطبيقات الويب التي تم بناؤها باستخدام Servlet API في جافا، تلعب واجهة `javax.servlet.FilterConfig` دورًا رئيسيًا في تكوين المرشحات (Filters). المرشحات هي مكونات تعترض وتعالج طلبات واستجابات HTTP قبل أن تصل إلى Servlet أو بعد مغادرتها لها. يوفر `FilterConfig` طريقة قياسية لتمرير معلومات التكوين إلى المرشح عندما يتم تهيئته بواسطة حاوية الويب (مثل Tomcat أو Jetty). أدناه، سأشرح كيف يعمل `FilterConfig`، والغرض منه، وكيفية استخدامه.

---

#### **ما هو `FilterConfig`؟**
`FilterConfig` هي واجهة في حزمة `javax.servlet`. تستخدمها حاوية الويب لتزويد المرشح ببيانات التكوين خلال مرحلة التهيئة الخاصة به. عندما يتم تعريف مرشح في تطبيق ويب (عبر `web.xml` أو التعليقات التوضيحية - annotations)، تقوم الحاوية بإنشاء نسخة من المرشح وتمرير كائن `FilterConfig` إلى طريقة `init` الخاصة به. يسمح هذا الكائن للمرشح بالوصول إلى:
- معاملات التهيئة الخاصة به.
- كائن `ServletContext` الخاص بتطبيق الويب.
- اسمه كما هو معرف في التكوين.

تطبق المرشحات واجهة `javax.servlet.Filter`، والتي تتضمن ثلاث طرق: `init`، و`doFilter`، و`destroy`. يتم استخدام كائن `FilterConfig` تحديدًا في طريقة `init` لإعداد المرشح قبل أن يبدأ في معالجة الطلبات.

---

#### **دورة حياة المرشح و `FilterConfig`**
لفهم كيفية عمل `FilterConfig`، دعنا نلقي نظرة على دوره في دورة حياة المرشح:
1. **بدء تشغيل الحاوية**: عندما يبدأ تشغيل تطبيق الويب، تقرأ الحاوية تعريفات المرشحات (من `web.xml` أو تعليقات `@WebFilter`) وتنشئ نسخة من كل مرشح.
2. **تهيئة المرشح**: لكل مرشح، تستدعي الحاوية طريقة `init`، وتمرر كائن `FilterConfig` كمعامل. هذه عملية لمرة واحدة لكل نسخة مرشح.
3. **معالجة الطلب**: بعد التهيئة، يتم استدعاء طريقة `doFilter` الخاصة بالمرشح لكل طلب مطابق. بينما لا يتم تمرير `FilterConfig` إلى `doFilter`، يمكن للمرشح تخزين بيانات التكوين من `FilterConfig` في متغيرات النسخة أثناء `init` لاستخدامها لاحقًا.
4. **إيقاف المرشح**: عندما يتوقف التطبيق، يتم استدعاء طريقة `destroy`، ولكن `FilterConfig` لا يكون متضمنًا هنا.

يعتبر كائن `FilterConfig` حاسمًا خلال مرحلة التهيئة، مما يمكن المرشح من الاستعداد لمعالجة الطلبات.

---

#### **الطرق الرئيسية لـ `FilterConfig`**
تحدد واجهة `FilterConfig` أربع طرق توفر الوصول إلى معلومات التكوين:

1. **`String getFilterName()`**
   - تُرجع اسم المرشح كما هو محدد في ملف `web.xml` (تحت `<filter-name>`) أو في تعليق `@WebFilter` التوضيحي.
   - هذا مفيد لتسجيل الأحداث (logging)، أو التصحيح (debugging)، أو تحديد هوية المرشح في سلسلة من المرشحات.

2. **`ServletContext getServletContext()`**
   - تُرجع كائن `ServletContext`، الذي يمثل تطبيق الويب بأكمله.
   - يسمح `ServletContext` للمرشح بالوصول إلى موارد على مستوى التطبيق، مثل سمات السياق (context attributes)، أو مرافق التسجيل (logging facilities)، أو `RequestDispatcher` لإعادة توجيه الطلبات.

3. **`String getInitParameter(String name)`**
   - تسترد قيمة معامل تهيئة محدد بواسطة اسمه.
   - معاملات التهيئة هي أزواج مفتاح-قيمة محددة للمرشح في `web.xml` (تحت `<init-param>`) أو في سمة `initParams` الخاصة بتعليق `@WebFilter` التوضيحي.
   - تُرجع `null` إذا كان المعامل غير موجود.

4. **`Enumeration<String> getInitParameterNames()`**
   - تُرجع تعدادًا (Enumeration) لجميع أسماء معاملات التهيئة المحددة للمرشح.
   - هذا يسمح للمرشح بالتكرار عبر جميع معاملاته واسترداد قيمها باستخدام `getInitParameter`.

يتم تنفيذ هذه الطرق بواسطة فئة ملموسة توفرها حاوية الويب (مثل `FilterConfigImpl` الداخلي لتومكات). كمطور، تتفاعل مع `FilterConfig` حصريًا من خلال هذه الواجهة.

---

#### **كيف يتم تكوين `FilterConfig`**
يمكن تعريف المرشحات وتكوينها بطريقتين:
1. **استخدام `web.xml` (مُعرِّف النشر - Deployment Descriptor)**:
   ```xml
   <filter>
       <filter-name>MyFilter</filter-name>
       <filter-class>com.example.MyFilter</filter-class>
       <init-param>
           <param-name>excludeURLs</param-name>
           <param-value>/login,/signup</param-value>
       </init-param>
   </filter>
   <filter-mapping>
       <filter-name>MyFilter</filter-name>
       <url-pattern>/*</url-pattern>
   </filter-mapping>
   ```
   - `<filter-name>` يحدد اسم المرشح.
   - `<init-param>` يحدد معاملات التهيئة كأزواج مفتاح-قيمة.

2. **استخدام التعليقات التوضيحية (Servlet 3.0 والإصدارات الأحدث)**:
   ```java
   import javax.servlet.annotation.WebFilter;
   import javax.servlet.annotation.WebInitParam;

   @WebFilter(
       filterName = "MyFilter",
       urlPatterns = "/*",
       initParams = @WebInitParam(name = "excludeURLs", value = "/login,/signup")
   )
   public class MyFilter implements Filter {
       // Implementation
   }
   ```
   - يحدد تعليق `@WebFilter` التوضيحي اسم المرشح وأنماط URL ومعاملات التهيئة.

في كلتا الحالتين، تستخدم الحاوية هذا التكوين لإنشاء كائن `FilterConfig` وتمريره إلى طريقة `init` الخاصة بالمرشح.

---

#### **مثال عملي**
إليك كيف قد يستخدم المرشح `FilterConfig` عمليًا:

```java
import javax.servlet.*;
import java.io.IOException;

public class MyFilter implements Filter {
    private String excludeURLs; // متغير نسخة لتخزين بيانات التكوين

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // الحصول على اسم المرشح
        String filterName = filterConfig.getFilterName();
        System.out.println("Initializing filter: " + filterName);

        // الحصول على معامل تهيئة
        excludeURLs = filterConfig.getInitParameter("excludeURLs");
        if (excludeURLs != null) {
            System.out.println("Exclude URLs: " + excludeURLs);
        }

        // تخزين ServletContext اختياريًا لاستخدام لاحق
        ServletContext context = filterConfig.getServletContext();
        context.log("Filter " + filterName + " initialized");
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // استخدام excludeURLs لتقرير ما إذا كان سيتم تصفية الطلب
        chain.doFilter(request, response); // المتابعة إلى المرشح أو Servlet التالي
    }

    @Override
    public void destroy() {
        // كود التنظيف
    }
}
```

- **في `init`**: يسترد المرشح اسمه، ومعامل التهيئة (`excludeURLs`)، و `ServletContext`. يقوم بتخزين `excludeURLs` في متغير نسخة لاستخدامه في `doFilter`.
- **في `doFilter`**: يمكن للمرشح استخدام التكوين المخزن (مثل `excludeURLs`) لمعالجة الطلبات.

---

#### **نقاط رئيسية حول `FilterConfig`**
- **نطاق محدد للمرشح**: معاملات التهيئة في `FilterConfig` خاصة بنسخة المرشح. يمكن أن يكون للمرشحات المختلفة معاملات بنفس الاسم ولكن بقيم مختلفة.
- **المقارنة مع `ServletContext`**: يوفر `ServletContext` (الذي يتم الوصول إليه عبر `getServletContext()`) معاملات تهيئة وموارد على مستوى التطبيق، وهي متميزة عن المعاملات الخاصة بالمرشح في `FilterConfig`.
- **استخدام لمرة واحدة في دورة الحياة**: يتم تمرير `FilterConfig` إلى `init` فقط. إذا احتاج المرشح إلى بياناته لاحقًا (مثلًا في `doFilter`)، يجب عليه تخزين البيانات في متغيرات النسخة.
- **مُقدم من الحاوية**: `FilterConfig` هي واجهة، وتوفر حاوية الويب التنفيذ الملموس.

---

#### **الخلاصة**
يعمل `javax.servlet.FilterConfig` من خلال تزويد المرشح بمعلومات التكوين أثناء تهيئته. تقوم حاوية الويب بتمرير كائن `FilterConfig` إلى طريقة `init` الخاصة بالمرشح، مما يسمح للمرشح بالوصول إلى:
- اسمه (`getFilterName`).
- استرداد معاملات التهيئة (`getInitParameter`, `getInitParameterNames`).
- التفاعل مع تطبيق الويب عبر `ServletContext` (`getServletContext`).

هذا يمكن المرشحات من أن يتم تكوينها بمرونة — عبر `web.xml` أو التعليقات التوضيحية — ويجهزها لمعالجة طلبات واستجابات HTTP بشكل فعال. سواء كنت تستثني عناوين URL معينة، أو تحدد مهلات زمنية، أو تسجل رسائل، فإن `FilterConfig` هو الجسر بين تكوين المرشح وسلوكه أثناء وقت التشغيل.