---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GPG暗号化オプションの解説
translated: true
type: note
---

### GPGオプションの説明

`gpg`コマンド（GNU Privacy Guard）は、暗号化、復号、鍵管理のためのツールです。ここで挙げられているオプションは、特定の受信者に対してファイルを暗号化する際によく一緒に使用されます。各オプションの意味は以下の通りです：

- **`--homedir <directory>`**: GnuPGのホームディレクトリを指定します（デフォルトは`~/.gnupg`）。GPGが鍵リング、設定ファイル、その他のデータを保存する場所です。`GNUPGHOME`環境変数を上書きし、カスタム場所へのGPG操作の分離（例：複数のプロファイルやセキュリティのため）に有用です。コマンドラインで指定する必要があります。

- **`-e`（または`--encrypt`）**: 公開鍵暗号方式を使用して入力データを暗号化します。これは非対称暗号化の主要モードで、データは受信者の公開鍵で暗号化されます。署名などの他のオプションと組み合わせることができます。

- **`-r <user-id>`（または`--recipient <user-id>`）**: 暗号化の受信者を指定します。`<user-id>`は鍵ID、メールアドレス、公開鍵に関連付けられた名前などが使用できます。GPGは対応する公開鍵を使用してデータを暗号化します。グループ暗号化のために複数の受信者をリストできます。

#### 使用例
これらのオプションを組み合わせた一般的なコマンドは以下のようになります：
```
gpg --homedir /path/to/custom/dir -e -r recipient@example.com inputfile.txt
```
これは、`/path/to/custom/dir`からの鍵を使用して`inputfile.txt`を`recipient@example.com`向けに暗号化し、`inputfile.txt.gpg`を生成します。

詳細については、`gpg --help`を実行するか、manページを参照してください。

[ArchWiki: GnuPG](https://wiki.archlinux.org/title/GnuPG)  
[GPG Cheat Sheet](https://irtfweb.ifa.hawaii.edu/~lockhart/gpg/)  
[GPG Command in Linux](https://www.tutorialspoint.com/unix_commands/gpg.htm)