---
audio: true
lang: ja
layout: post
title: llama.cppを試す
translated: true
---

## llama.cpp

`llama.cpp` を使ってモデルを実行しようとすると、次のようなエラーが発生することがあります:

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

このエラーは通常、`llama.cpp` のインストールまたはモデルファイル自体に問題があることを示しています。

一般的な解決策は、Homebrew を使って `llama.cpp` をインストールすることです:

```bash
brew install llama.cpp
```

これにより、互換性のあるバージョンのライブラリがインストールされます。

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

これは非常に便利なツールです。ただし、Ollamac にはいくつかのバグがあります。例えば、ローカル API からレスポンスを受け取ると、アプリ内の複数のテキストボックスが更新されることがあります。

## LLM Farm

これは素晴らしい iOS アプリです。設定には約20のモデルがあります。Hugging Face からダウンロードした GGUF モデルを自分でインポートすると、クラッシュすることがあります。

## 利点

これらの LLM モデルをセルフホスティングすることで、ネットワークアクセスなしでローカルで実行できます。例えば、ネットワークを混雑させる大きなファイルをダウンロードしている場合、ローカルモデルを実行することでメリットがあります。

## リソース

*   [Hugging Face GGML Models](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub リポジトリ](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub リポジトリ](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)