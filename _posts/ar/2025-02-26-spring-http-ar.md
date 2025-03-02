---
audio: false
generated: false
lang: ar
layout: post
title: عملاء HTTP الربيع
translated: true
---

لجواب الاستفسار "كيف يمكن استخدام FeignClient، أو Spring RestClient، أو Spring WebClient"، سأشرح كيفية استخدام كل من هذه الأدوات في Spring لإجراء طلبات HTTP، مع التركيز على إعدادها واستخدامها الأساسي. كل هذه الأدوات جزء من نظام Spring للتواصل مع خدمات RESTful، ولكن لها أغراض مختلفة حسب احتياجات تطبيقك. أدناه، سأقدم دليلًا واضحًا خطوة بخطوة لكل منها، مع أمثلة بسيطة.

---

### **1. استخدام FeignClient**
FeignClient هو عميل REST التوضيحي الذي يوفره Spring Cloud. يسمح لك بتحديد عميل HTTP كواجهات مع تعليقات، مما يجعله مفيدًا بشكل خاص في معمارية الخدمات الصغيرة حيث تحتاج إلى الاتصال بخدمات أخرى.

#### **خطوات استخدام FeignClient**
1. **إضافة التبعيات**: أضف التبعيات Spring Cloud إلى مشروعك. إذا كنت تستخدم Maven، أضف البدء Spring Cloud لـ Feign إلى ملف `pom.xml` الخاص بك:
   ```xml
   <dependency>
       <groupId>org.springframework.cloud</groupId>
       <artifactId>spring-cloud-starter-openfeign</artifactId>
   </dependency>
   ```
   تأكد أيضًا من وجود كتلة إدارة التبعيات لـ Spring Cloud، مع تحديد الإصدار المتوافق.

2. **تفعيل Feign Clients**: أضف تعليق `@EnableFeignClients` إلى فئة التطبيق الرئيسية أو فئة الإعدادات لتفعيل دعم Feign:
   ```java
   import org.springframework.boot.SpringApplication;
   import org.springframework.boot.autoconfigure.SpringBootApplication;
   import org.springframework.cloud.openfeign.EnableFeignClients;

   @SpringBootApplication
   @EnableFeignClients
   public class MyApplication {
       public static void main(String[] args) {
           SpringApplication.run(MyApplication.class, args);
       }
   }
   ```

3. **تعريف واجهة FeignClient**: أنشئ واجهة مع تعليق `@FeignClient`، مع تحديد اسم الخدمة أو URL، وحدد الأساليب التي تتوافق مع نقاط النهاية REST:
   ```java
   import org.springframework.cloud.openfeign.FeignClient;
   import org.springframework.web.bind.annotation.GetMapping;
   import java.util.List;

   @FeignClient(name = "user-service", url = "http://localhost:8080")
   public interface UserClient {
       @GetMapping("/users")
       List<User> getUsers();
   }
   ```
   هنا، `name` هو اسم منطقي للعميل، و `url` هو URL الأساس للخدمة المستهدفة. تعليق `@GetMapping` يتوافق مع نقطة النهاية `/users`.

4. **إدخال واستخدام العميل**: أدخل الواجهة في خدمة أو تحكم وتصل إلى أساليبها كما لو كانت محلية:
   ```java
   import org.springframework.beans.factory.annotation.Autowired;
   import org.springframework.stereotype.Service;
   import java.util.List;

   @Service
   public class UserService {
       @Autowired
       private UserClient userClient;

       public List<User> fetchUsers() {
           return userClient.getUsers();
       }
   }
   ```

#### **النقاط الرئيسية**
- FeignClient متزامن بشكل افتراضي.
- هو مثالي للميكروسيرفيس مع اكتشاف الخدمة (مثل Eureka) عندما تترك `url` وتسمح لـ Spring Cloud بإيجاده.
- يمكن إضافة معالجة الأخطاء مع استرجاعات أو محولات الدائرة (مثل Hystrix أو Resilience4j).

---

