---
audio: false
generated: true
lang: hi
layout: post
title: प्रमाणन और अनुमति Java में
translated: true
---

`javax.security.auth` पैकेज का उपयोग करने के लिए, आपको यह समझना होगा कि यह Java Authentication and Authorization Service (JAAS) फ्रेमवर्क का हिस्सा है। इस पैकेज में उपयोगकर्ताओं (किसी को पहचानने) और उन्हें (क्या करने की अनुमति) के लिए सत्यापित करने के लिए क्लास और इंटरफेस प्रदान करते हैं। नीचे एक बुनियादी सत्यापन दृश्य के लिए `javax.security.auth` का उपयोग करने के लिए चरण-दर-चरण मार्गदर्शन है, जैसे कि उपयोगकर्ता का सत्यापन करने के लिए एक उपयोगकर्ता नाम और पासवर्ड।

---

### **मुख्य अवधारणाओं का संक्षिप्त विवरण**
चरणों में डूबने से पहले, `javax.security.auth` में निम्नलिखित मुख्य घटकों का संक्षिप्त विवरण है:

- **Subject**: एक सत्यापित होने वाला एंटिटी (जैसे, एक उपयोगकर्ता या सेवा) को दर्शाता है। इसमें कई पहचान (Principals) और प्रमाणपत्र (जैसे, पासवर्ड या सर्टिफिकेट) हो सकते हैं।
- **Principal**: एक Subject के साथ जुड़ी पहचान या भूमिका, जैसे कि उपयोगकर्ता नाम या समूह सदस्यता।
- **Credential**: एक Subject को सत्यापित करने के लिए उपयोग किया जाने वाला जानकारी, जैसे कि पासवर्ड या एक क्रिप्टोग्राफिक कुंजी।
- **LoginModule**: एक प्लग-इन घटक जो सत्यापन तर्क (जैसे, एक डेटाबेस के खिलाफ उपयोगकर्ता नाम और पासवर्ड की जांच) को पूरा करता है।
- **LoginContext**: एक या अधिक LoginModules का उपयोग करके सत्यापन प्रक्रिया को समन्वय करने वाला केंद्रित क्लास।
- **CallbackHandler**: उपयोगकर्ता के साथ बातचीत करने के लिए एक इंटरफेस, जैसे कि उपयोगकर्ता नाम और पासवर्ड के लिए प्रॉम्प्ट करना।

इन अवधारणाओं को ध्यान में रखते हुए, पैकेज का उपयोग करने की प्रक्रिया को समझने के लिए आगे बढ़ते हैं।

---

### **`javax.security.auth` का उपयोग करने के चरण**

#### **1. एक JAAS कॉन्फ़िगरेशन सेट अप करें**
सत्यापन प्रक्रिया एक कॉन्फ़िगरेशन पर निर्भर करती है जो यह निर्धारित करती है कि कौन सी `LoginModule`(s) का उपयोग करना है। यह एक कॉन्फ़िगरेशन फ़ाइल में या प्रोग्रामेटिक रूप से परिभाषित किया जा सकता है।

उदाहरण के लिए, एक फ़ाइल बनाएं जिसका नाम `jaas.config` है और निम्नलिखित सामग्री के साथ:

```
MyApp {
    com.example.MyLoginModule required;
};
```

- **`MyApp`**: एप्लिकेशन या सन्दर्भ का नाम, जिसे आप अपने कोड में संदर्भित करेंगे।
- **`com.example.MyLoginModule`**: आपके कस्टम `LoginModule` का पूर्ण रूप से क्वालीफाइड नाम (आप इसे बाद में लागू करेंगे)।
- **`required`**: एक फ्लैग जो यह दर्शाता है कि इस मॉड्यूल को सत्यापन के लिए सफल होना चाहिए। अन्य फ्लैगों में `requisite`, `sufficient`, और `optional` शामिल हैं, जो कई मॉड्यूलों के साथ अधिक जटिल तर्क के साथ अनुमति देते हैं।

इस फ़ाइल को सेट करने के लिए सिस्टम गुण को सेट करें:

```java
System.setProperty("java.security.auth.login.config", "jaas.config");
```

या तो, आप कॉन्फ़िगरेशन को प्रोग्रामेटिक रूप से सेट कर सकते हैं, लेकिन अधिकांश मामलों में एक फ़ाइल अधिक सरल है।

#### **2. एक CallbackHandler लागू करें**
एक `CallbackHandler` उपयोगकर्ता से इनपुट इकट्ठा करता है, जैसे कि उपयोगकर्ता नाम और पासवर्ड। यहाँ एक सरल प्रोग्रामेटिक रूप से कंसोल का उपयोग करते हुए लागू करने का उदाहरण है:

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

- **NameCallback**: उपयोगकर्ता नाम के लिए प्रॉम्प्ट करता है और प्राप्त करता है।
- **PasswordCallback**: पासवर्ड के लिए प्रॉम्प्ट करता है और प्राप्त करता है (सुरक्षा के लिए एक `char[]` के रूप में संग्रहीत किया जाता है)।

