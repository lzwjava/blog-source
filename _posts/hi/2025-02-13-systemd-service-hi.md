---
audio: true
generated: true
lang: hi
layout: post
title: सिस्टमडी सर्विस
translated: true
---

## LLaMA सर्वर सेवा संरचना

इस खंड में LLaMA सर्वर की व्यवस्था करने के लिए एक systemd सेवा कैसे सेट अप करें, जो स्थानीय LLM अनुमान क्षमता प्रदान करता है, समझाया गया है।

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

## Open WebUI सेवा संरचना

इस खंड में Open WebUI की व्यवस्था करने के लिए एक systemd सेवा कैसे सेट अप करें, जो LLM मॉडलों के साथ इंटरैक्ट करने के लिए एक वेब इंटरफेस प्रदान करता है, समझाया गया है।

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

## Clash सेवा संरचना

इस खंड में Clash, एक नियम आधारित प्रॉक्सी टूल, की व्यवस्था करने के लिए एक systemd सेवा कैसे सेट अप करें, समझाया गया है।

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
# सेवा फाइल बनाएं
sudo emacs /etc/systemd/system/clash.service

# systemd डेमन रिलोड करें
sudo systemctl daemon-reload

# सेवा को सक्षम और शुरू करें
sudo systemctl enable clash.service
sudo systemctl start clash.service
sudo systemctl restart clash.service

# स्थिति जांचें
sudo systemctl status clash.service
```