---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-code-fast-1
title: دليل تهيئة Log4j
translated: true
type: note
---

### نظرة عامة على تهيئة Log4j
Log4j هو إطار عمل شائع لتسجيل الأحداث (logging) في جافا يسمح لك بالتحكم في مستويات إخراج السجلات ووجهاتها. بالنسبة للإصدار 2.x (المُوصى به)، يتم تعريف التهيئات عادةً في ملف XML أو JSON أو YAML أو Properties (مثل `log4j2.xml`). يتضمن هذا الإعداد:

- ** **Loggers** **: يحدد مستويات الرسائل (مثل DEBUG, INFO, WARN, ERROR) التي يجب تسجيلها لفئات أو حزم معينة.
- ** **Appenders** **: يحدد مكان إرسال السجلات، مثل وحدة التحكم (standard output) أو الملفات (مع خيارات مثل التدوير - rotation).
- ** **Root Logger** **: مسجل أحداث افتراضي ينطبق على جميع الفئات التي لا تشملها مسجلات أحداث محددة.

لتكوين التسجيل في كل من وحدة التحكم والملف، ستقوم عادةً بإضافة `ConsoleAppender` و `RollingFileAppender` (لسجلات الملفات مع التدوير التلقائي). ضع ملف التهيئة في classpath الخاص بك (مثل `src/main/resources` في مشاريع Maven).

إذا كنت تستخدم Log4j 1.x، فقم بالترقية إلى الإصدار 2.x — فهو أسرع ويحتوي على ميزات أفضل. أدناه دليل خطوة بخطوة مع نموذج تهيئة XML.

### خطوات تكوين مسجلات الملفات ووحدة التحكم
1. **إضافة التبعيات**: تأكد من وجود Log4j 2.x في ملف pom.xml (Maven) أو build.gradle (Gradle). مثال لـ Maven:
   ```
   <dependency>
       <groupId>org.apache.logging.log4j</groupId>
       <artifactId>log4j-core</artifactId>
       <version>2.23.1</version>  <!-- استخدم أحدث إصدار -->
   </dependency>
   <dependency>
       <groupId>org.apache.logging.log4j</groupId>
       <artifactId>log4j-api</artifactId>
       <version>2.23.1</version>
   </dependency>
   ```

2. **إنشاء ملف تهيئة**: أنشئ ملف `log4j2.xml` في مجلد الموارد (resources) الخاص بك.

3. **تحديد Appenders**:
   - ConsoleAppender: يُخرج السجلات إلى الطرفية/وحدة التحكم.
   - RollingFileAppender: يكتب إلى ملف ويديره بناءً على الحجم (مثلًا، عندما يصل إلى 10 ميجابايت، ينشئ ملفًا جديدًا).

4. **تكوين Loggers**: عيّن مستوى التسجيل (مثل INFO) وقم بتعيين appenders. مسجل الأحداث الجذر (Root logger) يتعامل مع التسجيل العام.

5. **الاستخدام في الكود**: في فئات جافا الخاصة بك، احصل على مسجل أحداث بهذه الطريقة:
   ```java
   import org.apache.logging.log4j.LogManager;
   import org.apache.logging.log4j.Logger;
   
   public class MyClass {
       private static final Logger logger = LogManager.getLogger(MyClass.class);
       // رسائل التسجيل: logger.debug("رسالة التصحيح"); logger.info("رسالة معلومات");
   }
   ```

### نموذج التهيئة (log4j2.xml)
إليك تهيئة XML كاملة للتسجيل في وحدة التحكم والملف المتداول. يقوم بتسجيل مستوى INFO وما فوقه في وحدة التحكم، وجميع المستويات في ملف يتم تدويره يوميًا أو عند الوصول إلى 10 ميجابايت.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">  <!-- مستوى التسجيل الداخلي لـ Log4j -->

    <!-- قسم Appenders -->
    <Appenders>

        <!-- Console Appender -->
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%t] %-5level %logger{36} - %msg%n"/>
        </Console>

        <!-- Rolling File Appender -->
        <RollingFile name="File" fileName="logs/app.log" filePattern="logs/app-%d{yyyy-MM-dd}-%i.log.gz">
            <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss} [%t] %-5level %logger{36} - %msg%n"/>
            <Policies>
                <TimeBasedTriggeringPolicy />  <!-- التدوير يوميًا -->
                <SizeBasedTriggeringPolicy size="10MB"/>  <!-- أو بناءً على الحجم -->
            </Policies>
            <DefaultRolloverStrategy max="7"/>  <!-- الاحتفاظ بما يصل إلى 7 ملفات قديمة -->
        </RollingFile>

    </Appenders>

    <!-- قسم Loggers -->
    <Loggers>

        <!-- مسجل أحداث محدد لحزمتك (اختياري) -->
        <Logger name="com.yourapp" level="DEBUG" additivity="false">
            <AppenderRef ref="File"/>  <!-- فقط إلى الملف لهذه الحزمة -->
        </Logger>

        <!-- مسجل الأحداث الجذر -->
        <Root level="INFO">
            <AppenderRef ref="Console"/>  <!-- Debug/Info إلى وحدة التحكم -->
            <AppenderRef ref="File"/>     <!-- جميع المستويات إلى الملف -->
        </Root>

    </Loggers>

</Configuration>
```

- ** **Pattern Layout** **: يحدد تنسيق السجل (مثل الطابع الزمني، الموضوع، مستوى السجل، اسم المسجل، الرسالة).
- ** **Rolling Policies** **: تتدور الملفات بناءً على الوقت (مثل `-d{yyyy-MM-dd}`) أو الحجم؛ ويتم ضغطها بـ `.gz`.
- ** **Levels** **: عيّن `DEBUG` لسجلات التطوير التفصيلية، و `INFO` للإنتاج (اضبط حسب الحاجة).
- ** **الاختبار** **: شغّل تطبيقك وتحقق من إخراج وحدة التحكم + مجلد `logs/` للبحث عن الملفات.

للحصول على تهيئة قائمة على Properties، راجع وثائق Log4j — فهي أبسط ولكنها أقل مرونة. إذا كنت بحاجة إلى تعديلات خاصة بـ JSON/YAML أو إصدار معين، فارجع إلى [وثائق تهيئة Log4j 2 الرسمية](https://logging.apache.org/log4j/2.x/manual/configuration.html). إذا كان هذا لا يتطابق مع إعداداتك (مثل Log4j 1.x)، قدم المزيد من التفاصيل!