---
audio: false
generated: false
image: false
lang: hant
layout: post
title: Zsh 設定檔
translated: true
type: post
---

此 zsh 設定檔旨在提升命令列體驗，重點放在代理配置、Git 整合和實用別名。以下各節詳細說明其功能：

**1. PATH 配置：**

   - `export PATH=...`：此行設置 `PATH` 環境變量，告訴 shell 在哪裡查找可執行文件。它包括各種目錄，如 Java、Ruby、Homebrew、Python、Flutter 和 Google Cloud SDK。這確保可以直接從終端運行這些工具的命令。

**2. 代理管理：**

   - `export GLOBAL_PROXY='127.0.0.1:7890'`：此變量 `GLOBAL_PROXY` 保存代理伺服器地址。
   - `function start_proxy { ... }`：此函數設置 `HTTP_PROXY`、`HTTPS_PROXY`、`http_proxy`、`https_proxy` 和 `ALL_PROXY` 環境變量以使用指定的代理。它還禁用代理的完整 URI 請求。
   - `function start_proxy_without_prefix { ... }`：類似於 `start_proxy`，但設置代理變量時不包含 `http://` 前綴。
   - `function stop_proxy { ... }`：此函數取消設置代理變量，有效禁用代理。它還啟用代理的完整 URI 請求。
   - `export NO_PROXY="localhost,127.0.0.1,.example.com,::1"`：此變量列出應繞過代理的主機。

**3. Git 代理：**

   - `function start_git_proxy { ... }`：此函數配置 git 使用全局代理進行 HTTP 和 HTTPS 連接。
   - `function stop_git_proxy { ... }`：此函數取消 git 代理設置。

**4. Homebrew 整合：**

   - `eval "$(/opt/homebrew/bin/brew shellenv)"`：此行將 Homebrew 整合到 shell 環境中，允許使用 Homebrew 命令。

**5. 便捷別名：**

   - `alias gpa='python ~/bin/gitmessageai.py --api mistral'`：此別名 `gpa` 用於運行 python 腳本 `gitmessageai.py` 並使用 mistral API。
   - `alias gca='python ~/bin/gitmessageai.py --no-push'`：此別名 `gca` 用於運行相同腳本而不推送更改。
   - `alias gm='python ~/bin/gitmessageai.py --only-message'`：此別名 `gm` 用於運行相同腳本並僅打印提交信息。
   - `alias gpam=/usr/local/bin/git-auto-commit`：此別名 `gpam` 用於運行 `git-auto-commit` 腳本。
   - `alias rougify=/Users/lzwjava/projects/rouge/bin/rougify`：此別名 `rougify` 用於運行 `rougify` 腳本。

**6. SSL 證書：**

   - `export SSL_CERT_FILE=~/bin/cacert.pem`：此變量設置自定義 SSL 證書文件的路徑。

**7. Homebrew 自動更新：**

   - `export HOMEBREW_NO_AUTO_UPDATE=1`：此變量禁用 Homebrew 的自動更新。

**8. 預執行代理檢查：**

   - `preexec() { ... }`：此函數在每個命令之前執行。它檢查命令是否在網絡依賴命令列表中。如果是，且如果設置了任何代理變量，則顯示代理設置。
   - `local network_commands=( ... )`：此數組列出被認為是網絡依賴的命令。
   - `display_proxy() { ... }`：此函數顯示當前代理設置。

**9. Google Cloud SDK 補全：**

   - `if [ -f '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc'; fi`：此行啟用 gcloud 的 shell 命令補全。

**10. API 密鑰和憑據：**

    - `export GOOGLE_APPLICATION_CREDENTIALS="/Users/lzwjava/bin/graphite-ally-445108-k3-035f0952219d.json"`：設置 Google Cloud 服務帳戶憑據的路徑。
    - `export DEEPSEEK_API_KEY="xxx"`：設置 DeepSeek API 密鑰。
    - `export MISTRAL_API_KEY="xxx"`：設置 Mistral API 密鑰。
    - `export DYLD_LIBRARY_PATH=$(brew --prefix curl)/lib`：設置 curl 的動態庫路徑。
    - `export SPEECH_ENDPOINT="https://ai-lzwjava-5596.cognitiveservices.azure.com/"`：設置 Azure 語音端點。
    - `export DO_API_KEY="xxx"`：設置 Digital Ocean API 密鑰。
    - `export GEMINI_API_KEY="xxx"`：設置 Gemini API 密鑰。

**11. Conda 環境：**

    - `conda activate base`：激活基礎 conda 環境。

**總結，此 zsh 設定檔為開發者提供了一個全面的設置，包括：**

- 使用函數啟動和停止代理的簡便代理管理。
- Git 代理配置。
- Homebrew 整合。
- 常見任務的便捷別名。
- 網絡依賴命令的預執行代理檢查。
- 各種服務的 API 密鑰和憑據。
- Conda 環境激活。

