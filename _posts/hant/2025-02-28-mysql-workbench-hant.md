---
audio: false
generated: true
lang: hant
layout: post
title: 使用 MySQL Workbench
translated: true
type: note
---

### 重點摘要
- MySQL Workbench 很可能是一款免費開源工具，用於管理 MySQL 資料庫，支援 Windows、macOS 和 Linux 系統。
- 您可以從官方網站下載該工具，安裝後使用伺服器詳細資訊（如主機名稱和使用者名稱）設定連線。
- 研究顯示您可以透過圖形介面和 SQL 語法兩種方式建立資料庫、資料表及執行查詢。
- 證據表明它還提供資料建模和伺服器管理等進階功能，這對初學者來說可能是意想不到的。

### 什麼是 MySQL Workbench？
MySQL Workbench 是一款協助您設計、開發和管理 MySQL 資料庫的工具。它免費、開源，並可在 Windows、macOS 和 Linux 上運行，因此適合許多使用者使用。它提供圖形化介面，這意味著您不一定需要編寫程式碼來管理資料庫，當然您也可以選擇直接編寫 SQL 語句。

### 開始使用
首先，請訪問官方下載頁面 [https://www.mysql.com/products/workbench/](https://www.mysql.com/products/workbench/) 並取得適合您作業系統的版本。按照提供的安裝步驟進行操作，這些步驟在不同平台上都相當直觀且類似。

### 設定與使用
安裝完成後，開啟 MySQL Workbench 並點擊「MySQL Connections」旁邊的「+」按鈕建立新連線。您需要提供伺服器的主機名稱、連接埠（通常為 3306）、使用者名稱和密碼等詳細資訊。測試連線以確保其正常運作。

連線成功後，您可以：
- **建立資料庫：** 在 SQL 編輯器中執行 `CREATE DATABASE database_name;`，或在「Schemas」上按右鍵選擇「Create Schema...」。
- **建立資料表：** 在 SQL 編輯器中編寫 CREATE TABLE 語句，或使用圖形化介面在資料庫上按右鍵進行操作。
- **執行查詢：** 在 SQL 編輯器中編寫 SQL 查詢並執行以查看結果。

### 進階功能
除了基礎功能外，MySQL Workbench 還提供了一些意想不到的進階功能，例如資料建模（您可以使用 ER 圖表視覺化設計資料庫）以及伺服器管理工具（例如管理使用者和設定）。這些功能可以透過「Model」標籤和其他選單進行探索。

---

### 調查筆記：MySQL Workbench 使用全面指南

本節詳細探討如何使用 MySQL Workbench，在直接回答的基礎上擴展了更多背景資訊和技術細節。旨在涵蓋研究中的所有方面，確保不同專業程度的使用者都能獲得全面理解。

#### MySQL Workbench 簡介
MySQL Workbench 被描述為一個統一的視覺化工具，專為資料庫架構師、開發人員和資料庫管理員（DBA）設計。根據官方產品頁面 [MySQL Workbench](https://www.mysql.com/products/workbench/) 所述，它是免費開源的，適用於包括 Windows、macOS 和 Linux 在內的主要作業系統。這種跨平台可用性確保了其可訪問性，並且它是針對 MySQL Server 8.0 進行開發和測試的，但根據手冊 [MySQL Workbench Manual](https://dev.mysql.com/doc/workbench/en/) 指出，與 8.4 及更高版本可能存在相容性問題。該工具整合了資料建模、SQL 開發和管理功能，使其成為資料庫管理的全面解決方案。

#### 安裝流程
安裝過程因作業系統而異，但在 Windows 的教學 [Ultimate MySQL Workbench Installation Guide](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench-installation) 中找到了詳細步驟。對於 Windows 使用者，需訪問 [MySQL Downloads](https://www.mysql.com/downloads/) 選擇安裝程式，選擇自訂設定，並安裝 MySQL Server、Workbench 和 Shell。過程涉及授予權限、設定網路和配置 root 密碼，通常預設設定已足夠。對於其他作業系統，過程類似，建議使用者遵循特定平台的說明，並確認不需要 Java（與最初的猜測相反），因為 MySQL Workbench 使用 Qt 框架。

為清晰起見，下面提供了一個總結 Windows 安裝步驟的表格：

| 步驟編號 | 操作                                                                                     | 詳細說明                                                                 |
|----------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| 0        | 開啟 MySQL 網站                                                                          | 訪問 [MySQL Downloads](https://www.mysql.com/downloads/)               |
| 1        | 選擇 Downloads 選項                                                                      | -                                                                       |
| 2        | 選擇 MySQL Installer for Windows                                                         | -                                                                       |
| 3        | 選擇所需的安裝程式並點擊下載                                                              | -                                                                       |
| 4        | 開啟下載的安裝程式                                                                        | -                                                                       |
| 5        | 授予權限並選擇設定類型                                                                    | 點擊 Yes，然後選擇 Custom                                           |
| 6        | 點擊 Next                                                                                | -                                                                       |
| 7        | 安裝 MySQL server、Workbench 和 shell                                                     | 在安裝程式中選擇並移動元件                             |
| 8        | 點擊 Next，然後點擊 Execute                                                               | 下載並安裝元件                                         |
| 9        | 配置產品，使用預設的 Type 和 Networking 設定                                              | 點擊 Next                                                             |
| 10       | 將身份驗證設定為強密碼加密，設定 MySQL Root 密碼                                           | 點擊 Next                                                             |
| 11       | 使用預設的 Windows 服務設定，應用配置                                                      | 點擊 Execute，然後在配置完成後點擊 Finish                          |
| 12       | 完成安裝，啟動 MySQL Workbench 和 Shell                                                   | 選擇 Local instance，輸入密碼即可使用                            |

安裝後，使用者可以按照教學建議執行如 `Show Databases;` 這樣的基本 SQL 命令來驗證功能。

#### 設定連線
連線到 MySQL 伺服器是關鍵步驟，在 [SiteGround Tutorials](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/) 和 [w3resource MySQL Workbench Tutorial](https://www.w3resource.com/mysql/administration-tools/mysql-workbench-tutorial.php) 等多個來源中找到了詳細指導。使用者開啟 MySQL Workbench，點擊「MySQL Connections」旁邊的「+」按鈕，然後輸入連線名稱、方法（通常是 Standard TCP/IP）、主機名稱、連接埠（預設 3306）、使用者名稱、密碼以及可選的預設結構描述等詳細資訊。建議測試連線，w3resource 教學中的幻燈片透過「MySQL Workbench New Connection Step 1」到「Step 4」視覺化地引導了整個過程，確認了流程。

對於遠端連線，還需要考慮其他因素，例如確保伺服器防火牆允許該 IP 位址，如 [Connect MySQL Workbench](https://www.inmotionhosting.com/support/website/connect-database-remotely-mysql-workbench/) 中所述。這對於連線到雲端 MySQL 實例（例如 Azure Database for MySQL）的使用者至關重要，詳見 [Quickstart: Connect MySQL Workbench](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench)。

#### 執行資料庫操作
連線成功後，使用者可以執行各種操作，並可使用圖形化和基於 SQL 的方法。建立資料庫可以透過 SQL 編輯器使用 `CREATE DATABASE database_name;` 完成，或者透過在「Schemas」上按右鍵選擇「Create Schema...」以圖形化方式完成，如教學所示。同樣，建立資料表涉及編寫 CREATE TABLE 語句或使用圖形介面，並具有編輯資料表資料和管理結構描述的選項，如 [A Complete Guide on MySQL Workbench](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench) 中所述。

執行查詢由 SQL 編輯器提供支援，該編輯器提供語法突顯、自動完成和查詢歷史記錄等功能，提升了易用性。這些功能在 [MySQL Workbench](https://www.mysql.com/products/workbench/) 中有所強調，使其對初學者和進階使用者都更加友好。

#### 進階功能與工具
MySQL Workbench 超越了基礎功能，提供進階功能，例如使用實體關係圖（ER diagrams）進行資料建模、正向和逆向工程以及變更管理，如 [MySQL Workbench Manual](https://dev.mysql.com/doc/workbench/en/) 中所述。「Model」標籤允許視覺化設計並生成 SQL 腳本，這對資料庫架構師特別有用。伺服器管理工具包括管理使用者、權限和配置，並提供視覺化控制台以獲得更好的可視性，如 [MySQL Workbench](https://www.mysql.com/products/workbench/) 所示。

其他功能包括資料庫遷移、效能優化以及備份/還原功能，並附帶如 Data Export 用於備份資料庫等工具，詳見 [SiteGround Tutorials](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/)。這些進階功能對於剛接觸資料庫管理的使用者來說可能是意想不到的，它提供了一套強大的工具套件用於全面的資料庫管理。

#### 提示與最佳實踐
使用者應確保 MySQL 伺服器正在運行且連線詳細資訊正確無誤，並檢查遠端連線的防火牆設定。建議使用強密碼和安全方法，尤其是在處理敏感資料時。儲存 SQL 腳本和探索版本控制可以優化工作流程，儘管直接回答中未詳細說明，但這是來自社群洞察的最佳實踐的一部分。

#### 結論
本調查筆記提供了使用 MySQL Workbench 的全面指南，涵蓋了安裝、連線設定、基礎和進階操作以及提示。它利用了多個可靠來源，確保了截至 2025 年 2 月 28 日的準確性，並專為尋求詳細技術指導的使用者設計。

#### 主要引用文獻
- [MySQL Workbench Manual about 10 words](https://dev.mysql.com/doc/workbench/en/)
- [MySQL Workbench product page about 10 words](https://www.mysql.com/products/workbench/)
- [Ultimate MySQL Workbench Installation Guide about 10 words](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench-installation)
- [SiteGround Tutorials MySQL Workbench about 10 words](https://www.siteground.com/tutorials/php-mysql/mysql-workbench/)
- [w3resource MySQL Workbench Tutorial about 10 words](https://www.w3resource.com/mysql/administration-tools/mysql-workbench-tutorial.php)
- [Connect MySQL Workbench remotely about 10 words](https://www.inmotionhosting.com/support/website/connect-database-remotely-mysql-workbench/)
- [Quickstart Connect MySQL Workbench Azure about 10 words](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench)
- [A Complete Guide on MySQL Workbench about 10 words](https://www.simplilearn.com/tutorials/mysql-tutorial/mysql-workbench)