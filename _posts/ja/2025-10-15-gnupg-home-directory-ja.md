---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GnuPGホームディレクトリの内容解説
translated: true
type: note
---

これらのファイルとディレクトリは、GnuPG（GPG）のホームディレクトリ（`~/.gnupg/`）の一部であり、暗号化、署名、認証のための暗号鍵と関連データを格納します。GPGは安全な通信とデータ保護のためのツールです。以下は、標準的なGnuPG 2.1+の動作に基づく各要素の詳細です：

- **openpgp-revocs.d**: 鍵ペアを作成する際に生成される失効証明書（`.rev`ファイル）を格納するディレクトリ。これらは、鍵が侵害された場合や不要になった場合に鍵を失効（無効化）し、それ以降の使用を防ぐために使用されます。

- **private-keys-v1.d**: GnuPG 2.1で導入されたモダンな鍵形式で、あなたのプライベート（秘密）鍵を格納するディレクトリ。各鍵はセキュリティと管理を向上させるために個別のファイルに保存されます。これはあなたのデジタル金庫のようなものなので、厳重に保護してください。

- **pubring.kbx**: 新しい「キーボックス」形式（`.kbx`）の公開鍵リングファイル。他の人からインポートした公開鍵を保持し、それらに対するメッセージの暗号化や署名の検証に使用します。

- **pubring.kbx~**: `pubring.kbx`のバックアップコピー。GPGによる編集や更新中に自動的に作成されます。チルダ（`~`）サフィックスは、バックアップを示す一般的なLinuxの慣例です。

- **trustdb.gpg**: トラストデータベースファイル。公開鍵に割り当てた信頼レベル（例：自身の鍵には「究極」、他の鍵には署名に基づくレベル）を追跡します。これにより、GPGは検証に信頼できる鍵かどうかを判断します。

最近鍵を生成またはインポートした場合、このセットアップは正常です。常に`~/.gnupg/`ディレクトリ全体を安全にバックアップし、プライベート鍵を決して共有しないでください。詳細については、公式のGnuPGドキュメントを参照してください。

[Using the GNU Privacy Guard](https://www.gnupg.org/documentation/manuals/gnupg.pdf)  
[GnuPG Part 2 - Create and Manage Keys](https://www.hacksanity.com/kb/gnupg-create-manage-keys/)  
[How to Back Up and Restore Your GPG Keys on Linux](https://www.howtogeek.com/816878/how-to-back-up-and-restore-gpg-keys-on-linux/)  
[GPG(1) Manual](https://www.gnupg.org/(en)/documentation/manuals/gnupg24/gpg.1.html)