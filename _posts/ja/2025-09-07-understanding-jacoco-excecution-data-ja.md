---
audio: false
date: 2025-09-07
generated: true
image: false
lang: ja
layout: post
title: JaCoCo実行データファイルの理解
translated: true
type: note
---

以下は、実用的なすべてを網羅した解説です。

# `jacoco-it.exec`とは何か？

* **統合テスト**中に生成される**JaCoCo実行データファイル**です。
* 「`-it`」は単なる**慣例**です（`jacoco-maven-plugin`の*report-integration*ゴールおよびFailsafeフェーズに由来）。ユニットテストでは`jacoco.exec`に出力されることが多く、統合テストでは`jacoco-it.exec`に出力されます。
* 複数の`.exec`ファイルを（モジュールごと、フェーズごと、実行ごとに）生成し、後で**マージ**して単一のカバレッジレポートを生成できます。

典型的なMaven設定：

```xml
<plugin>
  <groupId>org.jacoco</groupId>
  <artifactId>jacoco-maven-plugin</artifactId>
  <version>0.8.12</version>
  <executions>
    <!-- ユニットテスト用 -->
    <execution>
      <id>prepare-agent</id>
      <goals><goal>prepare-agent</goal></goals>
    </execution>
    <!-- 統合テスト用 -->
    <execution>
      <id>prepare-agent-integration</id>
      <goals><goal>prepare-agent-integration</goal></goals>
    </execution>
    <execution>
      <id>report</id>
      <phase>verify</phase>
      <goals><goal>report</goal></goals>
    </execution>
    <execution>
      <id>report-it</id>
      <phase>verify</phase>
      <goals><goal>report-integration</goal></goals>
    </execution>
  </executions>
</plugin>
```

これは通常、`target/jacoco.exec`（ユニットテスト）と`target/jacoco-it.exec`（統合テスト）を書き出します。

# `.exec`ファイルの中身は？

* **プローブヒットのみ**で、クラスごとにキー付けされています。
* 具体的には：読み込まれた各クラスについて、JaCoCoは**ID**を（バイトコードに基づいて）計算し、**プローブのブール配列**（どの命令/ブランチが実行されたか）を保存します。
* また、**セッションID**とタイムスタンプも保存します。
* **クラスのバイトコード、メソッド名、行番号、ソースコードは含まれていません**。その構造情報は後で、HTML/XMLをレンダリングするために`jacoco:report`を実行する際に、あなたの**クラスファイル**と**ソースファイル**から取得されます。

含意：

* `.exec`を生成した後でクラスが変更されると、ファイルが一致しなくなる可能性があります（IDが合わなくなる）。レポートは常に、execを生成したのと**全く同じビルド**のクラスファイルに対して生成してください。

# クラス構造情報は含まれているか？

* **いいえ。** メソッド、行番号、ソースコードは含まれません。
* これはクラスごとのコンパクトなバイナリ形式の**ヒットマップ**です。レポートステップでは、あなたの**コンパイル済みクラス**（およびオプションでソース）を読み、それらのヒットをパッケージ、クラス、メソッド、行、ブランチにマッピングします。

# `-javaagent`経由でアタッチした場合、更新されるか？

短い答え：**はい**、ただし詳細があります：

* エージェント付きでJVMを起動すると、クラスを**その場で**インストルメント化し、プローブヒットを**メモリ内に**記録します。
* エージェントは`destfile`に書き込みます：

  * **JVM終了時**（`output=file`、デフォルトの場合）、または
  * 明示的に**ダンプ**した場合（TCP/JMX/API経由）、または
  * `append=true`が設定されている場合、既存ファイルを上書きする代わりに**追加/マージ**します。

一般的なエージェントオプション：

```bash
-javaagent:/path/to/org.jacoco.agent.jar=\
destfile=/path/to/jacoco-it.exec,\
append=true,\
output=file
```

その他の便利なモード：

* `output=tcpserver`（ポートで待機；接続してダンプをトリガー可能）
* `output=tcpclient`（サーバーにプッシュ）
* `jmx=true`（ダンプ/リセット用のJMX MBeanを公開）
* プログラムによる操作：`org.jacoco.agent.rt.RT.getAgent().dump(/*reset*/ true|false)`

「更新」に関する注意点：

* `output=file`**かつ**`append=true`の場合、**各ダンプ**でプローブ配列が既存ファイルにマージされます（ヒットの論理和）。
* `append=true`なしでは、次の書き込みでダンプ/終了時にファイルが**上書き**されます。
* **複数のJVM**（マイクロサービス、フォークされたテスト）がある場合、それぞれを**異なるファイル**に向けるか、TCP/JMXを使用して中央に収集し、その後マージします。

# 典型的なワークフロー

**統合テストフェーズ (Failsafe):**

* Mavenは、統合テストJVMにエージェントを`destfile=target/jacoco-it.exec`でアタッチします。
* 最後に、以下を読み取る`jacoco:report-integration`を実行します：

  * `target/jacoco-it.exec`（ヒット）
  * `target/classes`（構造）
  * `src/main/java`（行ソース用、オプション）
* 出力：*統合テストのみ*に対するHTML/XML/CSVカバレッジ。

**複数実行のマージ：**

```bash
# Maven経由
mvn jacoco:merge -Djacoco.destFile=target/merged.exec \
  -Djacoco.dataFileList="target/jacoco.exec,target/jacoco-it.exec,other.exec"
# その後
mvn jacoco:report -Djacoco.dataFile=target/merged.exec
```

# 実践的な落とし穴とヒント

* **ビルドの一致**: レポートは、`.exec`を生成したのと**同じコンパイル済みクラス**に対して生成してください。
* **並列フォーク**: テストを並列または複数JVMで実行する場合、同じファイルへの複数の書き込みを避けてください（`append=true`で同時追加が問題ない場合を除く）。より安全なのはJVMごとに1つのファイルを作成し、後でマージすることです。
* **長時間実行サービス**: **TCP/JMX**を有効にするか、ランタイムAPIを呼び出して**定期的にダンプ**してください；プロセス終了を待たないでください。
* **クラスローダ分離**: 一部のアプリケーションサーバーは同じクラスを2回ロードします；JaCoCoはクラスIDで重複排除しますが、複雑なコンテナ内では注意してください。
* **オフラインインストルメンテーション**も存在しますが、通常は**javaagent**アプローチの方がよりシンプルで堅牢です。

---

## あなたの質問への直接的な回答

* **「`jacoco-it.exec`とは何ですか？」**
  **統合テスト**中にキャプチャされた実行データファイル（プローブヒット）です。これは単なる命名規則です；機能的には`jacoco.exec`と同じフォーマットです。

* **「クラス構造情報は含まれていますか？」**
  **いいえ。** クラスごとの**プローブヒット配列**とセッションメタデータのみを保存します。クラス/メソッド/行情報は、レポートステップ中にあなたのコンパイル済みクラス/ソースから取得されます。

* **「`-javaagent`経由でアタッチした場合、更新されますか？」**
  **はい。** `output=file`の場合、エージェントは**JVM終了時**または**オンデマンド**（TCP/JMX/API経由）で書き込みます。`append=true`の場合、既存ファイルと**マージ**します；ない場合は**上書き**します。マルチJVM実行の場合は、別々のファイルを使用するか、リモートダンプと後での**マージ**を使用してください。