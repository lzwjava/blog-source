---
audio: false
generated: true
lang: hant
layout: post
title: 在 Windows 中實施代理檢查
translated: true
type: note
---

要在 Windows 中使用 Git-Bash 和 PowerShell 實現代理檢查，您需要在每個 shell 中設置機制，以偵測何時執行網路相關命令，並在配置代理設置時顯示它們。以下是 Git-Bash 和 PowerShell 的步驟和程式碼。提到的「終端機」很可能是指承載這些 shell 的 Windows Terminal，因此我們將專注於 Git-Bash 和 PowerShell 的實現。

---

### **適用於 Git-Bash**

Git-Bash 是 Windows 上的 Bash 模擬環境，我們可以使用 `DEBUG` trap 在每個命令執行前運行一個函數。目標是檢查命令是否為網路相關，以及是否設置了代理設置，然後顯示它們。

#### **步驟：**

1. **定義網路相關命令列表。**
2. **建立顯示代理設置的函數。**
3. **建立檢查命令和代理設置的函數。**
4. **設置 `DEBUG` trap 在每個命令前運行檢查。**
5. **定義手動 `checkproxy` 函數以按需顯示代理設置。**
6. **將所有配置添加到 `.bashrc` 檔案。**

#### **實現：**

將以下程式碼添加到您的 `~/.bashrc` 檔案（如果不存在，請建立它）：

```bash
# 網路相關命令列表
network_commands=(
    "gpa"
    "git"
    "ssh"
    "scp"
    "sftp"
    "rsync"
    "curl"
    "wget"
    "apt"
    "yum"
    "dnf"
    "npm"
    "yarn"
    "pip"
    "pip3"
    "gem"
    "cargo"
    "docker"
    "kubectl"
    "ping"
    "traceroute"
    "netstat"
    "ss"
    "ip"
    "ifconfig"
    "dig"
    "nslookup"
    "nmap"
    "telnet"
    "ftp"
    "nc"
    "tcpdump"
    "adb"
    "bundle"
    "brew"
    "cpanm"
    "bundle exec jekyll"
    "make"
    "python"
    "glcoud"
)

# 顯示代理設置的函數
display_proxy() {
    echo -e "🚀 **偵測到代理設置：**"
    [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
    [ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
    [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
    [ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
    [ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
    [ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"
    echo ""
}

# 檢查命令是否為網路相關且已設置代理的函數
proxy_check() {
    local cmd
    # 提取命令的第一個單詞
    cmd=$(echo "$BASH_COMMAND" | awk '{print $1}')
    
    for network_cmd in "${network_commands[@]}"; do
        if [[ "$cmd" == "$network_cmd" ]]; then
            # 檢查是否有設置任何代理環境變數
            if [ -n "$HTTP_PROXY" ] || [ -n "$http_proxy" ] || \
               [ -n "$HTTPS_PROXY" ] || [ -n "$https_proxy" ] || \
               [ -n "$ALL_PROXY" ] || [ -n "$all_proxy" ]; then
                display_proxy
            fi
            break
        fi
    done
}

# 設置 DEBUG trap 在每個命令前運行 proxy_check
trap 'proxy_check' DEBUG

# 手動檢查代理設置的函數
checkproxy() {
    echo "HTTP_PROXY: $HTTP_PROXY"
    echo "HTTPS_PROXY: $HTTPS_PROXY"
    echo "Git HTTP Proxy:"
    git config --get http.proxy
    echo "Git HTTPS Proxy:"
    git config --get https.proxy
}
```

#### **運作原理：**

- `network_commands` 陣列列出了網路相關命令。
- `display_proxy` 顯示所有相關的代理環境變數（如果已設置）。
- `proxy_check` 使用 `BASH_COMMAND`（在 `DEBUG` trap 中可用）來取得正在執行的命令，提取第一個單詞，並檢查它是否匹配任何網路命令。如果代理變數已設置，則顯示它們。
- `trap 'proxy_check' DEBUG` 這一行確保 `proxy_check` 在每個命令前運行。
- `checkproxy` 允許您手動查看代理設置，包括 Git 特定的代理配置。
- 將此添加到 `.bashrc` 後，重新啟動 Git-Bash 或運行 `source ~/.bashrc` 以應用更改。

#### **使用方法：**

- 當您運行網路命令（例如 `git clone`、`curl`）時，如果配置了代理設置，它們將在命令執行前顯示。
- 運行 `checkproxy` 以手動查看代理設置。

---

### **適用於 PowerShell**

PowerShell 沒有直接等效於 Bash 的 `DEBUG` trap，但我們可以使用 `PSReadLine` 模組的 `CommandValidationHandler` 來實現類似的功能。此處理程序在每個命令前運行，允許我們檢查網路命令和代理設置。

#### **步驟：**

1. **定義網路相關命令列表。**
2. **建立顯示代理設置的函數。**
3. **設置 `CommandValidationHandler` 以檢查命令和代理設置。**
4. **定義手動 `checkproxy` 函數以按需顯示代理設置。**
5. **將所有配置添加到您的 PowerShell 設定檔。**

#### **實現：**

首先，通過在 PowerShell 中運行 `$PROFILE` 來找到您的 PowerShell 設定檔檔案。如果不存在，請建立它：

```powershell
New-Item -Type File -Force $PROFILE
```

將以下程式碼添加到您的 PowerShell 設定檔（例如 `Microsoft.PowerShell_profile.ps1`）：

