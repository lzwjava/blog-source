---
audio: true
generated: true
lang: ar
layout: post
title: استخدام SpringRunner في اختبارات Java
translated: true
---

لاستخدام `SpringRunner` مع جونيت `@RunWith` في اختبارات جافا، اتبع هذه الخطوات. يلاحظ أن هناك خطأ في كتابة "SpringRuner" في استفسارك، وأنك تقصد `SpringRunner`. إليك دليل كامل:

### الخطوة 1: إضافة التبعية للاختبار في سبرينغ
لاستخدام `SpringRunner`، تحتاج إلى وحدة اختبار سبرينغ في مشروعك. إذا كنت تستخدم مافن، أضف هذه التبعية إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-test</artifactId>
    <version>${spring.version}</version>
    <scope>test</scope>
</dependency>
```

استبدل `${spring.version}` بالنسخة التي تستخدمها من سبرينغ (مثلًا `5.3.22`). إذا كنت تستخدم غرادل، أضف هذا إلى ملف `build.gradle` الخاص بك:

```gradle
testImplementation 'org.springframework:spring-test:${springVersion}'
```

هذا يضمن توفر `SpringRunner` وخدمات اختبار سبرينغ الأخرى.

### الخطوة 2: تعليق الفئة الاختبار مع `@RunWith(SpringRunner.class)`
تعليق `@RunWith` يوضح لجونيت استخدام جاري خاص بدلاً من الجاري الافتراضي. لاستخدام سبرينغ، استخدم `SpringRunner`، وهو جزء من إطار عمل Spring TestContext. أضف هذا التعليق إلى فئة الاختبار:

```java
import org.junit.runner.RunWith;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
public class MyServiceTest {
    // كود الاختبار هنا
}
```

يتيح لك `SpringRunner` استخدام ميزات سبرينغ مثل حقن الاعتماد وتحميل السياق في اختباراتك. يلاحظ أن `@RunWith` هو تعليق لجونيت 4، لذلك فإن هذا النهج يفترض أنك تستخدم جونيت 4. لجونيت 5، يمكنك استخدام `@ExtendWith(SpringExtension.class)` بدلاً من ذلك، ولكن ذكرك لـ "RunWith runner" يشير إلى جونيت 4.

### الخطوة 3: تهيئة السياق التطبيقي لسبرينغ مع `@ContextConfiguration`
لاستخدام الكائنات التي يديرها سبرينغ في اختباراتك، تحتاج إلى تحميل السياق التطبيقي لسبرينغ. تعليق `@ContextConfiguration` يوضح كيفية القيام بذلك. على سبيل المثال، إذا كان لديك فئة تهيئة (مثلًا `AppConfig`), استخدم:

```java
import org.springframework.test.context.ContextConfiguration;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    // كود الاختبار هنا
}
```

إذا كانت تهيئةك في ملف XML (مثلًا `applicationContext.xml`), استخدم:

```java
@ContextConfiguration(locations = "classpath:applicationContext.xml")
```

هذا يوضح لـ `SpringRunner` أي الكائنات والتهيئات التي يجب تحميلها للاختبار.

### الخطوة 4: حقن الكائنات لسبرينغ مع `@Autowired`
بعد تحميل السياق، يمكنك حقن الكائنات التي يديرها سبرينغ في فئة الاختبار باستخدام `@Autowired`. على سبيل المثال، إذا كان لديك خدمة تسمى `MyService`:

```java
import org.springframework.beans.factory.annotation.Autowired;

@RunWith(SpringRunner.class)
@ContextConfiguration(classes = AppConfig.class)
public class MyServiceTest {
    @Autowired
    private MyService myService;

    // طرق الاختبار هنا
}
```

هذا يتيح لك استخدام الكائن المحقون في اختباراتك.

### الخطوة 5: كتابة طرق الاختبار مع `@Test`
حدد طرق الاختبار باستخدام تعليق `@Test` لجونيت. على سبيل المثال:

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
        assertEquals("Expected result", result);
    }
}
```

تعليق `@Test` يحدد الطرق التي يجب على جونيت تنفيذها كاختبارات. مع `SpringRunner`، يمكن لهذه الطرق التفاعل مع السياق لسبرينغ.

### مثال: جمع كل شيء معًا
هنا مثال كامل:

```java
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringRunner;
import static org.junit.Assert.assertEquals;

// فئة التهيئة للاختبار
@Configuration
class AppConfig {
    @Bean
    public MyService myService() {
        return new MyService();
    }
}

// فئة الخدمة للاختبار
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
- **الغرض**: `SpringRunner` مثالي للاختبارات التكاملية حيث تحتاج إلى حقن الاعتماد لسبرينغ أو ميزات السياق. للاختبارات الوحدوية، فكر في استخدام Mockito أو جونيت العادي.
- **المشاكل الشائعة**: تأكد من تضمين التبعية `spring-test` وإلا ستواجه أخطاء مثل `ClassNotFoundException`. أيضًا، تأكد من أن `@ContextConfiguration` يشير إلى تهيئة صالحة.
- **تعليقات اختيارية**: استخدم `@Transactional` للاختبارات التي تغير قاعدة البيانات (لإرجاع التغييرات) أو `@ActiveProfiles` لتحديد ملف (مثلًا "test").

هذا الإعداد يتيح لك تشغيل اختبارات جونيت مع دعم اختبار سبرينغ، واستغلال الميزات مثل حقن الاعتماد وإدارة السياق.