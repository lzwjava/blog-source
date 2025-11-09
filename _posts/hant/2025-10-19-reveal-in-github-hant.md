---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: GitHub Xcode 插件顯示功能
translated: true
type: note
---

### 什麼是 Reveal-In-GitHub？

Reveal-In-GitHub 是一款 Xcode 插件，可讓您快速從 Xcode 工作區導航至當前儲存庫的關鍵 GitHub 功能。它專為在 GitHub 託管的 Git 項目上工作的開發者設計，只需一鍵（或鍵盤快捷鍵）即可訪問提交歷史、追溯視圖、拉取請求、問題和通知等功能，無需離開 Xcode 或手動輸入網址。

### 先決條件
- 已安裝 Xcode（已在最新版本測試；未提及特定最低版本）。
- 您的項目必須是託管在 GitHub 上的 Git 儲存庫（插件會自動檢測儲存庫網址和文件路徑）。
- 如果您的項目有多個 Git 遠端，首次使用時會提示您選擇預設值。

### 安裝
有兩種主要安裝方式：

#### 選項 1：使用 Alcatraz（推薦）
1. 如果尚未安裝 Alcatraz（一個 Xcode 插件包管理器），請先安裝。您可以在網上找到設置指南，例如[這篇](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/)（如果您偏好中文說明）。
2. 在 Xcode 中打開 Alcatraz（通過選單：`Window > Package Manager`）。
3. 搜索 "Reveal In GitHub"。
4. 點擊 **安裝**。
5. 重新啟動 Xcode。

#### 選項 2：手動安裝
1. 克隆儲存庫：  
   ```
   git clone https://github.com/lzwjava/Reveal-In-GitHub.git
   ```
2. 在 Xcode 中打開 `Reveal-In-GitHub.xcodeproj` 文件。
3. 構建項目（Product > Build 或 ⌘B）。這將生成 `Reveal-In-GitHub.xcplugin` 文件。
4. 將插件移動到：  
   `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins/`
5. 重新啟動 Xcode。

安裝後，插件應出現在 Xcode 選單欄的 **Editor > Reveal In GitHub** 下。

### 使用方法
安裝並重啟 Xcode 後：
1. 在 Xcode 中打開一個 GitHub 託管的項目並編輯源文件（例如，導航到特定行）。
2. 使用鍵盤快捷鍵或 **Editor > Reveal In GitHub** 下的選單項目跳轉到 GitHub。插件會自動檢測您的儲存庫、當前文件、行號和最新提交哈希值。

以下是內置選單項目和快捷鍵的快速參考（快捷鍵遵循 ⌃⇧⌘ + 標題首字母的模式）：

| 選單項目      | 快捷鍵    | 功能說明 | GitHub 網址示例（針對儲存庫 lzwjava/LZAlbum 中文件 LZAlbumManager.m 第 40 行，提交 fd7224） |
|----------------|-------------|--------------|-----------------------------------------------------------------------------------------------|
| **設定**    | ⌃⇧⌘S      | 打開自定義面板 | 不適用 |
| **儲存庫**       | ⌃⇧⌘R      | 打開主儲存庫頁面 | https://github.com/lzwjava/LZAlbum |
| **問題**     | ⌃⇧⌘I      | 打開問題列表 | https://github.com/lzwjava/LZAlbum/issues |
| **拉取請求**        | ⌃⇧⌘P      | 打開拉取請求列表 | https://github.com/lzwjava/LZAlbum/pulls |
| **快速文件** | ⌃⇧⌘Q      | 在當前行打開文件視圖 | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40 |
| **歷史列表**| ⌃⇧⌘L     | 打開文件的提交歷史 | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m |
| **追溯**      | ⌃⇧⌘B      | 打開當前行的追溯視圖 | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40 |
| **通知**| ⌃⇧⌘N   | 打開儲存庫通知 | https://github.com/lzwjava/LZAlbum/notifications?all=1 |

- **提示**： 
  - 快捷鍵與 Xcode 的預設設置不衝突。
  - 如果您選擇了文本範圍，某些操作（如追溯）將錨定到該範圍（例如 #L40-L43）。
  - 測試方法：打開一個項目，轉到某一行，然後按下 ⌃⇧⌘B——它應該在瀏覽器中打開追溯頁面。

### 自定義
要調整或添加選單項目：
1. 按下 ⌃⇧⌘S 或前往 **Editor > Reveal In GitHub > 設定**。
2. 在面板中：
   - 點擊 "+" 按鈕添加新項目：輸入標題（例如 "Wiki"）、快捷鍵和網址模式。
   - 網址模式使用佔位符，例如：
     - `{git_remote_url}`：完整的儲存庫網址（例如 https://github.com/user/repo）。
     - `{commit}`：當前分支的最新提交哈希值。
     - `{file_path}`：文件的相對路徑。
     - `#{selection}`：當前行或選擇範圍（例如 #L40）。
   - 示例：對於 Wiki 鏈接，將模式設置為 `{git_remote_url}/wiki`。
3. 如果您有多個遠端，使用 "清除預設儲存庫" 按鈕重置選擇。

該插件靈感來自 [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub)，並基於 MIT 許可證授權。

[Reveal-In-GitHub GitHub 儲存庫](https://github.com/lzwjava/Reveal-In-GitHub)