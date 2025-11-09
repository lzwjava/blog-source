---
audio: false
date: 2025-09-08
generated: true
image: false
lang: ar
layout: post
title: تغطية تكنولوجيا المعلومات للتطبيقات النابضية المعيارية
translated: true
type: note
---

### التقييم الشامل لإعداداتك
إعداداتك الحالية قوية لمشروع صغير متعدد الوحدات مثل هذا، خاصةً أنك حصلت بالفعل على التدفق الأساسي الذي يعمل: إرفاق وكيل JaCoCo إلى Jetty، وتشغيل اختبارات تكامل Python الخارجية عبر Exec Plugin، وإنشاء تقرير في وحدة `PlaygroundWeb`. هذا يلتقط تغطية وقت التشغيل من نقاط نهاية API التي اختبرها `unittest` الخاص بـ Python، وهو بالضبط ما تحتاجه لتغطية اختبار التكامل (IT) في تطبيق ويب Spring.

النقاط القوية الرئيسية:
- **معياري ومقيد بالمراحل**: استخدام مراحل Maven (`pre-integration-test` لبدء Jetty، `integration-test` لاختبارات Python، `post-integration-test` للإيقاف، `verify` للتقرير) يضمن الموثوقية وإمكانية إعادة الإنتاج.
- **إرفاق الوكيل**: وسيطة JVM (`-javaagent:...`) على Jetty تقوم بتدوين وقت التشغيل بشكل صحيح، والاحتفاظ بالتغطية في `jacoco.it.exec`.
- **تكامل الاختبارات الخارجية**: Exec Plugin يتعامل مع Python بشكل جيد، والاحتفاظ بالاختبارات في جذر المستودع (`${project.parent.basedir}/tests`) يفصلها عن وحدات Java.
- **لا يوجد تكرار غير ضروري**: أنت تتجنب تشغيل Jetty/Python في `PlaygroundUtils` (والتي لا تحتوي على وحدات تحكم)، وهذا فعال.

التحديات التي حددتها:
- **التغطية لوحدات المكتبات مثل `PlaygroundUtils`**: نظرًا لأن كود utils يعمل في JVM الخاصة بـ `PlaygroundWeb` (كتبع في ملف WAR)، فإنه يتم تدوينه ويظهر في `jacoco.it.exec` الخاص بـ `PlaygroundWeb`. لكن تقاريرك خاصة بكل وحدة، لذا لا تظهر تغطية `PlaygroundUtils` ما لم يتم تجميعها أو تضمينها.
- **طبيعة JaCoCo غير المستقلة**: على عكس Checkstyle/Spotless (التي تقوم فقط بتحليل المصادر/القطع الأثرية الثابتة)، تحتاج JaCoCo إلى بيانات وقت التشغيل (ملفات `.exec`) من الاختبارات الخارجية وإرفاق الوكيل. هذا يجعلها هشة للإعدادات متعددة الوحدات بدون تنسيق دقيق.
- **قيود هدف التجميع**: `jacoco:report-aggregate` تتوقع ملفات `.exec` لكل وحدة (مثلًا، من اختبارات الوحدة)، لكن تغطيتك تأتي بشكل بحت من IT في وحدة واحدة. إجبار التجميع يمكن أن يؤدي إلى تقارير فارغة لمكتبات مثل `PlaygroundUtils`.
- **القابلية للتوسع إلى 10+ وحدات**: تكرار إعدادات Jetty/Python عبر الوحدات سيكون مبذرًا (خوادم/اختبارات زائدة عن الحاجة). الحلول البديلة مثل نسخ ملفات `.exec` أو تشغيل كل شيء مرتين (كما ذكرت) تقدم عبء صيانة وزيادة في وقت البناء.

التراجع إلى التقارير لكل وحدة هو حل عملي، لكن يمكننا التحسين لتضمين التغطية بدون تكرار.

### الاستراتيجية الموصى بها
ركز على **إنشاء تقرير تغطية IT واحد وشامل في الوحدة التي تشغل التطبيق** (`PlaygroundWeb` هنا)، مع **تضمين بيانات التغطية للوحدات التابعة** مثل `PlaygroundUtils`. هذا يتجنب تشغيل الاختبارات عدة مرات ويستفيد من حقيقة أن كل الكود ينفذ في JVM واحدة.

لماذا هذه الطريقة بدلاً من التجميع؟
- التجميع (`report-aggregate`) أفضل لتغطية اختبار الوحدة الموزعة عبر الوحدات. بالنسبة لتغطية IT من وقت تشغيل واحد (حالتك)، فهو مبالغ فيه ولا يناسب بشكل طبيعي.
- التقرير الموحد يعطي نظرة شاملة لتغطية التطبيق، والتي غالبًا ما تكون أكثر فائدة من التقارير المنعزلة لكل وحدة (مثلًا، "80% إجماليًا، لكن طبقة utils عند 60%").
- للمشاريع الأكبر، هذا يتوسع من خلال معاملة "وحدة التطبيق" (WAR/EAR) كمحور للتغطية، وسحب التبعيات.

