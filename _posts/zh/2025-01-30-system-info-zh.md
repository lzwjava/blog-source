---
audio: false
lang: zh
layout: post
title: macOS系统信息
translated: true
---

# 获取macOS系统信息的方法

在macOS上获取系统信息，你可以使用多种内置工具和命令。以下是获取各种系统信息的方法：

### 1. **系统信息实用工具**
System Information应用程序提供了对Mac硬件和软件的综合概述。

- 按下`Cmd + Space`打开**Spotlight搜索**，输入“System Information”然后按Enter键。
- 或者，你可以通过**Apple菜单** > **关于本机Mac** > **系统报告**打开它。

### 2. **关于本机Mac**
这提供了Mac的快速概述。

- 点击屏幕左上角的**Apple菜单**。
- 选择**关于本机Mac**。这将显示基本信息，如macOS版本、处理器、内存和序列号。

### 3. **终端命令**
你可以使用终端获取详细的系统信息。

- 打开**终端**，通过`应用程序` > `实用工具` > `终端`或在Spotlight中搜索。

#### 基本系统信息
```sh
system_profiler SPHardwareDataType
```

#### 详细系统信息
```sh
system_profiler
```

#### CPU信息
```sh
sysctl -n machdep.cpu.brand_string
```

#### 内存信息
```sh
sysctl hw.memsize
```

#### 磁盘使用情况
```sh
df -h
```

#### 网络信息
```sh
ifconfig
```

#### 电池信息（适用于笔记本电脑）
```sh
pmset -g batt
```

#### 已安装软件列表
```sh
ls /Applications
```

#### macOS版本
```sh
sw_vers
```

#### 用户信息
```sh
id
```

#### 运行中的进程列表
```sh
ps aux
```

#### 已安装的Brew包列表
```sh
brew list
```

#### 已安装的Pip包列表
```sh
pip list
```

#### 已安装的Gem包列表
```sh
gem list
```

### 4. **活动监视器**
该应用程序提供了Mac的实时CPU、内存、能量、磁盘和网络使用情况信息。

- 打开**活动监视器**，通过`应用程序` > `实用工具` > `活动监视器`或在Spotlight中搜索。

### 5. **磁盘工具**
该应用程序提供了关于存储设备的信息。

- 打开**磁盘工具**，通过`应用程序` > `实用工具` > `磁盘工具`或在Spotlight中搜索。

### 6. **第三方工具**
还有一些第三方应用程序，如**iStat Menus**和**CoconutBattery**，它们提供了详细的系统信息和监控功能。

通过这些方法，你可以获取macOS系统上的各种系统信息。