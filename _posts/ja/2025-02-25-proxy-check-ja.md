---
audio: false
generated: true
lang: ja
layout: post
title: Windowsでのプロキシチェックの実装
translated: true
type: note
---

WindowsでGit-BashとPowerShellを使用してプロキシチェックを実装するには、各シェルでネットワーク関連コマンドが実行された際にプロキシ設定が構成されている場合にそれを表示する仕組みを設定する必要があります。以下にGit-BashとPowerShellの両方の手順とコードを示します。ここで言う「ターミナル」はおそらくこれらのシェルをホストするWindows Terminalを指しているため、Git-BashとPowerShellの実装に焦点を当てます。

---

### **Git-Bashの場合**

Git-BashはWindows上のBashエミュレーションであり、`DEBUG`トラップを使用して各コマンド実行前に関数を実行できます。目標は、コマンドがネットワーク関連かどうかを確認し、プロキシ設定がセットされている場合はそれを表示することです。

#### **手順:**

1. **ネットワーク関連コマンドのリストを定義する**
2. **プロキシ設定を表示する関数を作成する**
3. **コマンドとプロキシ設定をチェックする関数を作成する**
4. **各コマンドの前にチェックを実行する`DEBUG`トラップを設定する**
5. **手動でプロキシ設定を表示する`checkproxy`関数を定義する**
6. **すべての設定を`.bashrc`ファイルに追加する**

#### **実装:**

以下のコードを`~/.bashrc`ファイルに追加します（存在しない場合は作成してください）:

```bash
# ネットワーク関連コマンドのリスト
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

# プロキシ設定を表示する関数
display_proxy() {
    echo -e "🚀 **プロキシ設定が検出されました:**"
    [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
    [ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
    [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
    [ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
    [ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
    [ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"
    echo ""
}

# コマンドがネットワーク関連かどうかとプロキシ設定をチェックする関数
proxy_check() {
    local cmd
    # コマンドの最初の単語を抽出
    cmd=$(echo "$BASH_COMMAND" | awk '{print $1}')
    
    for network_cmd in "${network_commands[@]}"; do
        if [[ "$cmd" == "$network_cmd" ]]; then
            # プロキシ環境変数が設定されているかチェック
            if [ -n "$HTTP_PROXY" ] || [ -n "$http_proxy" ] || \
               [ -n "$HTTPS_PROXY" ] || [ -n "$https_proxy" ] || \
               [ -n "$ALL_PROXY" ] || [ -n "$all_proxy" ]; then
                display_proxy
            fi
            break
        fi
    done
}

# 各コマンドの前にproxy_checkを実行するDEBUGトラップを設定
trap 'proxy_check' DEBUG

# 手動でプロキシ設定をチェックする関数
checkproxy() {
    echo "HTTP_PROXY: $HTTP_PROXY"
    echo "HTTPS_PROXY: $HTTPS_PROXY"
    echo "Git HTTP Proxy:"
    git config --get http.proxy
    echo "Git HTTPS Proxy:"
    git config --get https.proxy
}
```

#### **動作の仕組み:**

- `network_commands`配列はネットワーク関連コマンドをリストします
- `display_proxy`は関連するプロキシ環境変数が設定されている場合にそれらを表示します
- `proxy_check`は`DEBUG`トラップで利用可能な`BASH_COMMAND`を使用して実行されるコマンドを取得し、最初の単語を抽出してネットワークコマンドと一致するかチェックします。プロキシ変数が設定されている場合はそれらを表示します
- `trap 'proxy_check' DEBUG`行は各コマンドの前に`proxy_check`が実行されるようにします
- `checkproxy`は手動でプロキシ設定（Git固有のプロキシ設定を含む）を表示できます
- `.bashrc`に追加後、Git-Bashを再起動するか`source ~/.bashrc`を実行して変更を適用します

#### **使用方法:**

- ネットワークコマンド（例: `git clone`, `curl`）を実行すると、プロキシ設定が構成されている場合、コマンド実行前に表示されます
- `checkproxy`を実行して手動でプロキシ設定を表示します

---

### **PowerShellの場合**

PowerShellにはBashの`DEBUG`トラップに直接相当する機能はありませんが、`PSReadLine`モジュールの`CommandValidationHandler`を使用して同様の機能を実現できます。このハンドラーは各コマンドの前に実行され、ネットワークコマンドとプロキシ設定のチェックを可能にします。

#### **手順:**

1. **ネットワーク関連コマンドのリストを定義する**
2. **プロキシ設定を表示する関数を作成する**
3. **コマンドとプロキシ設定をチェックする`CommandValidationHandler`を設定する**
4. **手動でプロキシ設定を表示する`checkproxy`関数を定義する**
5. **すべての設定をPowerShellプロファイルに追加する**

#### **実装:**

まず、PowerShellで`$PROFILE`を実行してプロファイルファイルの場所を確認します。存在しない場合は作成します:

```powershell
New-Item -Type File -Force $PROFILE
```

以下のコードをPowerShellプロファイル（例: `Microsoft.PowerShell_profile.ps1`）に追加します:

```powershell
# ネットワーク関連コマンドのリスト
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

# プロキシ設定を表示する関数
function Display-Proxy {
    Write-Host "🚀 **プロキシ設定が検出されました:**"
    if ($env:HTTP_PROXY) { Write-Host "   - HTTP_PROXY: $env:HTTP_PROXY" }
    if ($env:http_proxy) { Write-Host "   - http_proxy: $env:http_proxy" }
    if ($env:HTTPS_PROXY) { Write-Host "   - HTTPS_PROXY: $env:HTTPS_PROXY" }
    if ($env:https_proxy) { Write-Host "   - https_proxy: $env:https_proxy" }
    if ($env:ALL_PROXY) { Write-Host "   - ALL_PROXY: $env:ALL_PROXY" }
    if ($env:all_proxy) { Write-Host "   - all_proxy: $env:all_proxy" }
    Write-Host ""
}

# コマンド実行前にコマンドとプロキシ設定をチェックするCommandValidationHandlerを設定
Set-PSReadLineOption -CommandValidationHandler {
    param($command)
    # コマンドの最初の単語を抽出
    $cmd = ($command -split ' ')[0]
    
    if ($networkCommands -contains $cmd) {
        # プロキシ環境変数が設定されているかチェック
        if ($env:HTTP_PROXY -or $env:http_proxy -or $env:HTTPS_PROXY -or $env:https_proxy -or $env:ALL_PROXY -or $env:all_proxy) {
            Display-Proxy
        }
    }
    # 常にtrueを返してコマンド実行を許可
    return $true
}

# 手動でプロキシ設定をチェックする関数
function checkproxy {
    Write-Host "HTTP_PROXY: $env:HTTP_PROXY"
    Write-Host "HTTPS_PROXY: $env:HTTPS_PROXY"
    Write-Host "Git HTTP Proxy:"
    git config --get http.proxy
    Write-Host "Git HTTPS Proxy:"
    git config --get https.proxy
}
```

#### **動作の仕組み:**

- `$networkCommands`はネットワーク関連コマンドの配列です
- `Display-Proxy`は関連するプロキシ環境変数が設定されている場合にそれらを表示します
- `Set-PSReadLineOption -CommandValidationHandler`は各コマンドの前に実行されるスクリプトブロックを定義します:
  - コマンドの最初の単語を抽出します
  - `$networkCommands`に含まれているかチェックします
  - プロキシ変数が設定されている場合は`Display-Proxy`を呼び出します
  - コマンド実行を確実にするために`$true`を返します
- `checkproxy`は手動でプロキシ設定（Git固有のプロキシを含む）を表示できます
- プロファイルに追加後、PowerShellを再起動するか`. $PROFILE`を実行して変更を適用します

#### **要件:**

- `PSReadLine`モジュールが必要で、PowerShell 5.1以降にはデフォルトで含まれています
- 古いバージョンを使用している場合は、PowerShellのアップグレードや代替方法の検討が必要です（ここではカバーしません）

#### **使用方法:**

- ネットワークコマンド（例: `git pull`, `curl`）を実行すると、プロキシ設定が構成されている場合、コマンド実行前に表示されます
- `checkproxy`を実行して手動でプロキシ設定を表示します

---

### **「ターミナル」に関する注意点**

- 「ターミナル」がWindows Terminalを指す場合、それは単にGit-Bash、PowerShell、またはコマンドプロンプト（cmd.exe）などのシェルをホストするものです
- 上記の実装はWindows Terminal内のGit-BashまたはPowerShellセッションで動作します
- コマンドプロンプト（cmd.exe）での同様の機能の実装は、スクリプト機能が限られているため実用的ではありません。代わりにGit-BashまたはPowerShellを使用することを推奨します

---

### **追加の考慮事項**

- **コマンド解析:**
  - 両方の実装では、コマンドの最初の単語のみをネットワークコマンドリストと照合します。例えば、`git clone`は`git`がリストにあるためトリガーされます
  - `bundle exec jekyll`のような複数単語のコマンドは、`bundle`がリストにある場合にトリガーされ、ほとんどの場合で十分です
  - 必要に応じて、コマンド内のすべての単語をチェックするようにコードを修正できますが、誤検出の可能性があり、一般的には不要です

- **プロキシ変数:**
  - 両方の実装では、一般的なバリエーションをカバーするために`HTTP_PROXY`、`http_proxy`、`HTTPS_PROXY`、`https_proxy`、`ALL_PROXY`、`all_proxy`をチェックします
  - Windowsでは環境変数は大文字小文字を区別しませんが、Unixライクな動作（特にGit-Bash）との一貫性のために両方のケースをチェックします

- **Gitプロキシ設定:**
  - 両方のシェルの`checkproxy`関数は`git config --get`を使用してGit固有のプロキシ設定を表示します

---

### **テスト**

- **プロキシ変数の設定:**
  - Git-Bash: `export HTTP_PROXY=http://proxy.example.com:8080`
  - PowerShell: `$env:HTTP_PROXY = "http://proxy.example.com:8080"`
- **ネットワークコマンドの実行:**
  - `git --version`、`curl -V`などのコマンドを試します
  - プロキシ設定がコマンド出力の前に表示されるはずです
- **`checkproxy`の使用:**
  - どちらのシェルでも`checkproxy`を実行して手動でプロキシ設定を表示します

---

この実装は、Windows Terminal内またはスタンドアロンでの使用に適した、Git-BashとPowerShellの両方での堅牢なプロキシチェックを提供します。