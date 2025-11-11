---
audio: false
generated: true
lang: hant
layout: post
title: 在 iOS 中使用 MBProgressHUD
translated: true
type: note
---

看來您是想了解如何在 iOS 專案中透過 CocoaPods 的 Podfile 使用 `MBProgressHUD` 函式庫（版本 `0.9.1`）。讓我為您逐步說明整個流程。

### 什麼是 MBProgressHUD？
`MBProgressHUD` 是一個廣受歡迎的 iOS 第三方函式庫，能輕鬆顯示包含活動指示器、進度條或自訂視圖的 HUD（抬頭顯示器），常用於呈現載入狀態或簡短訊息。

### 使用 `pod 'MBProgressHUD', '0.9.1'` 的步驟

#### 1. **安裝 CocoaPods（若尚未安裝）**
CocoaPods 是 iOS 專案的相依性管理工具。若未安裝，請在終端機執行：
```bash
sudo gem install cocoapods
```

#### 2. **設定 Podfile**
- 在終端機中導航至您的 Xcode 專案目錄：
  ```bash
  cd /path/to/your/project
  ```
- 若尚未建立 Podfile，請執行：
  ```bash
  pod init
  ```
- 用文字編輯器開啟 `Podfile`（例如 `nano Podfile` 或 `open Podfile`）

#### 3. **在 Podfile 中加入 MBProgressHUD**
在 `Podfile` 中的應用程式 target 區塊內加入 `MBProgressHUD` 版本 `0.9.1`，內容應類似：
```ruby
platform :ios, '9.0'  # 請指定您的部署目標版本

target 'YourAppName' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- 請將 `'YourAppName'` 替換為您的 Xcode target 實際名稱
- `platform :ios, '9.0'` 設定最低 iOS 版本，請根據專案需求調整

#### 4. **安裝 Pod**
- 儲存 `Podfile` 後在終端機執行：
  ```bash
  pod install
  ```
- 此命令將下載並整合 `MBProgressHUD` 版本 `0.9.1` 到您的專案中。若成功，您將看到確認安裝的輸出訊息

#### 5. **開啟 Workspace**
- 安裝完成後，請關閉您的 Xcode 專案（若已開啟），改為開啟新生成的 `.xcworkspace` 檔案（例如 `YourAppName.xcworkspace`），而非原本的 `.xcodeproj` 檔案。CocoaPods 會生成此 workspace 來管理相依性

#### 6. **在程式碼中使用 MBProgressHUD**
- **Swift**：導入模組後在程式碼中使用：
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()
          
          // 顯示帶有載入指示器的簡易 HUD
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "載入中..."
          
          // 在指定時間後隱藏（例如 2 秒）
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C**：導入標頭檔後使用：
  ```objc
  #import <MBProgressHUD/MBProgressHUD.h>

  @interface ViewController ()
  @end

  @implementation ViewController
  - (void)viewDidLoad {
      [super viewDidLoad];
      
      // 顯示帶有載入指示器的簡易 HUD
      MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.view animated:YES];
      hud.label.text = @"載入中...";
      
      // 在指定時間後隱藏（例如 2 秒）
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **常見 MBProgressHUD 功能**
- **基本 HUD**：如上所示，顯示旋轉指示器與可選文字
- **純文字顯示**：
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .text
  hud.label.text = "完成！"
  hud.hide(animated: true, afterDelay: 1.5)
  ```
- **進度條**：
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .determinate
  hud.progress = 0.5 // 50% 進度
  ```

#### 注意事項
- **版本 0.9.1**：這是較舊的版本（約 2015 年發布）。截至 2025 年 3 月的最新版本已更新許多（例如 1.2.0 或更高）。若需使用最新版，只需寫 `pod 'MBProgressHUD'` 而不指定版本號。除非有相容性需求，建議考慮更新版本
- **文件**：請查閱 [MBProgressHUD GitHub 頁面](https://github.com/jdg/MBProgressHUD) 獲取更多選項與範例。版本 0.9.1 的功能可能較現代版本少

若需要疑難排解協助或更具體的範例，請隨時告知！