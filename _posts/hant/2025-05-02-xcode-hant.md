---
audio: false
generated: true
lang: hant
layout: post
title: Xcode
translated: true
type: note
---

Xcode 是 Apple 的整合開發環境（IDE），用於開發 macOS、iOS、watchOS 和 tvOS 應用程式。本完整指南將引導您了解使用 Xcode 的基本要點，從安裝到應用程式分發。

**1. 入門指南：安裝與設定**

* **系統要求：** 確保您的 Mac 符合您打算安裝的 Xcode 版本所需的最低 macOS 版本要求。您可以在 Mac App Store 的 Xcode 頁面或 Apple Developer 網站上找到此資訊。
* **下載 Xcode：** 取得 Xcode 最簡單的方法是透過 Mac App Store。搜尋 "Xcode"，然後點擊「取得」和「安裝」。對於測試版，您需要從 Apple Developer 網站下載。
* **安裝：** 下載完成後，安裝過程非常簡單。請按照螢幕上的指示操作。由於檔案較大，可能需要一些時間。
* **啟動 Xcode：** 安裝後，您可以在「應用程式」檔案夾中找到 Xcode。啟動它以開始使用。

**2. 建立您的第一個專案**

* **歡迎視窗：** 當您開啟 Xcode 時，可能會看到一個歡迎視窗。在這裡您可以「建立一個新的 Xcode 專案」。
* **選擇範本：** Xcode 為不同平台（iOS、macOS、watchOS、tvOS）和應用程式類型（App、Framework、Game、Command Line Tool 等）提供各種範本。選擇最適合您專案的範本。對於初學者，通常從 iOS App 範本開始。
* **專案選項：** 選擇範本後，您將配置專案選項：
    * **Product Name：** 您的應用程式名稱。
    * **Team：** （需要 Apple Developer 帳戶）用於簽署應用程式的開發團隊。
    * **Organization Identifier：** 用於識別您組織的唯一字串（通常採用反向網域名稱格式，例如 `com.yourcompany`）。
    * **Bundle Identifier：** 根據 Organization Identifier 和 Product Name 自動生成（$ORGANIZATION_IDENTIFIER.$PRODUCT_NAME）。這在裝置和 App Store 上唯一識別您的應用程式。
    * **Interface：** 在 SwiftUI（現代聲明式 UI 框架）或 Storyboard（使用 segues 的視覺化 UI 設計）之間選擇。
    * **Lifecycle：** 對於 SwiftUI，在 App 和 UIKit App Delegate 之間選擇。
    * **Language：** 選擇 Swift（新專案推薦）或 Objective-C。
    * **Use Core Data：** 如果您需要管理結構化數據，請勾選。
    * **Include Tests：** 勾選以包含 Unit 和 UI 測試目標。
* **專案位置：** 選擇在 Mac 上儲存專案的位置。
* **建立專案：** 點擊「Create」，Xcode 將設定您的專案。

**3. 了解 Xcode 介面**

Xcode 的介面分為幾個關鍵區域：

* **工具列：** 位於視窗頂部，包含用於運行和停止應用程式、選擇方案和目的地以及存取各種工具的控制項。
* **導覽器區域：** （左側窗格）提供不同的導覽器來瀏覽您的專案：
    * **Project Navigator：** 顯示專案的檔案和檔案夾。
    * **Source Control Navigator：** 管理 Git 儲存庫。
    * **Issue Navigator：** 顯示錯誤、警告和其他問題。
    * **Test Navigator：** 管理和運行您的測試。
    * **Debug Navigator：** 協助除錯正在運行的應用程式。
    * **Breakpoint Navigator：** 管理您的中斷點。
    * **Report Navigator：** 顯示建置日誌、除錯工作階段等。
* **編輯器區域：** （中央窗格）您在此編寫和編輯程式碼、設計使用者介面以及檢視其他專案檔案。內容會根據在導覽器區域中選擇的檔案而變化。
* **檢查器區域：** （右側窗格）提供檢查器來檢視和編輯編輯器區域中選定項目的屬性。可用的檢查器會根據選定的項目而變化（例如，檔案屬性、UI 元素屬性、程式碼屬性）。
* **除錯區域：** （底部窗格）當您運行或除錯應用程式時出現，顯示控制台輸出、變數和除錯控制項。

您可以使用工具列中的按鈕顯示或隱藏導覽器、除錯和檢查器區域。

**4. 在 Xcode 中編碼**

* **原始碼編輯器：** 編寫程式碼的主要位置。它提供語法突顯、程式碼完成、即時問題報告和程式碼摺疊等功能。
* **Swift 和 Objective-C：** Xcode 支援 Swift 和 Objective-C。Swift 是現代、首選的 Apple 開發語言，以其安全性和速度著稱。Objective-C 是較舊但仍受支援的語言。
* **程式碼完成：** 當您輸入時，Xcode 會建議程式碼片段、類別名稱、方法名稱等，從而加快開發速度並減少錯誤。
* **語法突顯：** 程式碼的不同元素會以顏色標示，以提高可讀性。
* **即時問題報告：** Xcode 在您輸入時檢查程式碼中的語法錯誤和警告，並將其突顯顯示。
* **文件：** 您可以透過在程式碼編輯器中 Option-點擊類別、方法和屬性，或使用 Quick Help 檢查器，快速存取相關文件。

**5. 設計使用者介面**

Xcode 提供不同的方式來建置應用程式的使用者介面：

* **SwiftUI：** 一個聲明式框架，用於以更少的程式碼在所有 Apple 平台上建置 UI。您描述 UI 的結構和行為，SwiftUI 會隨著應用程式狀態的變化自動更新它。編輯器區域中的畫布提供 SwiftUI 視圖的即時預覽。
* **Interface Builder（Storyboards 和 .xib 檔案）：** 一個視覺化設計工具，您可以在畫布上拖放 UI 元素、排列它們並配置其屬性。
    * **Storyboards：** 表示多個畫面（View Controllers）和它們之間的轉場（Segues）。
    * **.xib 檔案：** 表示單個 UI 元素或 UI 的小部分。
