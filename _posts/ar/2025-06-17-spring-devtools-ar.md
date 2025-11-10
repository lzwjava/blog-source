---
audio: false
generated: true
lang: ar
layout: post
title: أدوات سبرينغ بوت للتشغيل التلقائي
translated: true
type: note
---

عند تشغيل تطبيق Spring Boot باستخدام `mvn spring-boot:run`، فإن مراقبة الملفات وإمكانيات إعادة التشغيل التلقائي أو إعادة التحميل الساخن (hot-reload) غير مفعلة افتراضيًا. ومع ذلك، يمكنك تمكينها عن طريق إضافة الاعتماد `spring-boot-devtools` إلى مشروعك. توفر هذه الوحدة ميزات مثل إعادة التشغيل التلقائي و LiveReload لتسريع عملية التطوير.

### التفاصيل
1. **السلوك الافتراضي بدون DevTools**:
   - تشغيل `mvn spring-boot:run` بدون `spring-boot-devtools` لا يتضمن مراقبة الملفات أو إعادة التشغيل التلقائي. تحتاج إلى إيقاف التطبيق وإعادة تشغيله يدويًا لتطبيق التغييرات على فئات Java أو الموارد الثابتة أو القوالب.
   - قد تتطلب الموارد الثابتة (مثل HTML, CSS, JS) إعادة بناء كاملة أو إعادة تشغيل ما لم يتم تكوينها بشكل مختلف.

2. **مع `spring-boot-devtools`**:
   - **مراقبة الملفات**: تراقب DevTools مسار الفئة (classpath) للتغييرات في ملفات Java وخصائص وموارد معينة (مثل `/resources`, `/static`, `/templates`).
   - **إعادة التشغيل التلقائي**: عندما يتغير ملف على مسار الفئة (مثل فئة Java أو ملف خصائص)، تقوم DevTools بتشغيل إعادة تشغيل تلقائية للتطبيق. هذا أسرع من بدء التشغيل البارد (cold start) لأنه يستخدم اثنين من محملي الفئات (classloaders): واحد لمكتبات الطرف الثالث غير المتغيرة (base classloader) وآخر لشفرة تطبيقك (restart classloader).
   - **LiveReload**: التغييرات في الموارد الثابتة (مثل HTML, CSS, JS في `/static`, `/public`, أو `/templates`) أو القوالب (مثل Thymeleaf) تؤدي إلى تحديث المتصفح بدلاً من إعادة تشغيل كاملة، بشرط تثبيت امتداد LiveReload في المتصفح (مدعوم لـ Chrome, Firefox, Safari).
   - **الاستثناءات**: افتراضيًا، لا تؤدي الموارد في `/META-INF/maven`, `/META-INF/resources`, `/resources`, `/static`, `/public`, و `/templates` إلى إعادة تشغيل ولكنها تؤدي إلى تشغيل LiveReload. يمكنك تخصيص هذا باستخدام `spring.devtools.restart.exclude`.

3. **الإعداد لـ DevTools**:
   أضف الاعتماد التالي إلى ملف `pom.xml` الخاص بك:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-devtools</artifactId>
       <scope>runtime</scope>
       <optional>true</optional>
   </dependency>
   ```
   - يضمن `<optional>true</optional>` عدم تضمين DevTools في بناءات الإنتاج.
   - شغل التطبيق باستخدام `mvn spring-boot:run`. ستمكن DevTools تلقائيًا مراقبة الملفات وإعادة التشغيل التلقائي.

4. **السلوك في بيئات التطوير المتكاملة (IDEs)**:
   - **Eclipse**: يؤدي حفظ التغييرات (Ctrl+S) تلقائيًا إلى تشغيل بناء، مما تكتشفه DevTools وتعيد تشغيل التطبيق.
   - **IntelliJ IDEA**: تحتاج إلى تشغيل بناء يدويًا (Ctrl+F9 أو "Make Project") لكي تكتشف DevTools التغييرات، ما لم تقم بتكوين البناء التلقائي. بدلاً من ذلك، قم بتمكين "Build project automatically" في إعدادات IntelliJ للحصول على إعادة تشغيل سلسة.
   - لـ LiveReload، قم بتثبيت امتداد المتصفح من http://livereload.com/extensions/ وقم بتمكينه.

5. **بديل: Spring Loaded**:
   - بدلاً من DevTools، يمكنك استخدام Spring Loaded لتبديل ساخن أكثر تقدمًا (مثل تغييرات توقيعات الطرق). أضفه إلى `spring-boot-maven-plugin`:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <dependencies>
             <dependency>
                 <groupId>org.springframework</groupId>
                 <artifactId>springloaded</artifactId>
                 <version>1.2.8.RELEASE</version>
             </dependency>
         </dependencies>
     </plugin>
     ```
   - لا يُوصى بـ Spring Loaded بقدر DevTools، لأنه لا يتم صيانته بنفس النشاط وقد لا يدعم جميع الأطر.

