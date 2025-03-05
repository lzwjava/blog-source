---
audio: true
generated: true
lang: hi
layout: post
title: 'XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans


  XML Configuration Files For Beans'
translated: true
---

आपके प्रश्न के बारे में बीन्स XML कैसे काम करता है, जिसमें बीन प्रॉपर्टीज, प्रॉप्स और कीज शामिल हैं, कौन सा क्लास इन XML फाइलों का उपयोग करता है, और वे कैसे लोड होते हैं, इसे स्पष्ट और व्यवस्थित रूप से समझने के लिए इसे तोड़ें। यह व्याख्या एक ऐसी सन्दर्भ में है जहां "बीन्स XML" एक आम शब्द है बीन्स को कॉन्फ़िगर करने के लिए, जैसे कि स्प्रिंग में।

### बीन्स XML कैसे काम करता है?

स्प्रिंग जैसे फ्रेमवर्क में, एक **बीन्स XML फाइल** एक कॉन्फ़िगरेशन फाइल है जो *बीन्स* कहलाने वाले ऑब्जेक्ट्स को परिभाषित और प्रबंधित करने के लिए उपयोग की जाती है। ये बीन्स आमतौर पर स्प्रिंग फ्रेमवर्क द्वारा इंस्टैंसियेट, कॉन्फ़िगर और प्रबंधित Java ऑब्जेक्ट्स होते हैं। XML फाइल में निम्नलिखित चीजें परिभाषित होती हैं:

- **बीन्स**: प्रत्येक बीन को एक `<bean>` टैग का उपयोग करके परिभाषित किया जाता है, जिसमें एक `id` (एक अनन्य पहचानकर्ता) और एक `class` (इंस्टैंसियेट करने के लिए Java क्लास का पूर्ण रूप से क्वालीफाइड नाम) शामिल होता है।
- **प्रॉपर्टीज**: बीन्स के पास प्रॉपर्टीज हो सकती हैं, जो बीन के व्यवहार को कॉन्फ़िगर करने के लिए बीन में सेट किए गए मान या संदर्भ होते हैं। प्रॉपर्टीज को एक `<property>` टैग का उपयोग करके परिभाषित किया जाता है।
- **प्रॉप्स और कीज**: एक `<property>` टैग के भीतर, आप एक `<props>` तत्व का उपयोग करके एक सेट ऑफ की-वैल्यू पेअर परिभाषित कर सकते हैं। यह तब उपयोगी होता है जब एक बीन एक `java.util.Properties` ऑब्जेक्ट या एक समान संरचना जैसे एक `Map` की अपेक्षा करता है। `<props>` तत्व में कई `<prop>` टैग होते हैं, प्रत्येक के साथ एक `key` अट्रिब्यूट और एक संबद्ध मान।

यह एक बीन्स XML फाइल में कैसे दिखता है:

```xml
<bean id="myBean" class="com.example.MyBean">
    <property name="someProperty">
        <props>
            <prop key="key1">value1</prop>
            <prop key="key2">value2</prop>
        </props>
    </property>
</bean>
```

इस उदाहरण में:
- एक बीन ID `myBean` से बनाया जाता है `com.example.MyBean` क्लास से।
- बीन के पास एक प्रॉपर्टी है जिसका नाम `someProperty` है।
- `<props>` तत्व एक सेट ऑफ की-वैल्यू पेअर (`key1=value1` और `key2=value2`) परिभाषित करता है, जो स्प्रिंग एक `Properties` ऑब्जेक्ट में परिवर्तित करता है और इसे `myBean` में एक सेटर विधि जैसे `setSomeProperty(Properties props)` के माध्यम से इंजेक्ट करता है।

आपके प्रश्न में "यह संसाधनों में डालता है" वाक्यांश थोड़ा अस्पष्ट है, लेकिन यह संभवतः XML फाइल को एक *संसाधन* (एक फाइल एप्लिकेशन के क्लासपाथ या फाइल सिस्टम में) के रूप में संदर्भित करता है जो एप्लिकेशन द्वारा उपयोग किया जाता है, या यह हो सकता है कि XML में परिभाषित बीन्स (जैसे एक डेटा स्रोत) एप्लिकेशन द्वारा उपयोग किए जाने वाले संसाधनों को दर्शाते हैं। अब, हम यह मानते हैं कि यह XML फाइल खुद को एक संसाधन के रूप में लोड करने के बारे में है।

### कौन सा क्लास इन XML फाइलों का उपयोग करेगा?

स्प्रिंग में, बीन्स XML फाइल का उपयोग करने (i.e., लोड और प्रोसेस) के लिए जिम्मेदार क्लास **`ApplicationContext`** है। अधिक स्पष्ट रूप से, यह `ApplicationContext` इंटरफेस का एक इम्प्लीमेंटेशन है, जैसे:

