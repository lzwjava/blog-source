---
audio: false
generated: true
lang: ja
layout: post
title: IntelliJ IDEAの組み込みリモートデバッグ
translated: true
type: note
---

WebSphere Liberty サーバーを `server debug default` で起動し、そのデバッグポートに WebSphere Liberty プラグインを使用せずに IntelliJ IDEA を接続するには、IntelliJ IDEA の組み込みのリモートデバッグ機能を活用できます。このアプローチが機能するのは、WebSphere Liberty がデバッグモードで起動されると、(通常デフォルトで 7777 の) デバッグポートを公開し、IntelliJ IDEA を含む任意の JVM デバッガーがこれにアタッチできるためです。これを実現する詳細な手順を以下に示します。

---

### ステップ 1: WebSphere Liberty サーバーをデバッグモードで起動する
`server debug default` を実行すると (「default」はサーバー名と仮定。異なる場合は実際のサーバー名に置き換えてください)、WebSphere Liberty はデバッグが有効な状態で起動します。デフォルトでは、このコマンドはサーバーがデバッグ接続をポート **7777** で待ち受けるように設定します。

- **コマンド**:
  ```bash
  server debug default
  ```
- **動作**: これにより「default」サーバーがデバッグモードで起動し、JVM デバッグオプション (例: `-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=7777`) が自動的に有効になります。
- **確認**: コマンド実行後、サーバーのコンソール出力またはログ (例: `messages.log`) を確認し、サーバーがデバッグポートで待機していることを確認してください。デバッグポート (通常は 7777。上書きされていないか、利用可能な場合) を示すメッセージを探してください。

---

### ステップ 2: デバッグポートを確認する
WebSphere Liberty のデフォルトのデバッグポートは **7777** です。ただし、このポートが使用中であるか、カスタマイズされている場合:
- サーバー起動後のコンソール出力を確認してください。「Listening for debugger connections on port 7777」のようなメッセージが表示されることがあります。
- ポートが異なる場合 (例: 競合によりランダムなポートが割り当てられた場合)、IntelliJ IDEA で使用する実際のポート番号をメモしてください。

このガイドでは、設定が特に示されない限り、デフォルトのポート **7777** を前提とします。

---

### ステップ 3: IntelliJ IDEA でリモートデバッグを設定する
IntelliJ IDEA のリモートデバッグ機能を使用すると、特定の WebSphere プラグインを必要とせずにサーバーの JVM に接続できます。設定方法は以下のとおりです。

1.  **実行/デバッグ構成を開く**:
    - IntelliJ IDEA で、上部メニューから **Run > Edit Configurations** を選択します。

2.  **新しいリモートデバッグ構成を追加する**:
    - 左上隅の **+** ボタン (または「Add New Configuration」) をクリックします。
    - リストから **Remote JVM Debug** (使用している IntelliJ のバージョンによっては単に「Remote」と表示されている場合もあります) を選択します。

3.  **構成の詳細を設定する**:
    - **Name**: 意味のある名前を付けます (例: "WebSphere Liberty Debug")。
    - **Host**: `localhost` に設定します (サーバーが IntelliJ IDEA と同じマシンで実行されていると仮定。リモートの場合はサーバーの IP アドレスを使用)。
    - **Port**: `7777` (または実際のデバッグポートが異なる場合はそのポート) に設定します。
    - **Transport**: **Socket** に設定されていることを確認します。
    - **Debugger Mode**: **Attach** を選択します (これにより、IntelliJ は既に実行中の JVM に接続するようになります)。
    - (特定の JVM オプションが必要でない限り) 他の設定 (「Command line arguments for remote JVM」など) はデフォルトのままにします。

4.  **構成を保存する**:
    - **Apply**、次に **OK** をクリックして保存します。

---

