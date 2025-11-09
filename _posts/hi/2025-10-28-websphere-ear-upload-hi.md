---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: वेबस्फीयर बड़ी ईएआर अपलोड त्रुटियों को ठीक करना
translated: true
type: note
---

### समस्या को समझना
"मल्टीपार्ट फ़ाइल अपलोड त्रुटि" (आमतौर पर कुछ इस तरह: `org.apache.commons.fileupload.FileUploadException: Processing of multipart/form-data request failed. File too large (errno:27)`) आमतौर पर IBM WebSphere Application Server (WAS) में प्रशासनिक कंसोल के माध्यम से एक EAR फ़ाइल अपडेट करते समय होती है। यह बड़ी EAR फाइलों (जैसे, >20MB) के लिए फ़ाइल अपलोड, अस्थायी संग्रहण, हीप मेमोरी, या OS संसाधन सीमाओं के कारण आम है। यह EAR की अपनी समस्या नहीं है, बल्कि यह कंसोल द्वारा HTTP मल्टीपार्ट अपलोड को हैंडल करने के तरीके की समस्या है।

### पहले आजमाने के लिए त्वरित समाधान
1. **EAR को सर्वर पर कॉपी करें और स्थानीय रूप से डिप्लॉय करें**:
   - नई EAR फ़ाइल को WAS सर्वर पर एक डायरेक्टरी में ट्रांसफर करने के लिए FTP/SCP का उपयोग करें (जैसे, `/opt/IBM/WebSphere/AppServer/installableApps/`)।
   - एडमिन कंसोल में: **Applications > Application Types > WebSphere enterprise applications** पर जाएं।
   - अपने मौजूदा एप्लिकेशन को चुनें > **Update**।
   - **Replace or add a single module** या **Replace the entire application** चुनें, फिर **Local file system** चुनें और कॉपी की गई EAR पथ को इंगित करें।
   - यह HTTP के ऊपर मल्टीपार्ट अपलोड को बायपास कर देता है।

2. **OS फ़ाइल आकार सीमा बढ़ाएँ (UNIX/Linux सर्वर)**:
   - `errno:27` त्रुटि का अक्सर मतलब होता है कि फ़ाइल प्रक्रिया के लिए ulimit से अधिक है।
   - वर्तमान सीमा जांचने के लिए WAS यूजर (जैसे, `webadmin`) के रूप में `ulimit -f` चलाएं।
   - इसे अनलिमिटेड सेट करें: यूजर के शेल प्रोफाइल (जैसे, `~/.bash_profile`) या सर्वर के स्टार्टअप स्क्रिप्ट में `ulimit -f unlimited` जोड़ें।
   - Deployment Manager (dmgr) को रीस्टार्ट करें और अपलोड फिर से करने का प्रयास करें।

### WAS में कॉन्फ़िगरेशन परिवर्तन
1. **Deployment Manager के लिए हीप साइज़ बढ़ाएँ**:
   - बड़ी EAR फाइलें प्रोसेसिंग के दौरान OutOfMemory का कारण बन सकती हैं।
   - एडमिन कंसोल में: **Servers > Server Types > Administrative servers > Deployment Manager**।
   - **Java and Process Management > Process definition > Java Virtual Machine** के अंतर्गत:
     - **Initial heap size** 1024 (या अधिक, जैसे बहुत बड़ी EAR के लिए 2048) पर सेट करें।
     - **Maximum heap size** 2048 (या अधिक) पर सेट करें।
   - सेव करें, dmgr को रीस्टार्ट करें, और पुनः प्रयास करें।

2. **HTTP सत्र या पोस्ट आकार सीमा समायोजित करें (यदि लागू हो)**:
   - वेब कंटेनर सीमाओं के लिए: **Servers > Server Types > WebSphere application servers > [आपका सर्वर] > Web Container > HTTP transports**।
   - **Maximum post size** (बाइट्स में) बढ़ाएँ यदि यह कम सेट है।
   - नोट: यह अप्रत्यक्ष रूप से एडमिन कंसोल के वेब ऐप को प्रभावित करता है।

