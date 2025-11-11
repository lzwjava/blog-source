---
audio: false
generated: true
lang: ar
layout: post
title: الجلسات في سيرفلت جافا
translated: true
type: note
---

دعني أتناول استفسارك حول كيفية عمل `HttpSession` في حزمة `javax.servlet`، وكيفية تعيين قيمة الجلسة، وكيفية استرجاعها. سأفترض أن "HTTPSession" في سؤالك هو خطأ مطبعي وأنك تقصد `HttpSession`، لأن هذا هو اسم الفئة الصحيح في حزمة `javax.servlet`.

---

### **كيف يعمل HttpSession؟**

`HttpSession` هو واجهة في حزمة `javax.servlet.http` تمكن إدارة الحالة في تطبيقات الويب الجافا. بروتوكول HTTP بطبيعته لا يحفظ الحالة — كل طلب من العميل (مثل المتصفح) إلى الخادم يكون مستقلاً، بدون ذاكرة للتفاعلات السابقة. للتغلب على هذا القيد وتتبع بيانات محددة للمستخدم عبر طلبات متعددة (مثل أثناء زيارة المستخدم لموقع ويب)، يوفر `HttpSession` آلية للحفاظ على "جلسة".

إليك كيف يعمل:

1. **إنشاء الجلسة**: عندما يصل المستخدم لأول مرة إلى سيرفليت في تطبيق ويب، تقوم حاوية السيرفليت (مثل Tomcat) بإنشاء كائن `HttpSession` جديد. يتم تعيين معرف فريد لهذه الجلسة يسمى **معرف الجلسة (session ID)**.

2. **نقل معرف الجلسة**: يتم إرسال معرف الجلسة إلى متصفح العميل، عادة كـ cookie باسم `JSESSIONID`. في الطلبات اللاحقة، يقوم المتصفح بتضمين هذا المعرف، مما يسمح للخادم بربط الطلب بالجلسة الحالية.

3. **آلية احتياطية**: إذا تم تعطيل الـ cookies في المتصفح، يمكن لحاوية السيرفليت استخدام **إعادة كتابة الرابط (URL rewriting)** كحل بديل. في هذه الحالة، يتم إلحاق معرف الجلسة بالروابط (مثال: `http://example.com/page;jsessionid=abc123`)، على الرغم من أن هذا يتطلب دعمًا صريحًا في كود التطبيق.

4. **التخزين على جانب الخادم**: يتم تخزين بيانات الجلسة الفعلية (السمات) على الخادم، وليس على العميل. يحتفظ العميل بمعرف الجلسة فقط، مما يجعل الجلسات أكثر أمانًا من الـ cookies لتخزين المعلومات الحساسة. يتم الاحتفاظ بالبيانات عادة في ذاكرة الخادم ولكن يمكن تخزينها في القرص أو قاعدة بيانات في التكوينات المتقدمة.

5. **دورة حياة الجلسة**: للجلسات فترة انتهاء (مهلة) (مثال: 30 دقيقة افتراضيًا، قابلة للتكوين عبر `web.xml` أو برمجيًا). إذا كان المستخدم غير نشط beyond هذا الوقت، تنتهي صلاحية الجلسة ويتم التخلص من بياناتها. يمكنك أيضًا إنهاء الجلسة يدويًا، مثل أثناء تسجيل الخروج.

تسمح هذه الآلية للخادم "بتذكر" معلومات خاصة بالمستخدم، مثل حالة تسجيل الدخول أو محتويات سلة التسوق، عبر طلبات متعددة.

---

### **كيفية تعيين قيمة في الجلسة**

لتخزين البيانات في `HttpSession`، تستخدم طريقة `setAttribute`. تربط هذه الطريقة مفتاحًا (من نوع `String`) بقيمة (أي كائن في جافا). إليك كيفية القيام بذلك:

1. **الحصول على كائن HttpSession**: في السيرفليت، احصل على `HttpSession` من كائن `HttpServletRequest` باستخدام `request.getSession()`. تقوم هذه الطريقة بإنشاء جلسة جديدة إذا لم تكن موجودة أو ترجع الجلسة الحالية.

2. **تعيين السمة**: استدعِ `setAttribute(key, value)` على كائن `HttpSession`.

إليك مثال في سيرفليت:

