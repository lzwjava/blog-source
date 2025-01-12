---
lang: hant
layout: post
title: 运行命令前显示代理设置
---

<div style="text-align: center;">  
    <img class="responsive" src="/assets/images/preexec/pe1.png" alt="prexec" />  
</div>

在中国生活或在需要使用VPN和代理的公司工作时，软件开发可能会变得复杂。忘记配置这些设置常常会导致连接问题。为了简化您的工作流程，我在ChatGPT的帮助下创建了一个简单的Zsh脚本，当您运行特定的依赖网络的命令时，它会自动显示您的代理设置。

## 为何显示代理设置？

代理和VPN对于安全访问外部资源至关重要。在执行依赖网络的命令之前显示您的代理设置，有助于您快速识别并解决连接问题。

## 脚本

此脚本利用Zsh的`preexec`函数来检查即将执行的命令是否依赖于网络。如果是，并且已设置代理环境变量，则显示当前的代理设置。

```bash
# 函數用於在某些命令執行前檢查並顯示代理設置
preexec() {
    # 定義依賴網絡的命令
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
        # 根據需要添加更多命令
    )
```

    # 從命令列中提取第一個單詞（命令）
    local cmd
    cmd=$(echo "$1" | awk '{print $1}')

    # 函数用于显示代理变量
    display_proxy() {
        echo -e "\n🚀 检测到代理设置："

        [ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
        [ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
        [ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
        [ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
        [ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
        [ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"

```
echo ""
```

```bash
    # 檢查命令是否依賴於網絡
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
```

## 在 Zsh 中设置脚本

### 1. 打开您的 `.zshrc` 文件

使用您偏好的文本编辑器打开 `.zshrc` 配置文件。例如：

```bash
nano ~/.zshrc
```

### 2. 添加 `preexec` 函数

将上述脚本粘贴到文件末尾。

### 3. 保存并关闭

按下 `CTRL + O` 保存，按下 `CTRL + X` 退出。

### 4. 应用更改

重新加载你的 `.zshrc` 以立即應用新的配置：

```bash
source ~/.zshrc
``` 

這行指令在終端機中執行，用於重新載入 `~/.zshrc` 檔案中的設定。`~/.zshrc` 是 Zsh shell 的設定檔，通常包含環境變數、別名、函數等設定。執行 `source ~/.zshrc` 會讓這些設定立即生效，而不需要重新啟動終端機。

## 测试设置

### 1. 启用代理时

暂时设置一个代理变量，并使用 `pip` 运行依赖网络的命令：

```bash
export HTTP_PROXY="http://127.0.0.1:7890"
pip install selenium beautifulsoup4 urllib3
```

预期输出：

```
```

🚀 检测到代理设置：
   - HTTP_PROXY: http://127.0.0.1:7890
   - http_proxy: 127.0.0.1:7890
   - HTTPS_PROXY: 127.0.0.1:7890
   - https_proxy: 127.0.0.1:7890
   - ALL_PROXY: 127.0.0.1:7890
   - all_proxy: 127.0.0.1:7890

收集Selenium
  正在下載selenium-4.x.x-py2.py3-none-any.whl（xxx kB）
收集BeautifulSoup4
  正在下載beautifulsoup4-4.x.x-py3-none-any.whl（xxx kB）
收集urllib3
  正在下載urllib3-1.x.x-py2.py3-none-any.whl（xxx kB）
...
```

### 2. 未启用代理

取消代理变量的设置，并运行相同的`pip`命令：

```bash
取消設置 HTTP_PROXY
pip 安裝 selenium beautifulsoup4 urllib3
```

预期输出：

```
正在收集 selenium
  下載 selenium-4.x.x-py2.py3-none-any.whl (xxx kB)
正在收集 beautifulsoup4
  下載 beautifulsoup4-4.x.x-py3-none-any.whl (xxx kB)
正在收集 urllib3
  下載 urllib3-1.x.x-py2.py3-none-any.whl (xxx kB)
...
```

*（不应出现任何代理通知。）*

### 3. 非网络命令

运行一个本地命令，例如 `ls`：

```bash
ls
```

预期输出：

```
[文件和目录列表]
```

*（不应出现任何代理通知。）*

## 自定义

- 扩展 `network_commands`：将任何额外的依赖于网络的命令添加到 `network_commands` 数组中。

- 处理别名：确保将任何依赖于网络的命令的别名包含在 `network_commands` 列表中。

```bash
  alias gpa='git push all'
  ```

翻譯成繁體中文：

```bash
  alias gpa='git push all'
  ```

在這個例子中，`alias` 是 Bash 中用來創建命令別名的關鍵字，`gpa` 是別名，`git push all` 是實際執行的命令。這段代碼的意思是將 `gpa` 設置為 `git push all` 的快捷方式，這樣在終端中輸入 `gpa` 時，實際上會執行 `git push all` 命令。

将 `"gpa"` 添加到 `network_commands` 数组中，以便在使用此别名时触发代理通知。

- 使用颜色增强可见性：

为了更好地可见性，特别是在杂乱的终端中，您可以为代理通知添加颜色：

  ```bash
  # 在 .zshrc 文件顶部添加颜色代码
  GREEN='\033[0;32m'
  NC='\033[0m' # 无颜色
```

  display_proxy() {
      echo -e "\n${GREEN}🚀 检测到代理设置：${NC}"

```bash
[ -n "$HTTP_PROXY" ] && echo "   - HTTP_PROXY: $HTTP_PROXY"
[ -n "$http_proxy" ] && echo "   - http_proxy: $http_proxy"
[ -n "$HTTPS_PROXY" ] && echo "   - HTTPS_PROXY: $HTTPS_PROXY"
[ -n "$https_proxy" ] && echo "   - https_proxy: $https_proxy"
[ -n "$ALL_PROXY" ] && echo "   - ALL_PROXY: $ALL_PROXY"
[ -n "$all_proxy" ] && echo "   - all_proxy: $all_proxy"
```

```
echo ""
}
```

## 结论

在受限的网络环境中管理代理设置对于顺畅的软件开发至关重要。这个Zsh脚本确保你在运行需要网络访问的命令时，始终了解你的代理配置，从而提升你的工作流程和故障排除效率。

编程愉快！🚀