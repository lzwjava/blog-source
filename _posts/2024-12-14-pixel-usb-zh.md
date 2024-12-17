---
layout: post  
title: "Pixel 的 USB 选项"  
---

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/pixel/pixel.jpg" alt="Pixel" width="50%" />  
</div>

Pixel 提供了多种 USB 选项，其中一个特别有趣的功能是将其用作网络摄像头。在 macOS 上，QuickTime 可以将 Android 摄像头用作视频源，提供了一种简单高效的解决方案。

设置方法如下：  

1. 在设置中进入 关于手机，连续点击 版本号 七次以启用开发者模式。  
2. 打开 开发者选项 并启用 USB 调试。  
3. 将 Pixel 通过 USB 连接到电脑，并在终端中运行以下命令以验证连接：  
   ```bash
   adb devices
   ```  