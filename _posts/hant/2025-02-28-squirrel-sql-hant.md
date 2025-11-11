---
audio: false
generated: true
lang: hant
layout: post
title: 使用 Squirrel SQL 連接數據庫
translated: true
type: note
---

### 重點摘要
- Squirrel SQL 似乎是一個基於 Java 的 SQL 客戶端，用於透過 JDBC 驅動程式連接資料庫。
- 研究顯示，您需要安裝 Java、適用於您資料庫的正確 JDBC 驅動程式，並建立包含連接詳細資訊的別名才能使用它。
- 證據傾向於步驟包括下載 Squirrel SQL、設定驅動程式，並透過用戶友好的介面進行連接。

### 開始使用 Squirrel SQL
Squirrel SQL 是一個協助您管理和查詢資料庫的工具，其設計對資料庫管理新手十分友好。以下是入門步驟：

#### 安裝
首先，請確保您的電腦已安裝 Java，您可以從[此網站](https://www.java.com/download)下載。接著，從 [SourceForge](https://sourceforge.net/p/squirrel-sql) 下載 Squirrel SQL，並按照安裝精靈的指示完成設定。

#### 連接至資料庫
要進行連接，您需要適用於特定資料庫（例如 MySQL、PostgreSQL）的 JDBC 驅動程式。請在資料庫供應商的網站上尋找這些驅動程式，例如 [MySQL](https://dev.mysql.com/downloads/connector/j) 或 [PostgreSQL](https://jdbc.postgresql.org/download.html)。在 Squirrel SQL 的「檢視驅動程式」下新增驅動程式，然後建立一個包含資料庫 URL（例如「jdbc:mysql://localhost:3306/mydatabase」）、使用者名稱和密碼的別名。雙擊別名即可連接。

#### 使用介面
連接成功後，使用「物件」標籤瀏覽資料庫結構和數據，並使用「SQL」標籤執行查詢。它還支援數據匯入和圖形視覺化等功能，這對於專注於 SQL 管理的工具來說可能出乎意料。

---

### 調查筆記：使用 Squirrel SQL 及連接資料庫的完整指南

本筆記詳細探討如何使用 Squirrel SQL（一個基於 Java 的圖形化 SQL 客戶端）進行資料庫管理，特別著重於連接資料庫。它基於現有資源，對初始指南進行了擴展，提供了專業且全面的概述，適合需要深入理解的用戶。

#### Squirrel SQL 簡介
Squirrel SQL 是一個開源的 Java SQL 客戶端程式，適用於任何符合 JDBC 標準的資料庫，讓用戶能夠檢視結構、瀏覽數據並執行 SQL 指令。它根據 GNU 較寬通用公共許可證分發，確保了可訪問性和靈活性。由於其基於 Java，它可以在任何具有 JVM 的平台上運行，使其對 Windows、Linux 和 macOS 用戶都具有通用性。

#### 安裝流程
安裝過程始於確保已安裝 Java，因為 Squirrel SQL 3.0 版本至少需要 Java 6，但更新版本可能需要更高版本的 Java。用戶可以從[此網站](https://www.java.com/download)下載 Java。接著，從 [SourceForge](https://sourceforge.net/p/squirrel-sql) 下載 Squirrel SQL，它提供為 JAR 檔案（例如「squirrel-sql-version-install.jar」）。安裝涉及使用 Java 運行 JAR 檔案，並使用設定助理，該助理提供如「基本」或「標準」安裝等選項，後者包括有用的外掛程式，例如程式碼完成和語法突顯。

#### 連接至資料庫：逐步指南
連接至資料庫涉及幾個關鍵步驟，每個步驟都需要注意細節以確保成功整合：

1. **取得 JDBC 驅動程式**：每種資料庫類型都需要特定的 JDBC 驅動程式。例如，MySQL 用戶可以從 [MySQL](https://dev.mysql.com/downloads/connector/j) 下載，PostgreSQL 從 [PostgreSQL](https://jdbc.postgresql.org/download.html) 下載，Oracle 從 [Oracle](https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html) 下載。驅動程式通常是一個 JAR 檔案，用於促進 Squirrel SQL 與資料庫之間的通訊。

2. **在 Squirrel SQL 中新增驅動程式**：開啟 Squirrel SQL，導航至「視窗」>「檢視驅動程式」，然後點擊「+」圖示新增驅動程式。為其命名（例如「MySQL Driver」），輸入類別名稱（例如，對於較新的 MySQL 版本為「com.mysql.cj.jdbc.Driver」，請注意版本差異），並在「額外類別路徑」標籤中新增 JAR 檔案路徑。藍色勾號表示驅動程式已在 JVM 類別路徑中；紅色 X 表示需要從供應商處下載。

3. **建立別名**：從選單中選擇「別名」>「新增別名…」或使用 Ctrl+N。輸入別名名稱，選擇驅動程式，並輸入資料庫 URL。URL 格式因資料庫而異：
   - MySQL：「jdbc:mysql://主機名稱:埠號/資料庫名稱」
   - PostgreSQL：「jdbc:postgresql://主機名稱:埠號/資料庫名稱」
   - Oracle：「jdbc:oracle:thin:@//主機名稱:埠號/SID」
   提供使用者名稱和密碼，確保詳細資訊正確無誤，這些資訊由資料庫管理員提供。

4. **建立連接**：在「別名」視窗中雙擊別名以開啟工作階段。Squirrel SQL 支援多個同時工作階段，對於比較數據或跨連接共享 SQL 語句非常有用。

#### 使用 Squirrel SQL：介面與功能
連接成功後，Squirrel SQL 提供了一個強大的介面用於資料庫互動：

- **物件標籤**：此標籤允許瀏覽資料庫物件，例如目錄、結構描述、表格、觸發器、視圖、序列、預存程序和 UDT。用戶可以以樹狀形式導航、編輯值、插入或刪除列，以及匯入/匯出數據，從而增強數據管理能力。

- **SQL 標籤**：基於 fifesoft.com 的 RSyntaxTextArea 的 SQL 編輯器，提供語法突顯，並支援開啟、建立、儲存和執行 SQL 檔案。它非常適合執行查詢，包括複雜的聯結，結果以包含元數據的表格形式返回。

- **附加功能**：Squirrel SQL 包括外掛程式，例如用於 Excel/CSV 的數據匯入外掛程式、DBCopy 外掛程式、用於用戶定義程式碼範本的 SQL 書籤外掛程式（例如常見的 SQL 和 DDL 語句）、SQL 驗證器外掛程式，以及用於 DB2、Firebird 和 Derby 的資料庫特定外掛程式。圖形外掛程式可視化表格關係和外來鍵，這對於僅期望基本 SQL 功能的用戶來說可能出乎意料。用戶可以使用 Ctrl+J 插入已加入書籤的 SQL 範本，從而簡化重複性任務。

#### 疑難排解與注意事項
用戶可能會遇到連接問題，可以透過以下方式解決：
- 確保資料庫伺服器正在運行且可訪問。
- 驗證 JDBC 驅動程式安裝和類別名稱的準確性，因為版本可能不同（例如，舊版 MySQL 驅動程式使用「com.mysql.jdbc.Driver」）。
- 檢查 URL 是否有拼寫錯誤或缺少參數，例如 SSL 設定（例如，對於 MySQL 為「?useSSL=false」）。
- 查閱資料庫供應商的文件以了解特定要求，例如安全連接的信任儲存區。

該介面支援多種語言的 UI 翻譯，如保加利亞語、巴西葡萄牙語、中文、捷克語、法語、德語、義大利語、日語、波蘭語、西班牙語和俄語，迎合全球用戶群體。

#### 比較分析
與其他 SQL 客戶端相比，Squirrel SQL 的優勢在於其外掛程式架構，允許資料庫供應商特定的擴展和廣泛的兼容性。然而，由於 Java 依賴性，安裝可能較不直接，且文件可能較為稀疏，通常需要第三方教程（如 [SqlBot](https://www.sqlbot.co/blog/squirrel-sql-review-and-tutorial) 上的教程）以獲取詳細指導。

#### 表格：以連接 MySQL 為例的關鍵步驟
為說明起見，以下是一個連接 MySQL（常見使用案例）的表格：

| 步驟                  | 詳細資訊                                                                                     |
|-----------------------|---------------------------------------------------------------------------------------------|
| 1. 安裝 Java       | 所需版本：SQuirreL SQL 3.0 版至少需要 Java 6；從[此網站](https://www.java.com/download)下載 |
| 2. 下載 SQuirreL SQL | 可從 [SourceForge](https://sourceforge.net/p/squirrel-sql) 取得 JAR 檔案（例如 "squirrel-sql-version-install.jar"） |
| 3. 安裝 SQuirreL SQL | 使用設定助理；選擇「基本」或「標準」安裝，後者包含如程式碼完成等外掛程式 |
| 4. 定義驅動程式  | 指向 MySQL 的 JDBC JAR 檔案（例如 mysql-connector-java-8.0.32.jar）；在驅動程式視窗中檢查狀態（若在 JVM 類別路徑中則為藍色勾號，否則為紅色 X）；從 [MySQL](https://dev.mysql.com/downloads/connector/j) 取得驅動程式 |
| 5. 建立別名    | 從選單列選擇「別名」>「新增別名…」或使用 Ctrl+N；輸入資料庫 URL（例如 "jdbc:mysql://localhost:3306/mydatabase"）、使用者名稱和密碼；詳情請諮詢資料庫管理員 |

此表格源自教程，突出了整個過程，並指出雙擊別名會開啟一個工作階段，以便透過物件或 SQL 標籤進行互動。

#### 結論
Squirrel SQL 為資料庫管理提供了一個全面的解決方案，具有詳細的連接步驟和豐富的功能集，包括外掛程式和視覺化。用戶應確保正確設定，利用供應商文件和第三方資源進行疑難排解，以確保在 2025 年 2 月 28 日為止的資料庫互動中獲得順暢的體驗。

#### 主要引用文獻
- [SQuirreL SQL - 回顧與教程 SqlBot](https://www.sqlbot.co/blog/squirrel-sql-review-and-tutorial)
- [SQuirreL SQL 客戶端 維基百科](https://en.wikipedia.org/wiki/SQuirreL_SQL_Client)
- [SQuirreL SQL 客戶端 下載 SourceForge](https://sourceforge.net/p/squirrel-sql)
- [Java 下載 官方網站](https://www.java.com/download)
- [MySQL Connector/J 下載頁面](https://dev.mysql.com/downloads/connector/j)
- [PostgreSQL JDBC 驅動程式 下載](https://jdbc.postgresql.org/download.html)
- [Oracle JDBC 驅動程式 下載](https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html)