---
audio: false
generated: true
lang: hi
layout: post
title: SASL प्रमाणन Java में
translated: true
---

`javax.security.sasl` पैकेज का उपयोग करने के लिए Java में, आप इसके क्लास और इंटरफेस का उपयोग करके Simple Authentication and Security Layer (SASL) मेकैनिज्म को क्लाइंट-सर्वर एप्लिकेशन में ऑथेंटिकेशन और, विकल्प के तौर पर, डेटा सिक्योरिटी के लिए लागू कर सकते हैं। मुख्य क्लास जो शामिल हैं, `Sasl`, `SaslClient`, और `SaslServer` हैं। नीचे एक व्यापक गाइड है कि इस पैकेज का उपयोग करने के लिए, जिसमें क्लाइंट और सर्वर दोनों के लिए चरण और उदाहरण कोड शामिल हैं।

---

### **javax.security.sasl का संक्षिप्त परिचय**
`javax.security.sasl` पैकेज SASL ऑथेंटिकेशन के लिए एक फ्रेमवर्क प्रदान करता है, जो प्रोटोकॉल जैसे LDAP, IMAP, या कस्टम एप्लिकेशन में आम तौर पर उपयोग किया जाता है। इसमें शामिल हैं:
- **`Sasl`**: एक यूटीलीटी क्लास है जिसमें स्टैटिक मेथड्स हैं `SaslClient` और `SaslServer` इंस्टेंस बनाने के लिए।
- **`SaslClient`**: SASL ऑथेंटिकेशन प्रक्रिया के क्लाइंट पक्ष को दर्शाता है।
- **`SaslServer`**: SASL ऑथेंटिकेशन प्रक्रिया के सर्वर पक्ष को दर्शाता है।
- **`CallbackHandler`**: एक इंटरफेस है जिसे आप ऑथेंटिकेशन कॉलबैक्स (जैसे, यूजरनेम या पासवर्ड प्रदान करने) को हैंडल करने के लिए लागू करते हैं।

प्रक्रिया में एक `SaslClient` या `SaslServer` बनाना शामिल है, ऑथेंटिकेशन डेटा को प्रबंधित करने के लिए एक कॉलबैक हैंडलर प्रदान करना, और ऑथेंटिकेशन पूरा होने तक चैलेंज-रिस्पॉन्स एक्सचेंज में शामिल होना।

---

### **javax.security.sasl का उपयोग करने के चरण**

#### **1. अपना भूमिका निर्धारित करें (क्लाइंट या सर्वर)**
तय करें कि आपका एप्लिकेशन एक क्लाइंट (एक सर्वर के साथ ऑथेंटिकेशन) के रूप में काम करता है या एक सर्वर (एक क्लाइंट को ऑथेंटिकेट करता है)। यह तय करता है कि आप `SaslClient` या `SaslServer` का उपयोग करेंगे।

#### **2. एक SASL मेकैनिज्म चुनें**
SASL विभिन्न मेकैनिज्म का समर्थन करता है, जैसे:
- `PLAIN`: सरल यूजरनेम/पासवर्ड ऑथेंटिकेशन (कोई एन्क्रिप्शन नहीं).
- `DIGEST-MD5`: पासवर्ड-आधारित चैलेंज-रिस्पॉन्स.
- `GSSAPI`: Kerberos-आधारित ऑथेंटिकेशन.

एक मेकैनिज्म चुनें जो दोनों क्लाइंट और सर्वर द्वारा समर्थित है। सरलता के लिए, इस गाइड में `PLAIN` मेकैनिज्म का उदाहरण के रूप में उपयोग किया जाता है।

#### **3. एक CallbackHandler लागू करें**
एक `CallbackHandler` ऑथेंटिकेशन क्रेडेंशियल प्रदान या सत्यापित करने के लिए आवश्यक है। आपको `javax.security.auth.callback.CallbackHandler` इंटरफेस लागू करना होगा।

- **एक क्लाइंट के लिए**: यूजरनेम और पासवर्ड जैसे क्रेडेंशियल प्रदान करें।
- **एक सर्वर के लिए**: क्लाइंट क्रेडेंशियल सत्यापित करें या सर्वर-साइड ऑथेंटिकेशन डेटा प्रदान करें।

