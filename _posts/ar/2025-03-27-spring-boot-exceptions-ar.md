---
audio: false
generated: true
lang: ar
layout: post
title: استثناءات سبرينغ بوت
translated: true
type: note
---

عند العمل مع Spring Boot أو إطار عمل Spring الأوسع، يواجه المطورون بشكل متكرر استثناءات بسبب مشاكل التهيئة، أو أخطاء وقت التشغيل، أو الاستخدام غير الصحيح لواجهات برمجة التطبيقات (APIs). أدناه قائمة بالاستثناءات الشائعة التي قد تواجهها، إلى جانب أسبابها النموذجية والحلول المحتملة. تم تجميع هذه الاستثناءات حسب الفئة من أجل الوضوح.

---

### **1. الاستثناءات المتعلقة بالتهيئة**

- **`org.springframework.beans.factory.BeanCreationException`**:
  - **السبب**: فشل إنشاء كائن bean بسبب التبعيات المفقودة، أو سوء التهيئة، أو أخطاء في التمثيل.
  - **مثال**: فقدان تعليق `@Component`، أو `@Service`، أو عدم العثور على تبعية `@Autowired`.
  - **الحل**: تحقق من تعريفات الـ bean، وتأكد من توفر التبعيات، وتحقق من التعليقات التوضيحية.

- **`org.springframework.beans.factory.NoSuchBeanDefinitionException`**:
  - **السبب**: لا يمكن لـ Spring العثور على bean من النوع أو الاسم المطلوب في سياق التطبيق.
  - **مثال**: محاولة استخدام `@Autowired` لـ bean غير مُعرّف أو غير ممسوح ضوئيًا.
  - **الحل**: تأكد من أن الـ bean عليه التعليق التوضيحي المناسب (مثل `@Component`) وأنه ضمن مسح المسار المكون.

- **`org.springframework.context.ApplicationContextException`**:
  - **السبب**: فشل عام في تهيئة سياق تطبيق Spring.
  - **مثال**: تهيئة غير صالحة في ملف `application.properties` أو خطأ في بناء الجملة في فئة `@Configuration`.
  - **الحل**: راجع تتبع المكدس للعثور على السبب الجذري (مثل خاصية غير صالحة أو مورد مفقود).

- **`org.springframework.beans.factory.UnsatisfiedDependencyException`**:
  - **السبب**: لا يمكن تلبية تبعية مطلوبة من قبل bean.
  - **مثال**: تبعية دائرية أو تنفيذ مفقود لواجهة.
  - **الحل**: كسر التبعيات الدائرية (على سبيل المثال، استخدم `@Lazy`) أو قم بتوفير التبعية المفقودة.

---

### **2. الاستثناءات المتعلقة بالويب و REST**

- **`org.springframework.web.bind.MissingServletRequestParameterException`**:
  - **السبب**: معلمة طلب مطلوبة مفقودة في طلب HTTP.
  - **مثال**: تم تحديد `@RequestParam("id")`، لكن العميل لم يرسل `id`.
  - **الحل**: اجعل المعلمة اختيارية (`required = false`) أو تأكد من أن العميل يتضمنها.

- **`org.springframework.http.converter.HttpMessageNotReadableException`**:
  - **السبب**: لا يمكن قراءة نص الطلب (على سبيل المثال، JSON غير صحيح التنسيق).
  - **مثال**: إرسال JSON غير صالح إلى نقطة نهاية `@RequestBody`.
  - **الحل**: تحقق من حمولة الطلب وتأكد من تطابقها مع هيكل الكائن المستهدف.

- **`org.springframework.web.method.annotation.MethodArgumentTypeMismatchException`**:
  - **السبب**: لا يمكن تحويل وسيط الدالة إلى النوع المتوقع.
  - **مثال**: تمرير سلسلة مثل `"abc"` إلى معلمة تتوقع `int`.
  - **الحل**: تحقق من صحة الإدخال أو استخدم محولات مخصصة.