* **Auto Layout：** 一個強大的基於約束的佈局系統，允許您定義 UI 元素應如何定位和調整大小的規則，確保您的介面在不同螢幕尺寸和方向上都能良好顯示。您可以在 Interface Builder 中視覺化地設定 Auto Layout 約束，或透過程式設計方式設定。
* **將 UI 連接到程式碼：**
    * **`@IBOutlet`：** 在 Interface Builder 中用於將 UI 元素（如按鈕、標籤、文字欄位）連接到程式碼中的變數，允許您以程式設計方式存取和修改它們。
    * **`@IBAction`：** 在 Interface Builder 中用於將 UI 元素（如按鈕、滑桿）連接到程式碼中的方法，允許您回應使用者互動。

**6. 除錯您的應用程式**

除錯是尋找和修復程式碼中錯誤的過程。Xcode 提供強大的除錯工具：

* **中斷點：** 您可以透過點擊原始碼編輯器中程式碼行旁邊的裝訂線來設定中斷點。當您的應用程式運行並到達中斷點時，執行會暫停，允許您檢查應用程式的狀態。
* **除錯區域：** 當執行在中斷點處暫停時，除錯區域會變為活動狀態，顯示：
    * **Variables View：** 顯示目前範圍內變數的值。
    * **Console：** 顯示來自應用程式的輸出（使用 `print()` 語句）和除錯資訊。
    * **Debug Bar：** 提供控制項以繼續執行、逐步執行、步入和步出程式碼。
* **除錯 Instruments：** Xcode 包含 Instruments，這是一個效能和分析工具，可協助您識別記憶體洩漏、過度 CPU 使用和渲染問題等問題。

**7. 測試您的應用程式**

測試對於確保應用程式穩定且按預期工作至關重要。Xcode 支援不同類型的測試：

* **Unit Tests：** 隔離測試程式碼的單個單元（例如，特定函數或類別），以驗證它們對於給定的輸入是否產生正確的輸出。
* **UI Tests：** 透過模擬使用者互動來測試應用程式的使用者介面，以確保 UI 行為符合預期，並且不同的畫面和元素正確顯示。
* **Test Navigator：** 使用 Test Navigator 來管理、運行和檢視測試結果。

**8. 運行您的應用程式**

您可以在兩個主要環境中運行應用程式：

* **模擬器：** Xcode 包含適用於各種 Apple 裝置和作業系統版本的模擬器。這是一種方便的方法，可以在不同的虛擬裝置上快速測試應用程式，而無需實體硬體。從工具列中的方案目的地下拉選單中選擇所需的模擬器，然後點擊 Run 按鈕。
* **在裝置上：** 要在實體 iPhone、iPad、Apple Watch 或 Apple TV 上測試應用程式，請將裝置連接到您的 Mac。Xcode 應該能識別該裝置，您可以在工具列中將其選為目的地。您需要免費或付費的 Apple Developer 帳戶才能在實體裝置上運行應用程式。

**9. 使用 Git 進行原始碼控制**

Xcode 具有對 Git（分散式版本控制系統）的整合支援：

* **建立本機儲存庫：** 建立新專案時，您可以選擇建立本機 Git 儲存庫。
* **提交變更：** 當您對程式碼進行變更時，可以將其提交到本機儲存庫，建立專案歷史的快照。
* **遠端儲存庫：** 您可以將本機儲存庫連接到遠端儲存庫（例如，在 GitHub、GitLab、Bitbucket 上），以備份程式碼、與他人協作以及管理專案的不同版本。
* **Source Control Navigator：** 使用 Source Control Navigator 來管理分支、拉取和推送變更以及檢視提交歷史記錄。

**10. 準備分發**

一旦您的應用程式準備就緒，您需要準備分發：

* **簽署與功能：** 在專案設定中配置應用程式的簽署憑證和識別碼。如果您的應用程式使用推送通知、App 內購買、iCloud 等功能，您還需要啟用這些功能。這需要 Apple Developer Program 會籍。
* **封存：** 在提交到 App Store 或在其外部分發之前，您需要建立應用程式的封存。請前往 `Product > Archive`。
* **驗證與分發：** 封存後，Organizer 視窗將會出現。從這裡，您可以根據 App Store 要求驗證應用程式，或以各種方式分發它（例如，App Store Connect、Ad Hoc、Enterprise）。

**有效使用 Xcode 的額外提示：**

* **學習鍵盤快捷鍵：** 掌握 Xcode 的鍵盤快捷鍵可以顯著加快工作流程。您可以在 Xcode 的偏好設定中或透過在線搜尋找到快捷鍵列表。
* **利用文件：** Xcode 擁有廣泛的內建文件。使用 Quick Help 檢查器或完整的 Developer Documentation 視窗（`Help > Developer Documentation`）來了解 API、框架和概念。
* **探索偏好設定：** Xcode 的偏好設定提供了許多編輯器、行為、按鍵綁定等方面的自訂選項。
* **使用物件庫：** 在使用 Interface Builder 時，物件庫（可從工具列或 `View > Library > Show Library` 存取）包含各種 UI 元素，您可以將其拖放到畫布上。
* **組織您的專案：** 在 Project Navigator 中使用群組來邏輯地組織您的檔案，使您的專案更易於瀏覽和維護。

本指南提供了使用 Xcode 的基礎理解。隨著您獲得更多經驗，您將在這個強大的 IDE 中發現更多功能和工作流程。編碼愉快！