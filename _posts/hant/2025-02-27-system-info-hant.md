---
audio: true
generated: false
lang: hant
layout: post
title: 系統資訊於 macOS
translated: true
---

要在 macOS 上獲取系統信息，可以使用多種內建工具和命令。以下是一些方法來獲取各種類型的系統信息：

### 1. **系統信息工具**
系統信息應用程式提供有關您的 Mac 硬體和軟體的全面概覽。

- 按 `Cmd + Space` 打開 **Spotlight Search**，輸入「系統信息」，然後按 Enter。
- 或者，您可以從 **Apple 選單** > **關於本機** > **系統報告** 打開它。

### 2. **關於本機**
這提供有關您的 Mac 規格的快速概覽。

- 點擊屏幕左上角的 **Apple 選單**。
- 選擇 **關於本機**。這將顯示基本信息，如 macOS 版本、處理器、記憶體和序列號。

### 3. **終端命令**
您可以使用終端來使用各種命令獲取詳細的系統信息。

- 從 `Applications` > `Utilities` > `Terminal` 打開 **Terminal**，或者在 Spotlight 中搜索它。

#### 基本系統信息
```sh
system_profiler SPHardwareDataType
```

#### 詳細系統信息
```sh
system_profiler
```

#### CPU 信息
```sh
sysctl -n machdep.cpu.brand_string
```

#### 記憶體信息
```sh
sysctl hw.memsize
```

#### 磁碟使用情況
```sh
df -h
```

#### 網絡信息
```sh
ifconfig
```

#### 電池信息（適用於筆記本電腦）
```sh
pmset -g batt
```

#### 已安裝軟體列表
```sh
ls /Applications
```

#### macOS 版本
```sh
sw_vers
```

#### 用戶信息
```sh
id
```

#### 正在運行的進程列表
```sh
ps aux
```

#### 已安裝的 Brew 套件列表
```sh
brew list
```

#### 已安裝的 Pip 套件列表
```sh
pip list
```

#### 已安裝的 Gem 套件列表
```sh
gem list
```

### 4. **活動監視器**
這個應用程式提供有關您的 Mac 的 CPU、記憶體、能源、磁碟和網絡使用情況的即時信息。

- 從 `Applications` > `Utilities` > `Activity Monitor` 打開 **Activity Monitor**，或者在 Spotlight 中搜索它。

### 5. **磁碟工具**
這個應用程式提供有關您的存儲設備的信息。

- 從 `Applications` > `Utilities` > `Disk Utility` 打開 **Disk Utility**，或者在 Spotlight 中搜索它。

### 6. **第三方工具**
還有像 **iStat Menus** 和 **CoconutBattery** 這樣的第三方應用程式，提供詳細的系統信息和監控功能。

通過這些方法，您可以在 macOS 上收集各種系統信息。