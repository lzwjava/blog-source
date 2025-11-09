---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GPGデジタル署名の検証
translated: true
type: note
---

### GPGでの署名検証

GnuPG（GPG）ではデジタル署名を検証し、ファイルやメッセージが改ざんされておらず、主張された送信者からのものであることを確認できます。検証には、署名者の公開鍵があなたのキーリングに存在する必要があります。以下に、一般的なシナリオにおける手順とコマンドを示します。

#### 前提条件
1. **GPGのインストール**: システムにGnuPGがインストールされていることを確認してください（例: Debianベースのシステムでは`apt install gnupg`、macOSでは`brew install gnupg`）。
2. **署名者の公開鍵のインポート**: ファイルに署名した個人または団体の公開鍵が必要です。キーサーバーまたはファイルからダウンロードし、インポートします：
   ```
   gpg --import public-key.asc
   ```
   （`public-key.asc`を実際の鍵ファイルに置き換えてください。キーサーバーからの場合は、`gpg --keyserver keyserver.ubuntu.com --recv-keys KEYID`を使用します。`KEYID`は鍵のフィンガープリントまたはIDです。）

#### 検証手順
使用するコマンドは、署名の作成方法（例: ファイルにインラインで埋め込むか、別ファイルにするか）によって異なります。

1. **分離署名の検証**（ソフトウェアリリースなどのファイルで一般的。署名は別の`.sig`ファイルに存在）：
   ```
   gpg --verify signature.sig original-file
   ```
   - 正常な署名の場合の出力例：
     ```
     gpg: Signature made [date] using [key type] key ID [KEYID]
     gpg: Good signature from "[Name] <email@example.com>"
     ```
   - 鍵が信頼されていない場合、「This key is not certified with a trusted signature!」のような警告が表示されることがあります。`gpg --edit-key KEYID`を実行後、`trust`で信頼レベルを調整できます。

2. **インライン署名ファイルの検証**（署名がファイルに埋め込まれている、多くの場合バイナリ）：
   - 署名のみを確認する場合：
     ```
     gpg --verify signed-file
     ```
   - 検証し、元のコンテンツを抽出する場合：
     ```
     gpg --output original-file --decrypt signed-file
     ```
     暗号化されている場合はパスフレーズの入力を求めますが、署名のみの場合は検証だけ行います。

3. **クリア署名メッセージの検証**（人間が読めるテキストにASCIIアーマー署名が付いたもの。メールやREADMEで一般的）：
   ```
   gpg --verify clearsigned-file.txt
   ```
   出力はファイルを変更せずに署名ステータスを表示します。

#### トラブルシューティング
- **「公開鍵がありません」エラー**: 上記のように鍵をインポートしてください。
- **不正な署名**: ファイルが改ざんされている可能性があります—再ダウンロードしてください。
- **鍵の有効性**: `gpg --list-keys`で鍵の詳細を確認するか、フィンガープリントが公式ソースと一致することを確認してください。
- バッチ検証やスクリプトでの使用には、`--batch --exit-on-status-write-error`を追加してください。

署名の作成や高度なオプションの詳細については、公式マニュアルを参照してください。

[署名の作成と検証 - GnuPGマニュアル](https://www.gnupg.org/gph/en/manual/x135.html)