### **2. استخدام Spring RestClient**
Spring RestClient هو عميل HTTP متزامن تم تقديمه في Spring Framework 6.1 كبديل حديث لـ `RestTemplate` المهدد بالإنقاض. يوفر واجهة متداخلة لبناء وإجراء الطلبات.

#### **خطوات استخدام RestClient**
1. **التبعيات**: RestClient هو جزء من `spring-web`، وهو جزء من `spring-boot-starter-web` لـ Spring Boot. لا تحتاج عادةً إلى تعليقات إضافية:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-web</artifactId>
   </dependency>
   ```

2. **إنشاء مثيل RestClient**: أنشئ مثيل `RestClient` باستخدام طريقة `create()` الثابتة أو قم بتخصيصه باستخدام بناء:
   ```java
   import org.springframework.web.client.RestClient;

   RestClient restClient = RestClient.create();
   ```
   لاستخدام الإعدادات المخصصة (مثل الأوقات الزمنية)، استخدم `RestClient.builder()`.

3. **بناء وإجراء طلب**: استخدم واجهة المتداخلة لتحديد طريقة HTTP، URI، الرؤوس، والجسم، ثم استرجاع الرد:
   ```java
   import org.springframework.http.MediaType;
   import org.springframework.web.client.RestClient;
   import java.util.List;

   public class UserService {
       private final RestClient restClient;

       public UserService() {
           this.restClient = RestClient.create();
       }

       public List<User> fetchUsers() {
           return restClient.get()
               .uri("http://localhost:8080/users")
               .accept(MediaType.APPLICATION_JSON)
               .retrieve()
               .body(new ParameterizedTypeReference<List<User>>() {});
       }
   }
   ```
   - `get()` يحدد طريقة HTTP.
   - `uri()` يحدد نقطة النهاية.
   - `accept()` يحدد نوع المحتوى المتوقع.
   - `retrieve()` يجرى الطلب، و `body()` يستخرج الرد، باستخدام `ParameterizedTypeReference` لأغراض عامة مثل القوائم.

4. **معالجة الرد**: يتم استرجاع الرد مباشرة لأن RestClient متزامن. للحصول على مزيد من التحكم (مثل رموز الحالة)، استخدم `toEntity()`:
   ```java
   import org.springframework.http.ResponseEntity;

   ResponseEntity<List<User>> response = restClient.get()
       .uri("http://localhost:8080/users")
       .accept(MediaType.APPLICATION_JSON)
       .retrieve()
       .toEntity(new ParameterizedTypeReference<List<User>>() {});
   List<User> users = response.getBody();
   ```

#### **النقاط الرئيسية**
- RestClient متزامن، مما يجعله مناسبًا للتطبيقات التقليدية، الموقوفة.
- يرمي الاستثناءات (مثل `RestClientException`) عند أخطاء HTTP، يمكنك القبض عليها ومعالجتها.
- هو بديل لـ `RestTemplate` مع واجهة أكثر وضوحًا.

---

### **3. استخدام Spring WebClient**
Spring WebClient هو عميل HTTP متفاعل، غير متزامن تم تقديمه في Spring WebFlux. تم تصميمه لعمليات غير متزامنة ويدمج مع تدفقات متفاعلة (Mono و Flux).

#### **خطوات استخدام WebClient**
1. **إضافة التبعيات**: أضف التبعية WebFlux إلى مشروعك:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-webflux</artifactId>
   </dependency>
   ```

2. **إنشاء مثيل WebClient**: أنشئ مثيل `WebClient` مع URL الأساس أو الإعدادات الافتراضية:
   ```java
   import org.springframework.web.reactive.function.client.WebClient;

   WebClient webClient = WebClient.create("http://localhost:8080");
   ```
   استخدم `WebClient.builder()` لإعدادات مخصصة (مثل الكودات، والفيلترات).

