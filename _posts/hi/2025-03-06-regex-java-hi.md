---
audio: false
generated: true
lang: hi
layout: post
title: जावा में रेगुलर एक्सप्रेशन्स
translated: true
type: note
---

# Java में `java.util.regex` का उपयोग कैसे करें

Java में `java.util.regex` पैकेज रेगुलर एक्सप्रेशन (regex) के साथ काम करने के लिए टूल्स प्रदान करता है, जो टेक्स्ट को मैच करने और मैनिपुलेट करने के लिए उपयोग किए जाने वाले पैटर्न होते हैं। यह गाइड आपको इस पैकेज के उपयोग की मूल बातें समझाएगी, जो दो मुख्य क्लासेस पर केंद्रित है: `Pattern` और `Matcher`। मैं आपको शुरुआत करने में मदद करने के लिए उदाहरणों के साथ सामान्य उपयोग के मामलों को भी कवर करूंगा।

## `java.util.regex` का अवलोकन

`java.util.regex` पैकेज में शामिल हैं:

- **`Pattern`**: एक कंपाइल्ड रेगुलर एक्सप्रेशन को रिप्रेजेंट करता है। आप इसे एक regex स्ट्रिंग से बनाते हैं।
- **`Matcher`**: पैटर्न को एक विशिष्ट इनपुट स्ट्रिंग पर लागू करता है और मैचिंग ऑपरेशन करता है।

इसके अतिरिक्त, Java की `String` क्लास सरल कार्यों के लिए regex-आधारित मेथड्स प्रदान करती है।

## `java.util.regex` का उपयोग करने के मूल चरण

Java में रेगुलर एक्सप्रेशन का उपयोग करने के लिए, इन चरणों का पालन करें:

1.  **एक Pattern कंपाइल करें**: अपनी regex स्ट्रिंग को एक `Pattern` ऑब्जेक्ट में बदलें।
2.  **एक Matcher बनाएं**: अपने इनपुट टेक्स्ट के लिए एक `Matcher` बनाने के लिए पैटर्न का उपयोग करें।
3.  **ऑपरेशन करें**: मैच की जांच करने, पैटर्न ढूंढने या टेक्स्ट को मैनिपुलेट करने के लिए matcher का उपयोग करें।

यहां बताया गया है कि यह व्यवहार में कैसे काम करता है।

## उदाहरण 1: एक ईमेल एड्रेस को वैलिडेट करना

आइए एक बेसिक regex पैटर्न: `".+@.+\\..+"` का उपयोग करके एक सरल ईमेल वैलिडेटर बनाएं। यह पैटर्न ऐसी स्ट्रिंग्स से मेल खाता है जिनमें `@` सिंबल से पहले और बाद में कम से कम एक कैरेक्टर होता है, उसके बाद एक डॉट और अधिक कैरेक्टर होते हैं (जैसे, `example@test.com`)।

```java
import java.util.regex.*;

public class EmailValidator {
    public static boolean isValidEmail(String email) {
        // regex पैटर्न को डिफाइन करें
        String regex = ".+@.+\\..+";
        // पैटर्न को कंपाइल करें
        Pattern pattern = Pattern.compile(regex);
        // इनपुट स्ट्रिंग के लिए एक matcher बनाएं
        Matcher matcher = pattern.matcher(email);
        // चेक करें कि क्या पूरी स्ट्रिंग पैटर्न से मेल खाती है
        return matcher.matches();
    }

    public static void main(String[] args) {
        String email = "example@test.com";
        if (isValidEmail(email)) {
            System.out.println("Valid email");
        } else {
            System.out.println("Invalid email");
        }
    }
}
```

### व्याख्या
- **`Pattern.compile(regex)`**: regex स्ट्रिंग को एक `Pattern` ऑब्जेक्ट में कंपाइल करता है।
- **`pattern.matcher(email)`**: इनपुट स्ट्रिंग `email` के लिए एक `Matcher` बनाता है।
- **`matcher.matches()`**: `true` रिटर्न करता है यदि पूरी स्ट्रिंग पैटर्न से मेल खाती है, अन्यथा `false`।

**आउटपुट**: `Valid email`

