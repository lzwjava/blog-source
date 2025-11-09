---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: GPG秘密鍵のエクスポート
translated: true
type: note
---

### サーバーからのGPG秘密鍵のエクスポート

秘密鍵をエクスポートするには、SSHまたはターミナル経由でサーバーにアクセスする必要があります。GPG秘密鍵は機密性が高いため、安全に取り扱い、転送後はエクスポートしたファイルを削除してください。

1. **秘密鍵の一覧表示**（メールアドレスまたは鍵IDで鍵を特定するため）:  
   ```
   gpg --list-secret-keys
   ```  
   `sec   rsa4096/ABC123DEF456 2023-01-01 [SC]` のようなエントリを探します。メールアドレスまたは鍵ID（例: `user@example.com` または `ABC123DEF456`）を控えておきます。

2. **秘密鍵のエクスポート**（ASCII形式でエクスポートするには `--armor` を使用。転送が容易になります）:  
   ```
   gpg --export-secret-keys --armor user@example.com > private-key.asc
   ```  
   - `user@example.com` は実際のメールアドレスまたは鍵IDに置き換えてください。  
   - これにより、カレントディレクトリに `private-key.asc` が作成されます。  
   - 複数の鍵がある場合は、鍵IDを指定して正確に行います: `gpg --export-secret-keys --armor ABC123DEF456 > private-key.asc`。  
   - **セキュリティ注意**: これはパスフレーズなしで鍵をエクスポートします。インポート時にプロンプトが表示された場合は、元のパスフレーズを入力する必要があります。

3. **ファイルをローカルのラップトップに安全に転送**:  
   - `scp` を使用する場合（ローカルマシンから実行）:  
     ```
     scp user@server-ip:/path/to/private-key.asc ./
     ```  
     `user@server-ip` はサーバーの詳細に、`/path/to/` は実際のパスに置き換えてください。  
   - 代替手段: 大きなファイルの場合は `rsync`、GUIオプションとしてはSFTP。メールや安全でないチャネルは避けてください。

4. **サーバー上のクリーンアップ**:  
   ```
   rm private-key.asc
   ```  
   `ls` で削除されたことを確認してください。

### ローカルのラップトップへのGPG秘密鍵のインポート

GPGがインストールされていることを前提とします（例: Linuxでは `apt install gnupg`、macOSでは `brew install gnupg`、WindowsではChocolatey）。

1. **鍵のインポート**:  
   ```
   gpg --import private-key.asc
   ```  
   - "gpg: key ABC123DEF456: secret key imported" のような出力が表示されます。  
   - インポート中にパスフレーズの入力を求められた場合は、元のパスフレーズを入力してください。

2. **インポートの確認**:  
   ```
   gpg --list-secret-keys
   ```  
   あなたの鍵が "sec" の下に表示されるはずです。

3. **オプション: 信頼レベルを設定**（署名/メール用に使用する場合）:  
   ```
   gpg --edit-key user@example.com
   ```  
   - プロンプトで、`trust` と入力し、「ultimate」（オプション5）を選択し、`save`、`quit` の順に入力します。  
   - これにより、ローカルマシン上で鍵が完全に信頼されたものとしてマークされます。

### ヒントと警告
- **パスフレーズ**: 常に強力なパスフレーズを使用してください。忘れると鍵は使用不能になります。
- **サブキー**: 鍵にサブキー（例: 暗号化用）がある場合は、`--export-secret-subkeys` を使用してそれらもエクスポートしてください。
- **バックアップ**: エクスポートした鍵は安全な保管庫（例: 暗号化ドライブ）に保管してください。
- **バージョン**: GPG 2.x でテスト済み。1.x でも同様に動作します。
- 詳細については、公式GPGドキュメントを参照してください: [GnuPG マニュアル](https://www.gnupg.org/documentation/manuals/gnupg/)。