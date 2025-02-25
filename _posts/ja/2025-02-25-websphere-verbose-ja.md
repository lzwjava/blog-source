---
audio: false
lang: ja
layout: post
title: WebSphere Liberty サーバーでの詳細なログ記録
translated: true
---

あなたのWebSphere Liberty Profile (WLP) の `server` コマンドの詳細なログオプションに関する質問に対応するために、`server` コマンドが何をするか、そして詳細度を制御する方法を明確にします。

WLP の `server` コマンドは、サーバーインスタンスを管理するために使用され、`start`、`stop`、`run`、`status` などのアクションがあります。例えば：

- `server start <serverName>` は、サーバーをバックグラウンドで起動し、出力をログファイル（例：`logs/console.log`）にリダイレクトします。
- `server run <serverName>` は、サーバーをフォアグラウンドで起動し、出力を直接ターミナルに表示します。

あなたの質問は、`server` コマンドの「詳細なログオプション」についてです。これは、コマンド自体の出力がより詳細になるか、管理するサーバーのログがより詳細になることを意味する可能性があります。オプションを探索した結果、`server` コマンドには `--verbose` や `-v` などの直接的なフラグはありません。代わりに、詳細度はサーバーのログ動作に関連しており、コマンドを呼び出す際に影響を受けます。

### 詳細なログの有効化
WLP では、ログの詳細度は `server` コマンドのフラグではなく、サーバーのログ設定を通じて制御されます。以下に、詳細なログを有効にする方法を示します。

#### 1. **`server.xml` でログを設定する**
詳細なログを有効にする主要な方法は、`server.xml` ファイル内の `<logging>` 要素を調整することです。このファイルは通常、`<WLP_HOME>/usr/servers/<serverName>/` にあります。詳細なトレース仕様を設定してログの詳細度を増やすことができます。例えば：

```xml
<logging traceSpecification="*=all" />
```

- `*=all` はすべてのトレースポイントを有効にし、ログを非常に詳細にします（デバッグに便利）。
- よりターゲット指向の詳細度を設定するには、コンポーネントを指定できます。例えば、`*=info:com.example.*=debug` は、デフォルトのレベルを `info` に設定し、`com.example` パッケージのレベルを `debug` に設定します。

他にも有用な属性があります：
- `logLevel`：一般的なログレベルを設定します（例：`INFO`、`DEBUG`、`TRACE`）。
- `consoleLogLevel`：コンソールに書き込まれるメッセージのレベルを制御します（例：`DEBUG` または `TRACE`）。

より細かいコンソールレベルの例：
```xml
<logging consoleLogLevel="DEBUG" traceSpecification="*=audit" />
```

`server start` を実行すると、ログ（詳細な出力を含む）は `logs/console.log` に記録されます。`server run` を使用すると、この詳細な出力は直接ターミナルに表示されます。

#### 2. **環境変数を使用する**
環境変数を使用してログの詳細度を制御することもできます。これらの変数は `server.xml` の設定を上書きまたは補完します。例えば、`server` コマンドを実行する前に `WLP_LOGGING_CONSOLE_LOGLEVEL` 変数を設定します：

```bash
export WLP_LOGGING_CONSOLE_LOGLEVEL=DEBUG
server start <serverName>
```

- これにより、コンソールのログレベルが `DEBUG` に設定され、より詳細な出力が確保されます。
- 有効なレベルには `INFO`、`DEBUG`、`FINE`、`FINER`、`FINEST` などがあります。

`server run` の場合、この設定によりターミナルの出力がより詳細になり、`server start` の場合は `console.log` に影響を与えます。

#### 3. **JVM 特有の詳細なオプション**
特定の詳細な出力（例：ガベージコレクションログ）が必要な場合は、JVM オプションを追加できます（ただし、これは `server` コマンドではなくサーバーのランタイムに関連します）。`<WLP_HOME>/usr/servers/<serverName>/` にある `jvm.options` ファイルに `-verbose:gc` を追加するか、`server.xml` を通じて含めます：

```xml
<jvmEntries verbose="gc" />
```

これにより、GC 関連のログが生成され、通常は `console.log` または `server run` でターミナルに表示されます。

### `server` コマンドとの関連性
- **直接的な `--verbose` オプションなし**：`server` コマンド自体（例：`server start`）には、実行ステップの詳細を基本的なステータスメッセージ（例："サーバーが開始されました"）を超える `--verbose` や同様のフラグはありません。
- **サーバーのログが詳細度を制御**：見る詳細度はサーバーのログ設定に依存します。`server run` を使用してログをリアルタイムでターミナルで観察するか、`server start` の後にログファイルを確認します。

例えば：
- `server.xml` に `<logging traceSpecification="*=all"/>` を含めると、`server run <serverName>` を実行するとターミナルに詳細なログが表示されます。
- `server start <serverName>` を実行すると、同じ詳細度が `logs/console.log` に表示されます。

### 推奨事項
`server` コマンドを使用して詳細なログを有効にするには：
1. `server.xml` を編集して詳細な `traceSpecification` を含めます（例：最大の詳細度を得るために `*=all` または特定のレベル `*=debug`）。
2. 代替として、環境に `WLP_LOGGING_CONSOLE_LOGLEVEL=DEBUG` を設定します。
3. `server run` を使用して詳細な出力を直接確認するか、`server start` を使用して `logs/console.log` を確認します。

このアプローチにより、デバッグや監視の要件に応じた詳細なログを得ることができます。

特定のもの（例：コマンド実行の詳細度ではなくサーバーログ）を意味する場合は、さらに詳しく教えてください！それ以外の場合、サーバーのログ設定を上記のように設定するのが、WLP で `server` コマンドを使用して詳細なログを有効にする標準的な方法です。