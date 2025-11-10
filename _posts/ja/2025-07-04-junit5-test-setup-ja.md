---
audio: false
generated: true
lang: ja
layout: post
title: JUnit 5ファイルベーステスト設定
translated: true
type: note
---

以下は、入力ファイル（`1.in`）を使用してアルゴリズムソリューションをテストするための、**JUnit 5のみ**を使用した簡略化されたセットアップです（Mockitoなし）：

---

### 1. `pom.xml` の更新（JUnitのみ）
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

### 2. ディレクトリ構造
```
src/
├── main/
│   ├── java/com/algorithm/solutions/codeforces/CF123A.java  # ソリューション例
│   └── resources/codeforces/1.in                           # 入力ファイル
└── test/
    ├── java/com/algorithm/solutions/codeforces/CF123ATest.java  # テストクラス
    └── resources/codeforces/1.expected                         # 期待される出力（オプション）
```

---

### 3. テストクラスの例（`CF123ATest.java`）
```java
package com.algorithm.solutions.codeforces;

import org.junit.jupiter.api.Test;
import java.io.*;

import static org.junit.jupiter.api.Assertions.*;

class CF123ATest {

    @Test
    void testWithInputFile() throws IOException {
        // src/test/resources から stdin をリダイレクト
        InputStream originalIn = System.in;
        FileInputStream fileIn = new FileInputStream("src/test/resources/codeforces/1.in");
        System.setIn(fileIn);

        // stdout をリダイレクトして出力をキャプチャ
        PrintStream originalOut = System.out;
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));

        // ソリューションを実行
        CF123A.main(new String[0]);

        // ストリームを復元
        System.setIn(originalIn);
        System.setOut(originalOut);

        // 出力を検証（オプションで 1.expected と比較）
        String output = outContent.toString().trim();
        assertTrue(output.endsWith("42"));  // アサーション例
    }
}
```

---

### 4. 主な機能：
1. **入力リダイレクト**  
   - `src/test/resources` から `1.in` を `System.in` として読み取ります。
   - `ByteArrayOutputStream` を使用して `System.out` をキャプチャします。

2. **出力検証**  
   - 期待される出力に対してアサート（またはキーパターンをチェック）します。

3. **クリーンなリソース処理**  
   - テスト後に元の `System.in`/`System.out` を復元します。

---

### 5. テストの実行
```bash
mvn test
```
または IDE（IntelliJ/Eclipse/VSCode）経由で実行。

---

### 6. 代替案：パラメータ化テスト（複数入力）
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
`src/test/resources/codeforces/test_cases.csv` を作成：
```csv
input,expected
1 2 3,6
4 5 6,15
```

---

このセットアップにより、以下の**軽量なテスト環境**が得られます：
- Mockito 依存関係なし
- 入力/出力リダイレクト
- IDE/Maven 互換性
- ファイルベースのテストをサポート

特定の問題に適応させたい場合はお知らせください！