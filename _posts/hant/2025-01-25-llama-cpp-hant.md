---
audio: false
lang: hant
layout: post
title: 嘗試 llama.cpp
translated: true
---

## llama.cpp

當嘗試使用模型運行 `llama.cpp` 時，你可能會遇到類似以下的錯誤：

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

這個錯誤是因為你正在運行 `main` 程序。運行位於 `build/bin` 下的 `llama-cli` 或 `llama-server` 程序應該可以解決這個問題。

`main` 程序是於 2023 年 8 月 8 日創建的，這意味著它不是最新的構建。

另一個解決方案是使用 Homebrew 安裝 `llama.cpp`：

```bash
brew install llama.cpp
```

這樣可以確保你擁有兼容的庫版本。

## 服務模型

```bash
/home/lzw/Projects/llama.cpp/build/bin/llama-server -m /home/lzw/Projects/llama.cpp/models/DeepSeek-R1-Distill-Qwen-14B-Q5_K_M.gguf --port 8000  --ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1
```

參數 `--ctx-size 2048 --batch-size 512 --n-gpu-layers 49 --threads 8 --parallel 1` 非常重要。它們會提高速度。

## LLM Farm

這是一個非常棒的 iOS 應用程序。在設置中，有約 20 個模型。當我們自己導入從 Hugging Face 下載的 GGUF 模型時，可能會導致崩潰。

## 好處

自行托管這些 LLM 模型可以讓你在本地運行它們，而不需要網絡訪問。例如，當下載大文件時網絡擁堵，運行本地模型會有幫助。

## 資源

*   [Hugging Face GGML Models](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub Repository](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub Repository](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)