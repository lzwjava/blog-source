---
audio: false
generated: true
lang: hi
layout: post
title: वीएसकोड में स्प्रिंग बूट के लिए लॉन्च.जेसन कॉन्फ़िगर करना
translated: true
type: note
---

Visual Studio Code (VSCode) में Maven Spring Boot प्रोजेक्ट के लिए `launch.json` फ़ाइल कॉन्फ़िगर करने के लिए, आपको एक लॉन्च कॉन्फ़िगरेशन सेट अप करने की आवश्यकता है जो VSCode को इसके Java एक्सटेंशन का उपयोग करके आपके एप्लिकेशन को चलाने और डीबग करने की अनुमति देता है। इसे प्राप्त करने में आपकी सहायता के लिए नीचे एक चरण-दर-चरण मार्गदर्शिका दी गई है।

### पूर्वापेक्षाएँ
आगे बढ़ने से पहले, सुनिश्चित करें:
- आपके पास VSCode में **Java Extension Pack** इंस्टॉल हो। इस पैक में Red Hat द्वारा "Debugger for Java" और "Language Support for Java" जैसे आवश्यक एक्सटेंशन शामिल हैं, जो Spring Boot प्रोजेक्ट सहित Java एप्लिकेशन चलाने और डीबग करने के लिए सहायता प्रदान करते हैं।
- आपका Spring Boot प्रोजेक्ट एक वैध `pom.xml` फ़ाइल के साथ एक Maven प्रोजेक्ट है।
- प्रोजेक्ट में `@SpringBootApplication` एनोटेशन वाला एक मुख्य वर्ग है, जिसमें एप्लिकेशन शुरू करने के लिए `main` मेथड है।

### `launch.json` कॉन्फ़िगर करने के चरण
1. **मुख्य वर्ग (Main Class) का पता लगाएं**
   - एक सामान्य Spring Boot प्रोजेक्ट में, मुख्य वर्ग `src/main/java` डायरेक्टरी में स्थित होता है और `@SpringBootApplication` से एनोटेटेड होता है। उदाहरण के लिए, इसका नाम `com.example.demo.DemoApplication` हो सकता है।
   - VSCode में अपना प्रोजेक्ट खोलें और इस वर्ग का पूरी तरह से योग्य नाम (fully qualified name) पहचानें (जैसे, `com.example.demo.DemoApplication`)।

2. **प्रोजेक्ट नाम निर्धारित करें**
   - Maven प्रोजेक्ट में प्रोजेक्ट नाम आपकी `pom.xml` फ़ाइल में परिभाषित `artifactId` से मेल खाता है।
   - अपनी `pom.xml` फ़ाइल खोलें और `<artifactId>` टैग देखें। उदाहरण के लिए:
     ```xml
     <artifactId>demo</artifactId>
     ```
     यहाँ, प्रोजेक्ट नाम `demo` होगा।

3. **डीबग व्यू (Debug View) खोलें**
   - VSCode में, बाएं साइडबार में **Debug** आइकन पर क्लिक करें (या Mac पर `Ctrl+Shift+D` / `Cmd+Shift+D` दबाएं)।
   - "Run and Debug" ड्रॉपडाउन के आगे गियर आइकन ⚙️ पर क्लिक करें ताकि लॉन्च सेटिंग्स कॉन्फ़िगर की जा सकें। यदि कोई `launch.json` मौजूद नहीं है, तो VSCode आपको एक बनाने के लिए प्रेरित करेगा।

4. **`launch.json` बनाएं या संपादित करें**
   - यदि पर्यावरण चुनने के लिए कहा जाए, तो **Java** चुनें। यह आपके प्रोजेक्ट की `.vscode` फ़ोल्डर में एक बेसिक `launch.json` फ़ाइल जनरेट करेगा।
   - `launch.json` फ़ाइल खोलें। यदि यह पहले से मौजूद है, तो आप इसे सीधे संपादित कर सकते हैं।

