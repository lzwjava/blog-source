---
audio: false
generated: false
image: false
lang: zh
layout: post
title: Zsh 配置文件
translated: true
---

这个zsh配置文件旨在提高命令行体验，重点放在代理配置、Git集成和方便的别名上。以下各节详细介绍其功能：

**1. PATH 配置:**

   - `export PATH=...`：这行设置了`PATH`环境变量，告诉shell在哪些目录中查找可执行文件。它包括Java、Ruby、Homebrew、Python、Flutter和Google Cloud SDK等各种目录。这确保了可以直接从终端运行这些工具的命令。

**2. 代理管理:**

   - `export GLOBAL_PROXY='127.0.0.1:7890'`：定义变量`GLOBAL_PROXY`，保存代理服务器地址。
   - `function start_proxy { ... }`：这个函数设置`HTTP_PROXY`、`HTTPS_PROXY`、`http_proxy`、`https_proxy`和`ALL_PROXY`环境变量以使用指定的代理。它还禁用了代理的完整URI请求。
   - `function start_proxy_without_prefix { ... }`：类似于`start_proxy`，但设置代理变量时不带`http://`前缀。
   - `function stop_proxy { ... }`：这个函数取消设置代理变量，从而禁用代理。它还启用了代理的完整URI请求。
   - `export NO_PROXY="localhost,127.0.0.1,.example.com,::1"`：指定应绕过代理的主机列表。

**3. Git 代理:**

   - `function start_git_proxy { ... }`：这个函数配置git使用全局代理进行HTTP和HTTPS连接。
   - `function stop_git_proxy { ... }`：这个函数取消git代理设置。

**4. Homebrew 集成:**

   - `eval "$(/opt/homebrew/bin/brew shellenv)"`：这行将Homebrew集成到shell环境中，允许使用Homebrew命令。

**5. 便捷别名:**

   - `alias gpa='python ~/bin/gitmessageai.py --api mistral'`：创建别名`gpa`，运行python脚本`gitmessageai.py`，使用mistral API。
   - `alias gca='python ~/bin/gitmessageai.py --no-push'`：创建别名`gca`，运行相同的脚本但不推送更改。
   - `alias gm='python ~/bin/gitmessageai.py --only-message'`：创建别名`gm`，运行相同的脚本并仅打印提交消息。
   - `alias gpam=/usr/local/bin/git-auto-commit`：创建别名`gpam`，运行`git-auto-commit`脚本。
   - `alias rougify=/Users/lzwjava/projects/rouge/bin/rougify`：创建别名`rougify`，运行`rougify`脚本。

**6. SSL 证书:**

   - `export SSL_CERT_FILE=~/bin/cacert.pem`：设置自定义SSL证书文件的路径。

**7. Homebrew 自动更新:**

   - `export HOMEBREW_NO_AUTO_UPDATE=1`：禁用Homebrew的自动更新。

**8. 预执行代理检查:**

   - `preexec() { ... }`：在每个命令执行前运行的函数。它检查命令是否在网络依赖命令列表中。如果是，并且设置了任何代理变量，则显示代理设置。
   - `local network_commands=( ... )`：列出被认为是网络依赖的命令的数组。
   - `display_proxy() { ... }`：显示当前代理设置的函数。

**9. Google Cloud SDK 补全:**

   - `if [ -f '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc'; fi`：启用gcloud的shell命令补全。

**10. API密钥和凭证:**

    - `export GOOGLE_APPLICATION_CREDENTIALS="/Users/lzwjava/bin/graphite-ally-445108-k3-035f0952219d.json"`：设置Google Cloud服务账户凭证的路径。
    - `export DEEPSEEK_API_KEY="xxx"`：设置DeepSeek API密钥。
    - `export MISTRAL_API_KEY="xxx"`：设置Mistral API密钥。
    - `export DYLD_LIBRARY_PATH=$(brew --prefix curl)/lib`：设置curl的动态库路径。
    - `export SPEECH_ENDPOINT="https://ai-lzwjava-5596.cognitiveservices.azure.com/"`：设置Azure语音端点。
    - `export DO_API_KEY="xxx"`：设置Digital Ocean API密钥。
    - `export GEMINI_API_KEY="xxx"`：设置Gemini API密钥。

**11. Conda 环境:**

    - `conda activate base`：激活base conda环境。

**总结，这个zsh配置文件为开发者提供了全面的设置，包括：**

- 使用函数进行简单的代理管理，启动和停止代理。
- Git代理配置。
- 与Homebrew的集成。
- 常见任务的便捷别名。
- 网络依赖命令的预执行代理检查。
- 各种服务的API密钥和凭证。
- Conda环境激活。

这个配置文件旨在简化用户的工作流程，使管理各种开发工具和服务更加容易。

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