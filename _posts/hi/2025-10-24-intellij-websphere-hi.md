---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: वेबस्फीयर डेवलपमेंट के लिए इंटेलीजे आईडीईए
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) डेवलपमेंट के लिए IntelliJ IDEA का उपयोग

IntelliJ IDEA, IBM WebSphere Application Server (WAS) के लिए बनाई जाने वाली Java EE एप्लिकेशन्स डेवलप करने का एक मजबूत विकल्प है। यह Java EE स्टैंडर्ड्स को सपोर्ट करता है, जिनका WAS पालन करता है, और एंटरप्राइज़ ऐप्स बनाने, डिप्लॉय करने और डीबग करने के लिए उत्कृष्ट टूलिंग प्रदान करता है। हालांकि Eclipse में IBM के टूल्स के जरिए अधिक नेटिव WAS इंटीग्रेशन है, IntelliJ कुछ सेटअप के साथ अच्छी तरह काम करता है। नीचे, मैं बेसिक्स, रिमोट डीबगिंग (हां, आप WAS JVM से अटैच कर सकते हैं), और अतिरिक्त टिप्स को कवर करूंगा।

#### 1. IntelliJ में WAS डेवलपमेंट के लिए प्रारंभिक सेटअप
- **आवश्यक प्लगइन्स इंस्टॉल करें**:
  - **File > Settings > Plugins** पर जाएं और JetBrains Marketplace में "WebSphere Server" सर्च करें। बेहतर लोकल सर्वर मैनेजमेंट (जैसे IntelliJ से WAS स्टार्ट/स्टॉप करना) के लिए इसे इंस्टॉल करें। यह प्लगइन बंडल नहीं है, इसलिए यह वैकल्पिक है लेकिन लोकल डेव के लिए रिकमंडेड है।
  - सुनिश्चित करें कि Java EE और Jakarta EE प्लगइन्स एनेबल हैं (ये आमतौर पर प्री-इंस्टॉल्ड आते हैं)।

- **प्रोजेक्ट बनाएं**:
  - एक नया **Java Enterprise** प्रोजेक्ट शुरू करें (या मौजूदा प्रोजेक्ट इम्पोर्ट करें)।
  - **Web Application** आर्किटाइप चुनें और Java EE (जैसे, आपके WAS वर्जन जैसे 9.x के आधार पर वर्जन 8 या 9) के लिए कॉन्फ़िगर करें।
  - जरूरत पड़ने पर WAS-स्पेसिफिक लाइब्रेरीज़ के लिए डिपेंडेंसीज एड करें (जैसे, Maven/Gradle के जरिए: JSP सपोर्ट के लिए `com.ibm.websphere.appserver.api:jsp-2.3`)।

- **लोकल WAS सर्वर कॉन्फ़िगर करें (लोकल रन्स के लिए वैकल्पिक)**:
  - **Run > Edit Configurations > + > WebSphere Server > Local** पर जाएं।
  - अपनी लोकल WAS इंस्टॉलेशन डायरेक्टरी की ओर पॉइंट करें (जैसे, `/opt/IBM/WebSphere/AppServer`)।
  - सर्वर नाम, JRE (WAS के साथ बंडल आई IBM का JDK इस्तेमाल करें), और डिप्लॉयमेंट ऑप्शन्स सेट करें (जैसे, हॉट-रीलोड के लिए exploded WAR)।
  - डिप्लॉयमेंट के लिए: **Deployment** टैब में, अपना आर्टिफैक्ट (जैसे, WAR फाइल) एड करें और कॉन्टेक्स्ट पाथ सेट करें।

यह सेटअप आपको लोकल टेस्टिंग के लिए सीधे IntelliJ से रन/डिप्लॉय करने देता है।

#### 2. रिमोट डीबगिंग: IntelliJ को WAS JVM से अटैच करना
हां, आप निश्चित रूप से IntelliJ डीबगर को एक रिमोट WAS JVM से अटैच कर सकते हैं। यह JDWP (Java Debug Wire Protocol) के जरिए स्टैंडर्ड Java रिमोट डीबगिंग है। यह लोकल और रिमोट दोनों WAS इंस्टेंसेज के लिए काम करता है—सर्वर को एक "रिमोट JVM" की तरह ट्रीट करें।

