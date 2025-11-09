---
audio: false
date: 2025-09-10
generated: true
image: false
lang: hi
layout: post
model: openai/gpt-5
title: मेवेन प्लेटफ़ॉर्म एन्कोडिंग चेतावनियों को ठीक करना
translated: true
type: note
---

उस Maven चेतावनी का मतलब है कि आपकी प्रोजेक्ट बिल्ड प्रक्रिया **डिफ़ॉल्ट प्लेटफ़ॉर्म एन्कोडिंग** (जैसे, चीनी विंडोज़ सिस्टम पर GBK) पर निर्भर करती है। यदि अन्य डेवलपर्स या CI सर्वर अलग एन्कोडिंग (जैसे Linux पर UTF-8) का उपयोग करते हैं, तो टेक्स्ट रिसोर्सेज (Java सोर्स, properties, XML, आदि) गलत पढ़े या कंपाइल किए जा सकते हैं।

इसे ठीक करने का तरीका यहाँ बताया गया है:

---

### 1. `pom.xml` में सोर्स एन्कोडिंग सेट करें

अपनी प्रोजेक्ट के `<properties>` सेक्शन में, एन्कोडिंग को स्पष्ट रूप से डिक्लेयर करें:

```xml
<properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    <maven.compiler.encoding>UTF-8</maven.compiler.encoding>
</properties>
```

यह सुनिश्चित करता है कि Maven आपके OS डिफ़ॉल्ट की परवाह किए बिना, सोर्स को UTF-8 में कंपाइल करे और रिपोर्ट्स जेनरेट करे।

---

### 2. कंपाइलर प्लगइन कॉन्फ़िगर करें (यदि पहले से नहीं है)

कुछ पुराने Maven सेटअप को कंपाइलर प्लगइन के तहत एन्कोडिंग की आवश्यकता होती है:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.11.0</version>
            <configuration>
                <source>1.8</source>
                <target>1.8</target>
                <encoding>UTF-8</encoding>
            </configuration>
        </plugin>
    </plugins>
</build>
```

---

### 3. फ़ाइल एन्कोडिंग्स जाँचें

* सुनिश्चित करें कि आपकी `.java`, `.properties`, `.yml`, आदि फ़ाइलें UTF-8 में सेव हों, GBK में नहीं।
* IntelliJ IDEA या VS Code में, प्रोजेक्ट सेटिंग्स में **File Encoding = UTF-8** सेट करें।
* Git के लिए, आप `.gitattributes` के साथ सुसंगत एन्कोडिंग लागू कर सकते हैं यदि आवश्यक हो।

---

### 4. Maven को एक्सप्लिसिट एन्कोडिंग के साथ रन करें (वैकल्पिक)

आप Maven को रन करते समय एन्कोडिंग ओवरराइड भी कर सकते हैं:

```bash
mvn clean install -Dfile.encoding=UTF-8
```

लेकिन सबसे अच्छा तरीका है कि इसे `pom.xml` के अंदर ठीक कर लिया जाए, ताकि यह सभी के लिए सुसंगत रहे।

---

✅ इन बदलावों के बाद, "platform dependent encoding GBK" वाली चेतावनी गायब हो जानी चाहिए, और आपका Spring + Maven प्रोजेक्ट सभी मशीनों पर एन्कोडिंग-सुरक्षित होगा।

क्या आप चाहते हैं कि मैं आपको यह भी दिखाऊँ कि मौजूदा GBK सोर्स फ़ाइलों को सुरक्षित रूप से **UTF-8 में कैसे कन्वर्ट करें** (ताकि आपका रेपो क्लीन और सुसंगत हो)?