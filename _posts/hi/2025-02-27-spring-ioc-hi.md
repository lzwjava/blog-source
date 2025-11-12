---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग आईओसी (इनवर्जन ऑफ कंट्रोल) कंटेनर
translated: true
type: note
---

मैं Spring IoC (इनवर्शन ऑफ कंट्रोल) कंटेनर के उपयोग को स्पष्ट और व्यावहारिक तरीके से समझाता हूँ। Spring IoC कंटेनर Spring Framework का मूल (core) है, जो एप्लिकेशन ऑब्जेक्ट्स (जिन्हें beans कहते हैं) के lifecycle और configuration का प्रबंधन करने के लिए जिम्मेदार है। यह नियंत्रण को "उलट" (invert) देता है क्योंकि यह आपके लिए ऑब्जेक्ट निर्माण और dependency injection को संभालता है, न कि आपको उन्हें मैन्युअल रूप से बनाना और जोड़ना (wiring) पड़ता है।

आरंभ करने के लिए यहां एक चरण-दर-चरण मार्गदर्शिका दी गई है:

---

### 1. **मूल बातें समझें**
- **यह क्या करता है**: IoC कंटेनर आपके द्वारा प्रदान किए गए metadata (XML, Java annotations, या Java code के माध्यम से) के आधार पर beans (आपके एप्लिकेशन ऑब्जेक्ट्स) को बनाता, कॉन्फ़िगर करता और प्रबंधित करता है।
- **मुख्य अवधारणाएँ**:
  - **Beans**: कंटेनर द्वारा प्रबंधित ऑब्जेक्ट्स।
  - **Dependency Injection (DI)**: कंटेनर आपके ऑब्जेक्ट्स में dependencies (अन्य beans या मान) inject करता है।
  - **Configuration**: आप कंटेनर को बताते हैं कि कौन से beans बनाने हैं और उन्हें कैसे जोड़ना (wire) है।

---

### 2. **अपना प्रोजेक्ट सेट अप करें**
Spring IoC का उपयोग करने के लिए, आपको एक Spring प्रोजेक्ट की आवश्यकता है। यदि आप नए सिरे से शुरू कर रहे हैं:
- **Spring Boot** (सबसे सरल तरीका) या सादा Spring का उपयोग करें।
- अपनी `pom.xml` में dependencies जोड़ें (यदि Maven का उपयोग कर रहे हैं):
  ```xml
  <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>6.1.3</version> <!-- नवीनतम version का उपयोग करें -->
  </dependency>
  ```
