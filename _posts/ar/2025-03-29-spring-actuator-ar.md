---
audio: false
generated: true
lang: ar
layout: post
title: أكتواتور سبرينغ
translated: true
type: note
---

Spring Actuator هي ميزة قوية في Spring Boot توفر أدوات جاهزة للإنتاج لمراقبة وإدارة تطبيقك. إليك دليل خطوة بخطوة حول كيفية استخدامها:

### 1. **إضافة تبعية Spring Actuator**
لاستخدام Spring Actuator، تحتاج إلى تضمين تبعيتها في مشروعك. إذا كنت تستخدم Maven، أضف هذا إلى ملف `pom.xml` الخاص بك:

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
```

أما إذا كنت تستخدم Gradle، أضف هذا إلى ملف `build.gradle` الخاص بك:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-actuator'
```

### 2. **بدء تشغيل تطبيق Spring Boot الخاص بك**
بمجرد إضافة التبعية، قم بتشغيل تطبيق Spring Boot الخاص بك. سيقوم Spring Actuator تلقائيًا بتمكين مجموعة من النقاط الطرفية (endpoints) التي يمكنك استخدامها لمراقبة تطبيقك والتفاعل معه.

### 3. **الوصول إلى النقاط الطرفية الافتراضية**
يعرض Spring Actuator عدة نقاط طرفية عبر HTTP بشكل افتراضي. المسار الأساسي هو `/actuator`. فيما يلي بعض النقاط الطرفية شائعة الاستخدام (بافتراض أن تطبيقك يعمل على `localhost:8080`):
- **فحص الصحة**: `http://localhost:8080/actuator/health`
  - يُرجع حالة تطبيقك (مثال: `{"status":"UP"}`).
- **معلومات التطبيق**: `http://localhost:8080/actuator/info`
  - يعرض معلومات تطبيقية اختيارية (قابلة للتكوين).
- **المقاييس**: `http://localhost:8080/actuator/metrics`
  - يوفر مقاييس مفصلة مثل استخدام الذاكرة، وحدة المعالجة المركزية، والمزيد.

بشكل افتراضي، يتم تمكين `/health` و `/info` فقط لأسباب أمنية. لكشف المزيد من النقاط الطرفية، تحتاج إلى تكوينها.

### 4. **تكوين نقاط طرفية Actuator**
يمكنك تخصيص النقاط الطرفية التي يتم كشفها في ملف `application.properties` أو `application.yml` الخاص بك. على سبيل المثال:

#### `application.properties`
```properties
# تمكين نقاط طرفية محددة
management.endpoints.web.exposure.include=health,info,metrics,beans

# تغيير المسار الأساسي (اختياري)
management.endpoints.web.base-path=/manage
```

#### `application.yml`
```yaml
management:
  endpoints:
    web:
      exposure:
        include: health, info, metrics, beans
      base-path: /manage
```

باستخدام هذا التكوين، ستكون النقاط الطرفية مثل `/manage/metrics` أو `/manage/beans` متاحة.

### 5. **استكشاف النقاط الطرفية المتاحة**
فيما يلي بعض نقاط طرفية Actuator المفيدة التي يمكنك تمكينها:
- `/actuator/beans`: يسرد جميع Spring beans في تطبيقك.
- `/actuator/env`: يعرض خصائص البيئة.
- `/actuator/loggers`: يعرض ويعدل مستويات المسجلات (loggers).
- `/actuator/shutdown`: يُوقف التطبيق بشكل متحكم (معطل بشكل افتراضي).

لتمكين جميع النقاط الطرفية لأغراض الاختبار، استخدم:
```properties
management.endpoints.web.exposure.include=*
```

### 6. **تأمين نقاط طرفية Actuator**
نظرًا لأن Actuator يعرض بيانات حساسة، يجب عليك تأمينه في بيئة الإنتاج:
- أضف Spring Security:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```
- قم بتكوين الأمان في `application.properties`:
```properties
spring.security.user.name=admin
spring.security.user.password=secret
management.endpoints.web.exposure.include=health,metrics
```
الآن، سيتطلب الوصول إلى النقاط الطرفية المصادقة (مثال: `admin:secret`).

### 7. **إضافة فحوصات صحة مخصصة (اختياري)**
يمكنك إنشاء مؤشرات صحة مخصصة من خلال تنفيذ واجهة `HealthIndicator`. مثال:

```java
import org.springframework.boot.actuate.health.Health;
import org.springframework.boot.actuate.health.HealthIndicator;
import org.springframework.stereotype.Component;

@Component
public class CustomHealthCheck implements HealthIndicator {
    @Override
    public Health health() {
        boolean isHealthy = checkSomeCondition();
        if (isHealthy) {
            return Health.up().withDetail("customCheck", "All good!").build();
        }
        return Health.down().withDetail("customCheck", "Something's wrong").build();
    }

    private boolean checkSomeCondition() {
        // منطقك هنا
        return true;
    }
}
```

سيظهر هذا في نقطة الطرف `/actuator/health`.

### 8. **مراقبة المقاييس**
للتعمق أكثر في المقاييس، قم بتمكين `/metrics` واستكشف المقاييس المحددة مثل:
- `http://localhost:8080/actuator/metrics/jvm.memory.used`
- `http://localhost:8080/actuator/metrics/http.server.requests`

يمكنك التكامل مع أدوات مثل Prometheus أو Grafana للمراقبة المتقدمة.

### 9. **اختبرها**
شغّل تطبيقك واختبر النقاط الطرفية باستخدام متصفح، أو `curl`، أو أدوات مثل Postman. على سبيل المثال:
```bash
curl http://localhost:8080/actuator/health
```

### نصائح
- استخدم `/actuator/info` لعرض معلومات مخصصة (مثل إصدار التطبيق) عن طريق إضافة:
```properties
info.app.name=MyApp
info.app.version=1.0.0
```
- أعد تشغيل تطبيقك بعد إجراء تغييرات على التكوين.

هذه هي الأساسيات! أعلمني إذا كنت تريد مساعدة في حالة استخدام محددة أو استكشاف الأخطاء وإصلاحها.