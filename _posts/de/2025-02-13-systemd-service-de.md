---
audio: true
lang: de
layout: post
title: Systemd-Dienst
translated: true
---

## LLaMA-Server-Dienstkonfiguration

Dieser Abschnitt erklärt, wie man einen systemd-Dienst zum Ausführen des LLaMA-Servers einrichtet, der lokale LLM-Inferenzfähigkeiten bietet.

```bash
sudo emacs /etc/systemd/system/llama.service
sudo systemctl daemon-reload
sudo systemctl enable llama.service
journalctl -u llama.service
```

```bash
[Unit]
Description=Llama-Skript

[Service]
ExecStart=/home/lzw/Projects/llama.cpp/build/bin/llama-server -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-Distill-Qwen-14B-Q5_K_M.gguf --port 8000  --ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1
WorkingDirectory=/home/lzw/Projects/llama.cpp
StandardOutput=append:/home/lzw/llama.log
StandardError=append:/home/lzw/llama.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

## Open WebUI-Dienstkonfiguration

Dieser Abschnitt erklärt, wie man einen systemd-Dienst zum Ausführen von Open WebUI einrichtet, der eine Web-Oberfläche zum Interagieren mit LLM-Modellen bietet.

```bash
[Unit]
Description=Open Web UI Dienst

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

## Clash-Dienstkonfiguration

Dieser Abschnitt erklärt, wie man einen systemd-Dienst zum Ausführen von Clash, einem regelbasierten Proxy-Tool, einrichtet.

```bash
[Unit]
Description=Clash-Dienst

[Service]
ExecStart=/home/lzw/clash-linux-386-v1.17.0/clash-linux-386
WorkingDirectory=/home/lzw/clash-linux-386-v1.17.0
StandardOutput=append:/home/lzw/clash.log
StandardError=append:/home/lzw/clash.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

```bash
# Erstellen der Dienstdatei
sudo emacs /etc/systemd/system/clash.service

# Neu laden des systemd-Daemons
sudo systemctl daemon-reload

# Dienst aktivieren und starten
sudo systemctl enable clash.service
sudo systemctl start clash.service
sudo systemctl restart clash.service

# Status überprüfen
sudo systemctl status clash.service
```