---
audio: false
generated: true
lang: ja
layout: post
title: リポジトリをMavenマルチモジュールに変換
translated: true
type: note
---

`algorithm-solutions`リポジトリをMavenで管理されるマルチモジュールJavaプロジェクトに変換するには、ルートディレクトリに親`pom.xml`ファイル、各サブモジュール（`nowcoder`と`uva`）に個別の`pom.xml`ファイルが必要です。親`pom.xml`は共通の設定を定義しサブモジュールを管理し、各サブモジュールの`pom.xml`は固有の設定を扱います。

以下に、親プロジェクトと2つのサブモジュール用の`pom.xml`ファイルを示します。以下の前提とします：
- プロジェクトはJava 17を使用（現代的なプロジェクトで一般的なバージョン。必要に応じて調整してください）。
- `nowcoder`と`uva`ディレクトリは標準的なMaven構造（`src/main/java`）でJavaソースファイルを含む。
- 現時点では外部依存関係は不要だが、構造は簡単な追加を可能にする。
- 各サブモジュールはJARとしてパッケージ化される（これらはスタンドアロンのアルゴリズム解法である可能性が高いため）。

### ディレクトリ構造
設定後、あなたのディレクトリ構造は以下のようになるはずです：

```
algorithm-solutions/
├── pom.xml
├── nowcoder/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── (あなたのJavaファイル, 例: Main.java, nc140 など)
├── uva/
│   ├── pom.xml
│   └── src/
│       └── main/
│           └── java/
│               └── (あなたのJavaファイル, 例: 100.java, 10000.java など)
└── README.md
```

### 親 `pom.xml`
このファイルはルートディレクトリ（`algorithm-solutions/pom.xml`）に配置します。親プロジェクトを定義し、サブモジュールをリストアップし、Javaバージョンやコンパイラ設定などの共通設定を設定します。

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

### Nowcoderサブモジュール `pom.xml`
このファイルは`nowcoder`ディレクトリ（`nowcoder/pom.xml`）に配置します。親から継承し、自身のアーティファクトの詳細を指定します。

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

### UVAサブモジュール `pom.xml`
このファイルは`uva`ディレクトリ（`uva/pom.xml`）に配置します。これも親から継承し、自身のアーティファクトの詳細を指定します。UVAの解法は通常単一の`Main`クラスを持たない（各問題がスタンドアロンのプログラムである可能性がある）ため、ここではメインクラスを指定しませんが、必要に応じて追加できます。

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

### 設定手順
1. **Mavenディレクトリ構造の作成**:
   - `nowcoder`内のJavaファイルを`nowcoder/src/main/java/`に移動します。
   - `uva`内のJavaファイルを`uva/src/main/java/`に移動します。
   - 例: `nowcoder/Main.java`は`nowcoder/src/main/java/Main.java`にあるべきです。

2. **`pom.xml`ファイルの配置**:
   - 親`pom.xml`を`algorithm-solutions`ルートディレクトリに配置します。
   - `nowcoder/pom.xml`を`nowcoder`ディレクトリに配置します。
   - `uva/pom.xml`を`uva`ディレクトリに配置します。

3. **プロジェクトのビルド**:
   - ターミナルで`algorithm-solutions`ルートディレクトリに移動します。
   - `mvn clean install`を実行して両方のサブモジュールをビルドします。

4. **特定のプログラムの実行**:
   - `nowcoder`の場合、`Main.java`がエントリーポイントであれば、以下で実行できます：
     ```bash
     mvn -pl nowcoder exec:java -Dexec.mainClass="Main"
     ```
   - UVAの解法の場合、各ファイルがスタンドアロンのプログラムである可能性があるため、特定のクラス（例: `100.java`）を以下で実行できます：
     ```bash
     mvn -pl uva exec:java -Dexec.mainClass="100"
     ```

### 注意点
- **Javaバージョン**: Java 17を使用しました。異なるバージョンが必要な場合は、親`pom.xml`の`<maven.compiler.source>`と`<maven.compiler.target>`プロパティを更新してください。
- **依存関係**: あなたの解法がライブラリ（例: 入出力ユーティリティ用）を必要とする場合、サブモジュールの`pom.xml`の`<dependencies>`セクションの下に追加してください。
- **ファイル命名**: Javaファイルがクラス名と一致していることを確認してください（例: `100.java`は`public class 100`を含むべきです）。
- **他のディレクトリ**: あなたのリポジトリには`codeforces`、`hacker_rank`などが含まれています。これらをサブモジュールとして含めたい場合は、親`pom.xml`に`<module>codeforces</module>`（など）を追加し、`nowcoder`や`uva`と同様にそれらのディレクトリに対応する`pom.xml`ファイルを作成してください。

追加のサブモジュールや特定の設定が必要な場合はお知らせください！