**स्टेप 1: WAS सर्वर पर डीबगिंग एनेबल करें**
- **एडमिन कंसोल के जरिए (प्रोडक्शन-लाइक सेटअप्स के लिए रिकमंडेड)**:
  - WAS एडमिन कंसोल में लॉग इन करें (जैसे, `https://your-host:9043/ibm/console`)।
  - **Servers > Server Types > WebSphere Application Servers > [आपका सर्वर] > Debugging Service** पर नेविगेट करें।
  - **Enable service at server startup** चेक करें।
  - **JVM debug port** सेट करें (डिफॉल्ट 7777 है; कॉन्फ्लिक्ट से बचने के लिए 8000 जैसा अनयूज्ड पोर्ट चुनें)।
  - सेव करें और सर्वर रीस्टार्ट करें।

- **server.xml के जरिए (स्टैंडअलोन या क्विक एडिट्स के लिए)**:
  - `$WAS_HOME/profiles/[प्रोफाइल]/config/cells/[सेल]/nodes/[नोड]/servers/[सर्वर]/server.xml` एडिट करें।
  - `<processDefinitions>` के अंदर `<jvmEntries>` सेक्शन में, एड या अपडेट करें:
    ```
    <jvmEntries xmi:id="..." debugMode="true">
      <debugArgs>-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:8000</debugArgs>
    </jvmEntries>
    ```
    - `suspend=n` सर्वर को नॉर्मली स्टार्ट करता है (स्टार्टअप पर पॉज़ करने के लिए `suspend=y` इस्तेमाल करें)।
    - `8000` को अपने पोर्ट से रिप्लेस करें।
  - सेव करें, फिर सर्वर रीस्टार्ट करें: `./startServer.sh [सर्वरनाम]` (या कंसोल के जरिए)।

- वेरिफाई करें: सर्वर लॉग्स में "JDWP: transport=dt_socket, address=*:8000" या इसी तरह का मैसेज चेक करें।

**स्टेप 2: IntelliJ में रिमोट डीबग कॉन्फ़िगर करें**
- **Run > Edit Configurations > + > Remote JVM Debug** पर जाएं।
- इसका नाम दें (जैसे, "WAS Remote Debug")।
- **Debugger mode** को "Attach to remote JVM" पर सेट करें।
- **Host**: आपका WAS सर्वर IP/होस्टनाम (जैसे, लोकल के लिए `localhost`, रिमोट के लिए `192.168.1.100`)।
- **Port**: JVM डीबग पोर्ट (जैसे, 8000)।
- वैकल्पिक रूप से, अगर आपके प्रोजेक्ट में स्पेसिफिक लाइब्स हैं तो **Use module classpath** सेट करें।
- एप्लाई करें और क्लोज करें।

**स्टेप 3: अटैच करें और डीबग करें**
- अपने कोड में ब्रेकपॉइंट्स सेट करें (जैसे, एक सर्वलेट या EJB में)।
- अपनी ऐप को WAS पर डिप्लॉय करें (मैन्युअली एडमिन कंसोल या wsadmin स्क्रिप्ट्स के जरिए)।
- डीबग कॉन्फ़िगरेशन रन करें (**Run > Debug 'WAS Remote Debug'**)।
- अपनी ऐप को ट्रिगर करें (जैसे, HTTP रिक्वेस्ट के जरिए)। IntelliJ अटैच हो जाएगा, और एक्जिक्यूशन ब्रेकपॉइंट्स पर पॉज़ हो जाएगा।
- कॉमन इशूज: फायरवॉल द्वारा पोर्ट ब्लॉक होना, मिसमैच्ड JDK वर्जन (IntelliJ में WAS के IBM JDK का इस्तेमाल करें), या कॉन्फ़िग बदलने के बाद सर्वर रीस्टार्ट नहीं किया गया।

यह WAS 7+ (Liberty प्रोफाइल सहित) के लिए काम करता है। रिमोट सर्वर के लिए, डीबग पोर्ट तक नेटवर्क एक्सेस सुनिश्चित करें।

