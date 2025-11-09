---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: واجهات برمجة تطبيقات JMS و JNDI لـ WebSphere
translated: true
type: note
---

### الحزم والواجهات البرمجية المطلوبة لـ JMS في جافا

لاستخدام مقتطف كود JMS الذي أشرت إليه (للبحث عن والتوصيل بـ JMS Connection Factory في IBM WebSphere Application Server)، ستحتاج إلى استيراد حزم جافا ذات الصلة. هذه واجهات برمجية قياسية من نظام Java EE/Jakarta EE:

- **JNDI (واجهة تسمية ودليل جافا)**: للبحث عن `InitialContext`.
  - الحزمة: `javax.naming` (أو `jakarta.naming` في إصدارات Jakarta EE الأحدث).
  - الفئة الرئيسية: `InitialContext` – هذه هي نقطة البداية لعمليات JNDI. توفر سياقًا للبحث عن الموارد (مثل مصانع JMS أو قوائم الانتظار) باستخدام أسماء JNDI الخاصة بها (مثل `"jms/MyConnectionFactory"`). في حاوية مثل WAS، تتصل تلقائيًا بخدمة التسمية في الخادم.

- **واجهة برمجة تطبيقات JMS (خدمة رسائل جافا)**: لإنشاء اتصالات، وجلسات، ومرسِلين/مستقبِلين، ورسائل.
  - الحزمة: `javax.jms` (JMS 1.1/2.0) أو `jakarta.jms` (Jakarta JMS 3.0+ في EE الحديث).
  - الواجهات الرئيسية: `QueueConnectionFactory`, `QueueConnection`, `QueueSession`, `QueueSender`, `Queue`, `TextMessage`, إلخ.

مثال على عمليات الاستيراد في أعلى فئة الجافا الخاصة بك:
```java
import javax.naming.InitialContext;
import javax.naming.NamingException;
import javax.jms.QueueConnectionFactory;
import javax.jms.QueueConnection;
import javax.jms.QueueSession;
import javax.jms.Queue;
import javax.jms.QueueSender;
import javax.jms.TextMessage;
import javax.jms.JMSException;
```

**ما هو `InitialContext`؟**  
إنها فئة في واجهة برمجة تطبيقات JNDI تعمل كنقطة دخول إلى خدمة تسمية. في الكود الخاص بك:  
```java
InitialContext ctx = new InitialContext();  // ينشئ سياقًا افتراضيًا مرتبطًا ببيئة JNDI لخادم التطبيق
QueueConnectionFactory qcf = (QueueConnectionFactory) ctx.lookup("jms/MyConnectionFactory");  // يبحث عن المصنع المُهيأ مسبقًا باستخدام اسم JNDI الخاص به
```  
لا حاجة إلى خصائص في المُنشئ للتطبيقات التي تعمل *داخل* WAS، لأن الحقة تحقن البيئة (على سبيل المثال، عبر `java.naming.factory.initial`). إذا كنت تشغل عميلاً قائمًا بذاته *خارج* WAS، فستقوم بتمرير `Hashtable` يحتوي على خصائص مثل عنوان URL للمزود.

### تبعيات Maven (pom.xml)

إذا كان تطبيق الجافا الخاص بك **مُنشرًا ويعمل داخل WAS** (مثل تطبيق ويب، أو EJB، أو enterprise bean):  
- **لا حاجة إلى تبعيات إضافية**. يوفر WAS واجهات برمجة تطبيقات JMS و JNDI جاهزة كجزء من وقت تشغيل Java EE الخاص به. فقط قم بالتجميع مقابلها (إنها موجودة في classpath أثناء البناء/النشر).  
- في `pom.xml`، يمكنك الإعلان عنها صراحة باستخدام `<scope>provided</scope>` لتجنب تضمينها في ملف WAR/EAR الخاص بك (يبقيه خفيفًا):  
  ```xml
  <dependencies>
      <dependency>
          <groupId>javax.jms</groupId>  <!-- أو jakarta.jms للإصدارات الأحدث -->
          <artifactId>javax.jms-api</artifactId>
          <version>2.0.1</version>  <!-- JMS 2.0، متوافق مع WAS 8.5+ -->
          <scope>provided</scope>
      </dependency>
      <dependency>
          <groupId>javax.naming</groupId>
          <artifactId>javax.naming-api</artifactId>
          <version>1.0</version>  <!-- JNDI 1.0، قياسي -->
          <scope>provided</scope>
      </dependency>
  </dependencies>
  ```

إذا كان تطبيقك هو **عميل قائم بذاته** (يعمل خارج WAS، على سبيل المثال، عميل خفيف يتصل بالخادم):  
- ستحتاج إلى مكتبات **WebSphere Application Client** للحصول على دعم JMS الكامل عبر IIOP. قم بتنزيل حزمة العميل "IBM WebSphere Application Server traditional" من IBM، ثم أضفها إلى classpath الخاص بك.  
- في `pom.xml`، قم بتضمين:  
  ```xml
  <dependency>
      <groupId>com.ibm.ws</groupId>
      <artifactId>was-jms-client</artifactId>  <!-- اسم تقريبي؛ استخدم مستودع Maven الخاص بـ IBM إذا كان متاحًا -->
      <version>9.0.5</version>  <!-- طابق إصدار WAS الخاص بك -->
  </dependency>
  ```  
  أو استخدم ملفات JAR الكاملة للعميل الخفيف (مثل `com.ibm.ws.orb_8.5.5.jar`, `com.ibm.ws.jndi_*.jar`). تحقق من وثائق IBM للإعداد الدقيق.

للهجرة إلى Jakarta EE (ما بعد 2020)، انتقل إلى حزم `jakarta.*`، لكن WAS 9.x لا يزال يستخدم حزم `javax.*` افتراضيًا — قم بتمكين Jakarta عبر حزم الميزات إذا لزم الأمر.

[وثائق واجهة برمجة تطبيقات JMS لـ IBM WebSphere](https://www.ibm.com/docs/en/was/9.0.5?topic=resources-jms-api)  
[برنامج تعليمي JNDI لـ Java EE](https://docs.oracle.com/javase/tutorial/jndi/)