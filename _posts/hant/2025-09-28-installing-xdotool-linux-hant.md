---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-sonnet-4
title: 在Linux上安裝與使用xdotool
translated: true
type: note
---

要在您的 Linux 系統上安裝 `xdotool`，可以使用發行版的套件管理工具。根據您的主機名顯示「XiaoXin」，您很可能使用的是 Ubuntu 或基於 Debian 的發行版。以下是常見 Linux 發行版的安裝指令：

## Ubuntu/Debian：
```bash
sudo apt update
sudo apt install xdotool
```

## CentOS/RHEL/Fedora：
```bash
# 適用新版本（dnf）
sudo dnf install xdotool

# 適用舊版本（yum）
sudo yum install xdotool
```

## Arch Linux：
```bash
sudo pacman -S xdotool
```

## openSUSE：
```bash
sudo zypper install xdotool
```

安裝完成後，您可以透過執行以下指令驗證是否正常運作：
```bash
xdotool --version
```

安裝完成後，您的 Python 腳本應能使用 `xdotool` 來取得瀏覽器標題。`xdotool` 工具常用於自動化 X11 桌面任務，包括取得視窗標題，這正是您的腳本試圖實現的功能。

若安裝後仍遇到問題，請確認：
1. 您正在 X11 環境中執行腳本（非 Wayland）
2. 您有開啟中的瀏覽器視窗
3. 瀏覽器視窗已取得焦點或處於可見狀態