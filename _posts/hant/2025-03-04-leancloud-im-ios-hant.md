---
audio: false
generated: true
lang: hant
layout: post
title: LeanCloud 即時 iOS SDK
translated: true
---

在你的 iOS 專案中使用 `pod 'AVOSCloudIM', '3.1.6.2'` 並使用 CocoaPods，請按照以下步驟進行。這假設你已經安裝了 CocoaPods 並且熟悉使用 Xcode 基本的 iOS 開發。

---

### 第 1 步：設置 CocoaPods（如果尚未完成）
如果你還沒有安裝 CocoaPods，請通過終端安裝：
```bash
sudo gem install cocoapods
```
驗證安裝：
```bash
pod --version
```

---

### 第 2 步：創建或打開你的 Xcode 專案
1. 打開你現有的 Xcode 專案或在 Xcode 中創建一個新的專案。
2. 現在先關閉 Xcode（我們稍後會用工作區重新打開）。

---

### 第 3 步：初始化 Podfile
1. 打開你的終端並導航到專案的根目錄（即 `.xcodeproj` 文件所在的位置）：
   ```bash
   cd /path/to/your/project
   ```
2. 如果你還沒有 Podfile，請通過運行以下命令創建一個：
   ```bash
   pod init
   ```
   這將在你的專案目錄中生成一個基本的 `Podfile`。

---

### 第 4 步：編輯 Podfile
1. 使用文本編輯器（例如 `nano`、`vim` 或任何代碼編輯器如 VS Code）打開 `Podfile`：
   ```bash
   open Podfile
   ```
2. 修改 `Podfile` 以包含版本為 `3.1.6.2` 的 `AVOSCloudIM` pod。以下是你的 `Podfile` 可能的樣子：
   ```ruby
   platform :ios, '9.0'  # 指定最低 iOS 版本（根據需要調整）
   use_frameworks!       # 可選：如果你的專案使用 Swift 或框架，請使用這個

   target 'YourAppName' do
     pod 'AVOSCloudIM', '3.1.6.2'  # 添加這行以包含 AVOSCloudIM 版本 3.1.6.2
   end
   ```
   - 用你的 Xcode 目標的實際名稱替換 `'YourAppName'`（通常是你的應用程序的名稱）。
   - `platform :ios, '9.0'` 行指定最低 iOS 版本；根據你的專案需求進行調整。
   - 如果你的專案使用 Swift 或 pod 需要動態框架，則需要 `use_frameworks!`。

3. 保存並關閉 `Podfile`。

---

### 第 5 步：安裝 Pod
1. 在終端中，從專案的根目錄運行以下命令：
   ```bash
   pod install
   ```
   - 這將下載並將 `AVOSCloudIM` 圖書館（版本 3.1.6.2）整合到你的專案中。
   - 如果成功，你會看到類似的輸出：
     ```
     Pod 安裝完成！Podfile 中有 X 個依賴項，總共安裝了 X 個 pod。
     ```

2. 如果遇到錯誤（例如找不到 pod），請確保版本 `3.1.6.2` 仍然在 CocoaPods 存儲庫中可用。較舊的版本可能不再受支持。你可以在 [CocoaPods.org](https://cocoapods.org) 下的 `AVOSCloudIM` 查看最新版本，或更新到較新版本（例如 `pod 'AVOSCloudIM', '~> 12.3'`）。

---

### 第 6 步：打開工作區
1. 安裝後，專案目錄中將創建一個 `.xcworkspace` 文件（例如 `YourAppName.xcworkspace`）。
2. 在 Xcode 中打開此文件：
   ```bash
   open YourAppName.xcworkspace
   ```
   - 從現在開始，始終使用 `.xcworkspace` 文件而不是 `.xcodeproj` 文件來處理你的專案。

---

### 第 7 步：在代碼中導入並使用 AVOSCloudIM
1. 在你的 Swift 或 Objective-C 文件中導入 `AVOSCloudIM` 模塊：
   - **Swift**：
     ```swift
     import AVOSCloudIM
     ```
   - **Objective-C**：
     ```objc
     #import <AVOSCloudIM/AVOSCloudIM.h>
     ```
2. 開始使用庫的功能。`AVOSCloudIM` 是 LeanCloud SDK 的一部分，通常用於即時消息傳遞。參考 [LeanCloud 文檔](https://leancloud.app/docs/) 以獲取具體的使用示例，例如設置聊天客戶端：
   - 示例（Swift）：
     ```swift
     let client = AVIMClient(clientId: "yourClientID")
     client.open { (succeeded, error) in
         if succeeded {
             print("已連接到 LeanCloud IM！")
         } else {
             print("錯誤：\(error?.localizedDescription ?? "未知")")
         }
     }
     ```

---

### 第 8 步：配置你的專案（如果需要）
- **應用程序密鑰和初始化**：LeanCloud SDK 通常需要應用程序 ID 和密鑰。在 `AppDelegate` 中添加此初始化代碼：
  - **Swift**：
    ```swift
    import AVOSCloud
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AVOSCloud.setApplicationId("yourAppID", clientKey: "yourAppKey")
        return true
    }
    ```
  - 用你的 LeanCloud 帳戶的憑證替換 `"yourAppID"` 和 `"yourAppKey"`。
- **權限**：確保你的應用程序在 `Info.plist` 中具有必要的權限（例如互聯網訪問）：
  ```xml
  <key>NSAppTransportSecurity</key>
  <dict>
      <key>NSAllowsArbitraryLoads</key>
      <true/>
  </dict>
  ```

---

### 注意事項
- **版本特定性**：使用 `pod 'AVOSCloudIM', '3.1.6.2'` 將你鎖定到該特定版本。如果你想要靈活性以進行次要更新，請使用 `~>`（例如 `pod 'AVOSCloudIM', '~> 3.1.6'` 允許更新如 3.1.6.1 但不允許 3.2）。
- **故障排除**：如果 `pod install` 失敗，請嘗試：
  - 更新 CocoaPods：`sudo gem install cocoapods`
  - 清理快取：`pod cache clean --all`
  - 運行 `pod repo update` 以刷新本地 CocoaPods 規範存儲庫。
- **LeanCloud SDK**：由於 `AVOSCloudIM` 是 LeanCloud 的一部分，請確保你遵循他們的設置指南以進行其他配置（例如在平台上註冊）。

---

就這樣！你現在已經將 `AVOSCloudIM` 版本 3.1.6.2 集成到你的 iOS 專案中。在 Xcode 中構建並運行你的應用程序以測試它。如果你需要幫助使用特定的 LeanCloud 功能，請告訴我！