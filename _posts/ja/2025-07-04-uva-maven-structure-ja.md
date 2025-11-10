---
audio: false
generated: true
lang: ja
layout: post
title: UVA問題のためのMaven構造
translated: true
type: note
---

あなたの `uva/106` サブディレクトリの具体的なディレクトリ構造を共有していただきありがとうございます。あなたのプロジェクトは、各UVA問題（例: `106`）が独自の `src` フォルダ（中に `Main.java` ファイル）と入力ファイル（例: `1.in`）を持つ、より細かい構造になっているようです。これは、各問題が個別のサブプロジェクトまたはモジュールとして扱われていることを示唆しています。これをMavenのマルチモジュール設定に対応させるには、以下の2つの方法があります：
1. 各問題ディレクトリ（例: `uva/106`）を独自のMavenサブモジュールとして扱う。
2. `uva` を単一のモジュールとして維持し、問題ファイルをその `src/main/java` ディレクトリ内で整理する。

UVA問題の数（あなたが以前示したリスト: `100`, `10000` など）を考慮すると、各問題に対して個別のMavenモジュールを作成すると、モジュール数が多くなり扱いにくくなる可能性があります。その代わりに、`uva` を単一のモジュールとし、各問題の `Main.java` を `uva/src/main/java` 内でパッケージ構造（例: 問題106用に `com.algorithm.solutions.uva.p106`）の下に整理する構造を提案します。これにより、プロジェクトの管理性を維持しつつ、Mavenの利点を活かすことができます。

ただし、もしその細かい粒度を希望される場合は、各問題を個別のサブモジュールとする代替案も提供します。以下に、あなたの構造に基づいて `pom.xml` ファイルを更新し、ファイルを再編成する手順を示します。

---

### オプション1: 問題をパッケージで整理した単一の `uva` モジュール

#### 更新後のディレクトリ構造
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
│   │               └── (その他)
│   └── resources/
│       └── uva/
│           ├── p100/
│           │   └── 1.in
│           ├── p106/
│           │   └── 1.in
│           └── (その他)
└── README.md
```

#### 親 `pom.xml` (ルート: `algorithm-solutions/pom.xml`)
これは以前とほぼ同じままです。`nowcoder` と `uva` をモジュールとして定義します。

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

#### Nowcoder サブモジュール `pom.xml` (`nowcoder/pom.xml`)
これは前回の応答から変更なく、`nowcoder` ファイルが `src/main/java/com/algorithm/solutions/nowcoder/` に移動されていることを想定しています。

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

#### UVA サブモジュール `pom.xml` (`uva/pom.xml`)
このモジュールには、`1.in` のような入力ファイル用の `resources` ディレクトリが含まれます。各問題の `Main.java` ファイルはパッケージ内で整理されます。

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

#### ファイルの構成
- **Javaファイルの移動**:
  - 各問題（例: `uva/106/src/Main.java`）について、`Main.java` を `uva/src/main/java/com/algorithm/solutions/uva/p106/Main.java` に移動します。
  - `Main.java` ファイルを更新して、パッケージ宣言を含めるようにします:
    ```java
    package com.algorithm.solutions.uva.p106;
    public class Main {
        // ... 既存のコード ...
    }
    ```
  - すべての問題（例: `p100`, `p10000` など）に対してこれを行います。

- **入力ファイルの移動**:
  - `uva/106/1.in` のような入力ファイルを `uva/src/main/resources/uva/p106/1.in` に移動します。
  - これにより、MavenがこれらのファイルをJARに含め、Javaコード内で `ClassLoader.getResource()` または類似の方法でアクセスできるようになります。

#### プログラムの実行
特定のUVA問題（例: 問題106）を実行するには:
```bash
mvn -pl uva exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
```

---

### オプション2: 各UVA問題をサブモジュールとして構成
もし各UVA問題（例: `106`, `100`）を独自のMavenモジュールにしたい場合は、以下のように設定します。これはより細かい粒度ですが、`pom.xml` ファイルの数が増加します。

#### 更新後のディレクトリ構造
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
│   │       └── (入力ファイルがあれば)
│   └── (他の問題ディレクトリ)
└── README.md
```

#### 親 `pom.xml` (ルート: `algorithm-solutions/pom.xml`)
各問題をモジュールとして追加します。

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

