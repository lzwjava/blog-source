---
audio: false
generated: true
lang: hant
layout: post
title: 使用 MBProgressHUD 在 iOS
translated: true
---

看來你在詢問如何在 iOS 專案中使用 `MBProgressHUD` 圖書館，特別是版本 `0.9.1`，通過 Podfile 在 CocoaPods 中。讓我一步一步地指導你完成這個過程。

### 什麼是 MBProgressHUD？
`MBProgressHUD` 是一個流行的第三方圖書館，用於 iOS，提供了一種簡單的方法來顯示 HUD（即時顯示屏幕），帶有活動指示器、進度條或自定義視圖，通常用於顯示加載狀態或簡短消息。

### 使用 `pod 'MBProgressHUD', '0.9.1'` 的步驟

#### 1. **安裝 CocoaPods（如果尚未安裝）**
CocoaPods 是 iOS 專案的依賴管理器。如果你還沒有安裝，請在終端中運行以下命令：
```bash
sudo gem install cocoapods
```

#### 2. **設置 Podfile**
- 在終端中導航到你的 Xcode 專案目錄：
  ```bash
  cd /path/to/your/project
  ```
- 如果你還沒有 Podfile，請通過運行以下命令來創建一個：
  ```bash
  pod init
  ```
- 使用文本編輯器打開 `Podfile`（例如 `nano Podfile` 或 `open Podfile`）。

#### 3. **在 Podfile 中添加 MBProgressHUD**
在 `Podfile` 中，在應用程序的目標塊中添加 `MBProgressHUD` 版本 `0.9.1` 的行。它應該看起來像這樣：
```ruby
platform :ios, '9.0'  # 指定你的部署目標

target 'YourAppName' do
  use_frameworks!
  pod 'MBProgressHUD', '0.9.1'
end
```
- 用你的 Xcode 目標的實際名稱替換 `'YourAppName'`。
- `platform :ios, '9.0'` 行設置最低 iOS 版本；根據你的專案需求進行調整。

#### 4. **安裝 Pod**
- 保存 `Podfile` 並在終端中運行以下命令：
  ```bash
  pod install
  ```
- 這將下載並將 `MBProgressHUD` 版本 `0.9.1` 集成到你的專案中。如果成功，你將看到確認安裝的輸出。

#### 5. **打開工作區**
- 安裝後，關閉你的 Xcode 專案（如果已打開）並打開新創建的 `.xcworkspace` 文件（例如 `YourAppName.xcworkspace`），而不是 `.xcodeproj` 文件。CocoaPods 生成這個工作區來管理依賴。

#### 6. **在代碼中使用 MBProgressHUD**
- **Swift**：導入模塊並在代碼中使用：
  ```swift
  import MBProgressHUD

  class ViewController: UIViewController {
      override func viewDidLoad() {
          super.viewDidLoad()

          // 顯示一個簡單的 HUD 帶有加載指示器
          let hud = MBProgressHUD.showAdded(to: self.view, animated: true)
          hud.label.text = "Loading..."

          // 過一段時間後隱藏它（例如 2 秒）
          DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
              hud.hide(animated: true)
          }
      }
  }
  ```

- **Objective-C**：導入標頭並使用：
  ```objc
  #import <MBProgressHUD/MBProgressHUD.h>

  @interface ViewController ()
  @end

  @implementation ViewController
  - (void)viewDidLoad {
      [super viewDidLoad];

      // 顯示一個簡單的 HUD 帶有加載指示器
      MBProgressHUD *hud = [MBProgressHUD showHUDAddedTo:self.view animated:YES];
      hud.label.text = @"Loading...";

      // 過一段時間後隱藏它（例如 2 秒）
      dispatch_after(dispatch_time(DISPATCH_TIME_NOW, 2 * NSEC_PER_SEC), dispatch_get_main_queue(), ^{
          [hud hideAnimated:YES];
      });
  }
  @end
  ```

#### 7. **常見的 MBProgressHUD 功能**
- **基本 HUD**：如上所示，顯示一個旋轉指示器，可選文本。
- **僅顯示自定義文本**：
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .text
  hud.label.text = "Done!"
  hud.hide(animated: true, afterDelay: 1.5)
  ```
- **進度條**：
  ```swift
  let hud = MBProgressHUD.showAdded(to: view, animated: true)
  hud.mode = .determinate
  hud.progress = 0.5 // 50% 進度
  ```

#### 注意事項
- **版本 0.9.1**：這是一個較舊的版本（約於 2015 年發布）。截至 2025 年 3 月的最新版本要新得多（例如 1.2.0 或更高）。要使用最新版本，只需寫 `pod 'MBProgressHUD'` 而不指定版本號。除非你需要 0.9.1 來保持兼容性，否則考慮更新。
- **文檔**：查看 [MBProgressHUD GitHub 頁面](https://github.com/jdg/MBProgressHUD) 以獲取更多選項和示例。版本 0.9.1 可能比現代版本具有更少的功能。