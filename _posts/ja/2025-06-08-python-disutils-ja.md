---
audio: false
generated: true
lang: ja
layout: post
title: Python distutils ModuleNotFoundError の修正
translated: true
type: note
---

このエラーは、Pythonの標準ライブラリに含まれる`distutils`モジュールが環境に存在しないために発生します。これは最小限のPythonインストール環境でよく見られます。以下の方法で修正できます：

### 解決策：
1. **Python開発ツールをインストール**（`distutils`を含む）：
   ```bash
   sudo apt update && sudo apt install python3-distutils python3-dev
   ```

2. **`setuptools`を再インストール**（正常な機能を確保するため）：
   ```bash
   pip install --upgrade --force-reinstall setuptools
   ```

3. **requirementsのインストールを再試行**：
   ```bash
   pip install -r requirements.local.txt
   ```

### この解決策が有効な理由：
- `python3-distutils`は不足している`distutils`モジュールを提供します
- `python3-dev`は必要なヘッダーファイルとビルドツールを含みます
- `setuptools`の再インストールは残存する設定問題を解決します

仮想環境を使用している場合は、システムパッケージをインストールした後、環境を再作成して必要なモジュールに確実にアクセスできるようにしてください。