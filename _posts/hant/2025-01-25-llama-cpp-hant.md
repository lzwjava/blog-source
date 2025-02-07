---
audio: false
lang: hant
layout: post
title: 嘗試 llama.cpp
translated: true
---

## llama.cpp

當嘗試使用模型運行 `llama.cpp` 時，您可能會遇到以下錯誤：

```bash
% ./main -m models/7B/Phi-3-mini-4k-instruct-q4.gguf
main: build = 964 (f3c3b4b)
main: seed  = 1737736417
llama.cpp: loading model from models/7B/Phi-3-mini-4k-instruct-q4.gguf
error loading model: unknown (magic, version) combination: 46554747, 00000003; is this really a GGML file?
llama_load_model_from_file: failed to load model
llama_init_from_gpt_params: error: failed to load model 'models/7B/Phi-3-mini-4k-instruct-q4.gguf'
main: error: unable to load model
```

此錯誤是因為您正在運行 `main` 程式。運行位於 `build/bin` 下的 `llama-cli` 或 `llama-server` 程式應能解決此問題。

`main` 程式於 2023 年 8 月 8 日創建，表示它不是最新的版本。

另一種解決方案是使用 Homebrew 安裝 `llama.cpp`：

```bash
brew install llama.cpp
```

這確保您擁有相容版本的函式庫。

## Ollama

```bash
% ollama list
名稱                   ID              大小      修改時間
deepseek-coder:6.7b    ce298d984115    3.8 GB    14 小時前
mistral:7b             f974a74358d6    4.1 GB    15 小時前
```

```bash
ollama remove model
```

它是一個非常有用的工具。Ollamac 中有一些錯誤。例如，當它從本地 API 收到響應時，應用程式中的幾個文字框會更新。

然而，在 Linux 系統中，Ollama 作為系統服務運行。以下是服務配置文件：

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

使用以下命令控制 Ollama 服務：

```bash
sudo systemctl stop ollama.service
sudo systemctl disable ollama.service
sudo systemctl status ollama.service
```

## LLM Farm

這是一個很棒的 iOS 應用程式。在設定中，大約有 20 個模型。當我們自己導入從 Hugging Face 下載的 GGUF 模型時，可能會導致崩潰。

## 優點

自行託管這些 LLM 模型允許您在本地運行它們，而無需網路訪問。例如，當下載大型文件阻塞網路時，運行本地模型會很有益。

## 資源

*   [Hugging Face GGML 模型](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub 倉庫](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub 倉庫](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)
