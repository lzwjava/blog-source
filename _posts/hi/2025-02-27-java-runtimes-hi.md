---
audio: false
generated: false
lang: hi
layout: post
title: 'Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code


  Java Runtimes in Visual Studio Code'
translated: true
---

`java.configuration.runtimes` को Visual Studio Code (VS Code) सेटिंग्स में उपयोग करने के लिए, आपको अपने `settings.json` फ़ाइल में इसे कॉन्फ़िगर करना होगा। यह सेटिंग आपको VS Code को आपके Java प्रोजेक्ट्स के लिए उपयोग करने के लिए कई Java Development Kit (JDK) संस्करणों को स्पेसिफ़ाई करने की अनुमति देता है। यह विशेष रूप से अलग-अलग प्रोजेक्ट्स के साथ काम करने के लिए उपयोगी है जो विशिष्ट Java संस्करणों की आवश्यकता होती हैं। यहां एक स्टेप-बाय-स्टेप गाइड है इसे सेटअप करने के लिए:

### `java.configuration.runtimes` को कॉन्फ़िगर करने के लिए चरण

1. **VS Code सेटिंग्स खोलें**:
   - Windows/Linux पर: `File > Preferences > Settings` पर जाएं या `Ctrl + ,` दबाएं।
   - macOS पर: `Code > Preferences > Settings` पर जाएं या `Cmd + ,` दबाएं।

2. **JSON सेटिंग्स फ़ाइल तक पहुंचें**:
   - सेटिंग्स UI में, `java.configuration.runtimes` के लिए खोजें।
   - आप "Java: Configuration: Runtimes" जैसा विकल्प देखेंगे। "Edit in settings.json" (सामान्यतः सेटिंग्स विवरण के नीचे एक लिंक) पर क्लिक करें `settings.json` फ़ाइल को खोलने के लिए।

3. **`settings.json` को संपादित करें**:
   - `settings.json` फ़ाइल में, `java.configuration.runtimes` एरे को जोड़ें या संपादित करें। इस एरे में वस्तुएं होती हैं, प्रत्येक एक JDK संस्करण को VS Code को पहचानने के लिए प्रतिनिधित्व करता है।
   - प्रत्येक वस्तु आमतौर पर शामिल होती है:
     - `name`: Java संस्करण पहचानकर्ता (उदाहरण के लिए, `JavaSE-1.8`, `JavaSE-11`, `JavaSE-17`).
     - `path`: आपके सिस्टम पर JDK इंस्टॉलेशन डायरेक्टरी का पूर्ण पथ।
     - `default` (वैकल्पिक): इसे `true` सेट करें ताकि यह अनमैनेज्ड फ़ोल्डर्स (मैवेन या ग्रेडल जैसी बिल्ड टूल्स के बिना प्रोजेक्ट्स) के लिए डिफ़ॉल्ट JDK बन जाए।

   यहां एक उदाहरण कॉन्फ़िगरेशन है:

   ```json
   {
       "java.configuration.runtimes": [
           {
               "name": "JavaSE-1.8",
               "path": "C:/Program Files/Java/jdk1.8.0_351",
               "default": true
           },
           {
               "name": "JavaSE-11",
               "path": "C:/Program Files/Java/jdk-11.0.15"
           },
           {
               "name": "JavaSE-17",
               "path": "C:/Program Files/Java/jdk-17.0.6"
           }
       ]
   }
   ```

4. **JDK पथों की पुष्टि करें**:
   - `path` को JDK इंस्टॉलेशन के रूट डायरेक्टरी (जहां `bin` फ़ोल्डर `java.exe` या `java` है) पर सेट करें।
   - Windows पर, पथ में फॉरवर्ड स्लैश (`/`) या बैकस्लैश (`\\`) का उपयोग करें।
   - macOS/Linux पर, उचित फ़ाइल सिस्टम पथ का उपयोग करें (उदाहरण के लिए, `/usr/lib/jvm/java-17-openjdk`).

