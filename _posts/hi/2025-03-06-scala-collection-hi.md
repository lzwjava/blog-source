---
audio: false
generated: true
lang: hi
layout: post
title: Scala के Collection Library का उपयोग Java में
translated: true
---

`scala.collection` पैकेज को जावा में उपयोग करने के लिए, आप Scala और Java के बीच के इंटरऑपरेबिलिटी का लाभ उठा सकते हैं क्योंकि दोनों भाषाएं JVM बाइटकोड में कॉम्पाइल होती हैं। यह Java कोड को Scala क्लासेज को कॉल करने की अनुमति देता है, जिसमें `scala.collection` पैकेज में भी शामिल हैं, यदि Scala लाइब्रेरी आपकी Java प्रोजेक्ट के लिए उपलब्ध है। नीचे दिए गए चरणों का पालन करके यह प्राप्त करने के लिए एक चरण-दर-चरण गाइड है, जिसमें व्याख्याएं और उदाहरण शामिल हैं।

---

### **चरण 1: Scala लाइब्रेरी को आपकी Java प्रोजेक्ट में शामिल करें**
`scala.collection` पैकेज Scala स्टैंडर्ड लाइब्रेरी का हिस्सा है, इसलिए आपको Scala लाइब्रेरी को आपकी Java प्रोजेक्ट के क्लासपाथ में शामिल करना होगा। यह आपकी बिल्ड टूल में Scala लाइब्रेरी डिपेंडेंसी को जोड़कर किया जा सकता है:

- **Maven**:
  `pom.xml` में निम्नलिखित को जोड़ें:
  ```xml
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-library</artifactId>
      <version>2.13.12</version> <!-- अपने आवश्यकताओं के अनुसार संस्करण का उपयोग करें -->
  </dependency>
  ```

- **Gradle**:
  `build.gradle` में निम्नलिखित को जोड़ें:
  ```gradle
  implementation 'org.scala-lang:scala-library:2.13.12'
  ```

यह सुनिश्चित करता है कि Scala क्लासेज, जिसमें `scala.collection` भी शामिल हैं, आपके Java कोड के लिए उपलब्ध हैं।

---

### **चरण 2: Scala Collection क्लासेज को इम्पोर्ट करें**
एक बार Scala लाइब्रेरी आपके क्लासपाथ में हो जाती है, तो आप अपने Java कोड में `scala.collection` पैकेज से विशिष्ट क्लासेज को इम्पोर्ट कर सकते हैं। उदाहरण के लिए, Scala के अचल `List` का उपयोग करने के लिए, आप इम्पोर्ट करेंगे:

```java
import scala.collection.immutable.List;
```

अन्य आमतौर पर उपयोग किए जाने वाले संग्रहों में शामिल हैं:
- `scala.collection.immutable.Set`
- `scala.collection.immutable.Map`
- `scala.collection.mutable.Buffer`

ध्यान रखें कि Scala संग्रहों में दोनों अचल और परिवर्तनीय संस्करण होते हैं, जबकि Java के संग्रह आमतौर पर परिवर्तनीय होते हैं, जब तक कि वे किसी अन्य द्वारा लपेटे नहीं होते (उदाहरण के लिए, `Collections.unmodifiableList` द्वारा).

---

### **चरण 3: Java में Scala संग्रह बनाएं**
Scala संग्रह आमतौर पर सहयोगी वस्तुओं का उपयोग करके बनाए जाते हैं, जो जैसे `apply` जैसी फैक्ट्री विधियाँ प्रदान करते हैं। हालांकि, Java Scala के सिंटैक्स का समर्थन नहीं करता (उदाहरण के लिए, `List(1, 2, 3)`), इसलिए आपको इन विधियों के साथ स्पष्ट रूप से काम करना होगा। इसके अलावा, Scala के `apply` विधि जैसे संग्रहों के लिए `List` को Java से कॉल करने पर एक `Seq` के रूप में एक अपेक्षित है, क्योंकि Scala के वरार्ग्स कैसे कॉम्पाइल होते हैं।

Java और Scala संग्रहों को जोड़ने के लिए, Scala द्वारा प्रदान की गई परिवर्तन यूटीलिटीज का उपयोग करें, जैसे `scala.collection.JavaConverters` (Scala 2.12 और उससे पहले के लिए) या `scala.jdk.CollectionConverters` (Scala 2.13 और बाद के लिए)। यहाँ एक Java `List` से Scala `List` बनाना कैसे है:

#### **उदाहरण: Scala List बनाएं**
```java
import scala.collection.immutable.List;
import scala.collection.Seq;
import scala.jdk.CollectionConverters;
import java.util.Arrays;

public class ScalaCollectionExample {
    public static void main(String[] args) {
        // Java List बनाएं
        java.util.List<Integer> javaList = Arrays.asList(1, 2, 3);

        // Java List को Scala Seq में परिवर्तित करें
        Seq<Integer> scalaSeq = CollectionConverters.asScala(javaList);

        // सहयोगी वस्तु का उपयोग करके Scala List बनाएं
        List<Integer> scalaList = List$.MODULE$.apply(scalaSeq);

        // Scala List को प्रिंट करें
        System.out.println(scalaList); // Output: List(1, 2, 3)
    }
}
```

