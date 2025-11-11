---
audio: false
generated: true
lang: hi
layout: post
title: जावा में कंसोल इनपुट पढ़ना
translated: true
type: note
---

Java में `org.jline.reader` पैकेज का उपयोग करने के लिए, जो कि लाइन एडिटिंग, हिस्ट्री और कम्प्लीशन जैसी एडवांस्ड फीचर्स के साथ कंसोल इनपुट को हैंडल करने के लिए JLine लाइब्रेरी का हिस्सा है, इन चरणों का पालन करें। यह गाइड आपको शुरुआत करने के लिए एक पूर्ण और व्यावहारिक तरीका प्रदान करती है।

### पूर्वापेक्षाएँ
सुनिश्चित करें कि आपने JLine लाइब्रेरी को अपने प्रोजेक्ट में जोड़ा है। यदि आप Maven का उपयोग कर रहे हैं, तो अपनी `pom.xml` फाइल में निम्नलिखित डिपेंडेंसी शामिल करें:

```xml
<dependency>
    <groupId>org.jline</groupId>
    <artifactId>jline</artifactId>
    <version>3.21.0</version> <!-- नवीनतम वर्जन का उपयोग करें -->
</dependency>
```

### `org.jline.reader` का उपयोग करने के बुनियादी चरण

1. **एक Terminal इंस्टेंस बनाएँ**
   - `org.jline.terminal` से `TerminalBuilder` क्लास का उपयोग करके एक `Terminal` ऑब्जेक्ट बनाएँ। यह उस कंसोल एनवायरनमेंट को रिप्रेजेंट करता है जहाँ इनपुट पढ़ा जाएगा।
   - उदाहरण:
     ```java
     import org.jline.terminal.Terminal;
     import org.jline.terminal.TerminalBuilder;

     Terminal terminal = TerminalBuilder.builder().build();
     ```
   - `build()` मेथड ज्यादातर एनवायरनमेंट के लिए उपयुक्त एक डिफॉल्ट टर्मिनल बनाती है। आप इसे और कस्टमाइज़ कर सकते हैं (जैसे, टर्मिनल टाइप सेट करना), लेकिन डिफॉल्ट अक्सर पर्याप्त होता है।

2. **एक LineReader इंस्टेंस बनाएँ**
   - `org.jline.reader` से `LineReaderBuilder` क्लास का उपयोग करके एक `LineReader` ऑब्जेक्ट बनाएँ, और इसमें `Terminal` इंस्टेंस पास करें।
   - `LineReader` JLine की फीचर्स के साथ यूजर इनपुट पढ़ने के लिए मुख्य इंटरफेस है।
   - उदाहरण:
     ```java
     import org.jline.reader.LineReader;
     import org.jline.reader.LineReaderBuilder;

     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .build();
     ```

3. **यूजर से इनपुट पढ़ें**
   - यूजर द्वारा दर्ज किए गए टेक्स्ट की एक लाइन पढ़ने के लिए `LineReader` की `readLine()` मेथड का उपयोग करें। आप वैकल्पिक रूप से डिस्प्ले करने के लिए एक प्रॉम्प्ट निर्दिष्ट कर सकते हैं।
   - उदाहरण:
     ```java
     String line = reader.readLine("> ");
     ```
   - यह `> ` को एक प्रॉम्प्ट के रूप में डिस्प्ले करता है, यूजर इनपुट की प्रतीक्षा करता है, और जब यूजर Enter दबाता है तो दर्ज किए गए स्ट्रिंग को रिटर्न करता है।

### सरल उदाहरण
यहाँ एक पूर्ण, न्यूनतम उदाहरण है जो यूजर द्वारा "exit" टाइप करने तक लूप में यूजर इनपुट पढ़ता है:

```java
import org.jline.reader.LineReader;
import org.jline.reader.LineReaderBuilder;
import org.jline.terminal.Terminal;
import org.jline.terminal.TerminalBuilder;

public class ConsoleExample {
    public static void main(String[] args) throws Exception {
        // Terminal बनाएँ
        Terminal terminal = TerminalBuilder.builder().build();
        
        // LineReader बनाएँ
        LineReader reader = LineReaderBuilder.builder()
            .terminal(terminal)
            .build();
        
        // लूप में इनपुट पढ़ें
        String line;
        while ((line = reader.readLine("> ")) != null) {
            System.out.println("You entered: " + line);
            if (line.equals("exit")) {
                break;
            }
        }
    }
}
```

