---
audio: false
generated: true
lang: hi
layout: post
title: कमांड लाइन ऑप्शन्स को जावा में पार्स करना
translated: true
---

JOptSimple एक Java लाइब्रेरी है जो अपने एप्लिकेशन में कमांड-लाइन ऑप्शन की पार्सिंग को सरल बनाने के लिए डिज़ाइन किया गया है। यह आपको फ्लैग्स (जैसे, `-v` के लिए वर्बोस मोड) और आर्ग्यूमेंट्स के साथ ऑप्शन (जैसे, `--file input.txt`) को एक फ्लेक्सिबल और इंटुइटिव तरीके से परिभाषित और प्रोसेस करने की अनुमति देता है। नीचे एक स्टेप-बाय-स्टेप गाइड है कि कैसे JOptSimple को प्रभावी रूप से उपयोग किया जा सकता है।

---

### **स्टेप 1: JOptSimple को अपने प्रोजेक्ट में जोड़ें**
JOptSimple का उपयोग करने के लिए, आपको पहले इसे अपने Java प्रोजेक्ट में शामिल करना होगा। अगर आप Maven का उपयोग कर रहे हैं, तो अपने `pom.xml` फ़ाइल में निम्नलिखित डिपेंडेंसी जोड़ें:

```xml
<dependency>
    <groupId>net.sf.jopt-simple</groupId>
    <artifactId>jopt-simple</artifactId>
    <version>5.0.4</version>
</dependency>
```

Maven Central पर सबसे नया संस्करण की जांच करें, क्योंकि `5.0.4` सबसे नया हो सकता है। अन्य बिल्ड टूल्स जैसे Gradle के लिए, आप डिपेंडेंसी को अनुकूलित कर सकते हैं (जैसे, `implementation 'net.sf.jopt-simple:jopt-simple:5.0.4'`).

---

### **स्टेप 2: एक OptionParser बनाएं**
JOptSimple का कोर `OptionParser` क्लास है, जिसे आप कमांड-लाइन ऑप्शन को परिभाषित और पार्स करने के लिए उपयोग करते हैं। अपने `main` मेथड में इसका एक इंस्टेंस बनाएं:

```java
import joptsimple.OptionParser;
import joptsimple.OptionSet;

public class MyApp {
    public static void main(String[] args) {
        OptionParser parser = new OptionParser();
        // यहाँ ऑप्शन परिभाषित करें (स्टेप 3 देखें)
    }
}
```

---

### **स्टेप 3: कमांड-लाइन ऑप्शन परिभाषित करें**
आप `accepts` या `acceptsAll` मेथड का उपयोग करके ऑप्शन परिभाषित कर सकते हैं। ऑप्शन फ्लैग्स (कोई आर्ग्यूमेंट नहीं) या आर्ग्यूमेंट्स की आवश्यकता वाले ऑप्शन (जैसे, फ़ाइल नाम या संख्या) हो सकते हैं। यहाँ उन्हें सेट करने का तरीका है:

- **फ्लैग्स**: एकल ऑप्शन नाम के लिए `accepts` का उपयोग करें या `acceptsAll` को स्पेसिफाई करने के लिए (जैसे, `-v` और `--verbose`):
  ```java
  parser.acceptsAll(Arrays.asList("v", "verbose"), "वर्बोस मोड को एनेबल करें");
  ```

- **आर्ग्यूमेंट्स के साथ ऑप्शन**: `withRequiredArg()` का उपयोग करके एक ऑप्शन को एक मान की आवश्यकता होती है, और `ofType()` के साथ ऑप्शनल रूप से इसका प्रकार स्पेसिफाई करें:
  ```java
  parser.acceptsAll(Arrays.asList("f", "file"), "इनपुट फ़ाइल स्पेसिफाई करें").withRequiredArg();
  parser.acceptsAll(Arrays.asList("c", "count"), "गिनती स्पेसिफाई करें").withRequiredArg().ofType(Integer.class).defaultsTo(0);
  ```

  - `defaultsTo(0)` एक डिफ़ॉल्ट मान (जैसे, `0`) सेट करता है अगर ऑप्शन प्रदान नहीं किया गया है।
  - `ofType(Integer.class)` सुनिश्चित करता है कि आर्ग्यूमेंट एक इंटीजर के रूप में पार्स किया जाता है।

- **हेल्प ऑप्शन**: उपयोग सूचना दिखाने के लिए एक हेल्प फ्लैग (जैसे, `-h` या `--help`) जोड़ें:
  ```java
  parser.acceptsAll(Arrays.asList("h", "help"), "इस हेल्प संदेश को दिखाएं");
  ```

---

### **स्टेप 4: कमांड-लाइन आर्ग्यूमेंट्स को पार्स करें**
`args` एरे को पार्सर में पास करें ताकि कमांड-लाइन इनपुट को प्रोसेस किया जा सके। यह एक `OptionSet` ऑब्जेक्ट लौटाता है जिसमें पार्स किए गए ऑप्शन शामिल हैं:

```java
OptionSet options = parser.parse(args);
```

इसको एक `try-catch` ब्लॉक में लपेटें ताकि पार्सिंग त्रुटियों (जैसे, अमान्य ऑप्शन या गुम आर्ग्यूमेंट्स) को हैंडल किया जा सके:

```java
try {
    OptionSet options = parser.parse(args);
    // ऑप्शन प्रोसेस करें (स्टेप 5 देखें)
} catch (Exception e) {
    System.err.println("त्रुटि: " + e.getMessage());
    try {
        parser.printHelpOn(System.err);
    } catch (IOException ex) {
        ex.printStackTrace();
    }
    System.exit(1);
}
```

---

