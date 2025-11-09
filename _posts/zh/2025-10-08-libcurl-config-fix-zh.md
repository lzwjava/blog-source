---
audio: false
generated: true
image: false
lang: zh
layout: post
model: x-ai/grok-4-fast
title: 修复libcurl配置错误
translated: true
type: note
---

这个错误意味着 `configure` 脚本试图寻找 **libcurl**（用于 HTTP/HTTPS 请求的库），但无法找到 `curl-config` —— 这是一个用于指示 libcurl 安装位置的辅助工具。

以下是针对不同系统的修复方法：

---

### 🧩 Ubuntu / Debian 系统

执行：

```bash
sudo apt update
sudo apt install libcurl4-openssl-dev
```

然后重试：

```bash
./configure
```

---

### 🧩 Fedora / CentOS / RHEL 系统

执行：

```bash
sudo dnf install libcurl-devel
```

---

### 🧩 Arch / Manjaro 系统

执行：

```bash
sudo pacman -S curl
```

---

### 🔍 验证安装

安装完成后，请确认 `curl-config` 可用：

```bash
which curl-config
```

如果返回类似 `/usr/bin/curl-config` 的路径，说明配置成功。

接着重新运行：

```bash
./configure
make
sudo make install
```

---

需要我解释 `curl-config` 的实际作用以及 `configure` 为何需要它吗？