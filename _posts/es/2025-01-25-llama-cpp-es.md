---
audio: false
lang: es
layout: post
title: Probando llama.cpp
translated: true
---

## llama.cpp

Al intentar ejecutar `llama.cpp` con un modelo, podrías encontrar un error como este:

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

Este error ocurre porque estás ejecutando el programa `main`. Ejecutar los programas `llama-cli` o `llama-server` ubicados en `build/bin` debería resolver el problema.

El programa `main` fue creado el 8 de agosto de 2023, lo que significa que no es la versión actual.

Otra solución es instalar `llama.cpp` usando Homebrew:

```bash
brew install llama.cpp
```

Esto asegura que tienes una versión compatible de la librería.

## LLM Farm

Es una gran aplicación para iOS. En la configuración, hay alrededor de 20 modelos. Al importar un modelo GGUF por nosotros mismos, descargados de Hugging Face, puede provocar un fallo.

## Beneficios

Alojar estos modelos LLM permite ejecutarlos localmente sin necesidad de acceso a la red. Por ejemplo, al descargar archivos grandes que congestionan la red, ejecutar un modelo local puede ser beneficioso.

## Recursos

*   [Modelos GGML de Hugging Face](https://huggingface.co/ggml-org?sort_models=downloads#models)
*   [Repositorio de llama.cpp en GitHub](https://github.com/ggerganov/llama.cpp)
*   [Repositorio de ggml en GitHub](https://github.com/ggerganov/ggml)
*   [Ollama](https://ollama.com)
*   [Ollamac](https://github.com/kevinhermawan/Ollamac)
