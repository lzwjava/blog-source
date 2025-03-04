---
audio: false
generated: true
lang: ar
layout: post
title: جلسات HTTP في Servlets Java
translated: true
---

أدعوك إلى معالجة استفسارك حول كيفية عمل `HttpSession` في حزمة `javax.servlet` وكيفية تعيين قيمة الجلسة وكيفية استرجاعها. سأفترض أن "HTTPSession" في استفسارك خطأ في الكتابة وأنك قصدت `HttpSession`، حيث أن هذا هو اسم الفئة الصحيح في حزمة `javax.servlet`.

---

### **كيف يعمل HttpSession؟**

`HttpSession` هو واجهة في حزمة `javax.servlet.http` تسمح بإدارة الحالة في تطبيقات الويب بالجاوا. HTTP من طبيعة عدم وجود حالة—كل طلب من العميل (مثل متصفح الويب) إلى الخادم مستقل، بدون ذكر للتواصلات السابقة. لتجاوز هذه القيود وتتبع البيانات الخاصة بالعميل عبر عدة طلبات (مثل خلال زيارة المستخدم لموقع الويب)، يوفر `HttpSession` آلية للحفاظ على "جلسة".

هكذا يعمل:

1. **إنشاء الجلسة**: عندما يفتح المستخدم أول مرة خادم Servlet في تطبيق الويب، يخلق خادم Servlet (مثل Tomcat) كائن `HttpSession` جديد. تُعطى هذه الجلسة معرف فريد يُعرف باسم **معرف الجلسة**.

2. **إرسال معرف الجلسة**: يُرسل معرف الجلسة إلى متصفح العميل، عادةً كعلبة مخصصة باسم `JSESSIONID`. في الطلبات اللاحقة، يُضيف المتصفح هذا المعرف، مما يسمح للخادم بربط الطلب بالجلسة الحالية.

3. **آلية الاحتياط**: إذا تم تعطيل العلبات في المتصفح، يمكن لخادم Servlet استخدام **تحرير URL** كآلية احتياطية. في هذه الحالة، يُضاف معرف الجلسة إلى URLs (مثل `http://example.com/page;jsessionid=abc123`)، ولكن هذا يتطلب دعمًا صريحًا في كود التطبيق.

4. **الخزن على الخادم**: تُخزن البيانات الفعلية للجلسة (الخصائص) على الخادم، وليس على العميل. يُحتفظ العميل فقط بمعرف الجلسة، مما يجعل الجلسة أكثر أمانًا من العلبات لحفظ المعلومات الحساسة. تُخزن البيانات عادةً في ذاكرة الخادم، ولكن يمكن أن تُحفظ على القرص أو قاعدة بيانات في تكوينات متقدمة.

5. **دورة حياة الجلسة**: للجلسة فترة انقضاء (مثل 30 دقيقة افتراضيًا، قابلة للتكوين عبر `web.xml` أو برمجيًا). إذا كان المستخدم غير نشط لفترة أطول من هذه الفترة، تنتهي الجلسة وتتم إزالة بياناتها. يمكنك أيضًا إنهاء الجلسة يدويًا، مثل أثناء تسجيل الخروج.

تسمح هذه الآلية للخادم "بذكر" المعلومات الخاصة بالعميل، مثل حالة تسجيل الدخول أو محتوى عربة التسوق، عبر عدة طلبات.

---

### **كيف يتم تعيين قيمة الجلسة؟**

لحفظ البيانات في `HttpSession`، تستخدم طريقة `setAttribute`. هذه الطريقة تربط مفتاحًا (مسلسلًا) بقيمة (أي كائن جاوا). هكذا يتم ذلك:

1. **الحصول على كائن HttpSession**: في Servlet، احصل على `HttpSession` من كائن `HttpServletRequest` باستخدام `request.getSession()`. هذه الطريقة تخلق جلسة جديدة إذا لم تكن موجودة أو ترجع الجلسة الحالية.

2. **تعيين الخواص**: استدعاء `setAttribute(key, value)` على كائن `HttpSession`.

هنا مثال في Servlet:

```java
import javax.servlet.http.*;
import java.io.*;

public class SetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        // الحصول على الجلسة (إنشاء واحدة إذا لم تكن موجودة)
        HttpSession session = request.getSession();

        // تعيين خاصية الجلسة
        session.setAttribute("username", "Alice");

        // الرد على العميل
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("تم تعيين قيمة الجلسة: username = Alice");
    }
}
```

