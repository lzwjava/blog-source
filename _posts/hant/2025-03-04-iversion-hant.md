---
audio: false
generated: true
lang: hant
layout: post
title: 使用 iVersion 在 iOS
translated: true
---

要在您的iOS項目中使用 `iVersion` pod，您需要遵循以下步驟：

1. **在 Xcode 中打開您的項目**：確保您已經打開了您想要添加 `iVersion` pod 的 Xcode 項目。

2. **初始化 CocoaPods**：如果您還沒有在項目中初始化 CocoaPods，請打開終端，導航到您的項目目錄，然後運行：
   ```bash
   pod init
   ```
   這將在您的項目目錄中創建一個 `Podfile`。

3. **編輯 Podfile**：在文本編輯器或 Xcode 中打開 `Podfile`。通過在目標部分內包含以下行來將 `iVersion` pod 添加到您的 `Podfile`：
   ```ruby
   pod 'iVersion', '1.11.4'
   ```

4. **安裝 Pod**：保存 `Podfile`，然後返回終端。運行以下命令以安裝 `iVersion` pod：
   ```bash
   pod install
   ```

5. **打開 `.xcworkspace` 文件**：安裝完成後，如果您的 Xcode 項目已打開，請關閉它，然後打開新創建的 `.xcworkspace` 文件。該文件通常位於與您的原始 `.xcodeproj` 文件相同的目錄中。

6. **導入 iVersion**：在您的 Swift 或 Objective-C 文件中，導入 `iVersion` 模組以開始使用它：
   ```swift
   import iVersion
   ```

7. **在您的代碼中使用 iVersion**：現在您可以在項目中使用 `iVersion` 圖書館。例如，您可以使用 `iVersion` 提供的方法來檢查應用程序版本或構建號。

通過遵循這些步驟，您應該能夠成功整合並使用 `iVersion` pod 到您的 iOS 項目中。