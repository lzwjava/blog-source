---
audio: false
generated: true
lang: ar
layout: post
title: شرح توضيحات Swagger
translated: true
type: note
---

لاستخدام حزمة `swagger-annotations` في مشروع جافا الخاص بك، خاصة لتوثيق واجهة برمجة تطبيقات REST المبنية باستخدام Spring Boot، اتبع هذه الخطوات. يفترض هذا الدليل أنك تستخدم Swagger 2.0، والذي يتم دمجه عادةً مع مكتبة `springfox`. توفر حزمة `swagger-annotations` تعريفات (annotations) لإضافة بيانات وصفية إلى نقاط نهاية واجهة برمجة التطبيقات الخاصة بك، مما يتيح إنشاء توثيق تلقائي لواجهة برمجة التطبيقات.

---

### الخطوة 1: إضافة التبعيات المطلوبة

تحتاج إلى تضمين حزمة `swagger-annotations` ومكتبة دمج Swagger (مثل `springfox`) في مشروعك. إذا كنت تستخدم Maven، أضف التبعيات التالية إلى ملف `pom.xml` الخاص بك:

```xml
<!-- Swagger Annotations -->
<dependency>
    <groupId>io.swagger</groupId>
    <artifactId>swagger-annotations</artifactId>
    <version>1.6.2</version>
</dependency>

<!-- Springfox Swagger 2 for Swagger Integration -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
</dependency>

<!-- Springfox Swagger UI for Interactive Documentation -->
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.9.2</version>
</dependency>
```

- **`io.swagger:swagger-annotations`**: يوفر تعريفات Swagger 2.0.
- **`springfox-swagger2`**: يدمج Swagger مع Spring Boot ويعالج التعريفات.
- **`springfox-swagger-ui`**: يضيف واجهة ويب لعرض التوثيق المُنشأ.

> **ملاحظة**: تحقق من أحدث الإصدارات على [Maven Repository](https://mvnrepository.com/) حيث قد تكون هناك تحديثات لهذه الإصدارات (1.6.2 لـ `swagger-annotations` و 2.9.2 لـ `springfox`).

---

### الخطوة 2: تهيئة Swagger في تطبيقك

لتمكين Swagger والسماح له بفحص واجهة برمجة التطبيقات الخاصة بك بحثًا عن التعريفات، قم بإنشاء فئة تهيئة تحتوي على bean من نوع `Docket`. أضف هذا إلى تطبيق Spring Boot الخاص بك:

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
                .apis(RequestHandlerSelectors.any()) // فحص جميع المتحكمات (Controllers)
                .paths(PathSelectors.any())          // تضمين جميع المسارات (Paths)
                .build();
    }
}
```

- **`@EnableSwagger2`**: ينشط دعم Swagger 2.0.
- **`Docket`**: يهيئ نقاط النهاية التي سيتم توثيقها. الإعداد أعلاه يفحص جميع المتحكمات والمسارات، ولكن يمكنك تخصيصه (على سبيل المثال، `RequestHandlerSelectors.basePackage("com.example.controllers")`) لتقييد النطاق.

---

### الخطوة 3: استخدام تعريفات Swagger في الكود الخاص بك

توفر حزمة `swagger-annotations` تعريفات لوصف واجهة برمجة التطبيقات الخاصة بك. طبق هذه التعريفات على فئات المتحكمات (Controllers) والطرق (Methods) والمعاملات (Parameters) والنماذج (Models). فيما يلي التعريفات الشائعة مع أمثلة:

#### تعريف المتحكم (Controller)

استخدم `@Api` لوصف المتحكم:

```java
import io.swagger.annotations.Api;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Api(value = "User Controller", description = "Operations pertaining to users")
@RestController
@RequestMapping("/users")
public class UserController {
    // Methods go here
}
```

- **`value`**: اسم مختصر لواجهة برمجة التطبيقات.
- **`description`**: شرح موجز لما يفعله المتحكم.

#### تعريف عمليات واجهة برمجة التطبيقات (API Operations)

استخدم `@ApiOperation` لوصف نقاط النهاية الفردية:

```java
import io.swagger.annotations.ApiOperation;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;

