---
audio: false
generated: true
lang: hant
layout: post
title: 弗吉尼亞大學題目的Maven結構
translated: true
type: note
---

感謝您分享 `uva/106` 子目錄的具體結構。看來您的專案採用了更細粒度的結構，每個 UVA 題目（例如 `106`）都是一個獨立的目錄，擁有自己的 `src` 資料夾，其中包含 `Main.java` 檔案以及可能的輸入檔案（如 `1.in`）。這表明每個題目可能被視為獨立的子專案或模組。為了在 Maven 多模組設定中容納這種結構，我們可以選擇：
1. 將每個題目目錄（例如 `uva/106`）視為獨立的 Maven 子模組。
2. 將 `uva` 保留為單一模組，並在其 `src/main/java` 目錄內組織題目檔案。

考慮到 UVA 題目的數量（根據您之前提供的清單：`100`、`10000` 等），為每個題目創建獨立的 Maven 模組可能會導致模組數量過多，管理起來可能較為繁瑣。因此，我建議採用一種結構，將 `uva` 設為單一模組，並將每個題目的 `Main.java` 組織在 `uva/src/main/java` 下，採用套件結構（例如，題目 106 的套件為 `com.algorithm.solutions.uva.p106`）。這樣可以在保持 Maven 優勢的同時，使專案易於管理。

不過，如果您偏好更細粒度的結構，我也會提供另一種方法，將每個題目設為獨立的子模組。下面，我將根據您的結構更新 `pom.xml` 檔案，並提供重組檔案的步驟。

---

### 選項 1：單一 `uva` 模組，使用題目套件

#### 更新後的目錄結構
```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── com/algorithm/solutions/nowcoder/
│                   ├── Main.java
│                   ├── nc140.java
│                   ├── nc45.java
│                   ├── nc78.java
│                   └── nc93.java
├── uva/
│   ├── pom.xml
│   ├── src/
│   │   └── main/
│   │       └── java/
│   │           └── com/algorithm/solutions/uva/
│   │               ├── p100/
│   │               │   └── Main.java
│   │               ├── p106/
│   │               │   └── Main.java
│   │               ├── p10000/
│   │               │   └── Main.java
│   │               └── (其他題目)
│   └── resources/
│       └── uva/
│           ├── p100/
│           │   └── 1.in
│           ├── p106/
│           │   └── 1.in
│           └── (其他題目)
└── README.md
```

#### 父層 `pom.xml`（根目錄：`algorithm-solutions/pom.xml`）
此檔案與之前大致相同，將 `nowcoder` 和 `uva` 定義為模組。

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.algorithm.solutions</groupId>
    <artifactId>algorithm-solutions</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <name>Algorithm Solutions Parent</name>
    <description>Parent project for algorithm solutions</description>

    <modules>
        <module>nowcoder</module>
        <module>uva</module>
    </modules>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.13.0</version>
                <configuration>
                    <source>${maven.compiler.source}</source>
                    <target>${maven.compiler.target}</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### Nowcoder 子模組 `pom.xml`（`nowcoder/pom.xml`）
此檔案與之前的回覆相同，假設 `nowcoder` 檔案已移至 `src/main/java/com/algorithm/solutions/nowcoder/`。

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.algorithm.solutions</groupId>
        <artifactId>algorithm-solutions</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>nowcoder</artifactId>
    <name>Nowcoder Solutions</name>
    <description>Solutions for Nowcoder algorithm problems</description>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.4.2</version>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>com.algorithm.solutions.nowcoder.Main</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### UVA 子模組 `pom.xml`（`uva/pom.xml`）