```powershell
# 網路相關命令列表
$networkCommands = @(
    "gpa",
    "git",
    "ssh",
    "scp",
    "sftp",
    "rsync",
    "curl",
    "wget",
    "apt",
    "yum",
    "dnf",
    "npm",
    "yarn",
    "pip",
    "pip3",
    "gem",
    "cargo",
    "docker",
    "kubectl",
    "ping",
    "traceroute",
    "netstat",
    "ss",
    "ip",
    "ifconfig",
    "dig",
    "nslookup",
    "nmap",
    "telnet",
    "ftp",
    "nc",
    "tcpdump",
    "adb",
    "bundle",
    "brew",
    "cpanm",
    "bundle exec jekyll",
    "make",
    "python",
    "glcoud"
)

# 顯示代理設置的函數
function Display-Proxy {
    Write-Host "🚀 **偵測到代理設置：**"
    if ($env:HTTP_PROXY) { Write-Host "   - HTTP_PROXY: $env:HTTP_PROXY" }
    if ($env:http_proxy) { Write-Host "   - http_proxy: $env:http_proxy" }
    if ($env:HTTPS_PROXY) { Write-Host "   - HTTPS_PROXY: $env:HTTPS_PROXY" }
    if ($env:https_proxy) { Write-Host "   - https_proxy: $env:https_proxy" }
    if ($env:ALL_PROXY) { Write-Host "   - ALL_PROXY: $env:ALL_PROXY" }
    if ($env:all_proxy) { Write-Host "   - all_proxy: $env:all_proxy" }
    Write-Host ""
}

# 設置 CommandValidationHandler 在執行前檢查命令
Set-PSReadLineOption -CommandValidationHandler {
    param($command)
    # 提取命令的第一個單詞
    $cmd = ($command -split ' ')[0]
    
    if ($networkCommands -contains $cmd) {
        # 檢查是否有設置任何代理環境變數
        if ($env:HTTP_PROXY -or $env:http_proxy -or $env:HTTPS_PROXY -or $env:https_proxy -or $env:ALL_PROXY -or $env:all_proxy) {
            Display-Proxy
        }
    }
    # 始終返回 true 以允許命令執行
    return $true
}

# 手動檢查代理設置的函數
function checkproxy {
    Write-Host "HTTP_PROXY: $env:HTTP_PROXY"
    Write-Host "HTTPS_PROXY: $env:HTTPS_PROXY"
    Write-Host "Git HTTP Proxy:"
    git config --get http.proxy
    Write-Host "Git HTTPS Proxy:"
    git config --get https.proxy
}
```

#### **運作原理：**

- `$networkCommands` 是一個網路相關命令的陣列。
- `Display-Proxy` 顯示所有相關的代理環境變數（如果已設置）。
- `Set-PSReadLineOption -CommandValidationHandler` 定義了一個腳本區塊，在每個命令前運行：
  - 它提取命令的第一個單詞。
  - 檢查它是否在 `$networkCommands` 中。
  - 如果代理變數已設置，則調用 `Display-Proxy`。
  - 返回 `$true` 以確保命令執行。
- `checkproxy` 允許手動查看代理設置，包括 Git 特定的代理。
- 添加到設定檔後，重新啟動 PowerShell 或運行 `. $PROFILE` 以應用更改。

#### **要求：**

- 需要 `PSReadLine` 模組，該模組在 PowerShell 5.1 及更高版本中預設包含。
- 如果使用舊版本，您可能需要升級 PowerShell 或尋找替代方法（此處不涵蓋，因為大多數系統使用較新版本）。

#### **使用方法：**

- 當您運行網路命令（例如 `git pull`、`curl`）時，如果配置了代理設置，它們將在命令執行前顯示。
- 運行 `checkproxy` 以手動查看代理設置。

---

### **關於「終端機」的說明**

- 如果「終端機」指的是 Windows Terminal，它只是一個承載 shell（如 Git-Bash、PowerShell 或 Command Prompt (cmd.exe)）的主機。
- 上述實現適用於 Windows Terminal 中的 Git-Bash 或 PowerShell 會話。
- 在 Command Prompt (cmd.exe) 中實現類似功能不切實際，因為其腳本功能有限。建議改用 Git-Bash 或 PowerShell。

---

### **其他注意事項**

- **命令解析：**
  - 兩種實現僅檢查命令的第一個單詞是否在網路命令列表中。例如，`git clone` 會觸發，因為 `git` 在列表中。
  - 像 `bundle exec jekyll` 這樣的多詞命令如果 `bundle` 在列表中則會觸發，這在大多數情況下已經足夠。
  - 如果需要，您可以修改程式碼以檢查命令中的所有單詞，但這可能導致誤報，通常沒有必要。

- **代理變數：**
  - 兩種實現檢查 `HTTP_PROXY`、`http_proxy`、`HTTPS_PROXY`、`https_proxy`、`ALL_PROXY` 和 `all_proxy` 以涵蓋常見的變體。
  - 在 Windows 中，環境變數不區分大小寫，但為了與類 Unix 行為（尤其是在 Git-Bash 中）保持一致，我們檢查兩種大小寫。

- **Git 代理設置：**
  - 兩種 shell 中的 `checkproxy` 函數使用 `git config --get` 顯示 Git 特定的代理設置。

---

### **測試**

- **設置代理變數：**
  - 在 Git-Bash 中：`export HTTP_PROXY=http://proxy.example.com:8080`
  - 在 PowerShell 中：`$env:HTTP_PROXY = "http://proxy.example.com:8080"`
- **運行網路命令：**
  - 嘗試命令如 `git --version`、`curl -V` 等。
  - 代理設置應在命令輸出前顯示。
- **使用 `checkproxy`：**
  - 在任一 shell 中運行 `checkproxy` 以手動查看代理設置。

---

此實現提供了在 Git-Bash 和 PowerShell 中強大的代理檢查功能，適用於在 Windows Terminal 或獨立環境中使用。