---
audio: true
lang: hant
layout: post
title: SSH 設定
translated: true
---

這個 `ssh-config` 文件配置 SSH 客戶端行為。讓我們逐一分解每個部分：

-   `Host * !192.*.*.*`: 這部分適用於所有主機，*除非*符合 `192.*.*.*` 模式（通常是本地網絡地址）。
    -   `ProxyCommand corkscrew localhost 7890 %h %p`: 這是關鍵部分。它告訴 SSH 使用 `corkscrew` 程序連接到目標主機。
        -   `corkscrew`: 一個工具，允許你通過 HTTP 或 HTTPS 代理隧道 SSH 連接。
        -   `localhost 7890`: 指定代理伺服器的地址 (`localhost`) 和端口 (`7890`)。這假設你在本地機器上運行一個代理伺服器，監聽端口 7890（例如 Shadowsocks、SOCKS 代理或其他隧道解決方案）。
        -   `%h`: 一個特殊的 SSH 變量，擴展到你試圖連接的目標主機名。
        -   `%p`: 另一個 SSH 變量，擴展到目標端口（通常是 22 端口用於 SSH）。
    - 總結來說，這個 `Host` 塊配置 SSH 使用 `corkscrew` 代理進行所有連接，*除非*是到本地網絡。

-   `Host *`: 這部分適用於*所有*主機。
    -   `UseKeychain yes`: 在 macOS 上，這告訴 SSH 從你的 Keychain 存儲和檢索 SSH 密鑰，所以你不需要每次都輸入密碼。
    -   `AddKeysToAgent yes`: 這自動將你的 SSH 密鑰添加到 SSH 代理，所以你不需要在每次重啟後手動添加它們。
    -   `IdentityFile ~/.ssh/id_rsa`: 指定你的私有 SSH 密鑰文件的路徑。`~/.ssh/id_rsa` 是 RSA 私有密鑰的默認位置。

**總的來說，這個配置為所有 SSH 連接設置代理，除非是本地網絡，並配置密鑰管理以方便使用。**

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