@ApiOperation(value = "Get a user by ID", response = User.class)
@GetMapping("/{id}")
public ResponseEntity<User> getUserById(@PathVariable Long id) {
    // Implementation
    return ResponseEntity.ok(new User(id, "John Doe"));
}
```

- **`value`**: ملخص للعملية.
- **`response`**: نوع الإرجاع المتوقع.

#### وصف المعاملات (Parameters)

استخدم `@ApiParam` لمعاملات الطرق:

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
    // Implementation
    return ResponseEntity.ok(user);
}
```

- **`value`**: يصف المعامل.
- **`required`**: يشير إلى ما إذا كان المعامل إلزاميًا.

#### تحديد الردود (Responses)

استخدم `@ApiResponses` و `@ApiResponse` لتوثيق ردود HTTP المحتملة:

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
    // Implementation
    return ResponseEntity.ok().build();
}
```

- **`code`**: رمز حالة HTTP.
- **`message`**: وصف للرد.

#### وصف النماذج (Models)

بالنسبة لكائنات نقل البيانات (DTOs)، استخدم `@ApiModel` و `@ApiModelProperty`:

```java
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

@ApiModel(description = "User data transfer object")
public class User {
    @ApiModelProperty(notes = "The user's unique identifier", example = "1")
    private Long id;

    @ApiModelProperty(notes = "The user's name", example = "John Doe")
    private String name;

    // Getters and setters
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
- **`@ApiModelProperty`**: يوضح كل حقل، مع أمثلة اختيارية.

---

### الخطوة 4: تشغيل والوصول إلى التوثيق

1.  ابدأ تشغيل تطبيق Spring Boot الخاص بك.
2.  افتح متصفحًا وانتقل إلى:  
    **http://localhost:8080/swagger-ui.html**  
    يعرض هذا الرابط واجهة مستخدم Swagger، وهي واجهة تفاعلية تعرض توثيق واجهة برمجة التطبيقات الخاص بك بناءً على التعريفات.

---

### ملخص لكيفية استخدام `swagger-annotations`

1.  **إضافة التبعيات**: قم بتضمين `swagger-annotations` و `springfox` في ملف `pom.xml` الخاص بك.
2.  **تهيئة Swagger**: قم بإعداد bean من نوع `Docket` لتمكين فحص Swagger.
3.  **تعريف الكود الخاص بك**:
    - `@Api` للمتحكمات (Controllers).
    - `@ApiOperation` للطرق (Methods).
    - `@ApiParam` للمعاملات (Parameters).
    - `@ApiResponses` و `@ApiResponse` لتفاصيل الردود.
    - `@ApiModel` و `@ApiModelProperty` لـ DTOs.
4.  **عرض التوثيق**: قم بالوصول إلى واجهة مستخدم Swagger على `/swagger-ui.html`.

---

### ملاحظات إضافية

-   **Swagger 2.0 مقابل OpenAPI 3.0**: يستخدم هذا الدليل Swagger 2.0 مع `io.swagger:swagger-annotations`. بالنسبة لـ OpenAPI 3.0، استخدم `io.swagger.core.v3:swagger-annotations` ومكتبة مثل `springdoc-openapi`، والتي تغير بعض أسماء التعريفات (على سبيل المثال، `@Tag` بدلاً من `@Api`).
-   **التخصيص**: اضبط تكوين `Docket` لتصفية حزم أو مسارات محددة للحصول على توثيق أكثر تركيزًا.
-   **الجودة**: قدم أوصافًا واضحة ومفصلة في التعريفات لتحسين فائدة التوثيق المُنشأ.

باتباع هذه الخطوات، يمكنك استخدام حزمة `swagger-annotations` بشكل فعال لتوثيق واجهة برمجة تطبيقات REST الخاصة بك، مما يسهل على المطورين والمستهلكين فهم والتفاعل مع نقاط النهاية الخاصة بك والتفاعل معها.