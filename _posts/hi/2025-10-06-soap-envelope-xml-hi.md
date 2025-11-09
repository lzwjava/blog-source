---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: साबुन लिफाफा एक्सएमएल समझाया
translated: true
type: note
---

### एनवेलप XML क्या है?

मेरा मानना है कि "envalop" एक टाइपो है "envelope" का, जो XML में **SOAP एनवेलप** को संदर्भित करता है। SOAP (सिंपल ऑब्जेक्ट एक्सेस प्रोटोकॉल) XML का उपयोग करके वेब सेवाओं में संरचित जानकारी के आदान-प्रदान के लिए एक प्रोटोकॉल है। SOAP एनवेलप एक SOAP संदेश का रूट एलिमेंट है, जो पूरे संदेश को लपेटता है और इसे एक SOAP दस्तावेज़ के रूप में पहचानता है। यह सुनिश्चित करता है कि रिसीवर को पता चल जाए कि यह एक पूरा संदेश है।

एक बुनियादी SOAP एनवेलप संरचना कुछ इस तरह दिखती है:

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope">
  <soap:Header>
    <!-- वैकल्पिक: प्रमाणीकरण जैसे मेटाडेटा -->
  </soap:Header>
  <soap:Body>
    <!-- अनिवार्य: वास्तविक पेलोड/डेटा -->
    <YourCustomElement>
      <Data>कुछ मान</Data>
    </YourCustomElement>
  </soap:Body>
</soap:Envelope>
```

- **एनवेलप**: संदेश की शुरुआत/अंत और नेमस्पेस को परिभाषित करता है।
- **हेडर** (वैकल्पिक): गैर-बॉडी जानकारी जैसे सुरक्षा या रूटिंग के लिए।
- **बॉडी** (आवश्यक): अनुरोध/प्रतिक्रिया डेटा रखती है।

यह फॉर्मेट SOAP संदेशों को स्व-निहित और ट्रांसपोर्ट-अज्ञेय (जैसे, HTTP पर) बनाता है।

### Java में SOAP एनवेलप XML का उपयोग कैसे करें

Java में **JAX-WS** (Java API for XML Web Services) और **SAAJ** (SOAP with Attachments API for Java) लाइब्रेरीज़ के माध्यम से SOAP के लिए अंतर्निहित सपोर्ट है, जो JDK का हिस्सा हैं (बुनियादी चीजों के लिए बाहरी निर्भरता की आवश्यकता नहीं है)।

#### एक SOAP संदेश बनाने और भेजने के चरण:
1.  **एक SOAP संदेश बनाएं**: एनवेलप को प्रोग्रामेटिक रूप से बनाने के लिए `javax.xml.soap` का उपयोग करें।
2.  **सामग्री जोड़ें**: बॉडी (और यदि आवश्यक हो तो हेडर) को भरें।
3.  **HTTP के माध्यम से भेजें**: पूर्ण वेब सेवा कॉल के लिए `HttpURLConnection` या JAX-WS जैसे क्लाइंट का उपयोग करें।

यहां एक साधारण Java उदाहरण दिया गया है जो एक SOAP एनवेलप बनाता है और इसे प्रिंट करता है (आप इसे HTTP पर भेजने के लिए विस्तारित कर सकते हैं):

```java
import javax.xml.soap.*;
import java.util.Iterator;

