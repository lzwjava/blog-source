---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 連接 Python 與 IBM DB2
translated: true
type: note
---

### 概述
IBM DB2 是一款關聯式資料庫管理系統，而 Python 可以透過 `ibm_db` 套件與其互動，該套件提供低階介面；另有 `ibm_db_dbi`，這是一個符合 DB-API 2.0 標準的封裝層，建構於 `ibm_db` 之上，提供更簡便、更符合 Python 風格的用法。`ibm_db` 更直接且功能強大，但需要更深入的知識；而 `ibm_db_dbi` 則模仿 Python 的 `sqlite3` 模組，使標準資料庫操作更簡單。兩者均屬於 IBM DB2 Python 驅動程式的一部分。

### 安裝
使用 pip 安裝套件：
```
pip install ibm_db
pip install ibm_db_dbi
```
注意：這些套件需要 DB2 用戶端函式庫。在 Windows/Linux 上，請從 IBM 網站下載並安裝 IBM Data Server Driver Package。在 macOS 上，可能需要額外設定。請確保您的 DB2 伺服器可存取（例如，在具有憑證的主機上運行）。

### 使用 ibm_db
`ibm_db` 提供連接、執行陳述式和處理結果的函式。它不符合 DB-API 標準，但提供更多控制權。

#### 基本連接與查詢
```python
import ibm_db

# 連接字串格式：DATABASE=<db_name>;HOSTNAME=<host>;PORT=<port>;PROTOCOL=TCPIP;UID=<user>;PWD=<password>;
conn_str = "DATABASE=mydb;HOSTNAME=192.168.1.100;PORT=50000;PROTOCOL=TCPIP;UID=myuser;PWD=mypassword;"

# 連接
conn = ibm_db.connect(conn_str, "", "")

# 執行查詢
stmt = ibm_db.exec_immediate(conn, "SELECT * FROM MYTABLE")

# 取得結果（一次一筆）
row = ibm_db.fetch_assoc(stmt)
while row:
    print(row)  # 返回字典
    row = ibm_db.fetch_assoc(stmt)

# 關閉
ibm_db.close(conn)
```
- **關鍵函式**：`connect()`、`exec_immediate()` 用於簡單查詢，`prepare()` 和 `execute()` 用於參數化查詢以防止注入攻擊。
- **預備陳述式**：使用 `prepare()` 編譯查詢，並使用 `execute()` 帶入參數。

#### 錯誤處理
```python
try:
    conn = ibm_db.connect(conn_str, "", "")
except Exception as e:
    print(f"連接失敗：{str(e)}")
```

### 使用 ibm_db_dbi
`ibm_db_dbi` 實作了 DB-API 2.0，使其可與 `sqlite3` 或 `psycopg2` 等模組互換使用。

#### 基本連接與查詢
```python
import ibm_db_dbi

# 連接字串類似 ibm_db
conn_str = "DATABASE=mydb;HOSTNAME=192.168.1.100;PORT=50000;PROTOCOL=TCPIP;UID=myuser;PWD=mypassword;"

# 連接
conn = ibm_db_dbi.connect(conn_str)

# 建立游標
cursor = conn.cursor()

# 執行查詢
cursor.execute("SELECT * FROM MYTABLE")

# 取得結果
rows = cursor.fetchall()  # 返回元組列表
for row in rows:
    print(row)

# 關閉
cursor.close()
conn.close()
```
- **參數化查詢**：`cursor.execute("SELECT * FROM MYTABLE WHERE ID = ?", (id_value,))` – 使用 ? 作為佔位符。
- **交易**：`conn.commit()` 或 `conn.rollback()`；預設情況下自動提交為關閉狀態。

### 主要差異與使用時機

| 功能特性         | ibm_db                          | ibm_db_dbi                      |
|------------------|---------------------------------|---------------------------------|
| 標準符合度       | 非 DB-API（低階）               | 符合 DB-API 2.0 標準           |
| 易用性           | 需要較多程式碼；直接存取        | 語法更簡單，類似 Python 風格   |
| 效能表現         | 複雜操作可能更快                | 封裝層帶來額外負擔             |
| 功能完整性       | 完整的 DB2 功能                | 透過 DB-API 介面提供子集功能   |
| 適用場景         | 需要原始控制的自訂應用程式      | 標準 CRUD 操作                 |

如果您習慣使用其他 DB-API 驅動程式，可選用 `ibm_db_dbi` 以保持熟悉度。若需使用進階的 DB2 特定功能（如預存程序或批量操作），請切換至 `ibm_db`。

### 最佳實踐
- 始終在 `try-finally` 或 `with` 區塊中處理例外並關閉連接，以避免資源洩漏。
- 對於大型結果集，使用 `fetchmany(size)` 而非 `fetchall()` 以限制記憶體使用量。
- 檢查 DB2 版本相容性；這些套件支援 DB2 LUW、z/OS、iSeries。
- 如需進階主題（如 SSL 連接或 CLPPlus 整合），請參閱 IBM 文件。

更多範例請參閱 [IBM db2 Python 驅動程式儲存庫](https://github.com/ibmdb/python-ibmdb)。若遇到問題，請確保您的 DB2 實例正在運行且憑證正確無誤。