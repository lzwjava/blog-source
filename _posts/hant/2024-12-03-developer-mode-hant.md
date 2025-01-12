---
lang: hant
layout: post
title: iOS开发者模式与ideviceinstaller
---

## 开发者模式

我曾担任过一段时间的iOS开发者。然而，我的职业重心已转向其他技术领域。尽管如此，即便现在我不再是专业的iOS开发者，运用iOS开发知识仍然非常有用。

最近，我想分享自己安装的应用。但如果从主屏幕或设置中的应用列表中截取所有应用的截图，会显得杂乱无章。因此，我需要找到一种方法来查看所有已安装的应用。

以下是使用Xcode查看所有已安装应用的步骤：

1. 使用USB線將您的iPhone連接到Mac
2. 打開Xcode
3. 前往“窗口” → “設備和模擬器”（或按下Shift + Cmd + 2）
4. 從左側邊欄中選擇您的iPhone
5. 在主面板中，向下滾動至“已安裝應用”部分

它还有其他实用的功能：

1. 截取屏幕截图
2. 打开最近的日志
3. 打开控制台

## xcrun

`xcrun` 是 Xcode 命令行工具中的一个实用程序，用于在终端中调用其他 Xcode 工具。它可以根据当前活动的开发者目录自动选择和使用适当的工具版本。通过 `xcrun`，开发者可以更方便地执行编译、打包、签名等操作，而无需手动指定工具路径。

例如，使用 `xcrun` 调用 `clang` 编译器：

```bash
xcrun clang -o myprogram myprogram.c
```

在这个例子中，`xcrun` 会自动找到并调用当前 Xcode 安装中的 `clang` 编译器。

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
使用详细日志记录。
2024-12-03 16:24:18.579+0800  启用开发者磁盘映像服务。
2024-12-03 16:24:18.637+0800  获取使用断言。
已安装的应用程序：
  - 0 个元素
```

命令完成，耗时0.120秒
```

## 设备安装器

```bash
brew install ideviceinstaller
ideviceinstaller -l
```

翻譯成繁體中文：

```bash
brew 安裝 ideviceinstaller
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