---
audio: false
generated: true
lang: hant
layout: post
title: JUnit 5 檔案測試設定
translated: true
type: note
---

以下是僅使用 **JUnit 5**（不含 Mockito）來測試演算法解題方案並讀取輸入檔案（`1.in`）的簡化設定：

---

### 1. 更新 `pom.xml`（僅 JUnit）
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

### 2. 目錄結構
```
src/
├── main/
│   ├── java/com/algorithm/solutions/codeforces/CF123A.java  # 範例解答
│   └── resources/codeforces/1.in                           # 輸入檔案
└── test/
    ├── java/com/algorithm/solutions/codeforces/CF123ATest.java  # 測試類別
    └── resources/codeforces/1.expected                         # 預期輸出（可選）
```

---

### 3. 範例測試類別 (`CF123ATest.java`)
```java
package com.algorithm.solutions.codeforces;

import org.junit.jupiter.api.Test;
import java.io.*;

import static org.junit.jupiter.api.Assertions.*;

class CF123ATest {

    @Test
    void testWithInputFile() throws IOException {
        // 從 src/test/resources 重新導向 stdin
        InputStream originalIn = System.in;
        FileInputStream fileIn = new FileInputStream("src/test/resources/codeforces/1.in");
        System.setIn(fileIn);

        // 重新導向 stdout 以擷取輸出
        PrintStream originalOut = System.out;
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));

        // 執行解題方案
        CF123A.main(new String[0]);

        // 還原串流
        System.setIn(originalIn);
        System.setOut(originalOut);

        // 驗證輸出（可選擇與 1.expected 比對）
        String output = outContent.toString().trim();
        assertTrue(output.endsWith("42"));  // 範例斷言
    }
}
```

---

### 4. 主要特色：
1. **輸入重新導向**  
   - 從 `src/test/resources` 讀取 `1.in` 作為 `System.in`。
   - 使用 `ByteArrayOutputStream` 擷取 `System.out`。

2. **輸出驗證**  
   - 根據預期輸出進行斷言（或檢查關鍵模式）。

3. **整潔的資源處理**  
   - 測試完成後還原原始的 `System.in`/`System.out`。

---

### 5. 執行測試
```bash
mvn test
```
或透過 IDE（IntelliJ/Eclipse/VSCode）執行。

---

### 6. 替代方案：參數化測試（多組輸入）
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
建立 `src/test/resources/codeforces/test_cases.csv`：
```csv
input,expected
1 2 3,6
4 5 6,15
```

---

此設定提供一個**輕量級測試環境**，具備：
- 無需 Mockito 依賴
- 輸入/輸出重新導向
- 相容 IDE/Maven
- 支援基於檔案的測試

如需針對特定題目調整此設定，請隨時告知！