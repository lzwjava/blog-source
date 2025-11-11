---
audio: false
generated: true
lang: hant
layout: post
title: Linux 系統資訊
translated: true
type: note
---

在 Ubuntu 系統中，你可以透過以下指令獲取系統資訊，例如系統是 32 位元還是 64 位元、作業系統版本、記憶體容量及磁碟大小。以下是逐步操作指南：

### 1. 判斷系統為 32 位元或 64 位元
- **指令**：`uname -m`
- **說明**：此指令會顯示機器硬體名稱。
  - 若輸出為 `x86_64`，則你的系統是 **64 位元**。
  - 若輸出為 `i686` 或 `i386`，則你的系統是 **32 位元**。
- **範例輸出**：
  ```
  x86_64
  ```
  這表示系統為 64 位元。

### 2. 取得作業系統版本
- **指令**：`lsb_release -a`
- **說明**：此指令提供 Linux Standard Base (LSB) 與發行版的詳細資訊。
  - 查看 `Description` 行即可得知 Ubuntu 版本。
- **範例輸出**：
  ```
  No LSB modules are available.
  Distributor ID: Ubuntu
  Description:    Ubuntu 20.04.3 LTS
  Release:        20.04
  Codename:       focal
  ```
  此處顯示作業系統為 **Ubuntu 20.04.3 LTS**。

### 3. 取得記憶體容量
- **指令**：`free -h`
- **說明**：此指令以易讀格式顯示記憶體使用狀況。
  - 查看 `Mem:` 列中 `total` 欄位的數值，即為總記憶體容量。
- **範例輸出**：
  ```
              total        used        free      shared  buff/cache   available
  Mem:          15Gi       2.3Gi       9.5Gi       300Mi       3.8Gi        12Gi
  Swap:        2.0Gi         0B       2.0Gi
  ```
  此範例中的總記憶體容量為 **15 GB**。

### 4. 取得磁碟容量
- **指令**：`lsblk -d -o NAME,SIZE`
- **說明**：此指令列出所有磁碟裝置的容量資訊。
  - `-d` 參數確保僅顯示磁碟裝置，不包含分割區。
  - 尋找磁碟名稱及其對應的容量數值。
- **範例輸出**：
  ```
  NAME   SIZE
  sda    1T
  sdb    500G
  ```
  此範例顯示系統有兩顆磁碟：`/dev/sda` 容量為 **1 TB**，`/dev/sdb` 容量為 **500 GB**。若系統僅有一顆磁碟，通常會顯示為 `sda`。

### 注意事項
- 上述指令皆使用 Ubuntu 內建工具，無需額外安裝軟體。
- 關於磁碟容量：若系統配備多顆磁碟，輸出將列出所有裝置。通常 `/dev/sda` 會是主要磁碟。
- 在終端機中執行這些指令，即可查看專屬於你系統的詳細資訊。

透過這些指令，你就能快速獲取 Ubuntu 電腦上所需的關鍵系統資訊！