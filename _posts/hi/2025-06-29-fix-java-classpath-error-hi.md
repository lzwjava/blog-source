---
audio: false
generated: true
lang: hi
layout: post
title: जावा क्लासपाथ त्रुटि को ठीक करें
translated: true
type: note
---

आपके सामने आई यह त्रुटि (`Could not find or load main class scripts.benchmark.MultiMark`) इसलिए हुई क्योंकि आपने प्रोजेक्ट रूट डायरेक्टरी (`~/projects/lzwjava.github.io`) से पूरी क्लास का नाम (`scripts.benchmark.MultiMark`) इस्तेमाल करके Java प्रोग्राम चलाने की कोशिश की, लेकिन Java रनटाइम क्लास को उस डायरेक्टरी से चलाने की उम्मीद करता है जहाँ पैकेज स्ट्रक्चर शुरू होता है, या फिर आपको classpath को सही तरीके से निर्दिष्ट करने की आवश्यकता होती है। जब आप `scripts/benchmark` डायरेक्टरी में गए और `java MultiMark` चलाया, तो यह काम कर गया क्योंकि क्लास कमांड के सापेक्ष सही डायरेक्टरी में थी।

`MultiMark.java` या `MultiMark.class` को प्रोजेक्ट रूट डायरेक्टरी (`~/projects/lzwjava.github.io`) से बिना डायरेक्टरी बदले चलाने के लिए, आप Java को यह बताने के लिए `java` कमांड के साथ `-cp` (classpath) विकल्प का उपयोग कर सकते हैं कि compiled क्लास फ़ाइल कहाँ मिलेगी। यहाँ दो तरीके दिए गए हैं जो आपको रूट डायरेक्टरी में रखते हुए यह हासिल करने में मदद करेंगे:

---

### **विकल्प 1: Classpath के साथ Compiled क्लास चलाएँ**
यदि `MultiMark.class` पहले से ही `scripts/benchmark/` में मौजूद है (जैसा कि आपके `ls` आउटपुट में दिख रहा है), तो आप classpath निर्दिष्ट करके इसे रूट डायरेक्टरी से चला सकते हैं।

1. **रूट डायरेक्टरी में रहें**
   सुनिश्चित करें कि आप `~/projects/lzwjava.github.io` में हैं।

2. **प्रोग्राम चलाएँ**
   क्लास फ़ाइल वाली डायरेक्टरी को इंगित करने के लिए `-cp` विकल्प का उपयोग करें:
   ```bash
   java -cp scripts/benchmark MultiMark
   ```
   - `-cp scripts/benchmark` Java को `scripts/benchmark` डायरेक्टरी में classes ढूंढने के लिए कहता है।
   - `MultiMark` क्लास का नाम है (`.class` या पैकेज उपसर्ग के बिना, क्योंकि `MultiMark.java` में कोई `package` स्टेटमेंट नहीं है)।

   इससे इस तरह का आउटपुट मिलना चाहिए:
   ```
   CPU cores: 32
   ...
   ```

3. **नोट**: यदि `MultiMark.class` पुरानी है या गायब है, तो पहले रूट डायरेक्टरी से सोर्स फ़ाइल को compile करें:
   ```bash
   javac scripts/benchmark/MultiMark.java
   ```
   फिर ऊपर दिया गया कमांड चलाएँ।

---

### **विकल्प 2: Classpath के साथ सीधे सोर्स फ़ाइल चलाएँ (Java 11+)**
यदि आप सीधे सोर्स फ़ाइल चलाना पसंद करते हैं (जैसे `python script.py`), तो आप classpath निर्दिष्ट करते हुए, सोर्स फ़ाइल पथ के साथ `java` कमांड का उपयोग कर सकते हैं।

1. **रूट डायरेक्टरी में रहें**
   सुनिश्चित करें कि आप `~/projects/lzwjava.github.io` में हैं।

