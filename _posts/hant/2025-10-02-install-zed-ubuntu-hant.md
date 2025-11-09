---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-code-fast-1
title: 在 Ubuntu 24.04 上安裝 Zed
translated: true
type: note
---

對於 Ubuntu 24.04 LTS 來說，安裝 Zed（高效能程式碼編輯器）最直接且官方推薦的方法是透過他們提供的 shell 腳本，該腳本原生支援大多數 Linux 發行版，包括像 Ubuntu 這類基於 Debian 的系統。它能自動處理依賴關係，並確保你獲得最新的穩定版本。

### 推薦安裝方式：官方腳本
在終端機中執行以下指令：
```
curl -f https://zed.dev/install.sh | sh
```
- 這會將 Zed 安裝到 `~/.local/bin/zed`（如有需要可加入 PATH：在 `~/.bashrc` 或類似檔案中加入 `export PATH="$HOME/.local/bin:$PATH"`）。
- 必要條件：你的系統（glibc 2.39 on kernel 6.14）需符合要求（x86_64 glibc >= 2.31）。
- 安裝後，可透過終端輸入 `zed` 或從 GNOME 應用程式選單啟動。
- 如需預覽頻道（nightly builds）：`curl -f https://zed.dev/install.sh | ZED_CHANNEL=preview sh`。

若你偏好沙盒化的通用套件（無需擔心原生依賴），可使用你清單中的 Flathub 選項（`dev.zed.Zed`）透過 Flatpak 安裝：
1. 若未安裝 Flatpak，請先安裝：`sudo apt update && sudo apt install flatpak`。
2. 添加 Flathub 軟體庫：`flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo`。
3. 安裝：`flatpak install flathub dev.zed.Zed`。
4. 執行：`flatpak run dev.zed.Zed`。

一般來說，腳本安裝方式更快速且與 GNOME 這類桌面環境整合度更高，但若你希望應用隔離或已習慣使用 Flatpak 管理其他應用，則 Flatpak 是不錯的選擇。請避免使用清單中的其他選項，因為那些是針對非 Debian 發行版所設計，若未經額外設定無法直接在 Ubuntu 上運作。

### 參考資料
- [Zed Linux 安裝文件](https://zed.dev/docs/linux)
- [Zed 登陸 Linux 公告](https://zed.dev/linux)
- [Repology 上的 Zed 套件列表](https://repology.org/project/zed-editor/versions)