### **स्टेप 5: पार्स किए गए ऑप्शन तक पहुंचें**
`OptionSet` का उपयोग करें ताकि फ्लैग्स, ऑप्शन मान, और नॉन-ऑप्शन आर्ग्यूमेंट्स की जांच की जा सके:

- **फ्लैग्स की जांच करें**: `has()` का उपयोग करें ताकि एक फ्लैग मौजूद है:
  ```java
  boolean verbose = options.has("v");
  if (verbose) {
      System.out.println("वर्बोस मोड एनेबल किया गया");
  }
  ```

- **ऑप्शन मान प्राप्त करें**: `valueOf()` का उपयोग करें ताकि एक ऑप्शन का आर्ग्यूमेंट प्राप्त किया जा सके, आवश्यकता के अनुसार इसे सही प्रकार में कास्ट करें:
  ```java
  String fileName = (String) options.valueOf("f"); // अगर स्पेसिफाई नहीं किया गया तो नल लौटता है
  int count = (Integer) options.valueOf("c");     // 0 लौटता है क्योंकि defaultsTo(0)
  ```

  अगर आपने `ofType()` और `defaultsTo()` स्पेसिफाई किया है, तो `valueOf()` टाइप्ड मान या डिफ़ॉल्ट लौटाता है।

- **नॉन-ऑप्शन आर्ग्यूमेंट्स**: ऑप्शन से जुड़े नहीं होने वाले आर्ग्यूमेंट्स (जैसे, फ़ाइलों की एक सूची) को `nonOptionArguments()` के साथ प्राप्त करें:
  ```java
  List<String> files = options.nonOptionArguments();
  System.out.println("फ़ाइलें: " + files);
  ```

- **हेल्प हैंडल करें**: अगर हेल्प ऑप्शन मौजूद है, तो उपयोग सूचना प्रिंट करें:
  ```java
  if (options.has("h")) {
      parser.printHelpOn(System.out);
      System.exit(0);
  }
  ```

---

### **उदाहरण: सब कुछ एक साथ**
एक वर्बोस फ्लैग, एक गिनती ऑप्शन, और फ़ाइलों की एक सूची स्वीकार करने वाले एक पूर्ण प्रोग्राम का उदाहरण:

```java
import joptsimple.OptionParser;
import joptsimple.OptionSet;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

public class MyApp {
    public static void main(String[] args) {
        OptionParser parser = new OptionParser();
        parser.acceptsAll(Arrays.asList("v", "verbose"), "वर्बोस मोड को एनेबल करें");
        parser.acceptsAll(Arrays.asList("c", "count"), "गिनती स्पेसिफाई करें")
              .withRequiredArg()
              .ofType(Integer.class)
              .defaultsTo(0);
        parser.acceptsAll(Arrays.asList("h", "help"), "इस हेल्प संदेश को दिखाएं");

        try {
            OptionSet options = parser.parse(args);

            if (options.has("h")) {
                parser.printHelpOn(System.out);
                System.exit(0);
            }

            boolean verbose = options.has("v");
            int count = (Integer) options.valueOf("c");
            List<String> files = options.nonOptionArguments();

            if (verbose) {
                System.out.println("वर्बोस मोड एनेबल किया गया");
            }
            System.out.println("गिनती: " + count);
            System.out.println("फ़ाइलें: " + files);

        } catch (Exception e) {
            System.err.println("त्रुटि: " + e.getMessage());
            try {
                parser.printHelpOn(System.err);
            } catch (IOException ex) {
                ex.printStackTrace();
            }
            System.exit(1);
        }
    }
}
```

इसको चलाएं: `java MyApp -v -c 5 file1 file2`, और यह निम्नलिखित को आउटपुट करता है:
```
वर्बोस मोड एनेबल किया गया
गिनती: 5
फ़ाइलें: [file1, file2]
```

`-h` के साथ चलाएं, और यह सभी परिभाषित ऑप्शन के साथ उपयोग सूचना दिखाता है।

---

### **अधिक विशेषताएं**
- **बहुत से मान**: एक ऑप्शन को कई बार दिखाई देने की अनुमति दें (जैसे, `-I dir1 -I dir2`):
  ```java
  parser.accepts("I").withRequiredArg().ofType(String.class);
  List<String> includes = options.valuesOf("I"); // एक सूची लौटाता है
  ```

- **ऑप्शनल आर्ग्यूमेंट्स**: अगर एक आर्ग्यूमेंट अनिवार्य नहीं है, तो `withOptionalArg()` का उपयोग करें:
  ```java
  parser.accepts("o").withOptionalArg().ofType(String.class);
  ```

- **त्रुटि हैंडलिंग**: JOptSimple पार्सिंग त्रुटियों के लिए एक `OptionException` फेंकता है, जिसे आप उपयोगकर्ता-फ्रेंडली फीडबैक प्रदान करने के लिए कैच कर सकते हैं।

---

### **सारांश**
JOptSimple Java में कमांड-लाइन ऑप्शन को हैंडल करने को आसान बनाता है। आप:
1. लाइब्रेरी को अपने प्रोजेक्ट में जोड़ें।
2. एक `OptionParser` बनाएं और ऑप्शन (फ्लैग्स, आर्ग्यूमेंट्स, डिफ़ॉल्ट्स) परिभाषित करें।
3. `args` एरे को एक `OptionSet` में पार्स करें।
4. `OptionSet` का उपयोग करें ताकि फ्लैग्स, मान, और नॉन-ऑप्शन आर्ग्यूमेंट्स तक पहुंचा जा सके।
5. त्रुटियों को हैंडल करें और आवश्यकता के अनुसार हेल्प प्रदान करें।

इस आधार के साथ, आप अपने एप्लिकेशन की आवश्यकताओं के अनुसार टेलर-मेड कमांड-लाइन इंटरफेस बनाएं!