---
audio: true
generated: true
lang: fr
layout: post
title: Service systemd
translated: true
---

## Configuration du service LLaMA Server

Cette section explique comment configurer un service systemd pour exécuter le serveur LLaMA, qui fournit des capacités d'inférence LLM locales.

```bash
sudo emacs /etc/systemd/system/llama.service
sudo systemctl daemon-reload
sudo systemctl enable llama.service
journalctl -u llama.service
```

```bash
[Unit]
Description=Script Llama

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

## Configuration du service Open WebUI

Cette section explique comment configurer un service systemd pour exécuter Open WebUI, qui fournit une interface web pour interagir avec les modèles LLM.

```bash
[Unit]
Description=Service Open Web UI

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

## Configuration du service Clash

Cette section explique comment configurer un service systemd pour exécuter Clash, un outil proxy basé sur des règles.

```bash
[Unit]
Description=Service Clash

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
# Créer le fichier de service
sudo emacs /etc/systemd/system/clash.service

# Recharger le démon systemd
sudo systemctl daemon-reload

# Activer et démarrer le service
sudo systemctl enable clash.service
sudo systemctl start clash.service
sudo systemctl restart clash.service

# Vérifier l'état
sudo systemctl status clash.service
```