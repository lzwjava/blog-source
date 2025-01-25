---
audio: true
lang: hant
layout: post
title: 尝试使用llama.cpp
translated: true
---

## llama.cpp

當嘗試使用模型運行 `llama.cpp` 時，您可能會遇到這樣的錯誤：

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

這個錯誤的發生是因為我正在運行 `main` 程序。運行位於 `build/bin` 下的 `llama-cli` 或 `llama-server` 程序應該可以解決這個問題。

另一個解決方案是使用 Homebrew 安裝 `llama.cpp`：

```bash
brew install llama.cpp
```

這確保您擁有兼容的庫版本。

## Ollama

```bash
% ollama list
NAME                   ID              SIZE      MODIFIED
deepseek-coder:6.7b    ce298d984115    3.8 GB    14 小時前
mistral:7b             f974a74358d6    4.1 GB    15 小時前
```

```bash
ollama remove model
```

這是一個非常好用的工具。Ollamac 中有一些錯誤。例如，當它從本地 API 收到響應時，應用程序中的幾個文本框會更新。

## LLM Farm

這是一個很棒的 iOS 應用程序。在設置中，有大約 20 個模型。當我們自己導入從 Hugging Face 下載的 GGUF 模型時，可能會導致應用程序崩潰。

## 好處

自託管這些 LLM 模型可以讓您在本地運行它們，而無需網絡訪問。例如，當下載大文件導致網絡擁塞時，運行本地模型會非常有益。

## 資源

*   [Hugging Face GGML 模型](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub 倉庫](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub 倉庫](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)