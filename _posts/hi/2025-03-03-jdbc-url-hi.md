---
audio: false
generated: true
lang: hi
layout: post
title: जेडीबीसी यूआरएल का निर्माण करें
translated: true
type: note
---

WebSphere Liberty Profile के `server.xml` फ़ाइल में `properties.db2.jcc` एलिमेंट के आधार पर DB2 डेटाबेस से कनेक्ट होने के लिए JDBC URL बनाने के लिए, आपको कुछ मुख्य एट्रिब्यूट्स जैसे `databaseName`, `serverName`, और `portNumber` के लिए दिए गए वैल्यूज़ का उपयोग करना होगा। यहाँ बताया गया है कि इसे कैसे करें:

### DB2 के लिए बेसिक JDBC URL फॉर्मेट
DB2 JDBC टाइप 4 ड्राइवर (जो आमतौर पर Liberty Profile सेटअप में उपयोग किया जाता है) का उपयोग करने वाले JDBC URL का स्टैंडर्ड फॉर्मेट है:

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

- **`jdbc:db2://`** - यह टाइप 4 ड्राइवर का उपयोग करने वाले DB2 डेटाबेस के लिए प्रोटोकॉल आइडेंटिफायर है, जो डायरेक्ट नेटवर्क कनेक्शन को दर्शाता है।
- **`<serverName>`** - DB2 सर्वर का होस्टनाम या IP एड्रेस, जो `properties.db2.jcc` में `serverName` एट्रिब्यूट द्वारा निर्दिष्ट किया गया है।
- **`<portNumber>`** - वह पोर्ट जिस पर DB2 इंस्टेंस लिसन कर रहा है, जो `portNumber` एट्रिब्यूट द्वारा निर्दिष्ट किया गया है (यदि निर्दिष्ट नहीं है तो डिफॉल्ट आमतौर पर `50000` होता है)।
- **`<databaseName>`** - कनेक्ट होने वाले डेटाबेस का नाम, जो `databaseName` एट्रिब्यूट द्वारा निर्दिष्ट किया गया है।

### URL बनाने के स्टेप्स
1.  **आवश्यक प्रॉपर्टीज़ की पहचान करें**: `server.xml` में `properties.db2.jcc` एलिमेंट से `serverName`, `portNumber`, और `databaseName` के वैल्यूज़ निकालें। ये URL के लिए आवश्यक घटक हैं।
2.  **URL को असेंबल करें**: इन वैल्यूज़ को उपरोक्त फॉर्मेट में कंबाइन करें, उचित सेपरेटर्स (`:` सर्वर और पोर्ट के बीच, `/` डेटाबेस नाम से पहले) सुनिश्चित करते हुए।
3.  **अतिरिक्त प्रॉपर्टीज़ को हैंडल करें (यदि मौजूद हों)**: यदि `properties.db2.jcc` में अन्य एट्रिब्यूट्स शामिल हैं (जैसे `currentSchema`, `sslConnection`), तो कभी-कभी उन्हें URL के अंत में जोड़ा जा सकता है, लेकिन यह उनकी प्रकृति पर निर्भर करता है। आमतौर पर, `user` और `password` जैसी प्रॉपर्टीज़ कनेक्शन स्थापित करते समय अलग से पास की जाती हैं, सुरक्षा कारणों से URL में नहीं।

### उदाहरण
मान लीजिए कि आपकी `server.xml` में निम्नलिखित `properties.db2.jcc` कॉन्फ़िगरेशन है:

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" user="dbuser" password="dbpass"/>
```

- `serverName="localhost"`
- `portNumber="50000"`
- `databaseName="SAMPLE"`

JDBC URL होगा:

```
jdbc:db2://localhost:50000/SAMPLE
```

- `user` और `password` को URL में शामिल नहीं किया गया है; उन्हें आमतौर पर अलग से प्रदान किया जाता है जब JDBC ड्राइवर के माध्यम से कनेक्शन प्राप्त किया जाता है (जैसे, `DataSource` या `DriverManager` के माध्यम से)।

### अतिरिक्त प्रॉपर्टीज़ को शामिल करना (ऑप्शनल)
यदि `properties.db2.jcc` में अतिरिक्त प्रॉपर्टीज़ निर्दिष्ट हैं, जैसे `currentSchema` या `sslConnection`, और आप उन्हें URL में शामिल करना चाहते हैं (हालाँकि कुछ को कनेक्शन प्रॉपर्टीज़ में सेट करना बेहतर हो सकता है), तो उन्हें डेटाबेस नाम के बाद एक कोलन (`:`) और सेमीकॉलन से अलग किए गए `property=value` जोड़े के साथ जोड़ें। उदाहरण के लिए:

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" currentSchema="MYSCHEMA" sslConnection="true"/>
```

URL हो सकता है:

```
jdbc:db2://localhost:50000/SAMPLE:currentSchema=MYSCHEMA;sslConnection=true;
```

हालाँकि:
- `sslConnection=true` जैसी प्रॉपर्टीज़ अक्सर `Properties` ऑब्जेक्ट या डेटा सोर्स कॉन्फ़िगरेशन में सेट की जाती हैं, न कि URL में।
- यह पुष्टि करने के लिए DB2 JDBC ड्राइवर डॉक्यूमेंटेशन चेक करें कि कौन सी प्रॉपर्टीज़ URL में वैध हैं बनिस्बत उनके जिनके लिए अलग कॉन्फ़िगरेशन की आवश्यकता होती है।

### अंतिम उत्तर
आपके क्वेरी के संदर्भ में, यह मानते हुए कि `properties.db2.jcc` कम से कम `databaseName`, `serverName`, और `portNumber` प्रदान करता है, JDBC URL इस प्रकार बनाया जाता है:

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

`<serverName>`, `<portNumber>`, और `<databaseName>` को आपकी `properties.db2.jcc` कॉन्फ़िगरेशन के वास्तविक वैल्यूज़ से बदल दें। यदि अतिरिक्त प्रॉपर्टीज़ मौजूद हैं और URL के लिए इरादा हैं, तो उन्हें `:property1=value1;property2=value2;` के रूप में जोड़ें, लेकिन आमतौर पर, `user`, `password`, और `sslConnection` जैसी प्रॉपर्टीज़ को कनेक्शन सेटअप में अलग से हैंडल किया जाता है।