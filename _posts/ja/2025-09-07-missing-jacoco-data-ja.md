---
audio: false
date: 2025-09-07
generated: true
image: false
lang: ja
layout: post
title: JaCoCo実行データファイル欠落の解決
translated: true
type: note
---

JaCoCo実行データファイル（**'.exec'ファイル**）を生成するには、JaCoCoエージェントを付加してテストを実行する必要があります。「Skipping JaCoCo execution due to missing execution data file」というログメッセージは、`prepare-agent`ゴールが先に正常に実行されていない状態で`report`ゴールが実行されたことを示しています。

-----

### ステップ1: JaCoCo Mavenプラグインの設定

まず、`pom.xml`ファイルにJaCoCo Mavenプラグインが正しく設定されていることを確認してください。以下のようになっている必要があります：

```xml
<plugin>
    <groupId>org.jacoco</groupId>
    <artifactId>jacoco-maven-plugin</artifactId>
    <version>0.8.12</version>
    <executions>
        <execution>
            <goals>
                <goal>prepare-agent</goal>
            </goals>
        </execution>
        <execution>
            <id>report</id>
            <phase>test</phase>
            <goals>
                <goal>report</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

**`prepare-agent`**ゴールは、JaCoCoランタイムエージェントをセットアップするために重要です。このエージェントは、テスト実行中にコードを計装してカバレッジデータを収集します。

-----

### ステップ2: テストの実行

プラグインを設定した後、Mavenビルドを実行します。テストを実行してレポートを生成するための典型的なコマンドは：

`mvn clean install`

このコマンドを実行すると、Mavenは最初に`prepare-agent`ゴールを実行し、JaCoCoエージェントをJVMにアタッチします。その後、`test`フェーズが実行されると、エージェントがコードカバレッジデータを記録し、通常は**`target/jacoco.exec`**にファイルとして保存します。その後`report`ゴールが実行され、この`.exec`ファイルを読み取って最終的なHTMLまたはXMLレポートを生成します。

まだ問題が解決しない場合は、以下を確認してください：

  * **プロジェクト構造**: テストが標準のMavenディレクトリ`src/test/java`に配置されていることを確認してください
  * **テスト失敗**: テストが失敗している場合、`.exec`ファイルが生成される前にビルドが停止する可能性があります。まずテストの失敗を解決してください
  * **バージョンの不一致**: JaCoCoプラグインのバージョンが、使用しているMavenおよびJavaのバージョンと互換性があることを確認してください