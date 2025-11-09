---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: بدء العمل مع جي إس بي
translated: true
type: note
---

JavaServer Pages (JSP) هي تقنية من جانب الخادم تُستخدم لإنشاء محتوى ويب ديناميكي في تطبيقات Java. تتيح لك تضمين كود Java مباشرةً في صفحات HTML، مما يسهل توليد استجابات ديناميكية بناءً على إدخال المستخدم أو البيانات. JSP هي جزء من منصة Jakarta EE (المعروفة سابقًا باسم Java EE) وتعمل بشكل جيد مع الخدمات (servlets) في تطبيقات الويب.

أدناه دليل خطوة بخطوة للبدء مع JSP، من الإعداد إلى النشر. يفترض هذا الدليل معرفة أساسية بـ Java وHTML.

## 1. المتطلبات الأساسية
- **Java Development Kit (JDK)**: قم بتثبيت JDK 8 أو إصدار أحدث (يُوصى بـ JDK 17+ للتطبيقات الحديثة). يمكنك التنزيل من [Oracle](https://www.oracle.com/java/technologies/downloads/) أو استخدام OpenJDK.
- **خادم/حاوية الويب (Web Server/Container)**: استخدم Apache Tomcat (مجاني وسهل للمبتدئين). قم بالتنزيل من [Apache Tomcat](https://tomcat.apache.org/).
- **بيئة التطوير المتكاملة (IDE) (اختياري ولكنه موصى به)**: IntelliJ IDEA، أو Eclipse، أو VS Code مع إضافات Java لتسهيل التطوير.

## 2. إعداد بيئتك
1. تثبيت Tomcat:
   - استخرج أرشيف Tomcat إلى دليل (مثل `C:\tomcat` على Windows أو `/opt/tomcat` على Linux).
   - ابدأ تشغيل Tomcat بتشغيل `bin/startup.bat` (Windows) أو `bin/startup.sh` (Unix). قم بالوصول إلى `http://localhost:8080` في متصفحك للتحقق من أنه يعمل.

2. إنشاء هيكل المشروع:
   - في مجلد `webapps` الخاص بـ Tomcat، قم بإنشاء دليل جديد لتطبيقك (مثل `my-jsp-app`).
   - بداخله، قم بإنشاء:
     - `WEB-INF/web.xml` (واصف النشر، اختياري في JSP 2.2+ ولكنه مفيد للإعدادات).
     - مجلد رئيسي لملفات JSP (مثل `index.jsp`).

   مثال أساسي لـ `web.xml`:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee
            https://jakarta.ee/xml/ns/jakartaee/web-app_5_0.xsd"
            version="5.0">
       <display-name>My JSP App</display-name>
   </web-app>
   ```

## 3. اكتب صفحة JSP الأولى الخاصة بك
ملفات JSP لها امتداد `.jsp` وتجمع بين HTML وكود Java باستخدام النصوص البرمجية (scriptlets) (`<% %>`)، والتعابير (expressions) (`<%= %>`)، والتعريفات (declarations) (`<%! %>`). لممارسات أفضل حديثة، استخدم لغة التعبير في JSP (EL) ومكتبة العلامات القياسية لـ JSP (JSTL) لتجنب النصوص البرمجية الخام.

مثال: أنشئ `index.jsp` في المجلد الرئيسي لتطبيقك:
```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>  <!-- لـ JSTL، إذا تم استخدامه -->

<html>
<head>
    <title>Hello JSP</title>
</head>
<body>
    <h1>Welcome to JSP!</h1>
    
    <!-- Scriptlet: كود Java -->
    <% 
        String name = request.getParameter("name") != null ? request.getParameter("name") : "World";
        java.util.Date now = new java.util.Date();
    %>
    
    <!-- Expression: إخراج القيمة -->
    <p>Hello, <%= name %>! The time is <%= now %>.</p>
    
    <!-- استخدام EL (لغة التعبير) لإخراج أنظف -->
    <p>Your name via EL: ${param.name}</p>
    
    <!-- مثال JSTL: التكرار عبر قائمة -->
    <c:set var="fruits" value="${{'Apple', 'Banana', 'Cherry'}}" />
    <ul>
        <c:forEach var="fruit" items="${fruits}">
            <li>${fruit}</li>
        </c:forEach>
    </ul>
</body>
</html>
```

- **العناصر الرئيسية**:
  - **التوجيهات (Directives)**: `<%@ page ... %>` تحدد خصائص الصفحة؛ `<%@ taglib ... %>` تستورد مكتبات العلامات.
  - **النصوص البرمجية (Scriptlets)**: تضمين كود Java (استخدمها باعتدال؛ يُفضل EL/JSTL).
  - **EL**: `${expression}` للوصول إلى البيانات بدون نصوص برمجية.
  - **JSTL**: قم بتنزيلها من [Apache Taglibs](https://tomcat.apache.org/taglibs/standard/) وضع ملفات JAR في `WEB-INF/lib`.

## 4. النشر والتشغيل
1. ضع مجلد تطبيقك (مثل `my-jsp-app`) في دليل `webapps` الخاص بـ Tomcat.
2. أعد تشغيل Tomcat.
3. قم بالوصول عبر المتصفح: `http://localhost:8080/my-jsp-app/index.jsp`.
4. اختبر باستخدام معلمات الاستعلام (query params): `http://localhost:8080/my-jsp-app/index.jsp?name=Grok` لرؤية المخرجات الديناميكية.

## 5. الميزات الشائعة وأفضل الممارسات
- **النماذج وإدخال المستخدم**: استخدم علامات `<form>` و `request.getParameter()` أو EL (`${param.field}`) للتعامل مع عمليات الإرسال.
- **الجلسات (Sessions) و JavaBeans**: استخدم `session.setAttribute()` لإدارة الحالة؛ واستخدم JavaBeans للبيانات القابلة لإعادة الاستخدام.
- **معالجة الأخطاء**: أضف `<error-page>` في `web.xml` أو استخدم `<%@ page errorPage="error.jsp" %>`.
- **الأمان**: قم بتنقية المدخلات لمنع هجمات XSS؛ استخدم HTTPS في بيئة الإنتاج.
- **البدائل الحديثة**: لا يزال JSP مستخدمًا، ولكن ضع في اعتبارك استخدام Thymeleaf أو Spring MVC للمشاريع الجديدة لأنها أكثر مرونة.
- **تصحيح الأخطاء**: تحقق من سجلات Tomcat (`logs/catalina.out`) للبحث عن الأخطاء.

## 6. مواضيع متقدمة
- التكامل مع الخدمات (Servlets): استخدم JSP لواجهات العرض، و Servlets للمنطق (نمط MVC).
- الاتصال بقاعدة البيانات: استخدم JDBC أو JPA (مثلًا مع H2 أو MySQL).
- أدوات البناء: استخدم Maven/Gradle للتبعيات مثل JSTL.

للتطبيق العملي، ابدأ بـ "Hello World" بسيط وأضف الميزات تدريجيًا. إذا كنت تبني تطبيق ويب كامل، فاستكشف دروس Jakarta EE.

## المراجع
- [Oracle JSP Tutorial](https://docs.oracle.com/javaee/7/tutorial/jspx.htm)
- [Baeldung: Introduction to JSP](https://www.baeldung.com/jsp-tutorial)
- [Apache Tomcat JSP Examples](https://tomcat.apache.org/tomcat-10.1-doc/jsp-examples/)