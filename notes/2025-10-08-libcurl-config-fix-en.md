---
audio: false
generated: true
image: false
lang: en
layout: post
model: x-ai/grok-4-fast
title: Fixing libcurl Configuration Error
translated: false
---

This error means the `configure` script is trying to find **libcurl** (a library for HTTP/HTTPS requests), but it cannot locate `curl-config` — a helper binary that tells where libcurl is installed.

Here’s how to fix it depending on your system:

---

### 🧩 For Ubuntu / Debian

Run:

```bash
sudo apt update
sudo apt install libcurl4-openssl-dev
```

Then try again:

```bash
./configure
```

---

### 🧩 For Fedora / CentOS / RHEL

Run:

```bash
sudo dnf install libcurl-devel
```

---

### 🧩 For Arch / Manjaro

Run:

```bash
sudo pacman -S curl
```

---

### 🔍 To verify installation

After installation, make sure `curl-config` is available:

```bash
which curl-config
```

If it returns a path like `/usr/bin/curl-config`, you’re good.

Then rerun:

```bash
./configure
make
sudo make install
```

---

Would you like me to explain what `curl-config` actually does and why `configure` needs it?