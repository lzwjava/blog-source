---
audio: false
generated: true
lang: hant
layout: post
title: 轉換儲存庫為 Maven 多模組
translated: true
type: note
---

要將你的 `algorithm-solutions` 倉庫轉換為由 Maven 管理的多模組 Java 專案，你需要在根目錄中放置一個父級 `pom.xml`，並為每個子模組（`nowcoder` 和 `uva`）建立各自的 `pom.xml` 檔案。父級 `pom.xml` 將定義通用配置並管理子模組，而每個子模組的 `pom.xml` 則處理其特定設定。

以下，我將提供父專案及兩個子模組的 `pom.xml` 檔案。我假設：
- 專案使用 Java 17（現代專案常用版本；可根據需要調整）。
- `nowcoder` 和 `uva` 目錄包含採用標準 Maven 結構（`src/main/java`）的 Java 原始碼檔案。
- 目前暫不需要外部依賴，但此結構便於後續添加。
- 每個子模組將打包為 JAR（因為這些很可能是獨立的演算法解決方案）。

### 目錄結構
設定完成後，你的目錄結構應如下所示：

```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── (你的 Java 檔案，例如 Main.java、nc140 等)
├── uva/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── (你的 Java 檔案，例如 100.java、10000.java 等)
└── README.md
```

### 父級 `pom.xml`
此檔案位於根目錄（`algorithm-solutions/pom.xml`）。它定義了父專案，列出了子模組，並設定了通用配置，如 Java 版本和編譯器設定。

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

### Nowcoder 子模組 `pom.xml`
此檔案位於 `nowcoder` 目錄（`nowcoder/pom.xml`）。它繼承自父級，並指定其自身的工件詳情。

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
                            <mainClass>Main</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

### UVA 子模組 `pom.xml`
此檔案位於 `uva` 目錄（`uva/pom.xml`）。它同樣繼承自父級，並指定其自身的工件詳情。由於 UVA 解決方案通常沒有單一的 `Main` 類別（每個問題可能是一個獨立的程式），我在此未指定主類別，但你可以根據需要添加。

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

### 設定步驟
1. **建立 Maven 目錄結構**：
   - 將 `nowcoder` 中的 Java 檔案移至 `nowcoder/src/main/java/`。
   - 將 `uva` 中的 Java 檔案移至 `uva/src/main/java/`。
   - 例如，`nowcoder/Main.java` 應位於 `nowcoder/src/main/java/Main.java`。

2. **放置 `pom.xml` 檔案**：
   - 將父級 `pom.xml` 置於 `algorithm-solutions` 根目錄。
   - 將 `nowcoder/pom.xml` 置於 `nowcoder` 目錄。
   - 將 `uva/pom.xml` 置於 `uva` 目錄。

3. **建置專案**：
   - 在終端機中導航至 `algorithm-solutions` 根目錄。
   - 執行 `mvn clean install` 以建置兩個子模組。

4. **執行特定程式**：
   - 對於 `nowcoder`，如果 `Main.java` 是進入點，你可以使用以下指令執行：
     ```bash
     mvn -pl nowcoder exec:java -Dexec.mainClass="Main"
     ```
   - 對於 UVA 解決方案，由於每個檔案可能是一個獨立的程式，你可以使用以下指令執行特定類別（例如 `100.java`）：
     ```bash
     mvn -pl uva exec:java -Dexec.mainClass="100"
     ```

### 注意事項
- **Java 版本**：我使用了 Java 17。如果你需要其他版本，請更新父級 `pom.xml` 中的 `<maven.compiler.source>` 和 `<maven.compiler.target>` 屬性。
- **依賴項**：如果你的解決方案需要函式庫（例如用於輸入/輸出工具），請將其添加到子模組的 `pom.xml` 中的 `<dependencies>` 區段。
- **檔案命名**：請確保你的 Java 檔案與類別名稱相符（例如 `100.java` 應包含 `public class 100`）。
- **其他目錄**：你的倉庫包含 `codeforces`、`hacker_rank` 等目錄。如果你想將這些也作為子模組包含，請在父級 `pom.xml` 中添加 `<module>codeforces</module>`（依此類推），並在這些目錄中建立對應的 `pom.xml` 檔案，類似於 `nowcoder` 和 `uva`。

如果你需要其他子模組或特定配置，請告知！