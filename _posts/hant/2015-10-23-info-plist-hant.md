---
audio: false
generated: false
lang: hant
layout: post
title: 解碼 Info.plist 文件
translated: true
---

如果你曾經與 macOS 或 iOS 開發有過接觸，你可能會遇到一個 `Info.plist` 文件。這個基於 XML 的文件是任何 Apple 應用程式或插件的重要組成部分，就像護照一樣，告訴系統它是誰，它做什麼以及它應該如何行為。今天，我們將探索來自 "Reveal-In-GitHub" 的 `Info.plist`，這是我們在之前的文章中介紹的 Xcode 插件。與其逐行分析，我們將專注於核心概念和模式，這些概念和模式定義了它的目的和功能。

---

#### 什麼是 `Info.plist` 文件？

`Info.plist`（即「資訊屬性列表」）是一個結構化的文件，包含有關應用程式、插件或捆綁包的元數據。以 XML 書寫（使用特定的 Apple 定義的結構），它使用鍵值對來描述基本信息，如應用程式的名稱、版本和兼容性。對於 "Reveal-In-GitHub"，這個文件將其識別為 Xcode 插件，並確保它能夠與 IDE 無縫整合。

與 `.pbxproj` 文件不同，`.pbxproj` 文件是關於如何構建某物，`Info.plist` 文件是關於這個某物是什麼。它是身份和意圖的聲明。

---

#### 文件中的核心概念

1. **捆綁包基礎**
   幾個鍵將插件定義為 macOS 捆綁包：
   - **`CFBundleExecutable`**：設置為 `$(EXECUTABLE_NAME)`，這是編譯二進制文件名的占位符（在構建過程中定義）。
   - **`CFBundleIdentifier`**：`$(PRODUCT_BUNDLE_IDENTIFIER)` 解析為 `com.lzwjava.Reveal-In-GitHub`，這是一個唯一的反向 DNS 格式 ID，用於區分這個插件與其他插件。
   - **`CFBundlePackageType`**：`BNDL` 將其標記為捆綁包，這是 macOS 插件和庫的常見格式。
   - **`CFBundleName`**：`$(PRODUCT_NAME)` 將成為 "Reveal-In-GitHub"，這是人類友好的名稱。

2. **版本和所有權**
   - **`CFBundleShortVersionString`**："1.0" 是用戶面向的版本。
   - **`CFBundleVersion`**："1" 是內部構建號。
   - **`NSHumanReadableCopyright`**："Copyright © 2015年 lzwjava. All rights reserved." 給予創作者 `lzwjava` 信用，並將插件日期定為 2015 年。
   - **`CFBundleSignature`**："????" 是占位符（通常是四個字符的代碼），儘管對於插件來說這不太重要。

3. **本地化**
   - **`CFBundleDevelopmentRegion`**："en" 將英文設置為默認語言，影響資源（如果有）的本地化方式。

4. **Xcode 插件兼容性**
   這裡的突出特點是 **`DVTPlugInCompatibilityUUIDs`**，這是一個長的 UUID 陣列。這些 UUID 與特定的 Xcode 版本（例如 Xcode 6、7 等）匹配，確保插件僅在兼容的 IDE 中加載。這個列表異常廣泛，表明 "Reveal-In-GitHub" 被設計用於多個 Xcode 版本之間的工作——這是前瞻性和向後兼容性的標誌。

5. **插件特定設置**
   - **`NSPrincipalClass`**：留空 (`<string></string>`)，暗示插件可能會動態定義其入口點或依賴 Xcode 的慣例。
   - **`XC4Compatible` 和 `XC5Compatible`**：兩者均為 `<true/>`，確認與 Xcode 4 和 5 兼容。
   - **`XCGCReady`**：`<true/>` 表示準備好進行垃圾回收，這是一個較舊的 macOS 記憶體管理功能（大多數在 2015 年之前已經被 ARC 取代）。
   - **`XCPluginHasUI`**：`<false/>` 表明沒有超出 Xcode 內建的自定義 UI——儘管這似乎與 `.pbxproj` 中的 `.xib` 文件相矛盾。也許 UI 是最小化的或以不同方式處理的。

---

#### 要注意的模式

1. **靈活的占位符**
   如 `$(EXECUTABLE_NAME)` 和 `$(PRODUCT_BUNDLE_IDENTIFIER)` 這樣的鍵使用與構建系統相關的變量（在 `.pbxproj` 中定義）。這使得 `Info.plist` 可以在不同的配置（例如調試與發布）之間重用。

2. **簡潔設計**
   這個文件非常簡潔，專注於基本信息。沒有花哨的圖標、權限或應用程式特定的設置——只有一個 Xcode 插件需要的功能。這種簡潔性對於擴展現有應用程式（Xcode）的插件來說是典型的，而不是獨立程式。

3. **兼容性重點**
   長長的 `DVTPlugInCompatibilityUUIDs` 列表和 `XC4Compatible` 這樣的標誌顯示出一個建造用來持久的插件。這種模式在開發者工具中很常見，用戶可能會因為穩定性而使用較舊的 Xcode 版本。

4. **元數據而非行為**
   與代碼文件不同，`Info.plist` 不會做任何事情——它描述。它的角色是被動的，提供 Xcode 和 macOS 在運行時解釋的信息。

---

#### 這告訴我們什麼關於 Reveal-In-GitHub？

這個 `Info.plist` 將 "Reveal-In-GitHub" 描繪為一個輕量級、專注的 Xcode 插件，可能由一個獨立開發者（`lzwjava`）在 2015 年創建。其廣泛的兼容性表明它被設計用於廣泛使用，而缺少 UI 旗標（儘管項目中有一個 `.xib`）暗示了一種微妙的整合——可能是一個菜單項或上下文操作，而不是一個華麗的介面。根據名稱和 `.pbxproj` 的上下文，它可能會簡化 GitHub 工作流程，例如將 Xcode 文件鏈接到它們的在線存儲庫。

---

#### 為什麼這很重要

`Info.plist` 是你的應用程式與系統的握手。對於開發者來說，理解它意味著你可以調整兼容性、版本或行為，而不需要觸碰代碼。對於 "Reveal-In-GitHub"，它是無縫整合到 Xcode 的關鍵。下次當你在調試插件或創建自己的插件時，這個文件將是你的起點——小而強大。