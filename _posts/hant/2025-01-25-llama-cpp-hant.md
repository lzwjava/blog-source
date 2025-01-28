---
audio: true
lang: hant
layout: post
title: 嘗試 llama.cpp
translated: true
---

## llama.cpp

當嘗試使用模型運行 `llama.cpp` 時，可能會遇到以下錯誤：

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

此錯誤是因為你正在運行 `main` 程序。運行位於 `build/bin` 下的 `llama-cli` 或 `llama-server` 程序應該可以解決這個問題。

`main` 程序是於 2023 年 8 月 8 日創建的，這意味著它不是當前版本。

另一個解決方案是使用 Homebrew 安裝 `llama.cpp`：

```bash
brew install llama.cpp
```

這將確保你擁有兼容的庫版本。

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

這是一個很好的工具。Ollamac 中有一些 bug。例如，當它從本地 API 接收到響應時，應用程序中的幾個文本框會更新。

## LLM Farm

這是一個很好的 iOS 應用程序。在設置中，有大約 20 個模型。當我們自行導入從 Hugging Face 下載的 GGUF 模型時，可能會導致崩潰。

## 優點

自行託管這些 LLM 模型允許你在本地運行它們，而無需網絡訪問。例如，當下載大文件時會堵塞網絡，這時運行本地模型會很有用。

## 資源

*   [Hugging Face GGML Models](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub Repository](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub Repository](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)