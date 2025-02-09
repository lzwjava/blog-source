---
audio: false
lang: zh
layout: post
title: SSH配置
translated: true
---

这个`ssh-config`文件配置SSH客户端的行为。让我们分解每一部分：

- `Host * !192.*.*.*`: 此部分应用于所有主机，*除了*匹配`192.*.*.*`模式的主机（通常是本地网络地址）。
    - `ProxyCommand corkscrew localhost 7890 %h %p`: 这是关键部分。它告诉SSH使用`corkscrew`程序连接到目标主机。
        - `corkscrew`: 一个允许你通过HTTP或HTTPS代理隧道SSH连接的工具。
        - `localhost 7890`: 指定代理服务器的地址（`localhost`）和端口（`7890`）。这假设你在本地机器上运行着一个代理服务器，监听7890端口（例如，Shadowsocks，一个SOCKS代理或其他隧道解决方案）。
        - `%h`: 一个特殊的SSH变量，展开为你要连接的目标主机名。
        - `%p`: 另一个SSH变量，展开为目标端口（通常SSH为22）。
    - 总之，这个`Host`块将SSH配置为对除本地网络以外的所有连接使用`corkscrew`代理。

- `Host *`: 此部分应用于*所有*主机。
    - `UseKeychain yes`: 在macOS上，这告诉SSH从你的Keychain存储和检索SSH密钥，这样你就不必每次都输入密码。
    - `AddKeysToAgent yes`: 这会自动将你的SSH密钥添加到SSH代理，这样你就不必在每次重启后手动添加它们。
    - `IdentityFile ~/.ssh/id_rsa`: 指定你的私有SSH密钥文件的路径。`~/.ssh/id_rsa`是RSA私钥的默认位置。

**本质上，此配置为除本地网络上的连接之外的所有SSH连接设置了代理，并为方便起见配置了密钥管理。**


```bash
Host * !192.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```
