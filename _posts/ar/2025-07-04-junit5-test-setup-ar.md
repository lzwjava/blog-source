---
audio: false
generated: true
lang: ar
layout: post
title: إعداد اختبارات جي يونيت 5 المعتمدة على الملفات
translated: true
type: note
---

إليك إعدادًا مبسطًا يستخدم **JUnit 5 فقط** (بدون Mockito) لاختبار حلول الخوارزميات الخاصة بك باستخدام ملفات الإدخال (`1.in`):

---

### 1. تحديث `pom.xml` (JUnit فقط)
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

### 2. هيكل المجلدات
```
src/
├── main/
│   ├── java/com/algorithm/solutions/codeforces/CF123A.java  # مثال على الحل
│   └── resources/codeforces/1.in                           # ملف الإدخال
└── test/
    ├── java/com/algorithm/solutions/codeforces/CF123ATest.java  # فئة الاختبار
    └── resources/codeforces/1.expected                         # المخرجات المتوقعة (اختياري)
```

---

### 3. مثال على فئة الاختبار (`CF123ATest.java`)
```java
package com.algorithm.solutions.codeforces;

import org.junit.jupiter.api.Test;
import java.io.*;

import static org.junit.jupiter.api.Assertions.*;

class CF123ATest {

    @Test
    void testWithInputFile() throws IOException {
        // إعادة توجيه stdin من src/test/resources
        InputStream originalIn = System.in;
        FileInputStream fileIn = new FileInputStream("src/test/resources/codeforces/1.in");
        System.setIn(fileIn);

        // إعادة توجيه stdout لالتقاط المخرجات
        PrintStream originalOut = System.out;
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));

        // تشغيل الحل
        CF123A.main(new String[0]);

        // استعادة streams
        System.setIn(originalIn);
        System.setOut(originalOut);

        // التحقق من المخرجات (مقارنتها بـ 1.expected اختياريًا)
        String output = outContent.toString().trim();
        assertTrue(output.endsWith("42"));  // مثال على التأكيد
    }
}
```

---

### 4. الميزات الرئيسية:
1. **إعادة توجيه الإدخال**  
   - يقرأ `1.in` من `src/test/resources` كـ `System.in`.
   - يستخدم `ByteArrayOutputStream` لالتقاط `System.out`.

2. **التحقق من المخرجات**  
   - التأكيد مقابل المخرجات المتوقعة (أو التحقق من الأنماط الرئيسية).

3. **معالجة نظيفة للموارد**  
   - يستعيد `System.in`/`System.out` الأصليين بعد الاختبار.

---

### 5. تشغيل الاختبارات
```bash
mvn test
```
أو عبر IDE (IntelliJ/Eclipse/VSCode).

---

### 6. بديل: اختبارات معاملية (مدخلات متعددة)
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
إنشاء `src/test/resources/codeforces/test_cases.csv`:
```csv
input,expected
1 2 3,6
4 5 6,15
```

---

يمنحك هذا **إعدادًا خفيفًا للاختبار** مع:
- لا توجد تبعيات Mockito
- إعادة توجيه الإدخال/المخرجات
- التوافق مع IDE/Maven
- دعم الاختبار القائم على الملفات

أعلمني إذا كنت ترغب في تكييف هذا لمشكلة محددة!