- **`ClassPathXmlApplicationContext`**: क्लासपाथ से XML फाइल लोड करता है।
- **`FileSystemXmlApplicationContext`**: फाइल सिस्टम से XML फाइल लोड करता है।

`ApplicationContext` स्प्रिंग का केंद्र इंटरफेस है एप्लिकेशन को कॉन्फ़िगरेशन जानकारी प्रदान करने के लिए। यह बीन्स XML फाइल को पढ़ता है, इसे पार्स करता है, और परिभाषाओं का उपयोग करके बीन्स को बनाता और प्रबंधित करता है। जबकि बीन्स खुद (जैसे `com.example.MyBean`) XML में परिभाषित प्रॉपर्टीज का उपयोग करते हैं, `ApplicationContext` वह क्लास है जो XML फाइल को पढ़ने के लिए सीधे प्रोसेस करता है।

### यह कैसे लोड होगा?

बीन्स XML फाइल को एप्लिकेशन में लोड करने के लिए, एक `ApplicationContext` इम्प्लीमेंटेशन का एक इंस्टैंस बनाया जाता है और XML फाइल का स्थान परिभाषित किया जाता है। यह कैसे काम करता है, चरण-दर-चरण:

1. **XML फाइल स्थान परिभाषित करें**: जब आप `ApplicationContext` को इंस्टैंसियेट करते हैं, तो आप XML फाइल का नाम या पथ प्रदान करते हैं। उदाहरण के लिए:
   ```java
   ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
   ```
   यहाँ, `"beans.xml"` को क्लासपाथ में मान लिया जाता है (जैसे कि एक आम Java प्रोजेक्ट में `src/main/resources` डायरेक्टरी में).

2. **संसाधन के रूप में लोड करें**: `ApplicationContext` एक `ResourceLoader` का उपयोग करता है XML फाइल को एक `Resource` के रूप में खोजने और लोड करने के लिए। इस मामले में, `ClassPathXmlApplicationContext` फाइल को क्लासपाथ में खोजता है।

3. **XML पार्स करें**: अंदरूनी रूप से, स्प्रिंग एक `XmlBeanDefinitionReader` का उपयोग करता है XML फाइल को पार्स करने के लिए। यह रीडर `<bean>` टैग, प्रॉपर्टीज, और `<props>` तत्वों को समझता है, और प्रत्येक बीन को कैसे बनाया जाना चाहिए, यह बताने वाले `BeanDefinition` ऑब्जेक्ट्स बनाता है।

4. **बीन बनाएं**: `ApplicationContext` (जो स्प्रिंग के `BeanFactory` का एक विस्तार है) इन बीन परिभाषाओं का उपयोग करता है बीन्स को इंस्टैंसियेट करने, उनके प्रॉपर्टीज सेट करने (जिसमें `<props>` से `Properties` ऑब्जेक्ट का इंजेक्शन शामिल है), और उनके लाइफसाइकल को प्रबंधित करने के लिए।

एक बार लोड होने के बाद, आप बीन्स को `ApplicationContext` से इस तरह से प्राप्त कर सकते हैं:
```java
MyBean myBean = context.getBean("myBean", MyBean.class);
```

### सब मिलाकर

- **बीन्स XML कैसे काम करता है**: XML बीन्स और उनके प्रॉपर्टीज, जिसमें `<props>` के माध्यम से की-वैल्यू पेअर शामिल हैं, परिभाषित करता है। स्प्रिंग इस XML को पार्स करता है बीन्स को कॉन्फ़िगर और इंस्टैंसियेट करने के लिए।
- **XML का उपयोग करने वाला क्लास**: `ApplicationContext` (जैसे `ClassPathXmlApplicationContext`) XML फाइल का उपयोग करता है एप्लिकेशन को सेट अप करने के लिए।
- **यह कैसे लोड होगा**: XML को एक संसाधन के रूप में क्लासपाथ या फाइल सिस्टम से लोड किया जाता है जब आप एक `ApplicationContext` इंस्टैंस बनाते हैं, और फाइल का स्थान परिभाषित करते हैं।

उदाहरण के लिए, अगर आपका `beans.xml` क्लासपाथ में है, तो आप इसे इस तरह से लोड करेंगे:
```java
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```
फिर स्प्रिंग बाकी सब संभाल लेता है, और कॉन्फ़िगर किए गए बीन्स को आपके एप्लिकेशन के लिए उपलब्ध कर देता है।

यह यंत्र शक्तिशाली और लचीला है, जो आपको XML में जटिल कॉन्फ़िगरेशन परिभाषित करने की अनुमति देता है जो स्प्रिंग रनटाइम पर जीवित कर देता है।