此模組包含一個 `resources` 目錄，用於存放輸入檔案如 `1.in`。每個題目的 `Main.java` 檔案以套件形式組織。

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.algorithm.solutions</groupId>
        <artifactId>algorithm-solutions</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>uva</artifactId>
    <name>UVA Solutions</name>
    <description>Solutions for UVA algorithm problems</description>

    <build>
        <resources>
            <resource>
                <directory>src/main/resources</directory>
                <includes>
                    <include>**/*.in</include>
                </includes>
            </resource>
        </resources>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.4.2</version>
            </plugin>
        </plugins>
    </build>
</project>
```

#### 檔案組織
- **移動 Java 檔案**：
  - 對於每個題目（例如 `uva/106/src/Main.java`），將 `Main.java` 移至 `uva/src/main/java/com/algorithm/solutions/uva/p106/Main.java`。
  - 更新 `Main.java` 檔案，加入套件宣告：
    ```java
    package com.algorithm.solutions.uva.p106;
    public class Main {
        // ... 現有代碼 ...
    }
    ```
  - 對所有題目（例如 `p100`、`p10000` 等）執行此操作。

- **移動輸入檔案**：
  - 將輸入檔案如 `uva/106/1.in` 移至 `uva/src/main/resources/uva/p106/1.in`。
  - 這允許 Maven 將這些檔案包含在 JAR 中，並可透過 `ClassLoader.getResource()` 或類似方法在 Java 代碼中存取。

#### 執行程式
要執行特定的 UVA 題目（例如題目 106）：
```bash
mvn -pl uva exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
```

---

### 選項 2：每個 UVA 題目作為獨立子模組
如果您希望每個 UVA 題目（例如 `106`、`100`）都是獨立的 Maven 模組，以下是設定方式。這種方式更細粒度，但會增加 `pom.xml` 檔案的數量。

#### 更新後的目錄結構
```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── com/algorithm/solutions/nowcoder/
│                   ├── Main.java
│                   ├── nc140.java
│                   ├── nc45.java
│                   ├── nc78.java
│                   └── nc93.java
├── uva/
│   ├── 106/
│   │   ├── pom.xml
│   │   ├── src/
│   │   │   └── main/
│   │   │       └── java/
│   │   │           └── com/algorithm/solutions/uva/p106/
│   │   │               └── Main.java
│   │   └── resources/
│   │       └── 1.in
│   ├── 100/
│   │   ├── pom.xml
│   │   ├── src/
│   │   │   └── main/
│   │   │       └── java/
│   │   │           └── com/algorithm/solutions/uva/p100/
│   │   │               └── Main.java
│   │   └── resources/
│   │       └── (輸入檔案，如有)
│   └── (其他題目目錄)
└── README.md
```

#### 父層 `pom.xml`（根目錄：`algorithm-solutions/pom.xml`）
將每個題目添加為模組。

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.algorithm.solutions</groupId>
    <artifactId>algorithm-solutions</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>pom</packaging>

    <name>Algorithm Solutions Parent</name>
    <description>Parent project for algorithm solutions</description>

    <modules>
        <module>nowcoder</module>
        <module>uva/106</module>
        <module>uva/100</module>
        <module>uva/10000</module>
        <module>uva/10006</module>
        <module>uva/10008</module>
        <module>uva/10009</module>
        <module>uva/10012</module>
        <module>uva/10013</module>
        <module>uva/10018</module>
        <module>uva/10019</module>
        <module>uva/10026</module>
        <module>uva/10033</module>
        <module>uva/10034</module>
    </modules>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.13.0</version>
                <configuration>
                    <source>${maven.compiler.source}</source>
                    <target>${maven.compiler.target}</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

#### Nowcoder 子模組 `pom.xml`（`nowcoder/pom.xml`）
與上述相同（未變更）。

#### UVA 題目 106 子模組 `pom.xml`（`uva/106/pom.xml`）
每個題目都有自己的 `pom.xml`。以下是 `uva/106` 的範例：

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>com.algorithm.solutions</groupId>
        <artifactId>algorithm-solutions</artifactId>
        <version>1.0-SNAPSHOT</version>
    </parent>

    <artifactId>uva-106</artifactId>
    <name>UVA Problem 106</name>
    <description>Solution for UVA problem 106</description>

    <build>
        <resources>
            <resource>
                <directory>resources</directory>
                <includes>
                    <include>**/*.in</include>
                </includes>
            </resource>
        </resources>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.4.2</version>
                <configuration>
                    <archive>
                        <manifest>
                            <mainClass>com.algorithm.solutions.uva.p106.Main</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

