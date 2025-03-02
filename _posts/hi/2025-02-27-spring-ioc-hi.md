---
audio: true
generated: true
lang: hi
layout: post
title: Spring IoC (Inversion of Control) Container का उपयोग
translated: true
---

मुझे स्प्रिंग IoC (Inversion of Control) कंटेनर का उपयोग करने के तरीके को स्पष्ट और व्यावहारिक तरीके से समझाने की कोशिश करूँगा। स्प्रिंग IoC कंटेनर स्प्रिंग फ्रेमवर्क का कोर है, जो एप्लिकेशन ऑब्जेक्ट्स (बीन्स) के लाइफसाइकल और कॉन्फ़िगरेशन का प्रबंधन करता है। यह "कंट्रोल को उल्टा" करता है, आपकी जगह ऑब्जेक्ट निर्माण और डिपेंडेंसी इंजेक्शन का प्रबंधन करता है।

यहाँ एक स्टेप-बाय-स्टेप गाइड है जो आपको शुरू करने में मदद करेगा:

---

### 1. **बेसिक्स को समझें**
- **क्या यह करता है**: IoC कंटेनर आपके द्वारा प्रदान की गई मेटाडेटा (XML, Java एनोटेशन, या Java कोड के माध्यम से) के आधार पर बीन्स (आपके एप्लिकेशन ऑब्जेक्ट्स) को बनाता, कॉन्फ़िगर करता और प्रबंधित करता है।
- **मुख्य अवधारणाएँ**:
  - **बीन्स**: कंटेनर द्वारा प्रबंधित ऑब्जेक्ट्स।
  - **डिपेंडेंसी इंजेक्शन (DI)**: कंटेनर आपके ऑब्जेक्ट्स में डिपेंडेंसियां (अन्य बीन्स या वेल्यूज) इंजेक्ट करता है।
  - **कॉन्फ़िगरेशन**: आप कंटेनर को बताते हैं कि कौन से बीन्स बनाए और कैसे उन्हें वायर करें।

---

### 2. **अपने प्रोजेक्ट को सेट अप करें**
स्प्रिंग IoC का उपयोग करने के लिए आपको एक स्प्रिंग प्रोजेक्ट चाहिए। अगर आप नया शुरू कर रहे हैं:
- **स्प्रिंग बूट** (सबसे आसान तरीका) या साधारण स्प्रिंग का उपयोग करें।
- अगर आप Maven का उपयोग कर रहे हैं, तो `pom.xml` में डिपेंडेंसियां जोड़ें:
  ```xml
  <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-context</artifactId>
      <version>6.1.3</version> <!-- नएतम वर्जन का उपयोग करें -->
  </dependency>
  ```
- स्प्रिंग बूट के लिए, यह उपयोग करें:
  ```xml
  <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter</artifactId>
      <version>3.2.2</version> <!-- अभी तक नएतम -->
  </dependency>
  ```

---

### 3. **अपने बीन्स को परिभाषित करें**
आप बीन्स को तीन मुख्य तरीकों से परिभाषित कर सकते हैं:

#### a) **एनोटेशन का उपयोग (सबसे आम)**
- एक साधारण Java क्लास बनाएं और इसे `@Component` (या विशेष एनोटेशन जैसे `@Service`, `@Repository` आदि) से एनोटेट करें।
- उदाहरण:
  ```java
  import org.springframework.stereotype.Component;

  @Component
  public class MyService {
      public void doSomething() {
          System.out.println("कुछ कर रहा हूँ!");
      }
  }
  ```

#### b) **Java कॉन्फ़िगरेशन का उपयोग**
- एक कॉन्फ़िगरेशन क्लास बनाएं जिसमें `@Configuration` है और बीन्स को `@Bean` से परिभाषित करें।
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

#### c) **XML का उपयोग (लेगेसी तरीका)**
- एक XML फ़ाइल में बीन्स परिभाषित करें (उदाहरण के लिए, `beans.xml`):
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
आपको कंटेनर को शुरू करना होगा ताकि आपकी बीन्स को प्रबंधित किया जा सके।

#### a) **स्प्रिंग बूट के साथ**
- स्प्रिंग बूट यह स्वचालित रूप से करता है। बस एक मुख्य क्लास बनाएं जिसमें `@SpringBootApplication` है:
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
- कंटेनर `@Component` क्लासों को स्कैन करता है और उन्हें प्रबंधित करता है।

#### b) **साधारण स्प्रिंग (एनोटेशन-आधारित) के साथ**
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

### 5. **डिपेंडेंसियां इंजेक्ट करें**
IoC कंटेनर आपके बीन्स में डिपेंडेंसियां इंजेक्ट कर सकता है।

#### a) **कंस्ट्रक्टर इंजेक्शन (सिफारिश किया गया)**
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

#### b) **सेटर इंजेक्शन**
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

#### c) **फील्ड इंजेक्शन (कम पसंदीदा)**
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
- इंजेक्शन पॉइंट्स को `@Autowired` (स्प्रिंग-विशिष्ट) या `@Inject` (JSR-330 मानक) से चिह्नित करें।

---

### 6. **बीन्स को चलाएं और उपयोग करें**
- एक बार जब कंटेनर चल रहा है, तो वह आपके बीन्स और उनके डिपेंडेंसियां को वायर करता है। आप `context.getBean()` (साधारण स्प्रिंग) के साथ बीन्स प्राप्त कर सकते हैं या स्प्रिंग बूट को इसे स्वचालित रूप से इंजेक्ट करने दें।

स्प्रिंग बूट के साथ उदाहरण:
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

### 7. **अधिक टिप्स**
- **स्कोप्स**: डिफ़ॉल्ट में बीन्स सिंगलटन होते हैं। नए इंस्टेंस प्रति अनुरोध के लिए `@Scope("prototype")` का उपयोग करें।
- **कंपोनेंट स्कैनिंग**: अगर बीन्स अलग-अलग पैकेज में हैं, तो कॉन्फ़िगरेशन क्लास में `@ComponentScan` जोड़ें।
- **प्रोफ़ाइल्स**: `@Profile` का उपयोग करके बीन्स को विशेष वातावरणों (उदाहरण के लिए, "dev", "prod") में सक्रिय करें।
- **कंटेक्स्ट को बंद करें**: नॉन-स्प्रिंग बूट ऐप्स में, `context.close()` को कॉल करें ताकि संसाधन मुक्त हों।

---

यह सब है! स्प्रिंग बूट और एनोटेशन के साथ शुरू करें ताकि यह आसान हो जाए। अगर आप किसी विशेष हिस्से पर अटक गए हैं—जैसे कि एक जटिल डिपेंडेंसी को वायर करना या डिबग करना—तो पूछें, और मैं आपके साथ गहरे में जाऊँगा!