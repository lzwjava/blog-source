---
audio: false
generated: true
lang: ja
layout: post
title: GPGの理解：安全な通信ツール
translated: true
type: note
---

## GPGとは
GPG（GNU Privacy Guard）は、OpenPGP標準（Pretty Good Privacy）のオープンソース実装です。安全な通信のためのツールであり、暗号化、復号、デジタル署名、鍵管理を提供します。GPGは電子メール、ファイル、その他のデータの保護に広く使用され、機密性、完全性、真正性を保証します。

GPGはLinux、macOS、Windowsなど、ほとんどのオペレーティングシステムで利用可能です。コマンドラインベースですが、GUIツールやThunderbirdのようなメールクライアントと統合することができます。

---

## GPGの仕組み
GPGは、データを保護するために**対称鍵暗号**と**公開鍵暗号**を組み合わせて使用します：

1. **対称鍵暗号**：
   - 暗号化と復号の両方に単一の鍵を使用します。
   - GPGは、大きなデータセットに対して高速であるため、実際のデータの暗号化に対称鍵アルゴリズム（例：AES）を使用します。
   - 各暗号化操作に対してランダムなセッション鍵が生成されます。

2. **公開鍵暗号**：
   - 暗号化用の**公開鍵**と復号用の**秘密鍵**のペアを使用します。
   - GPGはRSAやECDSAなどのアルゴリズムを鍵ペアでサポートします。
   - 公開鍵はセッション鍵を暗号化し、その後そのセッション鍵を使用してデータを暗号化します。受信者は自身の秘密鍵を使用してセッション鍵を復号し、その後そのセッション鍵を使用してデータを復号します。

3. **デジタル署名**：
   - GPGはユーザーが自身の秘密鍵を使用してデータに署名し、真正性と完全性を証明することを可能にします。
   - 受信者は送信者の公開鍵を使用して署名を検証します。

4. **鍵管理**：
   - GPGは鍵を鍵束（キーリング）で管理し、公開鍵と秘密鍵を保存します。
   - 鍵は生成、インポート、エクスポート、鍵サーバーへの公開が可能です。

### GPG暗号化プロセス
ファイルやメッセージを暗号化する場合：
1. GPGは対称暗号化用のランダムな**セッション鍵**を生成します。
2. データは対称アルゴリズム（例：AES-256）を使用してセッション鍵で暗号化されます。
3. セッション鍵は非対称アルゴリズム（例：RSA）を使用して受信者の**公開鍵**で暗号化されます。
4. 暗号化されたセッション鍵と暗号化されたデータは、単一の出力ファイルまたはメッセージに結合されます。

復号する場合：
1. 受信者は自身の**秘密鍵**を使用してセッション鍵を復号します。
2. セッション鍵は対称アルゴリズムを使用してデータを復号するために使用されます。

このハイブリッドアプローチは、対称暗号化の速さと非対称暗号化のセキュリティを組み合わせています。

---

## GPGのインストール
GPGは多くのLinuxディストリビューションにプリインストールされています。他のシステムの場合：
- **Linux**: パッケージマネージャー経由でインストール：
  ```bash
  sudo apt install gnupg  # Debian/Ubuntu
  sudo yum install gnupg  # CentOS/RHEL
  ```
- **macOS**: Homebrew経由でインストール：
  ```bash
  brew install gnupg
  ```