- **`CollectionConverters.asScala`**: एक Java `List` को Scala `Seq` में परिवर्तित करता है (विशेष रूप से Scala 2.13 में एक `mutable.Buffer`, जो `Seq` का एक उपवर्ग है).
- **`List$.MODULE$`**: Scala में `List` सहयोगी वस्तु का एकल उदाहरण को एक्सेस करता है, जिससे आप इसके `apply` विधि को कॉल कर सकते हैं।
- **`apply(scalaSeq)`**: एक नया अचल Scala `List` `Seq` से बनाता है।

---

### **चरण 4: Scala संग्रह का उपयोग करें**
एक बार आपकी Java में एक Scala संग्रह है, तो आप इसके विधियों का उपयोग कर सकते हैं। हालांकि, Scala और Java के बीच के अंतरों के बारे में जानकारी रखें:
- **अचलता**: कई Scala संग्रह (उदाहरण के लिए, `scala.collection.immutable.List`) अचल होते हैं, अर्थात विधियाँ नए संग्रहों को लौटाती हैं, बजाय मूल को परिवर्तित करने के।
- **टाइप एरेजर**: दोनों Scala और Java टाइप एरेजर का उपयोग करते हैं, इसलिए आप तत्वों को प्राप्त करने पर परिणामों को कास्ट करने की आवश्यकता हो सकती है।
- **फंक्शनल विधियाँ**: Scala संग्रह `map`, `filter` जैसे फंक्शनल ऑपरेशन का समर्थन करते हैं, जिन्हें आप Java 8+ लैम्ब्डा के साथ उपयोग कर सकते हैं।

#### **उदाहरण: तत्वों तक पहुंचें**
```java
// पहला तत्व प्राप्त करें
Integer head = (Integer) scalaList.head();
System.out.println("Head: " + head); // Output: Head: 1

// शेष (सिर के अलावा सब कुछ)
List<Integer> tail = scalaList.tail();
System.out.println("Tail: " + tail); // Output: Tail: List(2, 3)
```

#### **उदाहरण: Scala List पर मैप करें**
एक लैम्ब्डा का उपयोग करके प्रत्येक तत्व को दुगना करें:
```java
import scala.Function1;

Function1<Integer, Integer> doubler = x -> x * 2;
List<Integer> doubledList = scalaList.map(doubler);
System.out.println("Doubled: " + doubledList); // Output: Doubled: List(2, 4, 6)
```

यहाँ, `Function1` एक Scala इंटरफेस है जो एक तर्क के साथ एक फंक्शन को दर्शाता है, जो Java के लैम्ब्डा सिंटैक्स के साथ मेल खाता है।

---

### **मुख्य विचार**
- **टाइप सुरक्षा**: Scala संग्रह टाइप-परामिटराइज्ड होते हैं, लेकिन विधि लौटने वाले टाइप टाइप एरेजर के कारण Java में `Object` के रूप में दिखाई देते हैं। आवश्यकता के अनुसार कास्ट करें (उदाहरण के लिए, `(Integer) scalaList.head()`).
- **प्रदर्शन**: Java-Scala सीमा को पार करने में कुछ ओवरहेड शामिल है, हालांकि यह आमतौर पर अल्प है।
- **परदिग्म परिवर्तन**: Scala संग्रह अचलता और फंक्शनल प्रोग्रामिंग पर जोर देते हैं, जो Java के इम्पेरेटिव शैली से अलग हो सकते हैं। उदाहरण के लिए, आप एक अचल `List` में "जोड़" नहीं सकते—आप एक नया बनाते हैं (उदाहरण के लिए, `:+` का उपयोग करके जोड़ने के लिए, जो एक नया `List` लौटाता है).
- **वर्सन संगतता**: सुनिश्चित करें कि Scala लाइब्रेरी संस्करण आपके आवश्यकताओं के साथ मेल खाता है। Scala 2.13+ के लिए `scala.jdk.CollectionConverters` का उपयोग करें; 2.12 या उससे पहले के लिए `scala.collection.JavaConverters` का उपयोग करें।

---

### **सारांश**
आप `scala.collection` पैकेज को Java में उपयोग कर सकते हैं:
1. Scala लाइब्रेरी को आपकी प्रोजेक्ट के क्लासपाथ में जोड़ें (उदाहरण के लिए, Maven या Gradle के माध्यम से).
2. इच्छित Scala संग्रह क्लासेज को इम्पोर्ट करें (उदाहरण के लिए, `scala.collection.immutable.List`).
3. सहयोगी वस्तुओं का उपयोग करके Scala संग्रह बनाएं (उदाहरण के लिए, `List$.MODULE$.apply`) और Java संग्रहों को Scala `Seq` में परिवर्तित करें `CollectionConverters` के साथ.
4. संग्रहों को Scala विधियों के साथ संचालित करें, आवश्यकता के अनुसार कास्ट और लैम्ब्डा का उपयोग करें।

यह आपकी Java के भीतर काम करते हुए Scala के शक्तिशाली संग्रह लाइब्रेरी का लाभ उठाने की अनुमति देता है, जैसे कि उसके अचल डेटा संरचनाएं या फंक्शनल ऑपरेशन।