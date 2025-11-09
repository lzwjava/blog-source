---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 修復 libcurl 配置錯誤
translated: true
type: note
---

這個錯誤表示 `configure` 指令碼試圖尋找 **libcurl**（用於 HTTP/HTTPS 請求的程式庫），但無法找到 `curl-config` —— 這是一個用於告知 libcurl 安裝位置的輔助二進位檔。

以下根據你的系統提供解決方法：

---

### 🧩 適用於 Ubuntu / Debian

執行：

```bash
sudo apt update
sudo apt install libcurl4-openssl-dev
```

然後重新嘗試：

```bash
./configure
```

---

### 🧩 適用於 Fedora / CentOS / RHEL

執行：

```bash
sudo dnf install libcurl-devel
```

---

### 🧩 適用於 Arch / Manjaro

執行：

```bash
sudo pacman -S curl
```

---

### 🔍 驗證安裝

安裝完成後，請確認 `curl-config` 是否可用：

```bash
which curl-config
```

如果返回路徑如 `/usr/bin/curl-config`，表示設定正確。

接著重新執行：

```bash
./configure
make
sudo make install
```

---

需要我解釋 `curl-config` 的實際功能以及 `configure` 為何需要它嗎？