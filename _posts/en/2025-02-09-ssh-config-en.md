---
audio: true
lang: en
layout: post
title: SSH Configuration
translated: false
---

This `ssh-config` file configures SSH client behavior. Let's break down each part:

-   `Host * !192.*.*.*`: This section applies to all hosts *except* those matching the `192.*.*.*` pattern (typically, local network addresses).
    -   `ProxyCommand corkscrew localhost 7890 %h %p`:  This is the key part. It tells SSH to use the `corkscrew` program to connect to the target host.
        -   `corkscrew`: A tool that allows you to tunnel SSH connections through HTTP or HTTPS proxies.
        -   `localhost 7890`:  Specifies the proxy server's address (`localhost`) and port (`7890`).  This assumes you have a proxy server running on your local machine, listening on port 7890 (e.g., Shadowsocks, a SOCKS proxy, or another tunneling solution).
        -   `%h`:  A special SSH variable that expands to the target hostname you're trying to connect to.
        -   `%p`:  Another SSH variable that expands to the target port (usually 22 for SSH).
    - In summary, this `Host` block configures SSH to use the `corkscrew` proxy for all connections *except* those to the local network.

-   `Host *`: This section applies to *all* hosts.
    -   `UseKeychain yes`:  On macOS, this tells SSH to store and retrieve SSH keys from your Keychain, so you don't have to enter your password every time.
    -   `AddKeysToAgent yes`:  This automatically adds your SSH keys to the SSH agent, so you don't have to manually add them after each reboot.
    -   `IdentityFile ~/.ssh/id_rsa`:  Specifies the path to your private SSH key file.  `~/.ssh/id_rsa` is the default location for the RSA private key.

**In essence, this configuration sets up a proxy for all SSH connections except those on the local network, and it configures key management for convenience.**


```bash
Host * !192.*.*.*
    ProxyCommand corkscrew localhost 7890 %h %p
Host *
    UseKeychain yes
    AddKeysToAgent yes
    IdentityFile ~/.ssh/id_rsa
```