#### **3. एक LoginModule लागू करें**
एक `LoginModule` सत्यापन तर्क को परिभाषित करता है। नीचे एक बुनियादी उदाहरण है जो एक हार्डकोडेड उपयोगकर्ता नाम और पासवर्ड के खिलाफ जांच करता है (प्रैक्टिस में, आप एक डेटाबेस या बाहरी सेवा का उपयोग करेंगे):

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

    // मॉड्यूल को प्रारंभ करें
    public void initialize(Subject subject, CallbackHandler callbackHandler,
                           Map<String, ?> sharedState, Map<String, ?> options) {
        this.subject = subject;
        this.callbackHandler = callbackHandler;
    }

    // सत्यापन करना
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

            // हार्डकोडेड जांच (प्रैक्टिस में वास्तविक तर्क से बदलें)
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

    // सत्यापन को समर्पित करें (Subject में Principals को जोड़ें)
    public boolean commit() throws LoginException {
        if (succeeded) {
            subject.getPrincipals().add(new MyPrincipal("myuser"));
            return true;
        }
        return false;
    }

    // सत्यापन प्रक्रिया को रद्द करें
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

// सरल Principal लागू
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

- **login()**: `CallbackHandler` का उपयोग करके प्रमाणपत्र प्राप्त करता है और उन्हें जांचता है।
- **commit()**: यदि सत्यापन सफल होता है, तो एक `Principal` को `Subject` में जोड़ता है।
- **abort()** और **logout()**: साफ़-सफाई या रद्द करने का प्रबंधन करते हैं।

#### **4. LoginContext का उपयोग करके सत्यापित करें**
अब, `LoginContext` का उपयोग करके मुख्य एप्लिकेशन में सत्यापन करने के लिए:

```java
import javax.security.auth.login.*;
import java.security.Principal;

public class Main {
    public static void main(String[] args) {
        // JAAS कॉन्फ़िगरेशन सेट हो
        System.setProperty("java.security.auth.login.config", "jaas.config");

        try {
            // कॉन्फ़िगरेशन नाम और CallbackHandler के साथ LoginContext बनाएं
            LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler());

            // सत्यापन करना
            lc.login();

            // सत्यापित Subject प्राप्त करें
            Subject subject = lc.getSubject();
            System.out.println("Authenticated subject: " + subject);

            // Subject के Principals को प्रिंट करें
            for (Principal p : subject.getPrincipals()) {
                System.out.println("Principal: " + p.getName());
            }

            // जब खत्म हो जाए, तो लॉगआउट करें
            lc.logout();
        } catch (LoginException e) {
            System.err.println("Authentication failed: " + e.getMessage());
        }
    }
}
```

- **`LoginContext lc = new LoginContext("MyApp", new MyCallbackHandler())`**: `"MyApp"` कॉन्फ़िगरेशन से जुड़ता है और `MyCallbackHandler` का उपयोग करता है।
- **`lc.login()`**: सत्यापन प्रक्रिया को ट्रिगर करता है।
- **`lc.getSubject()`**: सत्यापित `Subject` प्राप्त करता है।

#### **5. सत्यापित कार्य (वैकल्पिक) करना**
सत्यापित होने के बाद, आप `Subject` का उपयोग करके अपने विशेषाधिकारों के साथ कोड को कार्यान्वित कर सकते हैं, `Subject.doAs()` का उपयोग करके:

```java
import java.security.PrivilegedAction;

Subject.doAs(subject, new PrivilegedAction<Void>() {
    public Void run() {
        System.out.println("Running as: " + Subject.getSubject(java.security.AccessController.getContext()));
        // यहाँ विशेषाधिकार कार्य करें
        return null;
    }
});
```

यह सत्यापन के लिए उपयोगी है, जहां कार्य `Subject` के `Principals` के आधार पर सीमित होते हैं।

---

### **सब कुछ एक साथ**
1. **कॉन्फ़िगरेशन**: `jaas.config` में अपने `LoginModule` के साथ परिभाषित करें।
2. **CallbackHandler**: उपयोगकर्ता इनपुट इकट्ठा करने के लिए `MyCallbackHandler` लागू करें।
3. **LoginModule**: अपने सत्यापन तर्क के साथ `MyLoginModule` लागू करें।
4. **मुख्य कोड**: `LoginContext` का उपयोग करके सत्यापित करें और एक `Subject` प्राप्त करें।
5. **सत्यापन**: आवश्यकता के अनुसार `Subject.doAs()` के लिए विशेषाधिकार कार्य करें।

जब आप `Main` क्लास चलाते हैं, तो यह:
- उपयोगकर्ता नाम और पासवर्ड के लिए प्रॉम्प्ट करेगा।
- `MyLoginModule` का उपयोग करके सत्यापित करेगा।
- यदि सफल, तो `Subject` और उसके `Principals` को प्रिंट करेगा।

---

### **अतिरिक्त टिप्पणियाँ**
- **वास्तविक उपयोग**: `MyLoginModule` में हार्डकोडेड प्रमाणपत्रों को एक डेटाबेस, LDAP, या अन्य सेवा के खिलाफ जांचों से बदलें। Java में मानक मॉड्यूल जैसे `Krb5LoginModule` (Kerberos) या `JndiLoginModule` (LDAP) उपलब्ध हैं, लेकिन उन्हें अतिरिक्त सेटअप की आवश्यकता हो सकती है।
- **कई LoginModules**: कॉन्फ़िगरेशन में कई मॉड्यूलों को फ्लैग (`required`, `sufficient`, आदि) के साथ परिभाषित किया जा सकता है, जिससे जटिल सत्यापन प्रवाह बनाया जा सकता है।
- **सुरक्षा**: सुरक्षित अभ्यासों का उपयोग करें, जैसे कि पासवर्ड के लिए `String` का उपयोग करने से बचें (`char[]` का उपयोग करें) और मौजूदा सुरक्षा फ्रेमवर्कों के साथ एकीकृत करें।

यह गाइड Java में सत्यापन और सत्यापन के लिए `javax.security.auth` का उपयोग करने के लिए बुनियादी बातें कवर करता है!