#### 3. एफिशिएंट WAS डेवलपमेंट के लिए अन्य टिप्स
- **हॉट डिप्लॉयमेंट/हॉटस्वैप**: तेज इटरेशन के लिए, "exploded" WAR (अनपैक्ड) के रूप में डिप्लॉय करें। WAS JSPs और कुछ क्लासेस के लिए हॉट-रिलोड सपोर्ट करता है, लेकिन फुल हॉटस्वैप (रीस्टार्ट के बिना कोड चेंजेस) के लिए, JRebel प्लगइन (पेड) या DCEVM + HotSwapAgent (फ्री, लेकिन WAS के IBM JDK के साथ कम्पैटिबिलिटी टेस्ट करें) इस्तेमाल करें।

- **बिल्ड टूल्स**: डिपेंडेंसीज के लिए Maven या Gradle इस्तेमाल करें। क्लासपाथ ब्लोट से बचने के लिए WAS रनटाइम लाइब्रेरीज को provided स्कोप के रूप में एड करें:
  ```
  <dependency>
    <groupId>com.ibm.websphere.appserver.runtime</groupId>
    <artifactId>shared</artifactId>
    <version>9.0.5</version>
    <scope>provided</scope>
  </dependency>
  ```
  `mvn clean package` रन करें और WAR को एडमिन कंसोल के जरिए डिप्लॉय करें।

- **लॉगिंग और प्रोफाइलिंग**: ऐप लॉग्स के लिए SLF4J/Logback इंटीग्रेट करें। परफॉर्मेंस के लिए, VisualVM या YourKit इस्तेमाल करें (डीबगिंग की तरह रिमोट अटैच करें)। WAS का PMI (Performance Monitoring Infrastructure) बढ़िया है—मेट्रिक्स के लिए इसे एडमिन कंसोल में एनेबल करें।

- **टेस्टिंग**: रिमोट WAS के खिलाफ इंटीग्रेशन टेस्ट्स के लिए Arquillian इस्तेमाल करें। या फुल WAS के बिना लोकल यूनिट टेस्ट्स के लिए Open Liberty (WAS-कम्पैटिबल) एम्बेड करें।

- **वर्जन-स्पेसिफिक नोट्स**: WAS 9.x+ के लिए, IntelliJ में Jakarta EE माइग्रेशन टूल्स का लाभ उठाएं। अगर WAS Liberty (माइक्रोप्रोफाइल-फोकस्ड) इस्तेमाल कर रहे हैं, तो Liberty Tools प्लगइन ऑटो-रीलोड के साथ डेव मोड एड करता है।

- **कॉमन पिटफॉल्स**:
  - क्लासपाथ इशूज: सुनिश्चित करें कि IntelliJ का प्रोजेक्ट SDK WAS के JDK से मेल खाता हो।
  - सिक्योरिटी: रिमोट डीबग पोर्ट को एक्सपोज़ करता है—इसे सिर्फ डेव/ट्रस्टेड नेटवर्क्स में इस्तेमाल करें।
  - प्लगइन लिमिटेशन्स: WebSphere प्लगइन बेसिक है; एडवांस्ड फीचर्स के लिए, IBM का Rational Application Developer कंसीडर करें (लेकिन इसके UX के लिए IntelliJ पर ही बने रहें)।

यह आपको शुरू करने और चलाने में मदद करेगा। अगर आप किसी स्पेसिफिक WAS वर्जन पर हैं, तो अधिक टेलर्ड सलाह के लिए डिटेल्स शेयर करें।

#### संदर्भ
- [Run/Debug Configuration: WebSphere Server | IntelliJ IDEA](https://www.jetbrains.com/help/idea/run-debug-configuration-websphere-server.html)
- [WebSphere remote server debug configuration in IntelliJ Idea](https://stackoverflow.com/questions/33013860/websphere-remote-server-debug-configuration-in-intellij-idea)
- [Debug code running on IBM Websphere using Eclipse / Intellij IDEA](https://davanum.wordpress.com/2009/11/20/debug-code-running-on-ibm-websphere-using-eclipse-intellij-idea/)
- [Debugging applications - IBM](https://www.ibm.com/docs/en/was/9.0.5?topic=applications-debugging)
- [Remote Debugging with IntelliJ IDEA | Baeldung](https://www.baeldung.com/intellij-remote-debugging)