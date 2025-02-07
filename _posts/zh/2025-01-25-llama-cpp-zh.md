---
audio: false
lang: zh
layout: post
title: 尝试 llama.cpp
translated: true
---

## llama.cpp

运行`llama.cpp`加载模型时，你可能会遇到这样的错误：

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

这个错误是因为你运行的是`main`程序。运行`build/bin`目录下的`llama-cli`或`llama-server`程序应该可以解决这个问题。

`main`程序创建于2023年8月8日，这意味着它不是当前版本。

另一个解决方案是用Homebrew安装`llama.cpp`：

```bash
brew install llama.cpp
```

这可以确保你拥有兼容版本的库。

## Ollama

```bash
% ollama list
NAME                   ID              SIZE      MODIFIED
deepseek-coder:6.7b    ce298d984115    3.8 GB    14 hours ago
mistral:7b             f974a74358d6    4.1 GB    15 hours ago
```

```bash
ollama remove model
```

这是一个非常棒的工具。Ollamac中有一些bug。例如，当它从本地API接收响应时，应用程序中的几个文本框会更新。

然而，在Linux系统中，Ollama运行为系统服务。以下是服务配置文件：

`/etc/systemd/system/ollama.service`:

```bash
[Unit]
Description=Ollama Service
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

使用以下命令来控制Ollama服务：

```bash
sudo systemctl stop ollama.service
sudo systemctl disable ollama.service
sudo systemctl status ollama.service
```

## LLM Farm

这是一个很棒的iOS应用程序。在设置中，大约有20个模型。当我们自己导入从Hugging Face下载的GGUF模型时，可能会导致崩溃。

## 优势

自托管这些LLM模型允许你在本地运行它们，而无需网络访问。例如，在下载导致网络拥塞的大文件时，运行本地模型非常有用。

## 资源

*   [Hugging Face GGML 模型](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub 仓库](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub 仓库](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)