नोट: यह एक सरलीकृत ईमेल पैटर्न है। रियल ईमेल वैलिडेशन के लिए एक अधिक जटिल regex (जैसे, RFC 5322 के अनुसार) की आवश्यकता होती है, लेकिन यह एक शुरुआती बिंदु के रूप में कार्य करता है।

## उदाहरण 2: एक स्ट्रिंग में सभी हैशटैग ढूंढना

मान लीजिए आप एक ट्वीट से सभी हैशटैग (जैसे, `#java`) निकालना चाहते हैं। regex `"#\\w+"` का उपयोग करें, जहां `#` लिटरल हैशटैग सिंबल से मेल खाता है और `\\w+` एक या अधिक वर्ड कैरेक्टर (अक्षर, अंक, या अंडरस्कोर) से मेल खाता है।

```java
import java.util.regex.*;

public class HashtagExtractor {
    public static void main(String[] args) {
        String tweet = "This is a #sample tweet with #multiple hashtags like #java";
        String regex = "#\\w+";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(tweet);

        // सभी मैच ढूंढें
        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}
```

### व्याख्या
- **`matcher.find()`**: इनपुट स्ट्रिंग में अगले मैच पर जाता है और `true` रिटर्न करता है यदि कोई मैच मिलता है।
- **`matcher.group()`**: वर्तमान मैच के लिए मैच किए गए टेक्स्ट को रिटर्न करता है।

**आउटपुट**:
```
#sample
#multiple
#java
```

## उदाहरण 3: Regex के साथ टेक्स्ट को रिप्लेस करना

किसी शब्द के सभी घटनाओं को रिप्लेस करने के लिए (जैसे, "badword" को एस्टेरिस्क से सेंसर करना), आप `String.replaceAll()` मेथड का उपयोग कर सकते हैं, जो आंतरिक रूप से regex का उपयोग करती है।

```java
public class TextCensor {
    public static void main(String[] args) {
        String text = "This is a badword example with badword repeated.";
        String censored = text.replaceAll("badword", "*******");
        System.out.println(censored);
    }
}
```

**आउटपुट**: `This is a ******* example with ******* repeated.`

अधिक जटिल रिप्लेसमेंट के लिए, `Matcher` का उपयोग करें:

```java
import java.util.regex.*;

public class ComplexReplacement {
    public static void main(String[] args) {
        String text = "Contact: 123-456-7890";
        String regex = "\\d{3}-\\d{3}-\\d{4}"; // फोन नंबर से मैच करता है
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);
        String result = matcher.replaceAll("XXX-XXX-XXXX");
        System.out.println(result);
    }
}
```

**आउटपुट**: `Contact: XXX-XXX-XXXX`

## उदाहरण 4: स्ट्रक्चर्ड डेटा को पार्स करने के लिए ग्रुप्स का उपयोग करना

Regex ग्रुप्स, जो कोष्ठक `()` के साथ डिफाइन किए जाते हैं, आपको मैच के भागों को कैप्चर करने की अनुमति देते हैं। उदाहरण के लिए, एक सोशल सिक्योरिटी नंबर (SSN) जैसे `123-45-6789` को पार्स करने के लिए:

```java
import java.util.regex.*;

public class SSNParser {
    public static void main(String[] args) {
        String ssn = "123-45-6789";
        String regex = "(\\d{3})-(\\d{2})-(\\d{4})"; // एरिया, ग्रुप, सीरियल के लिए ग्रुप
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(ssn);

        if (matcher.matches()) {
            System.out.println("Area number: " + matcher.group(1));
            System.out.println("Group number: " + matcher.group(2));
            System.out.println("Serial number: " + matcher.group(3));
        }
    }
}
```

### व्याख्या
- **`"(\\d{3})-(\\d{2})-(\\d{4})"`**: तीन ग्रुप्स को डिफाइन करता है:
  - ग्रुप 1: `\\d{3}` (तीन अंक)
  - ग्रुप 2: `\\d{2}` (दो अंक)
  - ग्रुप 3: `\\d{4}` (चार अंक)
- **`matcher.group(n)`**: ग्रुप `n` (1-आधारित इंडेक्स) द्वारा मैच किए गए टेक्स्ट को प्राप्त करता है।

**आउटपुट**:
```
Area number: 123
Group number: 45
Serial number: 6789
```

