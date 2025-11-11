---
audio: false
generated: true
lang: ar
layout: post
title: استخدام SpringRunner في اختبارات جافا
translated: true
type: note
---

لاستخدام `SpringRunner` مع مشغل `@RunWith` الخاص بـ JUnit في اختبارات Java، اتبع هذه الخطوات. لاحظ أنني أفترض أن "SpringRuner" في استفسارك هو خطأ مطبعي وأنك تقصد `SpringRunner`. إليك دليلًا كاملًا:

### الخطوة 1: إضافة تبعية Spring Test
لاستخدام `SpringRunner`، تحتاج إلى وحدة Spring Test في مشروعك. إذا كنت تستخدم Maven، أضف هذه التبعية إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```

استبدل `${spring.version}` بإصدار Spring الذي تستخدمه (مثل `5.3.22`). إذا كنت تستخدم Gradle، أضف هذا إلى ملف `build.gradle` الخاص بك:

```gradle
testImplementation 'org.springframework:spring-test:${springVersion}'
```

هذا يضمن أن `SpringRunner` وأدوات اختبار Spring الأخرى متاحة.

### الخطوة 2: ضع شرح `@RunWith(SpringRunner.class)` على فئة الاختبار
يخبر شرح `@RunWith` JUnit باستخدام مشغل محدد بدلاً من المشغل الافتراضي. للتكامل مع Spring، استخدم `SpringRunner`، الذي هو جزء من إطار عمل Spring TestContext. أضف هذا الشرح إلى فئة الاختبار الخاصة بك:

```java
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class MyServiceTest {
    // كود الاختبار يذهب هنا
}
```

يُمكّن `SpringRunner` ميزات Spring مثل حقن التبعية وتحميل السياق في اختباراتك. لاحظ أن `@RunWith` هو شرح خاص بـ JUnit 4، لذا يفترض هذا النهج أنك تستخدم JUnit 4. بالنسبة لـ JUnit 5، ستستخدم `@ExtendWith(SpringExtension.class)` بدلاً من ذلك، لكن ذكرك لـ "RunWith runner" يشير إلى JUnit 4.

### الخطوة 3: تكوين سياق تطبيق Spring باستخدام `@ContextConfiguration`
لاستخدام حبوب (beans) المدارة بواسطة Spring في اختباراتك، تحتاج إلى تحميل سياق تطبيق Spring. يحدد شرح `@ContextConfiguration` كيفية القيام بذلك. على سبيل المثال، إذا كان لديك فئة تكوين (مثل `AppConfig`)، استخدم:

```java
import org.springframework.test.context.ContextConfiguration;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    // كود الاختبار يذهب هنا
}
```

إذا كان التكوين الخاص بك في ملف XML (مثل `applicationContext.xml`)، استخدم:

```java
@ContextConfiguration(locations = "classpath:applicationContext.xml")
```

هذا يخبر `SpringRunner` بالحبوب والتكوينات التي يجب تحميلها للاختبار.

### الخطوة 4: حقن حبوب Spring باستخدام `@Autowired`
بمجرد تحميل السياق، يمكنك حقن الحبوب المدارة بواسطة Spring في فئة الاختبار الخاصة بك باستخدام `@Autowired`. على سبيل المثال، إذا كان لديك خدمة تسمى `MyService`:

```java
import org.springframework.beans.factory.annotation.Autowired;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    // طرق الاختبار تذهب هنا
}
```

هذا يسمح لك باستخدام الحبوب المحقونة في اختباراتك.

### الخطوة 5: اكتب طرق الاختبار باستخدام `@Test`
عرّف طرق الاختبار الخاصة بك باستخدام شرح `@Test` الخاص بـ JUnit. على سبيل المثال:

```java
import org.junit.Test;
import static org.junit.Assert.assertEquals;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    @Test
    public void testMyServiceMethod() {
        String result = myService.doSomething();
        assertEquals("النتيجة المتوقعة", result);
    }
}
```

يحدد شرح `@Test` الطرق التي يجب على JUnit تنفيذها كاختبارات. باستخدام `SpringRunner`، يمكن لهذه الطرق التفاعل مع سياق Spring.

### مثال: تجميع كل شيء معًا
إليك مثالاً كاملاً:

```java
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringRunner;
import static org.junit.Assert.assertEquals;

// فئة التكوين للاختبار
@Configuration
class AppConfig {
    @Bean
    public MyService myService() {
        return new MyService();
    }
}

// فئة الخدمة المطلوب اختبارها
class MyService {
    public String doSomething() {
        return "Hello, Spring!";
    }
}

// فئة الاختبار
@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    @Test
    public void testMyServiceMethod() {
        String result = myService.doSomething();
        assertEquals("Hello, Spring!", result);
    }
}
```

### ملاحظات إضافية
- **الغرض**: `SpringRunner` مثالي لاختبارات التكامل حيث تحتاج إلى حقن التبعية أو ميزات السياق الخاصة بـ Spring. لاختبارات الوحدة، فكر في استخدام Mockito أو JUnit العادي بدلاً من ذلك.
- **المشاكل الشائعة**: تأكد من تضمين تبعية `spring-test`، وإلا ستواجه أخطاء مثل `ClassNotFoundException`. أيضًا، تحقق من أن `@ContextConfiguration` يشير إلى تكوين صالح.
- **الشروحات الاختيارية**: استخدم `@Transactional` للاختبارات التي تعدل قاعدة البيانات (للتراجع عن التغييرات) أو `@ActiveProfiles` لتحديد ملف تعريف (مثل "test").

يسمح لك هذا الإعداد بتشغيل اختبارات JUnit مع دعم اختبار Spring، والاستفادة من ميزات مثل حقن التبعية وإدارة السياق.