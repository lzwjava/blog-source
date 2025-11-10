---
audio: false
generated: true
image: false
lang: ja
layout: post
title: PILイメージングバックエンドエラーの修正
translated: true
type: note
---

このエラーは、PILのインストールにバイナリバックエンド（`_imaging`）が欠けているか、もしくは最新の「Pillow」ではなく古い「PIL」パッケージを誤って使用していることを意味します。修正方法は以下の通りです：

1. **Python 3を使用していることを確認**
   `python`がPython 2を指している場合は、Python 3に切り替えてください：

   ```bash
   python3 --version
   python3 scripts/content/avatar.py
   ```

2. **古いPILパッケージをアンインストール**

   ```bash
   # pip経由でインストールされた古いPILを削除します
   python3 -m pip uninstall -y PIL
   ```

3. **Pillowを（再）インストール**

   ```bash
   python3 -m pip install --upgrade --force-reinstall pillow
   ```

4. **必要なシステムライブラリをインストール**
   Ubuntuでは、Pillowが`_imaging`拡張をビルドするためにイメージングヘッダーが必要です：

   ```bash
   sudo apt update
   sudo apt install -y libjpeg-dev zlib1g-dev
   # その後、Pillowを再インストールしてこれらのライブラリに対して再コンパイルします
   python3 -m pip install --upgrade --force-reinstall pillow
   ```

5. **仮想環境を使用する（任意ですが推奨）**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install pillow
   python scripts/content/avatar.py
   ```

これらを実行後、`from PIL import Image`は`_imaging`インポートエラーなしで動作するはずです。