---
audio: false
generated: true
lang: hi
layout: post
title: जावा एसक्यूएल स्टेटमेंट प्रकारों की तुलना
translated: true
type: note
---

Java के `java.sql` पैकेज में, `Statement`, `PreparedStatement`, और `CallableStatement` इंटरफेस SQL क्वेरीज़ को execute करने के लिए उपयोग किए जाते हैं, लेकिन उनके अलग-अलग उद्देश्य और विशेषताएं हैं। यहाँ एक संक्षिप्त तुलना दी गई है:

1. **Statement**:
   - **उद्देश्य**: बिना पैरामीटर वाली static SQL क्वेरीज़ को execute करने के लिए उपयोग किया जाता है।
   - **यह कैसे काम करता है**: आप एक पूर्ण SQL क्वेरी को स्ट्रिंग के रूप में `executeQuery()` या `executeUpdate()` मेथड में पास करते हैं।
   - **मुख्य विशेषताएँ**:
     - सरल, एक-बार की जाने वाली क्वेरीज़ के लिए उपयुक्त।
     - कोई पैरामीटर बाइंडिंग नहीं, इसलिए आप मानों को SQL स्ट्रिंग में मैन्युअल रूप से जोड़ते हैं, जिससे SQL इंजेक्शन का खतरा हो सकता है।
     - दोहराई जाने वाली क्वेरीज़ के लिए कम कुशल, क्योंकि डेटाबेस हर बार SQL को फिर से पार्स करता है।
   - **उदाहरण**:
     ```java
     Statement stmt = conn.createStatement();
     ResultSet rs = stmt.executeQuery("SELECT * FROM users WHERE id = 1");
     ```

2. **PreparedStatement**:
   - **उद्देश्य**: पैरामीटराइज्ड इनपुट वाली precompiled SQL क्वेरीज़ के लिए उपयोग किया जाता है।
   - **यह कैसे काम करता है**: आप प्लेसहोल्डर्स (`?`) के साथ एक क्वेरी को परिभाषित करते हैं और `setInt()`, `setString()` आदि जैसी मेथड्स का उपयोग करके पैरामीटर मान सेट करते हैं।
   - **मुख्य विशेषताएँ**:
     - SQL लॉजिक को डेटा से अलग करके SQL इंजेक्शन को रोकता है।
     - दोहराई जाने वाली क्वेरीज़ के लिए अधिक कुशल, क्योंकि SQL को एक बार कंपाइल करके बार-बार उपयोग किया जाता है।
     - डायनामिक पैरामीटर बाइंडिंग को सपोर्ट करता है, जो इसे सुरक्षित और अधिक लचीला बनाता है।
   - **उदाहरण**:
     ```java
     PreparedStatement pstmt = conn.prepareStatement("SELECT * FROM users WHERE id = ?");
     pstmt.setInt(1, 1);
     ResultSet rs = pstmt.executeQuery();
     ```

3. **CallableStatement**:
   - **उद्देश्य**: डेटाबेस में stored procedures को execute करने के लिए उपयोग किया जाता है।
   - **यह कैसे काम करता है**: `PreparedStatement` को extend करता है ताकि stored procedure कॉल्स को हैंडल कर सके, जो इनपुट (`IN`), आउटपुट (`OUT`), और इनपुट/आउटपुट (`IN OUT`) पैरामीटर्स को सपोर्ट करता है।
   - **मुख्य विशेषताएँ**:
     - विशेष रूप से डेटाबेस stored procedures के लिए डिज़ाइन किया गया।
     - `registerOutParameter()` जैसी मेथड्स का उपयोग करके आउटपुट पैरामीटर्स को रजिस्टर करने की अनुमति देता है।
     - stored procedure लॉजिक के लिए जटिल पैरामीटर हैंडलिंग को सपोर्ट करता है।
   - **उदाहरण**:
     ```java
     CallableStatement cstmt = conn.prepareCall("{call getUserName(?, ?)}");
     cstmt.setInt(1, 1);
     cstmt.registerOutParameter(2, Types.VARCHAR);
     cstmt.execute();
     String username = cstmt.getString(2);
     ```

**मुख्य अंतर**:
| फीचर                | Statement                          | PreparedStatement                  | CallableStatement                 |
|------------------------|------------------------------------|------------------------------------|------------------------------------|
| **उद्देश्य**            | Static SQL क्वेरीज़                | Parameterized SQL क्वेरीज़         | Stored procedure execution        |
| **SQL इंजेक्शन**      | Vulnerable (manual concatenation) | Safe (parameter binding)          | Safe (parameter binding)          |
| **परफॉर्मेंस**        | Less efficient (no precompilation)| More efficient (precompiled)      | Efficient for stored procedures   |
| **यूज़ केस**           | Simple, one-time queries          | Repeated or parameterized queries | Stored procedures with parameters|
| **पैरामीटर सपोर्ट**  | None                              | Input parameters only             | Input, output, and IN/OUT params |

**कब उपयोग करें**:
- `Statement` का उपयोग सरल, गैर-दोहराव वाली क्वेरीज़ के लिए करें जहां सुरक्षा और प्रदर्शन कम महत्वपूर्ण हों।
- `PreparedStatement` का उपयोग पैरामीटराइज्ड क्वेरीज़, दोहराव वाले execution, या जब सुरक्षा (SQL इंजेक्शन रोकथाम) एक चिंता का विषय हो, के लिए करें।
- `CallableStatement` का उपयोग तब करें जब इनपुट/आउटपुट पैरामीटर्स वाले डेटाबेस stored procedures को कॉल करना हो।

यह स्पष्टीकरण मेरे नॉलेज कटऑफ तक मानक Java SQL API व्यवहार पर आधारित है। यदि आपको और विवरण या उदाहरण चाहिए, तो मुझे बताएं!