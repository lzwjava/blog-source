---
audio: false
lang: hant
layout: post
title: 連接資料庫與Squirrel SQL
translated: true
---

### 主要要點
- 看來 Squirrel SQL 是一個基於 Java 的 SQL 客戶端，用於通過 JDBC 驅動程序連接到數據庫。
- 研究表明，您需要安裝 Java，適當的 JDBC 驅動程序和創建一個包含連接詳細信息的別名來使用它。
- 證據表明步驟包括下載 Squirrel SQL，設置驅動程序並通過用戶友好的介面連接。

### 開始使用 Squirrel SQL
Squirrel SQL 是一個幫助您管理和查詢數據庫的工具，並且設計上友好，適合新手數據庫管理員。以下是如何開始：

#### 安裝
首先，確保您的電腦上已安裝 Java，可以從 [這個網站](https://www.java.com/download) 下載。然後，從 [SourceForge](https://sourceforge.net/p/squirrel-sql) 下載 Squirrel SQL，並按照安裝向導進行設置。

#### 連接到數據庫
要連接，您需要特定數據庫的 JDBC 驅動程序（例如，MySQL、PostgreSQL）。可以在數據庫供應商的網站上找到這些驅動程序，例如 [MySQL](https://dev.mysql.com/downloads/connector/j) 或 [PostgreSQL](https://jdbc.postgresql.org/download.html)。在 Squirrel SQL 中的“查看驅動程序”下添加驅動程序，然後創建一個包含數據庫 URL（例如，“jdbc:mysql://localhost:3306/mydatabase”），用戶名和密碼的別名。雙擊別名以連接。

#### 使用介面
連接後，使用“對象”選項卡瀏覽數據庫結構和數據，使用“SQL”選項卡運行查詢。它還支持數據導入和圖形可視化等功能，這些功能可能對於專注於 SQL 管理的工具來說是意外的。

---

### 調查筆記：使用 Squirrel SQL 和連接到數據庫的全面指南

這篇筆記提供了使用 Squirrel SQL，一個基於 Java 的圖形 SQL 客戶端，進行數據庫管理的詳細探討，特別是連接到數據庫。它擴展了初步指導，提供了一個專業且全面的概述，基於可用資源，適合尋求深入理解的用戶。

#### Squirrel SQL 介紹
Squirrel SQL 是一個開源的 Java SQL 客戶端程序，設計用於任何符合 JDBC 的數據庫，使用戶能夠查看結構，瀏覽數據並執行 SQL 命令。它在 GNU 少許通用公共許可證下分發，確保了可訪問性和靈活性。由於其 Java 基礎，它可以在任何具有 JVM 的平台上運行，使其適合 Windows、Linux 和 macOS 用戶。

#### 安裝過程
安裝過程始於確保安裝了 Java，因為 Squirrel SQL 需要至少 Java 6 版本 3.0，雖然新版本可能需要更新。用戶可以從 [這個網站](https://www.java.com/download) 下載 Java。接下來，從 [SourceForge](https://sourceforge.net/p/squirrel-sql) 下載 Squirrel SQL，可用作 JAR 文件（例如，“squirrel-sql-version-install.jar”）。安裝涉及使用 Java 運行 JAR 文件並使用設置助手，該助手提供“基本”或“標準”安裝選項，後者包括有用的插件，如代碼補全和語法突出顯示。

#### 連接到數據庫：分步指南
連接到數據庫涉及幾個關鍵步驟，每個步驟都需要注意細節，以確保成功整合：

1. **獲取 JDBC 驅動程序**：每種數據庫類型都需要特定的 JDBC 驅動程序。例如，MySQL 用戶可以從 [MySQL](https://dev.mysql.com/downloads/connector/j) 下載，PostgreSQL 從 [PostgreSQL](https://jdbc.postgresql.org/download.html)，Oracle 從 [Oracle](https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html)。驅動程序，通常是 JAR 文件，促進了 Squirrel SQL 和數據庫之間的通信。

2. **在 Squirrel SQL 中添加驅動程序**：打開 Squirrel SQL，導航到“視窗”>“查看驅動程序”，然後點擊“+”圖標添加新驅動程序。命名它（例如，“MySQL 驅動程序”），輸入類名（例如，“com.mysql.cj JDBC 驅動程序”用於最新的 MySQL 版本，注意版本差異），並在“額外類路徑”選項卡中添加 JAR 文件路徑。藍色勾號表示驅動程序在 JVM 類路徑中；紅色 X 表示需要從供應商下載。

3. **創建別名**：從菜單中選擇“別名”>“新建別名…”或使用 Ctrl+N。輸入別名名稱，選擇驅動程序並輸入數據庫 URL。URL 格式各異：
   - MySQL: “jdbc:mysql://hostname:port/database_name”
   - PostgreSQL: “jdbc PostgreSQL://hostname:port/database_name”
   - Oracle: “jdbc:oracle:thin:@//hostname:port/SID”
   提供用戶名和密碼，確保詳細信息與數據庫管理員提供的信息一致。

4. **建立連接**：在“別名”窗口中雙擊別名以打開會話。Squirrel SQL 支持多個同時會話，這對於比較數據或在連接之間共享 SQL 語句非常有用。

#### 使用 Squirrel SQL：介面和功能
連接後，Squirrel SQL 提供了一個強大的介面來進行數據庫交互：

- **對象選項卡**：此選項卡允許瀏覽數據庫對象，如目錄、模式、表、觸發器、視圖、序列、過程和 UDT。用戶可以在樹狀形式中導航，編輯值，插入或刪除行，並導入/導出數據，增強數據管理能力。

- **SQL 選項卡**：SQL 編輯器基於 fifesoft.com 的 RSyntaxTextArea，提供語法突出顯示並支持打開、創建、保存和執行 SQL 文件。它適合運行查詢，包括複雜的連接，結果以包含元數據的表格返回。

- **其他功能**：Squirrel SQL 包括插件，如 Excel/CSV 數據導入插件、DBCopy 插件、SQL 書籤插件用於用戶定義的代碼模板（例如，常見的 SQL 和 DDL 語句）、SQL 驗證插件，以及特定於 DB2、Firebird 和 Derby 的數據庫插件。圖形插件可視化表關係和外鍵，這對於預期僅基本 SQL 功能的用戶來說可能是意外的。用戶可以使用 Ctrl+J 插入書籤 SQL 模板，簡化重複任務。

#### 故障排除和考慮事項
用戶可能會遇到連接問題，這可以通過以下方法解決：
- 確保數據庫伺服器正在運行並可訪問。
- 驗證 JDBC 驅動程序安裝和類名的準確性，因為版本可能有所不同（例如，較舊的 MySQL 驅動程序使用“com.mysql JDBC 驅動程序”）。
- 檢查 URL 是否有拼寫錯誤或缺少參數，例如 SSL 設置（例如，MySQL 的“?useSSL=false”）。
- 參考數據庫供應商的文檔，了解特定要求，例如信任存儲庫用於安全連接。

介面支持如保加利亞語、巴西葡萄牙語、中文、捷克語、法語、德語、意大利語、日語、波蘭語、西班牙語和俄語等語言的 UI 翻譯，滿足全球用戶的需求。

#### 比較見解
與其他 SQL 客戶端相比，Squirrel SQL 的優勢在於其插件架構，允許數據庫供應商特定的擴展和廣泛兼容性。然而，安裝可能不如預期那麼簡單，因為有 Java 依賴，文檔可能不足，通常需要第三方教程，如 [SqlBot](https://www.sqlbot.co/blog/squirrel-sql-review-and tutorial) 提供的詳細指南。

#### 表：連接到 MySQL 為例
為了說明，這裡有一個表格，用於連接到 MySQL，這是一個常見的用例：

| 步驟                  | 詳細信息                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------|
| 1. 安裝 Java       | 需要的版本：至少 Java 6 版本 3.0；從 [這個網站](https://www.java.com/download) 下載 |
| 2. 下載 SQuirreL SQL | 可從 [SourceForge](https://sourceforge.net/p/squirrel-sql) 以 JAR 文件（例如，“squirrel-sql-version-install.jar”）下載 |
| 3. 安裝 SQuirreL SQL | 使用設置助手；選擇“基本”或“標準”安裝，包括代碼補全等插件 |
| 4. 定義驅動程序  | 指向 MySQL 的 JDBC JAR 文件（例如，mysql-connector-java-8.0.32.jar）；在驅動程序窗口中檢查狀態（藍色勾號表示在 JVM 類路徑中，紅色 X 表示否）；從 [MySQL](https://dev.mysql.com/downloads/connector/j) 获取驅動程序 |
| 5. 創建別名    | 從菜單欄，選擇別名 > 新建別名… 或使用 Ctrl+N；輸入數據庫 URL（例如，“jdbc:mysql://localhost:3306/mydatabase”），用戶名和密碼；諮詢數據庫管理員以獲取詳細信息 |

這個表格來自教程，強調了過程，指出雙擊別名打開會話，通過對象或 SQL 選項卡進行交互。

#### 結論
Squirrel SQL 提供了一個全面的數據庫管理解決方案，詳細步驟連接和豐富的功能集，包括插件和可視化。用戶應確保正確設置，利用供應商文檔和第三方資源進行故障排除，確保在數據庫交互中有順暢的體驗，截至 2025 年 2 月 28 日。

#### 關鍵引用
- [SQuirreL SQL - 審查和教程 SqlBot](https://www.sqlbot.co/blog/squirrel-sql-review-and tutorial)
- [SQuirreL SQL 客戶端 Wikipedia](https://en.wikipedia.org/wiki/SQuirreL_SQL Client)
- [SQuirreL SQL 客戶端下載 SourceForge](https://sourceforge.net/p/squirrel-sql)
- [Java 下載官方網站](https://www.java.com/download)
- [MySQL Connector/J 下載頁面](https://dev.mysql.com/downloads/connector/j)
- [PostgreSQL JDBC 驅動程序下載](https://jdbc.postgresql.org/download.html)
- [Oracle JDBC 驅動程序下載](https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html)