---
audio: false
generated: true
image: false
lang: ja
layout: post
title: JaCoCoエージェント出力ディレクトリの設定
translated: true
type: note
---

はい — その通りです 👍。

デフォルトでは、以下のように記述した場合

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=jacoco.exec,output=file
```

`jacoco.exec` は JVM プロセスの**カレントワーキングディレクトリ**（多くの場合、サーバールートや Liberty を起動した場所）に作成されます。

出力先を制御したい場合は、**絶対パスまたは相対パス**を指定します。例えば：

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=/opt/coverage-data/jacoco.exec,output=file
```

または

```bash
-javaagent:/path/to/jacocoagent.jar=destfile=target/jacoco.exec,output=file
```

（`target/` は起動ディレクトリからの相対パスです）。

ですから、`.exec` ファイルの出力先を確実に指定したい場合は、フルパスを使用してください。

👉 ヒント：Maven/Gradle プロジェクトでは、後でレポートプラグインが自動的に取得できるように、`target/`（Maven）や `build/`（Gradle）に出力することが一般的です。

フルパスを設定した Liberty の `jvm.options` の例を見てみましょうか？