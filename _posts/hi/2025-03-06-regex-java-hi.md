---
audio: false
generated: true
lang: hi
layout: post
title: सामान्य अभिव्यक्तियाँ जावा में
translated: true
---

# `java.util.regex` का Java में उपयोग कैसे करें

Java में `java.util.regex` पैकेज नियमित अभिव्यक्तियाँ (regex) के साथ काम करने के लिए उपकरण प्रदान करता है, जो पाठ को मिलान और संशोधित करने के लिए उपयोग किए जाने वाले पैटर्न हैं। इस गाइड में आपको इस पैकेज का उपयोग करने के लिए आधारभूत बातें बताएंगे, जिसमें दो मुख्य क्लासों: `Pattern` और `Matcher` पर ध्यान केंद्रित किया जाएगा। मैं आम उपयोग के मामलों के साथ उदाहरण भी कवर करूँगा ताकि आप शुरू करने में मदद मिल सके।

## `java.util.regex` का परिचय

`java.util.regex` पैकेज में शामिल हैं:

- **`Pattern`**: एक संकलित नियमित अभिव्यक्ति को दर्शाता है। इसे एक regex string से बनाया जाता है।
- **`Matcher`**: पैटर्न को एक विशेष इनपुट string पर लागू करता है और मिलान ऑपरेशन करता है।

अतिरिक्त रूप से, Java के `String` क्लास regex आधारित विधियाँ अधिक सरल कार्य के लिए प्रदान करता है।

## `java.util.regex` का उपयोग करने के लिए आधारभूत कदम

Java में नियमित अभिव्यक्तियों का उपयोग करने के लिए, इन कदमों का पालन करें:

1. **एक पैटर्न को संकलित करें**: अपने regex string को एक `Pattern` object में बदलें।
2. **एक Matcher बनाएं**: पैटर्न का उपयोग करके अपने इनपुट टेक्स्ट के लिए एक `Matcher` बनाएं।
3. **ऑपरेशन करें**: मिलान की जांच करें, पैटर्न ढूंढें, या पाठ को संशोधित करें।

यह प्रैक्टिस में कैसे काम करता है।

## उदाहरण 1: ईमेल पते की सत्यापना

एक बुनियादी regex पैटर्न: `".+@.+\\..+"` का उपयोग करके एक सरल ईमेल सत्यापन बनाएं। यह पैटर्न `@` प्रतीक के पहले और बाद में कम से कम एक अक्षर वाले strings को मिलाता है, फिर एक बिंदु और अधिक अक्षरों (जैसे, `example@test.com`) के साथ।

```java
import java.util.regex.*;

public class EmailValidator {
    public static boolean isValidEmail(String email) {
        // regex पैटर्न को परिभाषित करें
        String regex = ".+@.+\\..+";
        // पैटर्न को संकलित करें
        Pattern pattern = Pattern.compile(regex);
        // इनपुट string के लिए एक matcher बनाएं
        Matcher matcher = pattern.matcher(email);
        // पूरी string पैटर्न से मिलती है तो `true` वर्ना `false` return करें
        return matcher.matches();
    }

    public static void main(String[] args) {
        String email = "example@test.com";
        if (isValidEmail(email)) {
            System.out.println("सत्यापित ईमेल");
        } else {
            System.out.println("असत्यापित ईमेल");
        }
    }
}
```

### व्याख्या
- **`Pattern.compile(regex)`**: regex string को एक `Pattern` object में संकलित करता है।
- **`pattern.matcher(email)`**: इनपुट string `email` के लिए एक `Matcher` बनाता है।
- **`matcher.matches()`**: पूरी string पैटर्न से मिलती है तो `true` वर्ना `false` return करता है।

**आउटपुट**: `सत्यापित ईमेल`

नोट: यह एक सरल ईमेल पैटर्न है। वास्तविक ईमेल सत्यापन के लिए एक अधिक जटिल regex (जैसे RFC 5322) की आवश्यकता होती है, लेकिन यह एक शुरुआत के रूप में काम करता है।