3. **بناء وإجراء طلب**: استخدم واجهة المتداخلة لبناء الطلب واسترجاع الرد المتفاعل:
   ```java
   import org.springframework.http.MediaType;
   import org.springframework.web.reactive.function.client.WebClient;
   import reactor.core.publisher.Mono;
   import java.util.List;

   public class UserService {
       private final WebClient webClient;

       public UserService(WebClient webClient) {
           this.webClient = webClient;
       }

       public Mono<List<User>> fetchUsers() {
           return webClient.get()
               .uri("/users")
               .accept(MediaType.APPLICATION_JSON)
               .retrieve()
               .bodyToFlux(User.class)
               .collectList();
       }
   }
   ```
   - `bodyToFlux(User.class)` يعالج تدفق من كائنات `User`.
   - `collectList()` يحول `Flux<User>` إلى `Mono<List<User>>`.

4. **الاشتراك في الرد**: لأن WebClient متفاعل، يجب عليك الاشتراك في `Mono` أو `Flux` لتفعيل الطلب:
   ```java
   Mono<List<User>> usersMono = fetchUsers();
   usersMono.subscribe(users -> System.out.println(users));
   ```
   أو تسلسله في خط أنابيب متفاعل أو إيقافه (غير موصى به في السياقات المتفاعلة):
   ```java
   List<User> users = fetchUsers().block();
   ```

#### **النقاط الرئيسية**
- WebClient غير متزامن ومثالي للتطبيقات المتفاعلة التي تم بناؤها باستخدام Spring WebFlux.
- استخدم `Mono` للردود ذات القيمة الواحدة و `Flux` للردود ذات القيم المتعددة.
- يمكن معالجة الأخطاء باستخدام عمليات مثل `onErrorResume()` أو `retry()`.

---

### **المقارنة ووقت استخدام كل منها**
- **FeignClient**: استخدمه للعميل التوضيحي، القائم على الواجهة في إعدادات الميكروسيرفيس. هو متزامن ويبسط الاتصالات بين الخدمات.
- **RestClient**: استخدمه للطلبات HTTP المتزامنة في التطبيقات التقليدية، الموقوفة لـ Spring. هو بديل حديث لـ `RestTemplate`.
- **WebClient**: استخدمه للطلبات HTTP المتفاعلة، غير المتزامنة في تطبيقات WebFlux أو عند التعامل مع كثافة عالية.

---

### **مثال: استدعاء نقطة النهاية POST**
فرض أن لديك إنشاء مستخدم من خلال استدعاء `POST /users` مع كائن `User`.

#### **FeignClient**
```java
@FeignClient(name = "user-service", url = "http://localhost:8080")
public interface UserClient {
    @PostMapping("/users")
    User createUser(@RequestBody User user);
}

@Service
public class UserService {
    @Autowired
    private UserClient userClient;

    public User createUser(User user) {
        return userClient.createUser(user);
    }
}
```

#### **RestClient**
```java
@Service
public class UserService {
    private final RestClient restClient = RestClient.create();

    public User createUser(User user) {
        return restClient.post()
            .uri("http://localhost:8080/users")
            .contentType(MediaType.APPLICATION_JSON)
            .body(user)
            .retrieve()
            .body(User.class);
    }
}
```

#### **WebClient**
```java
@Service
public class UserService {
    private final WebClient webClient;

    public UserService(WebClient webClient) {
        this.webClient = WebClient.create("http://localhost:8080");
    }

    public Mono<User> createUser(User user) {
        return webClient.post()
            .uri("/users")
            .contentType(MediaType.APPLICATION_JSON)
            .bodyValue(user)
            .retrieve()
            .bodyToMono(User.class);
    }
}
```

---

### **الخاتمة**
- **FeignClient**: حدد واجهة، تفعيلها، واستخدمها مثل كائن محلي.
- **RestClient**: بناء الطلبات بشكل متداخل واسترجاع الردود بشكل متزامن.
- **WebClient**: بناء الطلبات بشكل متداخل، استرجاع تدفقات متفاعلة، ومعالجتها بشكل غير متزامن.

اختر بناءً على بنية تطبيقك: FeignClient للميكروسيرفيس، RestClient للتطبيقات الموقوفة، و WebClient للتطبيقات المتفاعلة. كل منها يتبع نمط إعداد واستخدام بسيط كما هو موضح أعلاه.