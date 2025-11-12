---
audio: false
generated: true
lang: ar
layout: post
title: واجهة برمجة تطبيقات جافا لخدمات الويب المتنقلة
translated: true
type: note
---

لاستخدام `javax.ws.rs`، واجهة برمجة تطبيقات جافا لخدمات الويب المطابقة لـ REST (المعروفة شائعًا باسم JAX-RS)، تحتاج إلى اتباع سلسلة من الخطوات لإعداد مشروعك، وتحديد موارد RESTful، وتهيئة تطبيقك، ونشره. تتيح لك JAX-RS إنشاء خدمات ويب تلتزم بالنمط المعماري REST، باستخدام التوضيحات (annotations) لتحديد نقاط النهاية (endpoints) ومعالجة طلبات HTTP. فيما يلي دليل شامل لمساعدتك على البدء:

---

### **1. إعداد مشروعك**
لاستخدام `javax.ws.rs`، تحتاج إلى تضمين واجهة برمجة تطبيقات JAX-RS وتنفيذ (implementation) لها (نظرًا لأن `javax.ws.rs` هو مواصفات (specification) وليس بيئة وقت التشغيل (runtime)). أحد التنفيذات الشائعة هو Jersey. إذا كنت تستخدم Maven، أضف التبعيات (dependencies) اللازمة إلى ملف `pom.xml` الخاص بك:

#### **التبعيات**
```xml
<!-- JAX-RS API -->
<dependency>
    <groupId>javax.ws.rs</groupId>
    <artifactId>javax.ws.rs-api</artifactId>
    <version>2.1.1</version>
</dependency>

<!-- Jersey Implementation (includes core dependencies) -->
<dependency>
    <groupId>org.glassfish.jersey.bundles</groupId>
    <artifactId>jaxrs-ri</artifactId>
    <version>2.34</version>
</dependency>

<!-- Optional: JSON support with Jackson -->
<dependency>
    <groupId>org.glassfish.jersey.media</groupId>
    <artifactId>jersey-media-json-jackson</artifactId>
    <version>2.34</version>
</dependency>
```

- يوفر `javax.ws.rs-api` التوضيحات والفئات الأساسية لـ JAX-RS.
- تتضمن حزمة `jaxrs-ri` تنفيذ Jersey والتبعيات الخاصة به.
- تضيف وحدة `jersey-media-json-jackson` (اختياري) الدعم لتسلسل/إلغاء تسلسل JSON.

تأكد من إعداد مشروعك باستخدام حاوية servlet (مثل Tomcat) أو خادم Java EE، حيث تعمل تطبيقات JAX-RS عادةً في مثل هذه البيئات. بدلاً من ذلك، يمكنك التشغيل بشكل مستقل (standalone) باستخدام خادم خفيف الوزن مثل Grizzly (المزيد عن ذلك لاحقًا).

---

### **2. إنشاء مورد RESTful**
يتم تعريف خدمات RESTful في JAX-RS باستخدام فئات الموارد (resource classes) المشروحة بـ `@Path` وتوضيحات طرق HTTP مثل `@GET`، `@POST`، إلخ. إليك مثال على مورد بسيط:

#### **مثال: HelloResource.java**
```java
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/hello")
public class HelloResource {

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String sayHello() {
        return "Hello, World!";
    }
}
```

- **`@Path("/hello")`**: يحدد مسار URI لهذا المورد (على سبيل المثال، `http://localhost:8080/api/hello`).
- **`@GET`**: يشير إلى أن هذه الطريقة تتعامل مع طلبات HTTP GET.
- **`@Produces(MediaType.TEXT_PLAIN)`**: يحدد أن الاستجابة ستكون نصًا عاديًا (plain text).

عند إجراء طلب GET إلى `/hello`، ترجع هذه الطريقة `"Hello, World!"`.

---

### **3. تهيئة تطبيق JAX-RS**
تحتاج إلى إخبار بيئة وقت التشغيل JAX-RS بالموارد التي يجب تضمينها. يمكن القيام بذلك عن طريق إنشاء فئة تكوين تطبيق (application configuration class) تمدد `javax.ws.rs.core.Application`.

#### **مثال: MyApplication.java**
```java
import javax.ws.rs.ApplicationPath;
import javax.ws.rs.core.Application;
import java.util.HashSet;
import java.util.Set;

@ApplicationPath("/api")
public class MyApplication extends Application {

    @Override
    public Set<Class<?>> getClasses() {
        Set<Class<?>> classes = new HashSet<>();
        classes.add(HelloResource.class);
        return classes;
    }
}
```

- **`@ApplicationPath("/api")`**: يحدد مسار URI الأساسي لجميع الموارد (على سبيل المثال، `/api/hello`).
- **`getClasses()`**: يُرجع مجموعة فئات الموارد التي سيتم تضمينها في التطبيق.

