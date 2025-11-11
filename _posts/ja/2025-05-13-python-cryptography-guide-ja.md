---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-code-fast-1
title: Python暗号化ガイド
translated: true
type: note
---

### Cryptographyパッケージの紹介
`cryptography`パッケージは、暗号プリミティブと安全なプロトコルのためのレシピを提供する人気のPythonライブラリです。AES、RSAなどの標準を実装し、使いやすさとセキュリティに焦点を当てています。SSHやTLSのような高レベルプロトコルを直接実装するためのものではなく、ビルディングブロックとして使用してください。セキュリティパッチのために常に最新版であることを確認してください。

### インストール
pipでインストール:
```bash
pip install cryptography
```
より良いパフォーマンス（特に大きな鍵や頻繁な操作の場合）のために、OpenSSLサポート付きでインストール:
```bash
pip install cryptography[openssl]
```
注意: 一部のシステムでは、OpenSSLヘッダーを別途インストールする必要があります（例: Ubuntuでは`apt install libssl-dev`）。

### 基本概念
- **プリミティブ**: 暗号化/復号のような低レベル操作
- **レシピ**: 高レベルで意見が含まれた関数（例: 対称暗号化のためのFernet）
- **ハザード警告**: ライブラリは安全でない使用法に対して警告を使用します—これらに注意してください

ライブラリをインポート:
```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes, asyncioc as a
from cryptography.hazmat.primitives.asymmetric import rsa, padding
```

### 例

#### 1. Fernetを使った対称暗号化（初心者向けの最も簡単な方法）
FernetはAES-128をCBCモードで使用し、HMACで完全性を保証します。暗号化データの保存に理想的です。

```python
from cryptography.fernet import Fernet

# 鍵を生成（環境変数などに安全に保存）
key = Fernet.generate_key()
cipher = Fernet(key)

# 暗号化
plaintext = b"This is a secret message."
token = cipher.encrypt(plaintext)
print("Encrypted:", token)

# 復号
decrypted = cipher.decrypt(token)
print("Decrypted:", decrypted)
```
- **注意**: 鍵はURL-safe base64（44文字）です。鍵をハードコードせず、定期的にローテーションしてください。

#### 2. RSAを使った非対称暗号化
公開鍵/秘密鍵のペアを生成し、秘密鍵保持者のみが復号できるデータを暗号化します。

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# 秘密鍵を生成
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# 保存用にシリアライズ
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()  # パスワード保護にはBestAvailableEncryption()を使用
)

# 公開鍵を取得してシリアライズ
public_key = private_key.public_key()
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# 公開鍵で暗号化
plaintext = b"Secret message"
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

# 秘密鍵で復号
decrypted = private_key.decrypt(
    ciphertext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
print("Decrypted:", decrypted)
```
- **注意**: RSAは大きなデータには遅いです。鍵交換や小さなメッセージに使用してください。OAEPパディングは攻撃を防ぎます。

#### 3. ハッシュの生成と使用
完全性チェックやパスワードハッシュ用です。

```python
from cryptography.hazmat.primitives import hashes

# データをハッシュ化
digest = hashes.Hash(hashes.SHA256())
digest.update(b"Some data")
hash_result = digest.finalize()
print("SHA256 Hash:", hash_result.hex())
```

パスワードには、鍵導出に`cryptography.hazmat.primitives.kdf.pbkdf2`を使用してください（例: PBKDF2で遅い、ソルト付きハッシュ）。

#### 4. RSAを使ったデジタル署名
真正性を証明するためにデータに署名します。

```python
# 前の例のRSA鍵を使用
message = b"Data to sign"
signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

# 公開鍵で検証
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("Signature valid")
except Exception:
    print("Signature invalid")
```

### ベストプラクティス
- **鍵管理**: 鍵は安全に保存（例: AWS KMS、ハードウェアセキュリティモジュールを使用）。鍵の再利用は避けてください。
- **パディングとモード**: 常に安全なパディングを使用（例: RSAにはOAEP、AESにはGCM）。
- **ランダム性**: シードには`os.urandom()`または`secrets`モジュールを使用。`random`は避けてください。
- **更新**: 暗号技術は進化します—使用法の脆弱性を確認してください。
- **独自実装の回避**: 複雑なニーズには、レシピを使用するか、`pyjwt`や`boto3`のような高レベルライブラリと統合してください。
- **テスト**: エラーハンドリングにはライブラリの定数と例外を使用してください。

### さらなる学習
- [公式ドキュメント](https://cryptography.io/en/latest/) – 詳細なAPIリファレンスとチュートリアル
- [PyPIページ](https://pypi.org/project/cryptography/) – バージョン履歴と統合情報
- 高度なトピックには、`cryptography` wikiやRFC（例: PKCS#1のRFC 8017）を探索してください

特定のユースケース（例: ファイルの暗号化やAPIセキュリティ）がある場合は、詳細を提供すると具体的な例を作成できます。