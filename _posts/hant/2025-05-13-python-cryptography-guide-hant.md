---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: Python 密碼學指南
translated: true
type: note
---

### 密碼學套件簡介
`cryptography` 套件是一個流行的 Python 函式庫，提供密碼學基礎元件與安全協定的實用方法。它專注於易用性與安全性，實作了 AES、RSA 等標準。它並非直接用於實作高階協定（如 SSH 或 TLS），而是作為基礎構件使用。請務必確認已更新至最新版本以獲得安全修補程式。

### 安裝
透過 pip 安裝：
```bash
pip install cryptography
```
如需更佳效能（特別針對大型金鑰或頻繁操作），可安裝帶有 OpenSSL 支援的版本：
```bash
pip install cryptography[openssl]
```
注意：在某些系統上，可能需要單獨安裝 OpenSSL 標頭檔（例如在 Ubuntu 上使用 `apt install libssl-dev`）。

### 基本概念
- **基礎元件**：低階操作，如加密/解密。
- **實用方法**：高階、預設設定的函式（例如用於對稱加密的 Fernet）。
- **風險警告**：此函式庫會對不安全使用發出警告——請務必注意這些警告。

匯入函式庫：
```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes, asyncioc as a
from cryptography.hazmat.primitives.asymmetric import rsa, padding
```

### 範例

#### 1. 使用 Fernet 進行對稱加密（最適合初學者）
Fernet 使用 AES-128 CBC 模式與 HMAC 確保完整性，非常適合儲存加密資料。

```python
from cryptography.fernet import Fernet

# 產生金鑰（請安全儲存，例如在環境變數中）
key = Fernet.generate_key()
cipher = Fernet(key)

# 加密
plaintext = b"這是秘密訊息。"
token = cipher.encrypt(plaintext)
print("已加密：", token)

# 解密
decrypted = cipher.decrypt(token)
print("已解密：", decrypted)
```
- **注意事項**：金鑰為 URL 安全的 base64 編碼（44 字元）。切勿硬編碼金鑰，應定期輪換。

#### 2. 使用 RSA 進行非對稱加密
產生公鑰/私鑰對，並加密只有私鑰持有者能解密的資料。

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding

# 產生私鑰
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# 序列化以供儲存
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()  # 如需密碼保護，請使用 BestAvailableEncryption()
)

# 取得公鑰並序列化
public_key = private_key.public_key()
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# 使用公鑰加密
plaintext = b"秘密訊息"
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)

# 使用私鑰解密
decrypted = private_key.decrypt(
    ciphertext,
    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
)
print("已解密：", decrypted)
```
- **注意事項**：RSA 對大型資料處理較慢，請用於金鑰交換或小型訊息。OAEP 填充可防止攻擊。

#### 3. 產生與使用雜湊值
用於完整性檢查或密碼雜湊。

```python
from cryptography.hazmat.primitives import hashes

# 雜湊資料
digest = hashes.Hash(hashes.SHA256())
digest.update(b"某些資料")
hash_result = digest.finalize()
print("SHA256 雜湊值：", hash_result.hex())
```

對於密碼，請使用 `cryptography.hazmat.primitives.kdf.pbkdf2` 進行金鑰派生（例如使用 PBKDF2 進行慢速、加鹽的雜湊）。

#### 4. 使用 RSA 進行數位簽章
對資料簽章以證明真實性。

```python
# 使用先前產生的 RSA 金鑰
message = b"待簽署資料"
signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

# 使用公鑰驗證
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("簽章有效")
except Exception:
    print("簽章無效")
```

### 最佳實踐
- **金鑰管理**：安全儲存金鑰（例如使用 AWS KMS、硬體安全模組）。切勿重複使用金鑰。
- **填充與模式**：始終使用安全填充（例如 RSA 使用 OAEP，AES 使用 GCM）。
- **隨機性**：使用 `os.urandom()` 或 `secrets` 模組產生種子；避免使用 `random`。
- **更新**：密碼學技術不斷演進——請檢查使用方式是否存在漏洞。
- **避免自製方案**：對於複雜需求，請使用預設方法或整合高階函式庫如 `pyjwt` 或 `boto3`。
- **測試**：使用函式庫的常數與例外進行錯誤處理。

### 延伸閱讀
- [官方文件](https://cryptography.io/en/latest/) – 詳細 API 參考與教學。
- [PyPI 頁面](https://pypi.org/project/cryptography/) – 版本歷史與整合資訊。
- 對於進階主題，可探索 `cryptography` wiki 或 RFC（例如 RFC 8017 關於 PKCS#1）。

如果您有特定使用情境（例如加密檔案或 API 安全），請提供更多細節以獲取量身訂製的範例。