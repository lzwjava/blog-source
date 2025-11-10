---
audio: false
generated: true
lang: ja
layout: post
title: Mavenにおけるアルゴリズムソリューションの統合
translated: true
type: note
---

`nowcoder`、`uva`などのすべてのアルゴリズムソリューションを、`algorithm-solutions`ルートディレクトリにある1つの`pom.xml`ファイルで管理される単一のMavenモジュールに統合するには、プロジェクト全体を1つのモジュールとして扱います。`nowcoder`と`uva`（および`codeforces`、`hacker_rank`などの他のディレクトリ）からのJavaファイルは、適切なパッケージ構造（例: `com.algorithm.solutions.nowcoder`、`com.algorithm.solutions.uva`）で`src/main/java`の下に整理されます。入力ファイル（例: `1.in`）は`src/main/resources`に配置されます。

### 前提条件
- すべてのJavaファイル（例: `nowcoder/Main.java`、`uva/106/src/Main.java`）は`src/main/java/com/algorithm/solutions/<platform>`（例: `nowcoder`、`uva/p106`）に移動されます。
- 入力ファイル（例: `uva/106/1.in`）は`src/main/resources/<platform>`（例: `uva/p106`）に移動されます。
- プロジェクトはJava 17を使用します（`pom.xml`で調整可能）。
- `pom.xml`は`algorithm-solutions`ルートディレクトリに配置され、サブモジュールは使用しません。

### ディレクトリ構造
再編成後（`uva`用の前回の応答のPythonスクリプトと、`nowcoder`用の同様のスクリプトを実行したと仮定）、構造は以下のようになります:

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
│   │   │       │   └── (その他)
│   │   │       ├── codeforces/
│   │   │       └── hacker_rank/
│   │   └── resources/
│   │       ├── nowcoder/
│   │       │   └── (入力ファイルがある場合)
│   │       ├── uva/
│   │       │   ├── p106/
│   │       │   │   └── 1.in
│   │       │   ├── p100/
│   │       │   └── (その他)
│   │       ├── codeforces/
│   │       └── hacker_rank/
└── README.md
```

### 親`pom.xml`
この`pom.xml`は`algorithm-solutions`ルートディレクトリに配置します。プロジェクトを単一モジュールとして構成し、入力ファイルのリソースを含め、Java 17用のMavenコンパイラを設定します。

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

### `pom.xml`に関する注記
- **パッケージング**: 単一の実行可能モジュールであるため、`jar`に設定されています。
- **リソース**: 入力ファイル用に`src/main/resources`から`*.in`ファイルを含めます。
- **メインクラス**: デフォルトとして`com.algorithm.solutions.nowcoder.Main`に設定されています。各問題が独自の`Main`クラスを持つ可能性があるため、通常は`mvn exec:java`を使用して特定のクラスを実行します。
- **Javaバージョン**: Java 17を使用します。必要に応じて`<maven.compiler.source>`と`<maven.compiler.target>`を調整してください。

### セットアップ手順
1. **ディレクトリ構造の作成**:
   ```bash
   mkdir -p src/main/java/com/algorithm/solutions/{nowcoder,uva,codeforces,hacker_rank}
   mkdir -p src/main/resources/{nowcoder,uva,codeforces,hacker_rank}
   ```

2. **ファイルの移動**:
   - `nowcoder`の場合:
     ```bash
     mkdir -p src/main/java/com/algorithm/solutions/nowcoder
     mv nowcoder/*.java src/main/java/com/algorithm/solutions/nowcoder/
     ```
     各Javaファイルにパッケージ宣言を追加します（例: `Main.java`）:
     ```java
     package com.algorithm.solutions.nowcoder;
     // ... 残りのコード ...
     ```
   - `uva`の場合、前回の応答のPythonスクリプトを使用するか、手動で実行します:
     ```bash
     mkdir -p src/main/java/com/algorithm/solutions/uva/p106
     mv uva/106/src/Main.java src/main/java/com/algorithm/solutions/uva/p106/Main.java
     mkdir -p src/main/resources/uva/p106
     mv uva/106/1.in src/main/resources/uva/p106/1.in
     ```
     `Main.java`にパッケージ宣言を追加します:
     ```java
     package com.algorithm.solutions.uva.p106;
     // ... 残りのコード ...
     ```
     他のUVA問題（`100`、`10000`など）についても繰り返します。

3. **`pom.xml`の配置**:
   - 上記の`pom.xml`を`algorithm-solutions`ルートディレクトリに保存します。

4. **プロジェクトのビルド**:
   ```bash
   mvn clean install
   ```

5. **特定のプログラムの実行**:
   - `nowcoder`の問題の場合:
     ```bash
     mvn exec:java -Dexec.mainClass="com.algorithm.solutions.nowcoder.Main"
     ```
   - UVA問題の場合（例: 問題106）:
     ```bash
     mvn exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
     ```

### `nowcoder`用Pythonスクリプト
前回の`uva`スクリプトを補完するために、`nowcoder`ファイルを`src/main/java/com/algorithm/solutions/nowcoder/`に移動し、パッケージ宣言を追加するPythonスクリプトを以下に示します。このスクリプトを`algorithm-solutions`ルートディレクトリから実行してください。

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

### 注記
- **スクリプトの実行**: ファイルを移動するには、`reorganize_uva.py`（前回の応答から）と`reorganize_nowcoder.py`スクリプトを実行します:
  ```bash
  python reorganize_uva.py
  python reorganize_nowcoder.py
  ```
- **入力ファイル**: `nowcoder`に入力ファイルがある場合、スクリプトを修正して`*.in`ファイルを`src/main/resources/nowcoder/`に移動してください。
- **他のディレクトリ**: `codeforces`、`hacker_rank`などの場合、ソースディレクトリとパッケージ名を変更して`nowcoder`スクリプトを適応させることができます。
- **リソースアクセス**: Javaコードを更新して、入力ファイルを`src/main/resources`から読み取るようにします（例: `getClass().getResource("/uva/p106/1.in")`）。
- **ファイルの無視**: IntelliJプロジェクトファイルを除外するために、`*.iml`を`.gitignore`ファイルに追加します。

他のディレクトリ用のスクリプトや`pom.xml`のさらなる調整が必要な場合はお知らせください！