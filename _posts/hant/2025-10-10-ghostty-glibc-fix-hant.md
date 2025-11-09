---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 解決 Ghostty GLIBC 版本衝突
translated: true
type: note
---

您遇到的問題不僅僅是安裝衝突——主要是因為 Snap 和您下載的 `.deb` 套件都是針對 GLIBC 2.38（來自 Ubuntu 24.04）建置的，但您的系統是 Ubuntu 22.04（根據您 `libc-bin` 套件中的 GLIBC 2.35 版本）。這導致在嘗試執行二進位檔時出現「version `GLIBC_2.38' not found」錯誤。同時啟用兩個安裝也可能導致路徑衝突（例如，執行哪個 `ghostty` 二進位檔），所以是的，您應該先移除它們以清理環境。

### 步驟 1：移除現有安裝
執行以下指令來解除安裝兩者：
```
sudo snap remove ghostty
sudo apt remove ghostty
```
- 這將移除 Snap 版本和 `.deb` 版本，不會影響系統的其他部分。
- 使用 `which ghostty`（應不返回任何內容）和 `snap list | grep ghostty`（應為空）來驗證移除。

### 步驟 2：安裝相容版本
Ghostty 目前尚未提供 Ubuntu 22.04 的官方 `.deb` 套件，但有一個可靠的非官方儲存庫為其（及其他版本）建置相容的 `.deb` 檔案。它會自動處理 GLIBC 相容性問題。

最簡單的方法是使用他們的自動安裝腳本，該腳本會偵測您的 Ubuntu 版本並取得正確的套件：
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/mkasberg/ghostty-ubuntu/HEAD/install.sh)"
```
- 這會下載並安裝最新的相容 `.deb` 套件（截至近期版本，目前約為 v1.2.x）。
- 完成後，執行 `ghostty` 進行測試——它應該能啟動而不出現 GLIBC 錯誤。
- 如果在安裝過程中看到任何相依性提示（例如 `libonig5`），請輸入 `Y` 批准。

如果您偏好手動安裝：
1. 前往 [發布頁面](https://github.com/mkasberg/ghostty-ubuntu/releases)。
2. 下載標示為 Ubuntu 22.04 的 `.deb` 檔案（例如，名稱類似 `ghostty_1.2.1-0.ppa1_amd64_22.04.deb`——確切名稱因發布而異）。
3. 使用 `sudo dpkg -i ghostty_*.deb` 進行安裝（請在下載資料夾中執行）。
4. 如果它抱怨缺少相依套件，請使用 `sudo apt install -f` 進行修復。

### 補充說明
- **為何不需要從原始碼建置**：非官方儲存庫已為您處理了繁重的工作，但如果您想自行建置 Ghostty（例如，為了自訂版本），請遵循[官方原始碼建置指南](https://ghostty.org/docs/install/build)。它需要 Zig 0.13 和一些相依套件如 `libgtk-4-dev`，但使用 `.deb` 途徑更為簡單。
- **考慮升級 Ubuntu？** 如果您可以接受，升級到 24.04 將讓您能夠使用官方 Snap 或您之前嘗試的 24.04 `.deb` 而無需擔心問題。
- 安裝後，您可以透過 `~/.config/ghostty/config` 來配置 Ghostty（請參閱[文件](https://ghostty.org/docs/config)以了解選項）。

如果您在這些步驟中遇到任何錯誤，請將輸出內容貼到這裡以獲得進一步協助！