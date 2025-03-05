---
audio: true
generated: true
lang: ar
layout: post
title: تكوين الفلتر في سيرفليت جاڤا
translated: true
---

### كيف يعمل `javax.servlet.FilterConfig`?

في تطبيقات الويب التي يتم بناؤها باستخدام API Servlet في Java، يلعب الواجهة `javax.servlet.FilterConfig` دورًا رئيسيًا في تهيئة المصفوفات. المصفوفات هي مكونات تتدخل وتعمل على طلبات HTTP وإجابات HTTP قبل أن تصل إلى Servlet أو بعد مغادرتها. يوفر `FilterConfig` طريقة معيارية لتقديم معلومات التهيئة إلى مصفوفة عند تهيئتها من قبل حاوية الويب (مثل Tomcat، Jetty). أدناه، سأشرح كيفية عمل `FilterConfig`، غرضه، وكيف يتم استخدامه.

---

#### **ما هو `FilterConfig`?**
`FilterConfig` هو واجهة في حزمة `javax.servlet`. يتم استخدامه من قبل حاوية الويب لتقديم بيانات التهيئة إلى مصفوفة أثناء مرحلة تهيئتها. عندما يتم تعريف مصفوفة في تطبيق الويب (من خلال `web.xml` أو التسميات)، فإن الحاوية تخلق مثيلًا للمصفوفة وتقدم له كائنًا من `FilterConfig` إلى طريقة `init` الخاصة به. هذا الكائن يسمح للمصفوفة بالوصول إلى:
- متغيرات التهيئة الخاصة بها.
- `ServletContext` من تطبيق الويب.
- اسمها كما هو محدد في التهيئة.

تنفذ المصفوفات الواجهة `javax.servlet.Filter` التي تتضمن ثلاث طرق: `init`، `doFilter`، و `destroy`. يتم استخدام كائن `FilterConfig` بشكل خاص في طريقة `init` لتهيئة المصفوفة قبل بدء معالجة الطلبات.

---

#### **دورة حياة مصفوفة و `FilterConfig`**
لتفهم كيفية عمل `FilterConfig`، فلننظر إلى دوره في دورة حياة المصفوفة:
1. **بدء الحاوية**: عند بدء تطبيق الويب، تقرأ الحاوية تعريفات المصفوفات (من `web.xml` أو `@WebFilter` التسميات) وتخلق مثيلًا لكل مصفوفة.
2. **تهيئة المصفوفة**: لكل مصفوفة، تدعو الحاوية طريقة `init` وتقدم لها كائنًا من `FilterConfig` كمرجع. هذه عملية واحدة لكل مثيل مصفوفة.
3. **معالجة الطلب**: بعد التهيئة، يتم استدعاء طريقة `doFilter` للمصفوفة لكل طلب متطابق. بينما لا يتم تقديم `FilterConfig` إلى `doFilter`، يمكن للمصفوفة تخزين بيانات التهيئة من `FilterConfig` في متغيرات مثيل أثناء `init` للاستخدام لاحقًا.
4. **إغلاق المصفوفة**: عند إغلاق التطبيق، يتم استدعاء طريقة `destroy`، ولكن `FilterConfig` لا يكون مشاركًا هنا.

الكائن `FilterConfig` هو حاسم أثناء مرحلة التهيئة، مما يسمح للمصفوفة أن تحضر نفسها لمعالجة الطلبات.

---

#### **الطرق الرئيسية لـ `FilterConfig`**
تحدد الواجهة `FilterConfig` أربع طرق توفر الوصول إلى معلومات التهيئة:

1. **`String getFilterName()`**
   - يعيد اسم المصفوفة كما هو محدد في ملف `web.xml` (تحت `<filter-name>`) أو في التسمية `@WebFilter`.
   - هذا مفيد للسجلات، أو التشخيص، أو تحديد المصفوفة في سلسلة من المصفوفات.

2. **`ServletContext getServletContext()`**
   - يعيد كائن `ServletContext` الذي يمثل تطبيق الويب بأكمله.
   - يسمح `ServletContext` للمصفوفة بالوصول إلى الموارد على مستوى التطبيق، مثل سمات السياق، وسائل التسجيل، أو `RequestDispatcher` لتوجيه الطلبات.

3. **`String getInitParameter(String name)`**
   - يعيد قيمة متغير تهيئة محدد باسمه.
   - متغيرات التهيئة هي أزواج من المفتاح والقيمة التي يتم تعريفها للمصفوفة في `web.xml` (تحت `<init-param>`) أو في سمة `initParams` التسمية `@WebFilter`.
   - يعيد `null` إذا لم يكن المتغير موجودًا.

4. **`Enumeration<String> getInitParameterNames()`**
   - يعيد `Enumeration` من جميع أسماء متغيرات التهيئة التي تم تعريفها للمصفوفة.
   - هذا يسمح للمصفوفة بالتكرار على جميع متغيراتها وتسترجاع قيمها باستخدام `getInitParameter`.

