---
audio: false
generated: true
lang: ar
layout: post
title: تقنيات التصحيح والتسجيل في جافا
translated: true
type: note
---

لا تمتلك Java علمًا مدمجًا لتسجيل كل متغير وحالة تلقائيًا لكل عبارة يتم تنفيذها، لأن هذا سيولد كمية هائلة من المخرجات وسيؤثر بشكل كبير على الأداء. ومع ذلك، يمكنك تحقيق تصحيح أخطاء مفصل وتسجيل المتغيرات وحالة البرنامج باستخدام أدوات وتقنيات وتكوينات متنوعة. أدناه، سأوضح أقرب الطرق لتحقيق هذا في Java، بما في ذلك أعلام التصحيح والأدوات والحلول المخصصة.

---

### 1. **استخدام أعلام تصحيح JVM مع مصحح الأخطاء**
يدعم Java Virtual Machine (JVM) التصحيح عبر Java Debug Wire Protocol (JDWP). يمكنك تمكين التصحيح عن طريق تمرير أعلام JVM محددة، مما يسمح لك بإرفاق مصحح أخطاء (مثل IntelliJ IDEA أو Eclipse أو Visual Studio Code) لمراقبة المتغيرات وتتبع المكدس وحالة البرنامج خطوة بخطوة.

#### كيفية تمكين تصحيح JVM
ابدأ تطبيق Java الخاص بك باستخدام خيارات JVM التالية:
```bash
java -agentlib:jdwp=transport=dt_socket,server=y,suspend=y,address=*:5005 MyApp
```

- **الأعلام الرئيسية**:
  - `-agentlib:jdwp`: يمكل وكيل JDWP للتصحيح.
  - `transport=dt_socket`: يستخدم نقل المقبس للاتصال بمصحح الأخطاء.
  - `server=y`: يعمل JVM كخادم، في انتظار اتصال مصحح الأخطاء.
  - `suspend=y`: يوقف JVM مؤقتًا حتى يتم إرفاق مصحح الأخطاء (استخدم `suspend=n` للتشغيل دون انتظار).
  - `address=*:5005`: يحدد المنفذ (مثال: 5005) لاتصال مصحح الأخطاء.

#### الاستخدام مع مصحح الأخطاء
1. **إرفاق مصحح الأخطاء**: استخدم بيئة تطوير متكاملة (IDE) مثل IntelliJ IDEA أو Eclipse أو Visual Studio Code للاتصال بـ JVM على المنفذ المحدد (مثال: 5005).
2. **تعيين نقاط التوقف**: ضع نقاط توقف في الكود الخاص بك حيث تريد فحص المتغيرات والحالة.
3. **التنقل خلال الكود خطوة بخطوة**: تسمح لك المصححات بالتنقل خلال كل عبارة، وفحص قيم المتغيرات، وتقييم التعبيرات، وعرض مكدس الاستدعاءات في الوقت الفعلي.

#### ما تحصل عليه
- فحص المتغيرات في كل نقطة توقف.
- مراقبة حالة البرنامج (مثل المتغيرات المحلية، وحقول الكائن، وإطارات المكدس).
- الدخول إلى استدعاءات الدوال، أو تخطيها، أو الخروج منها لتتبع التنفيذ.

#### القيود
- يتطلب إعدادًا يدويًا لنقاط التوقف والتنقل خطوة بخطوة.
- لا يوجد تسجيل تلقائي لكل متغير في كل عبارة إلا إذا قمت بتكوين المراقبة أو نقاط السجل بشكل صريح.

---

### 2. **التسجيل باستخدام أطر العمل (مثل SLF4J أو Log4j أو Java Logging)**
لتسجيل قيم المتغيرات وحالة البرنامج، يمكنك استخدام إطار تسجيل مثل SLF4J مع Logback أو Log4j أو `java.util.logging` المدمج في Java. ومع ذلك، يتطلب هذا منك إضافة عبارات السجل يدويًا إلى الكود الخاص بك لالتقاط قيم المتغيرات والحالة.

