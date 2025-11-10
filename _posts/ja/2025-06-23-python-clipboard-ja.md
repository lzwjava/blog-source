---
audio: false
generated: true
lang: ja
layout: post
title: UbuntuでのPythonクリップボードアクセス
translated: true
type: note
---

UbuntuでPythonを使用してクリップボード（ペーストボード）から読み取るには、`pyperclip`のようなライブラリを使用するか、`xclip`や`xsel`のようなシステムクリップボードユーティリティと連携する方法があります。以下に2つの一般的なアプローチを示します：

### アプローチ1: `pyperclip`を使用する
`pyperclip`はクリップボードにアクセスするためのクロスプラットフォームなPythonライブラリです。

1. **pyperclipのインストール**:
   ```bash
   pip install pyperclip
   ```

2. **クリップボードから読み取るPythonコード**:
   ```python
   import pyperclip

   # クリップボードの内容を読み取る
   clipboard_content = pyperclip.paste()
   print(clipboard_content)
   ```

3. **注意点**:
   - `pyperclip`はUbuntu上で`xclip`または`xsel`に依存するため、これらがインストールされていることを確認してください：
     ```bash
     sudo apt update
     sudo apt install xclip xsel
     ```
   - この方法はシンプルで、クロスプラットフォームで動作します。

### アプローチ2: `xclip`を直接使用する
システムクリップボードと直接連携する場合は、`xclip`を使用できます。

1. **xclipのインストール**:
   ```bash
   sudo apt update
   sudo apt install xclip
   ```

2. **Pythonコード: `xclip`を使用してクリップボードから読み取る**:
   ```python
   import subprocess

   # クリップボードの内容を読み取る
   process = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True, text=True)
   clipboard_content = process.stdout
   print(clipboard_content)
   ```

3. **注意点**:
   - このアプローチは`xclip`コマンドラインツールを直接呼び出します。
   - モダンなクリップボード（Ctrl+C/Ctrl+V）には`-selection clipboard`を、マウス選択クリップボードには`-selection primary`を使用します。
   - `xclip`がインストールされていることを確認してください。

### 推奨事項
- **`pyperclip`を使用する**: 特定の理由がない限り、シンプルさと移植性のために`pyperclip`を使用してください。
- どちらの方法もUbuntu上でクリップボードにアクセスするには`xclip`または`xsel`のインストールが必要です。
- クリップボードの内容がテキストでない場合（例：画像）、これらの方法は期待通りに動作しない可能性があり、`pyclip`のようなライブラリや非テキストデータに対する追加の処理が必要になります。

Ubuntu 22.04とPython 3.10でテスト済み。問題が発生した場合は、必要なツール（`xclip`または`xsel`）がインストールされていることと、クリップボードにテキストデータが含まれていることを確認してください。