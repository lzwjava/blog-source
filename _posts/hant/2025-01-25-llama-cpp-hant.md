---
audio: false
lang: hant
layout: post
title: 嘗試 llama.cpp
translated: true
---

## llama.cpp

當嘗試使用模型運行 `llama.cpp` 時，你可能會遇到以下錯誤：

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

此錯誤是因為你正在運行 `main` 程式。運行位於 `build/bin` 目錄下的 `llama-cli` 或 `llama-server` 程式應能解決此問題。

`main` 程式於 2023 年 8 月 8 日建立，表示它不是最新版本。

另一個解決方案是使用 Homebrew 安裝 `llama.cpp`：

```bash
brew install llama.cpp
```

這確保你擁有相容版本的函式庫。

## LLM Farm

這是一個很棒的 iOS 應用程式。在設定中，大約有 20 個模型。當我們自己導入從 Hugging Face 下載的 GGUF 模型時，可能會導致程式當機。

## 優點

自行託管這些 LLM 模型允許你本地運行它們，無需網絡連接。例如，在下載大型文件導致網絡擁塞時，運行本地模型將非常有用。

## 資源

*   [Hugging Face GGML 模型](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub 程式庫](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub 程式庫](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)
