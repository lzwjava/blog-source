---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: نظرة عامة على أنظمة المراسلة في جافا
translated: true
type: note
---

### ما هي أنظمة المراسلة في Java؟

تمكّن أنظمة المراسلة في Java التواصل غير المتزامن بين التطبيقات، أو الخدمات، أو المكونات. بدلاً من المكالمات المتزامنة المباشرة (مثل استدعاءات الدوال)، يتم إرسال الرسائل إلى وسيط مركزي (**وسيط رسائل** أو **طابور**) ومعالجتها لاحقًا من قبل المستلمين. يؤدي هذا إلى فصل المنتجين (المرسلين) والمستهلكين (المستلمين)، مما يحسن قابلية التوسع، وتحمل الأخطاء، والموثوقية في الأنظمة الموزعة.

أبرز المزايا:
- **المعالجة غير المتزامنة**: لا ينتظر المنتجون ردودًا فورية، مما يسمح بعمليات غير عائقية.
- **موازنة الحمل**: يمكن توزيع الرسائل عبر عدة مستهلكين.
- **الموثوقية**: يمكن أن تبقى الرسائل مستمرة حتى يتم الإقرار باستلامها، مما يضمن بقاءها في حالات الأعطال أو مشاكل الشبكة.
- **الفصل**: التغييرات في جزء واحد من النظام لا تؤدي إلى كسر الأجزاء الأخرى.

من حالات الاستخدام الشائعة: اتصال الخدمات المصغرة، وهندسة الأنظمة القائمة على الأحداث، وتوزيع المهام في طوابير (مثل المهام في الخلفية)، ودمج الأنظمة القديمة.

#### JMS (Java Message Service): الواجهة البرمجية القياسية
JMS هو جزء من مواصفات Java EE (الآن Jakarta EE) ويوفر واجهة برمجية محايدة للبائعين للتفاعل مع أنظمة المراسلة. يقوم بتجريد الوسيط الأساسي (مثل Apache ActiveMQ، أو RabbitMQ، أو IBM MQ) بحيث يعمل الكود الخاص بك عبر التطبيقات المختلفة.

يدعم JMS نطاقي **مراسلة** رئيسيين:
- **نقطة إلى نقطة (PTP)**: يستخدم الطوابير. يرسل منتج واحد إلى طابور؛ ويستلم مستهلك واحد (أول داخل، أول خارج). مثالي لتوزيع المهام.
- **النشر-الاشتراك (Pub/Sub)**: يستخدم المواضيع. ينشر المنتجون إلى موضوع؛ ويستلم عدة مشتركين نسخًا من الرسالة. مثالي لبث الأحداث.

##### المكونات الأساسية
- **ConnectionFactory**: ينشئ اتصالات بالوسيط.
- **Connection**: يدير الجلسات مع الوسيط.
- **Session**: يتعامل with المعاملات وإنشاء الرسائل.
- **Destination**: طابور أو موضوع حيث يتم إرسال الرسائل.
- **MessageProducer**: يرسل الرسائل إلى الوجهة.
- **MessageConsumer**: يستلم الرسائل من الوجهة.
- **Message**: الحمولة، مع رؤوس (مثل الأولوية، الطابع الزمني) وخصائص.

يمكن أن تكون الرسائل نصًا، أو كائنات، أو خرائط، أو تدفقات.

##### مثال بسيط
إليك منتج ومستهلك أساسيان لـ JMS باستخدام الطوابير (كود شبه برمجي؛ يتطلب موفر JMS مثل ActiveMQ).

**المنتج (المرسل)**:
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

**المستهلك (المستلم)**:
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
        
        // الإبقاء على التشغيل للاستماع
        try { Thread.sleep(5000); } catch (InterruptedException e) {}
        consumer.close();
        session.close();
        connection.close();
    }
}
```

لتشغيل هذا، أضف تبعية JMS (عبر Maven مثلاً: `javax.jms:javax.jms-api` وعميل ActiveMQ).

##### البدائل الحديثة
بينما يعد JMS أساسيًا، غالبًا ما يستخدم مطورو Java أطر عمل أخف:
- **Spring Boot مع JMS**: يبسط التهيئة.
- **Apache Kafka**: للتدفق عالي الإنتاجية (غير متوافق تمامًا مع JMS ولكن يمكن دمجه).
- **RabbitMQ/AMQP**: قائم على البروتوكول، مع عملاء Java.

للتعمق أكثر، راجع وثائق Jakarta JMS الرسمية.

[Jakarta Messaging Specification](https://jakarta.ee/specifications/messaging/)  
[ActiveMQ Documentation](https://activemq.apache.org/)