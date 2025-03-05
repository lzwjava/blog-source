---
audio: false
generated: true
lang: hi
layout: post
title: कंसोल इनपुट पढ़ना जावा में
translated: true
---

`org.jline.reader` पैकेज का उपयोग करने के लिए Java में, जो JLine लाइब्रेरी का हिस्सा है, जो लाइन एडिटिंग, इतिहास और पूर्णता जैसी उन्नत सुविधाओं के साथ कंसोल इनपुट को संभालने के लिए है, इन चरणों का पालन करें। यह गाइड आपको शुरू करने के लिए एक पूर्ण और व्यावहारिक दृष्टिकोण प्रदान करता है।

### पूर्वापेक्षाएँ
यदि आप Maven का उपयोग कर रहे हैं, तो अपने `pom.xml` में निम्नलिखित निर्भरता शामिल करें:

```xml
<dependency>
    <groupId>org.jline</groupId>
    <artifactId>jline</artifactId>
    <version>3.21.0</version> <!-- नवीनतम संस्करण का उपयोग करें -->
</dependency>
```

### `org.jline.reader` का उपयोग करने के लिए बुनियादी चरण

1. **टर्मिनल इंस्टेंस बनाएं**
   - `org.jline.terminal` से `TerminalBuilder` क्लास का उपयोग करें `Terminal` ऑब्जेक्ट बनाने के लिए। यह कंसोल वातावरण का प्रतिनिधित्व करता है जहां इनपुट पढ़ा जाएगा।
   - उदाहरण:
     ```java
     import org.jline.terminal.Terminal;
     import org.jline.terminal.TerminalBuilder;

     Terminal terminal = TerminalBuilder.builder().build();
     ```
   - `build()` विधि एक डिफ़ॉल्ट टर्मिनल बनाती है जो अधिकांश वातावरणों के लिए उपयुक्त है। आप इसे और अधिक अनुकूलित कर सकते हैं (उदाहरण के लिए, टर्मिनल प्रकार सेट करना), लेकिन डिफ़ॉल्ट अधिकांश समय पर्याप्त होता है।

2. **लाइन रीडर इंस्टेंस बनाएं**
   - `org.jline.reader` से `LineReaderBuilder` क्लास का उपयोग करें `LineReader` ऑब्जेक्ट बनाने के लिए, उसे `Terminal` इंस्टेंस पास करें।
   - `LineReader` JLine के सुविधाओं के साथ उपयोगकर्ता इनपुट पढ़ने का मुख्य इंटरफ़ेस है।
   - उदाहरण:
     ```java
     import org.jline.reader.LineReader;
     import org.jline.reader.LineReaderBuilder;

     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .build();
     ```

3. **उपयोगकर्ता से इनपुट पढ़ें**
   - `LineReader` का `readLine()` विधि का उपयोग करें एक पंक्ति पाठ पढ़ने के लिए जो उपयोगकर्ता द्वारा दर्ज किया गया है। आप एक प्रोम्प्ट दर्शाने के लिए विकल्प के साथ भी पढ़ सकते हैं।
   - उदाहरण:
     ```java
     String line = reader.readLine("> ");
     ```
   - यह `> ` को एक प्रोम्प्ट के रूप में दर्शाता है, उपयोगकर्ता इनपुट के लिए इंतजार करता है, और उपयोगकर्ता Enter दबाता है तो दर्ज किया गया स्ट्रिंग लौटाता है।

### सरल उदाहरण
यह एक पूर्ण, न्यूनतम उदाहरण है जो उपयोगकर्ता इनपुट को एक लूप में पढ़ता है जब तक कि उपयोगकर्ता "exit" टाइप नहीं करता:

```java
import org.jline.reader.LineReader;
import org.jline.reader.LineReaderBuilder;
import org.jline.terminal.Terminal;
import org.jline.terminal.TerminalBuilder;

public class ConsoleExample {
    public static void main(String[] args) throws Exception {
        // टर्मिनल बनाएं
        Terminal terminal = TerminalBuilder.builder().build();

        // लाइन रीडर बनाएं
        LineReader reader = LineReaderBuilder.builder()
            .terminal(terminal)
            .build();

        // लूप में इनपुट पढ़ें
        String line;
        while ((line = reader.readLine("> ")) != null) {
            System.out.println("आपने दर्ज किया: " + line);
            if (line.equals("exit")) {
                break;
            }
        }
    }
}
```

