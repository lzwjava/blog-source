---
layout: post
title: "使用 iOS 的开发者模式"
---

我曾经做过一段时间的 iOS 开发者。但我的职业重心已经转向其他技术。然而，虽然我现在不是专业的 iOS 开发者，但应用 iOS 开发知识仍然非常有用。

最近，我想分享我安装的应用程序。但如果我从主屏幕或设置中的应用列表截取所有应用的截图，会很混乱。所以我需要找到一种查看所有已安装应用的方法。

以下是使用 Xcode 查看所有已安装应用的步骤：

1. 通过 USB 将 iPhone 连接到 Mac
2. 打开 Xcode
3. 转到 Window → Devices and Simulators（或按 Shift + Cmd + 2）
4. 从左侧边栏选择你的 iPhone
5. 在主面板中，向下滚动到"Installed Apps"部分

它还有其他有用的功能：

1. 截取屏幕截图
2. 打开最近的日志
3. 打开控制台

## xcrun

(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
使用详细日志记录。
2024-12-03 16:24:18.579+0800  启用开发者磁盘映像服务。
2024-12-03 16:24:18.637+0800  获取使用断言。
已安装的应用：
  - 0 个元素

命令完成，耗时 0.120 秒


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