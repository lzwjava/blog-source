---
audio: false
generated: true
lang: hant
layout: post
title: Maven 演算法解決方案整合
translated: true
type: note
---

為了將您所有的演算法解題方案（`nowcoder`、`uva` 等）整合到由 `algorithm-solutions` 根目錄中的單一 `pom.xml` 檔案管理的 Maven 模組中，我們將整個專案視為一個模組。來自 `nowcoder` 和 `uva`（以及其他目錄，如 `codeforces`、`hacker_rank` 等）的 Java 檔案將在 `src/main/java` 下以適當的套件結構（例如 `com.algorithm.solutions.nowcoder`、`com.algorithm.solutions.uva`）進行組織。輸入檔案（例如 `1.in`）將置於 `src/main/resources` 中。

### 假設條件
- 所有 Java 檔案（例如 `nowcoder/Main.java`、`uva/106/src/Main.java`）將被移至 `src/main/java/com/algorithm/solutions/<platform>`（例如 `nowcoder`、`uva/p106`）。
- 輸入檔案（例如 `uva/106/1.in`）將被移至 `src/main/resources/<platform>`（例如 `uva/p106`）。
- 專案使用 Java 17（可在 `pom.xml` 中調整）。
- `pom.xml` 將位於 `algorithm-solutions` 根目錄中，且不使用子模組。

### 目錄結構
重組後（假設您執行了先前針對 `uva` 的回應中的 Python 腳本，並對 `nowcoder` 執行了類似的腳本），結構將如下：

```
algorithm-solutions/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/algorithm/solutions/
│   │   │       ├── nowcoder/
│   │   │       │   ├── Main.java
│   │   │       │   ├── nc140.java
│   │   │       │   ├── nc45.java
│   │   │       │   ├── nc78.java
│   │   │       │   └── nc93.java
│   │   │       ├── uva/
│   │   │       │   ├── p100/
│   │   │       │   │   └── Main.java
│   │   │       │   ├── p106/
│   │   │       │   │   └── Main.java
│   │   │       │   ├── p10000/
│   │   │       │   │   └── Main.java
│   │   │       │   └── (等等)
│   │   │       ├── codeforces/
│   │   │       └── hacker_rank/
│   │   └── resources/
│   │       ├── nowcoder/
│   │       │   └── (輸入檔案，如有)
│   │       ├── uva/
│   │       │   ├── p106/
│   │       │   │   └── 1.in
│   │       │   ├── p100/
│   │       │   └── (等等)
│   │       ├── codeforces/
│   │       └── hacker_rank/
└── README.md
```

### 父層 `pom.xml`
此 `pom.xml` 置於 `algorithm-solutions` 根目錄中。它將專案配置為單一模組，包含輸入檔案的資源，並為 Java 17 設定 Maven 編譯器。

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.algorithm.solutions</groupId>
    <artifactId>algorithm-solutions</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>Algorithm Solutions</name>
    <description>Consolidated project for algorithm solutions from multiple platforms</description>

    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

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
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.13.0</version>
                <configuration>
                    <source>${maven.compiler.source}</source>
                    <target>${maven.compiler.target}</target>
                </configuration>
            </plugin>
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

### 關於 `pom.xml` 的說明
- **打包**：設定為 `jar`，因為這是一個單一的可執行模組。
- **資源**：包含來自 `src/main/resources` 的 `*.in` 檔案作為輸入檔案。
- **主類別**：預設設定為 `com.algorithm.solutions.nowcoder.Main`。由於每個問題可能有自己的 `Main` 類別，您通常會使用 `mvn exec:java` 來執行特定的類別。
- **Java 版本**：使用 Java 17；如有需要，可調整 `<maven.compiler.source>` 和 `<maven.compiler.target>`。

### 設定步驟
1. **建立目錄結構**：
   ```bash
   mkdir -p src/main/java/com/algorithm/solutions/{nowcoder,uva,codeforces,hacker_rank}
   mkdir -p src/main/resources/{nowcoder,uva,codeforces,hacker_rank}
   ```