في هذا الكود:
- `request.getSession()` يضمن وجود جلسة.
- `session.setAttribute("username", "Alice")` يحفظ السلسلة `"Alice"` تحت المفتاح `"username"`.

---

### **كيف يتم استرجاع قيمة الجلسة؟**

لاسترجاع قيمة من الجلسة، استخدم طريقة `getAttribute`. نظرًا لأنها ترجع كائنًا، عليك تحويلها إلى النوع المناسب. هكذا يتم ذلك:

1. **الحصول على كائن HttpSession**: استخدم `request.getSession()` أو `request.getSession(false)` (الآخر ترجع `null` إذا لم تكن هناك جلسة، مما يمنع إنشاء جلسة جديدة).

2. **الحصول على الخواص**: استدعاء `getAttribute(key)` وتحويل النتيجة.

هنا مثال:

```java
import javax.servlet.http.*;
import java.io.*;

public class GetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        // الحصول على الجلسة (ترجع null إذا لم تكن هناك جلسة)
        HttpSession session = request.getSession(false);

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        if (session != null) {
            // استرجاع خاصية الجلسة
            String username = (String) session.getAttribute("username");

            if (username != null) {
                out.println("تم استرجاع قيمة الجلسة: username = " + username);
            } else {
                out.println("لم يتم العثور على اسم مستخدم في الجلسة.");
            }
        } else {
            out.println("لا توجد جلسة نشطة.");
        }
    }
}
```

في هذا الكود:
- `request.getSession(false)` يسترجع الجلسة الحالية أو ترجع `null`.
- `session.getAttribute("username")` يسترجع القيمة، وتحويلها إلى `String`.
- التحقق من `null` يمنع الأخطاء إذا لم تكن الجلسة أو الخاصية موجودة.

---

### **مثال عملي**

هنا مثال مشترك يوضح تعيين واسترجاع قيمة الجلسة عبر الطلبات:

1. **SetSessionServlet.java** (مثل تسجيل الدخول):
```java
import javax.servlet.http.*;
import java.io.*;

public class SetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        HttpSession session = request.getSession();
        session.setAttribute("user", "Bob");

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("تم تعيين المستخدم في الجلسة: Bob");
    }
}
```

2. **GetSessionServlet.java** (مثل صفحة محمية):
```java
import javax.servlet.http.*;
import java.io.*;

public class GetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        HttpSession session = request.getSession(false);

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        if (session != null && session.getAttribute("user") != null) {
            String user = (String) session.getAttribute("user");
            out.println("مرحبًا بك مرة أخرى، " + user);
        } else {
            out.println("يرجى تسجيل الدخول أولًا.");
        }
    }
}
```

عندما يفتح العميل `SetSessionServlet`، تُخزن الجلسة `"Bob"`. لاحقًا، عند الوصول إلى `GetSessionServlet`، يتم استرجاعها وعرضها، حيث تظل الجلسة مستمرة عبر الطلبات.

---

### **ملاحظات إضافية**

- **وقت انقضاء الجلسة**: يتم تعيينه عبر `session.setMaxInactiveInterval(seconds)` (مثل `session.setMaxInactiveInterval(1800)` ل30 دقيقة) أو في `web.xml`:
  ```xml
  <session-config>
      <session-timeout>30</session-timeout> <!-- في الدقائق -->
  </session-config>
  ```
- **إنهاء الجلسة**: استخدم `session.invalidate()` (مثل تسجيل الخروج).
- **الأمان**: استخدم HTTPS لحماية معرف الجلسة من الاستحواذ. تجنب تخزين بيانات حساسة للغاية دون تشفير.
- **تحويل النوع**: دائمًا تحويل نتائج `getAttribute`، حيث ترجع كائنًا.

---

### **ملخص**

- **كيف يعمل**: `HttpSession` يحافظ على حالة المستخدم باستخدام معرف الجلسة (عن طريق العلبات أو تحرير URL) ويخزن البيانات على الخادم.
- **تعيين قيمة**: `session.setAttribute("key", value)`.
- **استرجاع قيمة**: `String value = (String) session.getAttribute("key")`.

يجب أن يوفر لك هذا فهمًا واضحًا لـ `HttpSession` في `javax.servlet`. دعني أعلم إذا كنت تحتاج إلى مزيد من التوضيح!