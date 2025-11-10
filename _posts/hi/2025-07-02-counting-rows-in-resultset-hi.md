---
audio: false
generated: true
lang: hi
layout: post
title: स्क्रॉल करने योग्य रिजल्टसेट में पंक्तियों की गिनती
translated: true
type: note
---

जावा में, जब आप `ResultSet` के साथ काम कर रहे होते हैं (उदाहरण के लिए, `Statement.executeQuery()` के माध्यम से), पंक्तियों की गिनती करना मुश्किल हो सकता है यदि `fetchSize` को `0` पर सेट किया गया है (जिसका अर्थ है कि JDBC ड्राइवर आवश्यकतानुसार पंक्तियाँ प्राप्त करेगा)। इसके अलावा, स्क्रॉल करने योग्य परिणाम सेट ( `ResultSet.TYPE_SCROLL_INSENSITIVE` या `ResultSet.TYPE_SCROLL_SENSITIVE` का उपयोग करके) का उपयोग करने से आप परिणाम सेट में नेविगेट कर सकते हैं, लेकिन इसके लिए अधिक मेमोरी की आवश्यकता होती है क्योंकि पंक्तियाँ मेमोरी में लोड हो जाती हैं।

यहाँ एक रणनीति है जिसका आप उपयोग कर सकते हैं `ResultSet` में पंक्तियों की गिनती करने के लिए बिना परिणाम सेट के पूर्ण ट्रैवर्सल के। यह `ResultSet` की `scrollable` सुविधा और "अंतिम पंक्ति पर जाने" और "पंक्ति संख्या प्राप्त करने" की क्षमता का उपयोग करती है।

### स्क्रॉल करने योग्य `ResultSet` का उपयोग करके पंक्तियों की गिनती करने के चरण:

1. **एक स्क्रॉल करने योग्य ResultSet बनाएँ**: उचित कर्सर प्रकार सेट करके एक `Statement` का उपयोग करना सुनिश्चित करें जो स्क्रॉल करने योग्य परिणाम सेट उत्पन्न कर सकता है।
2. **अंतिम पंक्ति पर जाएँ**: स्क्रॉल करने योग्य परिणाम सेट आपको `last()` का उपयोग करके अंतिम पंक्ति पर जाने की अनुमति देता है।
3. **पंक्ति संख्या प्राप्त करें**: अंतिम पंक्ति पर जाने के बाद, आप पंक्तियों की संख्या निर्धारित करने के लिए `getRow()` को कॉल कर सकते हैं।
4. **वैकल्पिक**: यदि आपको परिणाम सेट के माध्यम से पुनरावृति करने की आवश्यकता है, तो `first()` का उपयोग करके वापस पहली पंक्ति पर जाएँ।

यहाँ जावा में एक उदाहरण कार्यान्वयन दिया गया है:

```java
import java.sql.*;

public class RowCountExample {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/your_database";
        String username = "your_username";
        String password = "your_password";
        
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        
        try {
            conn = DriverManager.getConnection(url, username, password);
            stmt = conn.createStatement(
                    ResultSet.TYPE_SCROLL_INSENSITIVE, 
                    ResultSet.CONCUR_READ_ONLY);
            rs = stmt.executeQuery("SELECT * FROM your_table");
            
            // Move to the last row to count the total number of rows
            if (rs.last()) {
                int rowCount = rs.getRow();
                System.out.println("Total rows: " + rowCount);
                
                // Optionally, move back to the first row
                rs.first();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            try {
                if (rs != null) rs.close();
                if (stmt != null) stmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```

### मुख्य बिंदु:

* **स्क्रॉल करने योग्य ResultSet**: हम `ResultSet.TYPE_SCROLL_INSENSITIVE` का उपयोग करके एक स्क्रॉल करने योग्य `ResultSet` बनाते हैं। इस प्रकार का परिणाम सेट आपको अंतिम पंक्ति पर जाने और पंक्ति गिनती प्राप्त करने की अनुमति देता है।
* **पंक्ति गिनती**: `rs.getRow()` विधि वर्तमान पंक्ति संख्या लौटाती है जब कर्सर अंतिम पंक्ति पर स्थित होता है। यह मान प्रभावी रूप से परिणाम सेट में पंक्तियों की कुल संख्या होती है।
* **फ़ेच आकार**: यदि `fetchSize` `0` है, तो ड्राइवर पंक्तियों को गतिशील रूप से प्राप्त करता है, लेकिन स्क्रॉल करने योग्य परिणाम सेट का उपयोग करने से हम पंक्तियों में कुशलतापूर्वक नेविगेट कर सकते हैं।

### सर्वोत्तम अभ्यास:

* **मेमोरी दक्षता**: जबकि स्क्रॉल करने योग्य परिणाम सेट पंक्तियों की गिनती के लिए उपयोगी हैं, ध्यान रखें कि वे अधिक मेमोरी की खपत कर सकते हैं, क्योंकि सभी पंक्तियों को मेमोरी में लोड करने की आवश्यकता होती है। यदि आप एक बड़े डेटासेट के साथ काम कर रहे हैं, और मेमोरी उपयोग एक चिंता का विषय है, तो एक अलग दृष्टिकोण (जैसे कि `last()` के बिना पंक्तियों को वृद्धिशील रूप से गिनने के लिए परिणाम सेट पर पुनरावृति करना) पर विचार करें।
* **वैकल्पिक दृष्टिकोण**: यदि मेमोरी एक मुद्दा है और आपको केवल पंक्ति गिनती चाहिए, तो आप पूरा परिणाम सेट प्राप्त करने के बजाय एक `SELECT COUNT(*)` क्वेरी निष्पादित कर सकते हैं। यह अक्सर अधिक कुशल होता है।

```sql
SELECT COUNT(*) FROM your_table;
```

यदि आपको और स्पष्टीकरण की आवश्यकता है तो मुझे बताएं!