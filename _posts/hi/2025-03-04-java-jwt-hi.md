---
audio: false
generated: true
lang: hi
layout: post
title: जावा जेडब्ल्यूटी लाइब्रेरी
translated: true
type: note
---

JSON Web Token (JWT) से समाप्ति तिथि, जारीकरण तिथि और अन्य क्लेम जैसी जानकारी निकालने के लिए Java में `com.nimbusds.jwt` लाइब्रेरी का उपयोग करने के लिए, नीचे दिए गए चरणों का पालन करें। यह समाधान मानता है कि आप एक साइन किए गए JWT के साथ काम कर रहे हैं, जो सबसे आम प्रकार है, और आपके लक्ष्य को प्राप्त करने के लिए एक स्पष्ट, व्यावहारिक दृष्टिकोण प्रदान करने पर केंद्रित है।

---

## पूर्वापेक्षाएँ

सबसे पहले, सुनिश्चित करें कि आपने Nimbus JOSE + JWT लाइब्रेरी अपने प्रोजेक्ट में जोड़ दी है। यदि आप Maven का उपयोग कर रहे हैं, तो अपनी `pom.xml` फ़ाइल में निम्नलिखित डिपेंडेंसी शामिल करें:

```xml
<dependency>
    <groupId>com.nimbusds</groupId>
    <artifactId>nimbus-jose-jwt</artifactId>
    <version>9.37</version> <!-- नवीनतम संस्करण के साथ बदलें -->
</dependency>
```

