---
audio: false
generated: true
lang: hi
layout: post
title: जावा में कमांड-लाइन तर्कों का विश्लेषण
translated: true
type: note
---

`net.sourceforge.argparse4j` का उपयोग करने के लिए, जो कि Python के `argparse` से प्रेरित कमांड-लाइन आर्ग्युमेंट्स को पार्स करने वाली एक Java लाइब्रेरी है, इन चरणों का पालन करें:

---

### 1. **डिपेंडेंसी जोड़ें**
अपने प्रोजेक्ट में `argparse4j` को शामिल करने के लिए, इसे एक डिपेंडेंसी के रूप में जोड़ें। यदि आप Maven का उपयोग कर रहे हैं, तो अपनी `pom.xml` को निम्नलिखित के साथ अपडेट करें:

```xml
<dependency>
    <groupId>net.sourceforge.argparse4j</groupId>
    <artifactId>argparse4j</artifactId>
    <version>0.9.0</version>
</dependency>
```

Gradle जैसे अन्य बिल्ड टूल्स के लिए, समतुल्य कॉन्फ़िगरेशन के लिए [Maven Central Repository](https://central.sonatype.com/artifact/net.sourceforge.argparse4j/argparse4j) देखें।

---

### 2. **एक `ArgumentParser` ऑब्जेक्ट बनाएँ**
एक `ArgumentParser` इंस्टेंस बनाकर शुरुआत करें, `ArgumentParsers.newFor("prog").build()` का उपयोग करके, जहाँ `"prog"` आपके प्रोग्राम का नाम है। आप एक विवरण भी जोड़ सकते हैं और स्वचालित सहायता जनरेशन को सक्षम कर सकते हैं।

**उदाहरण:**
```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;

ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
    .defaultHelp(true)  // -h/--help विकल्प सक्षम करता है
    .description("दिए गए फ़ाइलों का चेकसम कैलकुलेट करें।");
```

---

### 3. **आर्ग्युमेंट्स जोड़ें**
`parser.addArgument()` का उपयोग करके उन कमांड-लाइन आर्ग्युमेंट्स को परिभाषित करें जिन्हें आपका प्रोग्राम स्वीकार करेगा। आप निर्दिष्ट कर सकते हैं:
- **वैकल्पिक आर्ग्युमेंट्स** (जैसे, `-t`, `--type`) फ्लैग्स, विकल्प, डिफ़ॉल्ट, और सहायता पाठ के साथ।
- **पोजिशनल आर्ग्युमेंट्स** (जैसे, `file`) `.nargs("*")` का उपयोग करके वैरिएबल-लेंथ सपोर्ट के साथ।

**उदाहरण:**
```java
parser.addArgument("-t", "--type")
    .choices("SHA-256", "SHA-512", "SHA1")  // इन विकल्पों तक सीमित करें
    .setDefault("SHA-256")                  // यदि प्रदान नहीं किया गया तो डिफ़ॉल्ट मान
    .help("उपयोग करने के लिए हैश फ़ंक्शन निर्दिष्ट करें");  // सहायता संदेश के लिए विवरण

parser.addArgument("file")
    .nargs("*")                             // शून्य या अधिक आर्ग्युमेंट्स स्वीकार करता है
    .help("चेकसम कैलकुलेट करने के लिए फ़ाइल");    // सहायता संदेश के लिए विवरण
```

---

### 4. **कमांड-लाइन आर्ग्युमेंट्स को पार्स करें**
कमांड-लाइन आर्ग्युमेंट्स (आमतौर पर आपकी `main` मेथड से `String[] args` के रूप में पास किए गए) को `parser.parseArgs()` का उपयोग करके पार्स करें। पार्सिंग एरर को सही तरीके से हैंडल करने के लिए इसे एक try-catch ब्लॉक में लपेटें।

**उदाहरण:**
```java
import net.sourceforge.argparse4j.inf.Namespace;
import net.sourceforge.argparse4j.inf.ArgumentParserException;

public class Checksum {
    public static void main(String[] args) {
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("दिए गए फ़ाइलों का चेकसम कैलकुलेट करें।");
        
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("उपयोग करने के लिए हैश फ़ंक्शन निर्दिष्ट करें");
        parser.addArgument("file").nargs("*")
            .help("चेकसम कैलकुलेट करने के लिए फ़ाइल");

        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);  // आर्ग्युमेंट्स को पार्स करें
        } catch (ArgumentParserException e) {
            parser.handleError(e);        // एरर और सहायता संदेश प्रिंट करें
            System.exit(1);               // एरर पर बाहर निकलें
        }
    }
}
```

---

### 5. **पार्स किए गए मानों तक पहुँचें**
`parseArgs()` मेथड एक `Namespace` ऑब्जेक्ट लौटाती है जिसमें पार्स किए गए आर्ग्युमेंट मान होते हैं। उन्हें पुनः प्राप्त करने के लिए `getString()` या `getList()` जैसी मेथड्स का उपयोग करें।

**उदाहरण:**
```java
String hashType = ns.getString("type");  // उदा., "SHA-256"
List<String> files = ns.getList("file"); // फ़ाइल नामों की सूची

System.out.println("Hash Type: " + hashType);
System.out.println("Files: " + files);
```

---

### सभी को एक साथ रखते हुए
यहाँ एक पूर्ण उदाहरण दिया गया है:

```java
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;
import net.sourceforge.argparse4j.inf.ArgumentParserException;
import net.sourceforge.argparse4j.inf.Namespace;
import java.util.List;

public class Checksum {
    public static void main(String[] args) {
        // चरण 2: पार्सर बनाएँ
        ArgumentParser parser = ArgumentParsers.newFor("Checksum").build()
            .defaultHelp(true)
            .description("दिए गए फ़ाइलों का चेकसम कैलकुलेट करें।");

        // चरण 3: आर्ग्युमेंट्स जोड़ें
        parser.addArgument("-t", "--type")
            .choices("SHA-256", "SHA-512", "SHA1").setDefault("SHA-256")
            .help("उपयोग करने के लिए हैश फ़ंक्शन निर्दिष्ट करें");
        parser.addArgument("file").nargs("*")
            .help("चेकसम कैलकुलेट करने के लिए फ़ाइल");

        // चरण 4: आर्ग्युमेंट्स पार्स करें
        Namespace ns = null;
        try {
            ns = parser.parseArgs(args);
        } catch (ArgumentParserException e) {
            parser.handleError(e);
            System.exit(1);
        }

        // चरण 5: पार्स किए गए मानों तक पहुँचें
        String hashType = ns.getString("type");
        List<String> files = ns.getList("file");

        // उदाहरण आउटपुट
        System.out.println("Hash Type: " + hashType);
        System.out.println("Files: " + files);
    }
}
```

---

### अतिरिक्त सुविधाएँ
- **स्वचालित सहायता**: जनरेट किए गए सहायता संदेश को देखने के लिए अपने प्रोग्राम को `-h` या `--help` के साथ चलाएँ।
- **सबकमांड्स**: कॉम्प्लेक्स कमांड्स (जैसे, `git commit`, `git push`) के लिए `parser.addSubparsers()` का उपयोग करें।
- **एनोटेशन्स**: एनोटेशन्स का उपयोग करके आर्ग्युमेंट्स को क्लास फ़ील्ड्स से बाइंड करें (विवरण के लिए यूज़र मैन्युअल देखें)।

अधिक एडवांस्ड उपयोग के लिए, [Argparse4j User Manual](https://argparse4j.github.io/userguide.html) से सलाह लें।

---

यह वर्कफ़्लो आपको `net.sourceforge.argparse4j` का उपयोग करके अपने Java एप्लिकेशन में कमांड-लाइन आर्ग्युमेंट्स को आसानी से पार्स और हैंडल करने देता है।