---
audio: false
generated: true
lang: ja
layout: post
title: PortAudioとPyAudio
translated: true
type: note
---

このエラーは、**pyaudio** がコンパイルするために必要な PortAudio の開発ヘッダーがシステムに存在しないために発生します。修正方法は以下の通りです：

### ステップバイステップの解決策：

1. **PortAudio 開発ヘッダーのインストール** (pyaudio に必要):
```bash
sudo apt update && sudo apt install portaudio19-dev
```

2. **Python 開発ツールのインストール** (まだインストールされていない場合):
```bash
sudo apt install python3-dev
```

3. **インストールの再試行**:
```bash
pip install -r requirements.local.txt
```

### まだ pycrypto の問題が発生する場合：
pycrypto パッケージは非推奨であり、互換性の問題がある可能性があります。`requirements.local.txt` を修正して **pycryptodome** に置き換えてください：

1. 要件ファイルを開く：
```bash
nano requirements.local.txt
```

2. `pycrypto` を以下に置き換える：
```
pycryptodome
```

3. 保存してインストールを再実行：
```bash
pip install -r requirements.local.txt
```

### これが機能する理由：
- `portaudio19-dev` は pyaudio のコンパイルに必要な PortAudio ヘッダーを提供します
- `python3-dev` には必要な Python 開発ヘッダーが含まれています
- `pycryptodome` は非推奨の pycrypto の代替としてメンテナンスされています

### pycrypto の代替方法（保持する必要がある場合）：
特に pycrypto が必要な場合は、まずビルド依存関係をインストールしてください：
```bash
sudo apt install build-essential libgmp-dev
pip install pycrypto
```
ただし、pycrypto は新しい Python バージョンとの互換性の問題があることに注意してください。

これらの手順を実行後、すべてのパッケージが正しくインストールされるはずです。レガシービルドに関する非推奨警告は情報提供のみを目的としており、インストールを妨げるものではありません - これらは将来 PEP 517 ビルドへの移行が必要であることを示しています。