---
audio: false
generated: true
lang: hant
layout: post
title: 修復 macOS 上找不到 Go 指令的問題
translated: true
type: note
---

錯誤訊息 `/bin/sh: go: command not found` 表示您的 macOS 系統未安裝 Go 程式語言，或者未在 PATH 中正確配置。`make` 指令試圖執行 Go 建置過程，這需要 Go 編譯器 (`go`)。以下是 macOS 上安裝 Go 並解決此問題的步驟。

### macOS 安裝 Go 的步驟

有兩種主要方式可在 macOS 上安裝 Go：使用官方 Go 安裝程式或使用 Homebrew。我將介紹兩種方法，但 Homebrew 對 macOS 用戶來說通常更簡單。請根據您的偏好選擇一種方法。

#### 先決條件
- 確保您的 macOS 版本為 10.10 或更高版本，以相容於最近的 Go 版本。
- 您需要管理員權限才能安裝 Go 並修改系統檔案。
- 終端機應用程式（位於 應用程式 > 工具程式 > 終端機）。

#### 方法 1：使用 Homebrew 安裝 Go（推薦）
Homebrew 是 macOS 上流行的套件管理員，可簡化軟體安裝。

1. **安裝 Homebrew（如果尚未安裝）**：
   - 開啟終端機並執行：
     ```bash
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```
   - 按照螢幕上的指示完成安裝。

2. **安裝 Go**：
   - 執行以下指令以安裝最新版本的 Go：
     ```bash
     brew install go
     ```
   - 這會將 Go 安裝到 `/usr/local/Cellar/go`（或類似路徑），並將 Go 二進位檔新增至 `/usr/local/bin`。

3. **驗證安裝**：
   - 執行以下指令檢查安裝的 Go 版本：
     ```bash
     go version
     ```
   - 您應該會看到類似 `go version go1.23.x darwin/amd64` 的輸出，確認 Go 已安裝。

4. **設定環境變數（如果需要）**：
   - Homebrew 通常會自動將 Go 新增到您的 PATH 中，但如果 `go` 指令無效，請將 Go 二進位檔路徑新增到您的 shell 設定檔：
     - 開啟或建立適當的 shell 設定檔（例如，`~/.zshrc` 適用於 Zsh，這是 macOS Catalina 之後的預設 shell，或 `~/.bash_profile` 適用於 Bash）：
       ```bash
       nano ~/.zshrc
       ```
     - 新增以下行：
       ```bash
       export PATH=$PATH:/usr/local/go/bin
       ```
     - 儲存檔案（在 nano 中按 Ctrl+X，然後按 Y，然後按 Enter）並套用變更：
       ```bash
       source ~/.zshrc
       ```
     - 如果您想使用自訂工作區，請設定 `GOPATH`（可選，因為 Go modules 通常不需要此設定）：
       ```bash
       export GOPATH=$HOME/go
       export PATH=$PATH:$GOPATH/bin
       ```
     - 再次 source 設定檔：
       ```bash
       source ~/.zshrc
       ```

5. **測試 Go 安裝**：
   - 再次執行 `go version` 以確保指令被識別。
   - 可選地，建立一個簡單的 Go 程式以確認一切正常：
     ```bash
     mkdir -p ~/go/src/hello
     nano ~/go/src/hello/main.go
     ```
     - 新增以下程式碼：
       ```go
       package main
       import "fmt"
       func main() {
           fmt.Println("Hello, World!")
       }
       ```
     - 儲存並退出（Ctrl+X, Y, Enter），然後編譯並執行：
       ```bash
       cd ~/go/src/hello
       go run main.go
       ```
     - 您應該會看到 `Hello, World!` 作為輸出。

#### 方法 2：使用官方安裝程式安裝 Go
如果您不想使用 Homebrew，可以使用官方 macOS 套件安裝 Go。

1. **下載 Go 安裝程式**：
   - 訪問官方 Go 下載頁面：https://go.dev/dl/
   - 為您的系統架構下載 macOS 套件（`.pkg`）（例如，`go1.23.x.darwin-amd64.pkg` 適用於 Intel Mac，`go1.23.x.darwin-arm64.pkg` 適用於 Apple Silicon）。

2. **執行安裝程式**：
   - 在 Finder 中雙擊下載的 `.pkg` 檔案。
   - 按照螢幕上的指示安裝 Go。預設情況下，它將安裝到 `/usr/local/go`。
   - 您可能需要輸入管理員密碼。