```java
import javax.servlet.http.*;
import java.io.*;

public class SetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        // احصل على الجلسة (تنشئ واحدة إذا لم تكن موجودة)
        HttpSession session = request.getSession();

        // عيّن سمة الجلسة
        session.setAttribute("username", "Alice");

        // رد على العميل
        response.setContentType("text/html");
        PrintWriter out = response.getWriter();
        out.println("Session value set: username = Alice");
    }
}
```

في هذا الكود:
- `request.getSession()` تضمن توفر جلسة.
- `session.setAttribute("username", "Alice")` تخزن النص `"Alice"` تحت المفتاح `"username"`.

---

### **كيفية الحصول على قيمة من الجلسة**

لاسترجاع قيمة من الجلسة، استخدم طريقة `getAttribute`. نظرًا لأنها ترجع `Object`، تحتاج إلى تحويلها (cast) إلى النوع المناسب. إليك العملية:

1. **الحصول على كائن HttpSession**: استخدم `request.getSession()` أو `request.getSession(false)` (الأخيرة ترجع `null` إذا لم تكن هناك جلسة موجودة، مما يتجنب إنشاء جلسة جديدة).

2. **الحصول على السمة**: استدعِ `getAttribute(key)` وقم بتحويل النتيجة.

إليك مثال:

```java
import javax.servlet.http.*;
import java.io.*;

public class GetSessionServlet extends HttpServlet {
    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws IOException {
        // احصل على الجلسة (ترجع null إذا لم تكن هناك جلسة موجودة)
        HttpSession session = request.getSession(false);

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        if (session != null) {
            // استرجع سمة الجلسة
            String username = (String) session.getAttribute("username");

            if (username != null) {
                out.println("Session value retrieved: username = " + username);
            } else {
                out.println("No username found in session.");
            }
        } else {
            out.println("No active session.");
        }
    }
}
```

في هذا الكود:
- `request.getSession(false)` تسترجع الجلسة الحالية أو ترجع `null`.
- `session.getAttribute("username")` تجلب القيمة، محولة إلى `String`.
- فحوصات الـ null تمنع الأخطاء إذا لم تكن الجلسة أو السمة موجودة.

---

### **مثال عملي**

إليك مثالاً مجمعًا يوضح تعيين قيمة في الجلسة واسترجاعها عبر طلبات متعددة:

1. **SetSessionServlet.java** (مثال: لتسجيل الدخول):

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
        out.println("User set in session: Bob");
    }
}
```

2. **GetSessionServlet.java** (مثال: لصفحة محمية):

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
            out.println("Welcome back, " + user);
        } else {
            out.println("Please log in first.");
        }
    }
}
```

عندما يصل العميل إلى `SetSessionServlet`، تقوم الجلسة بتخزين `"Bob"`. لاحقًا، الوصول إلى `GetSessionServlet` يسترجعها ويعرضها، حيث تستمر الجلسة عبر الطلبات.

---

### **ملاحظات إضافية**

- **مهلة الجلسة**: عيّنها عبر `session.setMaxInactiveInterval(seconds)` (مثال: `session.setMaxInactiveInterval(1800)` لمدة 30 دقيقة) أو في `web.xml`:

  ```xml
  <session-config>
      <session-timeout>30</session-timeout> <!-- بالدقائق -->
  </session-config>
  ```
- **إنهاء الجلسة**: استخدم `session.invalidate()` (مثال: لتسجيل الخروج).
- **الأمان**: استخدم HTTPS لحماية معرف الجلسة من الاعتراض. تجنب تخزين البيانات شديدة الحساسية بدون تشفير.
- **تحويل النوع**: قم دائمًا بتحويل نتائج `getAttribute`، لأنها ترجع `Object`.

---

### **ملخص**

- **كيف يعمل**: يحافظ `HttpSession` على حالة المستخدم باستخدام معرف جلسة (عبر cookies أو إعادة كتابة الرابط) ويخزن البيانات على الخادم.
- **تعيين قيمة**: `session.setAttribute("key", value)`.
- **الحصول على قيمة**: `String value = (String) session.getAttribute("key")`.

هذا يجب أن يمنحك فهمًا واضحًا لـ `HttpSession` في `javax.servlet`. دعني أعلم إذا كنت بحاجة إلى مزيد من التوضيح!