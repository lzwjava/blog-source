---
audio: false
generated: true
image: false
lang: hant
layout: post
model: x-ai/grok-4-fast
title: 預設未安裝Traceroute
translated: true
type: note
---

Traceroute 在 Linux 系統上絕對可用——它是一個標準的網絡診斷工具，用於追蹤封包前往目的地的路徑。不過，在許多現代發行版中（例如 Ubuntu、Fedora 或 Debian 最小安裝版本），為了保持基礎系統的輕量化，它通常**不會預設安裝**。這就是為什麼你在輸入 "trac" 時，標籤自動完成功能沒有顯示該指令的原因。

### 快速解決方法
透過你的套件管理程式進行安裝：
- **Debian/Ubuntu**：`sudo apt update && sudo apt install traceroute`
- **Fedora/RHEL/CentOS**：`sudo dnf install traceroute`（舊版系統請使用 `sudo yum install traceroute`）
- **Arch**：`sudo pacman -S traceroute`

安裝完成後，輸入 `trac` + Tab 鍵時，現在應該會在列表中看到 `traceroute`。接著你就可以執行 `traceroute example.com` 來進行測試。

如果你使用的是容器化或極簡化系統（例如 Alpine Linux），它可能會使用 `tr` 作為別名，或者需要安裝不同的套件——請告訴我你使用的發行版以獲得更具體的說明！