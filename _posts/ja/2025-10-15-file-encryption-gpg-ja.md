---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GPGによるファイルの暗号化
translated: true
type: note
---

### GPGキーを使用したファイルの暗号化

GPGキーの一覧には、メールアドレス `lzwjava@gmail.com` に関連付けられた公開鍵（pub）とフィンガープリント `982740390B5D33E90B6B6133892BC5A4789B71CD` が表示されています。このキーを使用してファイルを暗号化するには（あなただけが秘密鍵で復号できるように）、ターミナルで以下の手順に従ってください：

1. **暗号化したいファイルが含まれるディレクトリに移動**します（例：ファイルが `secret.txt` の場合）：
   ```
   cd ~/path/to/your/file
   ```

2. **`--encrypt` オプションを使用してファイルを暗号化**し、受信者（あなたのメールアドレスまたはキーID）を指定します。これにより暗号化された `.gpg` ファイルが作成されます。
   
   - メールアドレスを使用する場合（より簡単）：
     ```
     gpg --encrypt --recipient lzwjava@gmail.com secret.txt
     ```
   
   - キーID（完全なフィンガープリント）を使用する場合：
     ```
     gpg --encrypt --recipient 982740390B5D33E90B6B6133892BC5A4789B71CD secret.txt
     ```
   
   これにより `secret.txt.gpg` が出力されます。これは暗号化されたバージョンです。元の `secret.txt` は変更されません。

3. **暗号化を確認**します（オプション）：
   ```
   gpg --list-packets secret.txt.gpg
   ```
   これにより暗号化されたパケットの詳細が表示されます。

### ファイルの復号化（後で参照するため）

後で復号化するには（あなたの秘密鍵とパスフレーズでのみ可能）：
```
gpg --decrypt secret.txt.gpg > secret.txt.decrypted
```
プロンプトが表示されたらパスフレーズを入力してください。

### ヒント
- **対称暗号化**（受信者キーが不要で、パスフレーズのみ必要な場合）：代わりに `gpg -c secret.txt` を使用します。
- **暗号化と署名**（あなたからのものであることを証明するため）：暗号化コマンドに `--sign` を追加します。例：`gpg --encrypt --sign --recipient lzwjava@gmail.com secret.txt`。
- エラーが発生した場合（例：キーが信頼されていない）、`gpg --edit-key lzwjava@gmail.com` を実行し、`trust` を使用して信頼レベルを ultimate に設定します。
- キーの安全性のために、常に `~/.gnupg` ディレクトリをバックアップしてください。

詳細については、GPGマニュアルを参照してください：[GPG Documentation](https://www.gnupg.org/documentation/manpage.html)。