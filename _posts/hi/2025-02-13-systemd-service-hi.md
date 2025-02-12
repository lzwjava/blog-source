---
audio: false
lang: hi
layout: post
title: सिस्टमडी सेवा
translated: true
---

```bash
sudo emacs /etc/systemd/system/llama.service
sudo systemctl daemon-reload
sudo systemctl enable llama.service
journalctl -u llama.service
```

```bash
[Unit]
Description=Llama Script

[Service]
ExecStart=/home/lzw/Projects/llama.cpp/build/bin/llama-server -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-Distill-Llama-8B-Q4_K_M.gguf --port 8000
WorkingDirectory=/home/lzw/Projects/llama.cpp
StandardOutput=append:/home/lzw/llama.log
StandardError=append:/home/lzw/llama.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
[Unit]
Description=Open Web UI Service

[Service]
ExecStart=/home/lzw/.local/bin/open-webui serve
WorkingDirectory=/home/lzw
StandardOutput=append:/home/lzw/open-webui.log
StandardError=append:/home/lzw/open-webui.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
sudo systemctl enable openwebui.service
sudo systemctl daemon-reload
sudo systemctl start  openwebui.service
```