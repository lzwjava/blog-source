---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: WebSphere Application Serverの正しい作成方法
translated: true
type: note
---

いいえ、`nodeName -name serverName admin create applciation server`（"applciation"のタイプミスに注意）というコマンドは、IBM WebSphere Application Server (WAS) で wsadmin スクリプティングを使用してアプリケーションサーバーを作成する正しいコマンドではありません。

### 正しい構文
適切なコマンドは、Jython（wsadmin で推奨されるスクリプト言語）の `AdminTask.createApplicationServer` メソッドを使用します。これには以下が必要です：
- 第一引数として**ノード名**（文字列）。
- サーバー名の `-name` を含む、第二引数としての**オプションのリスト**。

**基本的な例:**
```jython
AdminTask.createApplicationServer('YourNodeName', ['-name', 'YourServerName'])
```

- `'YourNodeName'` を実際のノード名（例: `ndnode1`）に置き換えてください。
- `'YourServerName'` を希望のサーバー名（例: `appServer1`）に置き換えてください。
- オプションのパラメータ（例: デフォルトサーバーテンプレートを使用するための `'-templateName', 'default'`）をリストに追加できます。

### 実行手順
1. Jython モードで wsadmin を開始: `./wsadmin.sh -lang jython -user admin -password pass`。
2. 上記のコマンドを実行。
3. 設定を保存: `AdminConfig.save()`。
4. 終了: `quit`。

これにより、指定されたノード上に基本的なアプリケーションサーバーが作成されます。より多くのオプション（例: ポート、JVM 設定）については、完全な AdminTask ドキュメントを参照してください。

[AdminTask オブジェクトの ServerManagement コマンドグループ](https://www.ibm.com/docs/en/was-nd/9.0.5?topic=scripting-servermanagement-command-group-admintask-object)  
[スクリプトを使用したサーバーの作成](https://www.ibm.com/docs/en/was/9.0.5?topic=scripting-creating-server-using)