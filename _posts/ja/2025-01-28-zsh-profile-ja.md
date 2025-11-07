---
audio: false
generated: false
image: false
lang: ja
layout: post
title: Zsh プロファイル
translated: true
type: post
---

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

このzshプロファイルは、コマンドライン体験を向上させることを目的としており、プロキシ設定、Git統合、便利なエイリアスに焦点を当てています。以下のセクションでその機能を詳述します：

**1. PATH設定:**

   - `export PATH=...`: この行は`PATH`環境変数を設定し、シェルが実行可能なファイルを探す場所を指定します。Java、Ruby、Homebrew、Python、Flutter、Google Cloud SDKなどのディレクトリが含まれており、これらのツールのコマンドをターミナルから直接実行できるようにします。

**2. プロキシ管理:**

   - `export GLOBAL_PROXY='127.0.0.1:7890'`: これはプロキシサーバーアドレスを保持する変数`GLOBAL_PROXY`を定義します。
   - `function start_proxy { ... }`: この関数は`HTTP_PROXY`、`HTTPS_PROXY`、`http_proxy`、`https_proxy`、`ALL_PROXY`環境変数を指定されたプロキシで設定し、プロキシの全URIリクエストを無効にします。
   - `function start_proxy_without_prefix { ... }`: `start_proxy`と似ていますが、プレフィックスなしでプロキシ変数を設定します。
   - `function stop_proxy { ... }`: この関数はプロキシ変数を未設定にし、プロキシを無効にします。また、プロキシの全URIリクエストを有効にします。
   - `export NO_PROXY="localhost,127.0.0.1,.example.com,::1"`: プロキシをバイパスすべきホストのリストを指定します。

**3. Gitプロキシ:**

   - `function start_git_proxy { ... }`: この関数はgitにグローバルプロキシを使用するように設定します。
   - `function stop_git_proxy { ... }`: この関数はgitプロキシ設定を未設定にします。

**4. Homebrew統合:**

   - `eval "$(/opt/homebrew/bin/brew shellenv)"`: この行はHomebrewをシェル環境に統合し、Homebrewコマンドを使用できるようにします。

**5. 便利なエイリアス:**

   - `alias gpa='python ~/bin/gitmessageai.py --api mistral'`: これは`gpa`エイリアスを作成し、mistral APIを使用するpythonスクリプト`gitmessageai.py`を実行します。
   - `alias gca='python ~/bin/gitmessageai.py --no-push'`: これは`gca`エイリアスを作成し、変更をプッシュせずに同じスクリプトを実行します。
   - `alias gm='python ~/bin/gitmessageai.py --only-message'`: これは`gm`エイリアスを作成し、コミットメッセージのみを表示するように同じスクリプトを実行します。
   - `alias gpam=/usr/local/bin/git-auto-commit`: これは`gpam`エイリアスを作成し、`git-auto-commit`スクリプトを実行します。
   - `alias rougify=/Users/lzwjava/projects/rouge/bin/rougify`: これは`rougify`エイリアスを作成し、`rougify`スクリプトを実行します。

**6. SSL証明書:**

   - `export SSL_CERT_FILE=~/bin/cacert.pem`: これはカスタムSSL証明書ファイルへのパスを設定します。

**7. Homebrew自動更新:**

   - `export HOMEBREW_NO_AUTO_UPDATE=1`: これはHomebrewの自動更新を無効にします。

**8. 事前実行プロキシチェック:**

   - `preexec() { ... }`: この関数は各コマンドの実行前に実行され、コマンドがネットワーク依存コマンドのリストにあるかどうかを確認します。そうであり、プロキシ変数が設定されている場合、プロキシ設定を表示します。
   - `local network_commands=( ... )`: この配列はネットワーク依存コマンドのリストを表示します。
   - `display_proxy() { ... }`: この関数は現在のプロキシ設定を表示します。

**9. Google Cloud SDK補完:**

   - `if [ -f '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/lzwjava/bin/google-cloud-sdk/completion.zsh.inc'; fi`: この行はgcloudのシェルコマンド補完を有効にします。

**10. APIキーとクレデンシャル:**

    - `export GOOGLE_APPLICATION_CREDENTIALS="/Users/lzwjava/bin/graphite-ally-445108-k3-035f0952219d.json"`: Google Cloudサービスアカウントのクレデンシャルへのパスを設定します。
    - `export DEEPSEEK_API_KEY="xxx"`: DeepSeek APIキーを設定します。
    - `export MISTRAL_API_KEY="xxx"`: Mistral APIキーを設定します。
    - `export DYLD_LIBRARY_PATH=$(brew --prefix curl)/lib`: curlの動的ライブラリパスを設定します。
    - `export SPEECH_ENDPOINT="https://ai-lzwjava-5596.cognitiveservices.azure.com/"`: Azureのスピーチエンドポイントを設定します。
    - `export DO_API_KEY="xxx"`: Digital Ocean APIキーを設定します。
    - `export GEMINI_API_KEY="xxx"`: Gemini APIキーを設定します。

**11. Conda環境:**

    - `conda activate base`: ベースconda環境をアクティブにします。

**要するに、このzshプロファイルは開発者にとって包括的なセットアップを提供し、以下を含みます：**

- プロキシの簡単な管理および開始と停止の関数。
- Gitプロキシ設定。
- Homebrew統合。
- 一般的なタスクの便利なエイリアス。
- ネットワーク依存コマンドの事前実行プロキシチェック。
- 様々なサービスのAPIキーとクレデンシャル。
- Conda環境のアクティブ化。

このプロファイルは、ユーザーのワークフローをストリーミングし、さまざまな開発ツールとサービスを管理しやすくすることを目的としています。