- **आउटपुट**: जब आप इसे चलाते हैं, तो यह `> ` प्रोम्प्ट दर्शाता है। आप पाठ टाइप कर सकते हैं, बैकस्पेस या तीर चाबियों का उपयोग कर सकते हैं संपादन (जो `System.in` के साथ आसानी से उपलब्ध नहीं हैं), और Enter दबाएं। "exit" टाइप करने से प्रोग्राम समाप्त होता है।

### विकल्पीय सुविधाएँ
आप `LineReader` को अतिरिक्त कार्यक्षमता के साथ बढ़ा सकते हैं:

#### 1. **कमांड इतिहास सक्षम करें**
   - एक `History` ऑब्जेक्ट जोड़ें पूर्ववर्ती इनपुट को स्टोर और पुनः प्राप्त करने के लिए (उदाहरण के लिए, ऊपर/नीचे तीर चाबियों का उपयोग करके)।
   - उदाहरण:
     ```java
     import org.jline.reader.impl.history.DefaultHistory;
     import org.jline.reader.History;

     History history = new DefaultHistory();
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .history(history)
         .build();
     ```
   - अब, उपयोगकर्ता अपने इनपुट इतिहास में नाविगेट कर सकता है।

#### 2. **स्वचालित पूर्णता जोड़ें**
   - एक `Completer` लागू करें जब उपयोगकर्ता टैब दबाता है तो पूर्णताओं का सुझाव देना।
   - एक सरल स्ट्रिंग Completer के साथ उदाहरण:
     ```java
     import org.jline.reader.Completer;
     import org.jline.reader.impl.completer.StringsCompleter;

     Completer completer = new StringsCompleter("foo", "bar", "baz");
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .completer(completer)
         .build();
     ```
   - "f" टाइप करने और टैब दबाने से "foo" का सुझाव मिलता है।

#### 3. **पासवर्ड पढ़ें (मास्क्ड इनपुट)**
   - एक मास्क चरित्र के साथ `readLine()` का उपयोग करें दर्ज किया गया इनपुट छिपाने के लिए (उदाहरण के लिए, पासवर्ड के लिए)।
   - उदाहरण:
     ```java
     String password = reader.readLine("पासवर्ड दर्ज करें: ", '*');
     ```
   - टाइप किए गए चरित्रों के बजाय अस्तरिक (`*`) दर्शाता है।

### संसाधन प्रबंधन
रोबस्ट एप्लिकेशन के लिए, जब समाप्त हो जाए तो संसाधनों को मुक्त करने के लिए `Terminal` को बंद करें। क्योंकि `Terminal` `Closeable` को लागू करता है, तो एक try-with-resources ब्लॉक का उपयोग करें:

```java
try (Terminal terminal = TerminalBuilder.builder().build()) {
    LineReader reader = LineReaderBuilder.builder()
        .terminal(terminal)
        .build();
    String line = reader.readLine("> ");
    System.out.println("आपने दर्ज किया: " + line);
}
```

### `org.jline.reader` का उपयोग क्यों करें?
`System.in` और `BufferedReader` के साथ बुनियादी इनपुट के विपरीत, `org.jline.reader` प्रदान करता है:
- **लाइन संपादन**: बैकस्पेस, कर्सर आंदोलन आदि।
- **इतिहास**: पूर्ववर्ती इनपुट को याद करना।
- **पूर्णता**: स्वचालित विकल्प सुझाव।
- **क्रॉस-प्लेटफॉर्म टर्मिनल प्रबंधन**: विभिन्न वातावरणों में एकसमान रूप से काम करता है।

### टिप्पणियाँ
- यदि आप `LineReaderBuilder` में `Terminal` नहीं निर्दिष्ट करते हैं, तो यह एक डिफ़ॉल्ट एक बनाता है, इसलिए `LineReader reader = LineReaderBuilder.builder().build();` सरल मामलों के लिए काम करता है।
- `readLine()` को एक साथ कई थ्रेड्स से बुलाने से बचें, क्योंकि `LineReader` एक साथ पढ़ने के लिए थ्रेड-सेफ नहीं है।
- उन्नत उपयोग के मामलों (उदाहरण के लिए, बहु-पंक्ति इनपुट, कस्टम चाबी बाइंडिंग) के लिए, JLine के अतिरिक्त सुविधाओं जैसे पार्सर या चाबी मैप्स का पता लगाएं।

यह `org.jline.reader` का उपयोग करके Java में कंसोल इनपुट को प्रभावी ढंग से पढ़ने के लिए आवश्यकताओं को कवर करता है। बुनियादी सेटअप से शुरू करें और अपने एप्लिकेशन के लिए आवश्यकतानुसार इतिहास या पूर्णता जैसी सुविधाओं जोड़ें!