#### التنفيذ خطوة بخطوة لمشروعك المكون من وحدتين
ابدأ صغيرًا: طبق هذا على إعداداتك الحالية (1 وحدة تطبيق + 1 مكتبة). اختبرها، ثم قم بالتوسع.

1. **احتفظ بتنفيذ IT في `PlaygroundWeb` فقط**:
   - لا حاجة لتغييرات هنا. يبدأ Jetty ملف WAR (الذي يدمج `PlaygroundUtils`)، تصل اختبارات Python إلى نقاط النهاية، يتم التقاط التغطية في `${project.build.directory}/jacoco.it.exec`.
   - تأكد من تنفيذ كود utils: إذا كانت اختبارات Python الخاصة بك تستدعي نقاط نهاية تستخدم فئات `PlaygroundUtils` (مثل `SystemUtils`)، فسيتم تضمين تغطيتها في ملف `.exec`.

2. **عزز تقرير JaCoCo في `PlaygroundWeb` ليشمل `PlaygroundUtils`**:
   - استخدم `<additionalClassesDirectories>` و `<additionalSourceDirectories>` في هدف `report` الخاص بـ JaCoCo. هذا يخبر JaCoCo بفحص الفئات/المصادر من `PlaygroundUtils` مقابل نفس ملف `.exec`.
   - قم بتحديث POM الخاص بـ `PlaygroundWeb` (في إعداد `jacoco-maven-plugin`):

     ```xml
     <plugin>
         <groupId>org.jacoco</groupId>
         <artifactId>jacoco-maven-plugin</artifactId>
         <executions>
             <!-- الإعداد الحالي لـ prepare-agent -->
             <execution>
                 <id>prepare-agent</id>
                 <goals>
                     <goal>prepare-agent</goal>
                 </goals>
             </execution>
             <!-- التقرير المعزز: تضمين وحدة utils -->
             <execution>
                 <id>report-it</id>
                 <phase>verify</phase>
                 <goals>
                     <goal>report</goal>
                 </goals>
                 <configuration>
                     <dataFile>${jacoco.it.exec}</dataFile>
                     <outputDirectory>${project.reporting.outputDirectory}/jacoco-it</outputDirectory>
                     <!-- أضف هذه لتضمين تغطية PlaygroundUtils -->
                     <additionalClassesDirectories>
                         <directory>${project.parent.basedir}/PlaygroundUtils/target/classes</directory>
                     </additionalClassesDirectories>
                     <additionalSourceDirectories>
                         <directory>${project.parent.basedir}/PlaygroundUtils/src/main/java</directory>
                     </additionalSourceDirectories>
                 </configuration>
             </execution>
         </executions>
     </plugin>
     ```

   - هذا يولد تقريرًا واحدًا (في `PlaygroundWeb/target/site/jacoco-it`) يغطي كلا الوحدتين. سترى تفصيلًا حسب الحزمة/الفئة، بما في ذلك `org.lzw` من utils.

3. **عطل/أزل JaCoCo من `PlaygroundUtils`**:
   - نظرًا لأنه لا يحتوي على IT خاص به، قم بإزالة أي إعدادات/خصائص لـ JaCoCo (مثل `<jacoco.it.exec>`, `<it.report.skip>`). لا يحتاج إلى إنشاء تقريره الخاص—يتم التعامل مع التغطية في المصدر.
   - إذا كان لديك اختبارات وحدة في utils، احتفظ بـ `prepare-agent` + `report` منفصلين لتغطية الوحدة (`jacoco.exec` الافتراضي)، ولكن عزلهم عن IT.

4. **قم بالبناء والتحقق**:
   - شغل `mvn clean verify` من الوحدة الأصل.
   - يعمل Jetty/Python مرة واحدة فقط (في `PlaygroundWeb`).
   - تحقق من `PlaygroundWeb/target/site/jacoco-it/index.html`: يجب أن يعرض التغطية لفئات كلا الوحدتين.
   - إذا كانت تغطية utils 0%، تأكد من أن اختبارات Python الخاصة بك تنفذ تلك الفئات (مثلًا، أضف اختبارًا يستدعي `SystemUtils` عبر نقطة نهاية).

