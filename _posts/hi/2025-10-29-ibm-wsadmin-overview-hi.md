---
audio: false
generated: true
image: false
lang: hi
layout: post
model: x-ai/grok-4-fast
title: आईबीएम वेबस्फीयर wsadmin टूल अवलोकन
translated: true
type: note
---

### IBM WebSphere Application Server (WAS) में wsadmin का अवलोकन

`wsadmin` टूल WebSphere Application Server के प्रशासन के लिए एक कमांड-लाइन स्क्रिप्टिंग इंटरफेस है। यह आपको सर्वर प्रबंधित करने, एप्लिकेशन डिप्लॉय करने, संसाधन कॉन्फ़िगर करने और रनटाइम ऑपरेशन मॉनिटर करने जैसे कार्यों को स्वचालित करने की अनुमति देता है। स्क्रिप्ट Jython (Python-आधारित) या JACL (Tcl-आधारित) में लिखी जा सकती हैं, जिसमें Jython इसकी पठनीयता के कारण अधिक सामान्यतः उपयोग किया जाता है।

- **`wsadmin.bat`**: Windows सिस्टम पर उपयोग किया जाता है।
- **`wsadmin.sh`**: Unix/Linux/AIX सिस्टम पर उपयोग किया जाता है।

दोनों टूल WebSphere प्रोफाइल के `bin` डायरेक्टरी (जैसे, `<WAS_HOME>/profiles/<ProfileName>/bin/`) या बेस इंस्टॉलेशन (`<WAS_HOME>/bin/`) में स्थित होते हैं। सही वातावरण सुनिश्चित करने के लिए इन्हें प्रोफाइल की `bin` डायरेक्टरी से चलाने की सिफारिश की जाती है।

#### इंटरएक्टिव रूप से wsadmin शुरू करना
यह एक शेल लॉन्च करता है जहां आप सीधे कमांड दर्ज कर सकते हैं।

**सिंटेक्स:**
```
wsadmin[.bat|.sh] [options]
```

**बेसिक उदाहरण (Windows):**
```
cd C:\IBM\WebSphere\AppServer\profiles\AppSrv01\bin
wsadmin.bat -lang jython -user admin -password mypass
```

**बेसिक उदाहरण (Unix/Linux):**
```
cd /opt/IBM/WebSphere/AppServer/profiles/AppSrv01\bin
./wsadmin.sh -lang jython -user admin -password mypass
```

- `-lang jython`: Jython निर्दिष्ट करता है (JACL के लिए `-lang jacl` का उपयोग करें)।
- `-user` और `-password`: आवश्यक यदि ग्लोबल सिक्योरिटी सक्षम है (यदि अक्षम है तो छोड़ दें)।
- यदि छोड़ दिया जाता है, तो यह पोर्ट 8879 (या RMI पोर्ट 2809) पर डिफ़ॉल्ट SOAP कनेक्टर का उपयोग करके लोकल सर्वर से कनेक्ट होता है।

एक बार wsadmin प्रॉम्प्ट (जैसे, `wsadmin>`) में, आप स्क्रिप्टिंग ऑब्जेक्ट्स का उपयोग करके कमांड चला सकते हैं:
- **AdminConfig**: कॉन्फ़िगरेशन परिवर्तनों के लिए (जैसे, संसाधन बनाना)।
- **AdminControl**: रनटाइम ऑपरेशन के लिए (जैसे, सर्वर शुरू/बंद करना)।
- **AdminApp**: एप्लिकेशन डिप्लॉयमेंट/अपडेट के लिए।
- **AdminTask**: हाई-लेवल टास्क के लिए (जैसे, नोड्स सिंक करना)।
- **Help**: बिल्ट-इन हेल्प के लिए (जैसे, `Help.help()`)।

**शेल में उदाहरण कमांड:**
- सभी सर्वर सूचीबद्ध करें: `print AdminConfig.list('Server')`
- एक सर्वर शुरू करें: `AdminControl.invoke(AdminControl.completeObjectName('type=ServerIndex,process=server1,*'), 'start')`
- परिवर्तन सहेजें: `AdminConfig.save()`
- बाहर निकलें: `quit`

#### एक स्क्रिप्ट फ़ाइल चलाना
गैर-इंटरएक्टिव रूप से Jython (.py या .jy) या JACL (.jacl) स्क्रिप्ट निष्पादित करने के लिए `-f` विकल्प का उपयोग करें।

**उदाहरण स्क्रिप्ट (deployApp.py):**
```python
# कनेक्ट करें और एक ऐप डिप्लॉय करें
appName = 'MyApp'
AdminApp.install('/path/to/MyApp.ear', '[-appname ' + appName + ']')
AdminConfig.save()
print 'Application ' + appName + ' deployed successfully.'
```

