---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GPGピンエントリーループバックモードの解説
translated: true
type: note
---

### GPGにおける`--pinentry-mode loopback`とは？

GNU Privacy Guard（GPG）において、`--pinentry-mode loopback`オプションは、暗号化・復号・署名操作中のパスフレーズプロンプトの処理方法を制御します。PinentryはGPGのパスフレーズ（秘密鍵のパスワードなど）を安全に入力する仕組みで、通常はグラフィカルダイアログ、コンソールプロンプトなどを介して行われます。

#### 主な意味と目的
- **ループバックモード**: この設定により、pinentryは「ループバック」動作を行い、GPGは外部のpinentryプログラム（GUIポップアップなど）を起動しません。代わりに、呼び出し元プロセス（スクリプトやアプリケーションなど）に直接問い合わせを返すことでpinentryを模倣します。これにより、対話的なユーザープロンプトなしで、標準入力（STDIN）、環境変数、ファイルなどを通じてプログラム的にパスフレーズを提供できます。

- **使用する理由**
  - **自動化**に最適：bashスクリプト、CI/CDパイプライン（GitHub Actionsなど）、ヘッドレス環境（SSHセッションなど）で、グラフィカルダイアログが表示できない場合に有効です。
  - 非対話的な設定でハングや失敗を防ぎます。
  - GnuPG 2.1.12以降では、`--allow-loopback-pinentry`によりループバックがデフォルトで許可されることが多いですが、明示的に`--pinentry-mode loopback`を設定することで使用が保証されます。

- **一般的な使用例**:
  スクリプト内でSTDIN経由でパスフレーズを提供しながらファイルを復号する場合：
  ```
  echo "your-passphrase" | gpg --pinentry-mode loopback --passphrase-fd 0 --decrypt encrypted-file.gpg > decrypted-file.txt
  ```
  - `--passphrase-fd 0`：ファイルディスクリプタ0（STDIN）からパスフレーズを読み取ります。
  - これは一度だけプロンプトを表示し（または設定によりキャッシュを使用）、非対話的に動作します。

#### 注意点
- **セキュリティ注意**: ループバックモードは、慎重に扱わないとプロセスリストやログでパスフレーズが公開される可能性があります—信頼できる環境でのみ使用してください。
- **設定**: グローバルに有効にするには、`~/.gnupg/gpg-agent.conf`に`allow-loopback-pinentry`を追加し、`gpgconf --reload gpg-agent`でリロードします。
- 繰り返しプロンプトが表示される場合は、`gpg-agent.conf`のキャッシュタイムアウトを確認してください（例：`default-cache-ttl 3600`で1時間）。

このモードは、Git署名やEmacsワークフローなど、GPGをツールに統合する開発者にとって特に便利です。

#### 参考文献
- [How do I use gpg --pinentry-mode loopback in a bash script?](https://stackoverflow.com/questions/77231645/how-do-i-use-gpg-pinentry-mode-loopback-in-a-bash-script)
- [Agent OPTION (GnuPG Manual)](https://www.gnupg.org/documentation/manuals/gnupg/Agent-OPTION.html)
- [GnuPG - ArchWiki](https://wiki.archlinux.org/title/GnuPG)