2. **सोर्स फ़ाइल चलाएँ**
   इसका उपयोग करें:
   ```bash
   java -cp scripts/benchmark scripts/benchmark/MultiMark.java
   ```
   - `-cp scripts/benchmark` classpath को उस डायरेक्टरी पर सेट करता है जहाँ सोर्स है।
   - `scripts/benchmark/MultiMark.java` compile और run करने के लिए सोर्स फ़ाइल को निर्दिष्ट करता है।

   यह `MultiMark.java` को एक ही चरण में compile और run कर देता है, और पहले जैसा ही आउटपुट देता है।

---

### **विकल्प 3: रूट डायरेक्टरी में एक Shell Script बनाएँ**
इसे और भी सुविधाजनक बनाने के लिए (जैसे रूट डायरेक्टरी से `./multimark` चलाना), आप रूट डायरेक्टरी (`~/projects/lzwjava.github.io`) में एक shell script बना सकते हैं।

1. **एक Shell Script बनाएँ**
   रूट डायरेक्टरी में `multimark` नाम की एक फ़ाइल बनाएँ:
   ```bash
   nano multimark
   ```
   इसमें जोड़ें:
   ```bash
   #!/bin/bash
   java -cp scripts/benchmark MultiMark
   ```
   सेव करें और बाहर निकलें।

2. **इसे Executable बनाएँ**
   ```bash
   chmod +x multimark
   ```

3. **Script चलाएँ**
   रूट डायरेक्टरी से:
   ```bash
   ./multimark
   ```
   यह Java प्रोग्राम को बिना डायरेक्टरी बदले चला देगा।

4. **वैकल्पिक: Script में Compile करें**
   यदि आप चाहते हैं कि script compilation को संभाले (उदाहरण के लिए, यदि सोर्स फ़ाइल बदल गई है), तो script को इस तरह संशोधित करें:
   ```bash
   #!/bin/bash
   javac scripts/benchmark/MultiMark.java
   java -cp scripts/benchmark MultiMark
   ```

---

### **मुख्य नोट्स**
- **Classpath (`-cp`)**: `-cp` विकल्प Java को बताता है कि classes या सोर्स फ़ाइलें कहाँ मिलेंगी। चूंकि `MultiMark.java` में कोई `package` स्टेटमेंट नहीं है, इसलिए क्लास का नाम केवल `MultiMark` है, `scripts.benchmark.MultiMark` नहीं। यदि इसमें `package scripts.benchmark;` लाइन होती, तो आपको रूट से `java -cp . scripts.benchmark.MultiMark` का उपयोग करने की आवश्यकता होती।
- **Java Version**: सोर्स-फ़ाइल execution (`java scripts/benchmark/MultiMark.java`) के लिए Java 11 या बाद का संस्करण चाहिए। आपके सिस्टम में Java इंस्टॉल लगता है, क्योंकि यह `scripts/benchmark` डायरेक्टरी से काम कर गया था।
- **डायरेक्टरी**: ये समाधान आपको रूट डायरेक्टरी (`~/projects/lzwjava.github.io`) में रखते हैं, जो आपकी पसंद से मेल खाता है।
- **ऑटोमेशन**: Shell script (विकल्प 3) Python जैसे अनुभव के सबसे करीब है, क्योंकि आप इसे Python script की तरह `./multimark` चला सकते हैं। आप इसे वैश्विक पहुँच के लिए अपने `PATH` में भी जोड़ सकते हैं, लेकिन यह वैकल्पिक है।
- **त्रुटि प्रबंधन**: यदि आपको `NoClassDefFoundError` जैसी त्रुटियाँ मिलती हैं, तो सुनिश्चित करें कि `MultiMark.class` `scripts/benchmark/` में मौजूद है या फिर से compile करें। यदि Java नहीं मिलता है, तो इंस्टॉलेशन सत्यापित करें (`java --version`)।

यदि आप इसे अपनी Python scripts के साथ एकीकृत करना चाहते हैं या किसी विशिष्ट वर्कफ़्लो (जैसे `multimark.py` और `MultiMark.java` को एक साथ चलाना) की आवश्यकता है, तो मुझे बताएं!