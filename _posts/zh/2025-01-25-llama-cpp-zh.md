---
audio: true
lang: zh
layout: post
title: 尝试使用llama.cpp
translated: true
---

## llama.cpp

尝试运行 `llama.cpp` 并使用某个模型时，你可能会遇到如下错误：

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

出现此错误是因为我正在运行 `main` 程序。运行位于 `build/bin` 目录下的 `llama-cli` 或 `llama-server` 程序应该可以解决问题。

另一个解决方案是使用 Homebrew 安装 `llama.cpp`：

```bash
brew install llama.cpp
```

这样可以确保你拥有一个兼容的库版本。

## Ollama

```bash
% ollama list
NAME                   ID              SIZE      MODIFIED
deepseek-coder:6.7b    ce298d984115    3.8 GB    14小时前
mistral:7b             f974a74358d6    4.1 GB    15小时前
```

```bash
ollama remove model
```

这是一个非常好用的工具。Ollamac 中存在一些 bug。例如，当它从本地 API 接收到响应时，应用程序中的多个文本框会更新。

## LLM Farm

这是一个非常棒的 iOS 应用。在设置中，有大约 20 个模型。当我们自己导入从 Hugging Face 下载的 GGUF 模型时，可能会导致应用崩溃。

## 优势

自托管这些 LLM 模型可以让你在本地运行它们，而无需网络访问。例如，在下载大文件导致网络拥堵时，运行本地模型会非常有益。

## 资源

*   [Hugging Face GGML 模型](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub 仓库](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub 仓库](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)