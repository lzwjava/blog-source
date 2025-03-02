---
audio: true
generated: false
lang: ja
layout: post
title: JVM オプションの WebSphere Liberty サーバー
translated: true
---

WebSphere Liberty Profile (WLP) サーバーの `jvm.options` ファイルに設定された JVM オプションを確認するには、Java Development Kit (JDK) に含まれる `jinfo` コマンドを使用できます。この方法を使用すると、実行中のサーバーに適用されているオプションを効率的に確認できます。以下に、その手順を示します。

### JVM オプションの確認手順

1. **コンテキストの理解**
   サーバーディレクトリ（通常 `<WLP_HOME>/usr/servers/<serverName>/jvm.options`）にある `jvm.options` ファイルは、ヒープサイズ（例：`-Xmx`）、ガベージコレクション設定（例：`-XX:+UseG1GC`）、システムプロパティ（例：`-Dmy.property=value`）などの JVM 引数を指定するために使用されます。これらの設定は、Liberty サーバーが起動する際に適用されます。

2. **サーバーの起動**
   まず、以下のコマンドを使用して、Liberty サーバーをバックグラウンドで起動します：
   ```
   <WLP_HOME>/bin/server start <serverName>
   ```
   ここで、`<WLP_HOME>` は WebSphere Liberty のインストールパス、`<serverName>` はサーバー名に置き換えてください。このコマンドはサーバーをバックグラウンドプロセスとして起動します。

3. **プロセス ID (PID) の特定**
   サーバーを起動した後、実行中の Java プロセスのプロセス ID が必要です。Liberty はこれを以下の場所に保存します：
   ```
   <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
   ```
   このファイルを開いて（例：Unix 系システムでは `cat` コマンドを使用、テキストエディタを使用）サーバーのプロセスを表す数値の PID を取得します。

4. **JVM フラグの確認**
   `jinfo` コマンドを使用して、実行中のサーバーに適用されている JVM フラグを確認します。以下のコマンドを実行します：
   ```
   jinfo -flags <pid>
   ```
   ここで、`<pid>` は `.pid` ファイルから取得したプロセス ID に置き換えてください。このコマンドは、JVM に渡されたコマンドラインフラグ（例：`-Xmx1024m` または `-XX:+PrintGCDetails`）を出力します。出力を確認して、`jvm.options` に設定したフラグが含まれていることを確認します。

5. **システムプロパティの確認**
   `jvm.options` ファイルにシステムプロパティ（例：`-Dmy.property=value`）が含まれている場合は、以下のコマンドで個別に確認します：
   ```
   jinfo -sysprops <pid>
   ```
   これは、JVM に設定されたすべてのシステムプロパティを表示します。出力を検索して、定義した特定のプロパティが正しく適用されていることを確認します。

### 前提条件
- **JDK のインストール**: `jinfo` コマンドは JDK に含まれており、JRE に含まれていません。JDK がインストールされていることを確認し、`jinfo` 実行ファイルがシステムの PATH に含まれていることを確認してください。
- **権限**: `jinfo` をサーバーを起動した同じユーザーで実行するか、プロセスにアタッチするための十分な権限を持つユーザーで実行してください。

### 代替手法
`jinfo` が利用できない場合や他の方法を好む場合は、以下の 2 つの追加のオプションがあります：

- **`server dump` の使用**:
  1. サーバーを以下のコマンドで起動します：
     ```
     <WLP_HOME>/bin/server start <serverName>
     ```
  2. サーバーダンプを生成します：
     ```
     <WLP_HOME>/bin/server dump <serverName>
     ```
  3. 生成された `.zip` ファイルを `<WLP_HOME>/usr/servers/<serverName>/` に見つけ、展開して `javacore.<timestamp>.txt` ファイルを開きます。
  4. "CMDLINE" セクションを検索して、完全な Java コマンドライン（JVM フラグを含む）と "System Properties" セクションのシステムプロパティを確認します。

- **スタートアップスクリプトのトレース**（Unix 系システム）：
  1. トレースを有効にしてサーバースクリプトを実行します：
     ```
     sh -x <WLP_HOME>/bin/server start <serverName>
     ```
  2. 出力を確認して、スクリプトによって実行された Java コマンドを検索します。これは `jvm.options` からのすべてのオプションを含みます。

### 注意点
- **サーバーが実行されていない場合**: 無効なオプションによりサーバーが起動できない場合、`server run <serverName>` を使用してフォアグラウンドで実行し、コンソール出力を確認してエラーを確認するか、スクリプトのトレース方法を使用してコマンドを確認します。
- **ログファイル**: `<WLP_HOME>/usr/servers/<serverName>/logs/` にある `console.log` ファイルには、起動情報が含まれている場合がありますが、詳細なログが有効になっていない限り、すべての JVM オプションを信頼してリストすることはできません（例：`-XX:+PrintFlagsFinal`）。

