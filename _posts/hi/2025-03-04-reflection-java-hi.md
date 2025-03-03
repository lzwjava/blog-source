---
audio: false
generated: true
lang: hi
layout: post
title: Java में प्रतिबिम्ब
translated: true
---

### मुख्य बिंदु
- यह प्रतीत होता है कि `java.lang.reflect` Java में प्रतिबिम्ब (reflection) के लिए उपयोग किया जाता है, जो प्रोग्रामों को रनटाइम पर अपने संरचना को जांचने और संशोधित करने की अनुमति देता है।
- अनुसंधान से पता चलता है कि मुख्य वर्ग `Class`, `Method`, `Field`, और `Constructor` हैं, जो वर्ग घटकों को जांचने और संशोधित करने के लिए हैं।
- सबूत सामान्य उपयोगों जैसे डायनामीक विधि प्रारंभ (dynamic method invocation), निजी क्षेत्रों तक पहुंच (accessing private fields), और सामान्य फ्रेमवर्क बनाने की ओर इशारा करते हैं।

### `java.lang.reflect` क्या है?
`java.lang.reflect` Java में एक पैकेज है जो प्रतिबिम्ब (reflection) को सक्षम बनाता है, जो एक विशेषता है जो प्रोग्रामों को रनटाइम पर अपने संरचना और व्यवहार को जांचने या संशोधित करने की अनुमति देता है। इसका मतलब है कि आप वर्ग, विधियों, क्षेत्रों को जांच सकते हैं, और उन्हें डायनामीक रूप से प्रारंभ (invoke) कर सकते हैं, बिना उन्हें कॉम्पाइल टाइम पर जानने के।

### इसका उपयोग कैसे करें
`java.lang.reflect` का उपयोग करने के लिए, एक `Class` वस्तु प्राप्त करने से शुरू करें, जो आप जांचना चाहते हैं। आप इसे तीन तरीकों से कर सकते हैं:
- यदि आप वर्ग को कॉम्पाइल टाइम पर जानते हैं, तो `MyClass.class` का उपयोग करें।
- एक वस्तु पर `instance.getClass()` को कॉल करें।
- डायनामीक लोडिंग के लिए `Class.forName("package.ClassName")` का उपयोग करें, हालांकि यह `ClassNotFoundException` फेंक सकता है।

एक बार जब आप `Class` वस्तु प्राप्त कर लेते हैं, तो आप:
- `getMethods()` के साथ सार्वजनिक विधियों को प्राप्त करें या `getDeclaredMethods()` के साथ सभी विधियों को प्राप्त करें, जिसमें निजी विधियाँ भी शामिल हैं।
- `getFields()` के साथ सार्वजनिक क्षेत्रों तक पहुंचें या `getDeclaredFields()` के साथ सभी क्षेत्रों तक पहुंचें, और `setAccessible(true)` का उपयोग निजी क्षेत्रों तक पहुंचने के लिए करें।
- `getConstructors()` के साथ निर्माणकर्ताओं (constructors) के साथ काम करें और `newInstance()` के साथ उदाहरण (instances) बनाएं।

उदाहरण के लिए, एक निजी विधि को प्रारंभ करने के लिए:
- `Method` वस्तु प्राप्त करें, `setAccessible(true)` से इसे सक्षम करें, फिर `invoke()` का उपयोग करके इसे कॉल करें।

### अनपेक्षित विवरण
एक अनपेक्षित पहलू यह है कि प्रतिबिम्ब (reflection) सुरक्षा को कमजोर कर सकता है, क्योंकि यह एक्सेस मॉडिफायर को बाइपास कर सकता है, इसलिए `setAccessible(true)` का सावधानी से उपयोग करें, विशेष रूप से उत्पादन कोड में।

---

### सर्वेक्षण नोट: `java.lang.reflect` का उपयोग करने का व्यापक मार्गदर्शन

यह नोट `java.lang.reflect` पैकेज में Java में एक गहन अन्वेषण प्रदान करता है, जिसमें इसकी कार्यक्षमता, उपयोग, और परिणाम शामिल हैं, जो उपलब्ध संसाधनों का विस्तृत विश्लेषण पर आधारित हैं। प्रतिबिम्ब (reflection) Java में एक शक्तिशाली विशेषता है, जो प्रोग्रामों को रनटाइम पर अपने संरचना को जांचने और संशोधित करने की अनुमति देता है, और यह विशेष रूप से डायनामीक प्रोग्रामिंग सीनारियो में मूल्यवान है।

