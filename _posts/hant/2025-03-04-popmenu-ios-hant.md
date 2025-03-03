---
audio: false
generated: true
lang: hant
layout: post
title: 使用 PopMenu 在 iOS
translated: true
---

在你的 iOS 專案中使用 `pod 'PopMenu', '2.4'`，你將通過 CocoaPods（一個流行的 iOS 依賴管理器）整合 PopMenu 圖書館（版本 2.4）。這個圖書館提供了一個受 Sina Weibo 或 NetEase 等應用啟發的彈出動畫菜單。以下是設置和使用它的步驟：

---

### 第 1 步：安裝 CocoaPods（如果尚未安裝）
如果你的系統上還沒有安裝 CocoaPods，請先安裝它：
1. 打開你的終端。
2. 運行以下命令：
   ```bash
   sudo gem install cocoapods
   ```
3. 驗證安裝：
   ```bash
   pod --version
   ```

---

### 第 2 步：設置你的 Podfile
1. 在終端中導航到你的 Xcode 專案目錄：
   ```bash
   cd /path/to/your/project
   ```
2. 如果你還沒有 Podfile，通過運行以下命令創建一個：
   ```bash
   pod init
   ```
3. 使用文本編輯器打開 `Podfile`（例如 `nano Podfile` 或使用 Xcode）。
4. 添加以下行以指定你的目標的 PopMenu pod：
   ```ruby
   platform :ios, '8.0'  # 如果需要，調整 iOS 版本
   target 'YourAppName' do
     use_frameworks!
     pod 'PopMenu', '2.4'
   end
   ```
   - 用你的 Xcode 目標的名稱替換 `YourAppName`。
   - `use_frameworks!` 行是必需的，因為 PopMenu 可能是基於框架的圖書館。

5. 保存並關閉 Podfile。

---

### 第 3 步：安裝 Pod
1. 在終端中運行：
   ```bash
   pod install
   ```
2. 這將下載並將 PopMenu 版本 2.4 整合到你的專案中。等待看到類似以下的消息：
   ```
   Pod 安裝完成！Podfile 中有 X 個依賴項，總共安裝了 X 個 Pod。
   ```
3. 如果你的 Xcode 專案已打開，請關閉它，然後打開新生成的 `.xcworkspace` 文件（例如 `YourAppName.xcworkspace`），而不是 `.xcodeproj` 文件。

---

### 第 4 步：在你的代碼中進行基本使用
PopMenu 是用 Objective-C 寫的，所以你需要相應地使用它。以下是如何在你的應用中實現它的示例：

1. **導入圖書館**：
   - 在你的 Objective-C 文件中（例如 `ViewController.m`）：
     ```objective-c
     #import "PopMenu.h"
     ```
   - 如果你使用 Swift，創建一個橋接標頭：
     - 轉到 `File > New > File > Header File`（例如 `YourAppName-Bridging-Header.h`）。
     - 添加：
       ```objective-c
       #import "PopMenu.h"
       ```
     - 在 Xcode 中，在 `Build Settings > Swift Compiler - General > Objective-C Bridging Header` 下設置橋接標頭到你的標頭文件的路徑（例如 `YourAppName/YourAppName-Bridging-Header.h`）。

2. **創建菜單項目**：
   定義你想在彈出菜單中要的項目。每個項目都可以有標題、圖標和發光顏色。
   ```objective-c
   NSMutableArray *items = [[NSMutableArray alloc] init];

   MenuItem *menuItem1 = [[MenuItem alloc] initWithTitle:@"Flickr"
                                               iconName:@"post_type_bubble_flickr"
                                              glowColor:[UIColor grayColor]
                                                  index:0];
   [items addObject:menuItem1];

   MenuItem *menuItem2 = [[MenuItem alloc] initWithTitle:@"Twitter"
                                               iconName:@"post_type_bubble_twitter"
                                              glowColor:[UIColor blueColor]
                                                  index:1];
   [items addObject:menuItem2];
   ```

3. **初始化並顯示菜單**：
   創建一個 `PopMenu` 實例並在你的視圖中顯示它。
   ```objective-c
   PopMenu *popMenu = [[PopMenu alloc] initWithFrame:self.view.bounds items:items];
   popMenu.menuAnimationType = kPopMenuAnimationTypeNetEase; // 選項：kPopMenuAnimationTypeSina 或 kPopMenuAnimationTypeNetEase
   popMenu.perRowItemCount = 2; // 每行的項目數
   [popMenu showMenuAtView:self.view];
   ```

4. **處理選擇（可選）**：
   你可以子類化或擴展功能以檢測點擊，儘管 PopMenu 的基本版本（約 2.4）可能不會原生支持委派。檢查 GitHub 上的圖書館文檔（`xhzengAIB/PopMenu`）以獲取任何更新或自定義。

---

### 第 5 步：運行你的專案
在 Xcode 中構建並運行你的專案（`Cmd + R`）。如果圖標（例如 `post_type_bubble_flickr`）是你的資產目錄的一部分，請確保它們已添加到你的專案中。如果沒有，你需要獲取或創建它們。

---

### 注意事項
- **版本特定性**：`pod 'PopMenu', '2.4'` 將你鎖定在版本 2.4。如果你想要最新版本，使用 `pod 'PopMenu'` 而不帶版本號，但這可能會引入破壞性變更。
- **兼容性**：確保你的專案的部署目標至少是 iOS 8.0（或在 Podfile 中調整 `platform`）。
- **自定義**：PopMenu 允許動畫類型和佈局調整（例如 `perRowItemCount`）。探索源代碼以獲取更多選項。
- **故障排除**：如果你遇到類似“文件未找到”的錯誤，請確保你的 Pods 正確安裝並使用工作區。

這應該能讓你開始在 iOS 應用中使用 PopMenu 2.4！如果你需要進一步的說明，請告訴我。