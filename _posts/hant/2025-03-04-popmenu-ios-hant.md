---
audio: false
generated: true
lang: hant
layout: post
title: 在 iOS 中使用 PopMenu
translated: true
type: note
---

要在你的 iOS 專案中使用 `pod 'PopMenu', '2.4'`，代表你正透過 CocoaPods（一個流行的 iOS 依賴管理工具）整合 PopMenu 函式庫（版本 2.4）。這個函式庫提供了一個彈出式動畫選單，靈感來自新浪微博或網易等應用程式。以下是設定並在專案中使用的步驟：

---

### 步驟 1：安裝 CocoaPods（如果尚未安裝）
如果你的系統尚未安裝 CocoaPods，請先安裝：
1. 開啟終端機。
2. 執行以下指令：
   ```bash
   sudo gem install cocoapods
   ```
3. 驗證安裝：
   ```bash
   pod --version
   ```

---

### 步驟 2：設定 Podfile
1. 在終端機中導航至你的 Xcode 專案目錄：
   ```bash
   cd /path/to/your/project
   ```
2. 如果還沒有 Podfile，請執行以下指令建立：
   ```bash
   pod init
   ```
3. 在文字編輯器中開啟 `Podfile`（例如使用 `nano Podfile` 或 Xcode）。
4. 加入以下行以指定你的目標使用 PopMenu pod：
   ```ruby
   platform :ios, '8.0'  # 如有需要，請調整 iOS 版本
   target 'YourAppName' do
     use_frameworks!
     pod 'PopMenu', '2.4'
   end
   ```
   - 將 `YourAppName` 替換為你的 Xcode 目標名稱。
   - `use_frameworks!` 這一行是必需的，因為 PopMenu 很可能是一個基於框架的函式庫。

5. 儲存並關閉 Podfile。

---

### 步驟 3：安裝 Pod
1. 在終端機中執行：
   ```bash
   pod install
   ```
2. 這會下載並將 PopMenu 版本 2.4 整合到你的專案中。等待直到看到類似以下的訊息：
   ```
   Pod installation complete! There are X dependencies from the Podfile and X total pods installed.
   ```
3. 如果 Xcode 專案已開啟，請先關閉，然後開啟新生成的 `.xcworkspace` 檔案（例如 `YourAppName.xcworkspace`），而不是 `.xcodeproj` 檔案。

---

### 步驟 4：在程式碼中的基本用法
PopMenu 是用 Objective-C 編寫的，因此你需要相應地使用它。以下是在你的應用程式中實現的範例：

1. **匯入函式庫**：
   - 在你的 Objective-C 檔案中（例如 `ViewController.m`）：
     ```objective-c
     #import "PopMenu.h"
     ```
   - 如果你使用 Swift，請建立一個橋接標頭檔：
     - 前往 `File > New > File > Header File`（例如 `YourAppName-Bridging-Header.h`）。
     - 加入：
       ```objective-c
       #import "PopMenu.h"
       ```
     - 在 Xcode 中，於 `Build Settings > Swift Compiler - General > Objective-C Bridging Header` 設定橋接標頭檔的路徑（例如 `YourAppName/YourAppName-Bridging-Header.h`）。

2. **建立選單項目**：
   定義你想要在彈出選單中顯示的項目。每個項目可以有標題、圖示和發光顏色。
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

3. **初始化並顯示選單**：
   建立一個 `PopMenu` 實例並在你的視圖中顯示。
   ```objective-c
   PopMenu *popMenu = [[PopMenu alloc] initWithFrame:self.view.bounds items:items];
   popMenu.menuAnimationType = kPopMenuAnimationTypeNetEase; // 選項：kPopMenuAnimationTypeSina 或 kPopMenuAnimationTypeNetEase
   popMenu.perRowItemCount = 2; // 每行項目數量
   [popMenu showMenuAtView:self.view];
   ```

4. **處理選擇（可選）**：
   你可以子類化或擴展功能來偵測點擊，不過 PopMenu 的基本版本（約 2.4 版）可能不原生支援委派模式。請查閱 GitHub 上的函式庫文件（`xhzengAIB/PopMenu`）以獲取任何更新或自訂資訊。

---

### 步驟 5：執行你的專案
在 Xcode 中建置並執行你的專案（`Cmd + R`）。如果圖示（例如 `post_type_bubble_flickr`）是你的資產目錄的一部分，請確保它們已加入專案中。如果沒有，你需要尋找或建立它們。

---

### 注意事項
- **版本指定**：`pod 'PopMenu', '2.4'` 會將你鎖定在版本 2.4。如果你想要最新版本，請使用 `pod 'PopMenu'` 而不指定版本號，但這可能會引入破壞性變更。
- **相容性**：確保你的專案部署目標至少是 iOS 8.0（或在 Podfile 中調整 `platform`）。
- **自訂**：PopMenu 允許動畫類型和佈局調整（例如 `perRowItemCount`）。探索原始碼以獲取更多選項。
- **疑難排解**：如果遇到「檔案未找到」等錯誤，請確保你的 Pods 已正確安裝並且正在使用工作區。

這應該能幫助你在 iOS 應用程式中開始使用 PopMenu 2.4！如果你需要進一步的說明，請告訴我。