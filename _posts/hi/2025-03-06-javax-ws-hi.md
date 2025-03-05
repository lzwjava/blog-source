---
audio: false
generated: true
lang: hi
layout: post
title: 'Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services


  Java API for RESTful Web Services'
translated: true
---

`javax.ws.rs` का उपयोग करने के लिए, Java API for RESTful web services (जिसे JAX-RS के रूप में जाना जाता है), आपको अपने प्रोजेक्ट को सेट अप करने, RESTful resources को परिभाषित करने, अपने एप्लिकेशन को कॉन्फ़िगर करने और इसे डिप्लॉय करने के लिए एक श्रृंखला का पालन करना होगा। JAX-RS आपको REST आर्किटेक्चरल शैली का पालन करने वाले वेब सर्विसेस बनाने की अनुमति देता है, एनोटेशन का उपयोग करके एंडपॉइंट्स को परिभाषित करने और HTTP अनुरोधों को संभालने के लिए।

---

### **1. प्रोजेक्ट सेट अप करें**
`javax.ws.rs` का उपयोग करने के लिए, आपको JAX-RS API और एक इम्प्लीमेंटेशन (क्योंकि `javax.ws.rs` एक स्पेसिफिकेशन है, न कि एक रनटाइम) को शामिल करना होगा। एक लोकप्रिय इम्प्लीमेंटेशन Jersey है। अगर आप Maven का उपयोग कर रहे हैं, तो अपने `pom.xml` में आवश्यक डिपेंडेंसेज़ को जोड़ें:

#### **डिपेंडेंसेज़**
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

- `javax.ws.rs-api` कोर JAX-RS एनोटेशन और क्लासेज़ प्रदान करता है।
- `jaxrs-ri` बंडल Jersey इम्प्लीमेंटेशन और इसके डिपेंडेंसेज़ को शामिल करता है।
- `jersey-media-json-jackson` मॉड्यूल (ऑप्शनल) JSON सीरियलाइजेशन/डिसीरियलाइजेशन के लिए समर्थन जोड़ता है।

अपने प्रोजेक्ट को एक सर्वलेट कंटेनर (जैसे टोमकैट) या एक Java EE सर्वर के साथ सेट अप करें, क्योंकि JAX-RS एप्लिकेशन आमतौर पर ऐसे वातावरण में चलते हैं। विकल्प के रूप में, आप एक लाइटवेट सर्वर जैसे Grizzly (इसके बारे में बाद में अधिक) के साथ स्टैंडअलोन चल सकते हैं।

---

### **2. एक RESTful रिसोर्स बनाएं**
JAX-RS में RESTful सर्विसेस `@Path` और HTTP विधि एनोटेशन जैसे `@GET`, `@POST` आदि के साथ एनोटेट किए गए रिसोर्स क्लासेज़ के द्वारा परिभाषित किए जाते हैं। यहाँ एक सरल रिसोर्स का उदाहरण है:

#### **उदाहरण: HelloResource.java**
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

- **`@Path("/hello")`**: इस रिसोर्स के लिए URI पथ को परिभाषित करता है (जैसे, `http://localhost:8080/api/hello`).
- **`@GET`**: यह विधि HTTP GET अनुरोधों को संभालती है।
- **`@Produces(MediaType.TEXT_PLAIN)`**: यह स्पष्ट करता है कि प्रतिक्रिया साधारण पाठ होगी।

जब `/hello` पर एक GET अनुरोध किया जाता है, तो यह विधि `"Hello, World!"` लौटाती है।

---

### **3. JAX-RS एप्लिकेशन को कॉन्फ़िगर करें**
आपको JAX-RS रनटाइम को बताना होगा कि कौन से रिसोर्स शामिल होंगे। यह एक एप्लिकेशन कॉन्फ़िगरेशन क्लास बनाकर किया जा सकता है जो `javax.ws.rs.core.Application` को विस्तारित करता है।

#### **उदाहरण: MyApplication.java**
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

- **`@ApplicationPath("/api")`**: सभी रिसोर्सों के लिए आधार URI पथ को परिभाषित करता है (जैसे, `/api/hello`).
- **`getClasses()`**: एप्लिकेशन में शामिल होने वाले रिसोर्स क्लासेज़ का सेट लौटाता है।

आधुनिक सर्वलेट कंटेनर्स (Servlet 3.0+) के साथ, यह एनोटेशन-आधारित कॉन्फ़िगरेशन आमतौर पर पर्याप्त होता है, और आपको एक `web.xml` फ़ाइल की जरूरत नहीं हो सकती।

---