- **Windows**: [gpg4win.org](https://gpg4win.org/)からGpg4winをダウンロード。

インストールの確認：
```bash
gpg --version
```

---

## GPG鍵の生成
GPGを使用するには、鍵ペア（公開鍵と秘密鍵）が必要です。

### ステップバイステップの鍵生成
以下のコマンドを実行して鍵ペアを生成します：
```bash
gpg --full-generate-key
```

1. **鍵タイプの選択**：
   - デフォルトはRSAおよびRSA（オプション1）です。
   - RSAは広く使用されており、ほとんどの目的で安全です。

2. **鍵サイズ**：
   - 推奨：2048または4096ビット（4096はより安全ですが遅いです）。
   - 例：4096を選択。

3. **鍵の有効期限**：
   - 有効期限を選択（例：1年）、または有効期限なしの場合は0を選択。
   - 有効期限付き鍵は鍵の寿命を制限することでセキュリティを強化します。

4. **ユーザーID**：
   - 名前、メールアドレス、オプションのコメントを入力。
   - 例：`John Doe <john.doe@example.com>`。

5. **パスフレーズ**：
   - 秘密鍵を保護するための強力なパスフレーズを設定。
   - このパスフレーズは復号と署名に必要です。

コマンド実行後の出力例：
```
gpg: key 0x1234567890ABCDEF marked as ultimately trusted
gpg: generated key pair
```

### 鍵のエクスポート
- **公開鍵のエクスポート**：
  ```bash
  gpg --armor --output public-key.asc --export john.doe@example.com
  ```
  これにより、ASCII形式の公開鍵を含むファイル（`public-key.asc`）が作成されます。

- **秘密鍵のエクスポート**（注意：安全に保管してください）：
  ```bash
  gpg --armor --output private-key.asc --export-secret-keys john.doe@example.com
  ```

---

## ファイルの暗号化と復号
### ファイルの暗号化
受信者のためにファイルを暗号化するには：
1. 受信者の公開鍵が鍵束にあることを確認：
   ```bash
   gpg --import recipient-public-key.asc
   ```
2. ファイルを暗号化：
   ```bash
   gpg --encrypt --recipient john.doe@example.com --output encrypted-file.gpg input-file.txt
   ```
   - `--recipient`: 受信者のメールアドレスまたは鍵IDを指定。
   - `--output`: 出力ファイルを指定。
   - 結果は`encrypted-file.gpg`で、受信者のみが復号できます。

### ファイルの復号
自分宛に暗号化されたファイルを復号するには：
```bash
gpg --decrypt --output decrypted-file.txt encrypted-file.gpg
```
- プロンプトが表示されたらパスフレーズを入力。
- 復号された内容は`decrypted-file.txt`に保存されます。

---

## データの署名と検証
### ファイルの署名
署名はデータの真正性と完全性を証明します。
- **クリア署名**（人間が読める署名を含む）：
  ```bash
  gpg --clearsign input-file.txt
  ```
  出力：ファイル内容と署名を含む`input-file.txt.asc`。

- **分離署名**（署名ファイルが別）：
  ```bash
  gpg --detach-sign input-file.txt
  ```
  出力：`input-file.txt.sig`。

### 署名の検証
署名されたファイルを検証するには：
```bash
gpg --verify input-file.txt.asc
```
分離署名の場合：
```bash
gpg --verify input-file.txt.sig input-file.txt
```
署名者の公開鍵が鍵束にある必要があります。

---

## GPGによるパスワード生成
GPGはランダムデータを生成でき、安全なパスワードの作成に使用できます。GPGは主にパスワードジェネレーターではありませんが、その乱数生成は暗号的に安全です。

### パスワード生成コマンド
```bash
gpg --gen-random --armor 1 32
```
- `--gen-random`: ランダムバイトを生成。
- `--armor`: ASCII形式で出力。
- `1`: 品質レベル（1は暗号目的に適しています）。
- `32`: バイト数（希望するパスワード長に調整）。

出力例：
```
4eX9j2kPqW8mZ3rT5vY7nL9xF2bC6dA8
```
これをよりパスワードらしくするには、base64やhexコンバーターにパイプするか、希望の長さにトリミングします。

### 例：20文字のパスワードを生成
```bash
gpg --gen-random --armor 1 15 | head -c 20
```
これにより、20文字のランダム文字列が生成されます。

---

## 鍵管理
### 鍵の一覧表示
- 公開鍵の一覧：
  ```bash
  gpg --list-keys
  ```
- 秘密鍵の一覧：
  ```bash
  gpg --list-secret-keys
  ```

### 公開鍵の公開
鍵サーバー経由で公開鍵を共有：
```bash
gpg --keyserver hkps://keys.openpgp.org --send-keys 0x1234567890ABCDEF
```
`0x1234567890ABCDEF`を自分の鍵IDに置き換えてください。

### 鍵のインポート
ファイルから公開鍵をインポート：
```bash
gpg --import public-key.asc
```
または鍵サーバーから：
```bash
gpg --keyserver hkps://keys.openpgp.org --recv-keys 0x1234567890ABCDEF
```

### 鍵の失効
鍵が侵害されたり、期限切れになった場合：
1. 失効証明書を生成（鍵作成時に実行推奨）：
   ```bash
   gpg --output revoke.asc --gen-revoke john.doe@example.com
   ```
2. 失効証明書をインポートして公開：
   ```bash
   gpg --import revoke.asc
   gpg --keyserver hkps://keys.openpgp.org --send-keys john.doe@example.com
   ```

---

## ベストプラクティス
1. **鍵のバックアップ**：
   - 秘密鍵と失効証明書は安全に保管（例：暗号化USBドライブ）。
   - 秘密鍵は絶対に共有しない。

2. **強力なパスフレーズの使用**：
   - 秘密鍵には長くユニークなパスフレーズを使用。

3. **定期的な鍵の更新**：
   - 有効期限を設定し、定期的に鍵をローテーション。

4. **鍵フィンガープリントの検証**：
   - 公開鍵を信頼する前に、所有者とそのフィンガープリントを検証：
     ```bash
     gpg --fingerprint john.doe@example.com
     ```

5. **鍵サーバーの安全な使用**：
   - `hkps://keys.openpgp.org`のような信頼できる鍵サーバーを使用。

6. **信頼できる鍵のみに署名**：
   - 他人の鍵に署名する場合は、直接または信頼できるチャネルを通じて本人確認を実施。

---

## 一般的なGPGコマンドまとめ
一般的なGPGコマンドのクイックリファレンス：
- 鍵ペアの生成: `gpg --full-generate-key`
- ファイルの暗号化: `gpg --encrypt --recipient <email> --output <output.gpg> <input.txt>`
- ファイルの復号: `gpg --decrypt --output <output.txt> <input.gpg>`
- ファイルの署名: `gpg --clearsign <input.txt>` または `gpg --detach-sign <input.txt>`
- 署名の検証: `gpg --verify <file.asc>` または `gpg --verify <file.sig> <file>`
- 公開鍵のエクスポート: `gpg --armor --output public-key.asc --export <email>`
- 鍵のインポート: `gpg --import <key.asc>`
- ランダムパスワード生成: `gpg --gen-random --armor 1 <bytes>`

---

## トラブルシューティング
- **"No secret key" エラー**: 秘密鍵が鍵束にあるか確認（`gpg --list-secret-keys`）、かつ受信者の公開鍵と一致しているか確認。
- **パスフレーズ忘れ**: パスフレーズを失った場合、鍵を失効させて新しい鍵を生成する必要があります。
- **鍵が見つからない**: 受信者の公開鍵をインポートするか、鍵サーバーを確認。
- **GPGバージョン問題**: すべての関係者が互換性のあるGPGバージョンを使用しているか確認（`gpg --version`で確認）。

---

## 高度な機能
1. **メール連携**：
   - プラグイン（例：Enigmailまたは組み込みのOpenPGP）を介してThunderbirdなどのメールクライアントでGPGを使用。