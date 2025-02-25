---
audio: false
lang: ja
layout: post
title: JVM オプションの WebSphere Liberty サーバー
translated: true
---

WebSphere Liberty Profile (WLP) サーバーのサーバーディレクトリにある `jvm.options` ファイルに設定された JVM オプションを確認するには、Java Development Kit (JDK) に含まれる `jinfo` コマンドを使用できます。この方法を使用すると、実行中のサーバーに適用されたオプションを効率的に確認できます。以下に、これを実現するための手順を示します。

### JVM オプションの確認手順

1. **コンテキストの理解**
   サーバーディレクトリ（通常 `<WLP_HOME>/usr/servers/<serverName>/jvm.options`）にある `jvm.options` ファイルは、ヒープサイズ（例：`-Xmx`）、ガベージコレクション設定（例：`-XX:+UseG1GC`）、システムプロパティ（例：`-Dmy.property=value`）などの JVM 引数を指定するために使用されます。これらのオプションは、Liberty サーバーが起動する際に適用されます。

2. **サーバーの起動**
   まず、以下のコマンドを使用して、Liberty サーバーをバックグラウンドで起動します：
   ```
   <WLP_HOME>/bin/server start <serverName>
   ```
   `<WLP_HOME>` を WebSphere Liberty のインストールパスに、`<serverName>` をサーバー名に置き換えてください。このコマンドは、サーバーをバックグラウンドプロセスとして起動します。

3. **プロセスID (PID) の特定**
   サーバーを起動した後、実行中の Java プロセスのプロセスID が必要です。Liberty はこれを便利に `.pid` ファイルとして保存しています。その場所は以下の通りです：
   ```
   <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
   ```
   このファイルを開いて（例：Unix 系システムでは `cat` を使用、テキストエディタを使用）、サーバーのプロセスを表す数値の PID を取得します。

4. **JVM フラグの確認**
   `jinfo` コマンドを使用して、実行中のサーバーに適用された JVM フラグを確認します。以下を実行します：
   ```
   jinfo -flags <pid>
   ```
   `<pid>` を `.pid` ファイルから取得したプロセスID に置き換えてください。このコマンドは、JVM に渡されたコマンドラインフラグ（例：`-Xmx1024m` または `-XX:+PrintGCDetails`）を出力します。出力を確認して、`jvm.options` で設定したフラグが存在することを確認します。

5. **システムプロパティの確認**
   `jvm.options` ファイルにシステムプロパティ（例：`-Dmy.property=value`）が含まれている場合は、以下で個別に確認します：
   ```
   jinfo -sysprops <pid>
   ```
   これにより、JVM に設定されたすべてのシステムプロパティが表示されます。出力を検索して、正しく適用された特定のプロパティが存在することを確認します。

### 前提条件
- **JDK のインストール**: `jinfo` コマンドは JDK に含まれており、JRE に含まれていません。JDK がインストールされていることを確認し、`jinfo` 実行ファイルがシステムの PATH に含まれていることを確認してください。
- **権限**: サーバーを起動した同じユーザーで `jinfo` を実行するか、プロセスにアタッチするための十分な権限を持つユーザーで実行してください。

### 代替方法
`jinfo` が利用できない場合や他の方法を好む場合は、以下の 2 つの追加オプションがあります：

- **`server dump` の使用**:
  1. サーバーを `server start <serverName>` で起動します。
  2. サーバーダンプを生成します：
     ```
     <WLP_HOME>/bin/server dump <serverName>
     ```
  3. 生成された `.zip` ファイルを `<WLP_HOME>/usr/servers/<serverName>/` に見つけ、展開し、`javacore.<timestamp>.txt` ファイルを開きます。
  4. "CMDLINE" セクションを検索して、JVM フラグを含む完全な Java コマンドラインと "System Properties" セクションのシステムプロパティを確認します。

- **起動スクリプトのトレース** (Unix 系システム):
  1. トレースを有効にしてサーバースクリプトを実行します：
     ```
     sh -x <WLP_HOME>/bin/server start <serverName>
     ```
  2. 出力を確認して、スクリプトによって実行された Java コマンドを検索し、`jvm.options` からのすべてのオプションを含むことを確認します。

### 注意点
- **サーバーが起動しない場合**: 無効なオプションによりサーバーが起動しない場合、`server run <serverName>` を使用してフォアグラウンドで実行し、コンソール出力でエラーを確認するか、スクリプトのトレース方法を使用してコマンドを確認します。
- **ログファイル**: `<WLP_HOME>/usr/servers/<serverName>/logs/` にある `console.log` ファイルには、起動情報が含まれている場合がありますが、詳細なログが有効になっていない限り、すべての JVM オプションを信頼してリストすることはできません（例：`-XX:+PrintFlagsFinal`）。

### 結論
`jinfo` メソッドは、実行中の Liberty サーバーの `jvm.options` に設定された JVM オプションを確認する最も簡単な方法です。上記の手順に従うことで、JVM フラグとシステムプロパティが意図通りに適用されていることを確認できます。