---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग एचटीटीपी क्लाइंट्स
translated: true
type: note
---

क्वेरी "FeignClient, या Spring RestClient, या Spring WebClient का उपयोग कैसे करें" का जवाब देने के लिए, मैं समझाऊंगा कि HTTP अनुरोध करने के लिए इन Spring टूल्स का उपयोग कैसे किया जा सकता है, जिसमें उनकी सेटअप प्रक्रिया और बुनियादी उपयोग पर ध्यान केंद्रित किया गया है। ये सभी RESTful सेवाओं के साथ बातचीत करने के लिए Spring ecosystem का हिस्सा हैं, लेकिन आपकी एप्लिकेशन की जरूरतों के आधार पर ये अलग-अलग उद्देश्यों को पूरा करते हैं। नीचे, मैं प्रत्येक के लिए एक स्पष्ट, चरण-दर-चरण मार्गदर्शिका प्रदान करूंगा, साथ ही सरल उदाहरण भी दूंगा।

---

### **1. FeignClient का उपयोग**
FeignClient, Spring Cloud द्वारा प्रदान किया गया एक डिक्लेरेटिव REST क्लाइंट है। यह आपको एनोटेशन के साथ इंटरफेस के रूप में HTTP क्लाइंट को परिभाषित करने की अनुमति देता है, जो इसे माइक्रोसर्विसेज आर्किटेक्चर में विशेष रूप से उपयोगी बनाता है जहां आपको अन्य सेवाओं को कॉल करने की आवश्यकता होती है।

#### **FeignClient का उपयोग करने के चरण**
1. **डिपेंडेंसीज जोड़ें**: अपने प्रोजेक्ट में Spring Cloud डिपेंडेंसीज शामिल करें। यदि आप Maven का उपयोग कर रहे हैं, तो अपने `pom.xml` में Feign के लिए Spring Cloud स्टार्टर जोड़ें:
   ```xml
   <dependency>
       <groupId>org.springframework.cloud</groupId>
       <artifactId>spring-cloud-starter-openfeign</artifactId>
   </dependency>
   ```
   सुनिश्चित करें कि आपके पास Spring Cloud के लिए एक डिपेंडेंसी मैनेजमेंट ब्लॉक भी है, जो एक संगत संस्करण निर्दिष्ट करता हो।

2. **Feign क्लाइंट्स सक्षम करें**: Feign सपोर्ट को सक्रिय करने के लिए अपने मुख्य एप्लिकेशन क्लास या कॉन्फ़िगरेशन क्लास को `@EnableFeignClients` से एनोटेट करें:
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

3. **FeignClient इंटरफेस परिभाषित करें**: `@FeignClient` से एनोटेट एक इंटरफेस बनाएं, सेवा नाम या URL निर्दिष्ट करें, और REST एंडपॉइंट्स के अनुरूप मेथड्स परिभाषित करें:
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
   यहाँ, `name` क्लाइंट के लिए एक तार्किक नाम है, और `url` टार्गेट सेवा का बेस URL है। `@GetMapping` एनोटेशन `/users` एंडपॉइंट से मैप करता है।

4. **क्लाइंट को इंजेक्ट करें और उपयोग करें**: अपनी सेवा या कंट्रोलर में इंटरफेस को ऑटोवायर करें और इसकी मेथड्स को ऐसे कॉल करें जैसे कि वे स्थानीय हों:
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

#### **मुख्य बिंदु**
- FeignClient डिफ़ॉल्ट रूप से सिंक्रोनस है।
- यह सर्विस डिस्कवरी (जैसे, Eureka) वाले माइक्रोसर्विसेज के लिए आदर्श है जब आप `url` को छोड़ देते हैं और Spring Cloud को इसे रिज़ॉल्व करने देते हैं।
- फॉलबैक या सर्किट ब्रेकर (जैसे, Hystrix या Resilience4j) के साथ एरर हैंडलिंग जोड़ी जा सकती है।

---