5. **اختياري: فرض حدود التغطية**:
   - أضف تنفيذ `check` في إضافة JaCoCo الخاصة بـ `PlaygroundWeb` لفشل البناء إذا انخفضت التغطية تحت حد معين (مثلًا، 70% تغطية للأسطر إجمالاً).
     ```xml
     <execution>
         <id>check-it</id>
         <goals>
             <goal>check</goal>
         </goals>
         <configuration>
             <dataFile>${jacoco.it.exec}</dataFile>
             <rules>
                 <rule>
                     <element>BUNDLE</element>
                     <limits>
                         <limit>
                             <counter>LINE</counter>
                             <value>COVEREDRATIO</value>
                             <minimum>0.70</minimum>
                         </limit>
                     </limits>
                 </rule>
             </rules>
         </configuration>
     </execution>
     ```

#### التوسع إلى مشروع أكبر (مثلًا، 10 وحدات)
لـ 10+ وحدة (مثلًا، مكتبات متعددة + 1-2 وحدة تطبيق/WAR)، قم بتوسيع النهج أعلاه لتجنب التعقيد:

- **مركزية IT في وحدات التطبيق**: إذا كان لديك WAR رئيسي واحد (مثل `PlaygroundWeb`)، اجعله "محور التغطية". أضف `<additionalClassesDirectories>` و `<additionalSourceDirectories` لجميع المكتبات التابعة (مثلًا، عبر حلقة أو قوائم خصائص في POM الأصلي).
  - مثال: عرف المسارات في خصائص الوحدة الأصل:
    ```xml
    <properties>
        <lib1.classes>${project.basedir}/Lib1/target/classes</lib1.classes>
        <lib1.sources>${project.basedir}/Lib1/src/main/java</lib1.sources>
        <!-- كرر لـ 10 مكتبات -->
    </properties>
    ```
  - في إعداد تقرير JaCoCo الخاص بـ WAR: ارجع إليهم بشكل ديناميكي.

- **إذا كان هناك تطبيقات/WARs متعددة**: أنشئ وحدات IT مخصصة (مثل `App1-IT`, `App2-IT`) التي تعتمد على WAR، وقم بتعيين إعدادات Jetty/Exec/JaCoCo هناك، وتضمين فقط فئات/مصادر التبعيات ذات الصلة. هذا يحافظ على البناء المعياري (مثلًا، `mvn verify -pl App1-IT` للتغطية المستهدفة).

- **تجنب تكرار IT لكل وحدة**: لا تشغل Jetty/Python في وحدات المكتبة أبدًا—إنه إهدار. إذا كانت المكتبة تحتاج إلى IT معزول (نادر)، امنحها خادم صغير/مجموعة اختبار خاصة بها.

- **التجميع لإعداد التقارير (إذا لزم الأمر)**: إذا أصررت على تقارير منفصلة لكل وحدة:
  - أنشئ ملف `.exec` في وحدة التطبيق.
  - استخدم `dependency:copy` في Maven أو سكريبت مخصص (عبر Exec Plugin) في `post-integration-test` الخاص بالوحدة الأصل لنسخ ملف `.exec` إلى `target/` لكل مكتبة (مثلًا، كـ `jacoco-it.exec`).
  - ثم، قم بإعداد `report` في كل مكتبة لاستخدام ذلك الملف المنسوخ.
  - لكن هذا أكثر تعقيدًا—فضل التقرير الموحد ما لم يطالب أصحاب المصلحة بمقاييس لكل وحدة.

- **نصائح أدوات للتوسع**:
  - **ملفات تعريف Maven**: استخدم ملفات التعريف (مثل `-Pcoverage`) لتبديل IT/إعداد التقارير لبناء أسرع للمطورين.
  - **تحسين CI**: في التكامل المستمر (مثل GitHub Actions)، خزن تبعيات Maven وشغل IT فقط عند التغييرات في الاختبارات/نقاط النهاية.
  - **بدائل إذا أصبح JaCoCo معقدًا جدًا**: فكر في SonarQube للتحليل المجمع (يقوم باستيعاب بيانات JaCoCo عبر الوحدات). أو انتقل إلى أدوات وقت التشغيل مثل OpenClover، لكن JaCoCo جيد إذا التزمت بنهج المحور.
  - **اختبار الاختبارات**: أضف اختبارًا استباقيًا في Python للتحقق من بدء الخادم (مثلًا، استعلم عن `http://localhost:8080/health`).

هذه الاستراتيجية تقلل من عمليات التشغيل (Jetty/Python واحدة لكل تطبيق)، تتعامل مع تبعيات JaCoCo بشكل نظيف، وتتوسع بدون انفجار. إذا شاركت المزيد من التفاصيل (مثلًا، كيفية استخدام utils في نقاط النهاية)، يمكنني تحسين مقاطع POM أكثر.