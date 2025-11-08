---
audio: false
generated: false
image: true
lang: hant
layout: post
title: Pixel USB、iOS開發者工具、滑動輸入
translated: true
type: post
---

### 目錄

1. [Pixel 的 USB 選項](#pixels-usb-options)
   - 將 Pixel 用作網絡攝影機
   - 在設定中啟用開發者模式
   - 啟用 USB Debugging 進行連接
   - 使用 ADB 指令驗證連接

2. [iOS 的開發者模式和 ideviceinstaller](#developer-mode-of-ios-and-ideviceinstaller)
   - 透過 Xcode 查看已安裝的應用程式
   - 使用 Xcode 進行截圖和查看日誌
   - 使用 xcrun 指令列出應用程式
   - 安裝和使用 ideviceinstaller 工具

3. [快速滑動輸入](#quick-swipe-typing)
   - 透過滑動字母輸入單字
   - 意外發現此功能
   - 快速觸摸時出現線條

## Pixel 的 USB 選項

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/pixel/pixel.jpg" alt="Pixel" width="50%" />  
</div>

Pixel 提供了多種 USB 選項，其中一個特別有趣的功能是它能夠充當網絡攝影機。在 macOS 上，QuickTime 可以將 Android 網絡攝影機作為視訊來源，提供了一個簡單有效的解決方案。

設定步驟如下：

1. 在設定中導航至「關於手機」，然後點擊「版本號碼」七次以啟用開發者模式。
2. 打開「開發者選項」並啟用 USB Debugging。
3. 透過 USB 將您的 Pixel 連接到電腦，並在終端機中運行以下指令來驗證連接：
   ```bash
   adb devices
   ```

---

## iOS 的開發者模式和 ideviceinstaller

*2024.12.03*

## 開發者模式

我曾經在一段時間內是一名 iOS 開發者。但我的職業重心已轉向其他技術。然而，即使我現在不是專業的 iOS 開發者，應用 iOS 開發知識仍然非常有用。

最近，我想分享我已安裝的應用程式。但如果我從主畫面或設定中的應用程式列表截圖所有應用程式，那將會很混亂。所以我需要找到一種方法來查看所有已安裝的應用程式。

以下是使用 Xcode 查看所有已安裝應用程式的步驟：

1. 透過 USB 將 iPhone 連接到 Mac
2. 開啟 Xcode
3. 進入 Window → Devices and Simulators (或按下 Shift + Cmd + 2)
4. 從左側邊欄中選擇您的 iPhone
5. 在主面板中，向下捲動到「Installed Apps」部分

它還有其他有用的功能：

1. 截圖
2. 打開最近的日誌
3. 打開控制台

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
com.sf-express.waybillcn, "9.70.0.1", "順豐速運"
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

如果你想在 iOS 中輸入「threads」，你只需要快速滑動手指覆蓋「threads」字母的位置即可得到結果。讓我們看看它是如何運作的。

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

我偶然發現了這個。當我的手指快速觸摸輸入區域時，它會顯示一條線。我不知道那代表什麼。經過一些實驗，我發現了上述的發現。