---
audio: false
generated: true
lang: ar
layout: post
title: API Java للخدمات الويب RESTful
translated: true
---

لاستخدام `javax.ws.rs`، واجهة برمجة التطبيقات Java للخدمات الويب RESTful (المعروفة أيضًا باسم JAX-RS)، عليك اتباع سلسلة من الخطوات لتكوين مشروعك، تعريف الموارد RESTful، تهيئة تطبيقك، وإطلاقه. يسمح JAX-RS لك بإنشاء خدمات الويب التي تتبع نمط REST المعماري باستخدام التعليقات لتحديد النهايات وعلاج طلبات HTTP. أدناه دليل شامل للحصول على البدء:

---

### **1. إعداد مشروعك**
لاستخدام `javax.ws.rs`، عليك تضمين واجهة برمجة التطبيقات JAX-RS وتهية (لأن `javax.ws.rs` هو مواصفات وليس تنفيذ). أحد التهيئات الشائعة هو Jersey. إذا كنت تستخدم Maven، أضف الاعتماديات اللازمة إلى ملف `pom.xml` الخاص بك:

#### **الاعتماديات**
```xml
<!-- واجهة برمجة التطبيقات JAX-RS -->
<dependency>
    <groupId>javax.ws.rs</groupId>
    <artifactId>javax.ws.rs-api</artifactId>
    <version>2.1.1</version>
</dependency>

<!-- تنفيذ Jersey (يضم الاعتماديات الأساسية) -->
<dependency>
    <groupId>org.glassfish.jersey.bundles</groupId>
    <artifactId>jaxrs-ri</artifactId>
    <version>2.34</version>
</dependency>

<!-- اختياري: دعم JSON مع Jackson -->
<dependency>
    <groupId>org.glassfish.jersey.media</groupId>
    <artifactId>jersey-media-json-jackson</artifactId>
    <version>2.34</version>
</dependency>
```

- يوفر `javax.ws.rs-api` التعليقات الأساسية وطبقة JAX-RS.
- يضم `jaxrs-ri` تنفيذ Jersey واعتمادياته.
- يضيف `jersey-media-json-jackson` (اختياري) دعمًا لتسلسل/تسلسل عكس JSON.

تأكد من إعداد مشروعك مع حاوية Servlet (مثل Tomcat) أو خادم Java EE، لأن تطبيقات JAX-RS تعمل عادةً في هذه البيئة. أو يمكنك تشغيلها بشكل مستقل باستخدام خادم خفيف الوزن مثل Grizzly (أكثر من ذلك لاحقًا).

---

### **2. إنشاء مصدر RESTful**
تحدد خدمات RESTful في JAX-RS باستخدام فئات الموارد التي يتم تعليقاتها `@Path` وتعليقات طرق HTTP مثل `@GET`، `@POST`، إلخ. إليك مثال على مصدر بسيط:

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
        return "مرحبًا بالعالم!";
    }
}
```

- **`@Path("/hello")`**: يحدد مسار URI لهذا المصدر (مثل `http://localhost:8080/api/hello`).
- **`@GET`**: يشير إلى أن هذه الطريقة تتعامل مع طلبات HTTP GET.
- **`@Produces(MediaType.TEXT_PLAIN)`**: يحدد أن الرد سيكون نصًا عاديًا.

عند إجراء طلب GET إلى `/hello`، ترجع هذه الطريقة `"مرحبًا بالعالم!"`.

---

### **3. تهيئة تطبيق JAX-RS**
يجب أن تخبر Runtime JAX-RS أي الموارد يجب تضمينها. يمكن تحقيق ذلك من خلال إنشاء فئة تهيئة التطبيق التي تمتد من `javax.ws.rs.core.Application`.

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

- **`@ApplicationPath("/api")`**: يحدد مسار URI الأساسي لجميع الموارد (مثل `/api/hello`).
- **`getClasses()`**: يرجع مجموعة فئات الموارد التي يجب تضمينها في التطبيق.

مع حاويات Servlet الحديثة (Servlet 3.0+)، تكون هذه التهيئة القائمة على التعليقات كافية غالبًا، ولا تحتاج إلى ملف `web.xml`.

