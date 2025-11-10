---
audio: false
generated: true
image: false
lang: ja
layout: post
title: 安全なOpen WebUIへの今すぐアップグレード
translated: true
type: note
---

了解しました。ここでは安全で無駄のないOpen WebUIのアップグレード方法をご紹介します。

## `pip`でインストールした場合（あなたのケース）

```bash
# 1) (推奨) Open WebUI用の環境をアクティベート
#    condaの場合:
conda activate open-webui
#    venvの場合:
# source ~/open-webui-venv/bin/activate

# 2) 最新版にアップグレード
python3.11 -m pip install -U open-webui

# 3) (オプション) pipキャッシュが問題を引き起こす場合
python3.11 -m pip cache purge
python3.11 -m pip install --no-cache-dir -U open-webui

# 4) インストールされたバージョンを確認
python3.11 -m pip show open-webui
```

公式ドキュメントによると、`pip install -U open-webui`だけで最新リリースにアップグレードできます。（[Open WebUI][1]）

### データ/設定を永続化する

サーバーを実行する際にデータディレクトリを指定すれば、アップグレード時に影響を受けません：

```bash
# macOS/Linux
DATA_DIR="$HOME/.open-webui" open-webui serve
# Windows (PowerShell)
$env:DATA_DIR="C:\open-webui\data"; open-webui serve
```

これはドキュメントのガイダンスに沿っており、`DATA_DIR`を設定することでチャット履歴や設定がパッケージインストール外で管理されます。（[Open WebUI][2]）

> ヒント：以前に`DATA_DIR`なしで実行していた場合は、今から使用してください。Open WebUIは今後そのフォルダを使用します。

## Dockerを使用した場合（参考まで）

```bash
# 古いコンテナを停止・削除（データは名前付きボリュームに保存）
docker rm -f open-webui

# 最新イメージをプル
docker pull ghcr.io/open-webui/open-webui:main

# 既存のボリュームで再起動
docker run -d -p 3000:8080 \
  -v open-webui:/app/backend/data \
  --name open-webui \
  ghcr.io/open-webui/open-webui:main
```

これはプロジェクトが推奨する手動アップデート手順です。データは`open-webui` Dockerボリュームに永続化されます。（[Open WebUI][3]）

## 「最新版」の確認

アップグレード前後にGitHub Releasesから最新のタグを確認できます。（[GitHub][4]）

エラーが発生した場合（例：Pythonバージョンの不一致）、pipメソッドを使用する場合はPython 3.11を使用していることを確認してください。これはプロジェクトが明示的に推奨しています。（[GitHub][5]）

現在の環境を確認したり、アップグレードエラーの出力を解釈するお手伝いが必要ですか？ここに貼り付けてください、トラブルシューティングいたします。

[1]: https://docs.openwebui.com/getting-started/quick-start/?utm_source=chatgpt.com "️ Quick Start"
[2]: https://docs.openwebui.com/?utm_source=chatgpt.com "Open WebUI: Home"
[3]: https://docs.openwebui.com/getting-started/updating/?utm_source=chatgpt.com "Updating Open WebUI"
[4]: https://github.com/open-webui/open-webui/releases?utm_source=chatgpt.com "Releases · open-webui/open-webui"
[5]: https://github.com/open-webui/open-webui?utm_source=chatgpt.com "open-webui/open-webui: User-friendly AI Interface ..."