### ステップ 4: デバッグを開始する
サーバーがデバッグモードで実行されており、構成が設定されている状態で:
- **Run > Debug** に移動する (または虫アイコンをクリックし)、新しい構成 (例: "WebSphere Liberty Debug") を選択します。
- IntelliJ IDEA は、指定されたホストとポートでサーバーの JVM にアタッチを試みます。
- 成功すると、デバッグウィンドウに「Connected to the target VM, address: 'localhost:7777'」のようなメッセージが表示されます。

---

### ステップ 5: アプリケーションをデバッグする
- **ブレークポイントの設定**: ソースコードで、行番号の横のガターをクリックして、実行を一時停止したい場所にブレークポイントを追加します。
- **実行のトリガー**: アプリケーションと対話して (例: サーバーにリクエストを送信する)、ブレークポイントにヒットさせます。
- **デバッグ**: ブレークポイントにヒットしたら、IntelliJ のデバッグツール (ステップオーバー、ステップイン、再開など) を使用して変数を検査し、実行を制御します。

---

### 追加の注意点
- **ローカルサーバーとリモートサーバー**: WebSphere Liberty が別のマシンで実行されている場合は、リモートデバッグ構成の `localhost` をサーバーの IP アドレスに置き換えてください。デバッグポート (例: 7777) が開いており、ファイアウォールでブロックされていないことを確認してください。
- **ポートの競合**: サーバー起動時にポート 7777 が利用できない場合、WebSphere Liberty はランダムなポートを選択する可能性があります。サーバーの出力を確認してポートを確認し、IntelliJ 構成をそれに合わせて更新してください。
- **プラグインは不要**: この方法は IntelliJ IDEA の標準的なリモートデバッグ機能を使用するため、WebSphere Liberty プラグインは必要ありません。

---

### まとめ
WebSphere Liberty サーバーを `server debug default` (デフォルトでポート 7777 でデバッグを有効にする) で起動し、IntelliJ IDEA でリモートデバッグ設定を構成することで、WebSphere Liberty プラグインを使用せずにサーバーのデバッグポートに接続できます。これにより、IntelliJ IDEA 内で直接、ブレークポイント、変数の検査、ステップ実行などの完全なデバッグ機能を利用できます。

---

専用の Liberty Tools プラグインを使用せずに IntelliJ IDEA で WebSphere Liberty アプリケーションを実行およびデバッグするには、Liberty ランタイムを手動でセットアップし、IntelliJ IDEA をリモートデバッグおよび外部ツール実行用に構成することで実現できます。このアプローチは、統合プラグインを使用する場合と比較していくつかの手動ステップを必要としますが、Liberty アプリケーションを開発およびトラブルシュートするために必要な機能を提供します。

プロセスの概要を以下に示します。

**1. WebSphere Liberty ランタイムを取得してインストールする:**

プラグインがないため、ランタイムを管理するには、WebSphere Liberty ランタイムを手動でダウンロードしてインストールする必要があります。ランタイムは、IBM の公式 Web サイトから、または Maven や Gradle を使用してプロジェクトを管理している場合はそれらのツールを介して他の配布方法から取得できます。

通常、手動インストールでは、ZIP または JAR ファイルをダウンロードし、システム上のディレクトリに抽出します。このディレクトリが Liberty のインストールホーム (`<LIBERTY_HOME>`) になります。

**2. デバッグ用に Liberty サーバーを構成する:**

アプリケーションをデバッグするには、デバッグが有効な状態で Liberty サーバーを起動する必要があります。これは、サーバー起動時に特定の JVM オプションを追加することで行われます。これらのオプションは、Java 仮想マシン (JVM) に特定のポートでデバッガ接続を待機するように指示します。

Liberty サーバー構成ディレクトリ (`<LIBERTY_HOME>/usr/servers/<your_server_name>/`) 内の `jvm.options` ファイルを探してください。このファイルが存在しない場合は作成できます。`jvm.options` ファイルに次の行を追加します。

