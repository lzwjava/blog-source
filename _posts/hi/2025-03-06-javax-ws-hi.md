---
audio: false
generated: true
lang: hi
layout: post
title: रेस्टफुल वेब सेवाओं के लिए जावा एपीआई
translated: true
type: note
---

`javax.ws.rs` का उपयोग करने के लिए, जो कि RESTful वेब सेवाओं के लिए Java API है (जिसे आमतौर पर JAX-RS कहा जाता है), आपको अपनी प्रोजेक्ट सेट अप करने, RESTful संसाधनों को परिभाषित करने, अपने एप्लिकेशन को कॉन्फ़िगर करने और उसे डिप्लॉय करने के लिए चरणों का पालन करना होगा। JAX-RS आपको वेब सेवाएँ बनाने की अनुमति देता है जो REST आर्किटेक्चरल स्टाइल का पालन करती हैं, एंडपॉइंट्स को परिभाषित करने और HTTP रिक्वेस्ट्स को हैंडल करने के लिए एनोटेशन्स का उपयोग करती हैं। आरंभ करने के लिए यहाँ एक व्यापक गाइड दी गई है:

---

### **1. अपनी प्रोजेक्ट सेट अप करें**
`javax.ws.rs` का उपयोग करने के लिए, आपको JAX-RS API और एक इम्प्लीमेंटेशन (चूंकि `javax.ws.rs` एक स्पेसिफिकेशन है, रनटाइम नहीं) को शामिल करने की आवश्यकता है। एक लोकप्रिय इम्प्लीमेंटेशन Jersey है। यदि आप Maven का उपयोग कर रहे हैं, तो अपनी `pom.xml` में आवश्यक डिपेंडेंसीज़ जोड़ें:

#### **डिपेंडेंसीज़**
```xml
<!-- JAX-RS API -->
<dependency>
    <groupId>javax.ws.rs</groupId>
    <artifactId>javax.ws.rs-api</artifactId>
    <version>2.1.1</version>
</dependency>

<!-- Jersey Implementation (इसमें कोर डिपेंडेंसीज़ शामिल हैं) -->
<dependency>
    <groupId>org.glassfish.jersey.bundles</groupId>
    <artifactId>jaxrs-ri</artifactId>
    <version>2.34</version>
</dependency>

<!-- वैकल्पिक: Jackson के साथ JSON सपोर्ट -->
<dependency>
    <groupId>org.glassfish.jersey.media</groupId>
    <artifactId>jersey-media-json-jackson</artifactId>
    <version>2.34</version>
</dependency>
```

- `javax.ws.rs-api` कोर JAX-RS एनोटेशन्स और क्लासेज़ प्रदान करता है।
- `jaxrs-ri` बंडल में Jersey इम्प्लीमेंटेशन और उसकी डिपेंडेंसीज़ शामिल हैं।
- `jersey-media-json-jackson` मॉड्यूल (वैकल्पिक) JSON सीरियलाइज़ेशन/डी-सीरियलाइज़ेशन के लिए सपोर्ट जोड़ता है।

सुनिश्चित करें कि आपकी प्रोजेक्ट एक सर्वलेट कंटेनर (जैसे, Tomcat) या एक Java EE सर्वर के साथ सेट अप है, क्योंकि JAX-RS एप्लिकेशन आमतौर पर ऐसे वातावरण में चलते हैं। वैकल्पिक रूप से, आप Grizzly जैसे हल्के सर्वर के साथ स्टैंडअलोन भी चला सकते हैं (इस पर बाद में अधिक)।

---

### **2. एक RESTful संसाधन बनाएँ**
JAX-RS में RESTful सेवाएँ रिसोर्स क्लासेज़ का उपयोग करके परिभाषित की जाती हैं जिन पर `@Path` और HTTP मेथड एनोटेशन्स जैसे `@GET`, `@POST`, आदि लगे होते हैं। यहाँ एक साधारण संसाधन का उदाहरण दिया गया है:

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

- **`@Path("/hello")`**: इस संसाधन के लिए URI पथ निर्दिष्ट करता है (जैसे, `http://localhost:8080/api/hello`)।
- **`@GET`**: इंगित करता है कि यह मेथड HTTP GET रिक्वेस्ट्स को हैंडल करती है।
- **`@Produces(MediaType.TEXT_PLAIN)`**: निर्दिष्ट करता है कि प्रतिक्रिया plain text होगी।

जब `/hello` पर GET रिक्वेस्ट की जाती है, तो यह मेथड `"Hello, World!"` लौटाती है।

---

### **3. JAX-RS एप्लिकेशन को कॉन्फ़िगर करें**
आपको JAX-RS रनटाइम को यह बताने की आवश्यकता है कि किन संसाधनों को शामिल करना है। यह `javax.ws.rs.core.Application` को एक्सटेंड करने वाली एक एप्लिकेशन कॉन्फ़िगरेशन क्लास बनाकर किया जा सकता है।

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