此設定檔旨在簡化用戶工作流程，並使管理各種開發工具和服務更加輕鬆。

```bash
export PATH=/opt/homebrew/Cellar/openjdk@17/17.0.13/libexec/openjdk.jdk/Contents/Home/bin:/opt/homebrew/opt/ruby/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/lzwjava/Library/Python/3.9/bin:/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin:/Users/lzwjava/bin/flutter/bin:/opt/homebrew/lib/ruby/gems/3.3.0/bin:/opt/homebrew/Cellar/llama.cpp/4539/bin:/Users/lzwjava/bin/google-cloud-sdk/bin

# /opt/homebrew/opt/openjdk/bin

# /opt/homebrew/Cellar/openjdk@17/17.0.13/libexec/openjdk.jdk/Contents/Home/bin

export GLOBAL_PROXY='127.0.0.1:7890'
# export GLOBAL_PROXY='http://192.168.1.1:7890'

function start_proxy {
    export HTTP_PROXY="http://$GLOBAL_PROXY"
    export HTTPS_PROXY="http://$GLOBAL_PROXY"
    export http_proxy="http://$GLOBAL_PROXY"
    export https_proxy="http://$GLOBAL_PROXY"
    export HTTP_PROXY_REQUEST_FULLURI=false
    export HTTPS_PROXY_REQUEST_FULLURI=false
    export ALL_PROXY=$http_proxy
}

function start_proxy_without_prefix {
    export http_proxy=$GLOBAL_PROXY
		export HTTP_PROXY=$GLOBAL_PROXY
		export https_proxy=$GLOBAL_PROXY
    export HTTPS_PROXY=$GLOBAL_PROXY
    export HTTP_PROXY_REQUEST_FULLURI=false
    export HTTPS_PROXY_REQUEST_FULLURI=false
		export ALL_PROXY=$http_proxy
}

function stop_proxy {
    export http_proxy=
		export HTTP_PROXY=
		export https_proxy=
    export HTTPS_PROXY=
    export HTTP_PROXY_REQUEST_FULLURI=true
    export HTTPS_PROXY_REQUEST_FULLURI=true
		export ALL_PROXY=
}

export NO_PROXY="localhost,127.0.0.1,.example.com,::1"

function start_git_proxy {
  git config --global http.proxy $GLOBAL_PROXY
  git config --global https.proxy $GLOBAL_PROXY
}

function stop_git_proxy {
  git config --global --unset http.proxy
  git config --global --unset https.proxy
}

eval "$(/opt/homebrew/bin/brew shellenv)"

start_proxy
# start_git_proxy

# alias python3=/opt/homebrew/bin/python3
# alias pip3=/opt/homebrew/bin/pip3
# alias pip=pip3

alias gpa='python ~/bin/gitmessageai.py --api mistral'
alias gca='python ~/bin/gitmessageai.py --no-push'
alias gm='python ~/bin/gitmessageai.py --only-message'

alias gpam=/usr/local/bin/git-auto-commit

# bundle exec jekyll serve
export SSL_CERT_FILE=~/bin/cacert.pem

alias rougify=/Users/lzwjava/projects/rouge/bin/rougify

# git config --global core.editor "code --wait"
# git config --global -e

export HOMEBREW_NO_AUTO_UPDATE=1

# Function to check and display proxy settings before certain commands
# Function to check and display proxy settings before certain commands
preexec() {
    # Define network-dependent commands
    local network_commands=(
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
        # Add more commands as needed
    )

    # Extract the first word (command) from the command line
    local cmd
    cmd=$(echo "$1" | awk '{print $1}')

    # Function to display proxy variables
    display_proxy() {
        echo -e "🚀 **Proxy Settings Detected:**"

        [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
        [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"

        echo ""
    }

    # Check if the command is network-dependent
    for network_cmd in "${network_commands[@]}"; do
        if [[ "$1" == "$network_cmd"* ]]; then
            if [ -n "$HTTP_PROXY" ] || [ -n "$http_proxy" ] || \
               [ -n "$HTTPS_PROXY" ] || [ -n "$https_proxy" ] || \
               [ -n "$ALL_PROXY" ] || [ -n "$all_proxy" ]; then

                display_proxy
            fi
            break
        fi
    done
}

# The next line enables shell command completion for gcloud.
if [ -f '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc'; fi

export GOOGLE_APPLICATION_CREDENTIALS="/Users/lzwjava/bin/graphite-ally-445108-k3-035f0952219d.json"

export DEEPSEEK_API_KEY="xxx"

export MISTRAL_API_KEY="xxx"

export DYLD_LIBRARY_PATH=$(brew --prefix curl)/lib

export SPEECH_ENDPOINT="https://ai-lzwjava-5596.cognitiveservices.azure.com/"

export DO_API_KEY="xxx"

export GEMINI_API_KEY="xxx"

conda activate base
```