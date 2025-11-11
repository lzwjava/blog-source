---
audio: false
generated: true
lang: ar
layout: post
title: عملاء بروتوكول نقل النصوص التشعبية في ربيع
translated: true
type: note
---

للإجابة على الاستعلام "كيفية استخدام FeignClient، أو Spring RestClient، أو Spring WebClient"، سأشرح كيف يمكن استخدام كل من أدوات Spring هذه لإجراء طلبات HTTP، مع التركيز على إعدادها واستخدامها الأساسي. كل هذه الأدوات جزء من نظام Spring البيئي للتفاعل مع خدمات RESTful، لكنها تخدم أغراضًا مختلفة اعتمادًا على احتياجات تطبيقك. أدناه، سأقدم دليلًا واضحًا خطوة بخطوة لكل منها، جنبًا إلى جنب مع أمثلة بسيطة.

---

### **1. استخدام FeignClient**
FeignClient هو عميل REST تصريحي توفره Spring Cloud. يسمح لك بتعريف عملاء HTTP كواجهات مع شرح توضيحي (annotations)، مما يجعله مفيدًا بشكل خاص في هندسة الخدمات المصغرة (microservices) حيث تحتاج إلى استدعاء خدمات أخرى.

#### **خطوات استخدام FeignClient**
1.  **إضافة التبعيات**: قم بتضمين تبعيات Spring Cloud في مشروعك. إذا كنت تستخدم Maven، أضف بداية Spring Cloud لـ Feign إلى ملف `pom.xml`:
    ```xml
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-openfeign</artifactId>
    </dependency>
    ```
    تأكد أيضًا من وجود كتلة إدارة التبعيات لـ Spring Cloud، مع تحديد إصدار متوافق.

2.  **تمكين عملاء Feign**: علّق الفئة الرئيسية للتطبيق أو فئة التكوين بـ `@EnableFeignClients` لتفعيل دعم Feign:
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

3.  **تحديد واجهة FeignClient**: أنشئ واجهة مع التعليق التوضيحي `@FeignClient`، محددة اسم الخدمة أو URL، وعرف الطرق المقابلة لنقاط نهاية REST:
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
    هنا، `name` هو اسم منطقي للعميل، و `url` هو عنوان URL الأساسي للخدمة المستهدفة. التعليق التوضيحي `@GetMapping` يربط بنقطة النهاية `/users`.

4.  **حقن واستخدام العميل**: قم بحقن الواجهة تلقائيًا (Autowire) في خدمتك أو وحدة التحكم واستدعِ طرقها كما لو كانت محلية:
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
- FeignClient متزامن (synchronous) بشكل افتراضي.
- مثالي للخدمات المصغرة مع اكتشاف الخدمة (مثل Eureka) عندما تحذف `url` وتترك Spring Cloud يحلها.
- يمكن إضافة معالجة الأخطاء باستخدام الحلول الاحتياطية (fallbacks) أو قواطع الدائرة (circuit breakers) (مثل Hystrix أو Resilience4j).

---

### **2. استخدام Spring RestClient**
Spring RestClient هو عميل HTTP متزامن تم تقديمه في Spring Framework 6.1 كبديل حديث لـ `RestTemplate` الذي تم إهماله. يوفر واجهة برمجة تطبيقات (API) سلسة لبناء وتنفيذ الطلبات.