- Spring Boot के लिए, इसका उपयोग करें:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <version>3.2.2</version> <!-- वर्तमान में नवीनतम -->
  </dependency>
  ```

---

### 3. **अपनी Beans को परिभाषित करें**
आप beans को तीन मुख्य तरीकों से परिभाषित कर सकते हैं:

#### a) **Annotations का उपयोग करके (सबसे आम)**
- एक साधारण Java क्लास बनाएं और उसे `@Component` से annotate करें (या विशेष annotations जैसे `@Service`, `@Repository`, आदि)।
- उदाहरण:
  ```java
  import org.springframework.stereotype.Component;

  @Component
  public class MyService {
      public void doSomething() {
          System.out.println("Doing something!");
      }
  }
  ```

#### b) **Java Configuration का उपयोग करके**
- `@Configuration` के साथ एक configuration क्लास बनाएं और `@Bean` के साथ beans को परिभाषित करें।
- उदाहरण:
  ```java
  import org.springframework.context.annotation.Bean;
  import org.springframework.context.annotation.Configuration;

  @Configuration
  public class AppConfig {
      @Bean
      public MyService myService() {
          return new MyService();
      }
  }
  ```

#### c) **XML का उपयोग करके (Legacy Approach)**
- एक XML फ़ाइल (जैसे, `beans.xml`) में beans को परिभाषित करें:
  ```xml
  <beans xmlns="http://www.springframework.org/schema/beans"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://www.springframework.org/schema/beans
         http://www.springframework.org/schema/beans/spring-beans.xsd">
      <bean id="myService" class="com.example.MyService"/>
  </beans>
  ```

---

### 4. **IoC कंटेनर को प्रारंभ करें**
आपके beans का प्रबंधन करने के लिए कंटेनर को शुरू करना आवश्यक है।

#### a) **Spring Boot के साथ**
- Spring Boot यह स्वचालित रूप से कर देता है। बस `@SpringBootApplication` के साथ एक main क्लास बनाएं:
  ```java
  import org.springframework.boot.SpringApplication;
  import org.springframework.boot.autoconfigure.SpringBootApplication;

  @SpringBootApplication
  public class MyApp {
      public static void main(String[] args) {
          SpringApplication.run(MyApp.class, args);
      }
  }
  ```
- कंटेनर `@Component` क्लासेज को scan करता है और उनका प्रबंधन करता है।

#### b) **सादे Spring के साथ (Annotation-आधारित)**
- `AnnotationConfigApplicationContext` का उपयोग करें:
  ```java
  import org.springframework.context.annotation.AnnotationConfigApplicationContext;

  public class Main {
      public static void main(String[] args) {
          AnnotationConfigApplicationContext context = 
              new AnnotationConfigApplicationContext(AppConfig.class);
          MyService service = context.getBean(MyService.class);
          service.doSomething();
          context.close();
      }
  }
  ```

#### c) **XML के साथ**
- `ClassPathXmlApplicationContext` का उपयोग करें:
  ```java
  import org.springframework.context.support.ClassPathXmlApplicationContext;

  public class Main {
      public static void main(String[] args) {
          ClassPathXmlApplicationContext context = 
              new ClassPathXmlApplicationContext("beans.xml");
          MyService service = context.getBean("myService", MyService.class);
          service.doSomething();
          context.close();
      }
  }
  ```

---

### 5. **Dependencies Inject करें**
IoC कंटेनर आपकी beans में dependencies inject कर सकता है।

#### a) **Constructor Injection (अनुशंसित)**
```java
@Component
public class MyController {
    private final MyService myService;

    public MyController(MyService myService) {
        this.myService = myService;
    }

    public void execute() {
        myService.doSomething();
    }
}
```

#### b) **Setter Injection**
```java
@Component
public class MyController {
    private MyService myService;

    @Autowired
    public void setMyService(MyService myService) {
        this.myService = myService;
    }
}
```

#### c) **Field Injection (कम पसंदीदा)**
```java
@Component
public class MyController {
    @Autowired
    private MyService myService;

    public void execute() {
        myService.doSomething();
    }
}
```
- Injection points को चिह्नित करने के लिए `@Autowired` (Spring-specific) या `@Inject` (JSR-330 standard) का उपयोग करें।

---

### 6. **Beans को चलाएँ और उपयोग करें**
- एक बार कंटेनर चलने के बाद, यह आपकी beans और उनकी dependencies को wire कर देता है। आप `context.getBean()` (सादा Spring) के साथ beans प्राप्त कर सकते हैं या Spring Boot को injection के माध्यम से स्वचालित रूप से संभालने दें।

Spring Boot के साथ उदाहरण:
```java
@SpringBootApplication
public class MyApp {
    public static void main(String[] args) {
        ApplicationContext context = SpringApplication.run(MyApp.class, args);
        MyController controller = context.getBean(MyController.class);
        controller.execute();
    }
}
```

---

### 7. **अतिरिक्त सुझाव**
- **Scopes**: डिफ़ॉल्ट रूप से, beans singletons होते हैं। प्रति अनुरोध नए instances के लिए `@Scope("prototype")` का उपयोग करें।
- **Component Scanning**: यदि beans अलग-अलग packages में हैं तो अपनी configuration क्लास में `@ComponentScan` जोड़ें।
- **Profiles**: विशिष्ट वातावरणों (जैसे, "dev", "prod") में beans को सक्रिय करने के लिए `@Profile` का उपयोग करें।
- **Context को बंद करें**: गैर- Spring Boot ऐप्स में, resources को मुक्त करने के लिए `context.close()` को कॉल करें।

---

यह इसका सार है! सरलता के लिए Spring Boot और annotations के साथ शुरुआत करें। यदि आप किसी विशिष्ट भाग पर अटके हैं—जैसे किसी जटिल dependency को wire करना या debugging—तो बेझिझक पूछें, और मैं आपके साथ गहराई से जाऊंगा!