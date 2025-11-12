---
audio: false
generated: true
lang: hi
layout: post
title: ओरेकल जेडीबीसी ड्राइवर
translated: true
type: note
---

Oracle JDBC (Java Database Connectivity) ड्राइवर Java एप्लिकेशन्स को Oracle डेटाबेस से कनेक्ट होने और इंटरैक्ट करने की अनुमति देते हैं। मैं मुख्य घटकों और उनके उपयोग के तरीके को समझाता हूँ।

Oracle JDBC कनेक्शन के लिए मुख्य क्लास `oracle.jdbc.driver.OracleDriver` है, हालांकि नए वर्जन में आप अक्सर `oracle.jdbc.OracleDriver` का उपयोग करेंगे (जो Oracle 10g के बाद से सुझाई गई क्लास है)।

यहाँ बताया गया है कि Java एप्लिकेशन में Oracle JDBC का उपयोग कैसे करें:

1. सबसे पहले, आपको अपने प्रोजेक्ट में Oracle JDBC ड्राइवर JAR (आमतौर पर ojdbc.jar) शामिल करनी होगी।

2. ड्राइवर क्लास लोड करें:
```java
Class.forName("oracle.jdbc.OracleDriver");
```

3. कनेक्शन URL का उपयोग करके कनेक्शन स्थापित करें:
```java
String url = "jdbc:oracle:thin:@hostname:port:SID";
// या सर्विस नाम आधारित कनेक्शन के लिए
// String url = "jdbc:oracle:thin:@//hostname:port/service_name";
String username = "your_username";
String password = "your_password";

Connection connection = DriverManager.getConnection(url, username, password);
```

4. स्टेटमेंट बनाएं और एक्सेक्यूट करें:
```java
Statement statement = connection.createStatement();
ResultSet resultSet = statement.executeQuery("SELECT * FROM employees");

while (resultSet.next()) {
    // प्रत्येक पंक्ति को प्रोसेस करें
    String name = resultSet.getString("name");
    System.out.println(name);
}
```

5. काम पूरा होने पर हमेशा रिसोर्सेज बंद करें:
```java
resultSet.close();
statement.close();
connection.close();
```

Oracle JDBC ड्राइवर कई प्रकार के आते हैं:
- Thin ड्राइवर: Pure Java इम्प्लीमेंटेशन जिसे Oracle क्लाइंट इंस्टॉलेशन की आवश्यकता नहीं होती
- OCI ड्राइवर: Oracle Call Interface का उपयोग करता है और Oracle क्लाइंट सॉफ्टवेयर की आवश्यकता होती है
- Kerberos ड्राइवर: Kerberos ऑथेंटिकेशन के लिए
- JDBC-OCI ड्राइवर: JDBC और OCI का कॉम्बिनेशन

Thin ड्राइवर सबसे अधिक इस्तेमाल किया जाता है क्योंकि इसके लिए क्लाइंट मशीन पर अतिरिक्त Oracle क्लाइंट सॉफ्टवेयर की आवश्यकता नहीं होती।

क्या आप Oracle JDBC उपयोग के कनेक्शन पूलिंग, prepared statements, या किसी अन्य पहलू के बारे में अधिक विशिष्ट जानकारी चाहेंगे?