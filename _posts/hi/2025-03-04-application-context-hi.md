---
audio: false
generated: true
lang: hi
layout: post
title: स्प्रिंग एप्लिकेशन कॉन्टेक्स्ट तक पहुँच
translated: true
type: note
---

Spring के `ApplicationContextAware` इंटरफेस का उपयोग एक साधारण Java ऑब्जेक्ट (जैसे एक Kafka consumer) में `ApplicationContext` तक पहुँचने के लिए करने के लिए, आपको Spring-प्रबंधित beans और अपने साधारण ऑब्जेक्ट के बीच एक कनेक्शन बनाने की आवश्यकता होती है। यहाँ बताया गया है कि आप इसे कैसे कर सकते हैं:

### सामान्य दृष्टिकोण
`ApplicationContextAware` इंटरफेस एक Spring-प्रबंधित bean को Spring से स्वचालित रूप से `ApplicationContext` प्राप्त करने की अनुमति देता है। आप इसका उपयोग उस साधारण Java ऑब्जेक्ट के लिए context को उपलब्ध कराने के लिए कर सकते हैं जो Spring द्वारा प्रबंधित नहीं है (यानी, Spring container द्वारा निर्मित bean नहीं है)।

#### ApplicationContext तक पहुँचने के चरण
1. **एक Spring-प्रबंधित सहायक क्लास बनाएँ**:
   एक क्लास को परिभाषित करें जो `ApplicationContextAware` को implement करती हो और Spring द्वारा प्रबंधित हो (उदाहरण के लिए, `@Component` से एनोटेट)। यह क्लास Spring एप्लिकेशन शुरू होने पर `ApplicationContext` प्राप्त करेगी।

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

   - `@Component` सुनिश्चित करता है कि Spring इस bean को प्रबंधित करता है।
   - `setApplicationContext` को Spring द्वारा `ApplicationContext` को इंजेक्ट करने के लिए कहा जाता है।
   - एक static `context` variable और getter कहीं से भी पहुँच की अनुमति देते हैं।

2. **अपने साधारण Java ऑब्जेक्ट में Context तक पहुँचें**:
   अपने साधारण Java ऑब्जेक्ट (जैसे, मैन्युअल रूप से बनाया गया एक Kafka consumer) में, सहायक क्लास का उपयोग करके `ApplicationContext` को पुनः प्राप्त करें और Spring-प्रबंधित beans प्राप्त करने के लिए इसका उपयोग करें।

   ```java
   public class MyKafkaConsumer {
       public void processMessage() {
           ApplicationContext context = ApplicationContextProvider.getApplicationContext();
           SomeService service = context.getBean(SomeService.class);
           // आवश्यकतानुसार service या अन्य beans का उपयोग करें
       }
   }
   ```

   - यह काम करता है क्योंकि `ApplicationContextProvider` Spring द्वारा startup पर इनिशियलाइज़ किया जाता है, जिससे context स्टैटिक रूप से उपलब्ध हो जाता है।

3. **विकल्प: Context को स्पष्ट रूप से पास करें**:
   यदि आपका साधारण Java ऑब्जेक्ट एक Spring-प्रबंधित bean द्वारा बनाया गया है, तो आप उस bean में `ApplicationContext` को ऑटोवायर कर सकते हैं और इसे कंस्ट्रक्टर या सेटर के माध्यम से साधारण ऑब्जेक्ट को पास कर सकते हैं।

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
           // service का उपयोग करें
       }
   }
   ```

   - यह static variables से बचाता है, निर्भरता को स्पष्ट बनाता है और परीक्षण क्षमता (testability) में सुधार करता है।

### Kafka Consumer-विशिष्ट समाधान
यदि आप एक Kafka consumer के साथ काम कर रहे हैं और **Spring Kafka** का उपयोग कर रहे हैं, तो अनुशंसित दृष्टिकोण consumer को सीधे Spring ecosystem में एकीकृत करना है न कि इसे एक साधारण Java ऑब्जेक्ट के रूप में मानना।

#### `@KafkaListener` का उपयोग करना
अपने Kafka consumer को एक Spring-प्रबंधित bean के रूप में परिभाषित करें जिसमें एक `@KafkaListener` मेथड हो। यह आपको `ApplicationContext` या अन्य beans को सीधे ऑटोवायर करने की अनुमति देता है।

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
        // context या someService का सीधे उपयोग करें
        SomeService service = context.getBean(SomeService.class); // यदि आवश्यक हो
        someService.process(message);
    }
}
```

- Spring Kafka consumer lifecycle, जिसमें threading और polling शामिल है, को प्रबंधित करता है।
- ऑटोवायरिंग ज़्यादातर मामलों में context को मैन्युअल रूप से प्राप्त करने की आवश्यकता को समाप्त कर देती है।

#### मैन्युअल Kafka Consumer
यदि आपको मैन्युअल रूप से एक `KafkaConsumer` बनाना ही है (उदाहरण के लिए, Kafka client लाइब्रेरी का सीधे उपयोग करके), तो इसे एक Spring-प्रबंधित bean के भीतर बनाएँ और इसे `ApplicationContext` पास करें, जैसा कि ऊपर स्पष्ट पासिंग दृष्टिकोण में दिखाया गया है।

### सिफारिशें
- **Kafka Consumers के लिए**: जहाँ भी संभव हो, Spring-प्रबंधित bean में Spring Kafka के `@KafkaListener` का उपयोग करें। यह Kafka के साथ Spring के एकीकरण का लाभ उठाता है और `ApplicationContext` तथा अन्य beans तक पहुँच को सरल बनाता है।
- **सामान्य साधारण Java ऑब्जेक्ट्स के लिए**: या तो static `ApplicationContextProvider` दृष्टिकोण का उपयोग करें या Spring-प्रबंधित bean से `ApplicationContext` को स्पष्ट रूप से पास करें। स्पष्ट पासिंग विधि को संभव होने पर प्राथमिकता दी जाती है, क्योंकि यह static state से बचती है और परीक्षण क्षमता (testability) में सुधार करती है।

इन विधियों का पालन करके, आप अपने साधारण Java ऑब्जेक्ट, जिसमें एक Kafka consumer भी शामिल है, के लिए Spring context को उपलब्ध कराने के लिए `ApplicationContextAware` का प्रभावी ढंग से उपयोग कर सकते हैं, यह आपके specific setup पर निर्भर करता है।