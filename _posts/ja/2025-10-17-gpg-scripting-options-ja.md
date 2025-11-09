---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: スクリプト用GPGコマンドオプション
translated: true
type: note
---

### GPG コマンドオプションの説明

`--batch`、`--yes`、`-o`、`--pinentry-mode` は、`gpg` (GNU Privacy Guard) コマンドで、暗号化、復号、署名などの非対話的な操作やスクリプト操作で使用される一般的なフラグです。以下にそれぞれの説明を示します：

- **`--batch`**: バッチモードを有効にします。これにより、`gpg` が対話的な質問を行ったり、対話的なコマンドを許可したりするのを防ぎます。これは、ユーザー入力が不可能なスクリプトや自動化に便利です。`--no-batch` で無効にできます。

- **`--yes`**: ほとんどの確認プロンプト (例: ファイルの上書き) に対して自動的に「はい」と答えるようにします。これにより、Yes/No の質問による実行の中断を回避します。

- **`-o` (または `--output`)**: 操作の出力先ファイルを指定します。このオプションの後にはファイル名を指定する必要があります (例: `-o output.txt`)。このオプションを指定しない場合、出力は標準出力またはデフォルトの場所に送られます。

- **`--pinentry-mode`**: GPG エージェントによる PIN 入力 (パスフレーズプロンプト) の処理方法を制御します。このオプションには、`ask` (デフォルト: グラフィカルまたはコンソールのプロンプトを表示)、`loopback` (スクリプト用に標準入力経由でパスフレーズを許可、ポップアップなし)、`cancel` (PIN を必要とする操作をキャンセル)、`error` (プロンプトを表示する代わりにエラーを返す) などのモード値を指定します。これは、安全な非対話的なパスフレーズ入力のために、バッチスクリプトで `loopback` と共に使用されることが多いです。

これらのオプションは、例えば `gpg --batch --yes -o decrypted.txt --pinentry-mode loopback --decrypt encrypted.gpg` のようにスクリプト内で組み合わせて使用され、完全に自動化された実行を実現します。

#### 参考文献
- [GPG マニュアルページ](https://linux.die.net/man/1/gpg)
- [GnuPG エージェントオプション](https://www.gnupg.org/documentation/manuals/gnupg/Agent-Options.html)
- [GnuPG マニュアル](https://www.gnupg.org/documentation/manuals/gnupg/index.html)