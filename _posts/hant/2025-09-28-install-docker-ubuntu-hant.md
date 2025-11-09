---
audio: false
generated: true
image: false
lang: hant
layout: post
model: anthropic/claude-sonnet-4
title: 在 Ubuntu 上安裝 Docker 指南
translated: true
type: note
---

根據你的 Ubuntu 系統輸出，你有幾種安裝 Docker 的選擇。以下是推薦的方式：

## 選項 1：安裝 Docker Engine（推薦）

最常見且推薦的方式是從 Docker 官方儲存庫安裝 Docker Engine：

```bash
# 更新套件索引
sudo apt update

# 安裝必要套件
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# 加入 Docker 官方 GPG 金鑰
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 加入 Docker 儲存庫
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 再次更新套件索引
sudo apt update

# 安裝 Docker Engine
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## 選項 2：透過 APT 快速安裝（更簡單）

從你終端機顯示的選項中，你可以使用：

```bash
sudo apt install docker.io
```

## 安裝後設定

安裝完成後，你需要：

1. **啟動並啟用 Docker 服務：**
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

2. **將你的使用者加入 docker 群組**（以便無需 sudo 執行 Docker）：
```bash
sudo usermod -aG docker $USER
```

然後登出並重新登入，或執行：
```bash
newgrp docker
```

3. **驗證安裝：**
```bash
docker --version
docker run hello-world
```

## 該選擇哪個選項？

- **選項 1** 讓你直接從 Docker Inc. 獲得最新的 Docker 版本
- **選項 2** 更簡單，但可能來自 Ubuntu 儲存庫的版本稍舊

對大多數使用者來說，選項 2（`sudo apt install docker.io`）完全足夠且更簡單。版本差異對於常規使用通常很小。

需要我詳細解釋任何步驟嗎？