### **2. Spring RestClient का उपयोग**
Spring RestClient, Spring Framework 6.1 में पेश किया गया एक सिंक्रोनस HTTP क्लाइंट है, जो deprecated `RestTemplate` का एक आधुनिक विकल्प है। यह अनुरोधों को बनाने और निष्पादित करने के लिए एक फ्लुऐंट API प्रदान करता है।

#### **RestClient का उपयोग करने के चरण**
1. **डिपेंडेंसीज**: RestClient `spring-web` में शामिल है, जो Spring Boot के `spring-boot-starter-web` का हिस्सा है। आमतौर पर किसी अतिरिक्त डिपेंडेंसी की आवश्यकता नहीं होती:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-web</artifactId>
   </dependency>
   ```

2. **एक RestClient इंस्टेंस बनाएँ**: इसके स्टैटिक `create()` मेथड का उपयोग करके `RestClient` को इंस्टेंटिएट करें या बिल्डर के साथ इसे कस्टमाइज़ करें:
   ```java
   import org.springframework.web.client.RestClient;

   RestClient restClient = RestClient.create();
   ```
   कस्टम कॉन्फ़िगरेशन (जैसे, टाइमआउट) के लिए, `RestClient.builder()` का उपयोग करें।

3. **एक अनुरोध बनाएँ और निष्पादित करें**: HTTP मेथड, URI, हेडर और बॉडी निर्दिष्ट करने के लिए फ्लुऐंट API का उपयोग करें, फिर रिस्पॉन्स प्राप्त करें:
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
   - `get()` HTTP मेथड निर्दिष्ट करता है।
   - `uri()` एंडपॉइंट सेट करता है।
   - `accept()` अपेक्षित कंटेंट टाइप सेट करता है।
   - `retrieve()` अनुरोध निष्पादित करता है, और `body()` रिस्पॉन्स निकालता है, जो सूचियों जैसे जेनेरिक प्रकारों के लिए `ParameterizedTypeReference` का उपयोग करता है।

4. **रिस्पॉन्स को हैंडल करें**: रिस्पॉन्स सीधे लौटा दिया जाता है क्योंकि RestClient सिंक्रोनस है। अधिक नियंत्रण (जैसे, स्टेटस कोड) के लिए, `toEntity()` का उपयोग करें:
   ```java
   import org.springframework.http.ResponseEntity;

   ResponseEntity<List<User>> response = restClient.get()
       .uri("http://localhost:8080/users")
       .accept(MediaType.APPLICATION_JSON)
       .retrieve()
       .toEntity(new ParameterizedTypeReference<List<User>>() {});
   List<User> users = response.getBody();
   ```

#### **मुख्य बिंदु**
- RestClient सिंक्रोनस है, जो इसे पारंपरिक, ब्लॉकिंग एप्लिकेशन के लिए उपयुक्त बनाता है।
- यह HTTP एरर पर एक्सेप्शन (जैसे, `RestClientException`) फेंकता है, जिन्हें आप कैच और हैंडल कर सकते हैं।
- यह `RestTemplate` का एक प्रतिस्थापन है जिसमें अधिक सहज API है।

---

### **3. Spring WebClient का उपयोग**
Spring WebClient, Spring WebFlux में पेश किया गया एक रिएक्टिव, नॉन-ब्लॉकिंग HTTP क्लाइंट है। यह अतुल्यकालिक ऑपरेशन के लिए डिज़ाइन किया गया है और रिएक्टिव स्ट्रीम (Mono और Flux) के साथ एकीकृत होता है।

#### **WebClient का उपयोग करने के चरण**
1. **डिपेंडेंसीज जोड़ें**: अपने प्रोजेक्ट में WebFlux डिपेंडेंसी शामिल करें:
   ```xml
   <dependency>
       <groupId>org.springframework.boot</groupId>
       <artifactId>spring-boot-starter-webflux</artifactId>
   </dependency>
   ```

2. **एक WebClient इंस्टेंस बनाएँ**: बेस URL या डिफ़ॉल्ट सेटिंग्स के साथ `WebClient` को इंस्टेंटिएट करें:
   ```java
   import org.springframework.web.reactive.function.client.WebClient;

   WebClient webClient = WebClient.create("http://localhost:8080");
   ```
   कस्टम कॉन्फ़िगरेशन (जैसे, कोडेक्स, फ़िल्टर) के लिए `WebClient.builder()` का उपयोग करें।

3. **एक अनुरोध बनाएँ और निष्पादित करें**: अनुरोध का निर्माण करने और एक रिएक्टिव रिस्पॉन्स प्राप्त करने के लिए फ्लुऐंट API का उपयोग करें:
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
   - `bodyToFlux(User.class)` `User` ऑब्जेक्ट्स की एक स्ट्रीम को हैंडल करता है।
   - `collectList()` `Flux<User>` को `Mono<List<User>>` में बदल देता है।

4. **रिस्पॉन्स को सब्सक्राइब करें**: चूंकि WebClient रिएक्टिव है, आपको अनुरोध को ट्रिगर करने के लिए `Mono` या `Flux` को सब्सक्राइब करना होगा:
   ```java
   Mono<List<User>> usersMono = fetchUsers();
   usersMono.subscribe(users -> System.out.println(users));
   ```
   वैकल्पिक रूप से, इसे एक रिएक्टिव पाइपलाइन में चेन करें या ब्लॉक करें (रिएक्टिव कॉन्टेक्स्ट में अनुशंसित नहीं):
   ```java
   List<User> users = fetchUsers().block();
   ```

#### **मुख्य बिंदु**
- WebClient नॉन-ब्लॉकिंग है और Spring WebFlux के साथ बने रिएक्टिव एप्लिकेशन के लिए आदर्श है।
- सिंगल-वैल्यूड रिस्पॉन्स के लिए `Mono` और मल्टी-वैल्यूड रिस्पॉन्स के लिए `Flux` का उपयोग करें।
- एरर हैंडलिंग `onErrorResume()` या `retry()` जैसे ऑपरेटर्स के साथ की जा सकती है।

---

### **तुलना और कब किसका उपयोग करें**
- **FeignClient**: माइक्रोसर्विसेज सेटअप में डिक्लेरेटिव, इंटरफेस-आधारित क्लाइंट के लिए उपयोग करें। यह सिंक्रोनस है और सर्विस-टू-सर्विस कॉल को सरल बनाता है।
- **RestClient**: पारंपरिक, ब्लॉकिंग Spring एप्लिकेशन में सिंक्रोनस HTTP अनुरोधों के लिए उपयोग करें। यह `RestTemplate` का एक आधुनिक विकल्प है।
- **WebClient**: WebFlux-आधारित एप्लिकेशन में या उच्च समवर्तीता को हैंडल करते समय रिएक्टिव, नॉन-ब्लॉकिंग HTTP अनुरोधों के लिए उपयोग करें।

---

### **उदाहरण: एक POST एंडपॉइंट को कॉल करना**
मान लीजिए आपको एक `User` ऑब्जेक्ट के साथ `POST /users` को कॉल करके एक उपयोगकर्ता बनाने की आवश्यकता है।

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

### **निष्कर्ष**
- **FeignClient**: एक इंटरफेस परिभाषित करें, इसे सक्षम करें, और इसे एक स्थानीय बीन की तरह उपयोग करें।
- **RestClient**: फ्लुऐंट तरीके से अनुरोध बनाएं और सिंक्रोनस रूप से रिस्पॉन्स प्राप्त करें।
- **WebClient**: फ्लुऐंट तरीके से अनुरोध बनाएं, रिएक्टिव स्ट्रीम प्राप्त करें, और उन्हें अतुल्यकालिक रूप से प्रोसेस करें।

अपनी एप्लिकेशन की आर्किटेक्चर के आधार पर चुनें: माइक्रोसर्विसेज के लिए FeignClient, ब्लॉकिंग ऐप्स के लिए RestClient, और रिएक्टिव ऐप्स के लिए WebClient। प्रत्येक ऊपर दिखाए गए अनुसार एक सीधी सेटअप और उपयोग पैटर्न का पालन करता है।