---
audio: false
generated: true
lang: hi
layout: post
title: विजुअलवीएम में 'असमर्थित ओपनजेडीके' त्रुटि को ठीक करना
translated: true
type: note
---

VisualVM चलाते समय "Version of OpenJDK is not supported. Please use the default-jdk" त्रुटि इंगित करती है कि उपयोग किया जा रहा Java Development Kit (JDK) संस्करण VisualVM के साथ संगत नहीं है। यह समस्या आमतौर पर तब होती है जब VisualVM कोई समर्थित JDK नहीं ढूंढ पाता या जब इंस्टॉल किया गया JDK ठीक से कॉन्फ़िगर नहीं होता है। नीचे आपके सेटअप (YourKit Java Profiler 2025.3 और VisualVM जो कि एक Linux सिस्टम पर प्रतीत हो रहा है) के संदर्भ में इस समस्या को हल करने के चरण दिए गए हैं।

### समस्या ठीक करने के चरण

1. **अपने वर्तमान Java संस्करण की जाँच करें**
   इंस्टॉल किए गए Java संस्करण को सत्यापित करने के लिए निम्न कमांड चलाएँ:
   ```bash
   java -version
   ```
   यह OpenJDK संस्करण प्रदर्शित करेगा, जैसे:
   ```
   openjdk version "17.0.9" 2023-10-17
   OpenJDK Runtime Environment (build 17.0.9+9-Ubuntu-122.04)
   OpenJDK 64-Bit Server VM (build 17.0.9+9-Ubuntu-122.04, mixed mode, sharing)
   ```
   VisualVM को आमतौर पर एक JDK (सिर्फ JRE नहीं) की आवश्यकता होती है और यह Oracle JDK 8+ या संगत OpenJDK संस्करणों को सपोर्ट करता है। सुनिश्चित करें कि आपके पास एक समर्थित JDK इंस्टॉल है।[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://visualvm.github.io/troubleshooting.html)

2. **डिफ़ॉल्ट JDK इंस्टॉल करें**
   त्रुटि `default-jdk` के उपयोग का सुझाव देती है। Ubuntu/Debian पर, आप इसे इंस्टॉल कर सकते हैं:
   ```bash
   sudo apt update
   sudo apt install default-jdk
   ```
   यह आमतौर पर एक स्थिर, समर्थित OpenJDK संस्करण (जैसे, OpenJDK 11 या 17) इंस्टॉल करता है। इंस्टॉलेशन के बाद, `java -version` के साथ संस्करण को फिर से सत्यापित करें।[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

3. **JAVA_HOME एनविरोंमेंट वेरिएबल सेट करें**
   VisualVM JDK का पता लगाने के लिए `JAVA_HOME` एनविरोंमेंट वेरिएबल पर निर्भर करता है। जाँचें कि क्या यह सेट है:
   ```bash
   echo $JAVA_HOME
   ```
   यदि यह सेट नहीं है या किसी असमर्थित JDK की ओर इशारा करता है, तो इसे सही JDK पथ पर सेट करें। उदाहरण के लिए, यदि `default-jdk` ने OpenJDK 17 इंस्टॉल किया है, तो पथ `/usr/lib/jvm/java-17-openjdk-amd64` हो सकता है। इसे सेट करें:
   ```bash
   export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
   ```
   इसे स्थायी बनाने के लिए, इस लाइन को अपने `~/.bashrc` या `~/.zshrc` में जोड़ें:
   ```bash
   echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc
   source ~/.bashrc
   ```
   पथ को अपने सिस्टम पर वास्तविक JDK पथ से बदलें (इसे ढूंढने के लिए `update-alternatives --list java` का उपयोग करें)।[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)[](https://github.com/oracle/visualvm/issues/558)

4. **VisualVM के लिए JDK पथ निर्दिष्ट करें**
   यदि `JAVA_HOME` सेट करने से समस्या हल नहीं होती है, तो आप VisualVM लॉन्च करते समय स्पष्ट रूप से JDK पथ निर्दिष्ट कर सकते हैं:
   ```bash
   ~/bin/YourKit-JavaProfiler-2025.3/bin/visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64
   ```
   `/usr/lib/jvm/java-17-openjdk-amd64` को अपने JDK के पथ से बदलें। यह सुनिश्चित करता है कि VisualVM निर्दिष्ट JDK का उपयोग करता है।[](https://visualvm.github.io/download.html)[](https://notepad.onghu.com/2021/solve-visualvm-does-not-start-on-windows-openjdk/)

5. **एक संगत JDK इंस्टॉल करें**
   यदि `default-jdk` अभी भी असंगत है, तो VisualVM के साथ काम करने वाले किसी विशिष्ट JDK संस्करण, जैसे OpenJDK 11 या Oracle JDK 8+, को इंस्टॉल करने पर विचार करें:
   ```bash
   sudo apt install openjdk-11-jdk
   ```
   फिर, `JAVA_HOME` अपडेट करें या ऊपर बताए अनुसार `--jdkhome` विकल्प का उपयोग करें।[](https://stackoverflow.com/questions/78019430/visualvm-version-of-openjdk-is-not-supported)

6. **VisualVM इंस्टॉलेशन की जाँच करें**
   सुनिश्चित करें कि VisualVM सही ढंग से इंस्टॉल है। त्रुटि बताती है कि आप VisualVM को YourKit Java Profiler डायरेक्टरी (`~/bin/YourKit-JavaProfiler-2025.3/bin`) से चला रहे हैं। यह असामान्य है, क्योंकि VisualVM आमतौर पर एक स्टैंडअलोन टूल होता है या JDK के साथ बंडल होता है। सत्यापित करें कि VisualVM खराब तो नहीं है:
   - `visualvm.github.io/download.html` से नवीनतम VisualVM रिलीज़ डाउनलोड करें (जैसे, VisualVM 2.2, रिलीज़्ड April 22, 2025, JDK 24 को सपोर्ट करता है)।[](https://visualvm.github.io/relnotes.html)[](https://visualvm.github.io/)
   - इसे एक नई डायरेक्टरी में अनज़िप करें और चलाएँ:
     ```bash
     unzip visualvm_22.zip
     cd visualvm_22/bin
     ./visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64
     ```
   मौजूदा VisualVM इंस्टॉलेशन पर अनज़िप करने से बचें, क्योंकि इससे समस्याएँ हो सकती हैं।[](https://visualvm.github.io/troubleshooting.html)

7. **एकाधिक Java इंस्टॉलेशन के लिए जाँच करें**
   एकाधिक Java संस्करण संघर्ष पैदा कर सकते हैं। सभी इंस्टॉल किए गए Java संस्करणों की सूची बनाएँ:
   ```bash
   update-alternatives --list java
   ```
   यदि एकाधिक संस्करण सूचीबद्ध हैं, तो वांछित एक को डिफ़ॉल्ट के रूप में सेट करें:
   ```bash
   sudo update-alternatives --config java
   ```
   संगत JDK (जैसे, OpenJDK 11 या 17) के अनुरूप नंबर का चयन करें।[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

8. **VisualVM डिपेंडेंसीज़ सत्यापित करें**
   VisualVM को `libnb-platform18-java` और `libvisualvm-jni` की आवश्यकता होती है। सुनिश्चित करें कि ये इंस्टॉल हैं:
   ```bash
   sudo apt install libnb-platform18-java libvisualvm-jni
   ```
   यह विशेष रूप से प्रासंगिक है यदि आपने VisualVM को `apt` के माध्यम से इंस्टॉल किया है।[](https://askubuntu.com/questions/1504020/visualvm-version-of-openjdk-is-not-supported)

9. **OpenJDK प्रतिबंधों को बायपास करें (वैकल्पिक)**
   यदि आप किसी असमर्थित OpenJDK बिल्ड (जैसे, IcedTea या AdoptOpenJDK) का उपयोग कर रहे हैं, तो प्रोफाइलिंग फीचर्स सीमित हो सकते हैं। आप एक कमांड-लाइन आर्ग्युमेंट जोड़कर कुछ प्रतिबंधों को बायपास कर सकते हैं:
   ```bash
   ./visualvm --jdkhome /usr/lib/jvm/java-17-openjdk-amd64 -J-Dorg.graalvm.visualvm.profiler.SupportAllVMs=true
   ```
   यह असमर्थित JVMs के लिए प्रोफाइलिंग सक्षम करता है, हालाँकि यह पूरी तरह से काम करने की गारंटी नहीं है।[](https://github.com/oracle/visualvm/issues/143)

10. **YourKit और VisualVM संगतता की जाँच करें**
    चूंकि आप VisualVM को YourKit Java Profiler डायरेक्टरी से चला रहे हैं, सुनिश्चित करें कि YourKit का एनवायरनमेंट हस्तक्षेप नहीं कर रहा है। YourKit Java Profiler 2025.3 किसी विशिष्ट VisualVM संस्करण या कॉन्फ़िगरेशन को बंडल कर सकता है। अपने JDK के साथ संगतता की पुष्टि करने के लिए YourKit की डॉक्यूमेंटेशन देखें या `support@yourkit.com` से संपर्क करें। वैकल्पिक रूप से, समस्या को अलग करने के लिए स्वतंत्र रूप से (अलग से डाउनलोड किया गया) VisualVM चलाने का प्रयास करें।[](https://www.yourkit.com/changes/)

### अतिरिक्त नोट्स
- **YourKit संदर्भ**: त्रुटि सीधे तौर पर YourKit Java Profiler से संबंधित नहीं है, लेकिन YourKit की डायरेक्टरी से VisualVM चलाना एकीकरण का सुझाव देता है। YourKit Java 7–15 और बाद के संस्करणों को EAP बिल्ड्स के साथ सपोर्ट करता है, इसलिए सुनिश्चित करें कि आपका JDK दोनों टूल्स के साथ संगत है यदि उनका एक साथ उपयोग किया जाता है।[](https://www.yourkit.com/forum/viewtopic.php?t=41723)[](https://www.yourkit.com/forum/viewtopic.php?t=40299)
- **लॉग फाइलें**: अधिक जानकारी के लिए VisualVM लॉग्स की जाँच करें। लॉग आमतौर पर `~/.visualvm/<version>/var/log` में होते हैं। YourKit के लिए, प्रोफाइलर एजेंट लॉग के लिए `~/.yjp/log/` देखें। यदि समस्याएँ बनी रहती हैं, तो लॉग `support@yourkit.com` पर भेजें।[](https://stackoverflow.com/questions/70211315/java-17-and-yourkit-2021-11)[](https://www.yourkit.com/forum/viewtopic.php?t=40299)
- **विकल्प**: यदि VisualVM लगातार विफल रहता है, तो YourKit के बिल्ट-इन प्रोफाइलिंग टूल्स या किसी अन्य प्रोफाइलर जैसे JProfiler या Async Profiler का उपयोग करने पर विचार करें, जिनकी आपके सेटअप के साथ बेहतर संगतता हो सकती है।[](https://digma.ai/9-best-java-profilers-to-use-in-2024/)[](https://bell-sw.com/blog/a-guide-to-java-profiling-tools-techniques-best-practices/)

### यदि समस्या बनी रहती है
यदि उपरोक्त में से कोई भी समस्या का समाधान नहीं करता है, तो कृपया प्रदान करें:
- `java -version` और `echo $JAVA_HOME` का आउटपुट।
- `update-alternatives --list java` का आउटपुट।
- सटीक VisualVM संस्करण (`visualvm --help` या डाउनलोड पेज के माध्यम से जाँचें)।
- क्या आप YourKit के साथ बंडल किए गए VisualVM या स्टैंडअलोन इंस्टॉलेशन का उपयोग कर रहे हैं।

यह समस्या को और सटीक रूप से पहचानने में मदद करेगा। आप विशिष्ट मार्गदर्शन के लिए समस्या को VisualVM GitHub पेज (`https://github.com/oracle/visualvm`) या YourKit सपोर्ट पर भी रिपोर्ट कर सकते हैं।[](https://github.com/oracle/visualvm/issues/558)