---
audio: false
generated: true
lang: hi
layout: post
title: जावा में एसएएसएल प्रमाणीकरण
translated: true
type: note
---

Java में `javax.security.sasl` पैकेज का उपयोग करने के लिए, आपको क्लाइंट-सर्वर एप्लिकेशन में प्रमाणीकरण और, वैकल्पिक रूप से, डेटा सुरक्षा के लिए Simple Authentication and Security Layer (SASL) मैकेनिज्म को लागू करने के लिए इसकी कक्षाओं और इंटरफेस का लाभ उठाने की आवश्यकता है। इसमें शामिल प्राथमिक कक्षाएं `Sasl`, `SaslClient`, और `SaslServer` हैं। नीचे इस पैकेज का उपयोग करने के तरीके पर एक व्यापक मार्गदर्शिका दी गई है, जिसमें क्लाइंट और सर्वर दोनों कार्यान्वयन के लिए चरण और उदाहरण कोड शामिल हैं।

---

### **javax.security.sasl का अवलोकन**
`javax.security.sasl` पैकेज SASL प्रमाणीकरण के लिए एक फ्रेमवर्क प्रदान करता है, जो आमतौर पर LDAP, IMAP, या कस्टम एप्लिकेशन जैसे प्रोटोकॉल में उपयोग किया जाता है। इसमें शामिल हैं:
- **`Sasl`**: एक यूटिलिटी क्लास जिसमें `SaslClient` और `SaslServer` इंस्टेंस बनाने के लिए स्टैटिक मेथड होती हैं।
- **`SaslClient`**: SASL प्रमाणीकरण प्रक्रिया के क्लाइंट पक्ष का प्रतिनिधित्व करता है।
- **`SaslServer`**: SASL प्रमाणीकरण प्रक्रिया के सर्वर पक्ष का प्रतिनिधित्व करता है।
- **`CallbackHandler`**: एक इंटरफेस जिसे आप प्रमाणीकरण कॉलबैक (जैसे, यूजरनेम या पासवर्ड प्रदान करना) को संभालने के लिए लागू करते हैं।

इस प्रक्रिया में एक `SaslClient` या `SaslServer` बनाना, प्रमाणीकरण डेटा को प्रबंधित करने के लिए एक कॉलबैक हैंडलर प्रदान करना, और प्रमाणीकरण पूरा होने तक एक चैलेंज-रिस्पांस एक्सचेंज में शामिल होना शामिल है।

---

### **javax.security.sasl का उपयोग करने के चरण**

#### **1. अपनी भूमिका निर्धारित करें (क्लाइंट या सर्वर)**
तय करें कि आपका एप्लिकेशन क्लाइंट (सर्वर को प्रमाणित करना) के रूप में कार्य करता है या सर्वर (क्लाइंट को प्रमाणित करना)। यह निर्धारित करता है कि आप `SaslClient` या `SaslServer` का उपयोग करेंगे।

#### **2. एक SASL मैकेनिज्म चुनें**
SASL विभिन्न मैकेनिज्म का समर्थन करता है, जैसे:
- `PLAIN`: सरल यूजरनेम/पासवर्ड प्रमाणीकरण (कोई एन्क्रिप्शन नहीं)।
- `DIGEST-MD5`: चैलेंज-रिस्पांस के साथ पासवर्ड-आधारित।
- `GSSAPI`: Kerberos-आधारित प्रमाणीकरण।

क्लाइंट और सर्वर दोनों द्वारा समर्थित एक मैकेनिज्म चुनें। सरलता के लिए, यह मार्गदर्शिका उदाहरण के रूप में `PLAIN` मैकेनिज्म का उपयोग करती है।

#### **3. एक CallbackHandler लागू करें**
प्रमाणीकरण क्रेडेंशियल प्रदान करने या सत्यापित करने के लिए एक `CallbackHandler` आवश्यक है। आपको `javax.security.auth.callback.CallbackHandler` इंटरफेस को लागू करने की आवश्यकता होगी।