आप स्पष्टता के लिए **नामित ग्रुप्स** का भी उपयोग कर सकते हैं:

```java
String regex = "(?<area>\\d{3})-(?<group>\\d{2})-(?<serial>\\d{4})";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher("123-45-6789");
if (matcher.matches()) {
    System.out.println("Area: " + matcher.group("area"));
    System.out.println("Group: " + matcher.group("group"));
    System.out.println("Serial: " + matcher.group("serial"));
}
```

## अतिरिक्त फीचर्स और टिप्स

### फ्लैग्स
`Pattern.compile()` में फ्लैग्स के साथ पैटर्न व्यवहार को संशोधित करें:
- **`Pattern.CASE_INSENSITIVE`**: मैच करते समय केस को अनदेखा करता है।
  ```java
  Pattern pattern = Pattern.compile("hello", Pattern.CASE_INSENSITIVE);
  Matcher matcher = pattern.matcher("HELLO");
  System.out.println(matcher.matches()); // true
  ```

### स्ट्रिंग मेथड्स
सरल कार्यों के लिए, `String` मेथड्स का उपयोग करें:
- **`matches()`**: चेक करता है कि क्या पूरी स्ट्रिंग एक regex से मेल खाती है।
  ```java
  String text = "cat";
  System.out.println(text.matches("\\w{3}")); // true
  ```
- **`split()`**: एक स्ट्रिंग को regex पैटर्न द्वारा विभाजित करता है।
  ```java
  String data = "apple, banana, cherry";
  String[] fruits = data.split("\\s*,\\s*");
  // आउटपुट: apple, banana, cherry
  ```

### विशेष कैरेक्टर को एस्केप करना
Regex विशेष कैरेक्टर जैसे `.`, `*`, और `?` का उपयोग करता है। उन्हें शाब्दिक रूप से मैच करने के लिए, `\\` के साथ एस्केप करें:
- एक पीरियड से मैच करें: `"\\."`
- Java स्ट्रिंग्स में, बैकस्लैश को एस्केप करें: अंकों के लिए `"\\d"`, एक शाब्दिक बैकस्लैश के लिए `"\\\\"`।

### परफॉर्मेंस
एक पैटर्न को कंपाइल करना महंगा है। जब भी संभव हो `Pattern` ऑब्जेक्ट्स का पुन: उपयोग करें:
```java
Pattern pattern = Pattern.compile("\\d+"); // एक बार कंपाइल करें
for (String input : new String[]{"123", "456"}) {
    Matcher matcher = pattern.matcher(input);
    if (matcher.matches()) {
        System.out.println("Number: " + input);
    }
}
```

### एरर हैंडलिंग
अमान्य regex पैटर्न `PatternSyntaxException` थ्रो करते हैं। प्रोडक्शन कोड में इसे हैंडल करें:
```java
try {
    Pattern pattern = Pattern.compile("["); // अमान्य regex
} catch (PatternSyntaxException e) {
    System.err.println("Invalid regex: " + e.getMessage());
}
```

## सारांश

- **एक Pattern कंपाइल करें**: `Pattern.compile(regex)`
- **एक Matcher बनाएं**: `pattern.matcher(input)`
- **मुख्य ऑपरेशन**:
  - `matches()`: पूरी स्ट्रिंग मैच
  - `find()`: अगला मैच ढूंढें
  - `group()`: मैच किए गए टेक्स्ट को निकालें
  - `replaceAll()`: मैच को रिप्लेस करें
- **सुविधा**: सरल कार्यों के लिए `String` मेथड्स का उपयोग करें।
- **बेस्ट प्रैक्टिसेज**: विशेष कैरेक्टर को एस्केप करें, पैटर्न्स का पुन: उपयोग करें, और एक्सेप्शन को हैंडल करें।

यह `java.util.regex` के मूल सिद्धांतों को कवर करता है। लुकअहेड्स या कैरेक्टर क्लासेज जैसे उन्नत विषयों के लिए, [Java डॉक्यूमेंटेशन](https://docs.oracle.com/en/java/javase/17/docs/api/java.util.regex/package-summary.html) से परामर्श लें या विशिष्ट उपयोग के मामलों के साथ प्रयोग करें!