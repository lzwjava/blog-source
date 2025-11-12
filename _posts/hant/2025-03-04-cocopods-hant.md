---
audio: false
generated: true
lang: hant
layout: post
title: 在 iOS 專案中使用 CocoaPods 管理依賴項
translated: true
type: note
---

讓我們深入探討如何使用 CocoaPods、建立 Podfile、管理函式庫，以及一些熱門的 pod 推薦！我將逐步拆解說明，讓內容清晰且具可操作性。

### 什麼是 CocoaPods 和 Podfile？
CocoaPods 是一個專為 Swift 和 Objective-C 項目設計的依賴管理工具，廣泛應用於 iOS/macOS 開發。它能簡化向專案添加函式庫（稱為 "pods"）的流程。`Podfile` 是一個設定檔案，你可以在其中指定專案所需的 pods、它們的版本，以及它們如何與你的目標整合。

### 如何使用 CocoaPods 並建立 Podfile
1. **安裝 CocoaPods**（如果尚未安裝）：
   - 開啟 Terminal 並執行：
     ```bash
     sudo gem install cocoapods
     ```
   - 驗證安裝：
     ```bash
     pod --version
     ```

2. **設定 Podfile**：
   - 在 Terminal 中導航至你的 Xcode 專案目錄：
     ```bash
     cd /path/to/your/project
     ```
   - 建立 Podfile：
     ```bash
     pod init
     ```
   - 這會在專案資料夾中生成一個基本的 `Podfile`。

3. **編輯 Podfile**：
   - 在文字編輯器中開啟 `Podfile`（例如 `open Podfile`）。一個基本的 Podfile 如下所示：
     ```ruby
     platform :ios, '13.0'  # 指定最低 iOS 版本
     use_frameworks!        # 使用動態框架而非靜態函式庫

     target 'YourAppName' do
       # Pods 放在這裡
       pod 'Alamofire', '~> 5.6'  # 範例 pod
     end

     post_install do |installer|
       installer.pods_project.targets.each do |target|
         target.build_configurations.each do |config|
           config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = '13.0'
         end
       end
     end
     ```
   - 將 `'YourAppName'` 替換為你的 Xcode 目標名稱。
   - 在 `target` 區塊下添加 pods（更多熱門 pods 將在後續說明）。

4. **安裝 Pods**：
   - 在 Terminal 中執行：
     ```bash
     pod install
     ```
   - 這會下載指定的 pods 並建立一個 `.xcworkspace` 檔案。從現在開始，請在 Xcode 中開啟此工作區（而非 `.xcodeproj`）。

5. **在程式碼中使用 Pods**：
   - 在 Swift 檔案中導入 pod：
     ```swift
     import Alamofire  // 以 Alamofire pod 為例
     ```
   - 按照該函式庫的文件（通常可在 GitHub 或 pod 的 CocoaPods 頁面找到）使用該庫。

---

### 使用函式庫（Pods）及關鍵 Podfile 概念
- **指定 Pods**：
  - 添加帶有版本約束的 pod：
    ```ruby
    pod 'Alamofire', '~> 5.6'  # ~> 表示「直到下一個主要版本」
    pod 'SwiftyJSON'           # 未指定版本 = 使用最新版
    ```
- **多個目標**：
  - 如果專案有多個目標（例如應用程式和擴充功能）：
    ```ruby
    target 'YourAppName' do
      pod 'Alamofire'
    end

    target 'YourAppExtension' do
      pod 'SwiftyJSON'
    end
    ```
- **環境變數（例如 `COCOAPODS_DISABLE_STATS`）**：
  - CocoaPods 預設會發送匿名統計資料。若要停用：
    ```bash
    export COCOAPODS_DISABLE_STATS=1
    pod install
    ```
  - 將此添加到你的 `~/.zshrc` 或 `~/.bashrc` 中以永久設定。
- **抑制警告**：
  - 若要靜音 pod 警告：
    ```ruby
    inhibit_all_warnings!
    ```

---

### 推薦的熱門 Pods
以下是一些基於實用性和社群採用度而廣受歡迎的 iOS 開發 pods：

1. **Alamofire**：
   - 用途：網路請求（讓 HTTP 請求變得更簡單）。
   - Podfile：`pod 'Alamofire', '~> 5.6'`
   - 原因：簡化 URL 請求、JSON 處理等。

2. **SwiftyJSON**：
   - 用途：JSON 解析。
   - Podfile：`pod 'SwiftyJSON'`
   - 原因：比原生 Swift 字典更安全、更簡潔地處理 JSON。

3. **SnapKit**：
   - 用途：使用更簡潔的語法進行 Auto Layout。
   - Podfile：`pod 'SnapKit'`
   - 原因：非常適合無需 storyboard 的程式化 UI。

4. **Kingfisher**：
   - 用途：圖片下載與快取。
   - Podfile：`pod 'Kingfisher'`
   - 原因：能高效地將圖片載入到 UIImageViews。

5. **RealmSwift**：
   - 用途：本地資料庫儲存。
   - Podfile：`pod 'RealmSwift'`
   - 原因：在許多使用情境下比 Core Data 更快速且直觀。

6. **Firebase**（模組化）：
   - 用途：後端服務（分析、推播通知等）。
   - Podfile 範例：
     ```ruby
     pod 'Firebase/Analytics'
     pod 'Firebase/Messaging'
     ```
   - 原因：提供全面的應用程式分析和用戶互動套件。

7. **Lottie**：
   - 用途：動畫圖形。
   - Podfile：`pod 'lottie-ios'`
   - 原因：可輕鬆添加來自 Adobe After Effects 的高品質動畫。

---

### 疑難排解提示
- **Pod Install 失敗**：執行 `pod repo update`，然後再次執行 `pod install`。
- **版本衝突**：指定確切版本（例如 `pod 'Alamofire', '5.6.4'`）或使用 `pod update`。
- **清除建置**：安裝 pods 後，在 Xcode 中清除專案（`Cmd + Shift + K`）。

---

### 包含熱門 Pods 的範例 Podfile
以下是一個結合上述部分 pods 的實用範例：
```ruby
platform :ios, '13.0'
use_frameworks!

target 'MyAwesomeApp' do
  pod 'Alamofire', '~> 5.6'      # 網路請求
  pod 'SwiftyJSON'               # JSON 解析
  pod 'SnapKit'                  # Auto Layout
  pod 'Kingfisher'               # 圖片載入

  post_install do |installer|
    installer.pods_project.targets.each do |target|
      target.build_configurations.each do |config|
        config.build_settings['IPHONEOS_DEPLOYMENT_TARGET'] = '13.0'
      end
    end
  end
end
```

執行 `pod install`，開啟 `.xcworkspace`，即可開始編碼！

---

如果你希望深入了解任何特定的 pod 或步驟，請告訴我！你正在開發什麼類型的應用程式？這或許能幫助我提供更貼合的推薦。