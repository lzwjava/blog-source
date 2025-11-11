---
audio: false
generated: true
lang: hi
layout: post
title: इंटेलिजे आईडीईए में गैर-विश्वसनीय प्रमाणपत्रों का प्रबंधन
translated: true
type: note
---

IntelliJ IDEA में "अनट्रस्टेड सर्वर का सर्टिफिकेट" डायलॉग तब दिखाई देता है जब IDE को SSL सर्टिफिकेट मिलते हैं जो इसके कीस्टोर द्वारा विश्वसनीय नहीं हैं, जैसे कि सेल्फ-साइन्ड या कस्टम कॉर्पोरेट सर्टिफिकेट। चूंकि आपने पहले ही अपने कॉर्पोरेट कीस्टोर को `/lib/cacerts` में इम्पोर्ट कर लिया है लेकिन फिर भी प्रॉम्प्ट दिख रहा है, तो समस्या यह हो सकती है कि IntelliJ उस कीस्टोर का उपयोग नहीं कर रहा है या अतिरिक्त सर्टिफिकेट डायलॉग का कारण बन रहे हैं। यहां बताया गया है कि इसे कैसे ठीक करें और संभावित रूप से प्रॉम्प्ट्स को कैसे रोकें:

### विकल्प 1: IntelliJ को गैर-विश्वसनीय सर्टिफिकेट स्वचालित रूप से स्वीकार करने के लिए कॉन्फ़िगर करें
इस विकल्प को सक्षम करने से IntelliJ अनट्रस्टेड सर्टिफिकेट के लिए डायलॉग को बायपास कर देगा, लेकिन सावधान रहें क्योंकि यह सभी सर्टिफिकेट स्वीकार करके सुरक्षा को कम करता है, जिससे आप मैन-इन-द-मिडिल अटैक के संपर्क में आ सकते हैं।

- **Windows/Linux**:
  1. `File > Settings > Tools > Server Certificates` पर जाएं।
  2. **"Accept non-trusted certificates automatically"** के लिए बॉक्स को चेक करें।
  3. **Apply** और **OK** पर क्लिक करें।