- **為其他題目重複此操作**：為 `uva/100`、`uva/10000` 等創建類似的 `pom.xml` 檔案，調整 `artifactId`（例如 `uva-100`）、`name` 和 `mainClass`（例如 `com.algorithm.solutions.uva.p100.Main`）。

#### 檔案組織
- **移動 Java 檔案**：
  - 對於 `uva/106/src/Main.java`，移至 `uva/106/src/main/java/com/algorithm/solutions/uva/p106/Main.java`。
  - 加入套件宣告：
    ```java
    package com.algorithm.solutions.uva.p106;
    public class Main {
        // ... 現有代碼 ...
    }
    ```
- **移動輸入檔案**：
  - 將 `uva/106/1.in` 移至 `uva/106/resources/1.in`。

#### 執行程式
要執行題目 106：
```bash
mvn -pl uva/106 exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
```

---

### 建議
- **選項 1（單一 `uva` 模組）** 更簡單且更具擴展性，特別是當您有許多 UVA 題目時。它避免了創建大量 `pom.xml` 檔案，並保持專案結構整潔。使用套件來邏輯組織題目。
- **選項 2（每個題目獨立模組）** 更適合希望每個題目完全獨立的情況（例如用於獨立部署或測試）。但由於模組數量眾多，需要更多維護工作。

### 實施選項 1 的步驟
1. **創建目錄結構**：
   - 在 `algorithm-solutions` 根目錄執行以下命令：
     ```bash
     mkdir -p uva/src/main/java/com/algorithm/solutions/uva
     mkdir -p uva/src/main/resources/uva
     mkdir -p nowcoder/src/main/java/com/algorithm/solutions/nowcoder
     ```
2. **移動檔案**：
   - 對於每個 UVA 題目（例如 `106`）：
     ```bash
     mkdir -p uva/src/main/java/com/algorithm/solutions/uva/p106
     mv uva/106/src/Main.java uva/src/main/java/com/algorithm/solutions/uva/p106/Main.java
     mkdir -p uva/src/main/resources/uva/p106
     mv uva/106/1.in uva/src/main/resources/uva/p106/1.in
     ```
   - 對於 `nowcoder`：
     ```bash
     mv nowcoder/*.java nowcoder/src/main/java/com/algorithm/solutions/nowcoder/
     ```
3. **更新 Java 檔案**：
   - 加入適當的套件宣告（例如，對於 `uva/106/Main.java`，加入 `package com.algorithm.solutions.uva.p106;`）。
4. **添加 `pom.xml` 檔案**：
   - 將父層 `pom.xml` 置於 `algorithm-solutions/`。
   - 按照所示放置 `nowcoder/pom.xml` 和 `uva/pom.xml`。
5. **建置**：
   ```bash
   mvn clean install
   ```

### 注意事項
- **輸入檔案**：如果您的 `Main.java` 讀取輸入檔案如 `1.in`，請更新代碼以透過 `getClass().getResource("/uva/p106/1.in")` 或類似方法存取它們，因為它們現在位於 `src/main/resources` 中。
- **忽略 `.iml` 檔案**：在 `.gitignore` 檔案中加入 `*.iml`，以從版本控制中排除 IntelliJ 專案檔案。
- **其他目錄**：對於 `codeforces`、`hacker_rank` 等，您可以在準備好時創建類似的模組。如果您需要這些模組的 `pom.xml` 檔案，請告知我。
- **Java 版本**：如果您使用不同的 Java 版本，請調整 `<maven.compiler.source>` 和 `<maven.compiler.target>`。

如果您偏好選項 2 或需要特定問題的協助（例如調整 `Main.java` 以載入資源），請告知我！