---
audio: false
generated: false
lang: hant
layout: post
title: 使用Ollama
translated: true
---

```bash
% ollama list
名稱                   ID              大小      修改時間
deepseek-coder:6.7b    ce298d984115    3.8 GB    14 小時前
mistral:7b             f974a74358d6    4.1 GB    15 小時前
```

```bash
ollama remove model
```

這是一個很好用的工具。Ollamac有一些錯誤。例如，當它收到本地API的響應時，應用程式中的幾個文字框會更新。

然而，在Linux中，Ollama作為一個系統服務運行。以下是服務配置文件：

`/etc/systemd/system/ollama.service`:

```bash
[Unit]
Description=Ollama 服務
After=network-online.target

[Service]
ExecStart=/usr/local/bin/ollama serve
User=ollama
Group=ollama
Restart=always
RestartSec=3
Environment="PATH=/home/lzw/.local/bin:/home/lzw/bin:/usr/local/cuda-12.2/bin:/home/lzw/.local/share/gem/ruby/3.0.0/bin:/home/lzw/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/snap/bin"

[Install]
WantedBy=default.target
```

使用以下命令控制Ollama服務：

```bash
sudo systemctl stop ollama.service
sudo systemctl disable ollama.service
sudo systemctl status ollama.service
```
