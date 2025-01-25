---
audio: true
lang: en
layout: post
title: Trying llama.cpp
---

## llama.cpp

When attempting to run `llama.cpp` with a model, you might encounter an error like this:

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

This error typically indicates an issue with the `llama.cpp` installation or the model file itself.

A common solution is to install `llama.cpp` using Homebrew:

```bash
brew install llama.cpp
```

This ensures you have a compatible version of the library.

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

It's a great tool to use. There are some bugs in Ollamac. For example, when it receives a response from the local API, several text boxes in the app update.

## LLM Farm

It's a great iOS app. In the settings, there are around 20 models. When importing a GGUF model by ourselves, which are downloaded from Hugging Face, it may lead to a crash.

## Benefits

Self-hosting these LLM models allows you to run them locally without needing network access. For example, when downloading large files that congest the network, running a local model can be beneficial.

## Resources

*   [Hugging Face GGML Models](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [llama.cpp GitHub Repository](https://github.com/ggerganov/llama.cpp)
*   [ggml GitHub Repository](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)