### 結論
`jinfo` メソッドは、実行中の Liberty サーバーの `jvm.options` に設定された JVM オプションを確認する最も簡単な方法です。上記の手順に従うことで、JVM フラグとシステムプロパティが意図通りに適用されていることを確認できます。

---

`jinfo` コマンドはプロセスにアタッチできないと報告しました。

また、`javacore.<timestamp>.txt` ファイルは、ダンプコマンドを使用した後、期待される場所（`<WLP_HOME>/usr/servers/<serverName>/`）で見つからないことが報告されました。

WebSphere Liberty サーバーのバージョンは 24.0.0.9 です。

---

### WebSphere Liberty 24.0.0.9 での JVM オプションの確認に関する問題の解決

WebSphere Liberty Profile (WLP) サーバーのバージョン 24.0.0.9 で `jinfo` コマンドを使用して JVM オプションを確認する際に、エラーが表示され「プロセスにアタッチできない」と表示されました。また、サーバーダンプを生成した後、`javacore.<timestamp>.txt` ファイルが期待される場所（`<WLP_HOME>/usr/servers/<serverName>/`）で見つからないことが報告されました。以下に、これらの問題をトラブルシューティングし、解決するための詳細なガイドを示します。

---

### 問題の理解

- **`jinfo` の失敗**: 「プロセスにアタッチできない」エラーは、通常、`jinfo` が実行中の Java Virtual Machine (JVM) に接続できないことを示します。これは、権限の問題（例：サーバーを起動したユーザーとは異なるユーザーでコマンドを実行する）や、JVM プロセスに対する制限が原因です。
- **`javacore.<timestamp>.txt` が見つからない**: サーバーダンププロセスは、診断ファイルを含む `.zip` ファイルを生成するはずですが、その欠如は、ダンプが失敗したか、ファイルが予期しない場所にあるか、期待される内容が生成されなかったことを示します。

Unix 系システム（通常のファイルパスに基づく）で WebSphere Liberty 24.0.0.9 を使用しているため、解決策をそれに合わせて調整します。

---

### ステップバイステップの解決策

以下に、`jinfo` の代替手法を使用して JVM オプションを取得するための方法を示します。

#### 1. サーバーが実行中であることを確認
まず、Liberty サーバーが実行中であることを確認します：

- **コマンド**:
  ```bash
  <WLP_HOME>/bin/server status <serverName>
  ```
- **期待される出力**:
  実行中の場合、以下のようなメッセージが表示されます：「サーバー <serverName> はプロセス ID <pid> で実行中です。」実行中でない場合は、以下のコマンドで起動します：
  ```bash
  <WLP_HOME>/bin/server start <serverName>
  ```

- **PID の特定**:
  `<WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid` にあるプロセス ID を確認します：
  ```bash
  cat <WLP_HOME>/usr/servers/<serverName>/workarea/<serverName>.pid
  ```
  この PID を後続の手順で使用します。

#### 2. `jps -v` を `jinfo` の代替手法として使用
`jps` コマンド（JDK の一部）は、Java プロセスとそのオプションをリストアップし、`jinfo` が直面するアタッチの問題を回避することができます。

- **コマンド**:
  ```bash
  jps -v
  ```
- **出力**:
  Java プロセスのリスト、例：
  ```
  12345 Liberty -Xmx1024m -XX:+UseG1GC -Dmy.property=value
  ```
- **アクション**:
  `.pid` ファイルからの PID を一致させるか、コマンドラインに「Liberty」または `<serverName>` を検索して、サーバーのプロセスを特定します。リストされたオプション（例：`-Xmx1024m`、`-Dmy.property=value`）には、`jvm.options` からのものが含まれます。

- **権限の確認**:
  `jps -v` が失敗した場合や出力が表示されない場合は、サーバーを起動した同じユーザーとして実行するか（例：`sudo -u <serverUser> jps -v`）、`sudo` を使用して実行します：
  ```bash
  sudo jps -v
  ```

#### 3. `jcmd` を使用して詳細な JVM 情報を取得
`jps -v` が十分でない場合、`jcmd`（JDK の他のツール）を使用して、実行中の JVM を詳細にクエリできます。

- **コマンド**:
  - JVM オプション：
    ```bash
    jcmd <pid> VM.command_line
    ```
    出力：完全なコマンドライン、例：`java -Xmx1024m -XX:+UseG1GC -Dmy.property=value ...`
  - システムプロパティ：
    ```bash
    jcmd <pid> VM.system_properties
    ```
    出力：プロパティのリスト、例：`my.property=value`。