- **क्लाइंट के लिए**: यूजरनेम और पासवर्ड जैसे क्रेडेंशियल प्रदान करें।
- **सर्वर के लिए**: क्लाइंट क्रेडेंशियल सत्यापित करें या सर्वर-साइड प्रमाणीकरण डेटा प्रदान करें।

यहाँ `PLAIN` मैकेनिज्म के लिए एक क्लाइंट-साइड `CallbackHandler` का उदाहरण दिया गया है:

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

सर्वर के लिए, आप एक डेटाबेस के विरुद्ध क्रेडेंशियल सत्यापित कर सकते हैं:

```java
public class ServerCallbackHandler implements CallbackHandler {
    @Override
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                String username = ((NameCallback) callback).getName();
                // डेटाबेस से यूजरनेम के लिए अपेक्षित पासवर्ड प्राप्त करें
            } else if (callback instanceof PasswordCallback) {
                // सत्यापन के लिए अपेक्षित पासवर्ड सेट करें
                ((PasswordCallback) callback).setPassword("expectedPassword".toCharArray());
            } else if (callback instanceof AuthorizeCallback) {
                AuthorizeCallback ac = (AuthorizeCallback) callback;
                ac.setAuthorized(ac.getAuthenticationID().equals(ac.getAuthorizationID()));
            }
        }
    }
}
```

#### **4. क्लाइंट-साइड कार्यान्वयन**
क्लाइंट के रूप में प्रमाणित करने के लिए:

1. **एक SaslClient बनाएं**:
   मैकेनिज्म, प्रोटोकॉल, सर्वर नाम, गुण और कॉलबैक हैंडलर के साथ `Sasl.createSaslClient` का उपयोग करें।

   ```java
   import javax.security.sasl.Sasl;
   import javax.security.sasl.SaslClient;
   import java.util.HashMap;

   String[] mechanisms = {"PLAIN"};
   String authorizationId = null; // वैकल्पिक; null यदि प्रमाणीकरण ID के समान है
   String protocol = "ldap"; // उदा., "ldap", "imap"
   String serverName = "myserver.example.com";
   HashMap<String, Object> props = null; // वैकल्पिक गुण, उदा., QoP
   CallbackHandler cbh = new ClientCallbackHandler("user", "pass");

   SaslClient sc = Sasl.createSaslClient(mechanisms, authorizationId, protocol, serverName, props, cbh);
   ```

2. **चैलेंज-रिस्पांस एक्सचेंज को संभालें**:
   - प्रारंभिक प्रतिक्रिया के लिए जांचें (क्लाइंट-फर्स्ट मैकेनिज्म जैसे `PLAIN` में आम)।
   - सर्वर को प्रतिक्रियाएं भेजें और प्रमाणीकरण पूरा होने तक चैलेंज प्रोसेस करें।

   ```java
   byte[] response = sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) : null;
   if (response != null) {
       // सर्वर को प्रतिक्रिया भेजें (प्रोटोकॉल-विशिष्ट, उदा., सॉकेट या LDAP BindRequest के माध्यम से)
   }

   // सर्वर चैलेंज प्राप्त करें (प्रोटोकॉल-विशिष्ट)
   byte[] challenge = /* सर्वर से पढ़ें */;
   while (!sc.isComplete()) {
       response = sc.evaluateChallenge(challenge);
       // सर्वर को प्रतिक्रिया भेजें
       if (sc.isComplete()) break;
       challenge = /* सर्वर से अगला चैलेंज पढ़ें */;
   }

   // प्रमाणीकरण पूरा हो गया है; प्रोटोकॉल-विशिष्ट साधनों के माध्यम से सफलता की जांच करें
   ```

   `PLAIN` के लिए, क्लाइंट प्रारंभिक प्रतिक्रिया में क्रेडेंशियल भेजता है, और सर्वर आमतौर पर आगे के चैलेंज के बिना सफलता या विफलता के साथ प्रतिक्रिया करता है।

#### **5. सर्वर-साइड कार्यान्वयन**
क्लाइंट को सर्वर के रूप में प्रमाणित करने के लिए:

