---
audio: true
lang: hant
layout: post
title: SSH 設定
translated: true
---

這個 `ssh-config` 檔案設定 SSH 客戶端的行為。讓我們逐一分解：

- `Host * !192.*.*.*`：此區段適用於所有主機，*除了*符合 `192.*.*.*` 模式的那些主機（通常是本地網路地址）。
    - `ProxyCommand corkscrew localhost 7890 %h %p`：這是關鍵部分。它指示 SSH 使用 `corkscrew` 程式連接到目標主機。
        - `corkscrew`：一個允許您通過 HTTP 或 HTTPS 代理伺服器建立 SSH 連線的工具。
        - `localhost 7890`：指定代理伺服器的地址 (`localhost`) 和埠 (`7890`)。這假設您在本地機器上執行一個代理伺服器，監聽 7890 埠（例如，Shadowsocks、SOCKS 代理或其他隧道方案）。
        - `%h`：一個特殊的 SSH 變數，展開為您嘗試連接的目標主機名稱。
        - `%p`：另一個特殊的 SSH 變數，展開為目標埠（通常 SSH 為 22）。
    - 總而言之，此 `Host` 區塊將 SSH 設定為使用 `corkscrew` 代理進行所有連線，*除了*本地網路的連線。

- `Host *`：此區段適用於*所有*主機。
    - `UseKeychain yes`：在 macOS 上，這會指示 SSH 從您的 Keychain 儲存和擷取 SSH 金鑰，因此您無需每次都輸入密碼。
    - `AddKeysToAgent yes`：這會自動將您的 SSH 金鑰新增到 SSH 代理，因此您無需在每次重新啟動後手動新增它們。
    - `IdentityFile ~/.ssh/id_rsa`：指定您的 SSH 私鑰檔案的路徑。`~/.ssh/id_rsa` 是 RSA 私鑰的預設位置。

**總之，此設定為除本地網路外的所有 SSH 連線設定代理，並為方便起見配置金鑰管理。**


```bash
Host * !192.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```
