---
audio: false
generated: true
lang: hant
layout: post
title: 在 Ubuntu 中檢查乙太網路連結速度
translated: true
type: note
---

在 Ubuntu 系統中，你可以使用多種命令行工具來檢查乙太網路連接速度。以下是最常用的方法：

### **1. 使用 `ethtool`（推薦）**
`ethtool` 是檢查乙太網路介面當前連接速度最可靠的方式。

#### 安裝 `ethtool`（如未預先安裝）：
```bash
sudo apt install ethtool
```

#### 檢查連接速度：
```bash
sudo ethtool <介面名稱>
```
請將 `<介面名稱>` 替換為你的乙太網路介面（例如 `eth0`、`enp3s0`、`ens33`）。

#### 範例：
```bash
sudo ethtool enp3s0
```
在輸出結果中尋找 `Speed` 和 `Duplex` 欄位：
```
Settings for enp3s0:
    Supported ports: [ TP ]
    Supported link modes:   10baseT/Half 10baseT/Full 
                            100baseT/Half 100baseT/Full 
                            1000baseT/Full 
    Supported pause frame use: No
    Supports auto-negotiation: Yes
    Supported FEC modes: Not reported
    Advertised link modes:  10baseT/Half 10baseT/Full 
                            100baseT/Half 100baseT/Full 
                            1000baseT/Full 
    Advertised pause frame use: No
    Advertised auto-negotiation: Yes
    Advertised FEC modes: Not reported
    Speed: 1000Mb/s   # <--- 此為當前連接速度
    Duplex: Full      # <--- 全雙工或半雙工模式
    Port: Twisted Pair
    PHYAD: 1
    Transceiver: internal
    Auto-negotiation: on
    MDI-X: on (auto)
    Supports Wake-on: pumbg
    Wake-on: d
    Current message level: 0x00000007 (7)
                           drv probe link
    Link detected: yes      # <--- 顯示網路線是否連接
```

---

### **2. 使用 `ip` 或 `ifconfig`（基礎資訊）**
這些指令能顯示介面是否啟用，但不會直接顯示連接速度。

#### 使用 `ip`：
```bash
ip link show <介面名稱>
```
範例：
```bash
ip link show enp3s0
```
（僅顯示連接狀態，不包含速度資訊）

#### 使用 `ifconfig`（已過時但仍可使用）：
```bash
ifconfig <介面名稱>
```
範例：
```bash
ifconfig enp3s0
```
（顯示介面啟用狀態，但不包含速度資訊）

---

### **3. 使用 `dmesg`（檢查驅動程式記錄）**
有時乙太網路驅動程式會在初始化時記錄協商速度。
```bash
dmesg | grep <介面名稱>
```
範例：
```bash
dmesg | grep enp3s0
```
尋找類似以下的記錄行：
```
[    5.123456] e1000e: enp3s0 NIC Link is Up 1000 Mbps Full Duplex
```

---

### **4. 使用 `mii-tool`（舊版系統適用）**
針對較舊的系統，可嘗試使用 `mii-tool`：
```bash
sudo apt install net-tools
sudo mii-tool -v <介面名稱>
```
範例：
```bash
sudo mii-tool -v eth0
```
（不適用於現代千兆乙太網路環境）

---

### **總結**
- **最佳方式：** `sudo ethtool <介面名稱>`（顯示速度、雙工模式、自動協商狀態）
- **替代方案：** 當 `ethtool` 不可用時，可檢查 `dmesg` 記錄
- **基礎狀態檢查：** `ip link show` 或 `ifconfig`（不顯示速度資訊）

如需進一步說明，歡迎隨時詢問！🚀