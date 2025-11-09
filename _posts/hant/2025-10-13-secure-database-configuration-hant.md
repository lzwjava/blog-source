---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 安全數據庫配置策略
translated: true
type: note
---

### 處理 Python 專案中的敏感資料庫配置

在 Python 專案中管理敏感資訊（如資料庫密碼和端口）是常見的挑戰。目標是避免將機密資訊提交到版本控制系統（例如 Git），同時保持部署流程的簡潔。下面我將比較你提到的兩種方法：(1) 使用模板 `config_example.ini` 配合 `.gitignore` 忽略實際文件，並在 UAT 等伺服器上手動設置；(2) 使用 GPG 加密將加密值儲存在 `config.ini` 中，並在運行時解密。這兩種方法如果正確實施都是安全的，但它們在簡便性和自動化之間有所取捨。

#### 方法 1：模板配置 + `.gitignore` + 手動伺服器設置
這是一種直接且低技術含量的方法。你為開發者和 CI/CD 流水線創建一個示例配置文件，在 Git 中忽略真實文件，並在類生產環境（例如 UAT 伺服器）上手動處理實際配置。

**實施步驟：**
1. 創建帶有佔位符的 `config_example.ini`：
   ```
   [database]
   host = localhost
   port = 5432  # 示例端口；替換為真實端口
   user = dbuser
   password = example_password  # 替換為真實密碼
   database = mydb
   ```

2. 將真實的 `config.ini` 添加到 `.gitignore`：
   ```
   config.ini
   ```

3. 在你的 Python 代碼中，從 `config.ini` 加載（如果文件缺失則回退到示例文件以供開發使用）：
   ```python
   import configparser
   import os

   config = configparser.ConfigParser()
   config_file = 'config.ini' if os.path.exists('config.ini') else 'config_example.ini'
   config.read(config_file)

   db_host = config['database']['host']
   db_port = config['database']['port']
   db_user = config['database']['user']
   db_password = config['database']['password']
   db_name = config['database']['database']
   ```

4. 對於 UAT 伺服器：在部署期間手動複製帶有真實值的 `config.ini`（例如通過 SCP 或 Ansible）。開發者可以將 `config_example.ini` 複製為 `config.ini` 並在本地填寫。

**優點：**
- 簡單 — 無需額外的函式庫或密鑰管理。
- 無運行時開銷（解密）。
- 對小型團隊來說容易；與手動部署配合良好。

**缺點：**
- 在每個伺服器上手動設置增加了錯誤風險（例如忘記更新密碼）。
- 不適合自動化 CI/CD；需要安全的密鑰注入（例如通過流水線中的環境變數）。
- 如果有人誤提交 `config.ini`，機密資訊將會暴露。

這種方法非常適合早期專案或當加密顯得過於複雜時使用。

#### 方法 2：對配置值使用 GPG 加密
這種方法使用 GPG 加密敏感字段（例如密碼），將加密後的數據塊儲存在 `config.ini` 中，並在代碼運行時解密。只要你的私鑰從未共享，加密後的文件可以安全地提交到 Git。

**實施步驟：**
1. 在你的系統上安裝 GPG（Linux/Mac 上標準配備；Windows 上使用 Gpg4win）。如果需要，生成密鑰對：
   ```
   gpg --gen-key  # 按照提示操作生成你的密鑰
   ```

2. 將敏感值（例如密碼）加密到文件中：
   ```
   echo "real_password_here" | gpg --encrypt --recipient your-email@example.com -o encrypted_password.gpg
   ```
   - 這會創建 `encrypted_password.gpg`。你可以對其進行 base64 編碼以便於儲存在 INI 文件中：
     ```bash
     base64 encrypted_password.gpg > encrypted_password.b64
     ```

3. 更新 `config.ini` 以包含加密（並經過 base64 編碼）的值。提交此文件 — 它是安全的：
   ```
   [database]
   host = localhost
   port = 5432
   user = dbuser
   password_encrypted = <base64-encoded-encrypted-blob-here>  # 來自 encrypted_password.b64
   database = mydb
   ```

4. 在你的 Python 代碼中，使用 `gnupg` 函式庫進行解密（開發環境通過 `pip install python-gnupg` 安裝，但假設它可用）：
   ```python
   import configparser
   import gnupg
   import base64
   import tempfile
   import os

   config = configparser.ConfigParser()
   config.read('config.ini')  # 可以安全提交此文件

   # 解密密碼
   gpg = gnupg.GPG()  # 假設 GPG 已安裝且密鑰可用
   encrypted_b64 = config['database']['password_encrypted']
   encrypted_data = base64.b64decode(encrypted_b64)

   with tempfile.NamedTemporaryFile(delete=False) as tmp:
       tmp.write(encrypted_data)
       tmp.flush()
       decrypted = gpg.decrypt_file(None, passphrase=None, extra_args=['--batch', '--yes'], output=tmp.name)
       if decrypted.ok:
           db_password = decrypted.data.decode('utf-8').strip()
       else:
           raise ValueError("解密失敗")

   os.unlink(tmp.name)  # 清理

   db_host = config['database']['host']
   db_port = config['database']['port']
   db_user = config['database']['user']
   db_name = config['database']['database']

   # 現在使用 db_password...
   ```

5. 對於 UAT 伺服器：按原樣部署 `config.ini`（通過 Git 或複製）。確保 GPG 私鑰已安全地放置在伺服器上（例如通過 Ansible vault 或手動安全複製）。代碼將在啟動時解密。

**優點：**
- 加密的配置可以進行版本控制 — 無需為機密資訊使用 `.gitignore`。
- 自動化部署；與 CI/CD 配合良好（只需安全同步密鑰）。
- 可審計：加密值的更改會被追蹤。

**缺點：**
- 需要 GPG 設置和密鑰管理（例如定期輪換密鑰；絕不提交私鑰）。
- 運行時依賴於 GPG 和 `python-gnupg`；如果密鑰缺失，解密會失敗。
- 對初學者來說稍微複雜；解密可能帶來輕微性能損耗（對密碼來說可忽略不計）。

這種方法適用於具有自動化部署的團隊或需要在環境間共享配置的情況。

#### 比較表格

| 方面               | 模板 + .gitignore + 手動 | GPG 加密 + 運行時解密 |
|--------------------|--------------------------|----------------------|
| **安全性**        | 如果手動步驟小心則高；存在人為錯誤風險。 | 高；機密資訊絕不以明文形式存在。 |
| **設置簡易度**    | 非常容易（無需工具）。     | 中等（需要 GPG + 函式庫）。 |
| **版本控制**      | 提交模板；忽略真實文件。    | 提交完整配置（加密）。 |
| **部署**          | 每個伺服器手動操作（例如 SCP）。 | 自動化（需要密鑰同步）。 |
| **開銷**          | 無。                     | 輕微（加載時解密）。 |
| **最適合**        | 小型/手動專案。           | 自動化/CI/CD 流水線。 |

#### 建議
- 如果你的專案簡單或團隊規模小，從**方法 1**開始 — 它經過實踐檢驗。
- 為了擴展規模，轉向**方法 2**（或演進為使用環境變數/密鑰管理器，如 AWS SSM/HashiCorp Vault）。
- 始終結合環境變數進行覆蓋（例如 `os.getenv('DB_PASSWORD', db_password)`）。
- 在 UAT 之前，在預備環境中測試解密功能。

如果你分享更多細節（例如你的部署工具或完整配置），我可以進一步完善代碼！