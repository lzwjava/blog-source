---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 使用 Python Secrets 實現安全隨機生成
translated: true
type: note
---

### `secrets` 模組簡介
`secrets` 模組（於 Python 3.6 引入）是標準函式庫的一部分，提供加密強度隨機數生成的存取功能。與適用於模擬或遊戲的 `random` 模組不同，`secrets` 專為安全相關任務設計，例如生成密碼、令牌或密鑰，因為它使用作業系統的加密安全隨機數生成器（例如，在類 Unix 系統上使用 `/dev/urandom`）。

使用時只需導入：
```python
import secrets
```

### 主要功能與用法
以下是 `secrets` 中的主要功能，附有簡要說明和範例。這些功能生成的隨機值難以預測。

| 函數 | 用途 | 使用範例 |
|----------|---------|---------------|
| `secrets.token_bytes(n)` | 生成 `n` 個隨機位元組。適用於創建二進制密鑰。 | `key = secrets.token_bytes(16)`  # 16 個隨機位元組 |
| `secrets.token_hex(n)` | 生成 `n` 個隨機位元組，並以十六進制字串形式返回（由於十六進制編碼，長度為 `n` 的兩倍）。適用於十六進制令牌。 | `hex_key = secrets.token_hex(16)`  # 32 字元十六進制字串 |
| `secrets.token_urlsafe(n)` | 生成 `n` 個隨機位元組，並進行 base64 編碼，適用於 URL 安全用途（例如在網路令牌中）。 | `url_token = secrets.token_urlsafe(32)`  # 約 43 字元字串 |
| `secrets.randbelow(n)` | 返回一個介於 0 和 `n-1`（含）之間的隨機整數。是 `random.randint` 的安全替代方案。 | `num = secrets.randbelow(100)`  # 0 到 99 的隨機整數 |
| `secrets.choice(seq)` | 從非空序列 `seq` 中返回一個隨機元素。是 `random.choice` 的安全替代方案。 | `item = secrets.choice(['a', 'b', 'c'])`  # 從列表中隨機選擇 |

### 實際範例
1. **生成安全密碼**：
   結合 `secrets.choice` 與字串常數來生成隨機密碼。
   ```python
   import string
   import secrets

   alphabet = string.ascii_letters + string.digits + string.punctuation
   password = ''.join(secrets.choice(alphabet) for _ in range(12))
   print(password)  # 例如："X8f#9L&pW2c%"
   ```

2. **創建 API 令牌**：
   使用 `token_urlsafe` 生成網路安全的隨機字串。
   ```python
   token = secrets.token_urlsafe(32)
   print(token)  # 例如："e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
   ```

3. **遊戲或模擬中的隨機選擇（具安全性）**：
   ```python
   winners = secrets.choice(['Alice', 'Bob', 'Charlie'])
   print(f"Winner: {winners}")
   ```

### 最佳實踐與注意事項
- **安全原理**：`secrets` 避免可預測性，使其能夠抵抗攻擊。切勿使用 `random` 生成密碼或令牌，因為它可以被設定種子並預測。
- **效能**：呼叫可能比 `random` 慢，但對於安全關鍵程式碼來說是可以接受的——請勿在非關鍵任務的迴圈中過度使用。
- **邊界情況**：`secrets.choice` 對於空序列會引發 `ValueError`；`randbelow(0)` 會引發 `ValueError`。
- **依賴關係**：無需外部函式庫；它是內建的。
- 更多詳細資訊，請查閱 [官方 Python 文檔](https://docs.python.org/3/library/secrets.html)。如果您有特定使用案例，請提供更多上下文以獲得量身定制的建議！