مع حاويات servlet الحديثة (Servlet 3.0+)، يكون تكوين التوضيح (annotation-based configuration) هذا كافيًا في كثير من الأحيان، وقد لا تحتاج إلى ملف `web.xml`.

---

### **4. التعامل مع طرق HTTP والمعلمات المختلفة**
توفر JAX-RS توضيحات للتعامل مع طرق HTTP المختلفة، وأنواع الوسائط (media types)، والمعلمات.

#### **مثال: التعامل مع طلبات POST**
```java
import javax.ws.rs.POST;
import javax.ws.rs.Consumes;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@POST
@Consumes(MediaType.APPLICATION_JSON)
public Response createItem(MyItem item) {
    // Logic to process the item
    return Response.status(Response.Status.CREATED).build();
}
```

- **`@POST`**: يتعامل مع طلبات HTTP POST.
- **`@Consumes(MediaType.APPLICATION_JSON)`**: يتوقع إدخالاً بتنسيق JSON، والذي يتم إلغاء تسلسله (deserialized) إلى كائن `MyItem`.
- **`Response`**: يُرجع حالة 201 Created.

#### **مثال: معلمات المسار (Path Parameters)**
```java
import javax.ws.rs.PathParam;
import javax.ws.rs.Path;

@GET
@Path("/{id}")
@Produces(MediaType.APPLICATION_JSON)
public MyItem getItem(@PathParam("id") String id) {
    // Logic to retrieve item by ID
    return new MyItem(id);
}
```

- **`@Path("/{id}")`**: يحدد معلمة مسار (path parameter) (على سبيل المثال، `/hello/123`).
- **`@PathParam("id")`**: يحقن (inject) قيمة `id` من URI.

#### **مثال: معلمات الاستعلام (Query Parameters)**
```java
import javax.ws.rs.QueryParam;

@GET
@Produces(MediaType.APPLICATION_JSON)
public List<MyItem> getItems(@QueryParam("category") String category) {
    // Logic to filter items by category
    return itemList;
}
```

- **`@QueryParam("category")`**: يسترجع قيمة `category` من سلسلة الاستعلام (query string) (على سبيل المثال، `/hello?category=books`).

---

### **5. نشر التطبيق**
يمكنك نشر تطبيق JAX-RS الخاص بك في حاوية servlet مثل Tomcat:

1. حزّم مشروعك كملف WAR (على سبيل المثال، باستخدام `mvn package`).
2. انشر ملف WAR في حاويتك.
3. الوصول إلى خدمتك من خلال URI المُهيأ (على سبيل المثال، `http://localhost:8080/your-app/api/hello`).

بدلاً من ذلك، لأغراض التطوير أو الاستخدام المستقل، يمكنك تشغيل التطبيق برمجيًا باستخدام Jersey مع Grizzly:

#### **مثال: Main مستقل**
```java
import org.glassfish.jersey.grizzly2.httpserver.GrizzlyHttpServerFactory;
import org.glassfish.jersey.server.ResourceConfig;
import java.net.URI;

public class Main {
    public static void main(String[] args) {
        URI baseUri = URI.create("http://localhost:8080/api/");
        ResourceConfig config = new ResourceConfig(HelloResource.class);
        GrizzlyHttpServerFactory.createHttpServer(baseUri, config);
        System.out.println("Server running at " + baseUri);
    }
}
```

يبدأ هذا خادم HTTP بدون حاوية servlet كاملة.

---

### **6. ميزات إضافية**
- **معالجة الاستثناءات (Exception Handling)**: استخدم `ExceptionMapper` للتعامل مع الاستثناءات بشكل أنيق.
  ```java
  import javax.ws.rs.NotFoundException;
  import javax.ws.rs.core.Response;
  import javax.ws.rs.ext.ExceptionMapper;
  import javax.ws.rs.ext.Provider;

  @Provider
  public class NotFoundExceptionMapper implements ExceptionMapper<NotFoundException> {
      @Override
      public Response toResponse(NotFoundException exception) {
          return Response.status(Response.Status.NOT_FOUND).build();
      }
  }
  ```
- **حقن التبعيات (Dependency Injection)**: استخدم `@Context` لحقن كائنات مثل `UriInfo` أو اعتمد على إطار عمل DI الخاص بالتنفيذ (مثل HK2 في Jersey).
- **الاختبار (Testing)**: استخدم أدوات مثل Postman أو إطار عمل اختبار Jersey (Jersey Test Framework) لاختبار نقاط النهاية الخاصة بك.

---

### **الخلاصة**
لاستخدام `javax.ws.rs`، قم بتضمين واجهة برمجة تطبيقات JAX-RS وتنفيذ مثل Jersey في مشروعك، وحدد فئات الموارد باستخدام التوضيحات للمسارات وطرق HTTP، ويهيئ التطبيق (عبر فئة فرعية لـ `Application` أو `web.xml`)، وانشره في حاوية servlet أو شغله بشكل مستقل. هذا يمكنك من بناء خدمات ويب مطابقة لـ REST بكفاءة باستخدام جافا.