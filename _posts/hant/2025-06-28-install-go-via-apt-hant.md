---
audio: false
generated: true
lang: hant
layout: post
title: 在 Debian 上透過 APT 安裝 Go
translated: true
type: note
---

若要在基於 Debian 的 Linux 系統（例如 Ubuntu）上使用 `apt` 安裝 Go，請按照以下步驟操作。請注意，`apt` 可能會安裝較舊版本的 Go（例如在 Ubuntu 22.04 上安裝 1.18 版），因此你應驗證其是否符合專案需求（請檢查 `~/Projects/clash-core` 中的 `go.mod` 檔案以確認所需的 Go 版本）。

### 使用 APT 安裝 Go 的步驟

1. **更新套件索引**
   - 確保你的套件清單是最新的：
     ```bash
     sudo apt update
     ```

2. **安裝 Go**
   - 安裝 Go 套件：
     ```bash
     sudo apt install golang-go
     ```
   - 這將安裝 Go 編譯器、工具和標準函式庫。

3. **驗證安裝**
   - 檢查已安裝的 Go 版本：
     ```bash
     go version
     ```
   - 你應該會看到類似以下的輸出：
     ```
     go version go1.18.1 linux/amd64
     ```
     （實際版本取決於你的發行版套件庫。）

4. **設定 GOPATH（可選）**
   - 現代 Go 版本（1.13+）使用模組，因此 `GOPATH` 是可選的，但設定它對某些專案可能有用。
   - 編輯你的 shell 設定檔（例如 `~/.bashrc` 或 `~/.zshrc`）：
     ```bash
     nano ~/.bashrc
     ```
   - 加入以下內容：
     ```bash
     export GOPATH=$HOME/go
     export PATH=$PATH:$GOPATH/bin
     ```
   - 儲存並重新載入 shell 設定：
     ```bash
     source ~/.bashrc
     ```

5. **重新嘗試建構**
   - 切換到你的專案目錄：
     ```bash
     cd ~/Projects/clash-core
     ```
   - 再次執行 `make` 指令：
     ```bash
     make
     ```

### 注意事項
- **版本檢查**：如果你的專案需要較新的 Go 版本（例如 1.20 或更高），`apt` 版本可能已過時。請檢查 `go.mod` 或專案文件中的所需版本。如有需要，可從 [https://go.dev/dl/](https://go.dev/dl/) 手動下載 tarball 安裝新版（如先前回應所述）。
- **替代套件庫**：若要透過 `apt` 安裝較新版本，可加入第三方 PPA（例如在 Ubuntu 上使用 `ppa:longsleep/golang-backports`）。執行：
  ```bash
  sudo add-apt-repository ppa:longsleep/golang-backports
  sudo apt update
  sudo apt install golang-go
  ```
- **疑難排解**：
  - 若找不到 `go` 指令，請確認 `/usr/bin/go` 是否存在（使用 `ls /usr/bin/go`）。若不存在，請用 `sudo apt install --reinstall golang-go` 重新安裝。
  - 若出現相依性錯誤，請執行 `sudo apt install -f` 進行修復。
  - 若遇到權限問題，請確保你擁有 `sudo` 權限。

### 來源
- Ubuntu Go 安裝指南：[https://ubuntu.com/server/docs/programming-go](https://ubuntu.com/server/docs/programming-go)
- 一般 apt 使用方式：[https://help.ubuntu.com/community/AptGet/Howto](https://help.ubuntu.com/community/AptGet/Howto)

如果安裝的版本過舊或遇到問題，請告訴我你的 Linux 發行版（例如 Ubuntu 22.04）和所需的 Go 版本，我將進一步指導你！