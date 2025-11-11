---
audio: false
generated: true
lang: hi
layout: post
title: वीएसकोड में ग्रेडल के लिए प्रॉक्सी कॉन्फ़िगर करें
translated: true
type: note
---

Gradle के लिए Visual Studio Code (VSCode) में प्रॉक्सी कॉन्फ़िगर करने के लिए ताकि यह प्रॉक्सी के माध्यम से डिपेंडेंसीज़ डाउनलोड कर सके, आपको Gradle के कॉन्फ़िगरेशन में प्रॉक्सी सेटिंग्स सेट करनी होंगी। Gradle ऐसी सेटिंग्स को प्रबंधित करने के लिए एक प्रॉपर्टीज़ फ़ाइल का उपयोग करता है, और VSCode Gradle प्रोजेक्ट्स के लिए Gradle की बिल्ड सिस्टम पर निर्भर करता है। यहां बताया गया है कि आप इसे कैसे कर सकते हैं:

### VSCode में Gradle के लिए प्रॉक्सी कॉन्फ़िगर करने के चरण

1. **Gradle प्रॉपर्टीज़ फ़ाइल का पता लगाएं या बनाएं**
   - Gradle ग्लोबल कॉन्फ़िगरेशन सेटिंग्स को स्टोर करने के लिए `gradle.properties` नामक फ़ाइल का उपयोग करता है।
   - यह फ़ाइल आमतौर पर Gradle यूज़र होम डायरेक्टरी में स्थित होती है:
     - Windows पर: `C:\Users\<आपका यूज़रनेम>\.gradle\gradle.properties`
     - macOS/Linux पर: `~/.gradle/gradle.properties`
   - यदि फ़ाइल मौजूद नहीं है, तो उपरोक्त स्थान पर इसे बनाएं।

2. **`gradle.properties` में प्रॉक्सी सेटिंग्स जोड़ें**
   - `gradle.properties` फ़ाइल को एक टेक्स्ट एडिटर में खोलें।
   - निम्नलिखित लाइनें जोड़ें, प्लेसहोल्डर्स (`<proxyHost>`, `<proxyPort>`, `<username>`, `<password>`) को अपनी वास्तविक प्रॉक्सी जानकारी से बदलकर:
     ```
     systemProp.http.proxyHost=<proxyHost>
     systemProp.http.proxyPort=<proxyPort>
     systemProp.http.proxyUser=<username>
     systemProp.http.proxyPassword=<password>
     systemProp.https.proxyHost=<proxyHost>
     systemProp.https.proxyPort=<proxyPort>
     systemProp.https.proxyUser=<username>
     systemProp.https.proxyPassword=<password>
     ```
   - वास्तविक मानों के साथ उदाहरण:
     ```
     systemProp.http.proxyHost=proxy.example.com
     systemProp.http.proxyPort=8080
     systemProp.http.proxyUser=myuser
     systemProp.http.proxyPassword=mypassword
     systemProp.https.proxyHost=proxy.example.com
     systemProp.https.proxyPort=8080
     systemProp.https.proxyUser=myuser
     systemProp.https.proxyPassword=mypassword
     ```
   - यदि आपके प्रॉक्सी को प्रमाणीकरण (यूज़रनेम/पासवर्ड) की आवश्यकता नहीं है, तो आप `proxyUser` और `proxyPassword` लाइनों को छोड़ सकते हैं।

3. **वैकल्पिक: प्रति प्रोजेक्ट प्रॉक्सी कॉन्फ़िगर करें**
   - यदि आप चाहते हैं कि प्रॉक्सी सेटिंग्स केवल किसी विशिष्ट प्रोजेक्ट पर लागू हों (ग्लोबली के बजाय), तो आप `gradle.properties` फ़ाइल को अपनी प्रोजेक्ट की रूट डायरेक्टरी (जैसे, `<project-root>/gradle.properties`) में उपरोक्त समान कंटेंट के साथ जोड़ सकते हैं।

4. **सत्यापित करें कि Gradle प्रॉक्सी का उपयोग कर रहा है**
   - अपने Gradle प्रोजेक्ट को VSCode में खोलें।
   - VSCode टर्मिनल या Gradle एक्सटेंशन के माध्यम से एक बिल्ड टास्क (जैसे, `gradle build`) चलाएं।
   - Gradle को अब अपनी डाउनलोड (जैसे ऑफिशियल साइट से डिपेंडेंसीज़) निर्दिष्ट प्रॉक्सी के माध्यम से रूट करनी चाहिए।

5. **VSCode-विशिष्ट नोट्स**
   - सुनिश्चित करें कि VSCode में **Java Extension Pack** और **Gradle for Java** एक्सटेंशन इंस्टॉल हैं, क्योंकि ये Gradle प्रोजेक्ट सपोर्ट को बेहतर बनाते हैं।
   - यदि VSCode को अभी भी समस्या हो रही है, तो जांचें कि आपका Java रनटाइम (जिसका उपयोग Gradle करता है) भी प्रॉक्सी का सम्मान करता है। आपको JVM प्रॉक्सी आर्ग्युमेंट्स सेट करने की आवश्यकता हो सकती है:
     - VSCode में, `File > Preferences > Settings` पर जाएं।
     - `java.gradle.build.jvmArguments` खोजें।
     - कुछ इस तरह जोड़ें:
       ```
       -Dhttp.proxyHost=<proxyHost> -Dhttp.proxyPort=<proxyPort> -Dhttps.proxyHost=<proxyHost> -Dhttps.proxyPort=<proxyPort>
       ```

6. **कॉन्फ़िगरेशन का परीक्षण करें**
   - अपने प्रोजेक्ट को VSCode में रीलोड करें (जैसे, इसे बंद करके फिर से खोलें या Gradle साइडबार में "Refresh" बटन का उपयोग करें)।
   - यह पुष्टि करने के लिए कि यह फ़ाइलों को प्रॉक्सी के माध्यम से डाउनलोड करता है, एक Gradle टास्क (जैसे, `gradle build` या `gradle dependencies`) चलाएं।

### समस्या निवारण
- **प्रॉक्सी विवरण जांचें**: सुनिश्चित करें कि आपका प्रॉक्सी होस्ट, पोर्ट और क्रेडेंशियल्स सही हैं।
- **फ़ायरवॉल या नेटवर्क**: यदि यह अभी भी विफल होता है, तो आपका प्रॉक्सी या नेटवर्क विशिष्ट Gradle URL (जैसे, `https://services.gradle.org`) को ब्लॉक कर सकता है। `curl` जैसे कमांड के साथ परीक्षण करें या अपने नेटवर्क एडमिन से परामर्श लें।
- **वर्बोज़ आउटपुट**: नेटवर्क अनुरोधों के बारे में विस्तृत लॉग देखने के लिए VSCode टर्मिनल में `--debug` या `--info` (जैसे, `gradle build --debug`) के साथ Gradle चलाएं।

यह सेटअप VSCode में Gradle को आपके प्रॉक्सी के माध्यम से सफलतापूर्वक डिपेंडेंसीज़ डाउनलोड करने में सक्षम बनाना चाहिए। यदि आपको कोई समस्या आती है तो मुझे बताएं!