### अनुशंसित दीर्घकालिक समाधान: अपडेट के लिए wsadmin का उपयोग करें
बड़े या लगातार अपडेट के लिए, कंसोल का उपयोग पूरी तरह से छोड़ दें—यह बड़ी फाइलों के लिए अविश्वसनीय है। एप्लिकेशन को अपडेट करने के लिए wsadmin स्क्रिप्टिंग टूल (Jython या JACL) का उपयोग करें।

#### चरण:
1. नई EAR फ़ाइल को सर्वर-एक्सेसिबल पथ पर कॉपी करें (जैसे, `/tmp/myapp.ear`)।
2. wsadmin लॉन्च करें:  
   ```
   /opt/IBM/WebSphere/AppServer/bin/wsadmin.sh -lang jython -user admin -password pass
   ```
3. अपडेट करने के लिए यह Jython स्क्रिप्ट चलाएं:  
   ```python
   AdminApp.update('MyAppName', 'app', [-Map ModulesToApps, '[-MapWebModToVH [[default_host MyContext virtual_host]] ]'], [-Operation update], [-appname MyAppName], [-MapModulesToServers [[MyModule MyServer]]], [-nodefaultoptions], [-preCompileJSPs false], [-contextroot MyContext], [-noTxImport], [-connType SERVER], [ -contenturi /tmp/myapp.ear ])
   AdminConfig.save()
   ```
   - `MyAppName` को अपने ऐप के नाम से, `MyContext` को कॉन्टेक्स्ट रूट से, `MyServer` को टार्गेट सर्वर/क्लस्टर से, और `/tmp/myapp.ear` को EAR पथ से बदलें।
4. यदि क्लस्टर्ड एन्वायरनमेंट है तो नोड्स को सिंक करें: `AdminControl.invoke(AdminControl.completeServers(), 'sync')`।
5. ऐप को रीस्टार्ट करें: **Applications > [ऐप] > Restart**।

यह विधि तेज़ है, अपलोड सीमाओं से बचती है, और ऑटोमेशन (जैसे, Jenkins के माध्यम से) के लिए स्क्रिप्टेबल है।

### अतिरिक्त सुझाव
- **लॉग्स जांचें**: विवरण के लिए dmgr प्रोफाइल में `SystemOut.log` और `SystemErr.log` की समीक्षा करें (जैसे, `/opt/IBM/WebSphere/AppServer/profiles/Dmgr01/logs/dmgr/`)।
- **छोटी EAR के साथ परीक्षण करें**: यह सत्यापित करने के लिए कि क्या समस्या आकार-संबंधी है, एक न्यूनतम संस्करण को ज़िप करके देखें।
- **WAS वर्जन**: सुनिश्चित करें कि आप एक सपोर्टेड वर्जन पर हैं (जैसे, 8.5, 9.0)। यदि आवश्यक हो तो नवीनतम फिक्सेस लगाएं।
- यदि त्रुटि बनी रहती है (जैसे, टाइमआउट), तो **Environment > Web Application Servers > [सर्वर] > Container Settings > Web Container Settings > Web container > Session management > Configuration > Timeout** में HTTP टाइमआउट बढ़ाएँ।

यदि इनमें से कोई भी समस्या का समाधान नहीं करता है, तो अधिक अनुरूप सलाह के लिए सटीक त्रुटि संदेश और WAS वर्जन साझा करें।

### संदर्भ
- [Error during deploy of war file on Websphere Application Server 7.0](https://coderanch.com/t/459530/application-servers/Error-deploy-war-file-Websphere)
- [OutOfMemory errors while deploying applications in WebSphere Application Server](https://www.ibm.com/support/pages/outofmemory-errors-while-deploying-applications-websphere-application-server)
- [Maximum size limit of an Ear that can be deployed in WAS](https://stackoverflow.com/questions/58748076/maximum-size-limit-of-an-ear-that-can-be-deployed-in-was)
- [Deploying the enterprise archive (EAR) using the WebSphere Administrative Console](https://www.ibm.com/docs/en/configurepricequote/9.5.0?topic=cwaso-deploying-enterprise-archive-ear-using-websphere-admin-console)