#### مثال مع SLF4J و Logback
1. **إضافة التبعيات** (مثال: لـ Maven):

```xml
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-classic</artifactId>
    <version>1.4.11</version>
</dependency>
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-api</artifactId>
    <version>2.0.9</version>
</dependency>
```

2. **تكوين Logback** (`logback.xml`):

```xml
<configuration>
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss} %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    <root level="DEBUG">
        <appender-ref ref="CONSOLE" />
    </root>
</configuration>
```

3. **إضافة التسجيل إلى الكود**:

```java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class MyApp {
    private static final Logger logger = LoggerFactory.getLogger(MyApp.class);

    public static void main(String[] args) {
        int x = 10;
        String message = "Hello";
        logger.debug("Variable x: {}, message: {}", x, message);
        x++;
        logger.debug("After increment, x: {}", x);
    }
}
```

#### المخرجات
```
2025-06-06 20:50:00 DEBUG MyApp - Variable x: 10, message: Hello
2025-06-06 20:50:00 DEBUG MyApp - After increment, x: 11
```

#### ملاحظات
- **الإيجابيات**: يمكنك تسجيل متغيرات وحالات محددة في النقاط المطلوبة بتنسيقات قابلة للتخصيص.
- **السلبيات**: يتطلب إضافة عبارات السجل يدويًا لكل متغير أو حالة تريد تتبعها. يعد تسجيل كل متغير تلقائيًا غير عملي بدون تعديل الكود.

---

### 3. **تعديل البايت كود باستخدام الأدوات (مثل Java Agents أو Byte Buddy أو AspectJ)**
لتسجيل كل متغير وحالة تلقائيًا دون تعديل الكود المصدري، يمكنك استخدام تعديل البايت كود لحق منطق التسجيل أثناء وقت التشغيل أو وقت الترجمة. هذا النهج هو الأقرب لطلبك للتسجيل التلقائي لكل عبارة.

#### الخيار 1: Java Agent مع Byte Buddy
Byte Buddy هي مكتبة تسمح لك بإنشاء وكيل Java لاعتراض استدعاءات الدوال وتسجيل حالات المتغيرات ديناميكيًا.

1. **إضافة تبعية Byte Buddy** (Maven):

```xml
<dependency>
    <groupId>net.bytebuddy</groupId>
    <artifactId>byte-buddy</artifactId>
    <version>1.14.9</version>
</dependency>
<dependency>
    <groupId>net.bytebuddy</groupId>
    <artifactId>byte-buddy-agent</artifactId>
    <version>1.14.9</version>
</dependency>
```

2. **إنشاء وكيل Java**:

```java
import net.bytebuddy.agent.builder.AgentBuilder;
import net.bytebuddy.description.type.TypeDescription;
import net.bytebuddy.dynamic.DynamicType;
import net.bytebuddy.implementation.MethodDelegation;
import net.bytebuddy.matcher.ElementMatchers;
import java.lang.instrument.Instrumentation;

public class LoggingAgent {
    public static void premain(String args, Instrumentation inst) {
        new AgentBuilder.Default()
            .type(ElementMatchers.any())
            .transform((builder, type, classLoader, module) -> 
                builder.method(ElementMatchers.any())
                       .intercept(MethodDelegation.to(LoggingInterceptor.class)))
            .installOn(inst);
    }
}
```

3. **إنشاء معترض**:

```java
import net.bytebuddy.implementation.bind.annotation.AllArguments;
import net.bytebuddy.implementation.bind.annotation.Origin;
import net.bytebuddy.implementation.bind.annotation.RuntimeType;

import java.lang.reflect.Method;
import java.util.Arrays;

public class LoggingInterceptor {
    @RuntimeType
    public static Object intercept(@Origin Method method, @AllArguments Object[] args) throws Exception {
        System.out.println("Executing: " + method.getName() + " with args: " + Arrays.toString(args));
        // المتابعة باستدعاء الدالة الأصلية
        return method.invoke(null, args);
    }
}
```

