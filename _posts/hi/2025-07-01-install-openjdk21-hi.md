---
audio: false
generated: true
lang: hi
layout: post
title: मैकओएस पर ओपनजेडीके 21 में अपग्रेड करें
translated: true
type: note
---

चूंकि आपके macOS सिस्टम पर वर्तमान में Homebrew के माध्यम से OpenJDK 17 इंस्टॉल है, यहाँ OpenJDK 21 इंस्टॉल करने का एक संक्षिप्त गाइड दिया गया है, जो आपकी वर्तमान तिथि, 1 जुलाई, 2025 तक नवीनतम Long Term Support (LTS) रिलीज़ है। आप OpenJDK 21 को OpenJDK 17 के साथ-साथ इंस्टॉल कर सकते हैं और आवश्यकतानुसार उनके बीच स्विच कर सकते हैं। सबसे सरल तरीका Homebrew का उपयोग करना है, लेकिन मैं एक मैन्युअल इंस्टॉलेशन विकल्प भी प्रदान करूंगा।

### विधि 1: Homebrew का उपयोग करके OpenJDK 21 इंस्टॉल करें (सुझाया गया)
आपके सिस्टम पर Homebrew पहले से ही इंस्टॉल है, जैसा कि आपके वर्तमान Java वर्जन से पता चलता है। यह सबसे आसान और रखरखाव योग्य तरीका है।

1. **Homebrew अपडेट करें**:
   नवीनतम पैकेज प्राप्त करने के लिए सुनिश्चित करें कि Homebrew अप-टू-डेट है:
   ```bash
   brew update
   ```

2. **OpenJDK 21 इंस्टॉल करें**:
   Homebrew OpenJDK 21 के लिए एक विशिष्ट फॉर्मूला प्रदान करता है। निम्नलिखित कमांड चलाएँ:
   ```bash
   brew install openjdk@21
   ```
   यह OpenJDK 21 को एक keg-only तरीके से इंस्टॉल करता है, मतलब यह अन्य Java वर्जन के साथ टकराव से बचने के लिए `/usr/local/bin` में symlink नहीं किया जाएगा।

3. **अपने PATH में OpenJDK 21 जोड़ें**:
   OpenJDK 21 का उपयोग करने के लिए, आपको इसे अपने सिस्टम के PATH में जोड़ने की आवश्यकता है। इंस्टॉलेशन के बाद Homebrew निर्देश प्रदान करेगा, लेकिन आम तौर पर, आप इसे अस्थायी या स्थायी रूप से लिंक कर सकते हैं:
   - **अस्थायी (वर्तमान सत्र के लिए)**:
     ```bash
     export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
     ```
   - **स्थायी (शेल कॉन्फ़िगरेशन में जोड़ें)**:
     अपनी शेल कॉन्फ़िगरेशन फ़ाइल खोलें (संभावित रूप से `~/.zshrc` क्योंकि macOS डिफ़ॉल्ट रूप से Zsh का उपयोग करता है):
     ```bash
     nano ~/.zshrc
     ```
     निम्नलिखित लाइन जोड़ें:
     ```bash
     export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"
     ```
     फ़ाइल सेव करें और बंद करें, फिर परिवर्तन लागू करें:
     ```bash
     source ~/.zshrc
     ```

4. **JAVA_HOME सेट करें**:
   यह सुनिश्चित करने के लिए कि Java एप्लिकेशन OpenJDK 21 का पता लगा सकें, `JAVA_HOME` एनवायरनमेंट वेरिएबल सेट करें:
   ```bash
   export JAVA_HOME=$(/usr/libexec/java_home -v 21)
   ```
   इसे अपने `~/.zshrc` में स्थायी रूप से जोड़ें:
   ```bash
   echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 21)' >> ~/.zshrc
   source ~/.zshrc
   ```

5. **इंस्टॉलेशन सत्यापित करें**:
   जाँचें कि OpenJDK 21 इंस्टॉल और सक्रिय है:
   ```bash
   java -version
   ```
   आपको इसके जैसा आउटपुट दिखना चाहिए:
   ```
   openjdk 21.0.1 2023-10-17
   OpenJDK Runtime Environment (build 21.0.1+12)
   OpenJDK 64-Bit Server VM (build 21.0.1+12, mixed mode, sharing)
   ```

