---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: カスタムホームディレクトリでのGPGの使用
translated: true
type: note
---

### GPGの`--homedir`オプションの使用方法

`--homedir`フラグ（注意: `--home-dir`ではなく`--homedir`です - GPGは単語を1つで使用します）は、GPGに設定ファイル、キーリング、信頼データベース、その他のデータを保存する「ホーム」としてカスタムディレクトリを使用するように指示します。デフォルトでは、GPGは`~/.gnupg`を使用します（例: WindowsのGit Bashでは`/c/Users/YourName/.gnupg`）。このオプションは以下の場合に便利です:
- 複数のGPGセットアップを分離する場合（例: 個人用キーと仕事用キー）
- システム全体のGPG設定との競合を避けてテストする場合
- ポータブルまたはカスタム環境でGPGを実行する場合

#### 基本構文
```
gpg --homedir /path/to/custom/dir [other gpg commands]
```
- `/path/to/custom/dir`を希望のディレクトリパスに置き換えてください
- WindowsのGit Bashでは、パスに**常にスラッシュ（`/`）を使用**してください（例: `/c/Users/YourName/my-gpg-dir`）
- ディレクトリは事前に存在している必要があります。GPGは自動的に作成しません。まず`mkdir -p /path/to/custom/dir`で作成してください

#### 例: カスタムホームディレクトリの設定と使用
1. **カスタムディレクトリを作成**（Git Bashで）:
   ```
   mkdir -p /c/Users/YourName/my-custom-gpg
   ```

2. **カスタムhomedirを使用して鍵ペアを生成**:
   ```
   gpg --homedir /c/Users/YourName/my-custom-gpg --full-generate-key
   ```
   - これにより鍵と設定がデフォルトではなく`my-custom-gpg`に保存されます

3. **そのディレクトリから鍵を一覧表示**:
   ```
   gpg --homedir /c/Users/YourName/my-custom-gpg --list-secret-keys --keyid-format LONG
   ```

4. **カスタムディレクトリの鍵を使用してファイルを暗号化**:
   ```
   gpg --homedir /c/Users/YourName/my-custom-gpg --encrypt --recipient RECIPIENT_EMAIL secret.txt
   ```

5. **ファイルを復号化**:
   ```
   gpg --homedir /c/Users/YourName/my-custom-gpg --output decrypted.txt --decrypt secret.txt.gpg
   ```

#### Git Bash on Windowsでのヒント
- **パス:** `/`を使用してください - `\`や混合スラッシュはコマンドを壊す可能性があるため避けてください
- **権限:** カスタムディレクトリに読み書き権限があることを確認してください（セキュリティのためにデフォルトの`.gnupg`と同様に`chmod 700 /path/to/custom/dir`を使用）
- **環境変数の代替:** 毎回`--homedir`を使用する代わりに、`.bashrc`に`export GNUPGHOME=/c/Users/YourName/my-custom-gpg`を設定してください（編集後は`source ~/.bashrc`を実行）。その後GPGは自動的にそれを使用します
- **Git連携:** Git署名に使用する場合は、フラグを設定してください:
  ```
  git config --global gpg.program "gpg --homedir /c/Users/YourName/my-custom-gpg"
  ```
- **一般的な問題:** GPGがファイルがないと文句を言う場合、初期化が必要な可能性があります - まず`gpg --homedir /path --gen-key`を実行してください。Windowsでは、引用符で囲わない限りスペースを含むパスは避けてください

詳細については、GPGマニュアルを参照してください: [GnuPG Documentation](https://www.gnupg.org/documentation/manuals/gnupg/)