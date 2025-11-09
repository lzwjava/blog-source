---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast:free
title: 壊れたPython GIバインディングの修復
translated: true
type: note
---

### 診断の更新
新しい詳細情報に基づくと、Python 3.13.7のインストール（手動またはPPA/ソース経由の可能性が高い）により、システムのGObject Introspection（GI）バインディングが破損しています。`gi`モジュールの`_gi` C拡張は、ディストリビューションのデフォルトPython（おそらく3.10または3.11。`/usr/lib/python`内のディレクトリから判断）用にコンパイルされており、3.13用ではありません。これが原因で、`gnome-terminal`（Pythonスクリプト）がこれを読み込もうとした際に循環インポートエラーが発生します。`/usr/lib/python`内のマルチバージョン設定はこの不一致を裏付けており、`python3-gi`のようなシステムパッケージはまだ3.13用にビルドされていません（2025年現在、ほとんどのディストリビューションにとって新しすぎるバージョンです）。

UFWのログは無関係なノイズのままです。

### 推奨される修正: システムデフォルトのPythonに戻す
最もクリーンな解決策は、`/usr/bin/python3`をディストリビューションのデフォルト（例: 3.10）に戻し、GIバインディングを再インストールすることです。これにより、.soファイルをコピーするようなハックを避けられ、不整合が生じるリスクを減らせます。

1. **デフォルトのPythonバージョンを特定し、切り替える**（`update-alternatives`が設定されている場合は使用。それ以外の場合は手動でシンボリックリンクを作成）:
   ```
   # alternativesが設定されているか確認
   sudo update-alternatives --config python3
   ```
   - オプションがリストされた場合、最も優先度の低いもの（通常、ディストリビューションのデフォルト、例: 3.10）を選択してください。
   - alternativesがない場合（標準のUbuntuで一般的）、手動で戻します:
     ```
     # デフォルトが3.10と仮定（Ubuntu 22.04で一般的。ベースが3.11の場合は3.11に置き換え）
     sudo rm /usr/bin/python3
     sudo ln -s /usr/bin/python3.10 /usr/bin/python3
     ```
   - 確認: `python3 --version` が 3.10.x（またはデフォルトのバージョン）を表示するはずです。

2. **GIおよびGNOME Terminalパッケージを再インストール**:
   ```
   sudo apt update
   sudo apt install --reinstall python3-gi gir1.2-glib-2.0 gnome-terminal
   ```

3. **テスト**:
   ```
   python3 -c "from gi.repository import GLib, Gio; print('GI OK')"
   gnome-terminal
   ```
   - Pythonテストが成功してもターミナルが起動しない場合は、その設定をリセットしてください: `dconf reset -f /org/gnome/terminal/`.

### Python 3.13を保持したい場合
- これはより困難です。公式の`python3-gi`はまだ3.13用に存在しないためです。PyGObjectをソースからコンパイルする必要があります:
  1. ビルド依存関係をインストール: `sudo apt install libgirepository1.0-dev libcairo2-dev pkg-config python3.13-dev`.
  2. PyGObjectをダウンロードしてビルド: [公式ガイド](https://pygobject.gnome.org/install.html)に従い、`--prefix=/usr/local`を指定します。
  3. ただし、これにより他のシステムツールが壊れるリスクがあります。問題が発生した場合は元に戻してください。
- または、`_gi`拡張をハック的にコピーします（長期的には非推奨）:
  ```
  cd /usr/lib/python3/dist-packages/gi/
  sudo cp _gi.cpython-3[01]m*.so _gi.cpython-313m-x86_64-linux-gnu.so  # '3[01]'をデフォルト（3.10または3.11）に調整
  ```
  その後、上記のように`python3-gi`を再インストールします。

### 予防策
- `/usr/bin/python3`を手動で上書きしないでください。3.13が必要なプロジェクトには仮想環境（`python3 -m venv myenv`）を使用してください。
- deadsnakes PPA経由で3.13をインストールした場合は、それを削除し、ディストリビューションのPythonを使用してください。

これで修正されない場合は、`ls -l /usr/bin/python*` と `dpkg -l | grep python3 | grep -E 'gi|default'` を実行し、出力を共有してください。

[gnome-terminal will not start after trying to install newer version of Python 3](https://askubuntu.com/questions/880188/gnome-terminal-will-not-start-after-trying-to-install-newer-version-of-python-3)  
[ImportError: cannot import name '_gi' from partially initialized module 'gi'](https://stackoverflow.com/questions/59838238/importerror-cannot-import-name-gi-from-partially-initialized-module-gi-mo)  
[Why won't terminal open?](https://www.reddit.com/r/Ubuntu/comments/1f9qh0a/why_wont_terminal_open/)