#### Java में प्रतिबिम्ब (Reflection) का परिचय

प्रतिबिम्ब (reflection) एक विशेषता है जो Java प्रोग्रामिंग भाषा में है, जो एक चलने वाले प्रोग्राम को अपने आप पर "introspect" करने और आंतरिक गुणों को संशोधित करने की अनुमति देता है। यह क्षमता Pascal, C, या C++ जैसे भाषाओं में आम तौर पर नहीं पाई जाती है, जिससे Java का प्रतिबिम्ब एक अनोखा और शक्तिशाली औजार बन जाता है। उदाहरण के लिए, यह एक Java वर्ग को अपने सभी सदस्यों के नाम प्राप्त करने और उन्हें प्रदर्शित करने की अनुमति देता है, जो JavaBeans जैसे सीनारियो में उपयोगी है, जहां सॉफ्टवेयर घटक प्रतिबिम्ब (reflection) का उपयोग करके डायनामीक रूप से लोड और वर्ग गुणों को जांच कर सकते हैं, ताकि वे बिल्डर टूल्स के माध्यम से दृश्य रूप से संशोधित हो सकें ([Using Java Reflection](https://www.oracle.com/technical-resources/articles/java/javareflection.html)).

`java.lang.reflect` पैकेज आवश्यक वर्ग और इंटरफेस प्रदान करता है, जो प्रतिबिम्ब (reflection) को लागू करने के लिए हैं, जो डिबगर्स, इंटरप्रेटर्स, वस्तु जांचकर्ताओं, वर्ग ब्राउज़र्स, और Object Serialization और JavaBeans जैसे सेवाओं का समर्थन करते हैं। इस पैकेज, साथ ही `java.lang.Class`, लक्ष्य वस्तु के सार्वजनिक सदस्यों तक पहुंच प्रदान करता है, जो उसके रनटाइम वर्ग या किसी दिए गए वर्ग द्वारा घोषित सदस्यों के आधार पर है, साथ ही `ReflectPermission` उपलब्ध होने पर डिफॉल्ट प्रतिबिम्ब (reflection) एक्सेस कंट्रोल को दबाने के विकल्प के साथ ([java.lang.reflect (Java Platform SE 8)](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/package-summary.html)).

#### मुख्य वर्ग और उनके भूमिकाएँ

`java.lang.reflect` पैकेज में कुछ मुख्य वर्ग शामिल हैं, प्रत्येक प्रतिबिम्ब (reflection) में एक विशेष उद्देश्य निभाता है:

- **Class**: Java Virtual Machine (JVM) में एक वर्ग या इंटरफेस का प्रतिनिधित्व करता है। यह प्रतिबिम्ब (reflection) ऑपरेशनों के लिए प्रवेश द्वार है, जो रनटाइम गुणों को जांचने के लिए विधियाँ प्रदान करता है, जिसमें सदस्य और प्रकार जानकारी शामिल है। प्रत्येक प्रकार के वस्तु के लिए, JVM एक अपरिवर्तनीय `java.lang.Class` का उदाहरण बनाता है, जो नए वर्गों और वस्तुओं को बनाने के लिए आवश्यक है ([Lesson: Classes (The Java™ Tutorials > The Reflection API)](https://docs.oracle.com/javase/tutorial/reflect/class/index.html)).

- **Method**: एक वर्ग की विधि का प्रतिनिधित्व करता है, जो डायनामीक प्रारंभ और जांच के लिए अनुमति देता है। यह विधियाँ जैसे `getName()`, `getParameterTypes()`, और `invoke()` प्रदान करता है, जो प्रोग्राम को रनटाइम पर विधियों को कॉल करने की अनुमति देता है, यहां तक कि निजी विधियों को भी, एक्सेसिबिलिटी सेट करने के बाद ([Guide to Java Reflection | Baeldung](https://www.baeldung.com/java-reflection)).

- **Field**: एक वर्ग की क्षेत्र (field) का प्रतिनिधित्व करता है, जो डायनामीक रूप से मान प्राप्त करने या सेट करने की अनुमति देता है। इसमें विधियाँ जैसे `getName()`, `getType()`, `get()`, और `set()` शामिल हैं, साथ ही निजी क्षेत्रों तक पहुंचने के लिए `setAccessible(true)` का उपयोग ([Java Reflection Example Tutorial | DigitalOcean](https://www.digitalocean.com/community/tutorials/java-reflection-example-tutorial)).

- **Constructor**: एक वर्ग की निर्माणकर्ता (constructor) का प्रतिनिधित्व करता है, जो नए उदाहरणों को डायनामीक रूप से बनाने की अनुमति देता है। इसमें विधियाँ जैसे `getParameterTypes()` और `newInstance()` शामिल हैं, जो विशेष निर्माणकर्ता तर्कों के साथ वस्तुओं को बनाना उपयोगी है ([Reflection in Java - GeeksforGeeks](https://www.geeksforgeeks.org/reflection-in-java/)).

- **AccessibleObject**: `Field`, `Method`, और `Constructor` के लिए एक आधार वर्ग, जो `setAccessible()` विधि प्रदान करता है, जो एक्सेस कंट्रोल चेक्स को ओवरराइड करने के लिए आवश्यक है, जो निजी सदस्यों तक पहुंचने के लिए आवश्यक है, लेकिन सुरक्षा के कारणों से सावधानी से संभालना आवश्यक है ([java.lang.reflect (Java SE 19 & JDK 19 [build 1])](https://download.java.net/java/early_access/panama/docs/api/java.base/java/lang/reflect/package-summary.html)).

#### व्यावहारिक उपयोग और उदाहरण

`java.lang.reflect` का उपयोग करने के लिए, पहला कदम एक `Class` वस्तु प्राप्त करना है, जो आप तीन तरीकों से कर सकते हैं:

1. **`.class` संतृप्ति का उपयोग करें**: सीधे वर्ग का संदर्भ लेना, उदाहरण के लिए, `Class<?> cls1 = String.class`.
2. **`getClass()` विधि का उपयोग करें**: एक उदाहरण पर कॉल करें, उदाहरण के लिए, `String str = "hello"; Class<?> cls2 = str.getClass()`.
3. **`Class.forName()` का उपयोग करें**: नाम के द्वारा डायनामीक रूप से लोड करें, उदाहरण के लिए, `Class<?> cls3 = Class.forName("java.lang.String")`, ध्यान रखें कि यह `ClassNotFoundException` फेंक सकता है ([Trail: The Reflection API (The Java™ Tutorials)](https://docs.oracle.com/javase/tutorial/reflect/index.html)).

एक बार प्राप्त कर लिया, तो `Class` वस्तु विभिन्न वर्ग गुणों की जांच करने की अनुमति देता है:

- `getName()` पूर्ण रूप से योग्य नाम लौटाता है।
- `getSuperclass()` सुपर वर्ग प्राप्त करता है।
- `getInterfaces()` लागू इंटरफेसों की सूची देता है।
- `isInterface()` यह जांचता है कि क्या यह एक इंटरफेस है।
- `isPrimitive()` यह जांचता है कि क्या यह एक प्राइमिटिव प्रकार है।

##### विधियों के साथ काम करना

विधियों को प्राप्त करने के लिए:
- `getMethods()` सभी सार्वजनिक विधियों के लिए, जिसमें विरासत प्राप्त विधियाँ भी शामिल हैं।
- `getDeclaredMethods()` वर्ग में घोषित सभी विधियों के लिए, जिसमें निजी विधियाँ भी शामिल हैं।

एक विधि को प्रारंभ करने के लिए, `Method` वस्तु की `invoke()` विधि का उपयोग करें। उदाहरण के लिए, एक सार्वजनिक विधि को कॉल करने के लिए:
```java
Method method = cls.getMethod("toString");
String result = (String) method.invoke(str);
```
निजी विधियों के लिए, पहले एक्सेसिबिलिटी सेट करें:
```java
Method privateMethod = cls.getDeclaredMethod("privateMethod");
privateMethod.setAccessible(true);
privateMethod.invoke(obj);
```
यह विधि विशेष रूप से डायनामीक विधि प्रारंभ के लिए उपयोगी है, विशेष रूप से फ्रेमवर्कों में जहां विधि नाम रनटाइम पर निर्धारित होते हैं ([Invoking Methods (The Java™ Tutorials > The Reflection API > Members)](https://docs.oracle.com/javase/tutorial/reflect/member/methodInvocation.html)).

##### क्षेत्रों के साथ काम करना

क्षेत्रों तक पहुंचने के लिए:
- `getFields()` सार्वजनिक क्षेत्रों के लिए, जिसमें विरासत प्राप्त क्षेत्र भी शामिल हैं।
- `getDeclaredFields()` सभी घोषित क्षेत्रों के लिए।

एक क्षेत्र मान प्राप्त करने या सेट करने के लिए:
```java
Field field = cls.getDeclaredField("x");
field.setAccessible(true);
int value = (int) field.get(obj);
field.set(obj, 10);
```
यह विशेष रूप से डिबगिंग या लॉगिंग में उपयोगी है, जहां सभी वस्तु क्षेत्रों की जांच की आवश्यकता होती है ([Java Reflection (With Examples)](https://www.programiz.com/java-programming/reflection)).

##### निर्माणकर्ताओं के साथ काम करना

निर्माणकर्ताओं को प्राप्त करने के लिए:
- `getConstructors()` सार्वजनिक निर्माणकर्ताओं के लिए।
- `getDeclaredConstructors()` सभी निर्माणकर्ताओं के लिए।

एक उदाहरण बनाने के लिए:
```java
Constructor<?> constructor = cls.getConstructor(int.class, String.class);
Object obj = constructor.newInstance(10, "hello");
```
यह विशेष रूप से डायनामीक वस्तु निर्माण के लिए आवश्यक है, जैसे कि निर्भरता इंजेक्शन फ्रेमवर्कों में ([Java Reflection - javatpoint](https://www.javatpoint.com/java-reflection)).

#### एक्सेस कंट्रोल और सुरक्षा का संचालन

डिफॉल्ट रूप में, प्रतिबिम्ब (reflection) एक्सेस मॉडिफायर (public, private, protected) का सम्मान करता है। निजी सदस्यों तक पहुंचने के लिए, `setAccessible(true)` का उपयोग `Field`, `Method`, या `Constructor` वस्तु पर करें। हालांकि, यह सुरक्षा को कमजोर कर सकता है, क्योंकि यह एन्कैप्सुलेशन को बाइपास करता है, इसलिए इसे केवल जब आवश्यक हो, और सही अनुमतियों के साथ उपयोग करें, जैसे कि `ReflectPermission` ([java - What is reflection and why is it useful? - Stack Overflow](https://stackoverflow.com/questions/37628/what-is-reflection-and-why-is-it-useful)).

#### उपयोग के मामले और व्यावहारिक अनुप्रयोग

प्रतिबिम्ब (reflection) आम तौर पर उपयोग होता है:
- **सामान्य फ्रेमवर्क**: जैसे कि Spring या Hibernate, जो किसी भी वर्ग के साथ काम करने वाले लाइब्रेरी बनाते हैं।
- **Serialization/Deserialization**: वस्तुओं को और से स्ट्रीम में बदलना, जैसे कि Java के Object Serialization में।
- **टेस्टिंग फ्रेमवर्क**: जैसे कि JUnit, जहां विधियों को डायनामीक रूप से प्रारंभ किया जाता है।
- **टूल विकास**: जैसे कि डिबगर्स, IDEs, और वर्ग ब्राउज़र्स, जो वर्ग संरचनाओं को जांचते हैं।

उदाहरण के लिए, एक सीनारियो में, जहां आपको वर्ग नामों की एक सूची है और आप उदाहरण बनाना चाहते हैं और एक विधि को कॉल करना चाहते हैं:
```java
List<String> classNames = Arrays.asList("com.example.ClassA", "com.example.ClassB");
for (String className : classNames) {
    Class<?> cls = Class.forName(className);
    Object obj = cls.newInstance();
    Method method = cls.getMethod("doSomething");
    method.invoke(obj);
}
```
यह डायनामीक वर्ग लोडिंग और विधि प्रारंभ का एक शक्तिशाली उदाहरण है, जो रनटाइम अनुकूलन के लिए उपयोगी है ([Enhancements to the Java Reflection API](https://docs.oracle.com/javase/8/docs/technotes/guides/reflection/enhancements.html)).

एक अन्य व्यावहारिक उदाहरण एक सामान्य लॉगिंग यंत्र है:
```java
void printObjectFields(Object obj) {
    Class<?> cls = obj.getClass();
    Field[] fields = cls.getDeclaredFields();
    for (Field field : fields) {
        field.setAccessible(true);
        System.out.println(field.getName() + ": " + field.get(obj));
    }
}
```
यह डिबगिंग के लिए उपयोगी है, किसी भी वस्तु के सभी क्षेत्रों को प्रिंट करने के लिए, जो प्रतिबिम्ब (reflection) की उपयोगिता को जांचने के कार्य में दिखाता है ([Reflection in Java - GeeksforGeeks](https://www.geeksforgeeks.org/reflection-in-java/)).

#### संभावित गलतियाँ और सर्वोत्तम प्रथाएँ

हालांकि शक्तिशाली, प्रतिबिम्ब (reflection) में कुछ विचार हैं:

1. **प्रदर्शन**: प्रतिबिम्ब (reflection) ऑपरेशंस, जैसे कि `Method.invoke()` या `Constructor.newInstance()`, आम तौर पर डायनामीक लुकअप और चेक्स के कारण सीधे कॉलों से धीमे होते हैं, जैसा कि Java SE 8 में प्रदर्शन में सुधार में नोट किया गया है ([Enhancements to the Java Reflection API](https://docs.oracle.com/javase/8/docs/technotes/guides/reflection/enhancements.html)).

2. **सुरक्षा**: निजी सदस्यों तक अराजक पहुंच को अनुमति देने से एन्कैप्सुलेशन और सुरक्षा को कमजोर कर सकता है, इसलिए `setAccessible(true)` का सावधानी से उपयोग करें, विशेष रूप से उत्पादन कोड में, और प्रतिबिम्ब (reflection) उपयोग को कम करने के लिए अलग करें ([java - What is reflection and why is it useful? - Stack Overflow](https://stackoverflow.com/questions/37628/what-is-reflection-and-why-is-it-useful)).

3. **प्रकार सुरक्षा**: प्रतिबिम्ब (reflection) आम तौर पर सामान्य `Object` प्रकारों के साथ काम करने का मतलब है, जो `ClassCastException` की संभावना बढ़ाता है, यदि सही से संभाल नहीं किया गया, इसलिए सावधानीपूर्वक कास्टिंग और प्रकार जांच की आवश्यकता होती है ([Java Reflection Example Tutorial | DigitalOcean](https://www.digitalocean.com/community/tutorials/java-reflection-example-tutorial)).

4. **अपवाद संचालन**: कई प्रतिबिम्ब (reflection) विधियाँ अपवादों जैसे `NoSuchMethodException`, `IllegalAccessException`, या `InvocationTargetException` फेंक सकती हैं, जो प्रोग्राम स्थिरता सुनिश्चित करने के लिए सख्त अपवाद संचालन की आवश्यकता होती है ([Trail: The Reflection API (The Java™ Tutorials)](https://docs.oracle.com/javase/tutorial/reflect/index.html)).

सर्वोत्तम प्रथाएँ में शामिल हैं:
- प्रतिबिम्ब (reflection) का केवल जब आवश्यक हो, उपयोग करें, जहां संभव हो, स्थिर प्रकार का उपयोग करें।
- एन्कैप्सुलेशन को बनाए रखने के लिए `setAccessible(true)` का उपयोग कम करें।
- सावधानीपूर्वक कास्टिंग और वलिडेशन के माध्यम से प्रकार सुरक्षा सुनिश्चित करें।
- अपवादों को सावधानी से संभालें ताकि रनटाइम विफलताओं से बचा जा सके।

#### प्रतिबिम्ब (Reflection) विधियों का तुलनात्मक विश्लेषण

वर्ग घटकों तक पहुंचने के विभिन्न विधियों को संगठित करने के लिए, निम्नलिखित तालिका में प्रतिबिम्ब (reflection) ऑपरेशनों का तुलन करें:

| ऑपरेशन                  | सार्वजनिक एक्सेस विधि       | सभी एक्सेस विधि          | टिप्पणियाँ                                      |
|----------------------------|----------------------------|----------------------------|--------------------------------------------|
| विधियों को प्राप्त करें                | `getMethods()`            | `getDeclaredMethods()`     | सार्वजनिक के लिए विरासत प्राप्त, सभी घोषित के लिए सभी |
| क्षेत्रों को प्राप्त करें                 | `getFields()`             | `getDeclaredFields()`      | सार्वजनिक के लिए विरासत प्राप्त, सभी के लिए निजी |
| निर्माणकर्ताओं को प्राप्त करें           | `getConstructors()`       | `getDeclaredConstructors()`| सार्वजनिक के लिए, सभी के लिए निजी          |
| विधि प्रारंभ करें              | `invoke()` के बाद `getMethod()` | `invoke()` के बाद `getDeclaredMethod()` | निजी के लिए `setAccessible(true)` की आवश्यकता होती है |
| क्षेत्र तक पहुंचें               | `get()`/`set()` के बाद `getField()` | `get()`/`set()` के बाद `getDeclaredField()` | निजी के लिए `setAccessible(true)` की आवश्यकता होती है |

यह तालिका सार्वजनिक और सभी एक्सेस विधियों के बीच अंतर को उजागर करता है, जो प्रतिबिम्ब (reflection) की सीमा और सुरक्षा परिणामों को समझने के लिए महत्वपूर्ण है ([java.lang.reflect.Method Class in Java - GeeksforGeeks](https://www.geeksforgeeks.org/java-lang-reflect-method-class-in-java/)).

#### निष्कर्ष

`java.lang.reflect` पैकेज Java में डायनामीक प्रोग्रामिंग के लिए एक आधार है, जो रनटाइम पर वर्ग संरचनाओं को जांचने और संशोधित करने के लिए शक्तिशाली क्षमताएं प्रदान करता है। मुख्य वर्ग, व्यावहारिक उपयोग, और सर्वोत्तम प्रथाओं को समझने के माध्यम से, डेवलपर्स प्रतिबिम्ब (reflection) का उपयोग शक्तिशाली अनुप्रयोगों के लिए कर सकते हैं, जबकि इसके संभावित गलतियों को कम कर सकते हैं। यह व्यापक मार्गदर्शन, जो अधिकारिक स्रोतों पर आधारित है, नए और अनुभवी Java प्रोग्रामरों के लिए एक गहन समझ सुनिश्चित करता है।

**मुख्य सन्दर्भ:**
- [Using Java Reflection introduction and examples](https://www.oracle.com/technical-resources/articles/java/javareflection.html)
- [Guide to Java Reflection with detailed examples](https://www.baeldung.com/java-reflection)
- [Reflection in Java comprehensive tutorial](https://www.geeksforgeeks.org/reflection-in-java/)
- [Java Reflection Example Tutorial for beginners](https://www.digitalocean.com/community/tutorials/java-reflection-example-tutorial)
- [Java Reflection detailed guide with examples](https://www.javatpoint.com/java-reflection)
- [What is reflection and why is it useful in Java](https://stackoverflow.com/questions/37628/what-is-reflection-and-why-is-it-useful)
- [java.lang.reflect.Method Class in Java detailed](https://www.geeksforgeeks.org/java-lang-reflect-method-class-in-java/)
- [Java Reflection with practical examples](https://www.programiz.com/java-programming/reflection)
- [java.lang.reflect package summary Java SE 8](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/package-summary.html)
- [java.lang.reflect package summary Java SE 19](https://download.java.net/java/early_access/panama/docs/api/java.base/java/lang/reflect/package-summary.html)
- [Core Java Reflection official documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/reflection/index.html)
- [Trail The Reflection API Java Tutorials](https://docs.oracle.com/javase/tutorial/reflect/index.html)
- [Trail The Reflection API Java Tutorials detailed](https://docs.oracle.com/javase/tutorial/reflect/)
- [Enhancements to the Java Reflection API](https://docs.oracle.com/javase/8/docs/technotes/guides/reflection/enhancements.html)
- [Lesson Classes The Reflection API Java Tutorials](https://docs.oracle.com/javase/tutorial/reflect/class/index.html)
- [Invoking Methods The Reflection API Java Tutorials](https://docs.oracle.com/javase/tutorial/reflect/member/methodInvocation.html)