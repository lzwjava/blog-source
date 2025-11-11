---
audio: false
generated: true
lang: hi
layout: post
title: जावा में स्काला के संग्रह पुस्तकालय का उपयोग
translated: true
type: note
---

Java में `scala.collection` पैकेज का उपयोग करने के लिए, आप Scala और Java के बीच interoperability का लाभ उठा सकते हैं क्योंकि दोनों भाषाएं JVM बाइटकोड में compile होती हैं। यह Java कोड को Scala classes को call करने की अनुमति देता है, जिसमें `scala.collection` पैकेज की classes भी शामिल हैं, बशर्ते कि Scala library आपके Java project के लिए accessible हो। इसे प्राप्त करने के लिए एक चरण-दर-चरण मार्गदर्शिका नीचे दी गई है, जिसमें स्पष्टीकरण और उदाहरण शामिल हैं।

---

### **चरण 1: अपने Java प्रोजेक्ट में Scala लाइब्रेरी शामिल करें**
चूंकि `scala.collection` पैकेज Scala standard library का हिस्सा है, इसलिए आपको अपने Java प्रोजेक्ट की classpath में Scala library को शामिल करना होगा। यह आपके build tool में Scala library dependency जोड़कर किया जा सकता है:

- **Maven**:
  अपने `pom.xml` में निम्नलिखित जोड़ें:
  ```xml
  <dependency>
      <groupId>org.scala-lang</groupId>
      <artifactId>scala-library</artifactId>
      <version>2.13.12</version> <!-- अपनी आवश्यकताओं से मेल खाने वाले संस्करण का उपयोग करें -->
  </dependency>
  ```

- **Gradle**:
  अपने `build.gradle` में इसे जोड़ें:
  ```gradle
  implementation 'org.scala-lang:scala-library:2.13.12'
  ```

यह सुनिश्चित करता है कि Scala classes, जिनमें `scala.collection` वाली भी शामिल हैं, आपके Java code के लिए उपलब्ध हों।

---

### **चरण 2: Scala Collection Classes को Import करें**
एक बार Scala library आपकी classpath में हो जाने के बाद, आप अपने Java code में `scala.collection` पैकेज से विशिष्ट classes import कर सकते हैं। उदाहरण के लिए, Scala की immutable `List` का उपयोग करने के लिए, आप import करेंगे:

```java
import scala.collection.immutable.List;
```

अन्य सामान्य रूप से उपयोग की जाने वाली collections में शामिल हैं:
- `scala.collection.immutable.Set`
- `scala.collection.immutable.Map`
- `scala.collection.mutable.Buffer`

ध्यान दें कि Scala collections mutable और immutable दोनों variants में आती हैं, Java की collections के विपरीत, जो आमतौर पर mutable होती हैं जब तक कि wrapped न हों (उदा., `Collections.unmodifiableList` के माध्यम से)।

---

### **चरण 3: Java में Scala Collections बनाना**
Scala collections आमतौर पर companion objects का उपयोग करके बनाई जाती हैं, जो factory methods जैसे `apply` प्रदान करते हैं। हालाँकि, चूंकि Java सीधे Scala की syntax का समर्थन नहीं करता है (उदा., `List(1, 2, 3)`), आपको इन methods के साथ स्पष्ट रूप से काम करने की आवश्यकता है। इसके अतिरिक्त, collections जैसे `List` के लिए Scala का `apply` method Java से call किए जाने पर एक `Seq` argument की अपेक्षा करता है, क्योंकि Scala के varargs कैसे compile होते हैं।

Java और Scala collections के बीच सेतु बनाने के लिए, Scala द्वारा प्रदान किए गए conversion utilities का उपयोग करें, जैसे `scala.collection.JavaConverters` (Scala 2.12 और पहले के लिए) या `scala.jdk.CollectionConverters` (Scala 2.13 और बाद के लिए)। यहाँ बताया गया है कि Java `List` से Scala `List` कैसे बनाई जाती है:

#### **उदाहरण: एक Scala List बनाना**
```java
import scala.collection.immutable.List;
import scala.collection.Seq;
import scala.jdk.CollectionConverters;
import java.util.Arrays;

public class ScalaCollectionExample {
    public static void main(String[] args) {
        // एक Java List बनाएं
        java.util.List<Integer> javaList = Arrays.asList(1, 2, 3);

        // Java List को Scala Seq में बदलें
        Seq<Integer> scalaSeq = CollectionConverters.asScala(javaList);

        // Companion object का उपयोग करके एक Scala List बनाएं
        List<Integer> scalaList = List$.MODULE$.apply(scalaSeq);

        // Scala List को प्रिंट करें
        System.out.println(scalaList); // Output: List(1, 2, 3)
    }
}
```