- **आउटपुट**: जब आप इसे रन करते हैं, तो यह एक `> ` प्रॉम्प्ट डिस्प्ले करता है। आप टेक्स्ट टाइप कर सकते हैं, एडिटिंग के लिए बैकस्पेस या एरो कीज़ का उपयोग कर सकते हैं (ये फीचर्स `System.in` के साथ आसानी से उपलब्ध नहीं हैं), और Enter दबा सकते हैं। "exit" टाइप करने से प्रोग्राम समाप्त हो जाता है।

### वैकल्पिक सुविधाएँ
आप अतिरिक्त फंक्शनैलिटी के साथ `LineReader` को बेहतर बना सकते हैं:

#### 1. **कमांड हिस्ट्री सक्षम करें**
   - पिछले इनपुट को स्टोर और रिकॉल करने के लिए (जैसे, ऊपर/नीचे एरो कीज़ का उपयोग करके) एक `History` ऑब्जेक्ट जोड़ें।
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
   - अब, यूजर अपनी इनपुट हिस्ट्री के माध्यम से नेविगेट कर सकता है।

#### 2. **ऑटो-कम्प्लीशन जोड़ें**
   - जब यूजर Tab दबाता है तो सुझाव देने के लिए एक `Completer` इम्प्लीमेंट करें।
   - एक साधारण स्ट्रिंग कम्प्लीटर के साथ उदाहरण:
     ```java
     import org.jline.reader.Completer;
     import org.jline.reader.impl.completer.StringsCompleter;

     Completer completer = new StringsCompleter("foo", "bar", "baz");
     LineReader reader = LineReaderBuilder.builder()
         .terminal(terminal)
         .completer(completer)
         .build();
     ```
   - "f" टाइप करने और Tab दबाने पर "foo" का सुझाव देता है।

#### 3. **पासवर्ड पढ़ें (मास्क्ड इनपुट)**
   - इनपुट को छिपाने के लिए (जैसे, पासवर्ड के लिए) एक मास्क कैरेक्टर के साथ `readLine()` का उपयोग करें।
   - उदाहरण:
     ```java
     String password = reader.readLine("Enter password: ", '*');
     ```
   - टाइप किए गए कैरेक्टर्स के बजाय एस्टरिस्क (`*`) डिस्प्ले करता है।

### संसाधन प्रबंधन
मजबूत एप्लिकेशन्स के लिए, संसाधनों को मुक्त करने के लिए कार्य पूरा होने पर `Terminal` को बंद कर दें। चूंकि `Terminal` `Closeable` को इम्प्लीमेंट करता है, try-with-resources ब्लॉक का उपयोग करें:

```java
try (Terminal terminal = TerminalBuilder.builder().build()) {
    LineReader reader = LineReaderBuilder.builder()
        .terminal(terminal)
        .build();
    String line = reader.readLine("> ");
    System.out.println("You entered: " + line);
}
```

### `org.jline.reader` का उपयोग क्यों करें?
`System.in` और `BufferedReader` के साथ बेसिक इनपुट के विपरीत, `org.jline.reader` प्रदान करता है:
- **लाइन एडिटिंग**: बैकस्पेस, कर्सर मूवमेंट, आदि।
- **हिस्ट्री**: पिछले इनपुट को याद करना।
- **कम्प्लीशन**: ऑटो-सजेस्ट ऑप्शन्स।
- **क्रॉस-प्लेटफॉर्म टर्मिनल हैंडलिंग**: विभिन्न एनवायरनमेंट में लगातार काम करता है।

### नोट्स
- यदि आप `LineReaderBuilder` में एक `Terminal` निर्दिष्ट नहीं करते हैं, तो यह आंतरिक रूप से एक डिफॉल्ट बनाता है, इसलिए `LineReader reader = LineReaderBuilder.builder().build();` सरल मामलों के लिए काम करता है।
- एक साथ कई थ्रेड्स से `readLine()` को कॉल करने से बचें, क्योंकि `LineReader` कंकरंट रीड्स के लिए थ्रेड-सेफ नहीं है।
- एडवांस्ड यूज केस (जैसे, मल्टी-लाइन इनपुट, कस्टम की बाइंडिंग्स) के लिए पार्सर्स या की मैप्स जैसी अतिरिक्त JLine फीचर्स का पता लगाएँ।

यह Java में कंसोल इनपुट को प्रभावी ढंग से पढ़ने के लिए `org.jline.reader` का उपयोग करने की बुनियादी बातों को कवर करता है। बेसिक सेटअप से शुरुआत करें और अपनी एप्लिकेशन की आवश्यकतानुसार हिस्ट्री या कम्प्लीशन जैसी फीचर्स जोड़ें!