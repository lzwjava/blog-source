---
audio: false
generated: false
image: false
lang: zh
layout: post
title: iOS开发者模式与ideviceinstaller
translated: true
---

## 开发者模式

我曾做过一段时间的 iOS 开发者。但我的职业重心已转向其他技术方向。不过即使现在不是专业 iOS 开发者，具备 iOS 开发知识仍然非常有用。

最近我想分享自己安装的应用程序。但如果直接截取主屏幕或设置中的应用列表截图，会显得非常凌乱。因此我需要找到查看所有已安装应用的方法。

以下是使用 Xcode 查看已安装应用的步骤：

1. 通过 USB 数据线将 iPhone 连接到 Mac
2. 打开 Xcode
3. 点击 Window → Devices and Simulators（或按 Shift + Cmd + 2）
4. 在左侧边栏选择你的 iPhone
5. 在主面板中向下滚动至 "Installed Apps" 区域

这个工具还具备其他实用功能：

1. 截取屏幕截图
2. 查看最近日志
3. 打开控制台

## xcrun

```bash
(base) lzwjava@192 Downloads % xcrun devicectl device info apps --device 00008120-xxxx --verbose
正在启用详细日志记录
2024-12-03 16:24:18.579+0800  正在启用开发者磁盘映像服务
2024-12-03 16:24:18.637+0800  已获取使用授权
已安装应用：
  - 0 个元素

命令执行完成，耗时 0.120 秒
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

## 快速滑动输入

*2024.12.01*

在 iOS 中输入 "threads" 时，只需快速划过字母 "threads" 的轨迹位置即可得到结果。请看实际效果：

<video width="50%" controls>
  <source src="/assets/images/input/in.mp4" type="video/mp4">
  您的浏览器不支持视频标签
</video>

这个功能是我偶然发现的。当手指快速划过输入区域时，会显示一条轨迹线。起初我不明白其含义，经过多次尝试后发现了上述功能。