2. **移動檔案**：
   - 對於 `nowcoder`：
     ```bash
     mkdir -p src/main/java/com/algorithm/solutions/nowcoder
     mv nowcoder/*.java src/main/java/com/algorithm/solutions/nowcoder/
     ```
     在每個 Java 檔案中添加套件宣告（例如 `Main.java`）：
     ```java
     package com.algorithm.solutions.nowcoder;
     // ... 其餘程式碼 ...
     ```
   - 對於 `uva`，使用先前回應中的 Python 腳本，或手動操作：
     ```bash
     mkdir -p src/main/java/com/algorithm/solutions/uva/p106
     mv uva/106/src/Main.java src/main/java/com/algorithm/solutions/uva/p106/Main.java
     mkdir -p src/main/resources/uva/p106
     mv uva/106/1.in src/main/resources/uva/p106/1.in
     ```
     在 `Main.java` 中添加套件宣告：
     ```java
     package com.algorithm.solutions.uva.p106;
     // ... 其餘程式碼 ...
     ```
     對其他 UVA 問題（`100`、`10000` 等）重複此操作。

3. **放置 `pom.xml`**：
   - 將上述 `pom.xml` 儲存在 `algorithm-solutions` 根目錄中。

4. **建置專案**：
   ```bash
   mvn clean install
   ```

5. **執行特定程式**：
   - 對於 `nowcoder` 問題：
     ```bash
     mvn exec:java -Dexec.mainClass="com.algorithm.solutions.nowcoder.Main"
     ```
   - 對於 UVA 問題（例如問題 106）：
     ```bash
     mvn exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
     ```

### 用於 `nowcoder` 的 Python 腳本
為了補充先前的 `uva` 腳本，這裡提供一個 Python 腳本，用於將 `nowcoder` 檔案移至 `src/main/java/com/algorithm/solutions/nowcoder/` 並添加套件宣告。請在 `algorithm-solutions` 根目錄下執行此腳本。

```python
import os
from pathlib import Path

def add_package_declaration(java_file, package):
    """Add package declaration to the top of a Java file if not already present."""
    with open(java_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.strip().startswith('package '):
        new_content = f'package {package};\n\n{content}'
        with open(java_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Added package declaration to {java_file}')

def reorganize_nowcoder():
    # Define paths
    nowcoder_root = Path('nowcoder')
    target_dir = Path('src/main/java/com/algorithm/solutions/nowcoder')

    # Create target directory
    target_dir.mkdir(parents=True, exist_ok=True)

    if not nowcoder_root.exists():
        print('Error: nowcoder directory not found.')
        return

    # Move Java files
    for java_file in nowcoder_root.glob('*.java'):
        target_file = target_dir / java_file.name
        shutil.move(str(java_file), str(target_file))
        print(f'Moved {java_file} to {target_file}')
        
        # Add package declaration
        add_package_declaration(target_file, 'com.algorithm.solutions.nowcoder')

    # Remove empty nowcoder directory
    if not any(nowcoder_root.iterdir()):
        nowcoder_root.rmdir()
        print(f'Removed empty directory {nowcoder_root}')

if __name__ == '__main__':
    reorganize_nowcoder()
    print('Nowcoder reorganization complete.')
```

### 注意事項
- **執行腳本**：執行 `reorganize_uva.py`（來自先前的回應）和 `reorganize_nowcoder.py` 腳本來移動檔案：
  ```bash
  python reorganize_uva.py
  python reorganize_nowcoder.py
  ```
- **輸入檔案**：如果 `nowcoder` 有輸入檔案，請修改腳本以將 `*.in` 檔案移至 `src/main/resources/nowcoder/`。
- **其他目錄**：對於 `codeforces`、`hacker_rank` 等，您可以透過更改來源目錄和套件名稱來改編 `nowcoder` 腳本。
- **資源存取**：更新您的 Java 程式碼以從 `src/main/resources` 讀取輸入檔案（例如 `getClass().getResource("/uva/p106/1.in")`）。
- **忽略檔案**：將 `*.iml` 添加到 `.gitignore` 檔案中以排除 IntelliJ 專案檔案。

如果您需要其他目錄的腳本或對 `pom.xml` 進行進一步調整，請告訴我！