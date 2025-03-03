---
audio: false
generated: true
lang: hant
layout: post
title: 使用 AFNetworking 在 iOS
translated: true
---

看來你是指在使用 CocoaPods 這個流行的 Swift 和 Objective-C 專案依賴管理器將 AFNetworking 圖書館版本 2.5.4 集成到 iOS 專案中。以下是如何在專案中使用 `pod 'AFNetworking', '2.5.4'` 的逐步指南：

### 前提條件
1. **安裝 CocoaPods**：如果你還沒有安裝 CocoaPods，請在終端機中運行以下命令來安裝：
   ```bash
   sudo gem install cocoapods
   ```
2. **Xcode 專案**：確保你有一個現有的 Xcode 專案，你想要在其中添加 AFNetworking。

### 使用 `pod 'AFNetworking', '2.5.4'` 的步驟

1. **導航到專案目錄**
   打開終端機並切換到包含 Xcode 專案（`.xcodeproj` 文件）的目錄：
   ```bash
   cd /path/to/your/project
   ```

2. **初始化 Podfile**
   如果你還沒有 `Podfile`，請運行以下命令來創建一個：
   ```bash
   pod init
   ```
   這將在專案目錄中生成一個 `Podfile`。

3. **編輯 Podfile**
   使用文本編輯器（例如 `nano Podfile` 或使用任何代碼編輯器如 VS Code）打開 `Podfile`。在應用程式的 `target` 塊中添加以下行：
   ```ruby
   target 'YourAppTargetName' do
     # 如果不想使用動態框架，請註釋掉下一行
     use_frameworks!

     # 添加這一行以指定 AFNetworking 版本 2.5.4
     pod 'AFNetworking', '2.5.4'
   end
   ```
   將 `'YourAppTargetName'` 替換為應用程式的實際目標名稱（你可以在 Xcode 中的專案設置中找到）。

   範例 `Podfile`：
   ```ruby
   platform :ios, '9.0'

   target 'MyApp' do
     use_frameworks!
     pod 'AFNetworking', '2.5.4'
   end
   ```

4. **安裝 Pod**
   保存 `Podfile`，然後在終端機中運行以下命令來安裝 AFNetworking 2.5.4：
   ```bash
   pod install
   ```
   這將下載指定版本的 AFNetworking 並在專案中設置它。如果成功，你會看到一條成功的消息。

5. **打開工作區**
   安裝後，CocoaPods 會創建一個 `.xcworkspace` 文件。打開這個文件（例如 `MyApp.xcworkspace`）而不是原始的 `.xcodeproj` 文件：
   ```bash
   open MyApp.xcworkspace
   ```

6. **導入和使用 AFNetworking**
   在你的 Objective-C 或 Swift 代碼中導入 AFNetworking 並開始使用它。由於版本 2.5.4 較舊且用 Objective-C 寫成，以下是如何使用它的方法：

   - **Objective-C**：
     在你的 `.h` 或 `.m` 文件中：
     ```objective-c
     #import <AFNetworking/AFNetworking.h>

     - (void)makeRequest {
         AFHTTPRequestOperationManager *manager = [AFHTTPRequestOperationManager manager];
         [manager GET:@"https://api.example.com/data"
           parameters:nil
              success:^(AFHTTPRequestOperation *operation, id responseObject) {
                  NSLog(@"Success: %@", responseObject);
              }
              failure:^(AFHTTPRequestOperation *operation, NSError *error) {
                  NSLog(@"Error: %@", error);
              }];
     }
     ```

   - **Swift（與橋接標頭）**：
     如果你使用 Swift，請創建一個橋接標頭以使用這個 Objective-C 圖書館：
     - 添加一個名為 `YourApp-Bridging-Header.h` 的文件（例如 `MyApp-Bridging-Header.h`）。
     - 在橋接標頭中添加：
       ```objective-c
       #import <AFNetworking/AFNetworking.h>
       ```
     - 在 Xcode 中，轉到構建設置 > “Objective-C 橋接標頭” 並設置到你的橋接標頭的路徑（例如 `MyApp/MyApp-Bridging-Header.h`）。
     - 然後在你的 Swift 文件中：
       ```swift
       func makeRequest() {
           let manager = AFHTTPRequestOperationManager()
           manager.get("https://api.example.com/data",
                       parameters: nil,
                       success: { (operation, response) in
                           print("Success: \(response)")
                       },
                       failure: { (operation, error) in
                           print("Error: \(error)")
                       })
       }
       ```

7. **構建和運行**
   在 Xcode 中構建你的專案（`Cmd + B`）以確保一切正常設置。如果遇到錯誤，請檢查 Podfile 語法或確保打開了正確的工作區。

### 注意事項
- **版本 2.5.4**：這是一個較舊的 AFNetworking 版本（約於 2015 年發布）。截至 2025 年 3 月，最新版本可能會更新（例如 4.x 或 5.x）。除非你需要 2.5.4 以進行兼容性，否則考慮使用 `pod 'AFNetworking'` 而不指定版本以獲取最新版本。
- **廢棄**：AFNetworking 的較舊 API（例如 `AFHTTPRequestOperationManager`）在較新版本中已被廢棄。對於現代專案，可能值得探索像 Alamofire 這樣的 Swift 替代方案。
- **平台**：確保你的 `Podfile` 指定了一個與 AFNetworking 2.5.4 兼容的平台版本（例如 `platform :ios, '9.0'`）。

如果你遇到具體問題（例如安裝錯誤或代碼示例無法工作），請告訴我，我將進一步排除故障！你的下一步或問題是什麼？