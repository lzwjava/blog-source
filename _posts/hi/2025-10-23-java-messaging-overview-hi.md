---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: जावा मैसेजिंग सिस्टम्स का अवलोकन
translated: true
type: note
---

### जावा में मैसेजिंग सिस्टम क्या हैं?

जावा में मैसेजिंग सिस्टम एप्लिकेशन, सेवाओं या घटकों के बीच अतुल्यकालिक (asynchronous) संचार सक्षम करते हैं। प्रत्यक्ष, तुल्यकालिक कॉल (जैसे मेथड इनवोकेशन) के बजाय, संदेश एक केंद्रीय मध्यस्थ (एक **मैसेज ब्रोकर** या **कतार**) को भेजे जाते हैं और बाद में प्राप्तकर्ताओं द्वारा प्रसंस्कृत किए जाते हैं। यह उत्पादकों (भेजने वालों) और उपभोक्ताओं (प्राप्त करने वालों) को अलग करता है, जिससे वितरित सिस्टम में स्केलेबिलिटी, फॉल्ट टॉलरेंस और विश्वसनीयता में सुधार होता है।

मुख्य लाभ:
- **अतुल्यकालिक प्रसंस्करण**: उत्पादक तत्काल प्रतिक्रिया की प्रतीक्षा नहीं करते हैं, जिससे नॉन-ब्लॉकिंग ऑपरेशन संभव होते हैं।
- **लोड बैलेंसिंग**: संदेशों को कई उपभोक्ताओं में वितरित किया जा सकता है।
- **विश्वसनीयता**: संदेश स्वीकृत होने तक बने रह सकते हैं, क्रैश या नेटवर्क समस्याओं से बचे रहते हैं।
- **डीकपलिंग**: सिस्टम के एक हिस्से में परिवर्तन दूसरों को नहीं तोड़ते हैं।

सामान्य उपयोग के मामलों में माइक्रोसर्विसेज संचार, इवेंट-ड्रिवन आर्किटेक्चर, टास्क कतारबद्धता (जैसे, बैकग्राउंड जॉब) और लीगेसी सिस्टम को एकीकृत करना शामिल है।

#### JMS (जावा मैसेज सर्विस): मानक API
JMS जावा EE (अब जकार्ता EE) स्पेसिफिकेशन का हिस्सा है और मैसेजिंग सिस्टम के साथ इंटरैक्ट करने के लिए एक वेंडर-न्यूट्रल API प्रदान करता है। यह अंतर्निहित ब्रोकर (जैसे, Apache ActiveMQ, RabbitMQ, IBM MQ) को एब्स्ट्रैक्ट करता है ताकि आपका कोड सभी इम्प्लीमेंटेशन में काम करे।

JMS दो मुख्य **मैसेजिंग डोमेन** को सपोर्ट करता है:
- **पॉइंट-टू-पॉइंट (PTP)**: कतारों का उपयोग करता है। एक उत्पादक एक कतार को भेजता है; एक उपभोक्ता प्राप्त करता है (फर्स्ट-इन, फर्स्ट-आउट)। टास्क वितरण के लिए आदर्श।
- **पब्लिश-सब्सक्राइब (Pub/Sub)**: टॉपिक्स का उपयोग करता है। उत्पादक एक टॉपिक को पब्लिश करते हैं; कई सब्सक्राइबर्स प्रतियां प्राप्त करते हैं। इवेंट्स को प्रसारित करने के लिए आदर्श।

##### मुख्य घटक
- **ConnectionFactory**: ब्रोकर से कनेक्शन बनाता है।
- **Connection**: ब्रोकर के साथ सेशन प्रबंधित करता है।
- **Session**: लेन-देन और संदेश निर्माण को संभालता है।
- **Destination**: एक कतार या टॉपिक जहां संदेश भेजे जाते हैं।
- **MessageProducer**: एक डेस्टिनेशन को संदेश भेजता है।
- **MessageConsumer**: एक डेस्टिनेशन से संदेश प्राप्त करता है।
- **Message**: पेलोड, हेडर (जैसे, प्राथमिकता, टाइमस्टैम्प) और गुणों के साथ।

संदेश टेक्स्ट, ऑब्जेक्ट्स, मैप्स, या स्ट्रीम्स हो सकते हैं।

##### सरल उदाहरण
यहां कतारों का उपयोग करते हुए एक बुनियादी JMS प्रोड्यूसर और कंज्यूमर दिया गया है (स्यूडो-कोड; JMS प्रोवाइडर जैसे ActiveMQ की आवश्यकता होती है)।

**प्रोड्यूसर (भेजने वाला)**:
```java
import javax.jms.*;

public class JMSProducer {
    public static void main(String[] args) throws JMSException {
        ConnectionFactory factory = new ActiveMQConnectionFactory("tcp://localhost:61616");
        Connection connection = factory.createConnection();
        connection.start();
        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        Queue queue = session.createQueue("exampleQueue");
        MessageProducer producer = session.createProducer(queue);
        
        TextMessage message = session.createTextMessage("Hello, JMS!");
        producer.send(message);
        
        producer.close();
        session.close();
        connection.close();
    }
}
```

**कंज्यूमर (प्राप्त करने वाला)**:
```java
import javax.jms.*;

public class JMSConsumer {
    public static void main(String[] args) throws JMSException {
        ConnectionFactory factory = new ActiveMQConnectionFactory("tcp://localhost:61616");
        Connection connection = factory.createConnection();
        connection.start();
        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        Queue queue = session.createQueue("exampleQueue");
        MessageConsumer consumer = session.createConsumer(queue);
        
        consumer.setMessageListener(msg -> {
            try {
                System.out.println("Received: " + ((TextMessage) msg).getText());
            } catch (JMSException e) {
                e.printStackTrace();
            }
        });
        
        // सुनने के लिए चलते रहें
        try { Thread.sleep(5000); } catch (InterruptedException e) {}
        consumer.close();
        session.close();
        connection.close();
    }
}
```

इसे चलाने के लिए, एक JMS डिपेंडेंसी जोड़ें (जैसे, Maven के माध्यम से: `javax.jms:javax.jms-api` और एक ActiveMQ क्लाइंट)।

##### आधुनिक विकल्प
हालांकि JMS मूलभूत है, जावा डेवलपर्स अक्सर हल्के फ्रेमवर्क का उपयोग करते हैं:
- **Spring Boot with JMS**: कॉन्फ़िगरेशन को सरल बनाता है।
- **Apache Kafka**: उच्च-थ्रूपुट स्ट्रीमिंग के लिए (सख्ती से JMS-संगत नहीं है लेकिन एकीकरण योग्य)।
- **RabbitMQ/AMQP**: प्रोटोकॉल-आधारित, जावा क्लाइंट्स के साथ।

गहन जानकारी के लिए, आधिकारिक जकार्ता JMS डॉक्यूमेंटेशन देखें।

[Jakarta Messaging Specification](https://jakarta.ee/specifications/messaging/)  
[ActiveMQ Documentation](https://activemq.apache.org/)