- **`org.springframework.web.servlet.NoHandlerFoundException`**:
  - **السبب**: لا يوجد تعيين متحكم (controller) لـ URL المطلوب.
  - **مثال**: خطأ إملائي في `@RequestMapping` أو متحكم مفقود.
  - **الحل**: تحقق من تعيينات نقاط النهاية وتأكد من مسح المتحكمات ضوئيًا.

---

### **3. استثناءات الوصول إلى البيانات (Spring Data/JPA/Hibernate)**

- **`org.springframework.dao.DataIntegrityViolationException`**:
  - **السبب**: تنتهك عملية قاعدة البيانات قيدًا (مثل مفتاح فريد أو مفتاح أجنبي).
  - **مثال**: إدخال قيمة مفتاح أساسي مكررة.
  - **الحل**: تحقق من البيانات للتأكد من التفرد أو تعامل مع الاستثناء بأسلوب مناسب.

- **`org.springframework.orm.jpa.JpaSystemException`**:
  - **السبب**: خطأ عام في وقت التشغيل متعلق بـ JPA، غالبًا ما يلف استثناء Hibernate.
  - **مثال**: انتهاك قيد أو مشكلة في الاتصال.
  - **الحل**: افحص الاستثناء المتداخل (مثل `SQLException`) للحصول على التفاصيل.

- **`org.hibernate.LazyInitializationException`**:
  - **السبب**: محاولة الوصول إلى كيان محمّل بكسلية خارج جلسة نشطة.
  - **مثال**: الوصول إلى علاقة `@OneToMany` بعد انتهاء المعاملة.
  - **الحل**: استخدم جلب مبكر، أو اجلب في الاستعلام (مثل `JOIN FETCH`)، أو تأكد من وجود جلسة مفتوحة.

- **`org.springframework.dao.InvalidDataAccessApiUsageException`**:
  - **السبب**: استخدام غير صحيح لواجهات برمجة تطبيقات Spring Data أو JDBC.
  - **مثال**: تمرير معلمة فارغة (null) إلى استعلام يتوقع قيمة.
  - **الحل**: تحقق من معلمات الاستعلام واستخدام واجهة برمجة التطبيقات.

---

### **4. الاستثناءات المتعلقة بالأمان**

- **`org.springframework.security.access.AccessDeniedException`**:
  - **السبب**: يفتقر المستخدم المصادق إلى الإذن للوصول إلى مورد.
  - **مثال**: الوصول إلى نقطة نهاية مؤمنة بدون الدور المطلوب.
  - **الحل**: تحقق من `@PreAuthorize` أو تكوين الأمان وضبط الأدوار/الصلاحيات.

- **`org.springframework.security.authentication.BadCredentialsException`**:
  - **السبب**: فشلت المصادقة بسبب اسم مستخدم أو كلمة مرور غير صحيحة.
  - **مثال**: إدخال المستخدم بيانات اعتماد خاطئة في نموذج تسجيل الدخول.
  - **الحل**: تأكد من صحة بيانات الاعتماد؛ خصّص معالجة الأخطاء للحصول على ملاحظات المستخدم.

- **`org.springframework.security.authentication.DisabledException`**:
  - **السبب**: حساب المستخدم معطل.
  - **مثال**: إرجاع تنفيذ `UserDetails` لـ `isEnabled() == false`.
  - **الحل**: قم بتمكين الحساب أو قم بتحديث حالة المستخدم.

---

### **5. استثناءات وقت التشغيل المتنوعة**

- **`java.lang.IllegalStateException`**:
  - **السبب**: يواجه Spring حالة غير صالحة أثناء التنفيذ.
  - **مثال**: استدعاء دالة على bean لم يتم تهيئته بالكامل.
  - **الحل**: تحقق من أساليب دورة الحياة أو ترتيب تهيئة الـ bean.

