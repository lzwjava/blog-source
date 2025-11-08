---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 無需修改源代碼安裝 DirB
translated: true
type: note
---

### 無需修改 DirB 原始碼的替代方案

若因唯讀設定、政策限制或個人偏好而無法編輯原始碼（例如 `variables.h`），以下提供幾種無需編譯即可運行 DirB 的簡便方法。這些方案採用預先編譯套件或重新實作版本，本文將以 Linux 系統（根據您的編譯路徑）為重點，但亦會註明各作業系統的調整要點。

#### 1. **透過套件管理器安裝（最適用於 Debian/Ubuntu/Kali）**
   DirB 已收錄於多數發行版的套件庫中，可直接安裝預編譯版本，無需修改原始碼或進行編譯。
   - **Kali Linux**（推薦用於滲透測試工具）：
     ```
     sudo apt update
     sudo apt install dirb
     ```
     - 此為 Kali 官方支援維護的版本。[Kali 工具頁面](https://www.kali.org/tools/dirb/)
   - **Ubuntu/Debian**：
     ```
     sudo apt update
     sudo apt install dirb
     ```
     - 若找不到套件（舊版可能未收錄），請啟用 universe 套件庫：`sudo add-apt-repository universe && sudo apt update`
   - **驗證**：安裝後執行 `dirb --help`，字典檔位於 `/usr/share/dirb/wordlists/`
   - **運作原理**：套件版本已在上游修復所有問題（包含多重定義錯誤）

   其他發行版安裝方式：
   - **Fedora/RHEL**：`sudo dnf install dirb`（若存於 EPEL 套件庫，請先執行 `sudo dnf install epel-release`）
   - **Arch**：`sudo pacman -S dirb`

#### 2. **使用 Python 重製版（跨平台、無需 C 編譯）**
   原始 DirB 基於 C 語言且編譯過程繁瑣，但現有功能相同（甚至更佳）的現代 Python 移植版，可透過 pip 直接安裝，無需調整原始碼。
   - **專案庫**：[ct-Open-Source/dirb on GitHub](https://github.com/ct-Open-Source/dirb)
   - **安裝**：
     ```
     pip install git+https://github.com/ct-Open-Source/dirb.git
     ```
     - 或克隆專案：`git clone https://github.com/ct-Open-Source/dirb.git && cd dirb && pip install .`
   - **用法**：與原始版本相同，例如 `dirb https://example.com /usr/share/wordlists/dirb/common.txt`
   - **優點**：持續維護、部分情境速度更快、支援 Mac/Windows/Linux，額外包含遞歸掃描功能
   - **缺點**：非「官方」二進位檔，但輸出結果高度吻合

#### 3. **下載預編譯二進位檔（選擇有限）**
   - 官方 SourceForge 發布多為原始碼壓縮檔（如 dirb222.tar.gz），仍須編譯
   - 雖無通用二進位檔，但若使用 Kali/Parrot OS 建議優先採用套件安裝
   - 替代技巧：透過 Docker 執行 Kali 映像檔並運行 DirB：
     ```
     docker run -it kalilinux/kali-rolling dirb http://example.com
     ```
     - 無需安裝，容器已預先配置完成

#### 方案比較表

| 方案                | 支援平台            | 部署難度 | 備註 |
|---------------------|---------------------|--------|-------|
| **Apt/DNF/Pacman** | Linux (Debian/Fedora/Arch) | 低 | 預編譯版本；含字典檔 |
| **Python 移植版**  | 全平台 (Python 3+) | 低 | 現代化替代方案；僅需 pip |
| **Docker**         | 全平台 (需 Docker) | 中 | 環境隔離；免主機安裝 |

若上述方案皆不適用（如受限環境），可考慮改用 Gobuster（`go install github.com/OJ/gobuster/v3@latest`）—— 基於 Go 語言開發，編譯順暢且功能同為目錄爆破工具。

請提供您使用的作業系統以便進一步縮小建議範圍。若遭遇問題，請分享錯誤訊息/輸出結果。