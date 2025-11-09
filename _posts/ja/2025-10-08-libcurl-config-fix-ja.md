---
audio: false
generated: true
image: false
lang: ja
layout: post
model: x-ai/grok-4-fast
title: libcurl設定エラーの修正
translated: true
type: note
---

このエラーは、`configure`スクリプトが**libcurl**（HTTP/HTTPSリクエスト用のライブラリ）を見つけようとしているが、`curl-config` — libcurlのインストール場所を教えるヘルパーバイナリ — を見つけられないことを意味します。

システムに応じた解決方法は以下の通りです：

---

### 🧩 Ubuntu / Debian の場合

以下を実行：

```bash
sudo apt update
sudo apt install libcurl4-openssl-dev
```

その後、再度試行：

```bash
./configure
```

---

### 🧩 Fedora / CentOS / RHEL の場合

以下を実行：

```bash
sudo dnf install libcurl-devel
```

---

### 🧩 Arch / Manjaro の場合

以下を実行：

```bash
sudo pacman -S curl
```

---

### 🔍 インストールの確認

インストール後、`curl-config`が利用可能か確認：

```bash
which curl-config
```

`/usr/bin/curl-config`のようなパスが返れば成功です。

その後、再実行：

```bash
./configure
make
sudo make install
```

---

`curl-config`の実際の役割と、なぜ`configure`スクリプトがそれを必要とするのか説明しましょうか？