---
audio: false
generated: true
lang: hant
layout: post
title: 在 iOS 中使用 iVersion
translated: true
type: note
---

要在你的 iOS 專案中使用 `iVersion` pod，請按照以下步驟操作：

1. **在 Xcode 中開啟專案**：請先開啟你欲添加 `iVersion` pod 的 Xcode 專案。

2. **初始化 CocoaPods**：若你尚未在專案中初始化 CocoaPods，請開啟終端機，導航至專案目錄後執行：
   ```bash
   pod init
   ```
   這將在你的專案目錄中建立 `Podfile`。

3. **編輯 Podfile**：使用文字編輯器或 Xcode 開啟 `Podfile`。在 target 區塊內加入以下行來添加 `iVersion` pod：
   ```ruby
   pod 'iVersion', '1.11.4'
   ```

4. **安裝 Pod**：儲存 `Podfile` 後返回終端機。執行以下指令來安裝 `iVersion` pod：
   ```bash
   pod install
   ```

5. **開啟 `.xcworkspace` 檔案**：安裝完成後，請關閉已開啟的 Xcode 專案，然後開啟新建立的 `.xcworkspace` 檔案。此檔案通常位於原始 `.xcodeproj` 檔案的相同目錄中。

6. **匯入 iVersion**：在你的 Swift 或 Objective-C 檔案中匯入 `iVersion` 模組以開始使用：
   ```swift
   import iVersion
   ```

7. **在程式碼中使用 iVersion**：現在你可以在專案中使用 `iVersion` 函式庫。舉例來說，你可以透過 `iVersion` 提供的方法來檢查應用程式版本或建置編號。

遵循這些步驟，你應能成功在 iOS 專案中整合並使用 `iVersion` pod。