#### Nowcoder サブモジュール `pom.xml` (`nowcoder/pom.xml`)
上記と同じ（変更なし）。

#### UVA 問題106 サブモジュール `pom.xml` (`uva/106/pom.xml`)
各問題が独自の `pom.xml` を持ちます。以下は `uva/106` の例です:

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

- **他の問題についても繰り返し**: `uva/100`, `uva/10000` などに対して、`artifactId` (例: `uva-100`), `name`, `mainClass` (例: `com.algorithm.solutions.uva.p100.Main`) を調整した同様の `pom.xml` ファイルを作成します。

#### ファイルの構成
- **Javaファイルの移動**:
  - `uva/106/src/Main.java` を `uva/106/src/main/java/com/algorithm/solutions/uva/p106/Main.java` に移動します。
  - パッケージ宣言を追加します:
    ```java
    package com.algorithm.solutions.uva.p106;
    public class Main {
        // ... 既存のコード ...
    }
    ```
- **入力ファイルの移動**:
  - `uva/106/1.in` を `uva/106/resources/1.in` に移動します。

#### プログラムの実行
問題106を実行するには:
```bash
mvn -pl uva/106 exec:java -Dexec.mainClass="com.algorithm.solutions.uva.p106.Main"
```

---

### 推奨事項
- **オプション1 (単一の `uva` モジュール)** は、よりシンプルでスケーラブルです。特に多くのUVA問題がある場合に有効です。多数の `pom.xml` ファイルを作成することを避け、プロジェクト構造をクリーンに保ちます。問題を論理的に整理するためにパッケージを使用してください。
- **オプション2 (問題ごとのモジュール)** は、各問題を完全に独立させたい場合（例: 個別のデプロイやテストのため）に適しています。ただし、モジュール数の多さによりメンテナンスがより多く必要になります。

### オプション1を実装する手順
1. **ディレクトリ構造の作成**:
   - `algorithm-solutions` ルートで以下のコマンドを実行します:
     ```bash
     mkdir -p uva/src/main/java/com/algorithm/solutions/uva
     mkdir -p uva/src/main/resources/uva
     mkdir -p nowcoder/src/main/java/com/algorithm/solutions/nowcoder
     ```
2. **ファイルの移動**:
   - 各UVA問題（例: `106`）について:
     ```bash
     mkdir -p uva/src/main/java/com/algorithm/solutions/uva/p106
     mv uva/106/src/Main.java uva/src/main/java/com/algorithm/solutions/uva/p106/Main.java
     mkdir -p uva/src/main/resources/uva/p106
     mv uva/106/1.in uva/src/main/resources/uva/p106/1.in
     ```
   - `nowcoder` について:
     ```bash
     mv nowcoder/*.java nowcoder/src/main/java/com/algorithm/solutions/nowcoder/
     ```
3. **Javaファイルの更新**:
   - 適切なパッケージ宣言を追加します（例: `uva/106/Main.java` に対して `package com.algorithm.solutions.uva.p106;`）。
4. **`pom.xml` ファイルの追加**:
   - 親 `pom.xml` を `algorithm-solutions/` に配置します。
   - 示されているように `nowcoder/pom.xml` と `uva/pom.xml` を配置します。
5. **ビルド**:
   ```bash
   mvn clean install
   ```

### 注意点
- **入力ファイル**: あなたの `Main.java` が `1.in` のような入力ファイルを読み込む場合、コードを更新して `getClass().getResource("/uva/p106/1.in")` または類似の方法でアクセスするようにしてください。これらは現在 `src/main/resources` 内にあります。
- **`.iml` ファイルの無視**: `.gitignore` ファイルに `*.iml` を追加して、IntelliJプロジェクトファイルをバージョン管理から除外します。
- **他のディレクトリ**: `codeforces`, `hacker_rank` などについては、準備ができたら同様のモジュールを作成できます。それら用の `pom.xml` ファイルが必要な場合はお知らせください。
- **Javaバージョン**: 異なるJavaバージョンを使用する場合は、`<maven.compiler.source>` と `<maven.compiler.target>` を調整してください。

オプション2を希望される場合、または特定の問題（例: リソース読み込みのための `Main.java` の調整）に関するヘルプが必要な場合は、お知らせください！