6. **Java वर्जन के बीच स्विच करना**:
   चूंकि आपके पास OpenJDK 17 इंस्टॉल है, आप `/usr/libexec/java_home` का उपयोग करके वर्जन के बीच स्विच कर सकते हैं। उदाहरण के लिए:
   - OpenJDK 17 का उपयोग करने के लिए:
     ```bash
     export JAVA_HOME=$(/usr/libexec/java_home -v 17)
     ```
   - OpenJDK 21 का उपयोग करने के लिए:
     ```bash
     export JAVA_HOME=$(/usr/libexec/java_home -v 21)
     ```
   वैकल्पिक रूप से, आसान स्विचिंग के लिए `jenv` जैसे वर्जन मैनेजर का उपयोग करने पर विचार करें (`brew install jenv` के माध्यम से इंस्टॉल करें):
   ```bash
   jenv add /Library/Java/JavaVirtualMachines/openjdk-21.jdk/Contents/Home
   jenv add /Library/Java/JavaVirtualMachines/openjdk-17.jdk/Contents/Home
   jenv enable-plugin export
   jenv global 21
   ```

### विधि 2: मैन्युअल इंस्टॉलेशन
यदि आप Homebrew का उपयोग नहीं करना चाहते हैं, तो आप मैन्युअल रूप से OpenJDK 21 इंस्टॉल कर सकते हैं।

1. **OpenJDK 21 डाउनलोड करें**:
   - आधिकारिक OpenJDK वेबसाइट (jdk.java.net/21) या Oracle, Azul, या Adoptium जैसे किसी विश्वसनीय प्रदाता पर जाएँ।
   - Apple Silicon (M1/M2) के लिए, `macOS/AArch64` tar.gz फ़ाइल डाउनलोड करें। Intel-आधारित Macs के लिए, `macOS/x64` चुनें।
   - उदाहरण: Oracle के JDK 21 डाउनलोड पेज से, ARM64 या x64 tar.gz फ़ाइल चुनें।

2. **डाउनलोड सत्यापित करें**:
   डाउनलोड की गई फ़ाइल की अखंडता उसके SHA256 चेकसम का उपयोग करके जाँचें:
   ```bash
   shasum -a 256 openjdk-21.0.1_macos-aarch64_bin.tar.gz
   ```
   आउटपुट की तुलना डाउनलोड पेज पर प्रदान किए गए चेकसम से करें।

3. **फ़ाइल एक्सट्रैक्ट करें**:
   tar.gz फ़ाइल को वांछित डायरेक्टरी में एक्सट्रैक्ट करें, जैसे आपकी होम डायरेक्टरी:
   ```bash
   tar -xf openjdk-21.0.1_macos-aarch64_bin.tar.gz -C ~/OpenJDK
   ```
   JDK, `~/OpenJDK/jdk-21.0.1.jdk/Contents/Home` में एक्सट्रैक्ट हो जाएगी।

4. **सिस्टम डायरेक्टरी में ले जाएँ** (वैकल्पिक):
   स्थिरता के लिए, आप JDK को मानक macOS Java डायरेक्टरी में ले जा सकते हैं:
   ```bash
   sudo mv ~/OpenJDK/jdk-21.0.1.jdk /Library/Java/JavaVirtualMachines/
   ```

5. **JAVA_HOME और PATH सेट करें**:
   अपने `~/.zshrc` को अपडेट करें ताकि इसमें शामिल हो:
   ```bash
   export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-21.0.1.jdk/Contents/Home
   export PATH=$JAVA_HOME/bin:$PATH
   ```
   परिवर्तन लागू करें:
   ```bash
   source ~/.zshrc
   ```

6. **इंस्टॉलेशन सत्यापित करें**:
   इंस्टॉलेशन की पुष्टि करें:
   ```bash
   java -version
   ```
   सुनिश्चित करें कि यह OpenJDK 21 दिखाता है।

### नोट्स
- **Apple Silicon संगतता**: परफॉर्मेंस समस्याओं से बचने के लिए M1/M2 Macs के लिए AArch64 बिल्ड डाउनलोड करना सुनिश्चित करें। Homebrew स्वचालित रूप से सही आर्किटेक्चर का चयन करता है।
- **एकाधिक JDKs**: macOS `/Library/Java/JavaVirtualMachines/` में एकाधिक JDKs को सपोर्ट करता है। उनके बीच स्विच करने के लिए `/usr/libexec/java_home -v <version>` का उपयोग करें।
- **Homebrew लाभ**: Homebrew अपडेट (`brew upgrade openjdk@21`) को सरल बनाता है और आपके सिस्टम के साथ संगतता सुनिश्चित करता है।
- **वैकल्पिक प्रदाता**: आप OpenJDK 21 के Azul Zulu या Eclipse Temurin बिल्ड का भी उपयोग कर सकते हैं, जो उनकी संबंधित वेबसाइटों (जैसे azul.com या adoptium.net) से उपलब्ध हैं।

यदि आपको कोई समस्या आती है, तो मुझे बताएं, और मैं समस्या निवारण में मदद कर सकता हूँ।