---
audio: false
generated: true
image: false
lang: ar
layout: post
model: x-ai/grok-4-fast
title: مظروف SOAP في لغة XML موضَّح
translated: true
type: note
---

### ما هو مغلف XML؟

أعتقد أن "envalop" هو خطأ إملائي لكلمة "envelope"، في إشارة إلى **مغلف SOAP** في XML. SOAP (بروتوكول الوصول البسيط للكائنات) هو بروتوكول لتبادل المعلومات المنظمة في خدمات الويب باستخدام XML. يمثل مغلف SOAP العنصر الجذري لرسالة SOAP، والذي يغلف الرسالة بأكملها لتحديدها كمستند SOAP. وهو يضمن أن يعرف المستقبل أنها رسالة كاملة.

يبدو الهيكل الأساسي لمغلف SOAP كما يلي:

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Header>
    <!-- اختياري: بيانات وصفية مثل المصادقة -->
  </soap:Header>
  <soap:Body>
    <!-- إلزامي: الحمولة/البيانات الفعلية -->
    <YourCustomElement>
      <Data>قيمة ما</Data>
    </YourCustomElement>
  </soap:Body>
</soap:Envelope>
```

- **المغلف (Envelope)**: يحدد بداية/نهاية الرسالة ومساحة الاسم.
- **الرأس (Header)** (اختياري): للمعلومات غير المتعلقة بالجسم مثل الأمان أو التوجيه.
- **الجسم (Body)** (مطلوب): يحتوي على بيانات الطلب/الاستجابة.

يجعل هذا التنسيق رسائل SOAP مستقلة بذاتها ومحايدة للنقل (على سبيل المثال، عبر HTTP).

### كيفية استخدام مغلف SOAP XML في Java

تدعم Java ميزة SOAP مدمجة عبر مكتبات **JAX-WS** (واجهة برمجة تطبيقات Java لخدمات الويب XML) و **SAAJ** (واجهة برمجة تطبيقات SOAP مع المرفقات لـ Java)، وهي جزء من JDK (لا حاجة لاعتماديات خارجية للأساسيات).

#### خطوات إنشاء وإرسال رسالة SOAP:
1. **إنشاء رسالة SOAP**: استخدم `javax.xml.soap` لبناء المغلف برمجيًا.
2. **إضافة المحتوى**: املأ الجسم (والرأس إذا لزم الأمر).
3. **الإرسال عبر HTTP**: استخدم `HttpURLConnection` أو عميلاً مثل JAX-WS لمكالمات خدمة الويب الكاملة.

إليك مثالاً بسيطًا في Java لإنشاء مغلف SOAP وطباعته (يمكنك توسيع هذا لإرساله عبر HTTP):

```java
import javax.xml.soap.*;
import java.util.Iterator;

public class SoapEnvelopeExample {
    public static void main(String[] args) throws Exception {
        // إنشاء مصنع SOAP
        SOAPFactory soapFactory = SOAPFactory.newInstance();
        
        // إنشاء الرسالة والمغلف
        MessageFactory messageFactory = MessageFactory.newInstance();
        SOAPMessage soapMessage = messageFactory.createMessage();
        SOAPEnvelope envelope = soapMessage.getSOAPEnvelope();
        
        // مساحة الاسم لـ SOAP (الإصدار 1.2)
        envelope.addNamespaceDeclaration("soap", "http://www.w3.org/2003/05/soap-envelope");
        
        // إنشاء عنصر الجسم
        SOAPBody body = envelope.getBody();
        SOAPBodyElement bodyElement = body.addBodyElement(soapFactory.createName("GetBalance", "ns", "http://example.com"));
        SOAPElement amount = bodyElement.addChildElement("AccountNumber", "ns", "http://example.com");
        amount.addTextNode("12345");
        
        // حفظ وطباعة الرسالة
        soapMessage.saveChanges();
        System.out.println("SOAP Envelope:");
        soapMessage.writeTo(System.out);
    }
}
```

- **المخرجات**: يولد هذا XML لـ SOAP مع المغلف والجسم وعناصرك المخصصة.
- **لإرساله**: ضعه في غلاف عميل JAX-WS. قم بإنشاء Stubs من ملف WSDL باستخدام أداة `wsimport`: `wsimport -keep YourService.wsdl`. ثم استخدم فئات العميل المُنشأة لاستدعاء الطرق، والتي تتعامل مع المغلف تلقائيًا.
- **المكتبات**: للاستخدام المتقدم، أضف Apache CXF أو Axis2 إذا لزم الأمر، ولكن التزم بـ JDK للبساطة.

شغّل هذا في أي بيئة Java (JDK 8+). لخدمات الويب الكاملة، تأكد من أن مشروعك يتعامل مع الاستثناءات مثل `SOAPException`.

### هل يستخدم Finacle المغلف (SOAP XML)؟

نعم، يستخدم Finacle (برنامج الخدمات المصرفية الأساسية من Infosys) مغلفات SOAP XML على نطاق واسع للتكامل. يعرض خدمات الويب عبر SOAP over HTTP من خلال طبقة **Finacle Integrator**، مما يسمح للأنظمة الخارجية بالتواصل باستخدام بروتوكولات SOAP القياسية. يتضمن ذلك تفاعلات EJB والبرمجيات الوسيطة لخدمات مثل استعلامات الحساب أو المعاملات. غالبًا ما تتبع واجهات برمجة تطبيقات Finacle معايير SOAP للرسائل الآمنة القائمة على XML في عمليات التكامل المصرفية.

[XML Soap - W3Schools](https://www.w3schools.com/xml/xml_soap.asp)  
[The structure of a SOAP message - IBM](https://www.ibm.com/docs/en/integration-bus/9.0.0?topic=soap-structure-message)  
[SOAP - Envelope - Tutorials Point](https://www.tutorialspoint.com/soap/soap_envelope.htm)  
[java - how to add <soap:Envelope> and <soap:body> in xml request - Stack Overflow](https://stackoverflow.com/questions/44721823/how-to-add-soapenvelope-and-soapbody-in-xml-request)  
[SOAPEnvelope (Java Platform SE 8) - Oracle Help Center](https://docs.oracle.com/javase/8/docs/api/javax/xml/soap/SOAPEnvelope.html)  
[Implementation of Microservice on Finacle Integrator using Spring Boot](https://medium.com/@einjoku/implementation-of-microservice-on-finacle-integrator-using-spring-boot-docker-with-kubernetes-d8f9c6026a6d)  
[Architectural Considerations for Integrating with Finacle](https://www.ijcttjournal.org/2024/Volume-72%20Issue-6/IJCTT-V72I6P108.pdf)  
[AS-TFINFRIXM1012-FTX100 Finacle Integration Technical - Scribd](https://www.scribd.com/document/369534444/TFINFRIXM1012-ENU)