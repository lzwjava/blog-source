---
audio: false
lang: ar
layout: post
title: جدولة المهام في Spring
translated: true
---

### 1. **تفعيل الجدولة في تطبيق Spring الخاص بك**
لاستخدام الجدولة، عليك تفعيلها في تطبيق Spring الخاص بك. يتم ذلك بإضافة تعليق `@EnableScheduling` إلى فئة التكوين.

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@EnableScheduling
public class SchedulerConfig {
    // يمكن أن تكون فئة التكوين فارغة ما لم تحتاج إلى إعدادات الجدول الزمني المخصصة
}
```

هذا يوضح Spring البحث عن الأساليب التي تم تعليقها بـ `@Scheduled` و تنفيذها وفقًا لجداولها المحددة.

---

### 2. **إنشاء مهمة لتجديدها**
يمكنك تعريف طريقة في أي Bean مدار من Spring (مثل `@Component` أو `@Service`) وتعليقها بـ `@Scheduled`. إليك مثالًا:

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class MyScheduledTasks {

    // يتم تنفيذها كل 5 ثوان
    @Scheduled(fixedRate = 5000)
    public void performTask() {
        System.out.println("تم تنفيذ المهمة في: " + System.currentTimeMillis());
    }
}
```

في هذا المثال:
- `@Component` يجعل الفئة Bean من Spring.
- `@Scheduled(fixedRate = 5000)` يقوم بتنفيذ الطريقة كل 5 ثوان (5000 مللي ثانية).

---

### 3. **أنواع خيارات الجدولة**
يوفر Spring عدة طرق لتحديد متى يجب تنفيذ المهمة:

#### a) **معدل ثابت**
- يقوم بتنفيذ المهمة بمعدل ثابت، بغض النظر عن مدة تنفيذ المهمة.
- مثال: `@Scheduled(fixedRate = 5000)` (كل 5 ثوان).

#### b) **تأخير ثابت**
- يقوم بتنفيذ المهمة مع تأخير ثابت بين نهاية تنفيذ واحد و بداية التالي.
- مثال: `@Scheduled(fixedDelay = 5000)` (5 ثوان بعد انتهاء المهمة السابقة).

#### c) **تعبير Cron**
- يستخدم صيغة تشبه Cron لمواعيد أكثر تعقيدًا (مثل "كل يوم عمل في الساعة 9 صباحًا").
- مثال: `@Scheduled(cron = "0 0 9 * * MON-FRI")`.

#### d) **تأخير أولي**
- يؤخر تنفيذ المهمة الأولى. يمكن دمجه مع `fixedRate` أو `fixedDelay`.
- مثال: `@Scheduled(fixedRate = 5000, initialDelay = 10000)` (يبدأ بعد 10 ثوان، ثم يعمل كل 5 ثوان).

---

### 4. **أساسيات صيغة Cron**
إذا كنت تستخدم Cron، إليك مرجع سريع:
- الصيغة: `ثانية دقيقة ساعة يوم الشهر شهر يوم الأسبوع`
- مثال: `@Scheduled(cron = "0 15 10 * * ?")` (يعمل في الساعة 10:15 صباحًا كل يوم).

| الحقل         | القيم المسموح بها       |
|---------------|----------------------|
| الثانية        | 0-59                |
| الدقيقة        | 0-59                |
| الساعة          | 0-23                |
| يوم الشهر  | 1-31                |
| الشهر         | 1-12 أو JAN-DEC     |
| يوم الأسبوع   | 0-7 أو SUN-SAT (0 أو 7 هو الأحد) |

يمكن استخدام رموز خاصة مثل `*` (جميع) `,` (قائمة) `-` (نطاق) `/` (زيادة).

---

### 5. **التعليقات**
إذا كنت تستخدم Spring Boot، فإن ميزة الجدولة مدمجة بشكل افتراضي في تعليق `spring-boot-starter`. بالنسبة لمشروع Spring غير Boot، تأكد من أن لديك:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.3</version> <!-- استخدم أحدث الإصدار -->
</dependency>
```

---

### 6. **مثال كامل مع Spring Boot**
إليك مثال Spring Boot كامل:

```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@SpringBootApplication
@EnableScheduling
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}

@Component
class ScheduledTasks {

    @Scheduled(fixedRate = 5000)
    public void runEveryFiveSeconds() {
        System.out.println("يعمل كل 5 ثوان: " + System.currentTimeMillis());
    }

    @Scheduled(cron = "0 */1 * * * *")
    public void runEveryMinute() {
        System.out.println("يعمل كل دقيقة: " + System.currentTimeMillis());
    }
}
```

---

### 7. **تخصيص الجدول الزمني (اختياري)**
بالتعليمات الافتراضية، يستخدم Spring جدول زمني ذو خيط واحد. إذا كنت تحتاج إلى تنفيذ مهام متزامنة، يمكنك تكوين جدول زمني مخصص `TaskScheduler`:

```java
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.concurrent.ThreadPoolTaskScheduler;

@Configuration
public class SchedulerConfig {

    @Bean
    public ThreadPoolTaskScheduler taskScheduler() {
        ThreadPoolTaskScheduler scheduler = new ThreadPoolTaskScheduler();
        scheduler.setPoolSize(10); // عدد الخيوط
        scheduler.setThreadNamePrefix("my-scheduler-");
        return scheduler;
    }
}
```

هذا يسمح لعدة مهام بالعمل بشكل متزامن.

---

### 8. **اختبار مهامك المجدولة**
- قم بتشغيل تطبيقك وتحقق من سجلات الواجهة الأمامية لتأكيد أن المهام تعمل كما هو متوقع.
- استخدم فترات أقصر (مثل كل 2 ثوان) أثناء الاختبار لرؤية النتائج بسرعة.