6. **إعادة التحميل الساخن للموارد الثابتة**:
   - بدون DevTools، يمكنك تمكين إعادة التحميل الساخن للموارد الثابتة عن طريق تعيين خاصية `addResources` لـ `spring-boot-maven-plugin`:
     ```xml
     <plugin>
         <groupId>org.springframework.boot</groupId>
         <artifactId>spring-boot-maven-plugin</artifactId>
         <configuration>
             <addResources>true</addResources>
         </configuration>
     </plugin>
     ```
   - يضيف هذا `src/main/resources` إلى مسار الفئة، مما يسمح بالتحرير في المكان لملفات ثابتة، ولكنه أقل شمولاً من DevTools.

7. **محاذير**:
   - قد تسبب DevTools مشاكل في تحميل الفئات في المشاريع متعددة الوحدات. إذا حدث هذا، حاول تعطيل إعادة التشغيل باستخدام `spring.devtools.restart.enabled=false` أو استخدم JRebel لإعادة التحميل المتقدم.
   - لملفات غير موجودة على مسار الفئة، استخدم `spring.devtools.restart.additional-paths` لمراقبة الدلائل الإضافية.
   - يتطلب LiveReload امتداد متصفح وقد لا يعمل مع جميع إعدادات الواجهة الأمامية (مثل React مع Webpack).
   - إذا كانت عمليات إعادة التشغيل بطيئة، اضبط `spring.devtools.restart.poll-interval` و `spring.devtools.restart.quiet-period` لتحسين مراقبة الملفات.

### خطوات لتطبيق بسيط
1. أنشئ تطبيق Spring Boot أساسي (على سبيل المثال، باستخدام Spring Initializr مع `spring-boot-starter-web`).
2. أضف الاعتماد `spring-boot-devtools` إلى `pom.xml`.
3. شغل `mvn spring-boot:run`.
4. عدل ملف Java أو ملف خصائص أو مورد ثابت (مثل HTML في `src/main/resources/static`).
5. لاحظ إعادة التشغيل التلقائي (لـ Java/الخصائص) أو تحديث المتصفح (للموارد الثابتة مع تمكين LiveReload).

### مثال
لتطبيق بسيط مع وحدة تحكم REST:
```java
@RestController
public class HelloController {
    @GetMapping("/hello")
    public String hello() {
        return "Hello, World!";
    }
}
```
- أضف DevTools، وشغل `mvn spring-boot:run`، وغير القيمة المُرجعة للطريقة `hello()`. سيعيد التطبيق التشغيل تلقائيًا.
- أضف `index.html` في `src/main/resources/static`، وقم بتثبيت امتداد LiveReload، وغير الـ HTML. سيتحدد المتصفح دون إعادة تشغيل.

### الخلاصة
لتطبيق Spring Boot بسيط، فإن إضافة `spring-boot-devtools` هي أسهل طريقة لتمكين مراقبة الملفات وإعادة التشغيل التلقائي وإعادة التحميل الساخن. استخدم `mvn spring-boot:run` مع DevTools لتجربة تطوير سلسة. إذا كنت بحاجة إلى تبديل ساخن أكثر تقدمًا، ففكر في Spring Loaded أو JRebel، ولكن DevTools كافية لمعظم الحالات.

---

إليك مثالاً حول كيفية تكوين `spring-boot-devtools` لمراقبة الملفات وإعادة التشغيل التلقائي وإعادة التحميل الساخن في تطبيق Spring Boot الخاص بك باستخدام ملف `application.yml`. هذا التكوين مخصص لمشروع `blog-server` الخاص بك، بناءً على السجلات التي قدمتها والتي تظهر أن DevTools نشط ويراقب `target/classes`.

