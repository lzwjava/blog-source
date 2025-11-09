---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: CodeIgniter 使用者代理設定陣列
translated: true
type: note
---

### 概述
這段 PHP 程式碼片段是 CodeIgniter 框架（一個 PHP 網頁框架）的一部分，具體來自 User Agent 類別的設定檔。它定義了四個陣列（`$platforms`、`$browsers`、`$mobiles` 和 `$robots`），這些陣列將用戶代理字串片段映射到易讀的瀏覽器、作業系統、流動裝置和網絡爬蟲/機器人名稱。此程式碼用於根據客戶端發送的 HTTP User-Agent 標頭來解析和識別訪問網站的裝置類型、瀏覽器或機器人。

這些陣列是關聯陣列（鍵值對），其中鍵是用戶代理字串中的部分字串（不區分大小寫匹配），值是相應的顯示名稱。CodeIgniter 的 User Agent 函式庫使用這些進行檢測，例如判斷訪問者是否使用 Android、Chrome 或是搜尋機器人。

### $platforms 陣列
此陣列識別作業系統或平台。鍵是可能出現在 User-Agent 標頭中的子字串，值是用於顯示的清晰名稱。

- **範例條目**：
  - `'windows nt 10.0'` → `'Windows 10'`
  - `'android'` → `'Android'`
  - `'os x'` → `'Mac OS X'`
- **用途**：協助檢測客戶端的作業系統（例如 Windows、iOS、Linux），用於分析、內容自訂或功能調整。
- **注意**：順序對準確性很重要，因為某些子字串可能重疊（例如 `'windows'` 是最後的通用匹配項）。

### $browsers 陣列
識別網頁瀏覽器。瀏覽器通常報告多個識別符，因此順序會優先處理子類型（如註釋所述）。

- **範例條目**：
  - `'Chrome'` → `'Chrome'`
  - `'MSIE'` → `'Internet Explorer'`
  - `'Firefox'` → `'Firefox'`
  - 特殊情況：`'Opera.*?Version'`（類似正則表達式的匹配）用於報告為 "Opera/9.80" 並帶有版本的現代 Opera。
- **用途**：確定瀏覽器（例如 Chrome、Safari）以提供瀏覽器特定功能或重定向。
- **正則表達式注意**：某些鍵使用基本正則表達式模式（例如 `.*?` 用於萬用字元匹配），在函式庫中處理。

### $mobiles 陣列
映射流動裝置、手機及相關裝置/瀏覽器的用戶代理標誌。它較大，包括手機、平板電腦、遊戲主機和後備類別。

- **結構化部分**：
  - 手機/製造商：`'iphone'` → `'Apple iPhone'`、`'samsung'` → `'Samsung'`。
  - 作業系統：`'android'` → `'Android'`、`'symbian'` → `'Symbian'`。
  - 瀏覽器：`'opera mini'` → `'Opera Mini'`、`'fennec'` → `'Firefox Mobile'`。
  - 其他/後備：`'mobile'` → `'Generic Mobile'` 用於未匹配的流動裝置標誌。
- **用途**：標記流動裝置以實現響應式設計、僅限流動裝置的功能或應用程式重定向。包括舊條目（部分已註釋掉，因為過時）。

### $robots 陣列
列出常見的網絡爬蟲和機器人。鍵是來自機器人用戶代理的子字串。

- **範例條目**：
  - `'googlebot'` → `'Googlebot'`
  - `'bingbot'` → `'Bing'`
  - `'yandex'` → `'YandexBot'`
- **用途**：識別爬蟲以進行 SEO 處理，例如向機器人提供不同內容（例如無廣告）或記錄機器人流量。

### 在 CodeIgniter 中的使用方式
- User Agent 類別加載此檔案並使用如 `is_browser()`、`is_mobile()`、`is_robot()` 和 `platform()` 等方法來解析 User-Agent 字串。
- 它透過這些陣列執行不區分大小寫的搜尋，以將鍵與字串匹配。
- 對於差異（例如未列出的新裝置/瀏覽器），您需要手動或透過社群擴展更新這些陣列。

### 補充說明
- **安全性**：這僅用於數據收集；它不執行有害程式碼。用戶代理字串可能被偽造，因此請勿依賴此進行關鍵安全性檢查。
- **更新**：CodeIgniter 版本可能已添加/修改條目；這看起來像是較舊的快照（例如 Edge 標記為 'Spartan' 已過時）。
- **如何測試**：在 PHP 腳本中，您可以加載此檔案並使用 `strpos` 或正則表達式來匹配範例 User-Agent 字串。

如果您提供特定部分或對實現有疑問，請告訴我！