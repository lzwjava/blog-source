---
audio: true
generated: true
lang: ar
layout: post
title: Swagger Annotations
translated: true
---

لاستخدام حزمة `swagger-annotations` في مشروعك Java، خاصة لتوثيق API REST مبني باستخدام Spring Boot، اتبع هذه الخطوات. يتوقع هذا الدليل أنك تستخدم Swagger 2.0، والذي يتم دمجه عادة مع مكتبة `springfox`. توفر حزمة `swagger-annotations` تعليقات لتضيف البيانات الوصفية إلى نقاط النهاية الخاصة بك، مما يسمح بإنشاء وثائق API تلقائيًا.

---

### الخطوة 1: إضافة الاعتماديات المطلوبة

يجب عليك تضمين حزمة `swagger-annotations` ومكتبة دمج Swagger (مثل `springfox`) في مشروعك. إذا كنت تستخدم Maven، أضف الاعتماديات التالية إلى ملف `pom.xml` الخاص بك:

```xml
<!-- تعليقات Swagger -->
<dependency>
    <groupId>io.swagger</groupId>
    <artifactId>swagger-annotations</artifactId>
    <version>1.6.2</version>
</dependency>

<!-- Springfox Swagger 2 لتكامل Swagger -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
</dependency>

<!-- Springfox Swagger UI لتوثيق التفاعلي -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.9.2</version>
</dependency>
```

- **`io.swagger:swagger-annotations`**: توفر التعليقات لـ Swagger 2.0.
- **`springfox-swagger2`**: يدمج Swagger مع Spring Boot ويعمل على التعليقات.
- **`springfox-swagger-ui`**: يضيف واجهة ويب لعرض الوثائق المولدة.

> **ملاحظة**: تحقق من أحدث الإصدارات على [Maven Repository](https://mvnrepository.com/) حيث قد تكون هذه الإصدارات (1.6.2 لـ `swagger-annotations` و 2.9.2 لـ `springfox`) قد تم تحديثها.

---

### الخطوة 2: تكوين Swagger في تطبيقك

لتفعيل Swagger وسمح له بملء API الخاص بك للبحث عن التعليقات، قم بإنشاء فئة تكوين تحتوي على Bean `Docket`. أضف هذا إلى تطبيق Spring Boot الخاص بك:

```java
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@EnableSwagger2
public class SwaggerConfig {
    @Bean
    public Docket api() {
        return new Docket(DocumentationType.SWAGGER_2)
                .select()
                .apis(RequestHandlerSelectors.any()) // ملء جميع الموجهات
                .paths(PathSelectors.any())          // تضمين جميع المسارات
                .build();
    }
}
```

- **`@EnableSwagger2`**: يفعّل دعم Swagger 2.0.
- **`Docket`**: يحدد أي نقاط النهاية لتوثيقها. يحدد الإعداد أعلاه ملء جميع الموجهات والمسارات، ولكن يمكنك تخصيصه (مثل `RequestHandlerSelectors.basePackage("com.example.controllers")`) لتقييد النطاق.

---

### الخطوة 3: استخدام تعليقات Swagger في كودك

توفر حزمة `swagger-annotations` تعليقات لتوصيف API الخاص بك. استخدم هذه التعليقات في فئات الموجهات، الأطوار، المعلمات، والموديلات. أدناه تعليقات شائعة مع أمثلة:

#### تعليق على الموجه

استخدم `@Api` لتوصيف الموجه:

```java
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "User Controller", description = "عمليات تتعلق بالمستخدمين")
@RestController
@RequestMapping("/users")
public class UserController {
    // الأطوار هنا
}
```

- **`value`**: اسم قصير للAPI.
- **`description`**: شرح موجز لما يفعله الموجه.

#### تعليق على عمليات API

استخدم `@ApiOperation` لتوصيف نقاط النهاية الفردية:

```java
import io.swagger.annotations.ApiOperation;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Get a user by ID", response = User.class)
@GetMapping("/{id}")
public ResponseEntity<User> getUserById(@PathVariable Long id) {
    // التنفيذ
    return ResponseEntity.ok(new User(id, "John Doe"));
}
```

- **`value`**: ملخص للعملية.
- **`response`**: نوع الإرجاع المتوقع.

#### وصف المعلمات

استخدم `@ApiParam` للمعلمات الأطوار:

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

@ApiOperation(value = "Create a new user")
@PostMapping
public ResponseEntity<User> createUser(
        @ApiParam(value = "User object to be created", required = true)
        @RequestBody User user) {
    // التنفيذ
    return ResponseEntity.ok(user);
}
```

- **`value`**: يصف المعلمة.
- **`required`**: يشير إلى ما إذا كانت المعلمة مطلوبة.

#### تحديد الإجابات

استخدم `@ApiResponses` و `@ApiResponse` لتوثيق الإجابات HTTP المحتملة:

```java
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponses;
import io.swagger.annotations.ApiResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Delete a user")
@ApiResponses(value = {
    @ApiResponse(code = 200, message = "User deleted successfully"),
    @ApiResponse(code = 404, message = "User not found")
})
@DeleteMapping("/{id}")
public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
    // التنفيذ
    return ResponseEntity.ok().build();
}
```

- **`code`**: رمز حالة HTTP.
- **`message`**: وصف الإجابة.

#### وصف النماذج

لأجهزة نقل البيانات (DTOs)، استخدم `@ApiModel` و `@ApiModelProperty`:

```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(description = "User data transfer object")
public class User {
    @ApiModelProperty(notes = "The user's unique identifier", example = "1")
    private Long id;

    @ApiModelProperty(notes = "The user's name", example = "John Doe")
    private String name;

    // getter و setter
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public User(Long id, String name) {
        this.id = id;
        this.name = name;
    }
}
```

- **`@ApiModel`**: يصف النموذج.
- **`@ApiModelProperty`**: يحدد كل حقل، مع أمثلة اختيارية.

---

### الخطوة 4: تشغيل وفتح الوثائق

1. قم بتشغيل تطبيق Spring Boot الخاص بك.
2. افتح متصفح ويب واذهب إلى:
   **http://localhost:8080/swagger-ui.html**
   يفتح هذا الرابط واجهة Swagger UI، وهي واجهة تفاعلية تعرض وثائق API بناءً على التعليقات.

---

### ملخص كيفية استخدام `swagger-annotations`

1. **إضافة الاعتماديات**: أضف `swagger-annotations` و `springfox` إلى ملف `pom.xml`.
2. **تكوين Swagger**: قم بإعداد Bean `Docket` لتفعيل ملء Swagger.
3. **تعليق على كودك**:
   - `@Api` للموجهات.
   - `@ApiOperation` للأطوار.
   - `@ApiParam` للمعلمات.
   - `@ApiResponses` و `@ApiResponse` لتفاصيل الإجابات.
   - `@ApiModel` و `@ApiModelProperty` لأجهزة نقل البيانات.
4. **عرض الوثائق**: افتح واجهة Swagger UI في `/swagger-ui.html`.

---

### ملاحظات إضافية

- **Swagger 2.0 مقابل OpenAPI 3.0**: يستخدم هذا الدليل Swagger 2.0 مع `io.swagger:swagger-annotations`. لاستخدام OpenAPI 3.0، استخدم `io.swagger.core.v3:swagger-annotations` ومكتبة مثل `springdoc-openapi`، والتي تغير بعض أسماء التعليقات (مثل `@Tag` بدلاً من `@Api`).
- **التخصيص**: قم بتعديل تكوين `Docket` لتصفية حزم أو مسارات محددة للحصول على وثائق أكثر تركيزًا.
- **الجودة**: قدم وصفات واضحة ومفصلة في التعليقات لتحسين فائدة الوثائق المولدة.

بالتتبع لهذه الخطوات، يمكنك استخدام حزمة `swagger-annotations` لتوثيق API REST الخاص بك بشكل فعال، مما يجعل من السهل على المطورين والمستهلكين فهم وتفاعل مع نقاط النهاية الخاصة بك.