### تكوين `application.yml`
```yaml
spring:
  devtools:
    restart:
      # تمكين إعادة التشغيل التلقائي (الافتراضي: true)
      enabled: true
      # دلائل إضافية لمراقبتها لإعادة التشغيل (مثل مجلد تكوين مخصص)
      additional-paths:
        - /home/lzw/Projects/blog-server/config
      # ملفات/دلائل لاستبعادها من تحفيز إعادة التشغيل (تم الاحتفاظ بالاستثناءات الافتراضية)
      exclude: static/**,public/**,templates/**,logs/**,generated/**
      # فاصل الاستطلاع لتغييرات الملفات (بالميلي ثانية، الافتراضي: 1000)
      poll-interval: 1000
      # فترة الهدوء بعد تغييرات الملفات قبل إعادة التشغيل (بالميلي ثانية، الافتراضي: 400)
      quiet-period: 400
      # اختياري: ملف لتحفيز إعادة التشغيل يدويًا
      trigger-file: .restart
    livereload:
      # تمكين LiveReload لتحديث المتصفح عند تغيير الموارد الثابتة (الافتراضي: true)
      enabled: true
```

### شرح الإعدادات
- **`spring.devtools.restart.enabled`**: يمكّن إعادة التشغيل التلقائي عند تغيير ملفات مسار الفئة (مثل `target/classes`، كما رأيت في سجلك: `file:/home/lzw/Projects/blog-server/target/classes/`).
- **`spring.devtools.restart.additional-paths`**: يراقب دلائل إضافية (مثل `/home/lzw/Projects/blog-server/config`) للتغييرات لتحفيز إعادة التشغيل.
- **`spring.devtools.restart.exclude`**: يمنع إعادة التشغيل للتغييرات في دلائل `static/`، `public/`، `templates/`، `logs/`، أو `generated/`، بينما يسمح لـ LiveReload بالعمل مع الموارد الثابتة (مثل HTML, CSS, JS).
- **`spring.devtools.restart.poll-interval`**: يحدد عدد مرات فحص DevTools لتغييرات الملفات (1000 مللي ثانية = 1 ثانية).
- **`spring.devtools.restart.quiet-period`**: ينتظر 400 مللي ثانية بعد اكتشاف تغيير لضمان عدم وجود تغييرات أخرى معلقة قبل إعادة التشغيل.
- **`spring.devtools.restart.trigger-file`**: يسمح بإعادة التشغيل يدويًا عن طريق تحديث `.restart` (مثل `touch /home/lzw/Projects/blog-server/.restart`).
- **`spring.devtools.livereload.enabled`**: يمكّن خادم LiveReload، والذي يحفز تحديث المتصفح للتغييرات في `static/` أو `templates/` (يتطلب امتداد متصفح LiveReload).

### خطوات التطبيق
1. أنشئ أو حدّث `src/main/resources/application.yml` باستخدام التكوين أعلاه.
2. تأكد من وجود `spring-boot-devtools` في ملف `pom.xml` الخاص بك:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-devtools</artifactId>
       <scope>runtime</scope>
       <optional>true</optional>
   </dependency>
   ```
3. شغل `mvn spring-boot:run`. ستراقب DevTools `target/classes` و `/home/lzw/Projects/blog-server/config` (إذا تمت إضافته)، مع إعادة تشغيل التطبيق عند تغيير ملفات Java أو الخصائص وتحديث المتصفح عند تغيير الموارد الثابتة.
4. لـ LiveReload، قم بتثبيت امتداد متصفح (مثل من http://livereload.com/extensions/) أو دمج عميل LiveReload في الواجهة الأمامية الخاصة بك.

### ملاحظات
- تظهر سجلاتك بدء تشغيل سريع (0.8 ثانية)، لذا يجب أن يكون `poll-interval` و `quiet-period` الافتراضيين مناسبين. اضبطهما (مثل `poll-interval: 500`) إذا شعرت بأن عمليات إعادة التشغيل بطيئة في مشروع أكبر.
- إذا كنت لا تحتاج إلى LiveReload (مثل استخدام خادم تطوير واجهة أمامية منفصل)، عيّن `livereload.enabled: false`.
- لإعادة التشغيل يدويًا، أنشئ `.restart` في جذر مشروعك وقم بتحديثه عند الحاجة.

يجب أن يعمل تكوين YAML هذا بسلاسة مع إعداداتك، معززًا ميزات مراقبة الملفات وإعادة التشغيل التلقائي التي تراها بالفعل.