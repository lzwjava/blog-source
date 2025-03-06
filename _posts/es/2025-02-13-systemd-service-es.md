---
audio: true
generated: false
lang: es
layout: post
title: Servicio Systemd
translated: true
---

## Configuración del Servicio del Servidor LLaMA

Esta sección explica cómo configurar un servicio systemd para ejecutar el servidor LLaMA, que proporciona capacidades de inferencia local de LLM.

```bash
sudo emacs /etc/systemd/system/llama.service
sudo systemctl daemon-reload
sudo systemctl enable llama.service
journalctl -u llama.service
```

```bash
[Unit]
Description=Script de Llama

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

## Configuración del Servicio Open WebUI

Esta sección explica cómo configurar un servicio systemd para ejecutar Open WebUI, que proporciona una interfaz web para interactuar con los modelos LLM.

```bash
[Unit]
Description=Servicio de Open Web UI

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

## Configuración del Servicio Clash

Esta sección explica cómo configurar un servicio systemd para ejecutar Clash, una herramienta de proxy basada en reglas.

```bash
[Unit]
Description=Servicio de Clash

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
# Crear el archivo del servicio
sudo emacs /etc/systemd/system/clash.service

# Recargar el demonio systemd
sudo systemctl daemon-reload

# Habilitar y comenzar el servicio
sudo systemctl enable clash.service
sudo systemctl start clash.service
sudo systemctl restart clash.service

# Verificar el estado
sudo systemctl status clash.service
```