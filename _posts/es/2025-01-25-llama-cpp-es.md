---
audio: true
lang: es
layout: post
title: Probando llama.cpp
translated: true
---

## llama.cpp

Al intentar ejecutar `llama.cpp` con un modelo, podrías encontrarte con un error como este:

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

Este error ocurre porque estoy ejecutando el programa `main`. Ejecutar los programas `llama-cli` o `llama-server` ubicados en `build/bin` debería resolver el problema.

Otra solución es instalar `llama.cpp` usando Homebrew:

```bash
brew install llama.cpp
```

Esto asegura que tengas una versión compatible de la biblioteca.

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

Es una gran herramienta para usar. Hay algunos errores en Ollamac. Por ejemplo, cuando recibe una respuesta de la API local, varias cajas de texto en la aplicación se actualizan.

## LLM Farm

Es una gran aplicación para iOS. En los ajustes, hay alrededor de 20 modelos. Cuando importamos un modelo GGUF por nuestra cuenta, que se descargan de Hugging Face, puede causar un cierre inesperado de la aplicación.

## Beneficios

Alojar estos modelos LLM por tu cuenta te permite ejecutarlos localmente sin necesidad de acceso a la red. Por ejemplo, cuando descargas archivos grandes que congestionan la red, ejecutar un modelo local puede ser beneficioso.

## Recursos

*   [Modelos GGML en Hugging Face](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [Repositorio de GitHub de llama.cpp](https://github.com/ggerganov/llama.cpp)
*   [Repositorio de GitHub de ggml](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)