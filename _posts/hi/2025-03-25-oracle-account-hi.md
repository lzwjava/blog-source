---
audio: false
generated: true
lang: hi
layout: post
title: ओरेकल डेटाबेस - उपयोगकर्ता खाता
translated: true
type: note
---

`ORA-28000: The account is locked` त्रुटि तब होती है जब आप Oracle डेटाबेस से कनेक्ट होने का प्रयास करते हैं (उदाहरण के लिए, एक thin JDBC ड्राइवर के माध्यम से) और आप जिस यूजर अकाउंट का उपयोग करना चाह रहे हैं, वह लॉक हो गया है। यह आमतौर पर लॉगिन प्रयासों की बहुत अधिक विफलताओं, एक एडमिनिस्ट्रेटर द्वारा मैन्युअल लॉकिंग, या एक अकाउंट एक्सपायरी पॉलिसी के कारण होता है। इसे ठीक करने के लिए, आपको अकाउंट को अनलॉक करने की आवश्यकता होती है, और यदि आवश्यक हो, तो पासवर्ड रीसेट करें या अकाउंट की स्थिति जांचें। नीचे Oracle डेटाबेस से कनेक्ट होते समय इस समस्या को ठीक करने के चरण दिए गए हैं।

---

### ORA-28000 को ठीक करने के चरण

#### 1. **त्रुटि सत्यापित करें**
   जब आपको JDBC कनेक्शन में यह त्रुटि मिलती है, तो यह इस तरह दिख सकती है:
   ```
   java.sql.SQLException: ORA-28000: The account is locked
   ```
   यह पुष्टि करता है कि समस्या डेटाबेस अकाउंट के साथ है, JDBC कॉन्फ़िगरेशन (जैसे URL, ड्राइवर, या WebSphere डेटासोर्स सेटिंग्स) के साथ नहीं।

#### 2. **एक विशेषाधिकार प्राप्त यूजर के रूप में लॉग इन करें**
   अकाउंट को अनलॉक करने के लिए, आपको प्रशासनिक विशेषाधिकारों वाले डेटाबेस यूजर (जैसे `SYS`, `SYSTEM`, या `DBA` भूमिका वाला यूजर) की पहुंच की आवश्यकता होती है। SQL*Plus, SQL Developer, या JDBC क्लाइंट जैसे टूल का उपयोग करके डेटाबेस से कनेक्ट करें:
   ```bash
   sqlplus / as sysdba
   ```
   या
   ```bash
   sqlplus system/<password>@<service_name>
   ```
   `<password>` और `<service_name>` को अपने वास्तविक क्रेडेंशियल्स और डेटाबेस सर्विस नाम (जैसे `ORCL`) से बदलें।

#### 3. **अकाउंट की स्थिति जांचें**
   लॉक किए गए अकाउंट की स्थिति जांचने के लिए निम्न SQL क्वेरी चलाएँ:
   ```sql
   SELECT username, account_status, lock_date 
   FROM dba_users 
   WHERE username = 'YOUR_USERNAME';
   ```
   - `YOUR_USERNAME` को उस यूजरनेम से बदलें जिससे आप कनेक्ट करने का प्रयास कर रहे हैं (जैसे `myuser`)।
   - `ACCOUNT_STATUS` कॉलम देखें। यदि यह `LOCKED` या `LOCKED(TIMED)` कहता है, तो अकाउंट लॉक है।

   उदाहरण आउटपुट:
   ```
   USERNAME   ACCOUNT_STATUS   LOCK_DATE
   ---------- ---------------- -------------------
   MYUSER     LOCKED           24-MAR-25 10:00:00
   ```

#### 4. **अकाउंट को अनलॉक करें**
   अकाउंट को अनलॉक करने के लिए, विशेषाधिकार प्राप्त यूजर के रूप में इस SQL कमांड को निष्पादित करें:
   ```sql
   ALTER USER your_username ACCOUNT UNLOCK;
   ```
   उदाहरण:
   ```sql
   ALTER USER myuser ACCOUNT UNLOCK;
   ```

#### 5. **(वैकल्पिक) पासवर्ड रीसेट करें**
   यदि पासवर्ड एक्सपायर हो गया हो या आपको संदेह हो कि यह गलत है, तो इसे रीसेट कर दें:
   ```sql
   ALTER USER your_username IDENTIFIED BY new_password;
   ```
   उदाहरण:
   ```sql
   ALTER USER myuser IDENTIFIED BY mynewpass123;
   ```
   - रीसेट करने के बाद, अपने WebSphere `server.xml` (या जहाँ भी JDBC डेटासोर्स कॉन्फ़िगर किया गया है) में पासवर्ड अपडेट करें और यदि आवश्यक हो तो इसे फिर से एन्क्रिप्ट करें (AES एन्कोडिंग चरणों के लिए अपने पिछले प्रश्न देखें)।

