---
audio: false
date: 2025-09-11
generated: true
image: false
lang: ja
layout: post
model: openai/gpt-5
title: JaCoCoカバレッジファイルと追記モード
translated: true
type: note
---

これはJaCoCoの動作における微妙だが重要な詳細です。

### `jacoco:prepare-agent`の動作

* Mavenが**`prepare-agent`**ゴールを実行するとき、実際にはすぐにカバレッジファイルを生成しません。
* 代わりに、テストやアプリケーションの実行中にカバレッジデータが収集されるように**JVMを設定**します（通常は`-javaagent:jacocoagent.jar`引数を介して）。
* `.exec`ファイルの場所は`jacoco.destFile`プロパティで制御されます（デフォルトは`target/jacoco.exec`ですが、`target/jacoco-it.exec`のようにカスタマイズされることが多いです）。

### ファイルが既に存在する場合の動作

* デフォルトでは、**JaCoCoはJVMがエージェントで起動するときにファイルを上書きします**。
* これは`prepare-agent`→テスト実行の毎回が*新しい*`.exec`ファイルを生成することを意味します。
* 自動的には追記されません — 他の設定をしない限り、古いデータは失われます。

### 代わりに追記する方法

複数の実行を同じexecファイルに累積させたい場合は、明示的に追記モードを有効にする必要があります：

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <configuration>
    <destFile>${project.build.directory}/jacoco-it.exec</destFile>
    <append>true</append>   <!-- ✅ カバレッジデータを追記 -->
  </configuration>
</plugin>
```

`<append>true>`を設定すると、ファイルが存在する場合、新しいカバレッジデータがそれにマージされます。

### 要約すると

* **デフォルト:** 毎回の実行で古い`.exec`が置き換えられます。
* **`append=true`の場合:** 複数のJVM実行（または複数のモジュール/テスト）からのカバレッジが同じファイルにマージされます。

---

**マルチモジュールMavenビルド**との連携（各モジュールが独自のJaCoCo execを書き込もうとする場合）についても説明しましょうか？これが上書きと追記の問題に遭遇する一般的な理由だからです。