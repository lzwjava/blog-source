---
audio: false
generated: false
image: false
lang: hant
layout: post
title: 揭示 GitHub 之 Xcode 插件
translated: true
type: post
---

這是來自 GitHub 專案 [https://github.com/lzwjava/Reveal-In-GitHub](https://github.com/lzwjava/Reveal-In-GitHub) 的 README.md。

---

# Reveal-In-GitHub

一個設計用於在 Xcode 中無縫導航到當前儲存庫的關鍵 GitHub 功能的插件。僅需一個點擊，幾秒鐘內即可輕鬆訪問 GitHub History、Blame、Pull Requests、Issues 和 Notifications。

![plugin](https://cloud.githubusercontent.com/assets/5022872/10867703/96e980be-80ab-11e5-9aaa-a06ef476b7f7.gif)

我的公司在 GitHub 上工作。我經常打開 GitHub。有時候我在 Xcode 中編輯並不理解某些代碼，所以我會去 GitHub 進行 Blame。有時候，我會查找有關某個文件的最新提交，以幫助我了解代碼的演變。因此，我想知道是否有工具可以幫助我快速從 Xcode 打開 GitHub。因此，我編寫了這個插件。當您在 Xcode 中編輯某個源文件時，很容易知道您正在哪個 GitHub 儲存庫中工作，並知道您正在編輯的文件。這樣可以快速跳轉到 GitHub 上的文件，快速跳轉到當前編輯行的 GitHub Blame，快速跳轉到您正在 Xcode 上工作的當前儲存庫的 Issues 或 PRs。

## 選單項目

<img width="700" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864813/5df3f05e-8034-11e5-9f3e-03ae3fbc3cfc.png">

它有六個選單項目：

選單標題     | 快捷方式              | GitHub URL 模式（當我正在編輯 LZAlbumManager.m 行 40 時）
----------------|-----------------------|----------------------------------
 設定	    |⌃⇧⌘S
 儲存庫           |⌃⇧⌘R | https://github.com/lzwjava/LZAlbum
 Issues         |⌃⇧⌘I | https://github.com/lzwjava/LZAlbum/issues
 PRs            |⌃⇧⌘P | https://github.com/lzwjava/LZAlbum/pulls
 快速文件       |⌃⇧⌘Q | https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 歷史記錄       |⌃⇧⌘L | https://github.com/lzwjava/LZAlbum/commits/fd7224/LZAlbum/manager/LZAlbumManager.m
 Blame          |⌃⇧⌘B | https://github.com/lzwjava/LZAlbum/blame/fd7224/LZAlbum/manager/LZAlbumManager.m#L40
 通知          |⌃⇧⌘N | https://github.com/leancloud/LZAlbum/notifications?all=1

這些快捷方式經過精心設計，不會與 Xcode 默認快捷方式衝突。快捷方式模式是 ⌃⇧⌘（Ctrl+Shift+Command），加上選單標題的第一個字母。

## 自訂

有時候，您可能想快速跳轉到 Wiki。以下是方法，打開設定：

<img width="500" alt="2015-11-01 12 56 35" src="https://cloud.githubusercontent.com/assets/5022872/10864939/fa83f286-8037-11e5-97d7-e9549485b11d.png">

例如：

快速文件，模式和實際 URL：

```
           {git_remote_url}      /blob/{commit}/         {file_path}         #{selection}
https://github.com/lzwjava/LZAlbum/blob/fd7224/LZAlbum/manager/LZAlbumManager.m#L40-L43
```

{commit} 是當前分支的最新提交哈希值。它比使用分支更好，因為分支的 HEAD 可能會變化。因此，#L40-L43 中的代碼也可能會變化。

因此，如果您想為當前儲存庫的 Wiki 添加一個快捷方式，只需添加一個選單項目並將模式設置為 `{git_remote_url}/wiki`。

在設定中，`Clear Default Repos` 表示如果您有多個 git 傳輸，當首次觸發時，它會提示您選擇其中一個：

<img width="400" src="https://cloud.githubusercontent.com/assets/5022872/10865120/5794994a-803c-11e5-9527-965f7e617e8f.png">

然後插件會記住您的選擇。因此，當您再次觸發選單時，將打開該遠程儲存庫作為默認。按鈕 `Clear Default Repos` 將清除此設置，將再次提示您選擇。

## 安裝

推薦使用 [Alcatraz](http://alcatraz.io/)，

![qq20151101-1 2x](https://cloud.githubusercontent.com/assets/5022872/10867743/0ce351c6-80ae-11e5-82e2-f740887153f7.jpg)

或者

1. 克隆此儲存庫。
2. 打開 `Reveal-In-GitHub.xcodeproj`，並構建它。
3. Reveal-In-GitHub.xcplugin 应該位於 `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins`
4. 重新啟動 Xcode。
5. 打開任何 GitHub 專案並按下 ⌃⇧⌘B（Ctrl+Shift+Command+B）以 Blame 代碼。

## 安裝

建議使用 [Alcatraz](http://alcatraz.io/)，可參考巧神的一遍[博客](http://blog.devtang.com/blog/2014/03/05/use-alcatraz-to-manage-xcode-plugins/)。安裝好後，按照上圖搜索 `Reveal In GitHub`，點擊 `Install` 即可。

如果不使用這個工具，那麼也只需三步：

* 克隆該專案到本地。
* 打開 xcodeproj，點擊 Build 构建。這將在目錄 `~/Library/Application Support/Developer/Shared/Xcode/Plug-ins` 生成 Reveal-In-GitHub.xcplugin 文件。
* 重啟 Xcode，打開任意一個放在 GitHub 上的專案。按下 `Ctrl+Shift+Command+B` 即可。

## 致謝

在開發過程中，發現另一個插件 [ShowInGitHub](https://github.com/larsxschneider/ShowInGitHub) 做了類似的事情。我從中學到了一些技術。感謝這個。

## 許可證

MIT