---

### **4. معالجة طرق HTTP المختلفة والمتغيرات**
يوفر JAX-RS تعليقاتًا للتعامل مع طرق HTTP المختلفة، أنواع الوسائط، والمتغيرات.

#### **مثال: معالجة طلبات POST**
```java
import javax.ws.rs.POST;
import javax.ws.rs.Consumes;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@POST
@Consumes(MediaType.APPLICATION_JSON)
public Response createItem(MyItem item) {
    // منطق معالجة العنصر
    return Response.status(Response.Status.CREATED).build();
}
```

- **`@POST`**: يتعامل مع طلبات HTTP POST.
- **`@Consumes(MediaType.APPLICATION_JSON)`**: يتوقع إدخال JSON، والذي يتم تسلسله عكسه إلى كائن `MyItem`.
- **`Response`**: يرجع حالة 201 Created.

#### **مثال: متغيرات المسار**
```java
import javax.ws.rs.PathParam;
import javax.ws.rs.Path;

@GET
@Path("/{id}")
@Produces(MediaType.APPLICATION_JSON)
public MyItem getItem(@PathParam("id") String id) {
    // منطق استرجاع العنصر حسب ID
    return new MyItem(id);
}
```

- **`@Path("/{id}")`**: يحدد متغير مسار (مثل `/hello/123`).
- **`@PathParam("id")`**: يدرج قيمة `id` من URI.

#### **مثال: متغيرات الاستعلام**
```java
import javax.ws.rs.QueryParam;

@GET
@Produces(MediaType.APPLICATION_JSON)
public List<MyItem> getItems(@QueryParam("category") String category) {
    // منطق تصفية العناصر حسب الفئة
    return itemList;
}
```

- **`@QueryParam("category")`**: يسترجع قيمة `category` من سلسلة الاستعلام (مثل `/hello?category=books`).

---

### **5. نشر التطبيق**
يمكنك نشر تطبيق JAX-RS في حاوية Servlet مثل Tomcat:

1. حزم مشروعك كملف WAR (مثلًا باستخدام `mvn package`).
2. نشر ملف WAR إلى حاوية.
3. الوصول إلى الخدمة في URI المحدد (مثل `http://localhost:8080/your-app/api/hello`).

بدلاً من ذلك، يمكنك تشغيل التطبيق برمجيًا باستخدام Jersey مع Grizzly للتنمية أو الاستخدام المستقل:

#### **مثال: Main المستقل**
```java
import org.glassfish.jersey.grizzly2.httpserver.GrizzlyHttpServerFactory;
import org.glassfish.jersey.server.ResourceConfig;
import java.net.URI;

public class Main {
    public static void main(String[] args) {
        URI baseUri = URI.create("http://localhost:8080/api/");
        ResourceConfig config = new ResourceConfig(HelloResource.class);
        GrizzlyHttpServerFactory.createHttpServer(baseUri, config);
        System.out.println("الخادم يعمل في " + baseUri);
    }
}
```

يبدأ هذا خادم HTTP بدون حاوية Servlet كاملة.

---

### **6. ميزات إضافية**
- **معالجة الاستثناءات**: استخدم `ExceptionMapper` لمعالجة الاستثناءات بشكل لطيف.
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
- **إدخال الاعتماديات**: استخدم `@Context` لإدخال كائنات مثل `UriInfo` أو الاعتماد على إطار عمل DI للتهية (مثل HK2 في Jersey).
- **التحقيق**: استخدم أدوات مثل Postman أو إطار عمل اختبار Jersey للتحقيق في نقاط النهاية الخاصة بك.

---

### **ملخص**
لاستخدام `javax.ws.rs`، أضف واجهة برمجة التطبيقات JAX-RS وتهية مثل Jersey إلى مشروعك، وحدد فئات الموارد باستخدام تعليقات المسارات وطرق HTTP، وتهيئة التطبيق (من خلال فرع `Application` أو `web.xml`), ونشره في حاوية Servlet أو تشغيله بشكل مستقل. وهذا يتيح لك بناء خدمات الويب RESTful بشكل فعال باستخدام Java.