---
audio: false
generated: true
lang: hant
layout: post
title: 在 iOS 中使用 FXForms
translated: true
type: note
---

看來您正在參考如何透過 CocoaPods（一個專為 Swift 和 Objective-C 項目設計的熱門依賴管理工具）將 `FXForms` 函式庫整合到 iOS 專案中。以下是一份逐步指南，協助您在專案中使用 `pod 'FXForms', '1.2.13'`：

---

### 前置準備
1. **安裝 CocoaPods**：如果您的電腦上尚未安裝 CocoaPods，請先透過終端機執行以下指令進行安裝：
   ```bash
   sudo gem install cocoapods
   ```
2. **Xcode 專案**：請確保您已有一個現有的 Xcode 專案，並計劃在其中整合 `FXForms`。

---

### 使用 `pod 'FXForms', '1.2.13'` 的步驟

#### 1. **導航至您的專案目錄**
開啟終端機，並切換至包含您 Xcode 專案（`.xcodeproj` 檔案）的目錄：
```bash
cd /path/to/your/project
```

#### 2. **初始化 Podfile（如果尚未存在）**
如果您的專案目錄中還沒有 `Podfile`，請透過執行以下指令來建立：
```bash
pod init
```
這將在您的專案目錄中生成一個 `Podfile`。

#### 3. **編輯 Podfile**
使用文字編輯器（例如 `nano`、`vim` 或任何程式碼編輯器如 VS Code）開啟 `Podfile`，並加入指定版本 `1.2.13` 的 `FXForms` pod。您的 `Podfile` 應類似以下內容：

```ruby
platform :ios, '9.0'  # 指定最低 iOS 版本（請根據需要調整）
use_frameworks!       # 可選，如果您使用 Swift 或框架則需包含此行

target 'YourProjectName' do
  # YourProjectName 的 Pods
  pod 'FXForms', '1.2.13'
end
```

- 將 `'YourProjectName'` 替換為您 Xcode 目標的實際名稱（您可以在 Xcode 的專案設定中找到此名稱）。
- 行 `pod 'FXForms', '1.2.13'` 指定您要使用 `FXForms` 函式庫的 `1.2.13` 版本。

#### 4. **安裝 Pod**
儲存 `Podfile`，然後在終端機中執行以下指令以安裝指定版本的 `FXForms`：
```bash
pod install
```
這將下載並將 `FXForms` 版本 `1.2.13` 整合到您的專案中。如果成功，您將看到指示 pods 已安裝的輸出訊息。

#### 5. **開啟 Workspace**
執行 `pod install` 後，您的專案目錄中將建立一個 `.xcworkspace` 檔案。請在 Xcode 中開啟此檔案（而非 `.xcodeproj`）：
```bash
open YourProjectName.xcworkspace
```

#### 6. **在程式碼中使用 FXForms**
`FXForms` 是一個 Objective-C 函式庫，可簡化 iOS 應用程式中的表單建立。以下是一個基本的使用範例：

- **匯入 FXForms**：在您的 Objective-C 檔案（例如某個視圖控制器）中匯入該函式庫：
  ```objective-c
  #import <FXForms/FXForms.h>
  ```

- **建立表單模型**：定義一個遵循 `FXForm` 協定的類別。例如：
  ```objective-c
  // MyForm.h
  #import <Foundation/Foundation.h>
  #import <FXForms/FXForms.h>

  @interface MyForm : NSObject <FXForm>
  @property (nonatomic, copy) NSString *name;
  @property (nonatomic, copy) NSString *email;
  @end

  // MyForm.m
  #import "MyForm.h"

  @implementation MyForm
  - (NSArray *)fields {
      return @[
          @{FXFormFieldKey: @"name", FXFormFieldTitle: @"Name"},
          @{FXFormFieldKey: @"email", FXFormFieldTitle: @"Email"}
      ];
  }
  @end
  ```

- **顯示表單**：在您的視圖控制器中，使用 `FXFormViewController` 來呈現表單：
  ```objective-c
  #import "MyForm.h"

  - (void)viewDidLoad {
      [super viewDidLoad];
      FXFormViewController *formController = [[FXFormViewController alloc] init];
      formController.form = [[MyForm alloc] init];
      [self.navigationController pushViewController:formController animated:YES];
  }
  ```

#### 7. **建置並執行**
在 Xcode 中建置您的專案（`Cmd + B`）以確保所有設定正確無誤，然後在模擬器或裝置上執行（`Cmd + R`）。

---

### 疑難排解
- **找不到 Pod**：如果您遇到類似 "Unable to find a specification for `FXForms`" 的錯誤，請確認該函式庫在 CocoaPods 儲存庫中仍然可用。根據我最後的更新，`FXForms` 是一個較舊的函式庫，其可用性可能取決於 CocoaPods trunk。
- **版本錯誤**：如果版本 `1.2.13` 不可用，您可以透過執行以下指令來檢查可用版本：
  ```bash
  pod search FXForms
  ```
  然後相應地更新您 `Podfile` 中的版本。
- **建置錯誤**：請確保您在 Xcode 中的部署目標符合或超過 `FXForms` 所需的最低 iOS 版本（對於舊版本通常為 iOS 7.0+）。

---

### 補充說明
- **`FXForms` 概述**：`FXForms` 是由 Nick Lockwood 開發的函式庫，可自動化 iOS 中的表單建立。它特別適用於以最少的程式碼生成基於表格視圖的表單。
- **Swift 專案**：如果您使用 Swift，由於 `FXForms` 是一個 Objective-C 函式庫，您需要建立一個 Objective-C 橋接頭檔案來使用它。請將 `#import <FXForms/FXForms.h>` 加入該頭檔案中。

如果您在此過程的任何特定部分需要協助，請隨時告知！