5. **सहेजें और पुनः लोड करें**:
   - `settings.json` फ़ाइल को सहेजें।
   - VS Code को पुनः शुरू करें या विंडो को पुनः लोड करें (`Ctrl + R` या `Cmd + R`) बदलाव लागू करने के लिए।

6. **कॉन्फ़िगरेशन की जांच करें**:
   - कमांड पॅलेट (`Ctrl + Shift + P` या `Cmd + Shift + P`) खोलें और कमांड `Java: Configure Java Runtime` चलाएं।
   - यह एक दृश्य खोलता है जिसमें आपके प्रोजेक्ट्स के लिए उपलब्ध JDKs दिखते हैं। पुष्टि करें कि आपके कॉन्फ़िगर किए गए रनटाइम "Project JDKs" टैब के नीचे दिखाई देते हैं।

### यह कैसे काम करता है
- **अनमैनेज्ड फ़ोल्डर्स**: बिल्ड टूल्स के बिना प्रोजेक्ट्स (उदाहरण के लिए, साधारण Java फ़ाइलें) के लिए, VS Code `java.configuration.runtimes` में स्पेसिफ़ाई किया गया `default` JDK का उपयोग करता है।
- **मैनेज्ड प्रोजेक्ट्स (Maven/Gradle)**: बिल्ड टूल्स के साथ प्रोजेक्ट्स के लिए, JDK संस्करण बिल्ड कॉन्फ़िगरेशन (उदाहरण के लिए, `pom.xml` या `build.gradle`) द्वारा निर्धारित होता है, लेकिन VS Code अभी भी यहाँ सूचीबद्ध रनटाइम्स को अनुकूलता के लिए पहचानेगा।
- **लैंग्वेज सर्वर**: Java लैंग्वेज सर्वर (Java एक्सटेंशन का हिस्सा) को चलाने के लिए JDK 17+ की आवश्यकता होती है। अगर आवश्यक हो, इसे अलग से `java.jdt.ls.java.home` के साथ स्पेसिफ़ाई किया जा सकता है (उदाहरण के लिए, `"java.jdt.ls.java.home": "C:/Program Files/Java/jdk-17.0.6"`).

### कई JDKs के साथ उदाहरण
अगर आप Mac पर हैं और Homebrew के माध्यम से JDK 8 और 17 इंस्टॉल किए हैं, तो आपके कॉन्फ़िगरेशन इस तरह दिख सकता है:

```json
{
    "java.configuration.runtimes": [
        {
            "name": "JavaSE-1.8",
            "path": "/Library/Java/JavaVirtualMachines/jdk1.8.0_351.jdk/Contents/Home",
            "default": true
        },
        {
            "name": "JavaSE-17",
            "path": "/Library/Java/JavaVirtualMachines/jdk-17.0.6.jdk/Contents/Home"
        }
    ]
}
```

### टिप्स
- सही `name` फ़ॉर्मेट (`JavaSE-<version>`) का उपयोग करें, जो Java संस्करण (उदाहरण के लिए, Java 11 के लिए `JavaSE-11`) के साथ मिलता है।
- अगर आपके पास केवल एक JDK है, तो आप इसे सूचीबद्ध करके VS Code को इसे स्पेसिफ़िक रूप से उपयोग करने के लिए सुनिश्चित कर सकते हैं।
- JDK पथ को खोजने के लिए, एक टर्मिनल में `java -version` चलाएं और इंस्टॉलेशन डायरेक्टरी (उदाहरण के लिए, Windows पर `where java` या Unix-like सिस्टम पर `which java`, फिर JDK रूट तक वापस ट्रेस करने के लिए) की जांच करें।

यह सेटअप आपको VS Code में कई Java संस्करणों के साथ काम करने की सुविधा देता है! मुझे बताएं अगर आपको JDK पथों को खोजने या ट्रबलशूटिंग करने में मदद चाहिए।