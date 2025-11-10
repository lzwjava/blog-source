---
audio: false
generated: true
lang: hant
layout: post
title: Ubuntu Linux 硬件資訊
translated: true
type: note
---

若要在 Ubuntu Linux 系統中獲取筆記型電腦硬體的完整資訊（如記憶體、CPU 等），可結合使用終端機指令與工具。以下為取得詳細系統資訊的逐步指南：

---

### 1. 檢查 CPU 資訊
取得 CPU 詳細資訊（處理器類型、速度、核心數等）：
- 開啟終端機（Ctrl + Alt + T）
- 執行以下指令：
  ```bash
  lscpu
  ```
  - **輸出內容**：顯示 CPU 架構、核心數、執行緒數、時脈速度、快取大小等
- 如需更詳細的 CPU 資訊（包含型號名稱）：
  ```bash
  cat /proc/cpuinfo
  ```
  - 查看 `model name`、`cpu MHz` 及 `cpu cores` 等欄位

---

### 2. 檢查記憶體資訊
查看記憶體總量與使用量：
- 執行：
  ```bash
  free -h
  ```
  - **輸出內容**：以易讀格式顯示記憶體總量、已用量及剩餘量（如 GB 或 MB）
- 取得詳細記憶體資訊（類型、速度與插槽）：
  ```bash
  sudo dmidecode -t memory
  ```
  - **輸出內容**：提供實體記憶體詳細資料，如容量、類型（如 DDR4）、速度與插槽使用狀態（需 root 權限）

---

### 3. 檢查儲存裝置資訊
取得儲存裝置詳細資料：
- 執行：
  ```bash
  lsblk
  ```
  - **輸出內容**：列出所有區塊裝置（如 SSD、HDD）及其容量與掛載點
- 取得磁碟詳細資訊：
  ```bash
  sudo fdisk -l
  ```
  - **輸出內容**：顯示磁碟分割區與容量（需 root 權限）
- 檢查磁碟類型（如 HDD 或 SSD）與型號：
  ```bash
  sudo hdparm -I /dev/sda
  ```
  - 請將 `/dev/sda` 替換為您的磁碟裝置（可透過 `lsblk` 指令查詢）

---

### 4. 檢查顯示卡資訊
取得顯示卡詳細資料：
- 執行：
  ```bash
  lspci | grep -i vga
  ```
  或
  ```bash
  lspci | grep -i nvidia
  ```
  - **輸出內容**：顯示顯示卡型號（如 Intel、NVIDIA、AMD）
- 取得更詳細的 GPU 資訊：
  ```bash
  glxinfo | grep "OpenGL renderer"
  ```
  - 需安裝 `mesa-utils` 套件（若未安裝請執行 `sudo apt install mesa-utils`）
- 針對 NVIDIA 顯示卡：
  ```bash
  nvidia-smi
  ```
  - **輸出內容**：顯示 GPU 使用率、驅動程式版本與視訊記憶體（需已安裝 NVIDIA 驅動程式）

---

### 5. 檢查系統概覽
取得系統完整概覽（CPU、記憶體、主機板等）：
- 執行：
  ```bash
  sudo lshw
  ```
  - **輸出內容**：列出詳細硬體資訊，包含 CPU、記憶體、儲存裝置等（使用 `sudo lshw -short` 可顯示精簡版本）
- 或安裝使用 `hardinfo` 圖形化介面：
  ```bash
  sudo apt install hardinfo
  hardinfo
  ```
  - **輸出內容**：開啟圖形化介面顯示詳細系統資訊（CPU、記憶體、儲存裝置、感測器等）

---

### 6. 檢查 BIOS/UEFI 與主機板資訊
取得 BIOS/UEFI 與主機板詳細資料：
- 執行：
  ```bash
  sudo dmidecode -t bios
  ```
  - **輸出內容**：顯示 BIOS 版本、供應商與發布日期
- 取得主機板詳細資料：
  ```bash
  sudo dmidecode -t baseboard
  ```
  - **輸出內容**：顯示主機板製造商、型號與序號

---

### 7. 檢查作業系統與核心詳細資訊
確認 Ubuntu 版本與核心：
- 執行：
  ```bash
  lsb_release -a
  ```
  - **輸出內容**：顯示 Ubuntu 版本與發布詳細資訊
- 取得核心資訊：
  ```bash
  uname -r
  ```
  - **輸出內容**：顯示 Linux 核心版本

---

### 8. 即時監控系統資源
即時監控 CPU、記憶體與處理程序使用狀況：
- 執行：
  ```bash
  top
  ```
  或
  ```bash
  htop
  ```
  - **注意**：若未安裝 `htop` 請執行 `sudo apt install htop`（提供更友善的操作介面）

---

### 9. 使用 `inxi` 產生完整系統報告
透過單一指令收集全面系統資訊：
- 安裝 `inxi`：
  ```bash
  sudo apt install inxi
  ```
- 執行：
  ```bash
  inxi -Fxz
  ```
  - **輸出內容**：提供詳細報告，包含 CPU、記憶體、顯示卡、儲存裝置、網路等資訊。`-F` 參數產生完整報告，`-x` 參數增加額外細節，`-z` 參數過濾敏感資訊

---

### 範例輸出（使用 `inxi -Fxz`）
```plaintext
System:    Host: ubuntu-laptop Kernel: 5.15.0-73-generic x86_64 bits: 64 Desktop: GNOME 42.0
           Distro: Ubuntu 22.04.2 LTS (Jammy Jellyfish)
Machine:   Type: Laptop System: Dell product: Inspiron 15 v: N/A serial: <filter>
           Mobo: Dell model: 0XYZ serial: <filter> UEFI: Dell v: 1.2.3 date: 05/10/2023
CPU:       Info: 8-core model: Intel Core i7-12700H bits: 64 type: MT MCP cache: L2: 11.5 MiB
           Speed: 2500 MHz min/max: 400/4700 MHz Core speeds (MHz): 1: 2500 2: 2400 ...
Memory:    RAM: total: 15.5 GiB used: 3.2 GiB (20.6%)
           Array-1: capacity: 32 GiB slots: 2 EC: None
           Device-1: DIMM A size: 8 GiB speed: 3200 MT/s type: DDR4
           Device-2: DIMM B size: 8 GiB speed: 3200 MT/s type: DDR4
Graphics:  Device-1: Intel Alder Lake-P Integrated Graphics driver: i915 v: kernel
           Device-2: NVIDIA GA107M [GeForce RTX 3050 Mobile] driver: nvidia v: 535.54.03
           Display: x11 server: X.Org v: 1.21.1.4 driver: X: loaded: modesetting,nvidia
           OpenGL: renderer: Mesa Intel UHD Graphics (ADL-S GT2) v: 4.6 Mesa 23.0.4
Drives:    Local Storage: total: 512 GiB used: 120 GiB (23.4%)
           ID-1: /dev/nvme0n1 vendor: Samsung model: SSD 970 EVO Plus 500GB size: 512 GiB
...
```

---

### 注意事項
- 部分指令（如 `dmidecode`、`fdisk`）需要 root 權限（使用 `sudo`）
- 若指令未安裝（如 `inxi`、`htop`、`mesa-utils`），請透過 `sudo apt install <套件名稱>` 安裝
- 如需圖形化工具，可使用 `hardinfo` 或預裝的 `gnome-system-monitor` 獲得友善操作介面
- 如需特定詳細資訊（如電池狀態、網路介面卡），可提供額外指令

若需要解讀輸出結果或欲聚焦特定元件，請隨時告知！