आप नवीनतम संस्करण [Maven Central](https://mvnrepository.com/artifact/com.nimbusds/nimbus-jose-jwt) पर जाँच सकते हैं।

---

## समाप्ति तिथि, जारीकरण तिथि और अन्य क्लेम निकालने के चरण

यहाँ बताया गया है कि आप `com.nimbusds.jwt` लाइब्रेरी का उपयोग करके एक JWT को पार्स कैसे कर सकते हैं और समाप्ति तिथि, जारीकरण तिथि और अतिरिक्त क्लेम कैसे प्राप्त कर सकते हैं:

1.  **JWT स्ट्रिंग को पार्स करें**: JWT स्ट्रिंग को `SignedJWT` ऑब्जेक्ट में बदलने के लिए `SignedJWT.parse()` मेथड का उपयोग करें।
2.  **क्लेम सेट प्राप्त करें**: JWT से क्लेम (की-वैल्यू पेयर) तक पहुँचने के लिए `getJWTClaimsSet()` का उपयोग करें।
3.  **विशिष्ट क्लेम निकालें**:
    *   समाप्ति तिथि (`exp` क्लेम) के लिए `getExpirationTime()` का उपयोग करें।
    *   जारीकरण तिथि (`iat` क्लेम) के लिए `getIssueTime()` का उपयोग करें।
    *   अतिरिक्त क्लेम के लिए `getSubject()`, `getClaim()`, या अन्य मेथड का उपयोग करें।
4.  **त्रुटियों को हैंडल करें**: संभावित पार्सिंग समस्याओं को प्रबंधित करने के लिए पार्सिंग लॉजिक को try-catch ब्लॉक में लपेटें।

---

## उदाहरण कोड

नीचे एक संपूर्ण Java उदाहरण दिया गया है जो दर्शाता है कि JWT से समाप्ति तिथि, जारीकरण तिथि और एक अतिरिक्त क्लेम (जैसे, विषय) कैसे निकाला जाता है:

```java
import com.nimbusds.jwt.SignedJWT;
import com.nimbusds.jwt.JWTClaimsSet;
import java.text.ParseException;
import java.util.Date;

public class JwtExtractor {

    public static void main(String[] args) {
        // इसे अपनी वास्तविक JWT स्ट्रिंग से बदलें
        String jwtString = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyMzk5MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

        try {
            // चरण 1: JWT स्ट्रिंग को पार्स करें
            SignedJWT signedJWT = SignedJWT.parse(jwtString);

            // चरण 2: क्लेम सेट प्राप्त करें
            JWTClaimsSet claimsSet = signedJWT.getJWTClaimsSet();

            // चरण 3: समाप्ति और जारीकरण तिथियाँ निकालें
            Date expirationDate = claimsSet.getExpirationTime();
            Date issuedDate = claimsSet.getIssueTime();
            String subject = claimsSet.getSubject(); // किसी अन्य क्लेम का उदाहरण

            // चरण 4: परिणाम प्रदर्शित करें
            if (expirationDate != null) {
                System.out.println("Expiration date: " + expirationDate);
            } else {
                System.out.println("No expiration date set.");
            }

            if (issuedDate != null) {
                System.out.println("Issued date: " + issuedDate);
            } else {
                System.out.println("No issued date set.");
            }

            if (subject != null) {
                System.out.println("Subject: " + subject);
            } else {
                System.out.println("No subject set.");
            }

        } catch (ParseException e) {
            System.out.println("Invalid JWT: " + e.getMessage());
        }
    }
}
```

---

## कोड की व्याख्या

### 1. **इम्पोर्ट्स**
- `SignedJWT`: एक साइन किए गए JWT को रिप्रेजेंट करता है और इसे पार्स व प्रोसेस करने के लिए मेथड प्रदान करता है।
- `JWTClaimsSet`: JWT पेलोड से क्लेम रखता है।
- `ParseException`: तब थ्रो होती है जब JWT स्ट्रिंग मैलफॉर्म्ड हो या पार्स न हो सके।
- `Date`: समाप्ति और जारीकरण समय को रिप्रेजेंट करने के लिए उपयोग किया जाता है।

### 2. **JWT को पार्स करना**
- `SignedJWT.parse(jwtString)` मेथड एक JWT स्ट्रिंग (जैसे, `header.payload.signature`) लेती है और एक `SignedJWT` ऑब्जेक्ट रिटर्न करती है। यदि JWT अमान्य है, तो यह एक `ParseException` थ्रो करती है।

### 3. **क्लेम तक पहुँचना**
- `signedJWT.getJWTClaimsSet()` क्लेम सेट रिट्रीव करता है, जो JWT के पेलोड के सभी क्लेम रखता है।

### 4. **विशिष्ट क्लेम निकालना**
- **`getExpirationTime()`**: `exp` क्लेम को `Date` ऑब्जेक्ट के रूप में रिटर्न करता है (या `null` यदि मौजूद न हो)। यह दर्शाता है कि टोकन कब समाप्त होता है।
- **`getIssueTime()`**: `iat` क्लेम को `Date` ऑब्जेक्ट के रूप में रिटर्न करता है (या `null` यदि मौजूद न हो)। यह दर्शाता है कि टोकन कब जारी किया गया था।
- **`getSubject()`**: `sub` क्लेम को `String` के रूप में रिटर्न करता है (या `null` यदि मौजूद न हो), यह एक अन्य मानक क्लेम का उदाहरण है। आप कस्टम क्लेम को `Object` के रूप में रिट्रीव करने के लिए `getClaim("key")` का भी उपयोग कर सकते हैं।

### 5. **त्रुटि प्रबंधन**
- try-catch ब्लॉक यह सुनिश्चित करता है कि यदि JWT मैलफॉर्म्ड या अमान्य है, तो प्रोग्राम त्रुटि संदेश प्रिंट करके त्रुटि को सही तरीके से हैंडल करता है।

---

## नोट्स

- **साइन्ड बनाम अनसाइन्ड JWTs**: यह उदाहरण साइन किए गए टोकन के लिए `SignedJWT` का उपयोग करता है। यदि आपके पास एक अनसाइन्ड JWT है, तो इसके बजाय `PlainJWT.parse(jwtString)` का उपयोग करें। अधिक जेनेरिक दृष्टिकोण के लिए, आप `JWTParser.parse(jwtString)` का उपयोग कर सकते हैं और फिर प्रकार (`SignedJWT`, `PlainJWT`, आदि) की जाँच instanceof का उपयोग करके कर सकते हैं।
- **सिग्नेचर वेरिफिकेशन**: यह कोड JWT के सिग्नेचर को वेरिफाई नहीं करता है। प्रोडक्शन एनवायरनमेंट में, आपको टोकन की प्रामाणिकता सुनिश्चित करने के लिए उचित कुंजी के साथ `signedJWT.verify(verifier)` का उपयोग करके सिग्नेचर को वेरिफाई करना चाहिए।
- **नल चेक्स**: क्लेम रिट्रीव करते समय हमेशा `null` की जाँच करें, क्योंकि वे वैकल्पिक हैं और हर JWT में मौजूद नहीं हो सकते हैं।
- **कस्टम क्लेम**: गैर-मानक क्लेम तक पहुँचने के लिए, `claimsSet.getClaim("claimName")` का उपयोग करें, जो एक `Object` रिटर्न करता है जिसे आप उचित प्रकार (जैसे, `String`, `Integer`) में कास्ट कर सकते हैं।

---

## नमूना आउटपुट

ऊपर दी गई उदाहरण JWT स्ट्रिंग के लिए:
```
Expiration date: Wed Jan 17 19:52:02 UTC 2018
Issued date: Wed Jan 17 19:50:22 UTC 2018
Subject: 1234567890
```

---

यह दृष्टिकोण `com.nimbusds.jwt` लाइब्रेरी का उपयोग करके JWT से समाप्ति तिथि, जारीकरण तिथि और अन्य क्लेम निकालने का एक सरल और प्रभावी तरीका प्रदान करता है। `jwtString` को अपने स्वयं के टोकन से बदलें और कोड को अपनी विशिष्ट आवश्यकताओं के अनुकूल बनाएं!