यह एक क्लाइंट-साइड `CallbackHandler` के लिए `PLAIN` मेकैनिज्म का उदाहरण है:

```java
import javax.security.auth.callback.*;
import java.io.IOException;

public class ClientCallbackHandler implements CallbackHandler {
    private final String username;
    private final String password;

    public ClientCallbackHandler(String username, String password) {
        this.username = username;
        this.password = password;
    }

    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                ((NameCallback) callback).setName(username);
            } else if (callback instanceof PasswordCallback) {
                ((PasswordCallback) callback).setPassword(password.toCharArray());
            } else {
                throw new UnsupportedCallbackException(callback, "Unsupported callback");
            }
        }
    }
}
```

सर्वर के लिए, आप क्रेडेंशियल को डेटाबेस के साथ सत्यापित कर सकते हैं:

```java
public class ServerCallbackHandler implements CallbackHandler {
    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                String username = ((NameCallback) callback).getName();
                // Retrieve expected password for username from a database
            } else if (callback instanceof PasswordCallback) {
                // Set the expected password for verification
                ((PasswordCallback) callback).setPassword("expectedPassword".toCharArray());
            } else if (callback instanceof AuthorizeCallback) {
                AuthorizeCallback ac = (AuthorizeCallback) callback;
                ac.setAuthorized(ac.getAuthenticationID().equals(ac.getAuthorizationID()));
            }
        }
    }
}
```

#### **4. क्लाइंट-साइड इम्प्लिमेंटेशन**
एक क्लाइंट के रूप में ऑथेंटिकेट करने के लिए:

1. **एक SaslClient बनाएं**:
   `Sasl.createSaslClient` का उपयोग करें, मेकैनिज्म, प्रोटोकॉल, सर्वर नाम, प्रॉपर्टीज, और कॉलबैक हैंडलर के साथ।

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslClient;
   import java.util.HashMap;

   String[] mechanisms = {"PLAIN"};
   String authorizationId = null; // विकल्प; यदि ऑथेंटिकेशन आईडी के साथ समान है तो null
   String protocol = "ldap"; // उदाहरण के लिए, "ldap", "imap"
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null; // विकल्प प्रॉपर्टीज, उदाहरण के लिए, QoP
   CallbackHandler cbh = new ClientCallbackHandler("user", "pass");

   SaslClient sc = Sasl.createSaslClient(mechanisms, authorizationId, protocol, serverName, props, cbh);
   ```

2. **चैलेंज-रिस्पॉन्स एक्सचेंज को हैंडल करें**:
   - एक प्रारंभिक रिस्पॉन्स की जांच करें (क्लाइंट-फर्स्ट मेकैनिज्म जैसे `PLAIN` में आम है).
   - सर्वर को रिस्पॉन्स भेजें और चैलेंजों को प्रोसेस करें जब तक ऑथेंटिकेशन पूरा नहीं हो जाता।

   ```java
   byte[] response = sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) : null;
   if (response != null) {
       // रिस्पॉन्स को सर्वर भेजें (प्रोटोकॉल-विशिष्ट, उदाहरण के लिए, सोकेट या LDAP BindRequest के माध्यम से)
   }

   // सर्वर चैलेंज पढ़ें (प्रोटोकॉल-विशिष्ट)
   byte[] challenge = /* read from server */;
   while (!sc.isComplete()) {
       response = sc.evaluateChallenge(challenge);
       // रिस्पॉन्स को सर्वर भेजें
       if (sc.isComplete()) break;
       challenge = /* read next challenge from server */;
   }

   // ऑथेंटिकेशन पूरा है; सफलता की जांच करें प्रोटोकॉल-विशिष्ट तरीकों से
   ```

   `PLAIN` के लिए, क्लाइंट प्रारंभिक रिस्पॉन्स में क्रेडेंशियल भेजता है, और सर्वर आम तौर पर सफलता या विफलता के बिना और अधिक चैलेंज के साथ जवाब देता है।

#### **5. सर्वर-साइड इम्प्लिमेंटेशन**
एक क्लाइंट को सर्वर के रूप में ऑथेंटिकेट करने के लिए:

1. **एक SaslServer बनाएं**:
   `Sasl.createSaslServer` का उपयोग करें, मेकैनिज्म, प्रोटोकॉल, सर्वर नाम, प्रॉपर्टीज, और कॉलबैक हैंडलर के साथ।

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslServer;
   import java.util.HashMap;

   String mechanism = "PLAIN";
   String protocol = "ldap";
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null;
   CallbackHandler cbh = new ServerCallbackHandler();

   SaslServer ss = Sasl.createSaslServer(mechanism, protocol, serverName, props, cbh);
   ```

