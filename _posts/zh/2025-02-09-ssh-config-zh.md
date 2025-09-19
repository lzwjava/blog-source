---
audio: true
generated: false
image: false
lang: zh
layout: post
title: SSH 配置
translated: true
---

这个 `ssh-config` 文件配置了 SSH 客户端的行为。让我们逐一分解每个部分：

- `Host * !192.*.*.*`: 这个部分适用于所有主机，除了匹配 `192.*.*.*` 模式的主机（通常是本地网络地址）。
    - `ProxyCommand corkscrew localhost 7890 %h %p`: 这是关键部分。它告诉 SSH 使用 `corkscrew` 程序连接到目标主机。
        - `corkscrew`: 一个工具，允许你通过 HTTP 或 HTTPS 代理隧道 SSH 连接。
        - `localhost 7890`: 指定代理服务器的地址（`localhost`）和端口（`7890`）。这假设你在本地机器上运行一个代理服务器，监听端口 7890（例如 Shadowsocks、SOCKS 代理或其他隧道解决方案）。
        - `%h`: 一个特殊的 SSH 变量，展开为你试图连接的目标主机名。
        - `%p`: 另一个 SSH 变量，展开为目标端口（通常是 22 端口用于 SSH）。
    - 总之，这个 `Host` 块配置 SSH 使用 `corkscrew` 代理进行所有连接，除了本地网络的连接。

- `Host *`: 这个部分适用于所有主机。
    - `UseKeychain yes`: 在 macOS 上，这告诉 SSH 将 SSH 密钥存储和检索到你的 Keychain 中，这样你就不必每次都输入密码。
    - `AddKeysToAgent yes`: 这会自动将你的 SSH 密钥添加到 SSH 代理中，这样你就不必在每次重启后手动添加它们。
    - `IdentityFile ~/.ssh/id_rsa`: 指定私有 SSH 密钥文件的路径。`~/.ssh/id_rsa` 是 RSA 私钥的默认位置。

**总之，这个配置为所有 SSH 连接（除了本地网络的连接）设置了代理，并配置了密钥管理以方便使用。**

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