---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: ग्रालवीएम स्थापना एवं उपयोग गाइड
translated: true
type: note
---

## GraalVM क्या है?

GraalVM एक ओपन-सोर्स हाई-परफॉर्मेंस रनटाइम (JDK डिस्ट्रीब्यूशन) है जो Java, JavaScript, Python और अन्य जैसी कई प्रोग्रामिंग भाषाओं को सपोर्ट करता है। इसमें तेज एक्सेक्यूशन के लिए एक एडवांस्ड JIT कंपाइलर और Native Image के माध्यम से Java एप्लिकेशन को नेटिव एक्ज़िक्यूटेबल में कंपाइल करने की क्षमता है, जिससे स्टार्टअप टाइम और मेमोरी फुटप्रिंट कम होता है।

## इंस्टालेशन

1.  **GraalVM डाउनलोड करें**:
    *   आधिकारिक GraalVM डाउनलोड्स पेज पर जाएं।
    *   कम्युनिटी एडिशन (मुफ्त) या Oracle GraalVM (अतिरिक्त फीचर्स के साथ) चुनें।
    *   अपने प्लेटफॉर्म (जैसे Linux, macOS, Windows) और आर्किटेक्चर (x64 या ARM) के लिए वर्जन चुनें।
    *   2025 तक, नवीनतम स्टेबल रिलीज़ GraalVM for JDK 22 या 23 है—सबसे करंट के लिए साइट चेक करें।

2.  **एक्सट्रैक्ट और इंस्टॉल करें**:
    *   डाउनलोड की गई आर्काइव को एक डायरेक्टरी में अनज़िप करें, जैसे Linux/macOS पर `/opt/graalvm` या Windows पर `C:\Program Files\GraalVM`।
    *   किसी इंस्टॉलर की जरूरत नहीं है; यह एक पोर्टेबल डिस्ट्रीब्यूशन है।

3.  **एनवायरनमेंट वेरिएबल्स सेट करें**:
    *   `JAVA_HOME` को GraalVM डायरेक्टरी पर सेट करें (जैसे Linux/macOS पर `export JAVA_HOME=/opt/graalvm`)।
    *   `bin` डायरेक्टरी को अपने `PATH` में ऐड करें (जैसे `export PATH=$JAVA_HOME/bin:$PATH`)।
    *   `java -version` से वेरिफाई करें; इसमें GraalVM की डिटेल्स दिखनी चाहिए।

4.  **अतिरिक्त कंपोनेंट्स इंस्टॉल करें (ऑप्शनल)**:
    *   लैंग्वेज रनटाइम्स या Native Image के लिए `gu` (GraalVM अपडेटर) का उपयोग करें: `gu install native-image` (Linux पर `build-essential` जैसे बिल्ड टूल्स की आवश्यकता होती है)।

## एक Hello World प्रोग्राम बनाना

हम इस उदाहरण के लिए Java का उपयोग करेंगे, क्योंकि यह GraalVM की प्राथमिक भाषा है। एक साधारण "Hello World" ऐप बनाएं, इसे कंपाइल करें और रन करें।

### चरण 1: कोड लिखें
`HelloWorld.java` नाम की एक फाइल बनाएं:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World from GraalVM!");
    }
}
```

### चरण 2: कंपाइल करें
फाइल वाली डायरेक्टरी में एक टर्मिनल खोलें और रन करें:
```
javac HelloWorld.java
```
यह `HelloWorld.class` फाइल बनाता है।

### चरण 3: रन करें
```
java HelloWorld
```
आउटपुट:
```
Hello, World from GraalVM!
```

### एडवांस्ड: नेटिव एक्ज़िक्यूटेबल में कंपाइल करें
GraalVM का Native Image फीचर आपको एक स्टैंडअलोन बाइनरी बनाने देता है।

1.  सुनिश्चित करें कि Native Image इंस्टॉल है: `gu install native-image`.
2.  एक कॉन्फ़िगरेशन जेनरेट करें (पहली बार रन करने पर इसकी आवश्यकता हो सकती है):
    ```
    native-image --no-fallback -H:+ReportExceptionStackTraces HelloWorld
    ```
    *   यह `HelloWorld` (या Windows पर `helloworld.exe`) बनाता है, जो एक नेटिव बाइनरी है।
    *   पहले बिल्ड पर, यह ऐप का विश्लेषण करता है और इसमें कुछ मिनट लग सकते हैं।

3.  नेटिव बाइनरी रन करें:
    ```
    ./HelloWorld
    ```
    आउटपुट वही है, लेकिन यह कम मेमोरी उपयोग के साथ तुरंत शुरू होती है।

## GraalVM उपयोग करने के टिप्स
*   **JDK बदलना**: आसान प्रबंधन के लिए SDKMAN! (`sdk install java 22.0.2-graal`) का उपयोग करें।
*   **मल्टी-लैंग्वेज**: GraalVM से `node` के साथ Node.js कोड, या `python` के साथ Python रन करें।
*   **परफॉर्मेंस**: `-XX:+UnlockExperimentalVMOptions -XX:+UseJVMCICompiler` के साथ GraalVM का JIT एनेबल करें।
*   **ट्रबलशूटिंग**: समस्याओं के लिए `~/.gu/` में लॉग्स चेक करें; Native Image के लिए सुनिश्चित करें कि आपके सिस्टम में एक C कंपाइलर है।

अधिक जानकारी के लिए, आधिकारिक डॉक्स देखें।

[GraalVM डाउनलोड्स](https://www.graalvm.org/downloads/)  
[GraalVM यूजर गाइड](https://www.graalvm.org/latest/reference-manual/)  
[Native Image ट्यूटोरियल](https://www.graalvm.org/latest/reference-manual/native-image/)