- **`org.springframework.transaction.TransactionException`**:
  - **السبب**: حدثت مشكلة أثناء إدارة المعاملة.
  - **مثال**: التراجع عن المعاملة بسبب استثناء غير معالج.
  - **الحل**: تأكد من الاستخدام الصحيح لـ `@Transactional` وتعامل مع الاستثناءات داخل المعاملة.

- **`java.lang.NullPointerException`**:
  - **السبب**: محاولة الوصول إلى مرجع كائن فارغ (null).
  - **مثال**: لم يتم حقن تبعية `@Autowired` بسبب سوء التهيئة.
  - **الحل**: أضف فحوصات null أو قم بتصحيح الخطأ لمعرفة سبب فقدان التبعية.

---

### **6. استثناءات محددة في Spring Boot**

- **`org.springframework.boot.context.embedded.EmbeddedServletContainerException`** (في الإصدارات القديمة) أو **`org.springframework.boot.web.server.WebServerException`** (في الإصدارات الأحدث):
  - **السبب**: فشل في بدء خادم الويب المضمن (مثل Tomcat أو Jetty).
  - **مثال**: المنفذ قيد الاستخدام بالفعل (مثل `8080`).
  - **الحل**: غيّر المنفذ في `application.properties` (`server.port=8081`) أو حرر المنفذ المشغول.

- **`org.springframework.boot.autoconfigure.jdbc.DataSourceProperties$DataSourceBeanCreationException`**:
  - **السبب**: فشل في تكوين مصدر البيانات.
  - **مثال**: فقدان أو خطأ في `spring.datasource.url/username/password`.
  - **الحل**: تحقق من خصائص مصدر البيانات في `application.properties` أو `application.yml`.

- **`org.springframework.boot.SpringApplication - Application run failed`**:
  - **السبب**: فشل عام أثناء بدء تشغيل Spring Boot.
  - **مثال**: سوء التهيئة، أو beans مفقودة، أو تعارضات في التبعيات.
  - **الحل**: تحقق من تتبع المكدس الكامل للعثور على السبب الجذري.

---

### **أفضل الممارسات لمعالجة الاستثناءات**

1. **معالجة الاستثناءات العامة**:
   - استخدم `@ControllerAdvice` مع `@ExceptionHandler` للقبض على الاستثناءات ومعالجتها بشكل متناسق عبر تطبيقك.
   - مثال:
     ```java
     @ControllerAdvice
     public class GlobalExceptionHandler {
         @ExceptionHandler(DataIntegrityViolationException.class)
         public ResponseEntity<String> handleDataIntegrityViolation() {
             return ResponseEntity.status(HttpStatus.CONFLICT).body("Data integrity violation occurred.");
         }
     }
     ```

2. **التسجيل (Logging)**:
   - سجّل الاستثناءات باستخدام إطار عمل مثل SLF4J/Logback للمساعدة في التصحيح.

3. **الاستثناءات المخصصة**:
   - عرّف استثناءات محددة للتطبيق وقم بتعيينها على رموز حالة HTTP المناسبة.

4. **التحقق من الصحة**:
   - استخدم `@Valid` والتحقق من صحة Bean (مثل `@NotNull`) للقبض على الأخطاء مبكرًا وتجنب استثناءات وقت التشغيل.

5. **التصحيح**:
   - مكّن التسجيل التفصيلي (`logging.level.org.springframework=DEBUG`) في `application.properties` لتتبع المشكلات.

---

### **الخلاصة**

هذه الاستثناءات هي من بين أكثر الاستثناءات شيوعًا التي ستواجهها عند استخدام Spring Boot أو إطار عمل Spring. يمكن أن يؤدي فهم أسبابها وحلولها إلى تسريع عملية التطوير والتصحيح بشكل كبير. إذا كنت تواجه استثناءً محددًا وتحتاج إلى شرح أعمق، فلا تتردد في مشاركة التفاصيل، وسأقدم شرحًا مخصصًا!