3. **設定環境變數**：
   - 開啟終端機並編輯您的 shell 設定檔（例如，`~/.zshrc` 或 `~/.bash_profile`）：
     ```bash
     nano ~/.zshrc
     ```
   - 新增以下行：
     ```bash
     export GOROOT=/usr/local/go
     export GOPATH=$HOME/go
     export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
     ```
   - 儲存並套用變更：
     ```bash
     source ~/.zshrc
     ```
   - 注意：除非您正在開發 Go 本身或需要非標準安裝路徑，否則 `GOROOT` 是可選的。現代 Go 版本通常不需要設定 `GOROOT`。

4. **驗證安裝**：
   - 執行：
     ```bash
     go version
     ```
   - 您應該會看到安裝的 Go 版本（例如，`go version go1.23.x darwin/amd64`）。

5. **測試 Go 安裝**：
   - 按照方法 1 的步驟 5 建立並執行 "Hello, World!" 程式。

#### 疑難排解原始問題
安裝 Go 後，返回您的 `clash-core` 目錄並重試 `make` 指令：
```bash
cd /path/to/clash-core
make
```

如果您遇到問題：
- **代理設定**：您的終端機輸出顯示 `HTTP_PROXY` 和 `HTTPS_PROXY` 設定為 `http://127.0.0.1:7890`。請確保您的代理處於活動狀態且不會干擾 Go 的網路存取（例如，下載依賴項）。您可以暫時停用代理進行測試：
  ```bash
  unset HTTP_PROXY HTTPS_PROXY
  make
  ```
- **權限**：如果出現權限錯誤，請確保您對專案目錄和 Go 工作區（`$GOPATH` 或 `$HOME/go`）具有寫入權限。
- **Go Modules**：`clash-core` 專案可能使用 Go modules。請確保您在包含 `go.mod` 的正確目錄中，並在執行 `make` 之前執行 `go mod tidy` 以取得依賴項：
  ```bash
  go mod tidy
  make
  ```
- **架構不符**：`make` 指令正在為 `linux-amd64`（`GOOS=linux GOARCH=amd64`）建置。如果您打算在 macOS 上執行二進位檔，則可能需要修改 Makefile 或建置指令以目標為 `darwin-amd64`（適用於 Intel Mac）或 `darwin-arm64`（適用於 Apple Silicon）。檢查 Makefile 中的 `linux-amd64` 目標並進行調整，或執行：
  ```bash
  GOARCH=amd64 GOOS=darwin CGO_ENABLED=0 go build -trimpath -ldflags '-X "github.com/Dreamacro/clash/constant.Version=1.18" -X "github.com/Dreamacro/clash/constant.BuildTime=Sat Jun 28 12:24:27 UTC 2025" -w -s -buildid=' -o bin/clash-darwin-amd64
  ```
  如果您使用的是 Apple Silicon，請將 `amd64` 替換為 `arm64`。

#### 補充說明
- **解除安裝舊版 Go**：如果之前安裝過 Go，請移除它以避免衝突：
  ```bash
  sudo rm -rf /usr/local/go
  sudo rm -f /etc/paths.d/go
  ```
  然後使用上述方法之一重新安裝。
- **Go 工作區**：如果您設定了 `GOPATH`，請建立目錄：
  ```bash
  mkdir -p $HOME/go/{bin,src,pkg}
  ```
  但是，對於使用 Go modules 的大多數現代專案（如 `clash-core`），`GOPATH` 不那麼重要。
- **Xcode Command Line Tools**：某些 Go 專案需要 C 依賴項（例如，`CGO_ENABLED=1`）。如果需要，請安裝 Xcode Command Line Tools：
  ```bash
  xcode-select --install
  ```
- **多個 Go 版本**：如果您需要多個 Go 版本，請考慮使用版本管理員，例如 `gvm`（透過 Homebrew 或指令碼安裝）。

#### 驗證
一旦 Go 安裝成功且 `make` 指令執行成功，`clash-core` 二進位檔應出現在 `bin/` 目錄中（例如，`bin/clash-linux-amd64` 或 `bin/clash-darwin-amd64`）。透過執行以下指令驗證其是否正常運作：
```bash
./bin/clash-darwin-amd64 --version
```

如果您需要進一步協助或遇到特定錯誤，請告訴我確切的錯誤訊息或上下文，我可以提供更有針對性的幫助！