---
audio: true
lang: zh
layout: post
title: 尝试 llama.cpp
translated: true
---

## llama.cpp

在尝试使用模型运行 `llama.cpp` 时，您可能会遇到以下错误：

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

此错误发生是因为您正在运行 `main` 程序。运行位于 `build/bin` 下的 `llama-cli` 或 `llama-server` 程序应该可以解决此问题。

`main` 程序是在 2023 年 8 月 8 日创建的，这意味着它不是当前的构建版本。

另一个解决方案是使用 Homebrew 安装 `llama.cpp`：

```bash
brew install llama.cpp
```

这可以确保您拥有兼容的库版本。

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

它是一个很好的工具。Ollamac 中有一些 bugs。例如，当它从本地 API 接收到响应时，应用程序中的几个文本框会更新。

## LLM Farm

这是一款很棒的 iOS 应用程序。在设置中，有大约 20 个模型。当我们自己导入从 Hugging Face 下载的 GGUF 模型时，可能会导致崩溃。

## 优势

自托管这些 LLM 模型可以让您在不需要网络访问的情况下本地运行它们。例如，当下载大文件时网络拥堵时，运行本地模型会很有帮助。

## 资源

*   [Hugging Face GGML Models](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub Repository](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub Repository](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)