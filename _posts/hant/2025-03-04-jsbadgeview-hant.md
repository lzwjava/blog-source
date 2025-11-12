---
audio: false
generated: true
lang: hant
layout: post
title: 在 iOS 中使用 JSBadgeView
translated: true
type: note
---

看來您正在討論如何透過 CocoaPods（一個專為 Swift 和 Objective-C 項目設計的熱門依賴管理工具）將 `JSBadgeView` pod（版本 1.4.1）整合到 iOS 專案中。我將逐步引導您如何在專案中使用這個 pod。

### 前置準備
1. **安裝 CocoaPods**：請確認您的系統已安裝 CocoaPods。若尚未安裝，請執行以下指令：
   ```bash
   sudo gem install cocoapods
   ```
2. **Xcode 專案**：您需要有一個現有的 Xcode 專案，以便將 `JSBadgeView` 加入其中。

### 使用 `pod 'JSBadgeView', '1.4.1'` 的步驟

1. **導航至專案目錄**：
   開啟終端機並切換至包含您 Xcode 專案（`.xcodeproj` 檔案）的目錄：
   ```bash
   cd /path/to/your/project
   ```

2. **初始化 CocoaPods（若尚未執行）**：
   如果您的專案還沒有 `Podfile`，請透過以下指令建立：
   ```bash
   pod init
   ```
   這會在您的專案目錄中生成一個 `Podfile`。

3. **編輯 Podfile**：
   使用文字編輯器（例如 `nano`、`vim` 或任何 IDE）開啟 `Podfile`，並在您的 target 下加入 `JSBadgeView` pod。例如：
   ```ruby
   platform :ios, '9.0' # 請指定您的部署目標版本

   target 'YourProjectName' do
     use_frameworks! # 如果您的專案使用 Swift 或框架則需要此行
     pod 'JSBadgeView', '1.4.1'
   end
   ```
   請將 `'YourProjectName'` 替換為您 Xcode target 的實際名稱。

4. **安裝 Pod**：
   儲存 `Podfile`，然後在終端機中執行以下指令以安裝 pod：
   ```bash
   pod install
   ```
   這會下載 `JSBadgeView` 版本 1.4.1 並將其設定到您的專案中。若成功，您將看到 pod 已安裝的提示訊息。

5. **開啟 Workspace**：
   安裝完成後，CocoaPods 會建立一個 `.xcworkspace` 檔案。請在 Xcode 中開啟此檔案（而非 `.xcodeproj`）：
   ```bash
   open YourProjectName.xcworkspace
   ```

6. **在程式碼中導入並使用 JSBadgeView**：
   - 若您使用 **Objective-C**，請在檔案中導入標頭檔：
     ```objective-c
     #import <JSBadgeView/JSBadgeView.h>
     ```
   - 若您使用 **Swift**，且 `Podfile` 中包含 `use_frameworks!`，則無需導入，直接使用類別即可。
   - 使用範例（Objective-C）：
     ```objective-c
     JSBadgeView *badgeView = [[JSBadgeView alloc] initWithParentView:someView alignment:JSBadgeViewAlignmentTopRight];
     badgeView.badgeText = @"5"; // 將徽章文字設為 "5"
     ```
   - 使用範例（Swift）：
     ```swift
     let badgeView = JSBadgeView(parentView: someView, alignment: .topRight)
     badgeView.badgeText = "5"
     ```

7. **建置並執行**：
   在 Xcode 中建置您的專案（`Cmd + B`）以確認所有設定無誤，然後在模擬器或裝置上執行。

### 注意事項
- **JSBadgeView**：這是一個用於在 UI 元素（如按鈕或標籤列）上添加徽章視圖（例如通知氣泡）的函式庫。請查閱其 [GitHub 頁面](https://github.com/JaviSoto/JSBadgeView)以獲取詳細文檔，但請注意版本 1.4.1 發佈於 2016 年，可能不支援最新的 iOS 功能。
- **疑難排解**：
  - 若 `pod install` 失敗，請確認您的 CocoaPods 版本是否為最新：
    ```bash
    pod update
    ```
  - 若遇到相容性錯誤，請檢查您的 `platform :ios` 版本是否與專案的部署目標版本一致。
- **版本 1.4.1**：此設定會將 pod 鎖定在該特定版本。若您希望使用最新版本，可省略版本號：`pod 'JSBadgeView'`。

如果您需要具體的實作協助或遇到任何問題，請隨時告知！