### **4. विभिन्न HTTP विधियों और पैरामीटरों को संभालें**
JAX-RS विभिन्न HTTP विधियों, मीडिया प्रकारों और पैरामीटरों को संभालने के लिए एनोटेशन प्रदान करता है।

#### **उदाहरण: POST अनुरोधों को संभालना**
```java
import javax.ws.rs.POST;
import javax.ws.rs.Consumes;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@POST
@Consumes(MediaType.APPLICATION_JSON)
public Response createItem(MyItem item) {
    // आइटम को प्रोसेस करने के लिए लॉजिक
    return Response.status(Response.Status.CREATED).build();
}
```

- **`@POST`**: HTTP POST अनुरोधों को संभालता है।
- **`@Consumes(MediaType.APPLICATION_JSON)`**: JSON इनपुट की अपेक्षा करता है, जो एक `MyItem` ऑब्जेक्ट में डिसीरियलाइज किया जाता है।
- **`Response`**: एक 201 Created स्थिति लौटाता है।

#### **उदाहरण: पथ पैरामीटर**
```java
import javax.ws.rs.PathParam;
import javax.ws.rs.Path;

@GET
@Path("/{id}")
@Produces(MediaType.APPLICATION_JSON)
public MyItem getItem(@PathParam("id") String id) {
    // ID द्वारा आइटम को प्राप्त करने के लिए लॉजिक
    return new MyItem(id);
}
```

- **`@Path("/{id}")`**: एक पथ पैरामीटर को परिभाषित करता है (जैसे, `/hello/123`).
- **`@PathParam("id")`**: URI से `id` मान को इंजेक्ट करता है।

#### **उदाहरण: क्वेरी पैरामीटर**
```java
import javax.ws.rs.QueryParam;

@GET
@Produces(MediaType.APPLICATION_JSON)
public List<MyItem> getItems(@QueryParam("category") String category) {
    // कैटेगरी द्वारा आइटमों को फ़िल्टर करने के लिए लॉजिक
    return itemList;
}
```

- **`@QueryParam("category")`**: क्वेरी स्ट्रिंग से `category` मान को प्राप्त करता है (जैसे, `/hello?category=books`).

---

### **5. एप्लिकेशन को डिप्लॉय करें**
आप अपने JAX-RS एप्लिकेशन को एक सर्वलेट कंटेनर जैसे टोमकैट में डिप्लॉय कर सकते हैं:

1. अपने प्रोजेक्ट को एक WAR फ़ाइल के रूप में पैकेज करें (जैसे, `mvn package` का उपयोग करके).
2. WAR फ़ाइल को अपने कंटेनर में डिप्लॉय करें।
3. कॉन्फ़िगर किए गए URI पर अपने सर्विस तक पहुंचें (जैसे, `http://localhost:8080/your-app/api/hello`).

विकल्प के रूप में, विकास या स्टैंडअलोन उपयोग के लिए, आप Jersey के साथ Grizzly का उपयोग करके एप्लिकेशन को प्रोग्रामेटिक रूप से चला सकते हैं:

#### **उदाहरण: स्टैंडअलोन मुख्य**
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

यह एक पूर्ण सर्वलेट कंटेनर के बिना एक HTTP सर्वर शुरू करता है।

---

### **6. अतिरिक्त विशेषताएं**
- **एक्सेप्शन हैंडलिंग**: `ExceptionMapper` का उपयोग करके एक्सेप्शन को नम्रता से संभालें।
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
- **डिपेंडेंसी इंजेक्शन**: `@Context` का उपयोग करके ऑब्जेक्ट्स जैसे `UriInfo` को इंजेक्ट करें या इम्प्लीमेंटेशन के DI फ्रेमवर्क (जैसे Jersey में HK2) पर भरोसा करें।
- **टेस्टिंग**: Postman या Jersey Test Framework जैसे टूल्स का उपयोग करके अपने एंडपॉइंट्स को टेस्ट करें।

---

### **सारांश**
`javax.ws.rs` का उपयोग करने के लिए, अपने प्रोजेक्ट में JAX-RS API और एक इम्प्लीमेंटेशन जैसे Jersey को शामिल करें, एनोटेशन के साथ पथ और HTTP विधियों के लिए रिसोर्स क्लासेज़ को परिभाषित करें, एप्लिकेशन को कॉन्फ़िगर करें (एक `Application` उपवर्ग या `web.xml` के माध्यम से), और इसे एक सर्वलेट कंटेनर में डिप्लॉय करें या इसे स्टैंडअलोन चलाएं। यह आपको Java के साथ RESTful वेब सर्विसेस को दक्षता से बनाना संभव बनाता है।