- **アクション**:
  `<pid>` をサーバーの PID に置き換えます。適切な権限（例：必要に応じて `sudo jcmd <pid> ...`）でこれらのコマンドを実行します。

#### 4. Javacore ファイルを生成して確認
サーバーダンプが期待される `javacore.<timestamp>.txt` を生成しない場合、独立した javacore ファイルを生成します：

- **コマンド**:
  ```bash
  <WLP_HOME>/bin/server javadump <serverName>
  ```
- **期待される出力**:
  javacore ファイルの場所を示すメッセージ、通常 `<WLP_HOME>/usr/servers/<serverName>/javacore.<timestamp>.txt`。

- **アクション**:
  - ディレクトリを確認：
    ```bash
    ls <WLP_HOME>/usr/servers/<serverName>/javacore.*.txt
    ```
  - ファイルを開き、以下を検索します：
    - **CMDLINE**: JVM オプション（例：`-Xmx1024m`）。
    - **システムプロパティ**: `-D` プロパティ。

- **トラブルシューティング**:
  ファイルが表示されない場合は、コマンドの実行中にサーバーの `console.log` または `messages.log`（`<WLP_HOME>/usr/servers/<serverName>/logs/`）を確認してエラーを確認します。

#### 5. サーバーダンプの方法を再確認
完全なサーバーダンプが正しく機能していることを確認します：

- **コマンド**:
  ```bash
  <WLP_HOME>/bin/server dump <serverName>
  ```
- **期待される出力**:
  `<serverName>.dump-<timestamp>.zip` という `.zip` ファイルが `<WLP_HOME>/usr/servers/<serverName>/` に生成されます。

- **アクション**:
  - ファイルが存在することを確認：
    ```bash
    ls <WLP_HOME>/usr/servers/<serverName>/*.zip
    ```
  - それを展開：
    ```bash
    unzip <serverName>.dump-<timestamp>.zip -d temp_dir
    ```
  - `javacore.<timestamp>.txt` を検索：
    ```bash
    find temp_dir -name "javacore.*.txt"
    ```
  - ファイルを開き、「CMDLINE」と「システムプロパティ」のセクションを確認します。

- **トラブルシューティング**:
  - コマンドのコンソール出力を確認します。
  - サーバーがダンプ中に実行中であることを確認します（ただし、`server dump` は停止したサーバーでも機能することがありますが、javacore は実行中の JVM が必要です）。
  - `.zip` ファイルが欠落している場合は、ログ（`<WLP_HOME>/usr/servers/<serverName>/logs/`）を確認してヒントを得ます。

#### 6. 詳細な JVM 出力を有効にする（最終手段）
すべての手法が失敗した場合、`jvm.options` を編集してすべての JVM フラグをログに記録します：

- **`<WLP_HOME>/usr/servers/<serverName>/jvm.options` を編集**:
  次を追加：
  ```
  -XX:+PrintFlagsFinal
  ```
- **サーバーを再起動**:
  ```bash
  <WLP_HOME>/bin/server stop <serverName>
  <WLP_HOME>/bin/server start <serverName>
  ```
- **ログを確認**:
  `<WLP_HOME>/usr/servers/<serverName>/logs/console.log` を開き、JVM フラグの表を検索します、例：
  ```
  [uintx] MaxHeapSize = 1073741824 {product}
  ```

---

### 追加の注意点

- **権限**:
  `jinfo` の失敗は、権限の不一致を示しています。一貫して、サーバーを起動した同じユーザー（例：`sudo -u <serverUser>` またはそのユーザーとしてログイン）ですべてのコマンドを実行します。
- **WebSphere Liberty 24.0.0.9**:
  ダンプの動作は、ドキュメントに記載されているプロセス（`.zip` ファイルが `<WLP_HOME>/usr/servers/<serverName>/` に含まれ、`javacore.<timestamp>.txt`）に従うはずです。バージョン固有の変更がある場合は、IBM のドキュメントを確認してくださいが、`server javadump` メソッドは信頼性が高いです。
- **JDK の要件**:
  JDK（JRE ではなく）がインストールされていることを確認してください。`jps`、`jcmd`、`jinfo` は JDK ツールです。

---

### 推奨されるアプローチ

1. **まず `jps -v` を試す**: 迅速で、アタッチの問題を回避する可能性があります。
2. **`jcmd` に戻る**: `jps` が十分でない場合に詳細な出力を提供します。
3. **`server javadump` を使用**: javacore を直接生成し、完全なダンプの複雑さを回避します。
4. **ダンプのデバッグ**: 必要に応じて `server dump` を再実行し、`.zip` ファイルの内容を確認します。

これらの手順に従うことで、JVM オプションを取得し、`jinfo` と `javacore` ファイルの問題を解決できます。特定のエラーが発生した場合は、お知らせください！