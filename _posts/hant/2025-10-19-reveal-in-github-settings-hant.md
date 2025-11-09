---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GitHub 顯示設定視窗
translated: true
type: note
---

### 概述
此 XML 檔案是一個 macOS 應用程式的 Interface Builder XIB（XML Interface Builder）文件。XIB 檔案在 Xcode 中用於以宣告式方式定義使用者介面，特別是用於 Cocoa 應用程式中的視窗、視圖和控制項。此特定檔案定義了一個名為 **Reveal-In-GitHub** 的應用程式中的設定視窗使用者介面（可能是一個用於在 IDE 或檔案系統中快速於 GitHub 開啟原始碼檔案或儲存庫的實用工具）。

該檔案目標平台為 macOS（Cocoa 運行環境），並使用 Auto Layout (`useAutolayout="YES"`)。其結構圍繞一個主視窗物件構建，連接到一個自訂控制器類別 (`RIGSettingWindowController`)，包含關鍵視圖的 outlet，以及各種 UI 子視圖，如按鈕、標籤和一個自訂容器。

關鍵元資料：
- **工具版本**：Xcode 9.0.1 (toolsVersion="9059")，建置於 macOS 10.12.6 (systemVersion="14F27")。
- **視窗行為**：具標題欄、可關閉、可最小化、可調整大小。它不會自動重新計算鍵盤焦點循環，並使用預設動畫。
- **初始位置/大小**：在螢幕位置 (527, 176) 開啟，尺寸為 651x497 像素（在 1440x877 的螢幕上）。

檔案的根節點是 `<document>`，包含 `<dependencies>`（用於 Cocoa 外掛）和 `<objects>`（實際的 UI 層次結構）。

### 主要元件

#### 1. **File's Owner (自訂控制器)**
   - **類別**：`RIGSettingWindowController`
   - 此類別作為視窗的控制器，管理如載入/儲存設定等邏輯。
   - **Outlet**（與 UI 元素的連接）：
     - `configsView` → 用於顯示配置選項的自訂視圖 (ID: `IKd-Ev-B9V`)。
     - `mainView` → 視窗的內容視圖 (ID: `se5-gp-TjO`)。
     - `window` → 設定視窗本身 (ID: `F0z-JX-Cv5`)。
   - 視窗的 `delegate` 也連接到此控制器。

#### 2. **標準物件**
   - **First Responder** (`-1`)：用於鍵盤事件處理的佔位符。
   - **Application** (`-3`)：代表 NSApplication 實例（此處未直接使用）。

#### 3. **設定視窗**
   - **ID**：`F0z-JX-Cv5`
   - **標題**："Reveal-In-GitHub Settings"
   - **內容視圖** (ID: `se5-gp-TjO`)：一個全尺寸視圖 (651x497)，會隨視窗自動調整大小。它包含所有子視圖，使用固定框架定位（儘管啟用了 Auto Layout，這表明約束可能以程式方式或在 .storyboard 伴隨檔案中添加）。

   **子視圖佈局**（全部使用固定框架進行定位；y 座標從頂部向下遞增）：

   | 元素 | 類型 | 位置 (x, y) | 尺寸 (寬 x 高) | 描述 |
   |---------|------|-----------------|--------------|-------------|
   | **儲存按鈕** | `NSButton` (ID: `EuN-9g-Vcg`) | (14, 13) | 137x32 | 左下角的「儲存」按鈕（圓角邊框）。觸發控制器上的 `saveButtonClcked:` 動作。使用小型系統字體 (13pt)。 |
   | **重設預設選單按鈕** | `NSButton` (ID: `KvN-fn-w7m`) | (151, 12) | 169x32 | 附近的「重設預設選單」按鈕。觸發 `resetMenusButtonClicked:` 動作。小型系統字體 (13pt)。 |
   | **配置視圖** | `NSView` (自訂, ID: `IKd-Ev-B9V`) | (20, 54) | 611x330 | 中央的大型自訂視圖，標記為「Config View」。可能是一個用於動態內容（如表格、列表或 GitHub 儲存庫配置的開關）的容器。此視圖連接到 `configsView` outlet。 |
   | **自訂選單項目標籤** | `NSTextField` (ID: `G1C-Td-n9Y`) | (18, 425) | 187x17 | 靠近底部的靜態標籤「Custom Menu Items」。Helvetica Neue (17pt)，標籤顏色。 |
   | **清除預設儲存庫按鈕** | `NSButton` (ID: `KvN-fn-w7m`) | (14, 449) | 164x32 | 左下角的「清除預設儲存庫」按鈕。觸發 `clearButtonClicked:` 動作。小型系統字體 (13pt)。 |
   | **選單標題標籤** | `NSTextField` (ID: `UUf-Cr-5zs`) | (20, 392) | 77x18 | 靜態標籤「Menu Title」。Helvetica Neue (14pt)，標籤顏色。 |
   | **鍵盤快捷鍵標籤** | `NSTextField` (ID: `rMv-by-SKS`) | (112, 391) | 63x19 | 靜態標籤「⌃⇧⌘ +」（Control+Shift+Command +）。Lucida Grande UI (15pt)，標籤顏色。表示用於應用程式選單的可自訂全域快捷鍵。 |
   | **URL 模式標籤** | `NSTextField` (ID: `zW4-cw-Rhb`) | (410, 392) | 94x18 | 靜態標籤「URL Pattern 」。系統字體 (15pt)，標籤顏色。可能用於配置 GitHub URL 範本（例如，用於深層連結到檔案或 blame 視圖）。 |

   - **佈局說明**：
     - 元素大多左對齊 (x=14-20)，採用緊湊的表單式設計。
     - 頂部：操作按鈕（儲存/重設）。
     - 中部：大型配置視圖（用於儲存庫/設定管理的主要空間）。
     - 底部：用於選單自訂的標籤和一個清除按鈕。
     - 所有文字欄位均不可編輯（靜態標籤），表明使用者輸入發生在配置視圖內部或透過未在此處定義的單獨欄位進行。
     - 顏色：系統預設值（標籤/控制項顏色以符合無障礙需求）。
     - 字體：混合使用系統字體、Helvetica Neue 和 Lucida Grande，以呈現原生 macOS 風格。

### 目的與功能
此設定視窗允許使用者：
- **管理儲存庫/配置**：透過中央的「Config View」（例如，添加/移除預設的 GitHub 儲存庫）。
- **自訂選單**：設定選單標題、全域鍵盤快捷鍵 (⌃⇧⌘+) 以及用於在 GitHub 中顯示檔案的 URL 模式。
- **持久化變更**：使用專用按鈕儲存設定或重設/清除預設值。

控制器 (`RIGSettingWindowController`) 處理按鈕動作：
- `saveButtonClcked:` – 儲存使用者變更（例如，到 UserDefaults 或 plist）。
- `resetMenusButtonClicked:` – 恢復出廠選單設定。
- `clearButtonClicked:` – 移除預設儲存庫條目。

此 XIB 可能在應用程式程式碼中以程式方式載入（例如，`NSNib(nibNamed: "Settings", bundle: nil)`），並動態填充自訂視圖（例如，使用 NSTableView 來顯示儲存庫列表）。

如果您正在建置或修改此應用程式，可以在 Xcode 的 Interface Builder 中開啟 XIB 以視覺化方式檢視/編輯佈局。對於程式碼整合，請在控制器類別中尋找與動作選擇器匹配的 IBAction 方法。