تنفذ هذه الطرق من قبل فئة محددة تقدمها حاوية الويب (مثل `FilterConfigImpl` في Tomcat). كمبرمج، تتفاعل مع `FilterConfig` فقط من خلال هذه الواجهة.

---

#### **كيف يتم تهيئة `FilterConfig`**
يمكن تعريف المصفوفات وتهيئتها بطريقتين:
1. **استخدام `web.xml` (وصف التوزيع)**:
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
   - `<filter-name>` يحدد اسم المصفوفة.
   - `<init-param>` يحدد متغيرات التهيئة كأزواج من المفتاح والقيمة.

2. **استخدام التسميات (Servlet 3.0 وما بعده)**:
   ```java
   import javax.servlet.annotation.WebFilter;
   import javax.servlet.annotation.WebInitParam;

   @WebFilter(
       filterName = "MyFilter",
       urlPatterns = "/*",
       initParams = @WebInitParam(name = "excludeURLs", value = "/login,/signup")
   )
   public class MyFilter implements Filter {
       // التنفيذ
   }
   ```
   - التسمية `@WebFilter` تحدد اسم المصفوفة، نماذج URL، ومتغيرات التهيئة.

في كلا الحالتين، تستخدم الحاوية هذه التهيئة لإنشاء كائن `FilterConfig` وتقديمه إلى طريقة `init` للمصفوفة.

---

#### **مثال عملي**
هكذا قد تستخدم مصفوفة `FilterConfig` في الممارسة العملية:

```java
import javax.servlet.*;
import java.io.IOException;

public class MyFilter implements Filter {
    private String excludeURLs; // متغير مثيل لتخزين بيانات التهيئة

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        // الحصول على اسم المصفوفة
        String filterName = filterConfig.getFilterName();
        System.out.println("تهيئة المصفوفة: " + filterName);

        // الحصول على متغير تهيئة
        excludeURLs = filterConfig.getInitParameter("excludeURLs");
        if (excludeURLs != null) {
            System.out.println("تجاهل URLs: " + excludeURLs);
        }

        // تخزين ServletContext بشكل اختياري للاستخدام لاحقًا
        ServletContext context = filterConfig.getServletContext();
        context.log("تم تهيئة المصفوفة " + filterName);
    }

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain)
            throws IOException, ServletException {
        // استخدام excludeURLs لتحديد ما إذا كان يجب تصفية الطلب
        chain.doFilter(request, response); // الاستمرار إلى المصفوفة التالية أو Servlet
    }

    @Override
    public void destroy() {
        // كود التنظيف
    }
}
```

- **في `init`**: تسترجع المصفوفة اسمها، متغير تهيئة (`excludeURLs`)، و `ServletContext`. تخزن `excludeURLs` في متغير مثيل للاستخدام في `doFilter`.
- **في `doFilter`**: يمكن للمصفوفة استخدام البيانات المخزنة (مثل `excludeURLs`) لمعالجة الطلبات.

---

#### **نقاط رئيسية حول `FilterConfig`**
- **مجال محدد للمصفوفة**: متغيرات التهيئة في `FilterConfig` محددة للمصفوفة. يمكن أن يكون للمصفوفات المختلفة متغيرات بنفس الاسم ولكن قيم مختلفة.
- **مقارنة مع `ServletContext`**: `ServletContext` (الوصول إليه من خلال `getServletContext()`) يوفر متغيرات تهيئة على مستوى التطبيق والموارد، مختلفة عن متغيرات التهيئة المحددة للمصفوفة في `FilterConfig`.
- **استخدام واحد في دورة الحياة**: يتم تقديم `FilterConfig` فقط إلى `init`. إذا كان للمصفوفة حاجة إلى بياناتها لاحقًا (مثل في `doFilter`)، يجب أن تخزن البيانات في متغيرات مثيل.
- **مقدم من الحاوية**: `FilterConfig` هو واجهة، وتقدم الحاوية التنفيذ الفعلي.

---

#### **ملخص**
يعمل `javax.servlet.FilterConfig` من خلال تقديم معلومات التهيئة للمصفوفة أثناء تهيئتها. تقدم الحاوية كائنًا من `FilterConfig` إلى طريقة `init` للمصفوفة، مما يسمح للمصفوفة بالوصول إلى:
- اسمها (`getFilterName`).
- استرجاع متغيرات التهيئة (`getInitParameter`، `getInitParameterNames`).
- التفاعل مع تطبيق الويب من خلال `ServletContext` (`getServletContext`).

هذا يسمح للمصفوفات بالتهيئة بشكل مرن - من خلال `web.xml` أو التسميات - ويعدها لمعالجة طلبات HTTP وإجابات HTTP بشكل فعال. سواء كنت تبعد عن بعض URLs، أو تعيين أوقات انتظار، أو تسجيل رسائل، `FilterConfig` هو الجسر بين تهيئة المصفوفة وسيرتها التشغيلية.