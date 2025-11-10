---
audio: false
generated: true
lang: hant
layout: post
title: 缺少 libpq-fe.h 導致 psycopg2 安裝失敗
translated: true
type: note
---

當嘗試安裝 Python 套件 `psycopg2` 時，您遇到了一個錯誤，提示無法成功建置 wheel。錯誤訊息的關鍵部分是：

```
In file included from psycopg/adapter_asis.c:28:
./psycopg/psycopg.h:36:10: fatal error: libpq-fe.h: No such file or directory
   36 | #include <libpq-fe.h>
      |          ^~~~~~~~~~~~
compilation terminated.
```

這個錯誤是因為系統中缺少了 PostgreSQL 客戶端函式庫的標頭檔案 `libpq-fe.h`。`psycopg2` 套件需要此檔案才能從原始碼建置，因為它提供了 Python 連接到 PostgreSQL 資料庫的介面。下面，我將解釋為什麼會發生這種情況，並提供逐步解決方案來修復它。

---

### 為什麼會發生這個錯誤
`psycopg2` 套件是 Python 的 PostgreSQL 適配器，當您使用 `pip` 安裝它時，它會嘗試編譯其 C 擴充功能。這些擴充功能依賴於 PostgreSQL 客戶端函式庫，特別是開發標頭檔案，例如 `libpq-fe.h`。錯誤訊息確認了這一點：

```
It appears you are missing some prerequisite to build the package from source.
```

您的系統（根據使用 `x86_64-linux-gnu-gcc` 判斷，似乎是基於 Debian 的 Linux 發行版）缺少必要的 PostgreSQL 開發檔案。沒有這些檔案，編譯就會失敗，導致無法為 `psycopg2` 建置 wheel。

錯誤還建議了兩個選項：
1. 透過 PyPI 安裝預先建置的二進位套件 `psycopg2-binary`。
2. 安裝缺少的先決條件並從原始碼建置 `psycopg2`。

由於您的專案在需求文件中指定了 `psycopg2`（而不是 `psycopg2-binary`），並且為了相容性或自訂性，可能需要從原始碼建置，因此我們將專注於修復建置過程。不過，我也會在後面提到二進位套件的選項以保持完整性。

---

### 如何修復錯誤
為了解決這個問題，您需要安裝 PostgreSQL 客戶端開發套件，該套件提供了 `libpq-fe.h` 和其他必要的檔案。以下是操作方法：

#### 步驟 1：識別您的系統
您的建置輸出中包含 `x86_64-linux-gnu-gcc`，表示您可能正在使用基於 Debian 的系統，例如 Ubuntu。解決方案將針對此系統進行調整，但我會在其他發行版的備註中提供替代方案。

#### 步驟 2：安裝 PostgreSQL 開發套件
在基於 Debian 的系統（例如 Ubuntu）上，套件 `libpq-dev` 包含了 PostgreSQL 客戶端函式庫的標頭檔案，包括 `libpq-fe.h`。使用以下指令安裝它：

```bash
sudo apt-get update
sudo apt-get install libpq-dev
```

- **`sudo apt-get update`**：確保您的套件列表是最新的。
- **`sudo apt-get install libpq-dev`**：安裝 PostgreSQL 客戶端函式庫的開發檔案。

此套件會將 `libpq-fe.h` 放置在標準位置（通常是 `/usr/include/postgresql`），建置過程會搜尋該位置（如您的包含路徑所示：`-I/usr/include/post每月

#### 步驟 3：重試安裝
安裝 `libpq-dev` 後，重試安裝您的需求：

```bash
pip install -r scripts/requirements/requirements.local.txt
```

現在這應該會成功，因為缺少的 `libpq-fe.h` 檔案將可用，允許 `psycopg2` 建置其 wheel。

---

### 驗證修復
如果安裝仍然失敗，請檢查 PostgreSQL 標頭檔案是否正確安裝：
- 執行 `pg_config --includedir` 以查看標頭檔案的位置（例如 `/usr/include/postgresql`）。
- 確保這與建置指令中的包含路徑（`-I/usr/include/postgresql`）匹配。

您的建置輸出顯示 `-DPG_VERSION_NUM=140018`，表示它針對的是 PostgreSQL 14。`libpq-dev` 套件是版本無關的，應該與 PostgreSQL 14 標頭檔案相容。

---

### 替代方案：使用二進位套件
如果您不需要從原始碼建置 `psycopg2`（例如，為了特定的優化或相容性），您可以改為安裝預先建置的 `psycopg2-binary`：

```bash
pip install psycopg2-binary
```

要在您的專案中使用此套件，請將 `scripts/requirements/requirements.local.txt` 中的 `psycopg2` 替換為 `psycopg2-binary`。但是請注意，`psycopg2-binary` 可能有一些限制（例如，可能與某些 PostgreSQL 版本存在相容性問題），因此如果您的專案需要，從原始碼建置是首選。

---

### 對於其他發行版
如果您不在基於 Debian 的系統上，請安裝等效的套件：
- **Red Hat/CentOS/Fedora**：`sudo yum install postgresql-devel` 或 `sudo dnf install postgresql-devel`
- **Arch Linux**：`sudo pacman -S postgresql-libs`
- **macOS (使用 Homebrew)**：`brew install libpq`

然後，重試 `pip install` 指令。

---

### 總結
錯誤的發生是因為缺少 `libpq-fe.h`，該檔案是 PostgreSQL 客戶端開發檔案的一部分。對於您的基於 Debian 的系統，使用 `sudo apt-get install libpq-dev` 安裝 `libpq-dev` 應該可以解決問題。之後，重新執行您的 `pip install` 指令，`psycopg2` 應該可以成功建置。如果您偏好更快的修復方法且不需要原始碼編譯，請改用 `psycopg2-binary`。