---
audio: false
generated: true
lang: ar
layout: post
title: جدولة المهام في سبرينغ
translated: true
type: note
---

جدولة المهام في Spring هي متطلب شائع لأتمتة الوظائف المتكررة، مثل إرسال البريد الإلكتروني، أو إنشاء التقارير، أو تنفيذ صيانة النظام. تقدم Spring ميزة قوية وسهلة الاستخدام لجدولة المهام من خلال حاشية `@Scheduled` و Spring Task Scheduler. أدناه، سأرشدك خلال الخطوات لإعدادها وسأشرح المفاهيم الأساسية.

### 1. **تمكين الجدولة في تطبيق Spring الخاص بك**
لاستخدام الجدولة، تحتاج إلى تمكينها في تطبيق Spring الخاص بك. يتم ذلك بإضافة حاشية `@EnableScheduling` إلى فئة التكوين.

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableScheduling;

@Configuration
@EnableScheduling
public class SchedulerConfig {
    // يمكن أن تكون فئة التكوين فارغة ما لم تكن بحاجة إلى إعدادات مجدول مخصصة
}
```

يخبر هذا Spring بالبحث عن الطرق المشروحة بـ `@Scheduled` وتنفيذها وفقًا لجدولها الزمني المحدد.

---

### 2. **إنشاء مهمة مجدولة**
يمكنك تحديد طريقة في أي حبة Spring مُدارة (مثل `@Component` أو `@Service`) ووضع حاشية `@Scheduled` عليها. إليك مثال:

```java
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

@Component
public class MyScheduledTasks {

    // يعمل كل 5 ثوانٍ
    @Scheduled(fixedRate = 5000)
    public void performTask() {
        System.out.println("Task executed at: " + System.currentTimeMillis());
    }
}
```

في هذا المثال:
- `@Component` يجعل الفئة حبة Spring.
- `@Scheduled(fixedRate = 5000)` يشغل الطريقة كل 5 ثوانٍ (5000 ميلي ثانية).

---

### 3. **خيارات الجدولة المتاحة**
تقدم Spring عدة طرق لتحديد موعد تشغيل المهمة:

#### أ) **معدل ثابت**
- ينفذ المهمة على فترات ثابتة، بغض النظر عن المدة التي تستغرقها المهمة.
- مثال: `@Scheduled(fixedRate = 5000)` (كل 5 ثوانٍ).

#### ب) **تأخير ثابت**
- ينفذ المهمة بتأخير ثابت بين نهاية تنفيذ واحد وبداية التنفيذ التالي.
- مثال: `@Scheduled(fixedDelay = 5000)` (5 ثوانٍ بعد انتهاء المهمة السابقة).

#### ج) **تعبير Cron**
- يستخدم صيغة تشبه cron للجداول الزمنية الأكثر تعقيدًا (مثل "كل يوم عمل في الساعة 9 صباحًا").
- مثال: `@Scheduled(cron = "0 0 9 * * MON-FRI")`.

#### د) **تأخير أولي**
- يؤخر التنفيذ الأول للمهمة. ادمج مع `fixedRate` أو `fixedDelay`.
- مثال: `@Scheduled(fixedRate = 5000, initialDelay = 10000)` (يبدأ بعد 10 ثوانٍ، ثم يعمل كل 5 ثوانٍ).

---

### 4. **أساسيات صيغة Cron**
إذا كنت تستخدم cron، فإليك مرجع سريع:
- التنسيق: `ثانية دقيقة ساعة يوم-الشهر شهر يوم-الأسبوع`
- مثال: `@Scheduled(cron = "0 15 10 * * ?")` (يعمل في الساعة 10:15 صباحًا كل يوم).

| الحقل         | القيم المسموحة       |
|---------------|----------------------|
| الثانية      | 0-59                |
| الدقيقة       | 0-59                |
| الساعة        | 0-23                |
| يوم الشهر    | 1-31                |
| الشهر         | 1-12 أو JAN-DEC     |
| يوم الأسبوع  | 0-7 أو SUN-SAT (0 أو 7 هو الأحد) |

يمكن استخدام أحرف خاصة مثل `*` (الكل)، `,` (قائمة)، `-` (نطاق)، `/` (زيادة).

---

### 5. **التبعيات**
إذا كنت تستخدم Spring Boot، فإن ميزة الجدولة مضمنة افتراضيًا في تبعية `spring-boot-starter`. لمشروع Spring غير Boot، تأكد من وجود:

```xml
<dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.3</version> <!-- استخدم أحدث إصدار -->
</dependency>
```

---

### 6. **مثال كامل مع Spring Boot**
إليك مثالاً كاملاً لـ Spring Boot:

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
        System.out.println("Running every 5 seconds: " + System.currentTimeMillis());
    }

    @Scheduled(cron = "0 */1 * * * *")
    public void runEveryMinute() {
        System.out.println("Running every minute: " + System.currentTimeMillis());
    }
}
```

---

### 7. **تخصيص المجدول (اختياري)**
افتراضيًا، يستخدم Spring مجدولًا أحادي الخيط. إذا كنت بحاجة إلى تنفيذ مهام متزامنة، يمكنك تكوين `TaskScheduler` مخصص:

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

يسمح هذا بتشغيل مهام متعددة بالتوازي.

---

### 8. **اختبار المهام المجدولة الخاصة بك**
- شغل تطبيقك وتحقق من سجلات وحدة التحكم للتحقق من أن المهام تنفذ كما هو متوقع.
- استخدم فترات زمنية أقصر (مثل كل ثانيتين) أثناء الاختبار لرؤية النتائج بسرعة.