4. **التشغيل مع الوكيل**:
```bash
java -javaagent:logging-agent.jar -cp . MyApp
```

#### ملاحظات
- **الإيجابيات**: يمكنه تسجيل استدعاءات الدوال والمعاملات وحالات المتغيرات المحتملة تلقائيًا من خلال فحص المكدس أو البايت كود.
- **السلبيات**: يتطلب تسجيل كل متغير في كل عبارة تحليلاً معقدًا للبايت كود، مما قد يكون بطيئًا وصعب التنفيذ بشكل شامل. قد تحتاج إلى تخصيص الوكيل further لالتقاط المتغيرات المحلية.

#### الخيار 2: AspectJ للبرمجة الموجهة نحو الجوانب
يسمح لك AspectJ بتعريف جوانب تعترض تنفيذ الكود وتسجل حالات المتغيرات.

1. **إضافة تبعية AspectJ** (Maven):

```xml
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjrt</artifactId>
    <version>1.9.22</version>
</dependency>
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjweaver</artifactId>
    <version>1.9.22</version>
</dependency>
```

2. **تحديد جانب**:

```java
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;

@Aspect
public class LoggingAspect {
    @After("execution(* *(..))")
    public void logAfter(JoinPoint joinPoint) {
        System.out.println("Method executed: " + joinPoint.getSignature());
        System.out.println("Arguments: " + Arrays.toString(joinPoint.getArgs()));
    }
}
```

3. **التشغيل مع AspectJ**:
استخدم منسج AspectJ بإضافة الوكيل:
```bash
java -javaagent:aspectjweaver.jar -cp . MyApp
```

#### ملاحظات
- **الإيجابيات**: يمكنه تسجيل تنفيذ الدوال والمعاملات تلقائيًا.
- **السلبيات**: يلتقط كل متغير محلي وحالة يتطلب نقط قطع متقدمة وقد يحتاج إلى تعديلات على الكود المصدري أو نسج وقت التشغيل.

---

### 4. **استخدام ميزات التصحيح الخاصة بـ IDE**
توفر بيئات التطوير المتكاملة الحديثة مثل IntelliJ IDEA و Eclipse و Visual Studio Code ميزات تصحيح متقدمة يمكنها محاكاة السلوك الذي تريده:

- **نقاط السجل**: تسمح لك IntelliJ IDEA و Eclipse بتعيين "نقاط السجل" (أو "نقاط التتبع") التي تطبع قيم المتغيرات دون إيقاف التنفيذ.
- **مراقبة المتغيرات**: يمكنك مراقبة متغيرات محددة وتسجيل قيمها في كل خطوة.
- **نقاط التوقف الشرطية**: حدد نقاط توقف تسجل المتغيرات عند استيفاء شروط معينة.

#### مثال في IntelliJ IDEA
1. عيّن نقطة توقف.
2. انقر بزر الماوس الأيمن على نقطة التوقف، وحدد "More" أو "Edit Breakpoint."
3. فعّل "Evaluate and Log" لطباعة قيم المتغيرات أو التعبيرات (مثال: `System.out.println("x = " + x)`).
4. تنقل خلال الكود خطوة بخطوة لتسجيل الحالة في كل عبارة.

#### ملاحظات
- **الإيجابيات**: غير تدخلي وسهل الإعداد لمتغيرات أو دوال محددة.
- **السلبيات**: ليس تلقائيًا بالكامل؛ تحتاج إلى تحديد ما يجب تسجيله.

---

### 5. **تعديل الكود المخصص**
للتحكم الكامل، يمكنك كتابة أداة لتحليل وتعديل الكود المصدري أو البايت كود لـ Java لإدراج عبارات التسجيل لكل متغير وعبارة. يمكن أن تساعدك أدوات مثل **ASM** أو **Javassist** في معالجة البايت كود، ولكن هذا معقد ويُستخدم عادةً لحالات الاستخدام المتقدمة.