- **macOS**:
  1. `IntelliJ IDEA > Preferences > Tools > Server Certificates` पर जाएं।
  2. **"Accept non-trusted certificates automatically"** को चेक करें।
  3. **Apply** और **OK** पर क्लिक करें।[](https://stackoverflow.com/questions/60092405/untrusted-server-certificate-in-intellij)[](https://www.javahelps.com/2020/12/things-to-do-after-installing-intellij.html)

**नोट**: यह अनुशंसित नहीं है जब तक कि आप किसी विश्वसनीय, आइसोलेटेड नेटवर्क (जैसे एयर-गैप्ड कॉर्पोरेट वातावरण) में न हों, क्योंकि यह आपके IDE को अनवेरीफाइड कनेक्शन के प्रति संवेदनशील बना सकता है।[](https://stackoverflow.com/questions/60092405/untrusted-server-certificate-in-intellij)

### विकल्प 2: कीस्टोर कॉन्फ़िगरेशन को सत्यापित और सही करें
चूंकि आपने कॉर्पोरेट कीस्टोर को `/lib/cacerts` में इम्पोर्ट कर दिया है, सुनिश्चित करें कि IntelliJ इसका सही ढंग से उपयोग कर रहा है। समस्या यह हो सकती है कि IntelliJ अभी भी अपने स्वयं के ट्रस्टस्टोर या गलत cacerts फ़ाइल का उपयोग कर रहा है।

1. **कीस्टोर पथ की जांच करें**:
   - IntelliJ अक्सर अपने स्वयं के ट्रस्टस्टोर का उपयोग करता है जो `~/.IntelliJIdea<version>/system/tasks/cacerts` पर होता है या JetBrains Runtime (JBR) ट्रस्टस्टोर का उपयोग करता है जो `<IntelliJ Installation>/jbr/lib/security/cacerts` पर होता है।[](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360004301319-Adding-root-CA-to-intellij-on-Windows-10)
   - यदि आपने IntelliJ डायरेक्टरी में `/lib/cacerts` को संशोधित किया है, तो पुष्टि करें कि यह आपके IDE वर्जन के लिए सही पथ है। JetBrains Toolbox इंस्टॉलेशन के लिए, पथ अलग हो सकता है (उदाहरण के लिए, Windows पर `~/AppData/Local/JetBrains/Toolbox/apps/IDEA-U/ch-0/<version>/jbr/lib/security/cacerts`)।[](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360004301319-Adding-root-CA-to-intellij-on-Windows-10)
   - यह सत्यापित करने के लिए कि सर्टिफिकेट cacerts फ़ाइल में है, `keytool` कमांड का उपयोग करें:
     ```bash
     keytool -list -keystore <path-to-cacerts> -storepass changeit
     ```
     सुनिश्चित करें कि आपका कॉर्पोरेट CA सर्टिफिकेट सूचीबद्ध है।

2. **IntelliJ को कस्टम कीस्टोर की ओर इंगित करें**:
   - यदि सर्टिफिकेट सही ढंग से इम्पोर्ट किया गया है लेकिन IntelliJ फिर भी प्रॉम्प्ट करता है, तो यह संशोधित cacerts का उपयोग नहीं कर रहा हो सकता है। ट्रस्टस्टोर निर्दिष्ट करने के लिए एक कस्टम VM विकल्प जोड़ें:
     1. `Help > Edit Custom VM Options` पर जाएं।
     2. जोड़ें:
        ```
        -Djavax.net.ssl.trustStore=<path-to-cacerts>
        -Djavax.net.ssl.trustStorePassword=changeit
        ```
        `<path-to-cacerts>` को अपनी संशोधित `cacerts` फ़ाइल के पूर्ण पथ से बदलें।[](https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000080810-Setting-Truststore-)
     3. IntelliJ IDEA को रीस्टार्ट करें।

3. **सर्टिफिकेट को दोबारा इम्पोर्ट करें**:
   - यदि सर्टिफिकेट इम्पोर्ट अधूरा या गलत था, तो इसे दोबारा इम्पोर्ट करें:
     ```bash
     keytool -import -trustcacerts -file <certificate-file>.cer -alias <alias> -keystore <path-to-cacerts> -storepass changeit
     ```
     `<certificate-file>.cer` को अपने कॉर्पोरेट CA सर्टिफिकेट से और `<path-to-cacerts>` को सही cacerts फ़ाइल पथ से बदलें।[](https://www.baeldung.com/jvm-certificate-store-errors)

### विकल्प 3: IntelliJ के सर्वर सर्टिफिकेट सेटिंग्स के माध्यम से सर्टिफिकेट जोड़ें
cacerts फ़ाइल को मैन्युअल रूप से संशोधित करने के बजाय, आप IntelliJ के UI के माध्यम से सर्टिफिकेट जोड़ सकते हैं, जो उन्हें इसके आंतरिक ट्रस्टस्टोर में संग्रहीत करता है:

1. `File > Settings > Tools > Server Certificates` (या macOS पर `IntelliJ IDEA > Preferences`) पर जाएं।
2. एक नया सर्टिफिकेट जोड़ने के लिए **"+"** बटन पर क्लिक करें।
3. अपनी कॉर्पोरेट CA सर्टिफिकेट फ़ाइल (`.cer` या `.pem` फॉर्मेट में) पर ब्राउज़ करें और उसे इम्पोर्ट करें।
4. यह सुनिश्चित करने के लिए कि सर्टिफिकेट मान्यता प्राप्त है, IntelliJ को रीस्टार्ट करें।[](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360004301319-Adding-root-CA-to-intellij-on-Windows-10)

### विकल्प 4: प्रॉक्सी या एंटीवायरस हस्तक्षेप की जांच करें
कॉर्पोरेट वातावरण में अक्सर प्रॉक्सी या एंटीवायरस सॉफ़्टवेयर (जैसे Zscaler, Forcepoint) का उपयोग होता है जो मैन-इन-द-मिडिल SSL इंस्पेक्शन करते हैं, जो गतिशील रूप से नए सर्टिफिकेट उत्पन्न करते हैं। यह बार-बार प्रॉम्प्ट का कारण बन सकता है यदि सर्टिफिकेट अक्सर बदलते हैं (उदाहरण के लिए, दैनिक, जैसे McAfee Endpoint Security के साथ)।[](https://stackoverflow.com/questions/60092405/untrusted-server-certificate-in-intellij)[](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360004301319-Adding-root-CA-to-intellij-on-Windows-10)

- **प्रॉक्सी/एंटीवायरस CA सर्टिफिकेट इम्पोर्ट करें**:
  - अपने प्रॉक्सी या एंटीवायरस सॉफ़्टवेयर से रूट CA सर्टिफिकेट प्राप्त करें (अपनी IT टीम से पूछें)।
  - इसे `Settings > Tools > Server Certificates` के माध्यम से IntelliJ के ट्रस्टस्टोर में या ऊपर दिए गए `keytool` कमांड का उपयोग करके cacerts फ़ाइल में इम्पोर्ट करें।
- **SSL इंस्पेक्शन अक्षम करें (यदि संभव हो)**:
  - यदि आपका प्रॉक्सी अनुमति देता है, तो IntelliJ-संबंधित डोमेन (जैसे `plugins.jetbrains.com`, `repo.maven.apache.org`) के लिए SSL इंस्पेक्शन को बायपास करने के लिए इसे कॉन्फ़िगर करें।

### विकल्प 5: समस्या वाले सर्टिफिकेट की पहचान करने के लिए डीबग करें
यदि समस्या बनी रहती है, तो पहचानें कि कौन सा सर्वर या सर्टिफिकेट प्रॉम्प्ट का कारण बन रहा है:

1. वर्बोज़ SSL लॉगिंग सक्षम करें:
   - `Help > Edit Custom VM Options` पर जाएं और जोड़ें:
     ```
     -Djavax.net.debug=ssl:handshake:verbose
     ```
   - IntelliJ को रीस्टार्ट करें और SSL एरर के लिए `idea.log` फ़ाइल (जो `~/.IntelliJIdea<version>/system/log/` में स्थित है) की जांच करें, जैसे `PKIX path building failed`। यह समस्या वाले सर्वर या सर्टिफिकेट को दिखाएगा।[](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360010576419-Adding-trusted-certs)

2. विशिष्ट प्लगइन्स या इंटीग्रेशन के लिए जांच करें:
   - Maven, Gradle, या वर्जन कंट्रोल सिस्टम (जैसे Git, SVN) जैसे प्लगइन्स अलग-अलग सर्टिफिकेट वाले सर्वर से कनेक्ट हो सकते हैं। समस्या को अलग करने के लिए अस्थायी रूप से प्लगइन्स को अक्षम करें।[](https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000131364-Server-s-Certificate-is-not-trusted-pop-up)
   - Maven के लिए, सुनिश्चित करें कि `File > Settings > Build, Execution, Deployment > Build Tools > Maven > Runner` में कॉन्फ़िगर किया गया JDK अपडेटेड cacerts का उपयोग करता है।[](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360010576419-Adding-trusted-certs)

### अतिरिक्त नोट्स
- **सुरक्षा चेतावनी**: गैर-विश्वसनीय सर्टिफिकेट स्वचालित रूप से स्वीकार करना सुविधाजनक है लेकिन गैर-आइसोलेटेड नेटवर्क में जोखिम भरा है। इसका उपयोग केवल विश्वसनीय वातावरण में करें।[](https://stackoverflow.com/questions/60092405/untrusted-server-certificate-in-intellij)[](https://stackoverflow.com/questions/26192713/android-studio-servers-certificate-is-not-trusted)
- **सिस्टम टाइम सिंक**: सुनिश्चित करें कि आपकी सिस्टम घड़ी सिंक्रनाइज़्ड है, क्योंकि एक मिसमैच सर्टिफिकेट वैलिडेशन समस्याएं पैदा कर सकता है।[](https://stackoverflow.com/questions/60092405/untrusted-server-certificate-in-intellij)
- **JetBrains Runtime (JBR)**: IntelliJ अपने स्वयं के JBR पर चलता है, जो सिस्टम के Java ट्रस्टस्टोर का उपयोग नहीं कर सकता है। सिस्टम के `$JAVA_HOME/lib/security/cacerts` में किए गए परिवर्तन IntelliJ को तब तक प्रभावित नहीं करेंगे जब तक कि स्पष्ट रूप से कॉन्फ़िगर न किया गया हो।[](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360010576419-Adding-trusted-certs)
- **लगातार प्रॉम्प्ट**: यदि सर्टिफिकेट इम्पोर्ट करने के बाद भी प्रॉम्प्ट बने रहते हैं, तो यह किसी प्लगइन या सेवा (जैसे JFrog, SonarQube) के कारण हो सकता है जो एक अलग ट्रस्टस्टोर का उपयोग कर रही है। प्लगइन सेटिंग्स की जांच करें या पूर्ण सर्टिफिकेट चेन के लिए अपनी IT टीम से संपर्क करें।[](https://community.sonarsource.com/t/sonarlint-does-not-respect-the-certificates-added-in-the-intellijs-keystore/22897)[](https://github.com/jfrog/jfrog-idea-plugin/issues/34)

### अनुशंसित दृष्टिकोण
1. पहले **विकल्प 3** (IntelliJ के UI के माध्यम से सर्टिफिकेट जोड़ें) आज़माएं, क्योंकि यह सबसे सुरक्षित और सीधा तरीका है।
2. यदि वह विफल हो जाता है, तो **विकल्प 2** के साथ कीस्टोर पथ और कॉन्फ़िगरेशन सत्यापित करें।
3. **विकल्प 1** (स्वचालित स्वीकृति) का उपयोग केवल अंतिम उपाय के रूप में एक विश्वसनीय वातावरण में करें।
4. यदि समस्या में प्रॉक्सी या एंटीवायरस शामिल है, तो सही CA सर्टिफिकेट प्राप्त करने और इम्पोर्ट करने के लिए अपनी IT टीम के साथ काम करें।

यदि आपको अभी भी समस्या आ रही है, तो सर्टिफिकेट के बारे में विवरण (जैसे जारीकर्ता, डोमेन) या `idea.log` फ़ाइल से कोई भी एरर मैसेज साझा करें, और मैं इसे और अधिक संकीर्ण करने में मदद कर सकता हूं।