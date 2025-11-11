---
audio: false
generated: true
lang: hant
layout: post
title: LeanCloud 實時 iOS SDK
translated: true
type: note
---

若要在你的 iOS 專案中使用 CocoaPods 來安裝 `pod 'AVOSCloudIM', '3.1.6.2'`，請按照以下步驟操作。這假設你已經安裝了 CocoaPods，並且熟悉使用 Xcode 進行基本的 iOS 開發。

---

### 步驟 1：設定 CocoaPods（如果尚未完成）
如果你尚未安裝 CocoaPods，請透過終端機安裝：
```bash
sudo gem install cocoapods
```
驗證安裝：
```bash
pod --version
```

---

### 步驟 2：建立或開啟你的 Xcode 專案
1. 開啟你現有的 Xcode 專案，或在 Xcode 中建立一個新專案。
2. 暫時關閉 Xcode（我們稍後會使用 workspace 重新開啟）。

---

### 步驟 3：初始化 Podfile
1. 開啟終端機並導航至你的專案根目錄（即 `.xcodeproj` 檔案所在的位置）：
   ```bash
   cd /path/to/your/project
   ```
2. 如果你還沒有 Podfile，請執行以下指令來建立：
   ```bash
   pod init
   ```
   這會在專案目錄中生成一個基本的 `Podfile`。

---

### 步驟 4：編輯 Podfile
1. 在文字編輯器（例如 `nano`、`vim` 或任何程式碼編輯器如 VS Code）中開啟 `Podfile`：
   ```bash
   open Podfile
   ```
2. 修改 `Podfile` 以包含版本為 `3.1.6.2` 的 `AVOSCloudIM` pod。以下是你的 `Podfile` 可能看起來的樣子：
   ```ruby
   platform :ios, '9.0'  # 指定最低 iOS 版本（根據需要調整）
   use_frameworks!       # 可選：如果你的專案使用 Swift 或框架，請使用此指令

   target 'YourAppName' do
     pod 'AVOSCloudIM', '3.1.6.2'  # 加入此行以包含 AVOSCloudIM 版本 3.1.6.2
   end
   ```
   - 將 `'YourAppName'` 替換為你 Xcode target 的實際名稱（通常是你的應用程式名稱）。
   - `platform :ios, '9.0'` 這行指定了最低 iOS 版本；請根據你的專案需求進行調整。
   - 如果你的專案使用 Swift 或 pod 需要動態框架，則需要 `use_frameworks!`。

3. 儲存並關閉 `Podfile`。

---

### 步驟 5：安裝 Pod
1. 在終端機中，從你的專案根目錄執行以下指令：
   ```bash
   pod install
   ```
   - 這會下載並將 `AVOSCloudIM` 函式庫（版本 3.1.6.2）整合到你的專案中。
   - 如果成功，你將看到類似以下的輸出：  
     ```
     Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
     ```

2. 如果你遇到錯誤（例如找不到 pod），請確保版本 `3.1.6.2` 在 CocoaPods 儲存庫中仍然可用。舊版本可能不再受支援。你可以在 [CocoaPods.org](https://cocoapods.org) 上查看 `AVOSCloudIM` 的最新版本，或更新到較新的版本（例如 `pod 'AVOSCloudIM', '~> 12.3'`）。

---

### 步驟 6：開啟 Workspace
1. 安裝完成後，你的專案目錄中會建立一個 `.xcworkspace` 檔案（例如 `YourAppName.xcworkspace`）。
2. 在 Xcode 中開啟此檔案：
   ```bash
   open YourAppName.xcworkspace
   ```
   - 從現在開始，請始終使用 `.xcworkspace` 檔案來處理你的專案，而不是 `.xcodeproj` 檔案。

---

### 步驟 7：在程式碼中匯入並使用 AVOSCloudIM
1. 在你的 Swift 或 Objective-C 檔案中，匯入 `AVOSCloudIM` 模組：
   - **Swift**：
     ```swift
     import AVOSCloudIM
     ```
   - **Objective-C**：
     ```objc
     #import <AVOSCloudIM/AVOSCloudIM.h>
     ```
2. 開始使用該函式庫的功能。`AVOSCloudIM` 是 LeanCloud SDK 的一部分，通常用於即時通訊。請參考 [LeanCloud 文件](https://leancloud.app/docs/) 以獲取具體的使用範例，例如設定聊天客戶端：
   - 範例（Swift）：
     ```swift
     let client = AVIMClient(clientId: "yourClientID")
     client.open { (succeeded, error) in
         if succeeded {
             print("Connected to LeanCloud IM!")
         } else {
             print("Error: \\(error?.localizedDescription ?? "Unknown")")
         }
     }
     ```

---

### 步驟 8：設定你的專案（如果需要）
- **App Key 和初始化**：LeanCloud SDK 通常需要應用程式 ID 和金鑰。請在 `AppDelegate` 中加入初始化程式碼：
  - **Swift**：
    ```swift
    import AVOSCloud
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AVOSCloud.setApplicationId("yourAppID", clientKey: "yourAppKey")
        return true
    }
    ```
  - 將 `"yourAppID"` 和 `"yourAppKey"` 替換為來自你的 LeanCloud 帳戶的憑證。
- **權限**：確保你的應用程式在 `Info.plist` 中具有必要的權限（例如網路存取）：
  ```xml
  <key>NSAppTransportSecurity</key>
  <dict>
      <key>NSAllowsArbitraryLoads</key>
      <true/>
  </dict>
  ```

---

### 注意事項
- **版本指定**：使用 `pod 'AVOSCloudIM', '3.1.6.2'` 會將你鎖定在該確切版本。如果你希望對小更新有靈活性，請使用 `~>`（例如 `pod 'AVOSCloudIM', '~> 3.1.6'` 允許像 3.1.6.1 這樣的更新，但不允許 3.2）。
- **疑難排解**：如果 `pod install` 失敗，請嘗試：
  - 更新 CocoaPods：`sudo gem install cocoapods`
  - 清除快取：`pod cache clean --all`
  - 執行 `pod repo update` 以重新整理本地的 CocoaPods spec 儲存庫。
- **LeanCloud SDK**：由於 `AVOSCloudIM` 是 LeanCloud 的一部分，請確保你遵循他們的設定指南以進行其他配置（例如在他們的平台上註冊）。

---

就是這樣！你現在已經將 `AVOSCloudIM` 版本 3.1.6.2 整合到你的 iOS 專案中。在 Xcode 中建置並運行你的應用程式來進行測試。如果你需要有關特定 LeanCloud 功能的幫助，請告訴我！