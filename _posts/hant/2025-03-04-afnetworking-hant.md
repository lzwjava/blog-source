---
audio: false
generated: true
lang: hant
layout: post
title: 在 iOS 中使用 AFNetworking
translated: true
type: note
---

看來您正在討論如何透過 CocoaPods（Swift 和 Objective-C 專案常用的依賴管理工具）將 AFNetworking 函式庫版本 2.5.4 整合到 iOS 專案中。以下是在專案中使用 `pod 'AFNetworking', '2.5.4'` 的逐步指南：

### 前置準備
1. **安裝 CocoaPods**：若尚未安裝 CocoaPods，請在終端機執行以下指令：
   ```bash
   sudo gem install cocoapods
   ```
2. **Xcode 專案**：請確認您已有要加入 AFNetworking 的現有 Xcode 專案。

### 使用 `pod 'AFNetworking', '2.5.4'` 的步驟

1. **導航至專案目錄**  
   開啟終端機並切換至包含 Xcode 專案（`.xcodeproj` 檔案）的目錄：
   ```bash
   cd /path/to/your/project
   ```

2. **初始化 Podfile**  
   若尚未有 `Podfile`，請透過以下指令建立：
   ```bash
   pod init
   ```
   這會在專案目錄中產生 `Podfile`。

3. **編輯 Podfile**  
   用文字編輯器開啟 `Podfile（例如 `nano Podfile` 或使用 VS Code 等程式編輯器）。在應用程式的 `target` 區塊內加入以下行：
   ```ruby
   target 'YourAppTargetName' do
     # 若不想使用動態框架，請註解下一行
     use_frameworks!

     # 加入此行以指定 AFNetworking 版本 2.5.4
     pod 'AFNetworking', '2.5.4'
   end
   ```
   請將 `'YourAppTargetName'` 替換為應用程式的實際目標名稱（可在 Xcode 的專案設定中找到）。

   `Podfile` 範例：
   ```ruby
   platform :ios, '9.0'

   target 'MyApp' do
     use_frameworks!
     pod 'AFNetworking', '2.5.4'
   end
   ```

4. **安裝 Pod**  
   儲存 `Podfile`，接著在終端機執行以下指令來安裝 AFNetworking 2.5.4：
   ```bash
   pod install
   ```
   此指令會下載指定版本的 AFNetworking 並設定至專案。若運作正常，您將看到成功訊息。

5. **開啟 Workspace**  
   安裝完成後，CocoaPods 會建立 `.xcworkspace` 檔案。請在 Xcode 中開啟此檔案（例如 `MyApp.xcworkspace`），而非原始的 `.xcodeproj` 檔案：
   ```bash
   open MyApp.xcworkspace
   ```

6. **匯入並使用 AFNetworking**  
   在 Objective-C 或 Swift 程式碼中匯入 AFNetworking 並開始使用。由於 2.5.4 是較舊版本且以 Objective-C 撰寫，使用方法如下：

   - **Objective-C**：
     在 `.h` 或 `.m` 檔案中：
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

   - **Swift（使用 Bridging Header）**：  
     若使用 Swift，需建立 bridging header 來使用此 Objective-C 函式庫：
     - 新增名為 `YourApp-Bridging-Header.h` 的檔案（例如 `MyApp-Bridging-Header.h`）。
     - 在 bridging header 中加入：
       ```objective-c
       #import <AFNetworking/AFNetworking.h>
       ```
     - 在 Xcode 中，前往 Build Settings > "Objective-C Bridging Header" 並設定 bridging header 的路徑（例如 `MyApp/MyApp-Bridging-Header.h`）。
     - 接著在 Swift 檔案中：
       ```swift
       func makeRequest() {
           let manager = AFHTTPRequestOperationManager()
           manager.get("https://api.example.com/data", 
                       parameters: nil, 
                       success: { (operation, response) in
                           print("Success: \\(response)")
                       }, 
                       failure: { (operation, error) in
                           print("Error: \\(error)")
                       })
       }
       ```

7. **建置並執行**  
   在 Xcode 中建置專案（`Cmd + B`）以確認所有設定正確。若遇到錯誤，請檢查 Podfile 語法或確認是否開啟正確的 workspace。

### 注意事項
- **版本 2.5.4**：這是 AFNetworking 的舊版（約 2015 年發布）。截至 2025 年 3 月，最新版本可能已更新至 4.x 或 5.x。除非因相容性需求必須使用 2.5.4，否則建議使用 `pod 'AFNetworking'`（不指定版本）以取得最新版。
- **過時 API**：AFNetworking 的舊版 API（如 `AFHTTPRequestOperationManager`）在新版本中已被標記為過時。對於現代專案，可考慮使用 Alamofire（Swift 替代方案）等函式庫。
- **平台相容性**：請確認 `Podfile` 指定的平台版本與 AFNetworking 2.5.4 相容（例如 `platform :ios, '9.0'`）。

若遇到特定問題（例如安裝錯誤或程式範例無法運作），請告知我以進一步排查！您的下一步或疑問是什麼？