**Windows पर चलाएँ:**
```
wsadmin.bat -lang jython -f /path/to/deployApp.py -user admin -password mypass
```

**Unix/Linux पर चलाएँ:**
```
./wsadmin.sh -lang jython -f /path/to/deployApp.py -user admin -password mypass
```

#### एक सिंगल कमांड चलाना
वन-ऑफ कमांड के लिए `-c` विकल्प का उपयोग करें (बैच फ़ाइलों या ऑटोमेशन में उपयोगी)।

**उदाहरण (Windows बैच फ़ाइल स्निपेट):**
```batch
@echo off
call "C:\IBM\WebSphere\AppServer\profiles\AppSrv01\bin\wsadmin.bat" -lang jython -c "print AdminConfig.list('Server')" -user admin -password mypass
```

**उदाहरण (Unix शेल स्क्रिप्ट स्निपेट):**
```bash
#!/bin/bash
./wsadmin.sh -lang jython -c "print AdminConfig.list('Server')" -user admin -password mypass
```

#### मुख्य विकल्प

| विकल्प | विवरण | उदाहरण |
|--------|-------------|---------|
| `-conntype` | कनेक्टर प्रकार: `SOAP` (डिफ़ॉल्ट, पोर्ट 8879) या `RMI` (पोर्ट 2809)। | `-conntype RMI` |
| `-host` | कनेक्ट करने के लिए रिमोट होस्ट। | `-host myhost.example.com` |
| `-port` | कनेक्टर पोर्ट। | `-port 8879` |
| `-tracefile` | आउटपुट को एक फ़ाइल में लॉग करें। | `-tracefile wsadmin.log` |
| `-profile` | मुख्य स्क्रिप्ट से पहले एक प्रोफाइल स्क्रिप्ट चलाएँ। | `-profile init.py` |
| `-c` | एक सिंगल कमांड निष्पादित करें (गैर-इंटरएक्टिव)। | `-c "AdminConfig.save()"` |
| `-f` | एक स्क्रिप्ट फ़ाइल निष्पादित करें। | `-f myscript.py` |
| `-job` | एक जॉब मैनेजर कमांड चलाएँ। | `-job deploy.xml` |

#### टिप्स और बेस्ट प्रैक्टिसेज़
- **सुरक्षा**: यदि ग्लोबल सिक्योरिटी बंद है, तो `-user` और `-password` छोड़ दें। सुरक्षित सेटअप के लिए, एन्क्रिप्टेड क्रेडेंशियल्स या की फाइलों का उपयोग करें।
- **थिन क्लाइंट मोड**: पूर्ण WAS इंस्टॉलेशन के बिना रिमोट एडमिनिस्ट्रेशन के लिए, थिन क्लाइंट JARs (जैसे, `com.ibm.ws.admin.client_*.jar`) के साथ `wsadmin -conntype NONE` का उपयोग करें।
- **प्रदर्शन**: कई कमांड्स के लिए, JVM ओवरहेड से बचने के लिए बार-बार `-c` कॉल के बजाय एक ही `-f` स्क्रिप्ट का उपयोग करें।
- **त्रुटि प्रबंधन**: कॉन्फ़िगरेशन परिवर्तनों के बाद हमेशा `AdminConfig.save()` को कॉल करें। मजबूती के लिए Jython में try-except का उपयोग करें।
- **कमांड जनरेट करना**: WAS एडमिन कंसोल में, कोई क्रिया करें और समतुल्य wsadmin कमांड प्राप्त करने के लिए "View administrative scripting command for last action" पर क्लिक करें।
- **वर्जन नोट्स**: व्यवहार WAS 8.5+ और 9.0+ में सुसंगत है, लेकिन वर्जन-विशिष्ट विवरणों (जैसे, नए वर्जन में Jython 2.7) के लिए IBM डॉक्स चेक करें।

अधिक उन्नत उपयोग के लिए, सरलीकृत कमांड्स जैसे `AdminTask.importFile('path/to/file')` के लिए AdminTask ऑब्जेक्ट का अन्वेषण करें।

### संदर्भ
- [wsadmin scripting tool - IBM Docs](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-wsadmin-tool)
- [Getting started with wsadmin scripting - IBM Docs](https://www.ibm.com/docs/SSAW57_8.5.5/com.ibm.websphere.nd.doc/ae/txml_script.html)
- [WAS - wsadmin (Jython) Tutorial](http://www.mtitek.com/tutorials/websphere/wsadmin_jython.php)
- [IBM WebSphere - Getting Started with wsadmin](https://www.freekb.net/Article?id=1563)
- [WSADMIN Tutorial – Part1](https://websphereapplicationservernotes.wordpress.com/2012/12/25/wsadmin-tutorial-part1/)