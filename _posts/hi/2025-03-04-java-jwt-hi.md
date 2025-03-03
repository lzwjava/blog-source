---
audio: false
generated: true
lang: hi
layout: post
title: Java JWT Library का अनुवाद
translated: true
---

`com.nimbusds.jwt` लाइब्रेरी का उपयोग करके Java में JSON Web Token (JWT) से जैसे कि समाप्ति तिथि, जारी तिथि और अन्य दावों को निकालने के लिए नीचे दिए गए चरणों का पालन करें। यह समाधान मानता है कि आप एक साइन्ड JWT के साथ काम कर रहे हैं, जो सबसे आम प्रकार है, और लक्ष्य को प्राप्त करने के लिए एक स्पष्ट, व्यावहारिक दृष्टिकोण प्रदान करता है।

---

## पूर्वापेक्षाएँ

पहले, सुनिश्चित करें कि आपके प्रोजेक्ट में Nimbus JOSE + JWT लाइब्रेरी जोड़ दी गई है। अगर आप Maven का उपयोग कर रहे हैं, तो अपने `pom.xml` में निम्नलिखित निर्भरता शामिल करें:

```xml
<dependency>
    <groupId>com.nimbusds</groupId>
    <artifactId>nimbus-jose-jwt</artifactId>
    <version>9.37</version> <!-- नवीनतम संस्करण से बदलें -->
</dependency>
```

