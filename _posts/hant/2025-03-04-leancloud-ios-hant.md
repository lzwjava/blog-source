---
audio: false
generated: true
lang: hant
layout: post
title: LeanCloud iOS SDK
translated: true
type: note
---

若要在 iOS 專案中使用 `pod 'AVOSCloud', '3.1.6.2'`，您指的是透過 CocoaPods（iOS 專案的依賴管理工具）整合 AVOSCloud SDK（很可能是 LeanCloud 的雲端服務 SDK）。以下是設定步驟：

---

### 前置準備
1. **安裝 CocoaPods**：若尚未安裝 CocoaPods，請先透過終端機執行以下指令安裝：
   ```bash
   sudo gem install cocoapods
   ```
2. **Xcode 專案**：請確保您已有現成的 Xcode iOS 專案。

---

### 使用 `pod 'AVOSCloud', '3.1.6.2'` 的步驟

1. **導航至專案目錄**：
   開啟終端機並進入包含 `.xcodeproj` 檔案的目錄：
   ```bash
   cd /path/to/your/project
   ```

2. **初始化 Podfile**（若尚未建立）：
   執行以下指令建立 `Podfile`：
   ```bash
   pod init
   ```

3. **編輯 Podfile**：
   用文字編輯器開啟 `Podfile`（例如 `nano Podfile` 或 `open Podfile`），並加入指定版本 `3.1.6.2` 的 `AVOSCloud` pod。您的 `Podfile` 應類似以下內容：
   ```ruby
   platform :ios, '9.0'  # 指定最低 iOS 版本（請根據需求調整）

   target 'YourAppName' do
     use_frameworks!
     pod 'AVOSCloud', '3.1.6.2'  # 加入此行以引入 AVOSCloud SDK
   end
   ```
   - 請將 `'YourAppName'` 替換為您 Xcode target 的實際名稱。
   - 若使用 Swift 或動態框架，必須保留 `use_frameworks!`。

4. **安裝 Pod**：
   儲存 `Podfile` 後，在終端機執行以下指令以安裝指定版本的 AVOSCloud：
   ```bash
   pod install
   ```
   - 此指令將下載 `3.1.6.2` 版的 AVOSCloud SDK，並為您的專案建立 `.xcworkspace` 檔案。

5. **開啟 Workspace**：
   安裝完成後，若原先開啟了 `.xcodeproj` 請先關閉，改為開啟新建立的 `.xcworkspace` 檔案：
   ```bash
   open YourAppName.xcworkspace
   ```

6. **在程式碼中引入並使用 AVOSCloud**：
   - Objective-C：
     ```objc
     #import <AVOSCloud/AVOSCloud.h>

     - (void)example {
         [AVOSCloud setApplicationId:@"your_app_id" clientKey:@"your_client_key"];
         AVObject *testObject = [AVObject objectWithClassName:@"TestObject"];
         [testObject setObject:@"Hello" forKey:@"message"];
         [testObject save];
     }
     ```
   - Swift：
     ```swift
     import AVOSCloud

     func example() {
         AVOSCloud.setApplicationId("your_app_id", clientKey: "your_client_key")
         let testObject = AVObject(className: "TestObject")
         testObject["message"] = "Hello"
         try? testObject.save()
     }
     ```
   - 請將 `"your_app_id"` 與 `"your_client_key"` 替換為您在 LeanCloud 儀表板中取得的應用憑證。

7. **設定應用憑證**：
   - 請至 [LeanCloud](https://leancloud.app)（或相關 AVOSCloud 服務供應商）註冊帳號。
   - 從應用程式設定中取得 `App ID` 與 `Client Key`，並填入程式碼（如上所示）。

8. **建置並執行**：
   在 Xcode 中建置專案（`Cmd + B`）以確認設定無誤。若出現錯誤，請檢查 Podfile 語法或網路連線。

---

### 注意事項
- **版本指定**：透過指定 `'3.1.6.2'`，您將鎖定該特定版本的 SDK。截至 2025 年 3 月 3 日，此版本可能已過時。若需使用最新版本，只需寫 `pod 'AVOSCloud'` 而不加版本號。
- **相容性**：請確保 `3.1.6.2` 版本支援您的 iOS 部署目標（例如 iOS 9.0 或更高版本）。詳情請查閱 [LeanCloud 文件](https://leancloud.app/docs)。
- **Pod 更新**：若需更新 CocoaPods 或疑難排解，請執行：
  ```bash
  pod update
  ```
- **疑難排解**：若 `pod install` 失敗，請嘗試：
  ```bash
  pod repo update
  pod install --verbose
  ```

---

如需 AVOSCloud 特定功能（如推播通知、即時通訊）的整合協助，歡迎隨時提出！