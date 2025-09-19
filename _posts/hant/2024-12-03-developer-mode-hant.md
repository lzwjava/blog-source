---
audio: false
generated: false
image: false
lang: hant
layout: post
title: iOS 與 ideviceinstaller 的開發者模式
translated: true
---

## 開發者模式

我曾有一段時間是 iOS 開發者，但我的職業重心已轉向其他技術。不過，即使現在我不是專業的 iOS 開發者，運用 iOS 開發知識仍然非常有用。

最近，我想分享我安裝的應用程式。但如果我從主畫面或設定中的應用程式列表截取所有應用程式的截圖，會顯得雜亂無章。因此，我需要找到一種方法來查看所有已安裝的應用程式。

以下是使用 Xcode 查看所有已安裝應用程式的步驟：

1. 透過 USB 將 iPhone 連接到 Mac
2. 開啟 Xcode
3. 前往 Window → Devices and Simulators（或按 Shift + Cmd + 2）
4. 從左側邊欄選擇你的 iPhone
5. 在主面板中，向下滾動至「Installed Apps」部分

它還有其他實用功能：

1. 截取螢幕截圖
2. 開啟最近日誌
3. 開啟控制台

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
Using verbose logging.
2024-12-03 16:24:18.579+0800  Enabling developer disk image services.
2024-12-03 16:24:18.637+0800  Acquired usage assertion.
Apps installed:
  - 0 elements

Command Completed, took 0.120 seconds
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
com.sf-express.waybillcn, "9.70.0.1", "顺丰速运"
com.roblox.robloxmobile, "2.652.762", "Roblox"
co.alphaexploration.clubhouse, "3273", "Clubhouse"
com.dbs.mbanking.cn, "11", "DBS digibank"
global.longbridge.ios, "59579", "Longbridge"
imgurmobile, "416", "Imgur"
com.creditkarma.mobile, "17316145", "Credit Karma"
...
```

---

## 快速滑動輸入

*2024.12.01*

如果你想在 iOS 中輸入「threads」，只需快速畫一條線覆蓋字母「threads」的位置即可得到結果。來看看它是如何運作的。

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  您的瀏覽器不支援影片標籤。
</video>

我偶然發現了這個功能。當我的手指快速觸碰輸入區域時，會顯示一條線。我不知道那是什麼意思。經過一些實驗，我發現了上述的功能。