---
audio: false
generated: true
lang: ja
layout: post
title: llama.cppを試す
translated: true
---

## llama.cpp

`llama.cpp`をモデルと共に実行しようとすると、このようなエラーが発生することがあります。

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

このエラーは、`main`プログラムを実行していることが原因です。`build/bin`にある`llama-cli`または`llama-server`プログラムを実行すると、問題が解決するはずです。

`main`プログラムは2023年8月8日に作成されたものであり、現在のビルドではありません。

別の解決策として、Homebrewを使用して`llama.cpp`をインストールすることもできます。

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

これは非常に便利なツールです。Ollamacにはいくつかのバグがあります。例えば、ローカルAPIからレスポンスを受け取ると、アプリのいくつかのテキストボックスが更新されます。

しかし、Linuxでは、Ollamaはシステムサービスとして実行されます。サービス設定ファイルは次のとおりです。

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

Ollamaサービスを制御するには、次のコマンドを使用します。

```bash
sudo systemctl stop ollama.service
sudo systemctl disable ollama.service
sudo systemctl status ollama.service
```

## LLM Farm

これは優れたiOSアプリです。設定には約20個のモデルがあります。Hugging FaceからダウンロードしたGGUFモデルを自分でインポートすると、クラッシュすることがあります。

## 利点

これらのLLMモデルを自己ホスティングすることで、ネットワークアクセスなしにローカルで実行できます。例えば、ネットワークを輻輳させるような大きなファイルをダウンロードする場合、ローカルモデルを実行すると有益です。

## リソース

*   [Hugging Face GGML Models](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub Repository](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub Repository](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)
