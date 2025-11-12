---
audio: false
generated: true
lang: hant
layout: post
title: macOS 系統資訊
translated: true
type: note
---

要獲取 macOS 的系統資訊，你可以使用多種內建工具和指令。以下是幾種取得各類系統資訊的方法：

### 1. **系統資訊工具**
系統資訊應用程式提供 Mac 硬體與軟體的全面概覽。

- 按下 `Cmd + Space` 開啟 **Spotlight 搜尋**，輸入「系統資訊」後按 Enter。
- 或者，你可以透過 **Apple 選單** > **關於這部 Mac** > **系統報告** 開啟。

### 2. **關於這部 Mac**
這裡提供 Mac 規格的快速概覽。

- 點按螢幕左上角的 **Apple 選單**。
- 選擇 **關於這部 Mac**。這裡會顯示基本資訊，如 macOS 版本、處理器、記憶體和序號。

### 3. **終端機指令**
你可以使用終端機並透過各種指令取得詳細系統資訊。

- 從 `應用程式` > `工具程式` > `終端機` 開啟 **終端機**，或透過 Spotlight 搜尋開啟。

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

#### 磁碟使用量
```sh
df -h
```

#### 網路資訊
```sh
ifconfig
```

#### 電池資訊（適用筆記型電腦）
```sh
pmset -g batt
```

#### 已安裝軟體清單
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

#### 執行中程序清單
```sh
ps aux
```

#### 已安裝 Brew 套件清單
```sh
brew list
```

#### 已安裝 Pip 套件清單
```sh
pip list
```

#### 已安裝 Gem 套件清單
```sh
gem list
```

### 4. **活動監視器**
此應用程式提供 Mac 的 CPU、記憶體、能源、磁碟和網路使用量的即時資訊。

- 從 `應用程式` > `工具程式` > `活動監視器` 開啟 **活動監視器**，或透過 Spotlight 搜尋開啟。

### 5. **磁碟工具程式**
此應用程式提供儲存裝置的相關資訊。

- 從 `應用程式` > `工具程式` > `磁碟工具程式` 開啟 **磁碟工具程式**，或透過 Spotlight 搜尋開啟。

### 6. **第三方工具**
也有像 **iStat Menus** 和 **CoconutBattery** 這類第三方應用程式，能提供詳細的系統資訊和監控功能。

透過這些方法，你可以收集 macOS 上各式各樣的系統資訊。