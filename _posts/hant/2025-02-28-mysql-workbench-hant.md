---
audio: false
generated: true
lang: hant
layout: post
title: 使用 MySQL Workbench
translated: true
---

### 關鍵要點
- MySQL Workbench 可能是一個免費的開源工具，用於管理 MySQL 資料庫，適用於 Windows、macOS 和 Linux。
- 您似乎可以從官方網站下載它，然後安裝並使用伺服器詳細資訊（如主機名和用戶名）設置連接。
- 研究表明，您可以使用圖形和 SQL 方法創建資料庫、表和運行查詢。
- 証據顯示它提供高級功能，如數據建模和伺服器管理，這對於初學者來說可能是意外的。

### 什麼是 MySQL Workbench？
MySQL Workbench 是一個幫助您設計、開發和管理 MySQL 資料庫的工具。它是免費的、開源的，並且在 Windows、macOS 和 Linux 上運行，使其對許多用戶可用。它提供圖形界面，這意味著您不總是需要編寫代碼來管理資料庫，雖然如果您喜歡，您可以這樣做。

### 開始使用
首先，訪問官方下載頁面 [https://www.mysql.com/products/workbench/](https://www.mysql.com/products/workbench/) 並獲取適合您操作系統的版本。按照提供的安裝步驟進行操作，這些步驟簡單且跨平台相似。

### 設置和使用
安裝後，打開 MySQL Workbench 並通過點擊 "MySQL Connections" 旁邊的 '+' 按鈕創建新連接。您需要伺服器的主機名、端口（通常是 3306）、用戶名和密碼等詳細資訊。測試連接以確保其工作。

連接後，您可以：
- **創建資料庫：** 在 SQL 編輯器中運行 `CREATE DATABASE database_name;` 或右鍵點擊 "Schemas" 並選擇 "Create Schema..."
- **創建表：** 在 SQL 編輯器中編寫 CREATE TABLE 語句或使用圖形選項，右鍵點擊資料庫。
- **運行查詢：** 在 SQL 編輯器中編寫您的 SQL 查詢並執行以查看結果。

### 高級功能
除了基本功能，MySQL Workbench 還提供意外的功能，如數據建模，您可以使用 ER 圖表視覺設計資料庫，以及伺服器管理工具，如管理用戶和配置。這些可以通過 "Model" 選項卡和其他菜單進行探索。

---

### 調查筆記：MySQL Workbench 使用全面指南

本節提供了使用 MySQL Workbench 的詳細探討，擴展了直接答案，並添加了額外的背景和技術細節。它旨在涵蓋研究中討論的所有方面，確保對各個技能水平的用戶都有全面的理解。

#### MySQL Workbench 簡介
MySQL Workbench 被描述為一個統一的視覺工具，適用於資料庫架構師、開發人員和資料庫管理員（DBAs）。它是免費和開源的，適用於主要操作系統，包括 Windows、macOS 和 Linux，如官方產品頁面 [MySQL Workbench](https://www.mysql.com/products/workbench/) 中所記載。這種跨平台可用性確保了可訪問性，並且與 MySQL Server 8.0 一起開發和測試，對於 8.4 及更高版本可能存在兼容性問題，如手冊 [MySQL Workbench Manual](https://dev.mysql.com/doc/workbench/en/) 中所記載。該工具整合了數據建模、SQL 開發和管理，成為資料庫管理的全面解決方案。

#### 安裝過程
安裝過程因操作系統而異，但 Windows 的詳細步驟可以在教程 [Ultimate MySQL Workbench Installation Guide](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench-installation) 中找到。對於 Windows，用戶訪問 [MySQL Downloads](https://www.mysql.com/downloads/) 選擇安裝程序，選擇自定義設置，並安裝 MySQL Server、Workbench 和 shell。該過程涉及授予權限、設置網絡和配置根密碼，默認設置通常足夠。對於其他 OS，過程相似，並建議用戶遵循特定於平台的說明，確保不需要 Java，與最初的猜測相反，因為 MySQL Workbench 使用 Qt 框架。

以下是 Windows 安裝步驟的摘要表，以便清楚：

| 步驟編號 | 操作                                                                                     | 詳細資訊                                                                 |
|----------|--------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| 0        | 打開 MySQL 網站                                                                         | 訪問 [MySQL Downloads](https://www.mysql.com/downloads/)               |
| 1        | 選擇下載選項                                                                    | -                                                                       |
| 2        | 選擇 Windows 的 MySQL 安裝程序                                                         | -                                                                       |
| 3        | 選擇所需的安裝程序並點擊下載                                                | -                                                                       |
| 4        | 打開下載的安裝程序                                                                  | -                                                                       |
| 5        | 授予權限並選擇設置類型                                                     | 點擊是，然後選擇自定義                                           |
| 6        | 點擊下一步                                                                                | -                                                                       |
| 7        | 安裝 MySQL 伺服器、Workbench 和 shell                                                 | 在安裝程序中選擇並移動組件                             |
| 8        | 點擊下一步，然後執行                                                                   | 下載並安裝組件                                         |
| 9        | 配置產品，使用默認類型和網絡設置                                | 點擊下一步                                                             |
| 10       | 將身份驗證設置為強密碼加密，設置 MySQL 根密碼                  | 點擊下一步                                                             |
| 11       | 使用默認的 Windows 服務設置，應用配置                                  | 點擊執行，然後在配置後點擊完成                          |
| 12       | 完成安裝，啟動 MySQL Workbench 和 Shell                                    | 選擇本地實例，輸入密碼以使用                            |

安裝後，用戶可以通過運行基本的 SQL 命令（如 `Show Databases;`）來驗證，如教程中所建議的，以確保功能。

#### 設置連接
連接到 MySQL 伺服器是一個關鍵步驟，詳細指導可以在多個來源中找到，包括 [SiteGround Tutorials](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/) 和 [w3resource MySQL Workbench Tutorial](https://www.w3resource.com/mysql/administration-tools/mysql-workbench-tutorial.php)。用戶打開 MySQL Workbench，點擊 "MySQL Connections" 旁邊的 '+' 按鈕，然後輸入連接名稱、方法（通常是標準 TCP/IP）、主機名、端口（默認 3306）、用戶名、密碼和可選的默認模式。建議測試連接，並且 w3resource 教程中的幻燈片視覺指導 "MySQL Workbench 新連接步驟 1" 到 "步驟 4"，確認過程。

對於遠程連接，額外的考慮包括確保 IP 地址在伺服器的防火牆中允許，如 [Connect MySQL Workbench](https://www.inmotionhosting.com/support/website/connect-database-remotely-mysql-workbench/) 中所記載。這對於連接到基於雲的 MySQL 實例（如 Azure Database for MySQL）的用戶至關重要，詳細信息請參閱 [Quickstart: Connect MySQL Workbench](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench)。

#### 執行資料庫操作
連接後，用戶可以執行各種操作，圖形和 SQL 方法均可用。可以通過 SQL 編輯器中的 `CREATE DATABASE database_name;` 或圖形方式（右鍵點擊 "Schemas" 並選擇 "Create Schema..."）創建資料庫，如教程中所示。類似地，創建表涉及編寫 CREATE TABLE 語句或使用圖形界面，並且有選項編輯表數據和管理模式，如 [A Complete Guide on MySQL Workbench](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench) 中所述。

運行查詢由 SQL 編輯器促成，該編輯器提供語法突出顯示、自動完成和查詢歷史記錄，增強了可用性。這些功能在 [MySQL Workbench](https://www.mysql.com/products/workbench/) 中得到了強調，使其對初學者和高級用戶都友好。

#### 高級功能和工具
MySQL Workbench 除了基本功能外，還擁有高級功能，如使用實體關係（ER）圖表進行數據建模、正向和反向工程以及變更管理，如 [MySQL Workbench Manual](https://dev.mysql.com/doc/workbench/en/) 中所述。 "Model" 選項卡允許視覺設計，生成 SQL 腳本，這對於資料庫架構師特別有用。伺服器管理工具包括管理用戶、權限和配置，並且有視覺控制台以提供更好的可見性，如 [MySQL Workbench](https://www.mysql.com/products/workbench/) 中所示。

其他功能包括資料庫遷移、性能優化和備份/還原功能，具體工具如 Data Export 用於備份資料庫，詳細信息請參閱 [SiteGround Tutorials](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/)。這些高級功能可能對於新手資料庫管理員來說是意外的，提供了一套全面的資料庫管理工具。

#### 使用技巧和最佳實踐
用戶應確保 MySQL 伺服器正在運行，並且連接詳細資訊正確，防火牆設置已檢查遠程連接。建議使用強密碼和安全方法，特別是對於敏感數據。保存 SQL 腳本並探索版本控制可以增強工作流程，雖然在直接答案中沒有詳細說明，但這是社區見解的一部分。

#### 結論
本調查筆記提供了使用 MySQL Workbench 的全面指南，涵蓋安裝、連接設置、基本和高級操作以及技巧。它利用了多個可靠來源，確保截至 2025 年 2 月 28 日的準確性，並針對尋求詳細技術指導的用戶設計。

#### 關鍵引用
- [MySQL Workbench Manual 關於 10 個字](https://dev.mysql.com/doc/workbench/en/)
- [MySQL Workbench 產品頁面 關於 10 個字](https://www.mysql.com/products/workbench/)
- [Ultimate MySQL Workbench Installation Guide 關於 10 個字](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench-installation)
- [SiteGround Tutorials MySQL Workbench 關於 10 個字](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/)
- [w3resource MySQL Workbench Tutorial 關於 10 個字](https://www.w3resource.com/mysql/administration-tools/mysql-workbench-tutorial.php)
- [Connect MySQL Workbench 遠程 關於 10 個字](https://www.inmotionhosting.com/support/website/connect-database-remotely-mysql-workbench/)
- [Quickstart Connect MySQL Workbench Azure 關於 10 個字](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench)
- [A Complete Guide on MySQL Workbench 關於 10 個字](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench)