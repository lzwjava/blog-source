---
audio: false
generated: true
image: false
lang: hant
layout: post
title: Ubuntu 的 Node.js 升級指南
translated: true
type: note
---

在 Ubuntu 上升級 Node.js 有幾種方法。最可靠且推薦的方式是使用 **`nvm` (Node 版本管理器)** 或 **NodeSource 軟體庫**。以下是兩種方法的逐步說明。

---

## **方法一：使用 NVM (推薦)**
NVM 讓你能輕鬆安裝並管理多個 Node.js 版本。

### 1. 安裝 NVM
開啟終端機並執行：
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
```
接著重新載入你的 shell：
```bash
source ~/.bashrc
```
或
```bash
source ~/.zshrc
```
(根據你使用的 shell)

### 2. 安裝最新 Node.js 版本
列出可用的版本：
```bash
nvm ls-remote
```
安裝最新的 LTS 版本 (推薦大多數使用者使用)：
```bash
nvm install --lts
```
或安裝特定版本 (例如 20.x)：
```bash
nvm install 20
```

### 3. 設定預設版本
```bash
nvm alias default 20
```

### 4. 驗證
```bash
node -v
npm -v
```

---

## **方法二：使用 NodeSource 軟體庫**
此方法會在全系統範圍內安裝 Node.js。

### 1. 移除舊版 Node.js (如果透過 apt 安裝)
```bash
sudo apt remove --purge nodejs npm
sudo apt autoremove
```

### 2. 新增 NodeSource 軟體庫
對於 **Node.js 20.x** (截至 2025 年 8 月的 LTS 版本)：
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
```
對於 **Node.js 22.x** (如果可用)：
```bash
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
```

### 3. 安裝 Node.js
```bash
sudo apt install -y nodejs
```

### 4. 驗證
```bash
node -v
npm -v
```

---

## **方法三：使用 Ubuntu 預設軟體庫 (不推薦)**
Ubuntu 的預設軟體庫通常包含過時的 Node.js 版本。如果你仍想使用它：
```bash
sudo apt update
sudo apt install nodejs npm
```
但這**不推薦**用於開發，因為版本通常較舊。

---

## **你應該使用哪種方法？**
- **使用 NVM** 如果你想輕鬆切換 Node.js 版本或需要最新功能。
- **使用 NodeSource** 如果你想要一個全系統範圍內、穩定的安裝。