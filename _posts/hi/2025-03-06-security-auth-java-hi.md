---
audio: false
generated: true
lang: hi
layout: post
title: जावा में प्रमाणीकरण और प्राधिकरण
translated: true
type: note
---

Java में `javax.security.auth` पैकेज का उपयोग करने के लिए, आपको यह समझना होगा कि यह Java Authentication and Authorization Service (JAAS) फ्रेमवर्क का हिस्सा है। यह पैकेज यूजर्स को प्रमाणित करने (यह सत्यापित करने कि वे कौन हैं) और उन्हें अधिकृत करने (यह निर्धारित करने कि वे क्या कर सकते हैं) के लिए classes और interfaces प्रदान करता है। नीचे एक बुनियादी प्रमाणीकरण परिदृश्य, जैसे यूजरनेम और पासवर्ड के साथ एक यूजर को प्रमाणित करने, के लिए `javax.security.auth` का उपयोग करने का चरण-दर-चरण मार्गदर्शिका दी गई है।

---

### **मुख्य अवधारणाओं का अवलोकन**
चरणों में जाने से पहले, यहां `javax.security.auth` में मुख्य घटकों का संक्षिप्त विवरण दिया गया है:

- **Subject**: एक इकाई (जैसे, एक यूजर या सेवा) का प्रतिनिधित्व करता है जिसे प्रमाणित किया जा रहा है। इसकी कई पहचान (Principals) और क्रेडेंशियल्स (जैसे, पासवर्ड या सर्टिफिकेट) हो सकते हैं।
- **Principal**: एक Subject से जुड़ी एक पहचान या भूमिका, जैसे यूजरनेम या ग्रुप मेंबरशिप।
- **Credential**: एक Subject को प्रमाणित करने के लिए उपयोग की जाने वाली जानकारी, जैसे पासवर्ड या क्रिप्टोग्राफिक कुंजी।
- **LoginModule**: एक प्लग करने योग्य घटक जो प्रमाणीकरण लॉजिक को निष्पादित करता है (जैसे, डेटाबेस के विरुद्ध यूजरनेम और पासवर्ड की जांच करना)।
- **LoginContext**: केंद्रीय class जो एक या अधिक LoginModules का उपयोग करके प्रमाणीकरण प्रक्रिया का समन्वय करती है।
- **CallbackHandler**: यूजर के साथ इंटरैक्ट करने के लिए एक इंटरफेस, जैसे यूजरनेम और पासवर्ड के लिए संकेत देना।

इन अवधारणाओं को ध्यान में रखते हुए, आइए जानें कि पैकेज का उपयोग कैसे करें।

---

### **`javax.security.auth` का उपयोग करने के चरण**

#### **1. एक JAAS कॉन्फ़िगरेशन सेट अप करें**
प्रमाणीकरण प्रक्रिया एक कॉन्फ़िगरेशन पर निर्भर करती है जो निर्दिष्ट करती है कि किस `LoginModule`(s) का उपयोग करना है। इसे एक कॉन्फ़िगरेशन फ़ाइल में या प्रोग्रामेटिक रूप से परिभाषित किया जा सकता है।

उदाहरण के लिए, निम्नलिखित सामग्री के साथ `jaas.config` नामक एक फ़ाइल बनाएं:

```
MyApp {
    com.example.MyLoginModule required;
};
```

- **`MyApp`**: एप्लिकेशन या context का नाम, जिसे आप अपने कोड में संदर्भित करेंगे।
- **`com.example.MyLoginModule`**: आपके कस्टम `LoginModule` का पूरी तरह से योग्य नाम (आप इसे बाद में लागू करेंगे)।
- **`required`**: एक फ्लैग जो इंगित करता है कि प्रमाणीकरण पास होने के लिए इस मॉड्यूल का सफल होना आवश्यक है। अन्य फ्लैग्स में `requisite`, `sufficient`, और `optional` शामिल हैं, जो कई मॉड्यूल के साथ अधिक जटिल लॉजिक की अनुमति देते हैं।

सिस्टम प्रॉपर्टी को इस फ़ाइल की ओर इशारा करने के लिए सेट करें:

```java
System.setProperty("java.security.auth.login.config", "jaas.config");
```

वैकल्पिक रूप से, आप कॉन्फ़िगरेशन को प्रोग्रामेटिक रूप से सेट कर सकते हैं, लेकिन ज्यादातर मामलों के लिए एक फ़ाइल सरल होती है।