- **`CollectionConverters.asScala`**: एक Java `List` को Scala `Seq` (विशेष रूप से Scala 2.13 में एक `mutable.Buffer`, जो `Seq` का एक subtype है) में बदलता है।
- **`List$.MODULE$`**: Scala में `List` companion object के singleton instance तक पहुंचता है, जिससे आप इसके `apply` method को call कर सकते हैं।
- **`apply(scalaSeq)`**: `Seq` से एक नई immutable Scala `List` बनाता है।

---

### **चरण 4: Scala Collections का उपयोग करना**
एक बार आपके पास Java में एक Scala collection हो जाने के बाद, आप इसकी methods का उपयोग कर सकते हैं। हालाँकि, Scala और Java के बीच अंतरों से अवगत रहें:
- **Immutability**: कई Scala collections (उदा., `scala.collection.immutable.List`) immutable हैं, जिसका अर्थ है कि methods मूल collection को संशोधित करने के बजाय नई collections लौटाते हैं।
- **Type Erasure**: Scala और Java दोनों type erasure का उपयोग करते हैं, इसलिए elements प्राप्त करते समय आपको परिणामों को cast करने की आवश्यकता हो सकती है।
- **Functional Methods**: Scala collections functional operations जैसे `map`, `filter`, आदि का समर्थन करते हैं, जिनका आप Java 8+ lambdas के साथ उपयोग कर सकते हैं।

#### **उदाहरण: Elements तक पहुंचना**
```java
// पहला element प्राप्त करें
Integer head = (Integer) scalaList.head();
System.out.println("Head: " + head); // Output: Head: 1

// tail प्राप्त करें (head को छोड़कर सब कुछ)
List<Integer> tail = scalaList.tail();
System.out.println("Tail: " + tail); // Output: Tail: List(2, 3)
```

#### **उदाहरण: एक Scala List पर Mapping करना**
प्रत्येक element को दोगुना करने के लिए एक lambda का उपयोग करना:
```java
import scala.Function1;

Function1<Integer, Integer> doubler = x -> x * 2;
List<Integer> doubledList = scalaList.map(doubler);
System.out.println("Doubled: " + doubledList); // Output: Doubled: List(2, 4, 6)
```

यहाँ, `Function1` एक Scala interface है जो एक argument वाले function का प्रतिनिधित्व करता है, जो Java की lambda syntax के साथ संरेखित होता है।

---

### **मुख्य विचारणीय बिंदु**
- **Type Safety**: Scala collections parameterized हैं, लेकिन method return types type erasure के कारण Java में `Object` के रूप में दिखाई दे सकते हैं। आवश्यकतानुसार cast करें (उदा., `(Integer) scalaList.head()`)।
- **Performance**: Java-Scala सीमा पार करने में कुछ overhead आती है, हालाँकि यह आमतौर पर मामूली होती है।
- **Paradigm Shift**: Scala collections immutability और functional programming पर जोर देते हैं, जो Java की imperative style से भिन्न हो सकता है। उदाहरण के लिए, आप एक immutable `List` में "add" नहीं कर सकते—आप इसके बजाय एक नई बनाते हैं (उदा., append करने के लिए `:+` का उपयोग करके, जो एक नई `List` लौटाता है)।
- **Version Compatibility**: सुनिश्चित करें कि Scala library version आपकी आवश्यकताओं से मेल खाती हो। Scala 2.13+ के लिए, `scala.jdk.CollectionConverters` का उपयोग करें; 2.12 या पहले के लिए, `scala.collection.JavaConverters` का उपयोग करें।

---

### **सारांश**
आप Java में `scala.collection` पैकेज का उपयोग इस प्रकार कर सकते हैं:
1. अपने प्रोजेक्ट की classpath में Scala library जोड़कर (उदा., Maven या Gradle के माध्यम से)।
2. वांछित Scala collection classes को import करके (उदा., `scala.collection.immutable.List`)।
3. Companion objects का उपयोग करके Scala collections बनाकर (उदा., `List$.MODULE$.apply`) और Java collections को `CollectionConverters` के साथ Scala `Seq` में बदलकर।
4. Collections को Scala methods के साथ manipulate करके, आवश्यकतानुसार casts और lambdas का उपयोग करते हुए।

यह दृष्टिकोण आपको Java के ecosystem के भीतर काम करते हुए, Java में Scala की शक्तिशाली collection library, जैसे इसकी immutable data structures या functional operations का लाभ उठाने की अनुमति देता है।