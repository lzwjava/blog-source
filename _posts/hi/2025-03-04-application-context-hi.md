---
audio: false
generated: true
lang: hi
layout: post
title: Spring ke ApplicationContext ko Access Karna
translated: true
---

Spring के `ApplicationContextAware` interface का उपयोग करके, एक plain Java object, जैसे कि एक Kafka consumer, में `ApplicationContext` तक पहुंचने के लिए, aapko Spring-managed beans ko aapke plain object ke saath bridge karne ki zaroorat hai. Yeh aapko kaise kar sakte hain:

### General Approach
`ApplicationContextAware` interface ek Spring-managed bean ko automatically `ApplicationContext` ko Spring se receive karne ki suvidha deta hai. Aap isse use kar sakte hain taaki context ko ek plain Java object ko available kar sakte hain jo Spring ke dwara manage nahi kiya jaata hai (i.e., Spring container dwara create nahi kiya gaya bean).

#### ApplicationContext ko Access karne ke Steps
1. **Spring-Managed Helper Class Create Karein**:
   Ek class define karein jo `ApplicationContextAware` ko implement karta hai aur Spring dwara manage kiya jaata hai (e.g., `@Component` se annotate kiya gaya). Yeh class Spring application start hone par `ApplicationContext` ko receive karega.

   ```java
   import org.springframework.context.ApplicationContext;
   import org.springframework.context.ApplicationContextAware;
   import org.springframework.stereotype.Component;

   @Component
   public class ApplicationContextProvider implements ApplicationContextAware {
       private static ApplicationContext context;

       @Override
       public void setApplicationContext(ApplicationContext applicationContext) {
           context = applicationContext;
       }

       public static ApplicationContext getApplicationContext() {
           return context;
       }
   }
   ```

   - `@Component` ensure karta hai ki Spring yeh bean manage kare.
   - `setApplicationContext` Spring dwara `ApplicationContext` ko inject karne ke liye call kiya jaata hai.
   - Ek static `context` variable aur getter se har jagah se access karne ki suvidha deta hai.

2. **Plain Java Object mein Context ko Access Karein**:
   Aapke plain Java object (e.g., manually create kiya gaya Kafka consumer) mein, helper class ka use karke `ApplicationContext` ko retrieve karein aur use karke Spring-managed beans ko access karein.

   ```java
   public class MyKafkaConsumer {
       public void processMessage() {
           ApplicationContext context = ApplicationContextProvider.getApplicationContext();
           SomeService service = context.getBean(SomeService.class);
           // Use the service or other beans as needed
       }
   }
   ```

   - Yeh kaam karta hai kyunki `ApplicationContextProvider` Spring dwara startup par initialize kiya jaata hai, context ko statically available karke.

3. **Alternative: Context ko Explicitly Pass Karein**:
   Agar aapka plain Java object ek Spring-managed bean dwara create kiya jaata hai, to aap `ApplicationContext` ko us bean mein autowire kar sakte hain aur usse plain object ko constructor ya setter ke dwara pass kar sakte hain.

   ```java
   import org.springframework.beans.factory.annotation.Autowired;
   import org.springframework.context.ApplicationContext;
   import org.springframework.stereotype.Component;

   @Component
   public class KafkaConsumerCreator {
       @Autowired
       private ApplicationContext context;

       public MyKafkaConsumer createConsumer() {
           return new MyKafkaConsumer(context);
       }
   }

   public class MyKafkaConsumer {
       private final ApplicationContext context;

       public MyKafkaConsumer(ApplicationContext context) {
           this.context = context;
       }

       public void processMessage() {
           SomeService service = context.getBean(SomeService.class);
           // Use the service
       }
   }
   ```

   - Yeh static variables ko avoid karta hai, dependency ko explicit banata hai aur testability ko improve karta hai.

### Kafka Consumer-Specific Solution
Agar aap ek Kafka consumer ke saath kaam kar rahe hain aur **Spring Kafka** ka use kar rahe hain, to recommended approach hai ki consumer ko directly Spring ecosystem mein integrate karna hai, plain Java object ke roop mein treat karne ke bina.

#### `@KafkaListener` ka Use Karein
Aapke Kafka consumer ko ek Spring-managed bean ke roop mein define karein, ek `@KafkaListener` method ke saath. Yeh aapko `ApplicationContext` ya other beans ko directly autowire karne ki suvidha deta hai.

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class MyKafkaConsumer {
    @Autowired
    private ApplicationContext context;

    @Autowired
    private SomeService someService;

    @KafkaListener(topics = "my-topic")
    public void consume(String message) {
        // Use context or someService directly
        SomeService service = context.getBean(SomeService.class); // Agar zaroorat ho
        someService.process(message);
    }
}
```

- Spring Kafka consumer lifecycle ko manage karta hai, jisme threading aur polling shamil hain.
- Autowiring ke dwara context ko manually fetch karne ki zaroorat ko eliminate karta hai.

#### Manual Kafka Consumer
Agar aapko `KafkaConsumer` ko manually create karna padta hai (e.g., Kafka client library ka directly use karke), to usse ek Spring-managed bean ke andar karein aur usse `ApplicationContext` ko pass karein, jaisa explicit passing approach mein dikhaya gaya hai.

### Recommendations
- **Kafka Consumers ke liye**: Jaha bhi possible hai, Spring Kafka ke `@KafkaListener` ko ek Spring-managed bean mein use karein. Yeh Spring ke Kafka ke saath integration ko leverage karta hai aur `ApplicationContext` aur other beans tak access karne ko simplify karta hai.
- **General Plain Java Objects ke liye**: Ya to static `ApplicationContextProvider` approach ka use karein ya `ApplicationContext` ko ek Spring-managed bean se explicitly pass karein. Explicit passing method ko prefer karein jab feasible ho, kyunki yeh static state ko avoid karta hai aur testability ko improve karta hai.

In methods ko follow karke, aap `ApplicationContextAware` ka use karke effectively kar sakte hain taaki Spring context ko aapke plain Java object, including a Kafka consumer, ko available kar sakte hain, aapke specific setup ke hisaab se.