## उदाहरण 2: एक string में सभी हैशटैग ढूंढना

अगर आप एक ट्वीट से सभी हैशटैग (जैसे, `#java`) को निकालना चाहते हैं, तो regex `"#\\w+"` का उपयोग करें, जहां `#` हैशटैग प्रतीक को मिलाता है और `\\w+` एक या अधिक शब्द अक्षरों (अक्षर, अंकों या अंडरस्कोर) को मिलाता है।

```java
import java.util.regex.*;

public class HashtagExtractor {
    public static void main(String[] args) {
        String tweet = "यह एक #नमूना ट्वीट है #अनेक हैशटैग जैसे #java के साथ";
        String regex = "#\\w+";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(tweet);

        // सभी मिलान ढूंढें
        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}
```

### व्याख्या
- **`matcher.find()`**: इनपुट string में अगले मिलान पर जाता है और अगर एक मिलान मिलता है तो `true` return करता है।
- **`matcher.group()`**: वर्तमान मिलान के लिए मिले हुए पाठ को return करता है।

**आउटपुट**:
```
#नमूना
#अनेक
#java
```

## उदाहरण 3: regex के साथ पाठ बदलना

एक शब्द (जैसे, "badword" को अस्तरिक्स के साथ सेंसर करना) के सभी अवतरण बदलने के लिए, आप `String.replaceAll()` विधि का उपयोग कर सकते हैं, जो अंदरूनी रूप से regex का उपयोग करता है।

```java
public class TextCensor {
    public static void main(String[] args) {
        String text = "यह एक badword उदाहरण है badword दोहराया गया है।";
        String censored = text.replaceAll("badword", "*******");
        System.out.println(censored);
    }
}
```

**आउटपुट**: `यह एक ******* उदाहरण है ******* दोहराया गया है।`

जटिल बदलावों के लिए, `Matcher` का उपयोग करें:

```java
import java.util.regex.*;

public class ComplexReplacement {
    public static void main(String[] args) {
        String text = "संपर्क: 123-456-7890";
        String regex = "\\d{3}-\\d{3}-\\d{4}"; // फोन नंबर मिलाता है
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);
        String result = matcher.replaceAll("XXX-XXX-XXXX");
        System.out.println(result);
    }
}
```

**आउटपुट**: `संपर्क: XXX-XXX-XXXX`

## उदाहरण 4: संरचित डेटा को पार्स करने के लिए समूहों का उपयोग

regex समूह, जो कोष्ठकों `()` के साथ परिभाषित किए जाते हैं, आपको एक मिलान के हिस्सों को कैप्चर करने की अनुमति देते हैं। उदाहरण के लिए, एक सामाजिक सुरक्षा संख्या (SSN) जैसे `123-45-6789` को पार्स करने के लिए:

```java
import java.util.regex.*;

public class SSNParser {
    public static void main(String[] args) {
        String ssn = "123-45-6789";
        String regex = "(\\d{3})-(\\d{2})-(\\d{4})"; // क्षेत्र, समूह, सीरियल के लिए समूह
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(ssn);

        if (matcher.matches()) {
            System.out.println("क्षेत्र संख्या: " + matcher.group(1));
            System.out.println("समूह संख्या: " + matcher.group(2));
            System.out.println("सीरियल संख्या: " + matcher.group(3));
        }
    }
}
```

### व्याख्या
- **`"(\\d{3})-(\\d{2})-(\\d{4})"`**: तीन समूह परिभाषित करता है:
  - समूह 1: `\\d{3}` (तीन अंकों)
  - समूह 2: `\\d{2}` (दो अंकों)
  - समूह 3: `\\d{4}` (चार अंकों)
- **`matcher.group(n)`**: समूह `n` (1-आधारित सूचकांक) द्वारा मिले हुए पाठ को प्राप्त करता है।

**आउटपुट**:
```
क्षेत्र संख्या: 123
समूह संख्या: 45
सीरियल संख्या: 6789
```

