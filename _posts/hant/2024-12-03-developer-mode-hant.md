---
audio: false
generated: false
lang: hant
layout: post
title: iOS 的開發者模式及ideviceinstaller工具
translated: true
---

## 開發者模式

我曾有一段時間是iOS開發者。但我的職業重心已經轉移到其他技術上。然而，即使現在我不是專業的iOS開發者，應用iOS開發知識仍然非常有用。

最近，我想分享我安裝的應用程序。但如果我從主屏幕或設置中的應用程序列表中截取所有應用程序的屏幕截圖，那將會非常混亂。所以我需要找到一種方法來查看所有已安裝的應用程序。

以下是使用Xcode查看所有已安裝應用程序的步驟：

1. 通過USB將你的iPhone連接到Mac
2. 打開Xcode
3. 前往Window → Devices and Simulators（或按Shift + Cmd + 2）
4. 從左側邊欄中選擇你的iPhone
5. 在主面板中，向下滾動到“Installed Apps”部分

它還有其他有用的功能：

1. 截取屏幕截圖
2. 打開最近的日誌
3. 打開控制台

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
使用詳細日誌記錄。
2024-12-03 16:24:18.579+0800  啟用開發者磁盤映像服務。
2024-12-03 16:24:18.637+0800  獲取使用權限。
已安裝的應用程序：
  - 0 個元素

命令完成，耗時0.120秒
```

## ideviceinstaller

```bash
brew install ideviceinstaller
ideviceinstaller -l
```

```bash
(base) lzwjava@192 Downloads % ideviceinstaller -l
CFBundleIdentifier, CFBundleVersion, CFBundleDisplayName
com.huawei.smarthome-ios, "14.1.1.325", "HUAWEI AI Life"
com.sf-express.waybillcn, "9.70.0.1", "順豐速運"
com.roblox.robloxmobile, "2.652.762", "Roblox"
co.alphaexploration.clubhouse, "3273", "Clubhouse"
com.dbs.mbanking.cn, "11", "DBS digibank"
global.longbridge.ios, "59579", "Longbridge"
imgurmobile, "416", "Imgur"
com.creditkarma.mobile, "17316145", "Credit Karma"
...
```