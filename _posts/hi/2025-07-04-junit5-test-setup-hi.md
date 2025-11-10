---
audio: false
generated: true
lang: hi
layout: post
title: जेयूनिट ५ फाइल-आधारित परीक्षण सेटअप
translated: true
type: note
---

यहां **केवल JUnit 5** (बिना Mockito के) का उपयोग करके आपके एल्गोरिदम समाधानों को इनपुट फ़ाइलों (`1.in`) के साथ परीक्षण करने के लिए एक सरल सेटअप दिया गया है:

---

### 1. `pom.xml` अपडेट करें (केवल JUnit)
```xml
<dependencies>
    <!-- JUnit 5 -->
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-api</artifactId>
        <version>5.9.2</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>org.junit.jupiter</groupId>
        <artifactId>junit-jupiter-engine</artifactId>
        <version>5.9.2</version>
        <scope>test</scope>
    </dependency>
</dependencies>

<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-surefire-plugin</artifactId>
            <version>3.0.0-M7</version>
        </plugin>
    </plugins>
</build>
```

---

### 2. डायरेक्टरी संरचना
```
src/
├── main/
│   ├── java/com/algorithm/solutions/codeforces/CF123A.java  # उदाहरण समाधान
│   └── resources/codeforces/1.in                           # इनपुट फ़ाइल
└── test/
    ├── java/com/algorithm/solutions/codeforces/CF123ATest.java  # टेस्ट क्लास
    └── resources/codeforces/1.expected                         # अपेक्षित आउटपुट (वैकल्पिक)
```

---

### 3. उदाहरण टेस्ट क्लास (`CF123ATest.java`)
```java
package com.algorithm.solutions.codeforces;

import org.junit.jupiter.api.Test;
import java.io.*;

import static org.junit.jupiter.api.Assertions.*;

class CF123ATest {

    @Test
    void testWithInputFile() throws IOException {
        // src/test/resources से stdin को रीडायरेक्ट करें
        InputStream originalIn = System.in;
        FileInputStream fileIn = new FileInputStream("src/test/resources/codeforces/1.in");
        System.setIn(fileIn);

        // आउटपुट कैप्चर करने के लिए stdout को रीडायरेक्ट करें
        PrintStream originalOut = System.out;
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));

        // समाधान चलाएँ
        CF123A.main(new String[0]);

        // स्ट्रीम्स को पुनर्स्थापित करें
        System.setIn(originalIn);
        System.setOut(originalOut);

        // आउटपुट सत्यापित करें (वैकल्पिक रूप से 1.expected से तुलना करें)
        String output = outContent.toString().trim();
        assertTrue(output.endsWith("42"));  // उदाहरण assertion
    }
}
```

---

### 4. मुख्य विशेषताएँ:
1. **इनपुट रीडायरेक्शन**  
   - `src/test/resources` से `1.in` को `System.in` के रूप में पढ़ता है।
   - `System.out` को कैप्चर करने के लिए `ByteArrayOutputStream` का उपयोग करता है।

2. **आउटपुट सत्यापन**  
   - अपेक्षित आउटपुट के विरुद्ध assert करें (या मुख्य पैटर्न की जाँच करें)।

3. **साफ़ संसाधन हैंडलिंग**  
   - टेस्ट के बाद मूल `System.in`/`System.out` को पुनर्स्थापित करता है।

---

### 5. टेस्ट चलाएँ
```bash
mvn test
```
या IDE (IntelliJ/Eclipse/VSCode) के माध्यम से।

---

### 6. विकल्प: पैरामीटराइज्ड टेस्ट (एकाधिक इनपुट)
```java
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvFileSource;

@ParameterizedTest
@CsvFileSource(resources = "/codeforces/test_cases.csv", numLinesToSkip = 1)
void testMultipleCases(String input, String expected) {
    System.setIn(new ByteArrayInputStream(input.getBytes()));
    ByteArrayOutputStream out = new ByteArrayOutputStream();
    System.setOut(new PrintStream(out));

    CF123A.main(new String[0]);

    assertEquals(expected, out.toString().trim());
}
```
`src/test/resources/codeforces/test_cases.csv` बनाएँ:
```csv
input,expected
1 2 3,6
4 5 6,15
```

---

यह आपको एक **हल्का-फुल्का टेस्टिंग सेटअप** देता है जिसमें शामिल है:
- कोई Mockito निर्भरताएँ नहीं
- इनपुट/आउटपुट रीडायरेक्शन
- IDE/Maven संगतता
- फ़ाइल-आधारित परीक्षण के लिए समर्थन

मुझे बताएं यदि आप इसे किसी विशेष समस्या के लिए अनुकूलित करना चाहते हैं!