2. **चैलेंज-रिस्पॉन्स एक्सचेंज को हैंडल करें**:
   - क्लाइंट के प्रारंभिक रिस्पॉन्स को प्रोसेस करें और चैलेंज बनाएं जब तक ऑथेंटिकेशन पूरा नहीं हो जाता।

   ```java
   byte[] response = /* read initial response from client */;
   byte[] challenge = ss.evaluateResponse(response != null ? response : new byte[0]);
   // चैलेंज को क्लाइंट भेजें (प्रोटोकॉल-विशिष्ट)

   while (!ss.isComplete()) {
       response = /* read next response from client */;
       challenge = ss.evaluateResponse(response);
       if (ss.isComplete()) {
           // ऑथेंटिकेशन पूरा
           break;
       }
       // चैलेंज को क्लाइंट भेजें
   }

   if (ss.isComplete()) {
       String authorizedUser = ss.getAuthorizationID();
       // ऑथोराइज्ड यूजर के साथ आगे बढ़ें
   }
   ```

   `PLAIN` के लिए, सर्वर प्रारंभिक रिस्पॉन्स में क्रेडेंशियल सत्यापित करता है और और अधिक चैलेंज के बिना ऑथेंटिकेशन पूरा करता है।

#### **6. विकल्प: सिक्योरिटी लेयर का उपयोग करें**
यदि मेकैनिज्म (जैसे, `DIGEST-MD5`) एक सिक्योरिटी लेयर का समर्थन करता है:
- क्लाइंट पर `sc.wrap()` और `sc.unwrap()` का उपयोग करें, या सर्वर पर `ss.wrap()` और `ss.unwrap()` का उपयोग करें, ऑथेंटिकेशन के बाद संदेशों को एन्क्रिप्ट/डिक्रिप्ट करने के लिए।
- `PLAIN` सिक्योरिटी लेयर का समर्थन नहीं करता।

---

### **मुख्य बिंदु**
- **इंटिग्रेशन**: SASL एक्सचेंज को आपकी एप्लिकेशन की संचार प्रोटोकॉल में एम्बेड करें (जैसे, LDAP Bind अनुरोध, IMAP AUTHENTICATE कमांड).
- **एरर हैंडलिंग**: कोड को `SaslException` और अन्य संभावित त्रुटियों को हैंडल करने के लिए try-catch ब्लॉक्स में लपेटें।
- **प्रॉपर्टीज**: मेकैनिज्म द्वारा समर्थित विकल्पों जैसे गुणवत्ता के संरक्षण (`"javax.security.sasl.qop"`) को कॉन्फ़िगर करने के लिए `props` माप का उपयोग करें।

---

### **उदाहरण उपयोग मामला**
एक LDAP क्लाइंट `PLAIN` के साथ ऑथेंटिकेट करने के लिए:
1. एक `SaslClient` बनाएं `PLAIN` मेकैनिज्म के साथ।
2. एक LDAP `BindRequest` भेजें मेकैनिज्म और प्रारंभिक रिस्पॉन्स (`sc.evaluateChallenge(new byte[0])`) के साथ.
3. सर्वर के `BindResponse` को प्रोसेस करें सफलता की पुष्टि करने के लिए।

एक कस्टम प्रोटोकॉल के लिए, LDAP-विशिष्ट चरणों को आपकी प्रोटोकॉल के ऑथेंटिकेशन कमांडों से बदलें।

---

इन चरणों का पालन करके, आप `javax.security.sasl` का उपयोग करके अपने Java एप्लिकेशन में SASL ऑथेंटिकेशन लागू कर सकते हैं, प्रक्रिया को अपने चुने गए मेकैनिज्म और प्रोटोकॉल के अनुसार अनुकूलित करते हुए।