#### **خطوات استخدام RestClient**
1.  **التبعيات**: RestClient مدرج في `spring-web`، والذي هو جزء من `spring-boot-starter-web` في Spring Boot. لا توجد حاجة عادةً لتبعيات إضافية:
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    ```

2.  **إنشاء مثيل RestClient**: قم بإنشاء مثيل `RestClient` باستخدام طريقة `create()` الثابتة أو خصصه باستخدام الباني (builder):
    ```java
    import org.springframework.web.client.RestClient;

    RestClient restClient = RestClient.create();
    ```
    للتكوينات المخصصة (مثل المهلات الزمنية - timeouts)، استخدم `RestClient.builder()`.

3.  **بناء وتنفيذ طلب**: استخدم واجهة برمجة التطبيقات السلسة لتحديد طريقة HTTP، و URI، والرؤوس (headers)، والنص (body)، ثم استرجع الاستجابة:
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
    - `get()` تحدد طريقة HTTP.
    - `uri()` تحدد نقطة النهاية.
    - `accept()` تحدد نوع المحتوى المتوقع.
    - `retrieve()` تنفذ الطلب، و `body()` تستخرج الاستجابة، باستخدام `ParameterizedTypeReference` للأنواع العامة (generic types) مثل القوائم.

4.  **معالجة الاستجابة**: يتم إرجاع الاستجابة مباشرةً لأن RestClient متزامن. لمزيد من التحكم (مثل رموز الحالة)، استخدم `toEntity()`:
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
- RestClient متزامن، مما يجعله مناسبًا للتطبيقات التقليدية التي تعمل بطريقة الحجب (blocking).
- يرمي استثناءات (مثل `RestClientException`) في حالات أخطاء HTTP، والتي يمكنك التقاطها ومعالجتها.
- إنه بديل لـ `RestTemplate` مع واجهة برمجة تطبيقات أكثر سهولة.

---

### **3. استخدام Spring WebClient**
Spring WebClient هو عميل HTTP تفاعلي (reactive) وغير حاجز (non-blocking) تم تقديمه في Spring WebFlux. تم تصميمه للعمليات غير المتزامنة (asynchronous) ويتكامل مع التدفقات التفاعلية (Mono و Flux).

#### **خطوات استخدام WebClient**
1.  **إضافة التبعيات**: قم بتضمين تبعية WebFlux في مشروعك:
    ```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-webflux</artifactId>
    </dependency>
    ```

2.  **إنشاء مثيل WebClient**: قم بإنشاء مثيل `WebClient` مع عنوان URL أساسي أو إعدادات افتراضية:
    ```java
    import org.springframework.web.reactive.function.client.WebClient;

    WebClient webClient = WebClient.create("http://localhost:8080");
    ```
    استخدم `WebClient.builder()` للتكوينات المخصصة (مثل الكوديكات - codecs، المرشحات - filters).

3.  **بناء وتنفيذ طلب**: استخدم واجهة برمجة التطبيقات السلسة لبناء الطلب واسترداد استجابة تفاعلية:
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
    - `bodyToFlux(User.class)` تتعامل مع دفق من كائنات `User`.
    - `collectList()` تحول `Flux<User>` إلى `Mono<List<User>>`.

4.  **الاشتراك في الاستجابة**: نظرًا لأن WebClient تفاعلي، يجب عليك الاشتراك في `Mono` أو `Flux` لتحفيز الطلب:
    ```java
    Mono<List<User>> usersMono = fetchUsers();
    usersMono.subscribe(users -> System.out.println(users));
    ```
    بدلاً من ذلك، يمكنك ربطه في خط أنابيب تفاعلي أو حجبه (block) (غير موصى به في السياقات التفاعلية):
    ```java
    List<User> users = fetchUsers().block();
    ```

#### **النقاط الرئيسية**
- WebClient غير حاجز ومثالي للتطبيقات التفاعلية المبنية باستخدام Spring WebFlux.
- استخدم `Mono` للاستجابات ذات القيمة المفردة و `Flux` للاستجابات متعددة القيم.
- يمكن إجراء معالجة الأخطاء باستخدام عوامل مثل `onErrorResume()` أو `retry()`.

---

### **المقارنة ومتى تستخدم كل منها**
- **FeignClient**: استخدم للعملاء التصريحيين القائمين على الواجهة في إعدادات الخدمات المصغرة. إنه متزامن ويبسط المكالمات بين الخدمات.
- **RestClient**: استخدم لطلبات HTTP المتزامنة في تطبيقات Spring التقليدية التي تعمل بطريقة الحجب. إنه بديل حديث لـ `RestTemplate`.
- **WebClient**: استخدم لطلبات HTTP التفاعلية غير الحاجزة في التطبيقات القائمة على WebFlux أو عند التعامل مع ازدحام عالٍ (high concurrency).

---

### **مثال: استدعاء نقطة نهاية POST**
لنفترض أنك بحاجة إلى إنشاء مستخدم عن طريق استدعاء `POST /users` مع كائن `User`.

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

### **الخلاصة**
- **FeignClient**: حدد واجهة، مكنها، واستخدمها مثل كائن محلي (bean).
- **RestClient**: ابني الطلبات بسلاسة واحصل على الاستجابات بشكل متزامن.
- **WebClient**: ابني الطلبات بسلاسة، واسترجع التدفقات التفاعلية، ومعالجتها بشكل غير متزامن.

اختر بناءً على بنية تطبيقك: FeignClient للخدمات المصغرة، RestClient للتطبيقات التي تعمل بالحجب، و WebClient للتطبيقات التفاعلية. يتبع كل منها نمط إعداد واستخدام واضحًا كما هو موضح أعلاه.