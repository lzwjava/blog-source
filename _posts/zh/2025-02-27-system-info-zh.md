---
audio: true
generated: true
lang: zh
layout: post
title: macOS 系统信息
translated: true
---

要在 macOS 上获取系统信息，可以使用几种内置工具和命令。以下是获取各种类型系统信息的方法：

### 1. **系统信息实用工具**
系统信息应用程序提供了对 Mac 硬件和软件的全面概述。

- 按 `Cmd + Space` 打开 **Spotlight 搜索**，输入 "System Information"，然后按 Enter。
- 或者，可以从 **Apple 菜单** > **关于本机** > **系统报告** 打开。

### 2. **关于本机**
这提供了 Mac 规格的快速概述。

- 点击屏幕左上角的 **Apple 菜单**。
- 选择 **关于本机**。这将显示基本信息，如 macOS 版本、处理器、内存和序列号。

### 3. **终端命令**
可以使用终端通过各种命令获取详细的系统信息。

- 从 `Applications` > `Utilities` > `Terminal` 打开 **Terminal**，或者在 Spotlight 中搜索它。

#### 基本系统信息
```sh
system_profiler SPHardwareDataType
```

#### 详细系统信息
```sh
system_profiler
```

#### CPU 信息
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

#### 安装的软件列表
```sh
ls /Applications
```

#### macOS 版本
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

#### 安装的 Brew 包列表
```sh
brew list
```

#### 安装的 Pip 包列表
```sh
pip list
```

#### 安装的 Gem 包列表
```sh
gem list
```

### 4. **活动监视器**
该应用程序提供了有关 Mac 的 CPU、内存、能源、磁盘和网络使用情况的实时信息。

- 从 `Applications` > `Utilities` > `Activity Monitor` 打开 **Activity Monitor**，或者在 Spotlight 中搜索它。

### 5. **磁盘实用工具**
该应用程序提供了有关存储设备的信息。

- 从 `Applications` > `Utilities` > `Disk Utility` 打开 **Disk Utility**，或者在 Spotlight 中搜索它。

### 6. **第三方工具**
还有一些第三方应用程序，如 **iStat Menus** 和 **CoconutBattery**，提供详细的系统信息和监控功能。

通过这些方法，可以在 macOS 上收集各种系统信息。