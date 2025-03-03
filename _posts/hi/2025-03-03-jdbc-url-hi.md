---
audio: false
generated: true
lang: hi
layout: post
title: JDBC URL बनाएं
translated: true
---

WebSphere Liberty Profile में `server.xml` फ़ाइल के `properties.db2.jcc` तत्व के आधार पर एक DB2 डेटाबेस से जुड़ने के लिए एक JDBC URL बनाना, आपको कुछ मुख्य गुणों जैसे `databaseName`, `serverName`, और `portNumber` के लिए दिए गए मानों का उपयोग करना होगा। यहाँ कैसे करना है:

### DB2 के लिए आधारभूत JDBC URL प्रारूप
DB2 JDBC Type 4 ड्राइवर (जो आमतौर पर Liberty Profile सेटअप में उपयोग किया जाता है) का उपयोग करते हुए एक JDBC URL का मानक प्रारूप है:

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

- **`jdbc:db2://`** - यह एक DB2 डेटाबेस के लिए एक टाइप 4 ड्राइवर का उपयोग करते हुए एक सीधा नेटवर्क कनेक्शन को दर्शाने वाला प्रोटोकॉल पहचानकर्ता है।
- **`<serverName>`** - DB2 सर्वर का होस्टनेम या आईपी एड्रेस, जो `properties.db2.jcc` में `serverName` गुण द्वारा निर्दिष्ट किया गया है।
- **`<portNumber>`** - DB2 इंस्टेंस जो `portNumber` गुण द्वारा निर्दिष्ट किया गया है, जिस पर सुनता है (अगर निर्दिष्ट नहीं किया गया है तो आमतौर पर डिफ़ॉल्ट `50000` है).
- **`<databaseName>`** - जोड़ने के लिए डेटाबेस का नाम, जो `databaseName` गुण द्वारा निर्दिष्ट किया गया है।

### URL बनाना के कदम
1. **आवश्यक गुणों को पहचानें**: `server.xml` में `properties.db2.jcc` तत्व से `serverName`, `portNumber`, और `databaseName` के लिए मान निकालें। ये URL के लिए आवश्यक घटक हैं।
2. **URL को संयोजित करें**: इन मानों को ऊपर दिए गए प्रारूप में संयोजित करें, सही अलगाव चिह्नों (`:` सर्वर और पोर्ट के बीच, डेटाबेस नाम से पहले `/`) के साथ।
3. **अन्य गुणों का समावेश (अगर मौजूद हैं)**: अगर `properties.db2.jcc` में अन्य गुण मौजूद हैं (जैसे `currentSchema`, `sslConnection`), तो कभी-कभी URL में जोड़े जा सकते हैं, लेकिन यह उनके स्वभाव पर निर्भर करता है। आमतौर पर गुण जैसे `user` और `password` जब कनेक्शन स्थापित किया जाता है, तो अलग से प्रदान किए जाते हैं, सुरक्षा के लिए।

### उदाहरण
यदि आपका `server.xml` निम्नलिखित `properties.db2.jcc` संरचना को शामिल करता है:

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

- `user` और `password` URL में शामिल नहीं हैं; वे आमतौर पर JDBC ड्राइवर के माध्यम से कनेक्शन प्राप्त करने के समय अलग से प्रदान किए जाते हैं (जैसे एक `DataSource` या `DriverManager` के माध्यम से).

### अतिरिक्त गुणों को शामिल करना (वैकल्पिक)
यदि `properties.db2.jcc` में अतिरिक्त गुण निर्दिष्ट हैं, जैसे `currentSchema` या `sslConnection`, और आप उन्हें URL में शामिल करना चाहते हैं (हालांकि कुछ को कनेक्शन गुणों में सेट करने के लिए बेहतर होगा), तो डेटाबेस नाम के बाद एक कोलन (`:`) के साथ, और सेमी-कोलन-सेपरेटेड `property=value` जोड़ों के साथ उन्हें जोड़ें। उदाहरण के लिए:

```xml
<properties.db2.jcc databaseName="SAMPLE" serverName="localhost" portNumber="50000" currentSchema="MYSCHEMA" sslConnection="true"/>
```

URL बन सकता है:

```
jdbc:db2://localhost:50000/SAMPLE:currentSchema=MYSCHEMA;sslConnection=true;
```

हालांकि:
- गुण जैसे `sslConnection=true` आमतौर पर एक `Properties` वस्तु या डेटा स्रोत संरचना में सेट किए जाते हैं, URL में नहीं।
- DB2 JDBC ड्राइवर दस्तावेज़ को जांचें कि कौन से गुण URL में वैध हैं और कौन से अलग संरचना की आवश्यकता होती हैं।

### अंतिम उत्तर
आपके प्रश्न के संदर्भ में, यदि `properties.db2.jcc` कम से कम `databaseName`, `serverName`, और `portNumber` प्रदान करता है, तो JDBC URL बनाया जाता है:

```
jdbc:db2://<serverName>:<portNumber>/<databaseName>
```

`<serverName>`, `<portNumber>`, और `<databaseName>` को आपकी `properties.db2.jcc` संरचना से वास्तविक मानों से बदलें। यदि अतिरिक्त गुण मौजूद हैं और URL के लिए इरादे हैं, तो उन्हें `:property1=value1;property2=value2;` के रूप में जोड़ें, लेकिन आमतौर पर गुण जैसे `user`, `password`, और `sslConnection` कनेक्शन सेटअप में अलग से संभाले जाते हैं।