#### **2. एक CallbackHandler लागू करें**
एक `CallbackHandler` यूजर से इनपुट एकत्र करता है, जैसे यूजरनेम और पासवर्ड। कंसोल का उपयोग करके एक सरल कार्यान्वयन यहां दिया गया है:

```java
import javax.security.auth.callback.*;
import java.io.*;

public class MyCallbackHandler implements CallbackHandler {
    public void handle(Callback[] callbacks) throws IOException, UnsupportedCallbackException {
        for (Callback callback : callbacks) {
            if (callback instanceof NameCallback) {
                NameCallback nc = (NameCallback) callback;
                System.out.print(nc.getPrompt());
                nc.setName(System.console().readLine());
            } else if (callback instanceof PasswordCallback) {
                PasswordCallback pc = (PasswordCallback) callback;
                System.out.print(pc.getPrompt());
                pc.setPassword(System.console().readPassword());
            } else {
                throw new UnsupportedCallbackException(callback, "Unsupported callback");
            }
        }
    }
}
```

- **NameCallback**: यूजरनेम के लिए संकेत देता है और उसे प्राप्त करता है।
- **PasswordCallback**: पासवर्ड के लिए संकेत देता है और उसे प्राप्त करता है (सुरक्षा के लिए `char[]` के रूप में संग्रहीत)।

#### **3. एक LoginModule लागू करें**
एक `LoginModule` प्रमाणीकरण लॉजिक को परिभाषित करता है। नीचे एक बुनियादी उदाहरण दिया गया है जो एक हार्डकोडेड यूजरनेम और पासवर्ड के विरुद्ध जांच करता है (व्यवहार में, आप एक डेटाबेस या बाहरी सेवा का उपयोग करेंगे):

```java
import javax.security.auth.*;
import javax.security.auth.callback.*;
import javax.security.auth.login.*;
import javax.security.auth.spi.*;
import java.security.Principal;
import java.util.*;

public class MyLoginModule implements LoginModule {
    private Subject subject;
    private CallbackHandler callbackHandler;
    private boolean succeeded = false;

    // मॉड्यूल को इनिशियलाइज़ करें
    public void initialize(Subject subject, CallbackHandler callbackHandler,
                           Map<String, ?> sharedState, Map<String, ?> options) {
        this.subject = subject;
        this.callbackHandler = callbackHandler;
    }

    // प्रमाणीकरण करें
    public boolean login() throws LoginException {
        if (callbackHandler == null) {
            throw new LoginException("No callback handler provided");
        }

        try {
            NameCallback nameCallback = new NameCallback("Username: ");
            PasswordCallback passwordCallback = new PasswordCallback("Password: ", false);
            callbackHandler.handle(new Callback[]{nameCallback, passwordCallback});

            String username = nameCallback.getName();
            char[] password = passwordCallback.getPassword();

            // हार्डकोडेड जांच (व्यवहार में वास्तविक लॉजिक से बदलें)
            if ("myuser".equals(username) && "mypassword".equals(new String(password))) {
                succeeded = true;
                return true;
            } else {
                succeeded = false;
                throw new FailedLoginException("Authentication failed");
            }
        } catch (Exception e) {
            throw new LoginException("Login error: " + e.getMessage());
        }
    }

    // प्रमाणीकरण को कमिट करें (Subject में Principals जोड़ें)
    public boolean commit() throws LoginException {
        if (succeeded) {
            subject.getPrincipals().add(new MyPrincipal("myuser"));
            return true;
        }
        return false;
    }

    // प्रमाणीकरण प्रक्रिया को रोकें
    public boolean abort() throws LoginException {
        succeeded = false;
        return true;
    }

    // Subject को लॉगआउट करें
    public boolean logout() throws LoginException {
        subject.getPrincipals().clear();
        subject.getPublicCredentials().clear();
        subject.getPrivateCredentials().clear();
        return true;
    }
}

// सरल Principal कार्यान्वयन
class MyPrincipal implements Principal {
    private String name;

    public MyPrincipal(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
```

- **login()**: क्रेडेंशियल्स प्राप्त करने और उनकी जांच करने के लिए `CallbackHandler` का उपयोग करता है।
- **commit()**: यदि प्रमाणीकरण सफल होता है, तो `Subject` में एक `Principal` जोड़ता है।
- **abort()** और **logout()**: सफाई या रद्द करने को संभालते हैं।

#### **4. LoginContext का उपयोग करके प्रमाणित करें**
अब, अपने मुख्य एप्लिकेशन में प्रमाणीकरण करने के लिए `LoginContext` का उपयोग करें:

```java
import javax.security.auth.login.*;
import java.security.Principal;

public class Main {
    public static void main(String[] args) {
        // सुनिश्चित करें कि JAAS कॉन्फ़िगरेशन सेट है
        System.setProperty("java.security.auth.login.config", "jaas.config");

        try {
            // कॉन्फ़िगरेशन नाम और CallbackHandler के साथ LoginContext बनाएं
            LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler());

            // प्रमाणीकरण करें
            lc.login();

            // प्रमाणित Subject प्राप्त करें
            Subject subject = lc.getSubject();
            System.out.println("Authenticated subject: " + subject);

            // Subject के Principals प्रिंट करें
            for (Principal p : subject.getPrincipals()) {
                System.out.println("Principal: " + p.getName());
            }

            // काम पूरा होने पर लॉगआउट करें
            lc.logout();
        } catch (LoginException e) {
            System.err.println("Authentication failed: " + e.getMessage());
        }
    }
}
```

- **`LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler())`**: `"MyApp"` कॉन्फ़िगरेशन से लिंक करता है और `MyCallbackHandler` का उपयोग करता है।
- **`lc.login()`**: प्रमाणीकरण प्रक्रिया को ट्रिगर करता है।
- **`lc.getSubject()`**: प्रमाणित `Subject` को पुनः प्राप्त करता है।

#### **5. अधिकृत क्रियाएं करें (वैकल्पिक)**
एक बार प्रमाणित होने के बाद, आप `Subject` का उपयोग `Subject.doAs()` का उपयोग करके इसके विशेषाधिकारों के साथ कोड निष्पादित करने के लिए कर सकते हैं:

```java
import java.security.PrivilegedAction;

Subject.doAs(subject, new PrivilegedAction<Void>() {
    public Void run() {
        System.out.println("Running as: " + Subject.getSubject(java.security.AccessController.getContext()));
        // यहां विशेषाधिकार प्राप्त क्रियाएं करें
        return null;
    }
});
```

यह अधिकारीकरण के लिए उपयोगी है, जहां कार्यों को `Subject` के `Principals` के आधार पर प्रतिबंधित किया जाता है।

---

### **सभी को एक साथ रखना**
1.  **कॉन्फ़िगरेशन**: अपने `LoginModule` के साथ `jaas.config` को परिभाषित करें।
2.  **CallbackHandler**: यूजर इनपुट एकत्र करने के लिए `MyCallbackHandler` को लागू करें।
3.  **LoginModule**: अपनी प्रमाणीकरण लॉजिक के साथ `MyLoginModule` को लागू करें।
4.  **मुख्य कोड**: प्रमाणित करने और एक `Subject` को पुनः प्राप्त करने के लिए `LoginContext` का उपयोग करें।
5.  **अधिकारीकरण**: यदि आवश्यक हो तो विशेषाधिकार प्राप्त कार्यों के लिए `Subject.doAs()` का उपयोग करें।

जब आप `Main` class चलाते हैं, तो यह होगा:
- यूजरनेम और पासवर्ड के लिए संकेत देगा।
- `MyLoginModule` का उपयोग करके प्रमाणित करेगा।
- यदि सफल होता है तो `Subject` और उसके `Principals` को प्रिंट करेगा।

---

### **अतिरिक्त नोट्स**
- **वास्तविक दुनिया का उपयोग**: `MyLoginModule` में हार्डकोडेड क्रेडेंशियल्स को डेटाबेस, LDAP, या किसी अन्य सेवा के विरुद्ध जांच से बदलें। Java मानक मॉड्यूल जैसे `Krb5LoginModule` (Kerberos) या `JndiLoginModule` (LDAP) प्रदान करता है, लेकिन उन्हें अतिरिक्त सेटअप की आवश्यकता हो सकती है।
- **एकाधिक LoginModules**: कॉन्फ़िगरेशन जटिल प्रमाणीकरण प्रवाह बनाने के लिए फ्लैग्स (`required`, `sufficient`, आदि) के साथ कई मॉड्यूल निर्दिष्ट कर सकता है।
- **सुरक्षा**: सुरक्षित प्रथाओं का उपयोग करें, जैसे पासवर्ड के लिए `String` से बचना (`char[]` का उपयोग करें) और मौजूदा सुरक्षा फ्रेमवर्क के साथ एकीकृत करना।

यह मार्गदर्शिका Java में प्रमाणीकरण और अधिकारीकरण के लिए `javax.security.auth` का उपयोग करने की मूल बातें कवर करती है!