- **`@ApplicationPath("/api")`**: सभी संसाधनों के लिए बेस URI पथ को परिभाषित करता है (जैसे, `/api/hello`)।
- **`getClasses()`**: एप्लिकेशन में शामिल की जाने वाली रिसोर्स क्लासेज़ का सेट लौटाता है।

आधुनिक सर्वलेट कंटेनर्स (Servlet 3.0+) के साथ, यह एनोटेशन-आधारित कॉन्फ़िगरेशन अक्सर पर्याप्त होती है, और आपको `web.xml` फ़ाइल की आवश्यकता नहीं हो सकती है।

---

### **4. विभिन्न HTTP मेथड्स और पैरामीटर्स को हैंडल करें**
JAX-RS विभिन्न HTTP मेथड्स, मीडिया टाइप्स और पैरामीटर्स को हैंडल करने के लिए एनोटेशन्स प्रदान करता है।

#### **उदाहरण: POST रिक्वेस्ट्स को हैंडल करना**
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

- **`@POST`**: HTTP POST रिक्वेस्ट्स को हैंडल करता है।
- **`@Consumes(MediaType.APPLICATION_JSON)`**: JSON इनपुट की अपेक्षा करता है, जो एक `MyItem` ऑब्जेक्ट में डी-सीरियलाइज़ हो जाता है।
- **`Response`**: एक 201 Created स्टेटस लौटाता है।

#### **उदाहरण: पाथ पैरामीटर्स**
```java
import javax.ws.rs.PathParam;
import javax.ws.rs.Path;

@GET
@Path("/{id}")
@Produces(MediaType.APPLICATION_JSON)
public MyItem getItem(@PathParam("id") String id) {
    // ID द्वारा आइटम पुनर्प्राप्त करने के लिए लॉजिक
    return new MyItem(id);
}
```

- **`@Path("/{id}")`**: एक पाथ पैरामीटर को परिभाषित करता है (जैसे, `/hello/123`)।
- **`@PathParam("id")`**: URI से `id` वैल्यू को इंजेक्ट करता है।

#### **उदाहरण: क्वेरी पैरामीटर्स**
```java
import javax.ws.rs.QueryParam;

@GET
@Produces(MediaType.APPLICATION_JSON)
public List<MyItem> getItems(@QueryParam("category") String category) {
    // श्रेणी द्वारा आइटम्स को फ़िल्टर करने के लिए लॉजिक
    return itemList;
}
```

- **`@QueryParam("category")`**: क्वेरी स्ट्रिंग से `category` वैल्यू को पुनर्प्राप्त करता है (जैसे, `/hello?category=books`)।

---

### **5. एप्लिकेशन को डिप्लॉय करें**
आप अपने JAX-RS एप्लिकेशन को Tomcat जैसे सर्वलेट कंटेनर में डिप्लॉय कर सकते हैं:

1. अपनी प्रोजेक्ट को एक WAR फ़ाइल के रूप में पैकेज करें (जैसे, `mvn package` का उपयोग करके)।
2. WAR फ़ाइल को अपने कंटेनर में डिप्लॉय करें।
3. अपनी सेवा को कॉन्फ़िगर किए गए URI (जैसे, `http://localhost:8080/your-app/api/hello`) पर एक्सेस करें।

वैकल्पिक रूप से, डेवलपमेंट या स्टैंडअलोन उपयोग के लिए, आप Jersey के साथ Grizzly का उपयोग करके प्रोग्रामेटिक रूप से एप्लिकेशन चला सकते हैं:

#### **उदाहरण: स्टैंडअलोन मेन**
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

### **6. अतिरिक्त सुविधाएँ**
- **एक्सेप्शन हैंडलिंग**: एक्सेप्शन्स को सहजता से हैंडल करने के लिए `ExceptionMapper` का उपयोग करें।
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
- **डिपेंडेंसी इंजेक्शन**: `UriInfo` जैसी ऑब्जेक्ट्स को इंजेक्ट करने के लिए `@Context` का उपयोग करें या इम्प्लीमेंटेशन के DI फ्रेमवर्क (जैसे, Jersey में HK2) पर भरोसा करें।
- **टेस्टिंग**: अपने एंडपॉइंट्स को टेस्ट करने के लिए Postman या Jersey Test Framework जैसे टूल्स का उपयोग करें।

---

### **सारांश**
`javax.ws.rs` का उपयोग करने के लिए, अपनी प्रोजेक्ट में JAX-RS API और Jersey जैसे इम्प्लीमेंटेशन को शामिल करें, पाथ्स और HTTP मेथड्स के लिए एनोटेशन्स के साथ रिसोर्स क्लासेज़ को परिभाषित करें, एप्लिकेशन को कॉन्फ़िगर करें (एक `Application` सबक्लास या `web.xml` के माध्यम से), और इसे एक सर्वलेट कंटेनर में डिप्लॉय करें या स्टैंडअलोन चलाएँ। यह आपको Java के साथ RESTful वेब सेवाएँ कुशलतापूर्वक बनाने में सक्षम बनाता है।