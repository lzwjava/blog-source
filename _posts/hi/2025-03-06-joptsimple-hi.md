---
audio: false
generated: true
lang: hi
layout: post
title: जावा में कमांड-लाइन विकल्पों का पार्सिंग
translated: true
type: note
---

JOptSimple एक Java लाइब्रेरी है जो आपके एप्लिकेशन में कमांड-लाइन विकल्पों के पार्सिंग को सरल बनाने के लिए डिज़ाइन की गई है। यह आपको फ्लैग्स (जैसे, वर्बोज़ मोड के लिए `-v`) और आर्ग्युमेंट्स वाले विकल्पों (जैसे, `--file input.txt`) को लचीले और सहज तरीके से परिभाषित करने और प्रोसेस करने की अनुमति देती है। नीचे JOptSimple का प्रभावी ढंग से उपयोग करने के तरीके के बारे में एक चरण-दर-चरण मार्गदर्शिका दी गई है।

---

### **चरण 1: अपने प्रोजेक्ट में JOptSimple जोड़ें**
JOptSimple का उपयोग करने के लिए, आपको सबसे पहले इसे अपने Java प्रोजेक्ट में शामिल करना होगा। यदि आप Maven का उपयोग कर रहे हैं, तो अपनी `pom.xml` फ़ाइल में निम्नलिखित डिपेंडेंसी जोड़ें:

```xml
<dependency>
    <groupId>net.sf.jopt-simple</groupId>
    <artifactId>jopt-simple</artifactId>
    <version>5.0.4</version>
</dependency>
```

Maven Central पर नवीनतम संस्करण की जांच करना सुनिश्चित करें, क्योंकि `5.0.4` सबसे वर्तमान संस्करण नहीं हो सकता है। Gradle जैसे अन्य बिल्ड टूल्स के लिए, आप डिपेंडेंसी को तदनुसार अनुकूलित कर सकते हैं (उदाहरण के लिए, `implementation 'net.sf.jopt-simple:jopt-simple:5.0.4'`)।

---

### **चरण 2: एक OptionParser बनाएँ**
JOptSimple का मूल `OptionParser` क्लास है, जिसका उपयोग आप कमांड-लाइन विकल्पों को परिभाषित करने और पार्स करने के लिए करते हैं। अपने `main` मेथड में इसका एक इंस्टेंस बनाकर शुरुआत करें:

```java
import joptsimple.OptionParser;
import joptsimple.OptionSet;

public class MyApp {
    public static void main(String[] args) {
        OptionParser parser = new OptionParser();
        // विकल्पों को यहाँ परिभाषित करें (चरण 3 देखें)
    }
}
```

---

### **चरण 3: कमांड-लाइन विकल्प परिभाषित करें**
आप `accepts` या `acceptsAll` मेथड्स का उपयोग करके विकल्पों को परिभाषित कर सकते हैं। विकल्प फ्लैग्स (बिना आर्ग्युमेंट के) या ऐसे विकल्प हो सकते हैं जिनके लिए आर्ग्युमेंट की आवश्यकता होती है (जैसे, एक फ़ाइल नाम या एक संख्या)। उन्हें सेट अप करने का तरीका यहाँ बताया गया है:

- **फ्लैग्स**: एकल विकल्प नाम के लिए `accepts` का उपयोग करें या उपनाम निर्दिष्ट करने के लिए `acceptsAll` (जैसे, `-v` और `--verbose`):
  ```java
  parser.acceptsAll(Arrays.asList("v", "verbose"), "वर्बोज़ मोड सक्षम करें");
  ```

- **आर्ग्युमेंट्स वाले विकल्प**: यह इंगित करने के लिए कि एक विकल्प को एक मान की आवश्यकता है, `withRequiredArg()` का उपयोग करें, और वैकल्पिक रूप से `ofType()` के साथ इसके प्रकार को निर्दिष्ट करें:
  ```java
  parser.acceptsAll(Arrays.asList("f", "file"), "इनपुट फ़ाइल निर्दिष्ट करें").withRequiredArg();
  parser.acceptsAll(Arrays.asList("c", "count"), "काउंट निर्दिष्ट करें").withRequiredArg().ofType(Integer.class).defaultsTo(0);
  ```

  - `defaultsTo(0)` एक डिफ़ॉल्ट मान सेट करता है (जैसे, `0`) यदि विकल्प प्रदान नहीं किया गया है।
  - `ofType(Integer.class)` सुनिश्चित करता है कि आर्ग्युमेंट को एक पूर्णांक के रूप में पार्स किया जाए।

- **हेल्प विकल्प**: उपयोग जानकारी प्रदर्शित करने के लिए एक हेल्प फ्लैग जोड़ें (जैसे, `-h` या `--help`):
  ```java
  parser.acceptsAll(Arrays.asList("h", "help"), "यह सहायता संदेश दिखाएँ");
  ```

---

### **चरण 4: कमांड-लाइन आर्ग्युमेंट्स को पार्स करें**
कमांड-लाइन इनपुट को प्रोसेस करने के लिए अपने `main` मेथड से `args` ऐरे को पार्सर को पास करें। यह एक `OptionSet` ऑब्जेक्ट लौटाता है जिसमें पार्स किए गए विकल्प होते हैं:

```java
OptionSet options = parser.parse(args);
```

पार्सिंग एरर (जैसे, अमान्य विकल्प या लापता आर्ग्युमेंट) को हैंडल करने के लिए इसे एक `try-catch` ब्लॉक में लपेटें:

