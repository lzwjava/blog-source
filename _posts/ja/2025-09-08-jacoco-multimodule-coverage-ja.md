---
audio: false
date: 2025-09-08
generated: true
image: false
lang: ja
layout: post
title: マルチモジュールカバレッジレポート戦略
translated: true
type: note
---

もちろんです。外部統合テストにおけるJaCoCoの複雑さに関するあなたの分析は、特に的を射ています。ビルドを2回実行するのは確かに理想的ではありません。

あなたが求めている戦略は、テスト実行を一元化し、その結果を集約するものです。あなたのアプローチは非常に近く、`aggregate`ゴールが確かに正しいツールですが、このシナリオでは特定の方法で適用する必要があります。

以下が推奨される戦略です：**Webアプリケーションモジュールで1つのカバレッジファイル（`.exec`）を生成し、別の専用のレポートモジュールを使用して、関連するすべてのモジュールに対する単一の集約レポートを作成します。**

このアプローチはクリーンで、スケーラブルであり、冗長なビルドを回避します。

-----

## 核となるコンセプト

あなたの`PlaygroundWeb`アプリケーションがJaCoCoエージェントとともにJettyで実行されると、エージェントは**アプリケーションのクラスローダーによってロードされたすべてのクラス**を計装します。これには、`PlaygroundWeb`自体のクラス*と*、`PlaygroundUtils.jar`のようなすべての依存関係のクラスが含まれます。

したがって、`PlaygroundWeb`のビルド中に生成される単一の`jacoco-it.exec`ファイルには、**両方のモジュール**に対するカバレッジデータが既に含まれています。課題は、JaCoCoレポートツールを、最終的なHTMLレポートを構築するために必要なすべてのモジュールのソースコードに向けることだけです。

-----

## 4ステップのスケーラブルな戦略

以下は、クリーンで集約されたカバレッジレポートのためにプロジェクトをリファクタリングするステップバイステップガイドです。

### ステップ 1: 専用のレポートモジュールを作成する

まず、集約のためだけに新しいモジュールを作成します。これは関心を分離するMavenのベストプラクティスです。

1.  ルートの`pom.xml`（`PlaygroundLib`）に、新しいモジュールを追加します：
    ```xml
    <modules>
        <module>PlaygroundUtils</module>
        <module>PlaygroundWeb</module>
        <module>PlaygroundReports</module> </modules>
    ```
2.  ルートに新しいディレクトリ`PlaygroundReports`を作成し、その中に独自の`pom.xml`を配置します。

新しいプロジェクト構造は以下のようになります：

```
.
├── PlaygroundReports
│   └── pom.xml
├── PlaygroundUtils
│   └── pom.xml
├── PlaygroundWeb
│   └── pom.xml
└── pom.xml
```

### ステップ 2: レポートモジュールの `pom.xml` を設定する

この新しい`pom.xml`が重要な役割を果たします。これは、レポートに含めたいすべてのモジュールに依存し、`report-aggregate`ゴールを実行します。

**`PlaygroundReports/pom.xml`:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>com.lzw</groupId>
        <artifactId>PlaygroundLib</artifactId>
        <version>1.0</version>
    </parent>
    <artifactId>PlaygroundReports</artifactId>
    <packaging>pom</packaging>
    <name>PlaygroundReports</name>

    <dependencies>
        <dependency>
            <groupId>com.lzw</groupId>
            <artifactId>PlaygroundWeb</artifactId>
            <version>${project.version}</version>
        </dependency>
        <dependency>
            <groupId>com.lzw</groupId>
            <artifactId>PlaygroundUtils</artifactId>
            <version>${project.version}</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <executions>
                    <execution>
                        <id>aggregate-report</id>
                        <phase>verify</phase>
                        <goals>
                            <goal>report-aggregate</goal>
                        </goals>
                        <configuration>
                            <dataFiles>
                                <dataFile>${project.basedir}/../PlaygroundWeb/target/jacoco-it.exec</dataFile>
                            </dataFiles>
                            <outputDirectory>${project.reporting.outputDirectory}/jacoco-aggregate</outputDirectory>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### ステップ 3: `PlaygroundWeb` モジュールを簡素化する

あなたの`PlaygroundWeb`モジュールは、**カバレッジデータを生成する**ことだけを担当し、それに対するレポート作成は行いません。その`pom.xml`から`jacoco:report`の実行を削除できます。

**`PlaygroundWeb/pom.xml` (変更点のみ):**

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>prepare-agent</id>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
            <configuration>
                <propertyName>jacoco.it.agent</propertyName>
                <destFile>${project.build.directory}/jacoco-it.exec</destFile>
            </configuration>
        </execution>
        </executions>
</plugin>

<plugin>
    <groupId>org.eclipse.jetty</groupId>
    <artifactId>jetty-maven-plugin</artifactId>
    <executions>
        <execution>
            <id>start-jetty</id>
            <phase>pre-integration-test</phase>
            <goals>
                <goal>start</goal>
            </goals>
            <configuration>
                <daemon>true</daemon>
                <jvmArgs>
                    ${jacoco.it.agent}
                </jvmArgs>
                </configuration>
        </execution>
        </executions>
</plugin>
```

*注記*: `prepare-agent`の設定を少し変更し、プロパティ（`jacoco.it.agent`）を使用して、そのプロパティを`jetty-maven-plugin`で参照するようにしました。これはエージェント文字列を渡すための堅牢な方法です。あなたの`pom.xml`の以前の設定も問題ありませんでしたが、この方が意図が明確になります。

### ステップ 4: `PlaygroundUtils` をクリーンアップする

`PlaygroundUtils`モジュールは、統合テストに関するJaCoCoプラグイン設定を必要としません。そのコードは`PlaygroundWeb`経由でカバーされ、レポート作成は`PlaygroundReports`によって処理されます。その`pom.xml`からJaCoCo関連のプロパティやプラグインを削除できます。

-----

## これがどのように問題を解決するか

1.  **単一ビルド:** ルートディレクトリから`mvn clean verify`を1回だけ実行します。
2.  **正しいライフサイクル:**
      * Mavenは`PlaygroundUtils`をビルドします。
      * Mavenは`PlaygroundWeb`をビルドし、JaCoCoエージェントとともにJettyを起動し、Pythonテストを実行し（これは両方のモジュールのコードにアクセスします）、Jettyを停止し、`PlaygroundWeb/target/jacoco-it.exec`を生成します。
      * Mavenは`PlaygroundReports`をビルドします。`verify`フェーズで、`report-aggregate`ゴールが実行されます。これは`PlaygroundWeb`からの`.exec`ファイルを見つけ、依存関係があるため、`PlaygroundWeb`と`PlaygroundUtils`の両方のソースコードを見つける場所を知っています。
      * 両方のモジュールに対するカバレッジを含む**単一の統一されたHTMLレポート**を生成します。
3.  **スケーラビリティ:** さらに10個のライブラリモジュールを追加した場合、それらを`PlaygroundReports/pom.xml`の依存関係として追加するだけです。コアロジックは変更されません。これはあなたが探していた、クリーンでスケーラブルなソリューションです。