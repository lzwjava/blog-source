---
audio: true
lang: ar
layout: post
title: خدمة Systemd
translated: true
---

## إعداد خدمة LLaMA Server

يشرح هذا القسم كيفية إعداد خدمة systemd لتشغيل خادم LLaMA، الذي يوفر قدرات استدلال LLM المحلية.

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
ExecStart=/home/lzw/Projects/llama.cpp/build/bin/llama-server -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-Distill-Qwen-14B-Q5_K_M.gguf --port 8000  --ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1
WorkingDirectory=/home/lzw/Projects/llama.cpp
StandardOutput=append:/home/lzw/llama.log
StandardError=append:/home/lzw/llama.err
Restart=always
User=lzw

[Install]
WantedBy=default.target
```

## إعداد خدمة Open WebUI

يشرح هذا القسم كيفية إعداد خدمة systemd لتشغيل Open WebUI، التي توفر واجهة ويب للتفاعل مع نماذج LLM.

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

## إعداد خدمة Clash

يشرح هذا القسم كيفية إعداد خدمة systemd لتشغيل Clash، أداة بروكسي تعتمد على القواعد.

```bash
[Unit]
Description=Clash Service

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
# إنشاء ملف الخدمة
sudo emacs /etc/systemd/system/clash.service

# إعادة تحميل ديمون systemd
sudo systemctl daemon-reload

# تمكين وبدء الخدمة
sudo systemctl enable clash.service
sudo systemctl start clash.service
sudo systemctl restart clash.service

# التحقق من الحالة
sudo systemctl status clash.service
```