```
-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005
```

  * `-agentlib:jdwp`: Java Debug Wire Protocol (JDWP) ライブラリをロードします。
  * `transport=dt_socket`: デバッガがソケットを使用して接続することを指定します。
  * `server=y`: JVM がサーバーとして動作し、デバッガ接続を待機することを示します。
  * `suspend=n`: JVM が起動前にデバッガの接続を待機すべきでないことを指定します。サーバー起動時に実行されるコードをデバッグする必要がある場合は、これを `suspend=y` に変更できます。
  * `address=5005`: デバッガが接続するポート番号を設定します。これは任意の利用可能なポートに変更できます。

**3. IntelliJ IDEA を Liberty 実行用に構成する:**

IntelliJ IDEA の「External Tools」構成を使用して、IDE 内から Liberty サーバーを起動できます。

  * `File` > `Settings` (または macOS では `IntelliJ IDEA` > `Preferences`) に移動します。
  * `Tools` > `External Tools` に移動します。
  * `+` アイコンをクリックして新しい外部ツールを追加します。
  * 以下の詳細でツールを構成します。
      * **Name:** 説明的な名前を付けます (例: 「Start Liberty Server」)。
      * **Program:** Liberty サーバースクリプトを参照します。通常、Linux/macOS では `<LIBERTY_HOME>/bin/server`、Windows では `<LIBERTY_HOME>\bin\server.bat` です。
      * **Arguments:** 特定のサーバーインスタンスを起動するための引数を追加します。通常は `start <your_server_name>` です。`<your_server_name>` は `<LIBERTY_HOME>/usr/servers/` 内のサーバーディレクトリの名前です。
      * **Working directory:** これを `<LIBERTY_HOME>/bin` に設定します。

これで、`Tools` > `External Tools` に移動し、今構成したツールを選択することで、Liberty サーバーを起動できるようになります。

**4. IntelliJ IDEA をリモートデバッグ用に構成する:**

手動で起動した Liberty サーバー上で実行されているアプリケーションをデバッグするには、IntelliJ IDEA の「Remote JVM Debug」構成を使用します。

  * `Run` > `Edit Configurations` に移動します。
  * `+` アイコンをクリックし、`Remote JVM Debug` を選択します。
  * 設定を構成します。
      * **Name:** 説明的な名前を付けます (例: 「Debug Liberty Server」)。
      * **Debugger mode:** `Attach to remote JVM` を選択します。
      * **Host:** `localhost` (または Liberty がローカルマシンで実行されていない場合は、そのマシンの IP アドレス) を入力します。
      * **Port:** `jvm.options` ファイルで構成したポート番号 (例: `5005`) を入力します。
      * **Use module classpath of:** IntelliJ IDEA プロジェクト内で Liberty アプリケーションコードを含むモジュールを選択します。これにより、IntelliJ IDEA が実行中のコードをソースファイルにマッピングしてデバッグするのに役立ちます。

**5. 実行とデバッグ:**

1.  IntelliJ IDEA で作成した「External Tools」構成を使用して Liberty サーバーを起動します。
2.  サーバーが起動し、構成したポートでデバッガを待機していることを示すまで待機します (サーバーコンソール出力にメッセージが表示されるはずです)。
3.  IntelliJ IDEA 内のアプリケーションコードにブレークポイントを設定します。
4.  `Run` > `Debug` に移動し、作成した「Debug Liberty Server」構成を選択します。

IntelliJ IDEA は、指定されたポートで実行中の Liberty サーバーへの接続を試みます。接続されると、コードのステップ実行、変数の検査、式の評価など、IntelliJ IDEA のデバッグ機能のすべてを使用できます。

これらの手順に従うことで、専用の Liberty Tools プラグインに依存せずに、IntelliJ IDEA で WebSphere Liberty アプリケーションを効果的に実行およびデバッグでき、サーバーのライフサイクルとデバッグプロセスを直接制御できます。