1. **एक SaslServer बनाएं**:
   मैकेनिज्म, प्रोटोकॉल, सर्वर नाम, गुण और कॉलबैक हैंडलर के साथ `Sasl.createSaslServer` का उपयोग करें।

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

2. **चैलेंज-रिस्पांस एक्सचेंज को संभालें**:
   - क्लाइंट की प्रारंभिक प्रतिक्रिया को प्रोसेस करें और प्रमाणीकरण पूरा होने तक चैलेंज जनरेट करें।

   ```java
   byte[] response = /* क्लाइंट से प्रारंभिक प्रतिक्रिया पढ़ें */;
   byte[] challenge = ss.evaluateResponse(response != null ? response : new byte[0]);
   // क्लाइंट को चैलेंज भेजें (प्रोटोकॉल-विशिष्ट)

   while (!ss.isComplete()) {
       response = /* क्लाइंट से अगली प्रतिक्रिया पढ़ें */;
       challenge = ss.evaluateResponse(response);
       if (ss.isComplete()) {
           // प्रमाणीकरण पूरा
           break;
       }
       // क्लाइंट को चैलेंज भेजें
   }

   if (ss.isComplete()) {
       String authorizedUser = ss.getAuthorizationID();
       // अधिकृत उपयोगकर्ता के साथ आगे बढ़ें
   }
   ```

   `PLAIN` के लिए, सर्वर प्रारंभिक प्रतिक्रिया में क्रेडेंशियल सत्यापित करता है और अतिरिक्त चैलेंज के बिना प्रमाणीकरण पूरा करता है।

#### **6. वैकल्पिक: सुरक्षा परतों का उपयोग करें**
यदि मैकेनिज्म (जैसे `DIGEST-MD5`) एक सुरक्षा परत का समर्थन करता है:
- प्रमाणीकरण के बाद संदेशों को एन्क्रिप्ट/डिक्रिप्ट करने के लिए क्लाइंट पर `sc.wrap()` और `sc.unwrap()`, या सर्वर पर `ss.wrap()` और `ss.unwrap()` का उपयोग करें।
- `PLAIN` सुरक्षा परतों का समर्थन नहीं करता है।

---

### **मुख्य बिंदु**
- **एकीकरण**: SASL एक्सचेंज को अपने एप्लिकेशन के संचार प्रोटोकॉल (जैसे, LDAP Bind अनुरोध, IMAP AUTHENTICATE कमांड) में एम्बेड करें।
- **त्रुटि प्रबंधन**: `SaslException` और अन्य संभावित त्रुटियों को संभालने के लिए कोड को try-catch ब्लॉक में लपेटें।
- **गुण**: यदि मैकेनिज्म द्वारा समर्थित है, तो सुरक्षा की गुणवत्ता (`"javax.security.sasl.qop"`) जैसे विकल्पों को कॉन्फ़िगर करने के लिए `props` मैप का उपयोग करें।

---

### **उदाहरण उपयोग मामला**
`PLAIN` के साथ प्रमाणीकरण करने वाले एक LDAP क्लाइंट के लिए:
1. `PLAIN` मैकेनिज्म के साथ एक `SaslClient` बनाएं।
2. मैकेनिज्म और प्रारंभिक प्रतिक्रिया (`sc.evaluateChallenge(new byte[0])`) के साथ एक LDAP `BindRequest` भेजें।
3. सफलता की पुष्टि करने के लिए सर्वर के `BindResponse` को प्रोसेस करें।

एक कस्टम प्रोटोकॉल के लिए, LDAP-विशिष्ट चरणों को अपने प्रोटोकॉल की प्रमाणीकरण कमांड से बदलें।

---

इन चरणों का पालन करके, आप अपने चुने हुए मैकेनिज्म और प्रोटोकॉल के लिए प्रक्रिया को तैयार करते हुए, अपने Java एप्लिकेशन में SASL प्रमाणीकरण लागू करने के लिए `javax.security.sasl` का प्रभावी ढंग से उपयोग कर सकते हैं।