```java
try {
    OptionSet options = parser.parse(args);
    // विकल्पों को प्रोसेस करें (चरण 5 देखें)
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

### **चरण 5: पार्स किए गए विकल्पों तक पहुँचें**
फ्लैग्स की जांच करने, विकल्प मान प्राप्त करने और गैर-विकल्प आर्ग्युमेंट प्राप्त करने के लिए `OptionSet` का उपयोग करें:

- **फ्लैग्स की जांच करें**: यह देखने के लिए कि कोई फ्लैग मौजूद है या नहीं, `has()` का उपयोग करें:
  ```java
  boolean verbose = options.has("v");
  if (verbose) {
      System.out.println("वर्बोज़ मोड सक्षम");
  }
  ```

- **विकल्प मान प्राप्त करें**: किसी विकल्प के आर्ग्युमेंट को पुनः प्राप्त करने के लिए `valueOf()` का उपयोग करें, आवश्यकता पड़ने पर इसे उचित प्रकार में कास्ट करें:
  ```java
  String fileName = (String) options.valueOf("f"); // निर्दिष्ट न होने पर null लौटाता है
  int count = (Integer) options.valueOf("c");     // defaultsTo(0) के कारण 0 लौटाता है
  ```

  यदि आपने `ofType()` और `defaultsTo()` निर्दिष्ट किया है, तो `valueOf()` टाइप किया गया मान या डिफ़ॉल्ट लौटाता है।

- **गैर-विकल्प आर्ग्युमेंट**: विकल्पों से न जुड़े आर्ग्युमेंट प्राप्त करें (जैसे, फ़ाइलों की एक सूची) `nonOptionArguments()` के साथ:
  ```java
  List<String> files = options.nonOptionArguments();
  System.out.println("फ़ाइलें: " + files);
  ```

- **हेल्प को हैंडल करें**: यदि हेल्प विकल्प मौजूद है तो उपयोग जानकारी प्रिंट करें:
  ```java
  if (options.has("h")) {
      parser.printHelpOn(System.out);
      System.exit(0);
  }
  ```

---

### **उदाहरण: सभी को एक साथ रखना**
यहाँ एक प्रोग्राम का पूर्ण उदाहरण दिया गया है जो एक वर्बोज़ फ्लैग, एक काउंट विकल्प और फ़ाइलों की एक सूची स्वीकार करता है:

```java
import joptsimple.OptionParser;
import joptsimple.OptionSet;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

public class MyApp {
    public static void main(String[] args) {
        OptionParser parser = new OptionParser();
        parser.acceptsAll(Arrays.asList("v", "verbose"), "वर्बोज़ मोड सक्षम करें");
        parser.acceptsAll(Arrays.asList("c", "count"), "काउंट निर्दिष्ट करें")
              .withRequiredArg()
              .ofType(Integer.class)
              .defaultsTo(0);
        parser.acceptsAll(Arrays.asList("h", "help"), "यह सहायता संदेश दिखाएँ");

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
                System.out.println("वर्बोज़ मोड सक्षम");
            }
            System.out.println("काउंट: " + count);
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

इसे इसके साथ चलाएँ: `java MyApp -v -c 5 file1 file2`, और यह आउटपुट देगा:
```
वर्बोज़ मोड सक्षम
काउंट: 5
फ़ाइलें: [file1, file2]
```

इसे `-h` के साथ चलाएँ, और यह सभी परिभाषित विकल्पों के साथ उपयोग संदेश प्रदर्शित करेगा।

---

### **अतिरिक्त सुविधाएँ**
- **एकाधिक मान**: किसी विकल्प को कई बार दिखाई देने की अनुमति दें (जैसे, `-I dir1 -I dir2`):
  ```java
  parser.accepts("I").withRequiredArg().ofType(String.class);
  List<String> includes = options.valuesOf("I"); // एक सूची लौटाता है
  ```

- **वैकल्पिक आर्ग्युमेंट**: यदि कोई आर्ग्युमेंट अनिवार्य नहीं है तो `withRequiredArg()` के बजाय `withOptionalArg()` का उपयोग करें:
  ```java
  parser.accepts("o").withOptionalArg().ofType(String.class);
  ```

- **त्रुटि हैंडलिंग**: JOptSimple पार्सिंग एरर के लिए एक `OptionException` थ्रो करता है, जिसे आप उपयोगकर्ता-अनुकूल फीडबैक प्रदान करने के लिए कैच कर सकते हैं।

---

### **सारांश**
JOptSimple Java में कमांड-लाइन विकल्पों को हैंडल करना आसान बनाती है। आप:
1. लाइब्रेरी को अपने प्रोजेक्ट में जोड़ें।
2. एक `OptionParser` बनाएँ और विकल्पों (फ्लैग्स, आर्ग्युमेंट्स, डिफ़ॉल्ट) को परिभाषित करें।
3. `args` ऐरे को `OptionSet` में पार्स करें।
4. फ्लैग्स, मानों और गैर-विकल्प आर्ग्युमेंट तक पहुँचने के लिए `OptionSet` का उपयोग करें।
5. आवश्यकतानुसार एरर और हेल्प को हैंडल करें।

इस आधार के साथ, आप अपने एप्लिकेशन की आवश्यकताओं के अनुरूप मजबूत कमांड-लाइन इंटरफेस बना सकते हैं!