#### 6. **परिवर्तनों को कमिट करें (यदि आवश्यक हो)**
   ज्यादातर मामलों में, `ALTER USER` कमांड तुरंत प्रभावी हो जाती हैं और `COMMIT` की आवश्यकता नहीं होती है। हालाँकि, यदि आप एक ट्रांजैक्शन-हेवी वातावरण में हैं, तो सत्र या डेटाबेस को यदि आवश्यक हो तो रीस्टार्ट करके रोलबैक न होने सुनिश्चित करें।

#### 7. **कनेक्शन का परीक्षण करें**
   अपने JDBC एप्लिकेशन या एक सरल परीक्षण का उपयोग करके फिर से कनेक्ट करने का प्रयास करें:
   ```java
   import java.sql.Connection;
   import java.sql.DriverManager;

   public class TestJDBC {
       public static void main(String[] args) throws Exception {
           String url = "jdbc:oracle:thin:@//localhost:1521/ORCL";
           String user = "myuser";
           String password = "mynewpass123";
           Connection conn = DriverManager.getConnection(url, user, password);
           System.out.println("Connection successful!");
           conn.close();
       }
   }
   ```
   - `url`, `user`, और `password` को अपने वातावरण के अनुसार अपडेट करें।
   - यदि यह काम करता है, तो अपने WebSphere डेटासोर्स कॉन्फ़िगरेशन को तदनुसार अपडेट करें।

#### 8. **प्रोफाइल पॉलिसियों की जांच करें (भविष्य की लॉक को रोकें)**
   अकाउंट यूजर की प्रोफाइल में एक सुरक्षा नीति (जैसे `FAILED_LOGIN_ATTEMPTS` या `PASSWORD_LOCK_TIME`) के कारण लॉक हो सकता है। यूजर को असाइन की गई प्रोफाइल जांचें:
   ```sql
   SELECT profile 
   FROM dba_users 
   WHERE username = 'YOUR_USERNAME';
   ```
   फिर, प्रोफाइल की सीमाओं का निरीक्षण करें:
   ```sql
   SELECT resource_name, limit 
   FROM dba_profiles 
   WHERE profile = 'YOUR_PROFILE_NAME';
   ```
   इनकी तलाश करें:
   - `FAILED_LOGIN_ATTEMPTS`: लॉक होने से पहले विफल प्रयासों की संख्या (जैसे `10`)।
   - `PASSWORD_LOCK_TIME`: लॉक की अवधि (जैसे `1` दिन)।

   इन सेटिंग्स को आराम देने के लिए (यदि उचित हो), प्रोफाइल को संशोधित करें:
   ```sql
   ALTER PROFILE your_profile_name LIMIT 
       FAILED_LOGIN_ATTEMPTS UNLIMITED 
       PASSWORD_LOCK_TIME UNLIMITED;
   ```
   उदाहरण:
   ```sql
   ALTER PROFILE DEFAULT LIMIT FAILED_LOGIN_ATTEMPTS UNLIMITED;
   ```

#### 9. **WebSphere रीस्टार्ट करें (यदि आवश्यक हो)**
   यदि आप WebSphere का उपयोग कर रहे हैं और डेटासोर्स पासवर्ड अपडेट किया है, तो परिवर्तनों के प्रभावी होने सुनिश्चित करने के लिए एप्लिकेशन सर्वर को रीस्टार्ट करें:
   - Liberty के लिए: `./bin/server stop` और `./bin/server start`।
   - पारंपरिक WebSphere के लिए: Admin Console या `stopServer.sh`/`startServer.sh` का उपयोग करें।

---

### ORA-28000 के सामान्य कारण
- **लॉगिन प्रयासों की बहुत अधिक विफलताएं**: पिछले कनेक्शन त्रुटियों के लिए एप्लिकेशन लॉग या WebSphere लॉग (जैसे `SystemOut.log`) जांचें।
- **मैन्युअल लॉक**: एक एडमिन ने जानबूझकर अकाउंट को लॉक किया हो सकता है (`ALTER USER myuser ACCOUNT LOCK`)।
- **एक्सपायर्ड अकाउंट**: कुछ वातावरण पासवर्ड एक्सपायर होने पर अकाउंट को लॉक कर देते हैं। `dba_users` में `EXPIRY_DATE` जांचें।

---

### समस्या निवारण सुझाव
- यदि आपके पास `SYS` या `SYSTEM` एक्सेस नहीं है, तो अकाउंट को अनलॉक करने के लिए अपने डेटाबेस एडमिनिस्ट्रेटर से संपर्क करें।
   - पुनः प्रयास करने से पहले `server.xml` में JDBC URL, यूजरनेम और पासवर्ड सही हैं यह सुनिश्चित करें।
   - यदि समस्या बनी रहती है, तो सत्यापित करें कि Oracle लिसनर चल रहा है:
  ```bash
  lsnrctl status
  ```

मुझे बताएं कि क्या आपको कोई अतिरिक्त त्रुटियाँ मिलती हैं या किसी विशिष्ट चरण में सहायता की आवश्यकता है!