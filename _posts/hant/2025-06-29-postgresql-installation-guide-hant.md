---
audio: false
generated: true
lang: hant
layout: post
title: 安裝 PostgreSQL 以修復 psycopg2
translated: true
type: note
---

您遇到的錯誤表明 `psycopg2` 套件需要 PostgreSQL 的 `pg_config` 可執行檔才能從原始碼建構，但在您的系統中找不到。這表示您需要在 macOS 系統上安裝 PostgreSQL 以提供必要的依賴項。以下是在 macOS 上安裝 PostgreSQL 並解決問題的步驟。

### 在 macOS 上安裝 PostgreSQL 的步驟

#### 1. **使用 Homebrew 安裝 PostgreSQL（推薦）**
Homebrew 是在 macOS 上安裝和管理 PostgreSQL 最簡單的方法。

1. **安裝 Homebrew（如果尚未安裝）**：
   - 開啟 Terminal 並執行：
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - 按照螢幕上的指示完成 Homebrew 安裝。

2. **安裝 PostgreSQL**：
   - 在 Terminal 中執行：
     ```bash
     brew install postgresql
     ```
   - 此命令將安裝 PostgreSQL 及其依賴項，包括 `psycopg2` 所需的 `pg_config` 可執行檔。

3. **啟動 PostgreSQL**：
   - 要啟動 PostgreSQL 服務，請執行：
     ```bash
     brew services start postgresql
     ```
   - 或者，要為單次工作階段手動啟動：
     ```bash
     pg_ctl -D /opt/homebrew/var/postgres start
     ```

4. **驗證安裝**：
   - 檢查 PostgreSQL 是否已安裝並正在執行：
     ```bash
     psql --version
     ```
   - 您應該會看到 PostgreSQL 版本（例如 `psql (PostgreSQL) 17.0`）。
   - 您也可以登入 PostgreSQL shell 來確認：
     ```bash
     psql -U $(whoami)
     ```

#### 2. **安裝 PostgreSQL 後安裝 `psycopg2`**
安裝 PostgreSQL 後，請重試安裝 `psycopg2`。`pg_config` 可執行檔現在應該可以在您的 PATH 中找到。

1. **安裝 `psycopg2`**：
   - 執行：
     ```bash
     pip install psycopg2
     ```
   - 如果您使用 requirements 檔案，請執行：
     ```bash
     pip install -r scripts/requirements/requirements.local.txt
     ```

2. **替代方案：安裝 `psycopg2-binary`（更簡單的選項）**：
   - 如果您想避免從原始碼建構 `psycopg2`（這需要 PostgreSQL 依賴項），您可以安裝預編譯的 `psycopg2-binary` 套件：
     ```bash
     pip install psycopg2-binary
     ```
   - 注意：由於潛在的相容性問題，`psycopg2-binary` 不建議用於生產環境，但對於開發或測試來說是可以的。

#### 3. **可選：將 `pg_config` 新增至 PATH（如果需要）**
如果安裝 PostgreSQL 後仍然找不到 `pg_config` 可執行檔，您可能需要手動將其新增至 PATH。

1. 找到 `pg_config`：
   - Homebrew 通常將 PostgreSQL 安裝在 `/opt/homebrew/bin`（適用於 Apple Silicon）或 `/usr/local/bin`（適用於 Intel Mac）。
   - 驗證位置：
     ```bash
     find /opt/homebrew -name pg_config
     ```
     或
     ```bash
     find /usr/local -name pg_config
     ```

2. 新增至 PATH：
   - 如果找到 `pg_config`（例如在 `/opt/homebrew/bin` 中），請透過編輯您的 shell 設定檔（例如 `~/.zshrc` 或 `~/.bash_profile`）將其新增至 PATH：
     ```bash
     echo 'export PATH="/opt/homebrew/bin:$PATH"' >> ~/.zshrc
     ```
   - 套用變更：
     ```bash
     source ~/.zshrc
     ```

3. 驗證 `pg_config`：
   - 執行：
     ```bash
     pg_config --version
     ```
   - 如果它返回一個版本，則 PATH 設定正確。

#### 4. **疑難排解**
- **錯誤持續存在**：如果 `pip install psycopg2` 仍然失敗，請確保您擁有必要的建構工具：
  - 安裝 Xcode Command Line Tools：
    ```bash
    xcode-select --install
    ```
  - 如果需要，請明確安裝 `libpq`（PostgreSQL 客戶端函式庫）：
    ```bash
    brew install libpq
    ```

- **Python 版本相容性**：確保您的 Python 版本（在您的情況下是 3.13）與 `psycopg2` 相容。如果問題持續存在，請考慮使用稍舊 Python 版本（例如 3.11 或 3.12）的虛擬環境：
  ```bash
  python3.11 -m venv venv
  source venv/bin/activate
  pip install psycopg2
  ```

- **檢查 Homebrew**：確保 Homebrew 是最新的：
  ```bash
  brew update
  brew upgrade
  ```

#### 5. **替代安裝方法（可選）**
如果您不想使用 Homebrew，可以透過以下方式安裝 PostgreSQL：
- **Postgres.app**：
  - 從 [postgresapp.com](https://postgresapp.com/) 下載。
  - 按照設定指示安裝並啟動 PostgreSQL。
  - 如上所述，將 `bin` 目錄（例如 `/Applications/Postgres.app/Contents/Versions/latest/bin`）新增至您的 PATH。
- **官方 PostgreSQL 安裝程式**：
  - 從 [postgresql.org](https://www.postgresql.org/download/macosx/) 下載 macOS 安裝程式。
  - 按照安裝精靈的指示操作。

#### 6. **重試您的專案**
安裝 PostgreSQL 和 `psycopg2`（或 `psycopg2-binary`）後，請重試執行您的專案或重新安裝 requirements：
```bash
pip install -r scripts/requirements/requirements.local.txt
```

### 補充說明
- **錯誤發生的原因**：`psycopg2` 套件需要 PostgreSQL 開發函式庫（特別是 `libpq`）才能從原始碼建構。透過 Homebrew 安裝 PostgreSQL 會提供這些函式庫。
- **生產環境考量**：對於生產環境，請使用 `psycopg2`（而非 `psycopg2-binary`），並確保您的 PostgreSQL 版本與目標環境相符。
- **文件**：更多詳細資訊，請參閱 `psycopg2` 安裝指南：[psycopg.org/docs/install.html](https://www.psycopg.org/docs/install.html)。

如果您遇到其他問題，請分享具體的錯誤訊息，我可以協助進一步疑難排解！