#### مثال على سير العمل
1. حلل الكود المصدري أو البايت كود لـ Java باستخدام مكتبة مثل ASM.
2. حدد جميع المتغيرات المحلية والعبارات.
3. أدخل استدعاءات التسجيل (مثال: `System.out.println("Variable x = " + x)`) قبل أو بعد كل عبارة.
4. ترجم وشغّل الكود المعدل.

نادرًا ما يكون هذا النهج عمليًا للمشاريع الكبيرة due to التعقيد وتحميل الأداء.

---

### 6. **الأدوات الحالية للتتبع والتوصيف**
يمكن أن تساعدك عدة أدوات في تتبع وتسجيل تنفيذ البرنامج دون تعديل الكود الخاص بك:

- **Java Flight Recorder (JFR)**:
  - فعّل JFR مع أعلام JVM:
    ```bash
    java -XX:StartFlightRecording=settings=profile,dumponexit=true,filename=recording.jfr MyApp
    ```
  - حلل التسجيلات باستخدام JDK Mission Control لعرض استدعاءات الدوال وتتبع المكدس والأحداث.
  - **القيود**: لا يسجل كل متغير ولكنه يوفر تتبعًا مفصلًا للتنفيذ.

- **VisualVM**:
  - أداة توصيف يمكنها مراقبة استدعاءات الدوال واستخدام الذاكرة ونشاط وحدة المعالجة المركزية.
  - استخدم مع البرنامج المساعد VisualVM-MBeans لتسجيل متغيرات أو حالات محددة.
  - **القيود**: يتطلب تكوينًا يدويًا لتسجيل المتغيرات.

- **BTrace**:
  - أداة تتبع ديناميكية لـ Java تسمح لك بحق منطق التتبع في JVM قيد التشغيل.
  - نموذج نصي:

    ```java
    import com.sun.btrace.annotations.*;
    import static com.sun.btrace.BTraceUtils.*;

    @BTrace
    public class TraceVariables {
        @OnMethod(clazz = "MyApp", method = "main")
        public static void trace(@ProbeMethodName String methodName, @AllLocals Object[] locals) {
            println("Method: " + methodName + ", Locals: " + Arrays.toString(locals));
        }
    }
    ```
  - **القيود**: يتطلب كتابة نصوص بحذر وقد لا يلتقط جميع المتغيرات المحلية بسهولة.

---

### التوصية
لا يوجد علم JVM واحد يسجل كل متغير وحالة تلقائيًا لكل عبارة، لأن هذا سيكون غير عملي due to الأداء وحجم المخرجات. بدلاً من ذلك، ضع في اعتبارك ما يلي بناءً على احتياجاتك:

- **للتطوير**: استخدم مصحح أخطاء (مثل IntelliJ IDEA) مع نقاط توقف ونقاط سجل للتحكم الدقيق.
- **للتسجيل الآلي**: استخدم إطار تسجيل (SLF4J/Logback) مع عبارات السجل اليدوية أو AspectJ للتسجيل على مستوى الدالة.
- **لحالات الاستخدام المتقدمة**: نفذ وكيل Java مع Byte Buddy أو استخدم BTrace للتتبع الديناميكي.
- **لرصد الإنتاج**: استخدم Java Flight Recorder أو VisualVM للتوصيف دون تغييرات في الكود.

إذا كنت تريد تسجيل متغيرات أو دوال محددة تلقائيًا، يمكنني مساعدتك في إعداد تكوين وكيل Java أو AspectJ. بدلاً من ذلك، إذا كان لديك مقتطف كود محدد، يمكنني أن أوضح لك كيفية إضافة التسجيل أو تصحيحه بشكل فعال. دعني أعرف تفضيلاتك أو قيودك!