---
audio: false
generated: true
image: false
lang: ja
layout: post
title: JVMオプション分類クイックガイド
translated: true
type: note
---

JVMの世界では、設定可能な**多数のオプション**が存在し、その正確なセットはJVMの実装（HotSpot、OpenJ9、GraalVMなど）とバージョンに依存します。大まかに、JVMオプションは以下のカテゴリに分類されます：

---

## 1. 標準オプション

これらは安定しており、バージョンを跨いで動作することが公式に文書化され保証されているオプションです。例：

* `-classpath` / `-cp` → クラスパスを指定
* `-Dproperty=value` → システムプロパティを設定
* `-version` → JVMのバージョンを表示
* `-Xms` / `-Xmx` → ヒープの初期サイズと最大サイズ
* `-ea` → アサーションを有効化

---

## 2. 非標準オプション (`-X`)

これらはJVM固有のオプションで、安定性が保証されていません。例（HotSpot）：

* `-Xint` → インタプリタモードのみ（JITなし）
* `-Xcomp` → 初回使用時に全てのメソッドをコンパイル
* `-Xbatch` → バックグラウンドコンパイルを無効化
* `-Xss512k` → スレッドスタックサイズを設定

---

## 3. 詳細オプション (`-XX`)

これらはGC、JIT、ランタイムの挙動に対するきめ細かいチューニングを提供します。例：

* `-XX:+UseG1GC` → G1ガベージコレクタを有効化
* `-XX:+PrintGCDetails` → GCアクティビティをログ出力
* `-XX:MaxMetaspaceSize=256m` → メタスペースの上限を設定
* `-XX:+HeapDumpOnOutOfMemoryError` → OOM発生時にヒープダンプを取得
* `-XX:+UnlockExperimentalVMOptions` → 実験的なフラグを許可
* `-XX:+UseStringDeduplication` → 文字列の重複排除によりメモリ使用量を削減

---

## 4. 診断 & 実験的オプション

一部のフラグは隠されており、アンロックが必要です：

* `-XX:+UnlockDiagnosticVMOptions` → 診断フラグを有効化
* `-XX:+UnlockExperimentalVMOptions` → 実験的なチューニングを許可

その後、以下のようなオプションが使用できます：

* `-XX:+PrintFlagsFinal` → 全てのJVMオプションとその値を一覧表示
* `-XX:+LogCompilation` → JITコンパイラのアクティビティをログ出力

---

## 5. JVMオプションを扱うツール

* **`java -X`** → 使用しているJVMビルドの非標準オプションを一覧表示
* **`java -XX:+PrintFlagsFinal`** → 認識される全てのオプションをデフォルト値と現在値で表示
* **`jcmd <pid> VM.flags`** → 実行中のプロセスのJVMフラグを表示
* **`jcmd <pid> VM.uptime`**, `jcmd <pid> VM.system_properties` → ランタイムの検査
* **`jps` + `jinfo`** → Javaプロセスを一覧表示し、JVMオプションを出力
* **VisualVM / JConsole** → ヒープ、GC、ランタイムパラメータを監視

---

👉 環境を探る実用的な方法は、以下を実行することです：

```bash
java -XX:+PrintFlagsFinal | grep GC
```

これによりGC関連のオプション全てを表示できます。あるいは単に：

```bash
java -X
```

で利用可能な非標準フラグを確認できます。

---

巨大な`PrintFlagsFinal`のリストを解析しなくて済むように、**最も有用なJVMオプション（GC、メモリ、デバッグ、パフォーマンスチューニング）をカテゴリ分けしたチートシート**をお伝えしましょうか？