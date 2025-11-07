---
audio: false
generated: false
image: false
lang: hant
layout: post
title: Netplan、Systemd、SSH、Conda 清理
translated: true
type: post
---

### 目錄

1. [嘗試 Netplan](#trying-netplan)
   - 靜態 IP 配置導致 SSH 中斷
   - 需要實體接觸才能還原
   - 修改系統的 DNS 解析器檔案

2. [Systemd 服務](#systemd-service)
   - 配置本地 LLM 推理服務
   - 設置 LLM 模型的 Web 介面
   - 建立基於規則的代理工具服務
   - 使用 systemctl 命令進行服務管理

3. [SSH 配置](#ssh-configuration)
   - 透過 corkscrew 代理外部連線
   - 將本地網絡排除在代理之外
   - 透過鑰匙圈和代理管理 SSH 密鑰
   - 指定預設私鑰位置

4. [在 Linux 中刪除 Conda](#delete-conda-in-linux)
   - 移除整個 conda 安裝目錄
   - 從 bashrc 刪除 conda 初始化代碼
   - 更新 PATH 環境變數
   - 從系統路徑中清除 conda 二進制檔案


## 嘗試 Netplan

我嘗試了以下配置，為 Ubuntu 機器分配靜態 IP 地址。我在該伺服器上執行 OpenWebUI 和 llama.cpp。

```
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.128/32
      gateway4: 192.168.1.1
```

執行 `sudo netplan apply` 後，無法再透過 `ssh lzw@192.168.1.128` 訪問該機器。

使用鍵盤和滑鼠登入機器，刪除檔案並還原設定。

`/etc/resolv.conf` 已被更改。

---

## Systemd 服務

*2025.02.13*

## LLaMA 伺服器服務設定

本節說明如何設定 systemd 服務，以執行 LLaMA 伺服器，該伺服器提供本地 LLM 推理功能。

```bash
sudo emacs /etc/systemd/system/llama.service
sudo systemctl daemon-reload
sudo systemctl enable llama.service
journalctl -u llama.service
```

```bash
[Unit]
Description=Llama Script

[Service]
ExecStart=/home/lzw/Projects/llama.cpp/build/bin/llama-server -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-Distill-Qwen-14B-Q5_K_M.gguf --port 8000  --ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1
WorkingDirectory=/home/lzw/Projects/llama.cpp
StandardOutput=append:/home/lzw/llama.log
StandardError=append:/home/lzw/llama.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

## Open WebUI 服務設定

本節說明如何設定 systemd 服務，以執行 Open WebUI，該服務提供了一個用於與 LLM 模型互動的 Web 介面。

```bash
[Unit]
Description=Open Web UI Service

[Service]
ExecStart=/home/lzw/.local/bin/open-webui serve
WorkingDirectory=/home/lzw
StandardOutput=append:/home/lzw/open-webui.log
StandardError=append:/home/lzw/open-webui.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
sudo systemctl enable openwebui.service
sudo systemctl daemon-reload
sudo systemctl start  openwebui.service
```

## Clash 服務設定

本節說明如何設定 systemd 服務，以執行 Clash，一個基於規則的代理工具。

```bash
[Unit]
Description=Clash Service

[Service]
ExecStart=/home/lzw/clash-linux-386-v1.17.0/clash-linux-386
WorkingDirectory=/home/lzw/clash-linux-386-v1.17.0
StandardOutput=append:/home/lzw/clash.log
StandardError=append:/home/lzw/clash.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
# 建立服務檔案
sudo emacs /etc/systemd/system/clash.service 

# 重新載入 systemd daemon
sudo systemctl daemon-reload

# 啟用並啟動服務
sudo systemctl enable clash.service
sudo systemctl start clash.service
sudo systemctl restart clash.service

# 檢查狀態
sudo systemctl status clash.service
```

---

## SSH 配置

*2025.02.09*

這個 `ssh-config` 檔案配置了 SSH 客戶端的行為。我們來分解每個部分：

-   `Host * !192.*.*.*`: 此部分適用於所有主機，*除了*與 `192.*.*.*` 模式匹配的主機（通常是本地網路地址）。
    -   `ProxyCommand corkscrew localhost 7890 %h %p`: 這是關鍵部分。它指示 SSH 使用 `corkscrew` 程式連接到目標主機。
        -   `corkscrew`: 一個工具，允許您透過 HTTP 或 HTTPS 代理隧穿 SSH 連線。
        -   `localhost 7890`: 指定代理伺服器的地址 (`localhost`) 和埠 (`7890`)。這假設您的本地機器上正在執行代理伺服器，並偵聽埠 7890（例如，Shadowsocks、SOCKS 代理或其他隧穿解決方案）。
        -   `%h`: 一個特殊的 SSH 變數，展開為您嘗試連接的目標主機名。
        -   `%p`: 另一個 SSH 變數，展開為目標埠（SSH 通常為 22）。
    - 總之，這個 `Host` 塊配置 SSH 使用 `corkscrew` 代理進行所有連接，*除了*連接到本地網路的那些。

-   `Host *`: 此部分適用於*所有*主機。
    -   `UseKeychain yes`: 在 macOS 上，這會指示 SSH 將 SSH 密鑰儲存並從您的鑰匙圈中檢索，這樣您就不必每次都輸入密碼。
    -   `AddKeysToAgent yes`: 這會自動將您的 SSH 密鑰添加到 SSH 代理中，這樣您就不必在每次重啟後手動添加它們。
    -   `IdentityFile ~/.ssh/id_rsa`: 指定您的私有 SSH 密鑰檔案的路徑。`~/.ssh/id_rsa` 是 RSA 私鑰的預設位置。

**本質上，此配置為所有 SSH 連接（本地網路除外）設定了代理，並為方便起見配置了密鑰管理。**


```bash
Host 192.168.1.*
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa 
Host * !192.*.*.* !47.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa    
```

---

## 在 Linux 中刪除 Conda

*2025.02.07*

```bash
rm -rf ~/anaconda3
```

刪除 `.bashrc` 中的以下代碼：

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/lzw/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/lzw/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/lzw/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/lzw/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

將路徑從：

```bash
export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/anaconda3/bin:/home/lzw/anaconda3/condabin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
```

更改為：

```bash
export PATH="/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"
```