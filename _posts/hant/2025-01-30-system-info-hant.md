---
audio: false
lang: hant
layout: post
title: 在 macOS 上的系統資訊
translated: true
---

### 獲取 macOS 系統資訊

在 macOS 上獲取系統資訊，可以使用多種內建工具和命令。以下是獲取各種系統資訊的方法：

### 1. **系統資訊工具**

系統資訊應用程式提供您 Mac 硬體和軟體的全面概覽。

- 按 `Cmd + Space` 打開 **Spotlight 搜尋**，輸入「系統資訊」，然後按 Enter。
- 或者，您可以從 **Apple 菜單** > **關於這部 Mac** > **系統報告** 打開它。

### 2. **關於這部 Mac**

這提供您 Mac 規格的快速概覽。

- 點擊屏幕左上角的 **Apple 菜單**。
- 選擇 **關於這部 Mac**。這將顯示基本資訊，如 macOS 版本、處理器、記憶體和序列號。

### 3. **終端命令**

您可以使用終端獲取詳細的系統資訊。

- 從 `應用程式` > `實用工具` > `終端` 打開 **終端**，或在 Spotlight 中搜尋。

#### 基本系統資訊
```sh
system_profiler SPHardwareDataType
```

#### 詳細系統資訊
```sh
system_profiler
```

#### CPU 資訊
```sh
sysctl -n machdep.cpu.brand_string
```

#### 記憶體資訊
```sh
sysctl hw.memsize
```

#### 磁盤使用量
```sh
df -h
```

#### 網路資訊
```sh
ifconfig
```

#### 電池資訊（適用於筆記型電腦）
```sh
pmset -g batt
```

#### 安裝的軟體列表
```sh
ls /Applications
```

#### macOS 版本
```sh
sw_vers
```

#### 使用者資訊
```sh
id
```

#### 運行中的進程列表
```sh
ps aux
```

#### 安裝的 Brew 套件列表
```sh
brew list
```

#### 安裝的 Pip 套件列表
```sh
pip list
```

#### 安裝的 Gem 套件列表
```sh
gem list
```

### 4. **活動監視器**

這個應用程式提供您 Mac 的 CPU、記憶體、能源、磁盤和網路用量的即時資訊。

- 從 `應用程式` > `實用工具` > `活動監視器` 打開 **活動監視器**，或在 Spotlight 中搜尋。

### 5. **磁盤工具**

這個應用程式提供您存儲設備的資訊。

- 從 `應用程式` > `實用工具` > `磁盤工具` 打開 **磁盤工具**，或在 Spotlight 中搜尋。

### 6. **第三方工具**

還有第三方應用程式如 **iStat Menus** 和 **CoconutBattery**，這些應用程式提供詳細的系統資訊和監控功能。

通過使用這些方法，您可以在 macOS 上獲取廣泛的系統資訊。