5. **एक लॉन्च कॉन्फ़िगरेशन जोड़ें**
   - `launch.json` में `"configurations"` ऐरे के अंदर निम्नलिखित कॉन्फ़िगरेशन जोड़ें। प्लेसहोल्डर्स को अपने प्रोजेक्ट के विवरण से बदलें:
     ```json
     {
         "type": "java",
         "name": "Launch Spring Boot App",
         "request": "launch",
         "mainClass": "com.example.demo.DemoApplication",
         "projectName": "demo"
     }
     ```
     - **फ़ील्ड्स की व्याख्या:**
       - `"type": "java"`: निर्दिष्ट करता है कि यह एक Java लॉन्च कॉन्फ़िगरेशन है।
       - `"name": "Launch Spring Boot App"`: इस कॉन्फ़िगरेशन के लिए एक वर्णनात्मक नाम, जो डीबग ड्रॉपडाउन में दिखाई देगा।
       - `"request": "launch"`: इंगित करता है कि VSCode को एप्लिकेशन लॉन्च करना चाहिए (किसी मौजूदा प्रोसेस से अटैच करने के विपरीत)।
       - `"mainClass"`: आपके Spring Boot मुख्य वर्ग का पूरी तरह से योग्य नाम (जैसे, `com.example.demo.DemoApplication`)।
       - `"projectName"`: आपकी `pom.xml` से `artifactId` (जैसे, `demo`), जो VSCode को मल्टी-मॉड्यूल सेटअप में प्रोजेक्ट का पता लगाने में मदद करता है।

   - इस कॉन्फ़िगरेशन के साथ एक पूर्ण `launch.json` फ़ाइल का उदाहरण यहाँ दिया गया है:
     ```json
     {
         "version": "0.2.0",
         "configurations": [
             {
                 "type": "java",
                 "name": "Launch Spring Boot App",
                 "request": "launch",
                 "mainClass": "com.example.demo.DemoApplication",
                 "projectName": "demo"
             }
         ]
     }
     ```

6. **वैकल्पिक: VM Arguments या Program Arguments जोड़ें**
   - यदि आपके एप्लिकेशन को अतिरिक्त सेटिंग्स की आवश्यकता है (जैसे, Spring प्रोफ़ाइल सक्रिय करना), तो आप उन्हें `"vmArgs"` या `"args"` का उपयोग करके जोड़ सकते हैं:
     - Spring प्रोफ़ाइल के साथ उदाहरण:
       ```json
       {
           "type": "java",
           "name": "Launch Spring Boot App with Profile",
           "request": "launch",
           "mainClass": "com.example.demo.DemoApplication",
           "projectName": "demo",
           "vmArgs": "-Dspring.profiles.active=dev"
       }
       ```
       यह `spring.profiles.active` प्रॉपर्टी को `dev` पर सेट करता है।
     - प्रोग्राम आर्गुमेंट्स के साथ उदाहरण:
       ```json
       "args": ["arg1", "arg2"]
       ```

7. **सेव करें और रन करें**
   - `launch.json` फ़ाइल सेव करें।
   - डीबग व्यू पर वापस जाएं, ड्रॉपडाउन से **"Launch Spring Boot App"** चुनें, और ग्रीन प्ले बटन पर क्लिक करें (या `F5` दबाएं)।
   - VSCode Maven और Java एक्सटेंशन का उपयोग करके आपके Spring Boot एप्लिकेशन को बिल्ड और रन करेगा। आपको डीबग कंसोल में Spring Boot स्टार्टअप लॉग दिखाई देने चाहिए।

### कॉन्फ़िगरेशन सत्यापित करना
- यदि आपका Spring Boot एप्लिकेशन एक वेब एप्लिकेशन है, तो एक ब्राउज़र खोलें और `http://localhost:8080` पर नेविगेट करें (या आपकी `application.properties` या `application.yml` फ़ाइल में निर्दिष्ट पोर्ट) ताकि यह पुष्टि हो सके कि यह चल रहा है।
- आप अपने कोड में ब्रेकपॉइंट सेट कर सकते हैं और अपने एप्लिकेशन को डीबग करने के लिए डीबग कंट्रोल्स (पॉज़, स्टेप ओवर, आदि) का उपयोग कर सकते हैं।

### नोट्स
- VSCode में Java एक्सटेंशन आपकी `pom.xml` के आधार पर क्लासपाथ और बिल्ड प्रक्रिया को स्वचालित रूप से हैंडल करते हैं, इसलिए आपको आमतौर पर पहले से मैन्युअल रूप से `mvn clean install` चलाने की आवश्यकता नहीं होती है।
- यदि आपका प्रोजेक्ट मल्टी-मॉड्यूल Maven सेटअप का हिस्सा है, तो सुनिश्चित करें कि `projectName` सही मॉड्यूल के `artifactId` से मेल खाता है।
- उन्नत कॉन्फ़िगरेशन (जैसे, कस्टम वर्किंग डायरेक्टरी या प्री-लॉन्च टास्क) के लिए, [VSCode Java Debugging documentation](https://code.visualstudio.com/docs/java/java-debugging) देखें।

इस सेटअप के साथ, आपका `launch.json` VSCode में आपके Maven Spring Boot प्रोजेक्ट को चलाने और डीबग करने के लिए सही ढंग से कॉन्फ़िगर होना चाहिए!