आप **नामित समूहों** का उपयोग भी **स्पष्टता** के लिए कर सकते हैं:

```java
String regex = "(?<area>\\d{3})-(?<group>\\d{2})-(?<serial>\\d{4})";
Pattern pattern = Pattern.compile(regex);
Matcher matcher = pattern.matcher("123-45-6789");
if (matcher.matches()) {
    System.out.println("क्षेत्र: " + matcher.group("area"));
    System.out.println("समूह: " + matcher.group("group"));
    System.out.println("सीरियल: " + matcher.group("serial"));
}
```

## अतिरिक्त विशेषताएं और टिप्स

### झंडे
`Pattern.compile()` में झंडों का उपयोग करके पैटर्न व्यवहार को संशोधित करें:
- **`Pattern.CASE_INSENSITIVE`**: मिलान करते समय case को नजरअंदाज करें।
  ```java
  Pattern pattern = Pattern.compile("hello", Pattern.CASE_INSENSITIVE);
  Matcher matcher = pattern.matcher("HELLO");
  System.out.println(matcher.matches()); // true
  ```

### String विधियाँ
सरल कार्य के लिए `String` विधियों का उपयोग करें:
- **`matches()`**: पूरी string एक regex से मिलती है तो `true` return करता है।
  ```java
  String text = "cat";
  System.out.println(text.matches("\\w{3}")); // true
  ```
- **`split()`**: एक string को एक regex पैटर्न द्वारा विभाजित करता है।
  ```java
  String data = "apple, banana, cherry";
  String[] fruits = data.split("\\s*,\\s*");
  // आउटपुट: apple, banana, cherry
  ```

### विशेष अक्षरों को बचाना
Regex विशेष अक्षरों जैसे `.`, `*`, और `?` का उपयोग करता है। उन्हें वास्तविक रूप से मिलाने के लिए `\\` से बचाएं:
- बिंदु मिलाएं: `"\\."`
- Java strings में, बैकस्लैश बचाएं: `"\\d"` अंकों के लिए, `"\\\\"` एक वास्तविक बैकस्लैश के लिए।

### प्रदर्शन
एक पैटर्न को संकलित करना महंगा है। जब संभव हो, `Pattern` objects को पुन: उपयोग करें:
```java
Pattern pattern = Pattern.compile("\\d+"); // एक बार संकलित करें
for (String input : new String[]{"123", "456"}) {
    Matcher matcher = pattern.matcher(input);
    if (matcher.matches()) {
        System.out.println("संख्या: " + input);
    }
}
```

### त्रुटि निपटान
अवैध regex पैटर्न `PatternSyntaxException` फेंकते हैं। उत्पादन कोड में इसे संभालें:
```java
try {
    Pattern pattern = Pattern.compile("["); // अवैध regex
} catch (PatternSyntaxException e) {
    System.err.println("अवैध regex: " + e.getMessage());
}
```

## सारांश

- **एक पैटर्न को संकलित करें**: `Pattern.compile(regex)`
- **एक Matcher बनाएं**: `pattern.matcher(input)`
- **मुख्य ऑपरेशन**:
  - `matches()`: पूरी string मिलान
  - `find()`: अगला मिलान ढूंढें
  - `group()`: मिले हुए पाठ को निकालें
  - `replaceAll()`: मिलान बदलें
- **सुविधा**: सरल कार्य के लिए `String` विधियों का उपयोग करें।
- **बेस्ट प्रैक्टिस**: विशेष अक्षरों को बचाएं, पैटर्न को पुन: उपयोग करें, और अपवादों का निपटान करें।

यह `java.util.regex` के मूल तत्वों को कवर करता है। उन्नत विषयों जैसे lookaheads या character classes के लिए, [Java documentation](https://docs.oracle.com/en/java/javase/17/docs/api/java.util.regex/package-summary.html) पर जांच करें या विशिष्ट उपयोग के मामलों के साथ प्रयोग करें!