public class SoapEnvelopeExample {
    public static void main(String[] args) throws Exception {
        // एक SOAP फैक्ट्री बनाएं
        SOAPFactory soapFactory = SOAPFactory.newInstance();
        
        // संदेश और एनवेलप बनाएं
        MessageFactory messageFactory = MessageFactory.newInstance();
        SOAPMessage soapMessage = messageFactory.createMessage();
        SOAPEnvelope envelope = soapMessage.getSOAPEnvelope();
        
        // SOAP के लिए नेमस्पेस (वर्जन 1.2)
        envelope.addNamespaceDeclaration("soap", "http://www.w3.org/2003/05/soap-envelope");
        
        // बॉडी एलिमेंट बनाएं
        SOAPBody body = envelope.getBody();
        SOAPBodyElement bodyElement = body.addBodyElement(soapFactory.createName("GetBalance", "ns", "http://example.com"));
        SOAPElement amount = bodyElement.addChildElement("AccountNumber", "ns", "http://example.com");
        amount.addTextNode("12345");
        
        // संदेश सेव करें और प्रिंट करें
        soapMessage.saveChanges();
        System.out.println("SOAP एनवेलप:");
        soapMessage.writeTo(System.out);
    }
}
```

- **आउटपुट**: यह एनवेलप, बॉडी और आपके कस्टम एलिमेंट्स के साथ एक SOAP XML जनरेट करता है।
- **इसे भेजने के लिए**: इसे एक JAX-WS क्लाइंट में रैप करें। `wsimport` टूल का उपयोग करके WSDL फ़ाइल से स्टब जनरेट करें: `wsimport -keep YourService.wsdl`। फिर मेथड्स को इनवोक करने के लिए जनरेट की गई क्लाइंट क्लासेस का उपयोग करें, जो एनवेलप को स्वचालित रूप से हैंडल करती हैं।
- **लाइब्रेरीज़**: उन्नत उपयोग के लिए, यदि आवश्यक हो तो Apache CXF या Axis2 जोड़ें, लेकिन सरलता के लिए JDK पर ही बने रहें।

इसे किसी भी Java एनवीरोंमेंट (JDK 8+) में रन करें। पूर्ण वेब सेवाओं के लिए, सुनिश्चित करें कि आपका प्रोजेक्ट `SOAPException` जैसे एक्सेप्शन्स को हैंडल करता है।

### क्या फाइनेकल एनवेलप (SOAP XML) का उपयोग करता है?

हां, फाइनेकल (इन्फोसिस का कोर बैंकिंग सॉफ्टवेयर) एकीकरण के लिए बड़े पैमाने पर SOAP XML एनवेलप का उपयोग करता है। यह **फाइनेकल इंटीग्रेटर** लेयर के माध्यम से SOAP over HTTP के जरिए वेब सेवाएं एक्सपोज़ करता है, जिससे बाहरी सिस्टम मानक SOAP प्रोटोकॉल का उपयोग करके संचार कर सकते हैं। इसमें EJB इंटरैक्शन और अकाउंट क्वेरीज़ या लेन-देन जैसी सेवाओं के लिए मिडलवेयर शामिल है। फाइनेकल की API अक्सर बैंकिंग एकीकरण में सुरक्षित, XML-आधारित मैसेजिंग के लिए SOAP मानकों का पालन करती हैं।

[XML Soap - W3Schools](https://www.w3schools.com/xml/xml_soap.asp)  
[The structure of a SOAP message - IBM](https://www.ibm.com/docs/en/integration-bus/9.0.0?topic=soap-structure-message)  
[SOAP - Envelope - Tutorials Point](https://www.tutorialspoint.com/soap/soap_envelope.htm)  
[java - how to add <soap:Envelope> and <soap:body> in xml request - Stack Overflow](https://stackoverflow.com/questions/44721823/how-to-add-soapenvelope-and-soapbody-in-xml-request)  
[SOAPEnvelope (Java Platform SE 8) - Oracle Help Center](https://docs.oracle.com/javase/8/docs/api/javax/xml/soap/SOAPEnvelope.html)  
[Implementation of Microservice on Finacle Integrator using Spring Boot](https://medium.com/@einjoku/implementation-of-microservice-on-finacle-integrator-using-spring-boot-docker-with-kubernetes-d8f9c6026a6d)  
[Architectural Considerations for Integrating with Finacle](https://www.ijcttjournal.org/2024/Volume-72%20Issue-6/IJCTT-V72I6P108.pdf)  
[AS-TFINFRIXM1012-FTX100 Finacle Integration Technical - Scribd](https://www.scribd.com/document/369534444/TFINFRIXM1012-ENU)