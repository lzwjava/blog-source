---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग के एप्लिकेशन कॉन्टेक्स्ट तक पहुंच
translated: true
---

Spring के `ApplicationContextAware` interface का उपयोग करके, एक plain Java object, जैसे कि एक Kafka consumer, में `ApplicationContext` को access करने के liye, aapko ek tarah se Spring-managed beans ko aapke plain object ke saath bridge karna padta hai. Yeh aapko kaisa karna hai:

### General Approach
`ApplicationContextAware` interface ek Spring-managed bean ko Spring se `ApplicationContext` ko automatically receive karne ki suvidha deta hai. Aap isse use kar sakte hain ek plain Java object ke liye jo Spring ke dwara manage nahi kiya jaata hai (i.e., Spring container dwara create nahi kiya gaya bean).

#### ApplicationContext ko Access Karne ke Steps
1. **Spring-Managed Helper Class Create Karein**:
   Ek class define karein jo `ApplicationContextAware` implement karta hai aur Spring dwara manage kiya jaata hai (e.g., `@Component` se annotate kiya gaya). Yeh class Spring application start hone par `ApplicationContext` receive karega.

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

   - `@Component` Spring ko yeh bean manage karne ke liye ensure karta hai.
   - `setApplicationContext` Spring dwara `ApplicationContext` inject karne ke liye call kiya jaata hai.
   - Ek static `context` variable aur getter kisi bhi jagah se access karne ki suvidha deta hai.

2. **Plain Java Object mein Context ko Access Karein**:
   Aapke plain Java object (e.g., manually create kiya gaya Kafka consumer) mein, helper class ka use karke `ApplicationContext` ko retrieve karein aur usse Spring-managed beans ko access karne ke liye use karein.

   ```java
   public class MyKafkaConsumer {
       public void processMessage() {
           ApplicationContext context = ApplicationContextProvider.getApplicationContext();
           SomeService service = context.getBean(SomeService.class);
           // Service ya dusre beans ka use karein jahan zaroori hai
       }
   }
   ```

   - Yeh kaam karta hai kyunki `ApplicationContextProvider` Spring dwara startup par initialize kiya jaata hai, context ko statically available karke.

3. **Alternative: Context ko Explicitly Pass Karein**:
   Agar aapka plain Java object ek Spring-managed bean dwara create kiya jaata hai, to aap `ApplicationContext` ko us bean mein autowire kar sakte hain aur usse plain object ko ek constructor ya setter ke dwara pass kar sakte hain.

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
           // Service ka use karein
       }
   }
   ```

   - Yeh static variables ko avoid karta hai, dependency ko explicit banata hai aur testability ko improve karta hai.

### Kafka Consumer-Specific Solution
Agar aap ek Kafka consumer ke saath kaam kar rahe hain aur **Spring Kafka** ka use kar rahe hain, to recommended approach hai consumer ko directly Spring ecosystem mein integrate karna, plain Java object ke roop mein treat karne ke bina.

#### `@KafkaListener` ka Use Karein
Aapka Kafka consumer ko ek Spring-managed bean ke roop mein define karein, ek `@KafkaListener` method ke saath. Yeh aapko `ApplicationContext` ya dusre beans ko directly autowire karne ki suvidha deta hai.

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
        // Context ya someService ko directly use karein
        SomeService service = context.getBean(SomeService.class); // Agar zaroori hai
        someService.process(message);
    }
}
```

- Spring Kafka consumer lifecycle ko manage karta hai, jisme threading aur polling shamil hai.
- Autowiring ke dwara context ko manually fetch karne ki zaroorat kam ho jaati hai.

#### Manual Kafka Consumer
Agar aapko `KafkaConsumer` ko manually create karna padta hai (e.g., Kafka client library ka directly use karke), to usse ek Spring-managed bean ke andar create karein aur usme `ApplicationContext` ko pass karein, jaisa explicit passing approach mein dikhaya gaya hai.

### Recommendations
- **Kafka Consumers ke liye**: Jahan bhi possible hai, Spring Kafka ke `@KafkaListener` ka use karein ek Spring-managed bean mein. Yeh Spring ke Kafka ke saath integration ko leverage karta hai aur `ApplicationContext` aur dusre beans ko access karne ko simplify karta hai.
- **General Plain Java Objects ke liye**: Ya to static `ApplicationContextProvider` approach ka use karein ya `ApplicationContext` ko ek Spring-managed bean se explicitly pass karein. Explicit passing method preferred hota hai jab feasible hai, kyunki yeh static state ko avoid karta hai aur testability ko improve karta hai.

Inhe methods ko follow karke, aap `ApplicationContextAware` ka use karke aapke plain Java object mein, jisme ek Kafka consumer bhi shamil ho sakta hai, Spring context ko effectively available kar sakte hain, aapke specific setup ke hisaab se.