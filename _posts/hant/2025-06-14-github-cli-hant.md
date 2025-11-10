---
audio: false
generated: true
lang: hant
layout: post
title: 安裝 GitHub 命令行工具
translated: true
type: note
---

若要在 Ubuntu 上安裝 GitHub CLI (`gh`) 並使用 `gh workflow run` 指令觸發 GitHub Actions 工作流程，請遵循以下步驟：

### 在 Ubuntu 上安裝 GitHub CLI (`gh`) 的步驟

1. **新增 GitHub CLI 儲存庫與 GPG 金鑰**：
   在終端機中執行以下指令以設定官方 GitHub CLI 套件儲存庫：

   ```bash
   (type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
   && sudo mkdir -p -m 755 /etc/apt/keyrings \
   && wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
   && sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
   && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
   ```

   此腳本會：
   - 若尚未安裝則安裝 `wget`
   - 建立 APT 金鑰環目錄
   - 下載並新增 GitHub CLI GPG 金鑰
   - 為您的系統設定 GitHub CLI 儲存庫

2. **更新套件索引並安裝 `gh`**：
   更新套件清單並安裝 `gh` 指令列工具：

   ```bash
   sudo apt update
   sudo apt install gh -y
   ```

3. **驗證安裝**：
   執行以下指令檢查 `gh` 是否正確安裝：

   ```bash
   gh --version
   ```

   您應會看到類似 `gh version X.Y.Z (YYYY-MM-DD)` 的輸出，確認安裝成功。

4. **向 GitHub 進行身份驗證**：
   在使用 `gh` 前，請先向您的 GitHub 帳戶進行身份驗證：

   ```bash
   gh auth login
   ```

   依照提示操作：
   - 選擇 `GitHub.com`（或適用的企業伺服器）
   - 選擇偏好的通訊協定（`HTTPS` 或 `SSH`；若已設定 SSH 金鑰則推薦使用 `SSH`）
   - 選擇身份驗證方法（瀏覽器方式最簡便，會開啟網頁登入頁面）
   - 複製提供的一次性代碼，貼入瀏覽器並授權 `gh`
   - 確認預設設定或按需調整

   成功驗證後，您將看到確認訊息。

### 使用 `gh workflow run` 操作 GitHub Actions

`gh workflow run` 指令可觸發 GitHub Actions 工作流程。使用方法如下：

1. **導航至您的儲存庫**（可選）：
   若您位於連結至 GitHub 的本機 Git 儲存庫中，`gh` 會自動偵測。否則請使用 `--repo` 旗標指定儲存庫。

2. **列出可用工作流程**（可選）：
   若要查詢工作流程 ID 或檔案名稱，請執行：

   ```bash
   gh workflow list
   ```

   此指令會顯示儲存庫中的所有工作流程，包括名稱、ID 與狀態（例如 `active`）。

3. **執行工作流程**：
   使用 `gh workflow run` 指令並指定工作流程的檔案名稱或 ID。例如：

   ```bash
   gh workflow run workflow.yml
   ```

   或使用工作流程 ID（例如 `123456`）：

   ```bash
   gh workflow run 123456
   ```

   若工作流程接受輸入參數，請使用 `--field` 旗標提供：

   ```bash
   gh workflow run workflow.yml --field key=value
   ```

   若要指定分支或參照，請使用 `--ref` 旗標：

   ```bash
   gh workflow run workflow.yml --ref branch-name
   ```

4. **監控工作流程**：
   觸發後，可檢查執行狀態：

   ```bash
   gh run list
   ```

   若要即時監控特定執行，請使用：

   ```bash
   gh run watch <run-id>
   ```

   請將 `<run-id>` 替換為 `gh run list` 中的執行 ID。

### 疑難排解提示

- **GPG 簽章錯誤**：若在 `apt update` 過程中遇到 GPG 相關問題，請參考 GitHub 的問題追蹤器以尋求修復（例如 `cli/cli#9569`）或重新執行金鑰匯入步驟。[](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- **防火牆問題**：若 `keyserver.ubuntu.com` 連線失敗，請嘗試：

   ```bash
   sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key C99B11DEB97541F0
   ```

   或視需要安裝 `dirmngr`：

   ```bash
   sudo apt-get install dirmngr
   ```

  [](https://gist.github.com/Manoj-Paramsetti/dc957bdd6a4430275d0fc28a0dc43ae9)
- **Snap 安裝警告**：GitHub 不建議使用 Snap 套件安裝 `gh`，因可能存在執行階段問題。請遵循上述 APT 安裝方式。[](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)
- **身份驗證範圍**：若 `gh workflow run` 因權限問題失敗，請確認您的 token 具有 `workflow` 範圍。可透過以下指令重新驗證：

   ```bash
   gh auth refresh -s workflow
   ```

### 補充說明

- **GitHub CLI 手冊**：有關 `gh` 指令的詳細資訊，請執行 `gh help` 或造訪官方手冊 [cli.github.com](https://cli.github.com)。[](https://cli.github.com/manual/)
- **工作流程需求**：請確認工作流程檔案（例如 `workflow.yml`）存在於儲存庫的 `.github/workflows/` 目錄中，且設定為手動觸發（例如 `workflow_dispatch` 事件）。
- **替代安裝方式**：您亦可透過 Homebrew（`brew install gh`）或從[發佈頁面](https://github.com/cli/cli/releases)下載二進位檔安裝 `gh`，但建議 Ubuntu 用戶使用 APT 安裝方式。[](https://github.com/cli/cli)

此設定讓您能在 Ubuntu 上透過指令列高效管理 GitHub Actions 工作流程。如需特定 `gh` 指令或工作流程設定的協助，請隨時告知！