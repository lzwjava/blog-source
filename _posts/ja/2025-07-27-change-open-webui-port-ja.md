---
audio: false
generated: true
image: false
lang: ja
layout: post
title: Open WebUIポートの変更
translated: true
type: note
---

`open-webui serve` コマンド（通常はpip経由でインストール後）を使用してOpen WebUIを実行する際にポートを変更するには、`--port` フラグに続けて希望するポート番号を指定します。デフォルトのポートは8080です。

### 手順:
1. Open WebUIがインストールされていることを確認します:  
   ```
   pip install open-webui
   ```

2. 別のポート（例: 3000）でサーバーを実行します:  
   ```
   open-webui serve --port 3000
   ```

   - これにより、WebUIは `http://localhost:3000` （または新しいポートを使用するサーバーのIPアドレス）でアクセス可能になります。
   - 注意: `serve` コマンドを使用する場合、`PORT` 環境変数は無視されます。代わりに `--port` フラグを使用する必要があります。

代わりにDockerを使用している場合:
- `PORT` 環境変数を設定します（例: `docker run -e PORT=3000 ...`）。
- `-p <ホストポート>:3000` でポートを外部にマップします（必要に応じて調整してください）。

完全なインストールと設定の詳細については、公式ドキュメントを参照してください。

[Environment Variable Configuration | Open WebUI](https://docs.openwebui.com/getting-started/env-configuration/)  
[Quick Start | Open WebUI](https://docs.openwebui.com/getting-started/quick-start/)