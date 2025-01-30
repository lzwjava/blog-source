---
audio: false
lang: ja
layout: post
title: ラマ.cppを試してみる
translated: true
---

## llama.cpp

`llama.cpp` をモデルと一緒に実行しようとすると、以下のようなエラーが発生することがあります：

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

このエラーは、`main` プログラムを実行しているために発生します。`build/bin` にある `llama-cli` または `llama-server` プログラムを実行すると、問題が解決するはずです。

`main` プログラムは 2023 年 8 月 8 日に作成されたため、現在のビルドではありません。

別の解決策として、Homebrew を使用して `llama.cpp` をインストールする方法があります：

```bash
brew install llama.cpp
```

これにより、互換性のあるライブラリバージョンを確保できます。

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

これは素晴らしいツールです。ただし、Ollamac にはいくつかのバグがあります。例えば、ローカル API からの応答を受信したときに、アプリ内の複数のテキストボックスが更新されます。

## LLM Farm

これは素晴らしい iOS アプリです。設定には約 20 のモデルがあります。Hugging Face からダウンロードした GGUF モデルを自分でインポートすると、クラッシュすることがあります。

## メリット

これらの LLM モデルを自分でホストすることで、ネットワークアクセスを必要とせずにローカルで実行できます。例えば、ネットワークを混雑させる大きなファイルをダウンロードする際に、ローカルモデルを実行することが有益です。

## リソース

*   [Hugging Face GGML Models](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub Repository](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub Repository](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)