---
audio: true
generated: false
image: false
lang: ja
layout: post
title: システムDサービス
translated: true
---

## LLaMA サーバーサービスの設定

このセクションでは、LLaMA サーバーを実行するための systemd サービスの設定方法について説明します。このサービスは、ローカルの LLM 推論機能を提供します。

```bash
sudo emacs /etc/systemd/system/llama.service
sudo systemctl daemon-reload
sudo systemctl enable llama.service
journalctl -u llama.service
```

```bash
[Unit]
Description=Llama スクリプト

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

## Open WebUI サービスの設定

このセクションでは、Open WebUI を実行するための systemd サービスの設定方法について説明します。このサービスは、LLM モデルと対話するためのウェブインターフェースを提供します。

```bash
[Unit]
Description=Open Web UI サービス

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

## Clash サービスの設定

このセクションでは、Clash、ルールベースのプロキシツールを実行するための systemd サービスの設定方法について説明します。

```bash
[Unit]
Description=Clash サービス

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
# サービスファイルを作成
sudo emacs /etc/systemd/system/clash.service

# systemd デーモンを再読み込み
sudo systemctl daemon-reload

# サービスを有効化して開始
sudo systemctl enable clash.service
sudo systemctl start clash.service
sudo systemctl restart clash.service

# ステータスを確認
sudo systemctl status clash.service
```