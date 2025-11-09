---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast:free
title: GNOME端末のPythonインポートエラー修正
translated: true
type: note
---

### 問題の診断
GNOME Terminal が起動しない原因は、GObject Introspection (GI) ライブラリにおける Python のインポートエラーです。トレースバックによると、`/usr/lib/python3/dist-packages/gi/__init__.py` の40行目、具体的には `from gi.repository import GLib, Gio` の部分でエラーが発生しています。完全なエラーメッセージ（一般的な報告に基づく）は、おそらく以下の通りです：

```
ImportError: cannot import name '_gi' from partially initialized module 'gi' (most likely due to a circular import)
```

このエラーは通常、手動での Python アップグレード、仮想環境、またはパッケージの破損により、システムの Python バージョンと GI バインディング（python3-gi パッケージ）の間の不一致が生じた場合に発生します。journalctl 出力にある UFW BLOCK ログは無関係です。これらはファイアウォールが（192.168.1.x からの他のデバイスによる mDNS/UPnP ディスカバリなどの）無害なマルチキャストトラフィックをドロップしているだけです。今のところこれらは無視してください。

### 試すべき簡単な修正
現在シェルプロンプトが動作している（`~/projects` にいるようです）ので、以下のコマンドを直接実行できます。最も単純なものから始めてください：

1. **GI パッケージと GNOME Terminal の再インストール**（最も一般的な修正）：
   ```
   sudo apt update
   sudo apt install --reinstall python3-gi gir1.2-glib-2.0 gnome-terminal
   ```
   その後、現在のシェルから `gnome-terminal` を実行してテストしてください。

2. **もしそれでうまくいかない場合、Python のシンボリックリンクを確認/修正**（最近 Python バージョンをいじった場合）：
   - システムの Python を確認：`ls -l /usr/bin/python3`（ディストリビューションのバージョンに応じて、python3.10 や 3.12 などを指しているはずです）。
   - 壊れている場合は、デフォルトの Python を再インストール：
     ```
     sudo apt install --reinstall python3-minimal
     ```
   - または手動でシンボリックリンクを設定（`3.10` はディストリビューションのデフォルトに置き換えてください）：
     ```
     sudo ln -sf /usr/bin/python3.10 /usr/bin/python3
     ```

3. **GNOME の完全リセット**（上記が失敗した場合。端末の設定はリセットされますが、データは消えません）：
   ```
   dconf reset -f /org/gnome/terminal/
   gnome-terminal --reset-config
   ```

4. **最終手段：GNOME Terminal の完全削除と再インストール**：
   ```
   sudo apt purge gnome-terminal
   sudo apt install gnome-terminal
   ```

修正後は、デスクトップ環境が変更を確実に認識するように、ログアウト/ログインするか再起動してください。Ubuntu/Debian 系を使用している（パスから推測）場合、これらは動作するはずです。他のディストリビューション（例: Fedora）の場合は、`apt` を `dnf` に置き換えてください。

どれも解決しない場合は、現在のシェルで `python3 -c "from gi.repository import GLib; print('OK')"` を実行し、さらなる手がかりのために出力を共有してください。

### 参考資料
- [Gnome terminal will not start after trying to install newer version of Python](https://askubuntu.com/questions/880188/gnome-terminal-will-not-start-after-trying-to-install-newer-version-of-python-3)
- [Why won't terminal open?](https://www.reddit.com/r/Ubuntu/comments/1f9qh0a/why_wont_terminal_open/)
- [ImportError: cannot import name '_gi' from partially initialized module](https://stackoverflow.com/questions/59838238/importerror-cannot-import-name-gi-from-partially-initialized-module-gi-mo)
- [Some applications not working on Zorin 17 Core](https://forum.zorin.com/t/some-applications-not-working-on-zorin-17-core/43391)