आप नवीनतम संस्करण को [Maven Central](https://mvnrepository.com/artifact/com.nimbusds/nimbus-jose-jwt) पर जांच सकते हैं।

---

## समाप्ति तिथि, जारी तिथि और अन्य दावों को निकालने के लिए चरण

नीचे दिए गए तरीके से एक JWT को पार्स करें और `com.nimbusds.jwt` लाइब्रेरी का उपयोग करके समाप्ति तिथि, जारी तिथि और अतिरिक्त दावों को प्राप्त करें:

1. **JWT स्ट्रिंग को पार्स करें**: `SignedJWT.parse()` विधि का उपयोग करें ताकि JWT स्ट्रिंग को एक `SignedJWT` वस्तु में परिवर्तित किया जा सके।
2. **दावों का सेट प्राप्त करें**: JWT से दावों (की-वैल्यू जोड़े) को `getJWTClaimsSet()` का उपयोग करके प्राप्त करें।
3. **विशिष्ट दावों को निकालें**:
   - `getExpirationTime()` को समाप्ति तिथि (`exp` दावा) के लिए उपयोग करें।
   - `getIssueTime()` को जारी तिथि (`iat` दावा) के लिए उपयोग करें।
   - अतिरिक्त दावों के लिए `getSubject()`, `getClaim()`, या अन्य विधियों का उपयोग करें।
4. **त्रुटियों का प्रबंधन करें**: पार्सिंग तर्क को एक try-catch ब्लॉक में लपेटें ताकि संभावित पार्सिंग समस्याओं का प्रबंधन किया जा सके।

---

## उदाहरण कोड

नीचे एक पूर्ण Java उदाहरण दिया गया है जो दिखाता है कि कैसे एक JWT से समाप्ति तिथि, जारी तिथि और एक अतिरिक्त दावा (जैसे कि विषय) को निकालें:

```java
import com.nimbusds.jwt.SignedJWT;
import com.nimbusds.jwt.JWTClaimsSet;
import java.text.ParseException;
import java.util.Date;

public class JwtExtractor {

    public static void main(String[] args) {
        // इसको अपने वास्तविक JWT स्ट्रिंग से बदलें
        String jwtString = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiaWF0IjoxNTE2MjM5MDIyLCJleHAiOjE1MTYyMzk5MjJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";

        try {
            // चरण 1: JWT स्ट्रिंग को पार्स करें
            SignedJWT signedJWT = SignedJWT.parse(jwtString);

            // चरण 2: दावों का सेट प्राप्त करें
            JWTClaimsSet claimsSet = signedJWT.getJWTClaimsSet();

            // चरण 3: समाप्ति और जारी तिथियों को निकालें
            Date expirationDate = claimsSet.getExpirationTime();
            Date issuedDate = claimsSet.getIssueTime();
            String subject = claimsSet.getSubject(); // एक और दावा का उदाहरण

            // चरण 4: परिणामों को प्रदर्शित करें
            if (expirationDate != null) {
                System.out.println("समाप्ति तिथि: " + expirationDate);
            } else {
                System.out.println("समाप्ति तिथि सेट नहीं है.");
            }

            if (issuedDate != null) {
                System.out.println("जारी तिथि: " + issuedDate);
            } else {
                System.out.println("जारी तिथि सेट नहीं है.");
            }

            if (subject != null) {
                System.out.println("विषय: " + subject);
            } else {
                System.out.println("विषय सेट नहीं है.");
            }

        } catch (ParseException e) {
            System.out.println("अवैध JWT: " + e.getMessage());
        }
    }
}
```

---

## कोड की व्याख्या

### 1. **आयात**
- `SignedJWT`: एक साइन्ड JWT को दर्शाता है और इसे पार्स और प्रोसेस करने के लिए विधियों को प्रदान करता है।
- `JWTClaimsSet`: JWT पेलोड से दावों को रखता है।
- `ParseException`: अगर JWT स्ट्रिंग गलत है या पार्स नहीं की जा सकती है, तो यह फेंक दिया जाता है।
- `Date`: समाप्ति और जारी समय को दर्शाने के लिए उपयोग किया जाता है।

### 2. **JWT को पार्स करना**
- `SignedJWT.parse(jwtString)` विधि एक JWT स्ट्रिंग (जैसे कि `header.payload.signature`) लेती है और एक `SignedJWT` वस्तु लौटाती है। अगर JWT अवैध है, तो यह एक `ParseException` फेंकता है।

### 3. **दावों तक पहुंचना**
- `signedJWT.getJWTClaimsSet()` दावों का सेट प्राप्त करता है, जो JWT पेलोड से सभी दावों को रखता है।

### 4. **विशिष्ट दावों को निकालना**
- **`getExpirationTime()`**: `exp` दावा को एक `Date` वस्तु के रूप में लौटाता है (या `null` अगर उपस्थित नहीं है)। यह दर्शाता है कि टोकन कब समाप्त हो जाएगा।
- **`getIssueTime()`**: `iat` दावा को एक `Date` वस्तु के रूप में लौटाता है (या `null` अगर उपस्थित नहीं है)। यह दर्शाता है कि टोकन कब जारी किया गया था।
- **`getSubject()`**: `sub` दावा को एक `String` के रूप में लौटाता है (या `null` अगर उपस्थित नहीं है), एक और मानक दावा का उदाहरण। आप भी `getClaim("key")` का उपयोग करके कस्टम दावों को एक `Object` के रूप में प्राप्त कर सकते हैं जिसे आप सही प्रकार में कास्ट कर सकते हैं (जैसे कि `String`, `Integer`)।

### 5. **त्रुटि प्रबंधन**
- try-catch ब्लॉक सुनिश्चित करता है कि अगर JWT गलत है या अवैध है, तो प्रोग्राम त्रुटि को नम्रता से संभालता है और एक त्रुटि संदेश को प्रिंट करता है।

---

## टिप्पणियाँ

- **साइन्ड vs. अनसाइन्ड JWTs**: यह उदाहरण साइन्ड टोकनों के लिए `SignedJWT` का उपयोग करता है। अगर आपके पास एक अनसाइन्ड JWT है, तो `PlainJWT.parse(jwtString)` का उपयोग करें। एक अधिक सामान्य दृष्टिकोण के लिए, आप `JWTParser.parse(jwtString)` का उपयोग कर सकते हैं और फिर प्रकार (`SignedJWT`, `PlainJWT`, आदि) का जांच कर सकते हैं `instanceof` का उपयोग करके।
- **हस्ताक्षर की पुष्टि**: यह कोड JWT की हस्ताक्षर की पुष्टि नहीं करता है। एक उत्पादन वातावरण में, आप `signedJWT.verify(verifier)` का उपयोग करके एक उपयुक्त कुंजी के साथ हस्ताक्षर की पुष्टि कर सकते हैं ताकि टोकन की सत्यापन की पुष्टि की जा सके।
- **नल चेक**: दावों को प्राप्त करने के समय हमेशा `null` की जांच करें, क्योंकि वे विकल्प हैं और प्रत्येक JWT में उपस्थित नहीं होंगे।
- **कस्टम दावों**: नॉन-स्टैंडर्ड दावों तक पहुंचने के लिए, `claimsSet.getClaim("claimName")` का उपयोग करें, जो एक `Object` लौटाता है जिसे आप सही प्रकार में कास्ट कर सकते हैं (जैसे कि `String`, `Integer`)।

---

## नमूना आउटपुट

उपरोक्त उदाहरण JWT स्ट्रिंग के लिए:
```
समाप्ति तिथि: Wed Jan 17 19:52:02 UTC 2018
जारी तिथि: Wed Jan 17 19:50:22 UTC 2018
विषय: 1234567890
```

---

यह दृष्टिकोण `com.nimbusds.jwt` लाइब्रेरी का उपयोग करके JWT से समाप्ति तिथि, जारी तिथि और अन्य दावों को निकालने का एक सरल और प्रभावी तरीका प्रदान करता है। `jwtString` को अपने टोकन से बदलें और कोड को अपने विशिष्ट आवश्यकताओं के अनुसार अनुकूलित करें!