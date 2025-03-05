---
audio: false
generated: true
lang: hi
layout: post
title: कमांड लाइन अर्ग्यूमेंट्स को पार्सिंग करना जावा में
translated: true
---

`net.sourceforge.argparse4j` का उपयोग करने के लिए, एक Java लाइब्रेरी जो Python की `argparse` से प्रेरित है, निम्नलिखित चरणों का पालन करें:

---

### 1. **Dependency जोड़ें**
अपने प्रोजेक्ट में `argparse4j` को शामिल करने के लिए, इसे एक डिपेंडेंसी के रूप में जोड़ें। अगर आप Maven का उपयोग कर रहे हैं, तो अपने `pom.xml` को निम्नलिखित से अपडेट करें:

```xml
<dependency>
    <groupId>net.sourceforge.argparse4j</groupId>
    <artifactId>argparse4j</artifactId>
    <version>0.9.0</version>
</dependency>
```

अन्य बिल्ड टूल्स जैसे Gradle के लिए, [Maven Central Repository](https://central.sonatype.com/artifact/net.sourceforge.argparse4j/argparse4j) पर समकक्ष कॉन्फ़िगरेशन के लिए जांच करें।

---

### 2. **एक `ArgumentParser` ऑब्जेक्ट बनाएं**
`ArgumentParsers.newFor("prog").build()` का उपयोग करके एक `ArgumentParser` इंस्टेंस बनाएं, जहाँ `"prog"` आपके प्रोग्राम का नाम है। आप एक विवरण जोड़ सकते हैं और स्वचालित हेल्प जनरेशन को सक्रिय कर सकते हैं।

**उदाहरण:**
```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;

ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
    .defaultHelp(true)  // -h/--help विकल्प को सक्रिय करता है
    .description("दिए गए फाइलों का चेकसम गणना करें।");
```

---

### 3. **Arguments जोड़ें**
अपने प्रोग्राम द्वारा स्वीकार किए जाने वाले कमांड-लाइन arguments को `parser.addArgument()` का उपयोग करके परिभाषित करें। आप निम्नलिखित को स्पेसिफाई कर सकते हैं:
- **ऑप्शनल arguments** (जैसे, `-t`, `--type`) के साथ फ्लैग, चॉइस, डिफ़ॉल्ट और हेल्प टेक्स्ट।
- **पोजिशनल arguments** (जैसे, `file`) के साथ ऑप्शनल वेरिएबल-लेंथ समर्थन का उपयोग करके `.nargs("*")`.

**उदाहरण:**
```java
parser.addArgument("-t", "--type")
    .choices("SHA-256", "SHA-512", "SHA1")  // इन विकल्पों तक सीमित करें
    .setDefault("SHA-256")                  // अगर प्रदान नहीं किया गया तो डिफ़ॉल्ट मान
    .help("उपयोग करने के लिए हैश फंक्शन को स्पेसिफाई करें");  // हेल्प संदेश के लिए विवरण

parser.addArgument("file")
    .nargs("*")                             // शून्य या अधिक arguments स्वीकार करता है
    .help("चेकसम गणना करने के लिए फाइल");    // हेल्प संदेश के लिए विवरण
```

---

### 4. **कमांड-लाइन Arguments को पर्स करें**
कमांड-लाइन arguments (आम तौर पर `String[] args` के रूप में `main` विधि से पास किए जाते हैं) को `parser.parseArgs()` का उपयोग करके पर्स करें। इसे एक try-catch ब्लॉक में लपेटें ताकि पर्सिंग त्रुटियों को नम्रता से संभाल सकें।

**उदाहरण:**
```java
import net.sourceforge.argparse4j.inf.Namespace;
import net.sourceforge.argparse4j.inf.ArgumentParserException;

public class Checksum {
    public static void main(String[] args) {
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("दिए गए फाइलों का चेकसम गणना करें।");

        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("उपयोग करने के लिए हैश फंक्शन को स्पेसिफाई करें");
        parser.addArgument("file").nargs("*")
            .help("चेकसम गणना करने के लिए फाइल");

        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);  // arguments को पर्स करें
        } catch (ArgumentParserException e) {
            parser.handleError(e);        // त्रुटि और हेल्प संदेश प्रिंट करें
            System.exit(1);               // त्रुटि पर निकलें
        }
    }
}
```

---

### 5. **पर्स किए गए मानों तक पहुंचें**
`parseArgs()` विधि एक `Namespace` ऑब्जेक्ट लौटाती है जिसमें पर्स किए गए argument मान शामिल होते हैं। उन्हें प्राप्त करने के लिए `getString()` या `getList()` जैसे विधियों का उपयोग करें।

**उदाहरण:**
```java
String hashType = ns.getString("type");  // उदाहरण के लिए, "SHA-256"
List<String> files = ns.getList("file"); // फाइल नामों की सूची

System.out.println("Hash Type: " + hashType);
System.out.println("Files: " + files);
```

---

### सब कुछ एक साथ
यह एक पूर्ण उदाहरण है:

```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;
import net.sourceforge.argparse4j.inf.ArgumentParserException;
import net.sourceforge.argparse4j.inf.Namespace;
import java.util.List;

public class Checksum {
    public static void main(String[] args) {
        // चरण 2: parser बनाएं
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("दिए गए फाइलों का चेकसम गणना करें।");

        // चरण 3: arguments जोड़ें
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("उपयोग करने के लिए हैश फंक्शन को स्पेसिफाई करें");
        parser.addArgument("file").nargs("*")
            .help("चेकसम गणना करने के लिए फाइल");

        // चरण 4: arguments को पर्स करें
        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);
        } catch (ArgumentParserException e) {
            parser.handleError(e);
            System.exit(1);
        }

        // चरण 5: पर्स किए गए मानों तक पहुंचें
        String hashType = ns.getString("type");
        List<String> files = ns.getList("file");

        // उदाहरण आउटपुट
        System.out.println("Hash Type: " + hashType);
        System.out.println("Files: " + files);
    }
}
```

---

### अतिरिक्त विशेषताएं
- **स्वचालित हेल्प**: अपने प्रोग्राम को `-h` या `--help` के साथ चलाएं ताकि एक जनरेटेड हेल्प संदेश देख सकें।
- **सबकमांड**: जटिल कमांडों (जैसे, `git commit`, `git push`) के लिए `parser.addSubparsers()` का उपयोग करें।
- **एनोटेशन**: arguments को class फील्ड्स से बाइंड करने के लिए एनोटेशन का उपयोग करें (उपयोगकर्ता मैनुअल में विवरण के लिए देखें).

अधिक उन्नत उपयोग के लिए, [Argparse4j User Manual](https://argparse4j.github.io/userguide.html) पर जांच करें।

---

इस कार्यप्रणाली से आप अपने Java application में `net.sourceforge.argparse4j` का उपयोग करके कमांड-लाइन arguments को आसानी से पर्स और संभाल सकते हैं।